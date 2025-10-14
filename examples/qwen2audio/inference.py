#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用Qwen2-Audio模型加载LoRA进行推理测试
基于transformers和peft库
"""

import os
import json
import argparse
from tqdm import tqdm
import torch
import librosa
from transformers import Qwen2AudioForConditionalGeneration, AutoProcessor
from peft import PeftModel

def load_model_and_processor(base_model_path, lora_path):
    """加载基础模型、处理器和LoRA适配器"""
    
    print("1. 加载处理器...")
    processor = AutoProcessor.from_pretrained(base_model_path)
    
    print("2. 加载基础模型...")
    model = Qwen2AudioForConditionalGeneration.from_pretrained(
        base_model_path, 
        device_map={"": "cuda:0"},  # 固定使用GPU 0
        torch_dtype=torch.float16
    )
    
    print("3. 加载LoRA适配器...")
    model = PeftModel.from_pretrained(model, lora_path)
    
    print("4. 合并LoRA权重...")
    model = model.merge_and_unload()
    
    print("5. 确保模型在正确的设备上...")
    if torch.cuda.is_available():
        # 由于使用了device_map={"": "cuda:0"}，模型应该已经在cuda:0上
        print(f"   模型设备: {next(model.parameters()).device}")
    else:
        print("   CUDA不可用，使用CPU设备")
    
    print("6. 模型加载完成！")
    return model, processor

def create_conversation(prompt):
    """创建对话格式"""
    conversation = [
        {'role': 'system', 'content': 'You are a helpful assistant.'}, 
        {"role": "user", "content": [
            {"type": "audio", "audio_url": "placeholder"},  # 这个会被替换
            {"type": "text", "text": prompt},
        ]},
    ]
    return conversation

def inference_single_audio(model, processor, audio_path, prompt):
    """对单个音频文件进行推理"""
    
    try:
        # 创建对话
        conversation = create_conversation(prompt)
        
        # 应用聊天模板
        text = processor.apply_chat_template(conversation, add_generation_prompt=True, tokenize=False)
        
        # 加载音频
        audio, _ = librosa.load(
            audio_path, 
            sr=processor.feature_extractor.sampling_rate
        )
        audios = [audio]
        
        # 处理输入 - Qwen2-Audio使用audio参数而不是audios
        inputs = processor(text=text, audio=audios, return_tensors="pt", padding=True)
        
        # 确保所有输入张量都在cuda:0上
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        print(f"   目标设备: {device}")
        
        inputs = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in inputs.items()}
        
        # 验证输入张量设备
        for k, v in inputs.items():
            if isinstance(v, torch.Tensor):
                print(f"   输入 {k} 设备: {v.device}")
        
        # 生成响应
        with torch.no_grad():
            generate_ids = model.generate(
                **inputs, 
                max_new_tokens=512,
                do_sample=False,
                temperature=0.1
            )
        
        # 解码响应
        input_length = inputs['input_ids'].size(1)
        generate_ids = generate_ids[:, input_length:]
        response = processor.batch_decode(
            generate_ids, 
            skip_special_tokens=True, 
            clean_up_tokenization_spaces=False
        )[0]
        
        return response.strip()
        
    except Exception as e:
        return f"推理错误: {str(e)}"

def batch_inference(base_model_path, lora_path, test_file, output_file, num_samples=None, gpu_id="0"):
    """批量推理"""
    
    # 设置GPU
    os.environ['CUDA_VISIBLE_DEVICES'] = gpu_id
    
    print("=" * 80)
    print("Qwen2-Audio LoRA 批量推理")
    print("=" * 80)
    print(f"GPU设备: {gpu_id}")
    print(f"基础模型: {base_model_path}")
    print(f"LoRA路径: {lora_path}")
    print(f"测试文件: {test_file}")
    print(f"输出文件: {output_file}")
    print("-" * 80)
    
    # 检查基础模型路径（如果是本地路径才检查）
    # 判断是否为模型ID（格式如 organization/model-name）
    is_model_id = (
        '/' in base_model_path and 
        not base_model_path.startswith(('./', '../', '/')) and 
        len(base_model_path.split('/')) == 2
    )
    
    if is_model_id:
        print(f"检测到模型ID: {base_model_path}")
        print(f"将尝试从 ModelScope/HuggingFace 下载...")
    else:
        # 本地路径，需要检查是否存在
        if not os.path.exists(base_model_path):
            print(f"错误: 基础模型路径不存在: {base_model_path}")
            return
        
    if not os.path.exists(lora_path):
        print(f"错误: LoRA路径不存在: {lora_path}")
        return
        
    if not os.path.exists(test_file):
        print(f"错误: 测试文件不存在: {test_file}")
        return
    
    # 加载模型
    try:
        model, processor = load_model_and_processor(base_model_path, lora_path)
    except Exception as e:
        print(f"模型加载失败: {e}")
        return
    
    # 读取测试数据
    print("正在读取测试数据...")
    with open(test_file, 'r', encoding='utf-8') as f:
        test_data = [json.loads(line.strip()) for line in f if line.strip()]
    
    # 限制样本数量
    if num_samples:
        test_data = test_data[:num_samples]
    
    print(f"总共 {len(test_data)} 个样本需要处理")
    print("-" * 80)
    
    results = []
    success_count = 0
    error_count = 0
    prompt = "请将语音转录成文本，并标出其中出现的所有声音事件"
    
    for i, data in enumerate(tqdm(test_data, desc="推理进度")):
        try:
            audio_path = data["audio"]
            ground_truth = data["txt"]
            
            # 检查音频文件是否存在
            if not os.path.exists(audio_path):
                print(f"\n警告: 音频文件不存在: {audio_path}")
                error_count += 1
                continue
            
            # 执行推理
            prediction = inference_single_audio(model, processor, audio_path, prompt)
            
            result = {
                "audio_path": audio_path,
                "ground_truth": ground_truth,
                "prediction": prediction,
                "speaker": data.get("speaker", ""),
                "filename": data.get("filename", "")
            }
            
            results.append(result)
            success_count += 1
            
            # 每5个样本输出一次进度
            if (i + 1) % 5 == 0:
                print(f"\n样本 {i+1}:")
                print(f"音频: {os.path.basename(audio_path)}")
                print(f"真实标签: {ground_truth}")
                print(f"模型预测: {prediction}")
                print("-" * 80)
                
        except Exception as e:
            print(f"\n处理样本 {i+1} 时出错: {e}")
            error_count += 1
            continue
    
    # 保存结果
    print(f"\n正在保存结果到: {output_file}")
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        for result in results:
            f.write(json.dumps(result, ensure_ascii=False) + '\n')
    
    # 统计信息
    print("\n" + "=" * 80)
    print("批量推理完成！")
    print("=" * 80)
    print(f"总样本数: {len(test_data)}")
    print(f"成功处理: {success_count}")
    print(f"处理出错: {error_count}")
    print(f"结果保存至: {output_file}")
    
    # 计算简单的准确率指标
    if results:
        exact_matches = sum(1 for r in results if r["ground_truth"].strip() == r["prediction"].strip())
        print(f"完全匹配率: {exact_matches}/{len(results)} ({exact_matches/len(results)*100:.1f}%)")
    
    print("=" * 80)

def test_single_audio(base_model_path, lora_path, audio_path, prompt=None, gpu_id="0"):
    """测试单个音频文件"""
    
    # 设置GPU
    os.environ['CUDA_VISIBLE_DEVICES'] = gpu_id
    
    if prompt is None:
        prompt = "请将语音转录成文本，并标出其中出现的所有声音事件"
    
    print("=" * 80)
    print("单个音频推理测试")
    print("=" * 80)
    print(f"基础模型: {base_model_path}")
    print(f"LoRA路径: {lora_path}")
    print(f"音频文件: {audio_path}")
    print(f"提示词: {prompt}")
    print("-" * 80)
    
    # 检查文件
    if not os.path.exists(audio_path):
        print(f"错误: 音频文件不存在: {audio_path}")
        return
    
    # 加载模型
    try:
        model, processor = load_model_and_processor(base_model_path, lora_path)
    except Exception as e:
        print(f"模型加载失败: {e}")
        return
    
    # 执行推理
    print("正在推理...")
    prediction = inference_single_audio(model, processor, audio_path, prompt)
    
    print("\n推理结果:")
    print("-" * 40)
    print(prediction)
    print("-" * 40)

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='Qwen2-Audio LoRA推理')
    parser.add_argument('--base_model', required=True, help='基础模型路径')
    parser.add_argument('--lora_path', required=True, help='LoRA适配器路径')
    parser.add_argument('--mode', choices=['batch', 'single'], default='batch', help='推理模式')
    
    # 批量推理参数
    parser.add_argument('--test_file', 
                       help='测试数据文件')
    parser.add_argument('--output_file', 
                       help='输出结果文件')
    parser.add_argument('--num_samples', type=int, default=None, help='限制处理的样本数量')
    
    # 单个推理参数
    parser.add_argument('--audio_path', help='单个音频文件路径')
    parser.add_argument('--prompt', help='推理提示词')
    
    parser.add_argument('--gpu_id', default="0", help='GPU设备ID')
    
    args = parser.parse_args()
    
    if args.mode == 'batch':
        batch_inference(
            args.base_model,
            args.lora_path,
            args.test_file,
            args.output_file,
            args.num_samples,
            args.gpu_id
        )
    elif args.mode == 'single':
        if not args.audio_path:
            print("错误: 单个推理模式需要指定 --audio_path")
            return
        test_single_audio(
            args.base_model,
            args.lora_path,
            args.audio_path,
            args.prompt,
            args.gpu_id
        )

if __name__ == "__main__":
    main()
