#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用SWIFT PtEngine进行推理测试
"""

import os
import json
import sys
import argparse
from tqdm import tqdm

from swift.llm import (
    PtEngine, RequestConfig, get_model_tokenizer, get_template, InferRequest
)
from swift.tuners import Swift

def test_checkpoint_with_engine(base_model_path, checkpoint_path, test_file, output_file, num_samples=20, gpu_id="0"):
    """
    使用PtEngine测试checkpoint
    """
    # 设置GPU
    os.environ['CUDA_VISIBLE_DEVICES'] = gpu_id
    
    print(f"GPU设备: {gpu_id}")
    print(f"基础模型: {base_model_path}")
    print(f"Checkpoint: {checkpoint_path}")
    print(f"测试文件: {test_file}")
    print(f"输出文件: {output_file}")
    print(f"测试样本数: {num_samples}")
    print("-" * 80)
    
    # 模型配置
    model_path = base_model_path  # 基础模型路径
    lora_checkpoint = checkpoint_path  # checkpoint目录
    template_type = None  # None: 使用对应模型默认的template_type
    default_system = None  # None: 使用对应模型默认的default_system

    try:
        # 加载模型和对话模板
        print("1. 加载基础模型...")
        model, tokenizer = get_model_tokenizer(model_path)
        
        print("2. 加载LoRA适配器...")
        model = Swift.from_pretrained(model, lora_checkpoint)
        
        print("3. 设置对话模板...")
        template_type = template_type or model.model_meta.template
        template = get_template(template_type, tokenizer, default_system=default_system)
        
        print("4. 创建推理引擎...")
        engine = PtEngine.from_model_template(model, template, max_batch_size=1)
        request_config = RequestConfig(max_tokens=256, temperature=0.1)
        
        print("5. 模型加载完成！")
        
    except Exception as e:
        print(f"模型加载失败: {e}")
        import traceback
        traceback.print_exc()
        return
    
    # 读取测试数据
    with open(test_file, 'r', encoding='utf-8') as f:
        test_data = [json.loads(line.strip()) for line in f if line.strip()]
    
    print(f"开始测试，共 {len(test_data)} 个样本，测试前 {num_samples} 个")
    
    results = []
    prompt = "请将语音转录成文本，并标出其中出现的所有声音事件"
    
    for i, data in enumerate(tqdm(test_data[:num_samples])):
        try:
            audio_path = data["audio"]
            ground_truth = data["txt"]
            
            # 检查音频文件是否存在
            if not os.path.exists(audio_path):
                print(f"音频文件不存在: {audio_path}")
                continue
            
            # 构建推理请求
            infer_request = InferRequest(
                messages=[{
                    'role': 'user', 
                    'content': f'<audio>{prompt}'
                }],
                audios=[audio_path]  # 音频文件路径
            )
            
            # 执行推理
            try:
                resp_list = engine.infer([infer_request], request_config)
                prediction = resp_list[0].choices[0].message.content
            except Exception as e:
                prediction = f"推理错误: {str(e)}"
            
            result = {
                "audio_path": audio_path,
                "ground_truth": ground_truth,
                "prediction": prediction,
                "speaker": data.get("speaker", ""),
                "filename": data.get("filename", "")
            }
            
            results.append(result)
            
            # 每5个样本输出一次进度
            if (i + 1) % 5 == 0:
                print(f"\n样本 {i+1}:")
                print(f"音频: {os.path.basename(audio_path)}")
                print(f"真实标签: {ground_truth}")
                print(f"模型预测: {prediction}")
                print("-" * 80)
                
        except Exception as e:
            print(f"处理样本 {i+1} 时出错: {e}")
            continue
    
    # 保存结果
    with open(output_file, 'w', encoding='utf-8') as f:
        for result in results:
            f.write(json.dumps(result, ensure_ascii=False) + '\n')
    
    print(f"\n测试完成！")
    print(f"测试样本数: {num_samples}")
    print(f"成功处理: {len(results)}")
    print(f"结果保存至: {output_file}")
    
    # 计算简单的准确率指标
    if results:
        exact_matches = sum(1 for r in results if r["ground_truth"].strip() == r["prediction"].strip())
        print(f"完全匹配率: {exact_matches}/{len(results)} ({exact_matches/len(results)*100:.1f}%)")

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='测试微调模型推理')
    parser.add_argument('--base_model', required=True, help='基础模型路径')
    parser.add_argument('--checkpoint', required=True, help='LoRA checkpoint路径')
    parser.add_argument('--test_file', default="/inspire/ssd/project/embodied-multimodality/public/yangchen/asr_nv/dataset/test.jsonl", help='测试数据文件')
    parser.add_argument('--output_file', required=True, help='输出结果文件')
    parser.add_argument('--num_samples', type=int, default=20, help='测试样本数量')
    parser.add_argument('--gpu_id', default="0", help='GPU设备ID')
    
    args = parser.parse_args()
    
    # 检查基础模型路径（如果是本地路径才检查）
    # 判断是否为模型 ID（格式如 organization/model-name）
    is_model_id = (
        '/' in args.base_model and 
        not args.base_model.startswith(('./', '../', '/')) and 
        len(args.base_model.split('/')) == 2
    )
    
    if is_model_id:
        print(f"检测到模型 ID: {args.base_model}")
        print(f"将尝试从 ModelScope/HuggingFace 下载...")
    else:
        # 本地路径，需要检查是否存在
        if not os.path.exists(args.base_model):
            print(f"错误: 基础模型路径不存在: {args.base_model}")
            return
        
    if not os.path.exists(args.checkpoint):
        print(f"错误: Checkpoint路径不存在: {args.checkpoint}")
        return
        
    if not os.path.exists(args.test_file):
        print(f"错误: 测试文件不存在: {args.test_file}")
        return
    
    # 创建输出目录
    output_dir = os.path.dirname(args.output_file)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    print("=" * 80)
    print("开始推理测试")
    print("=" * 80)
    
    # 执行测试
    test_checkpoint_with_engine(
        args.base_model,
        args.checkpoint,
        args.test_file,
        args.output_file,
        args.num_samples,
        args.gpu_id
    )

if __name__ == "__main__":
    main() 