#!/bin/bash
# Qwen2-Audio LoRA 批量推理脚本
export CUDA_VISIBLE_DEVICES=0

python ./inference.py \
    --base_model Qwen/Qwen2-Audio-7B-Instruct \
    --lora_path ../../ckpt/qwen2-audio-7b-instruct-finetuned_no_oral/v0-20250916-113845/checkpoint-384\
    --mode batch \
    --test_file ./testset/test.jsonl \
    --output_file ./results/qwen2_audio_results.jsonl \
    --num_samples  5\
    --gpu_id 0
