#!/bin/bash
# Qwen2.5-Omni 推理脚本

python ./inference.py \
    --base_model "Qwen/Qwen2.5-Omni-7B" \
    --checkpoint "../../ckpt/qwen25-omni-7b-finetuned/v0-20250914-150113/checkpoint-192" \
    --test_file "../testset/test.jsonl" \
    --output_file "results/qwen25omni_results.jsonl" \
    --num_samples 5 \
    --gpu_id "0"
