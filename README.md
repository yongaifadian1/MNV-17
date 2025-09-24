# MNV-17 Qwen2.5-Omni Demo: Nonverbal Vocalization Recognition

**中文副语言识别演示 | Nonverbal Vocalization Recognition Demo**

本仓库展示了在 [MNV-17 数据集](https://huggingface.co/datasets/maimai11/MNV_17) 上微调的 Qwen2.5-Omni 模型在非语言发声（NV）ASR识别任务上的卓越表现。

This repository demonstrates the excellent performance of Qwen2.5-Omni model fine-tuned on the [MNV-17 dataset](https://huggingface.co/datasets/maimai11/MNV_17) for Nonverbal Vocalization (NV) ASR recognition tasks.

## 🎵 在线演示 | Online Demo

**[点击这里体验可播放的音频演示 | Click here for interactive audio demo](https://yongaifadian1.github.io/MNV-17-Demo/)**

## 关键发现 | Key Findings

### 未见说话人泛化能力 | Unseen Speaker Generalization
- **重要说明**: 所有演示音频均来自测试集说话人（speaker_F_02, speaker_F_03, speaker_M_02, speaker_M_03），这些说话人在训练过程中完全未见
- **Crucial Note**: All demo audio samples are from test set speakers (speaker_F_02, speaker_F_03, speaker_M_02, speaker_M_03), who were completely unseen during training

这证明了模型学会了**通用的NV发声规律**，而非仅仅拟合特定说话人的发声习惯，展现了优秀的跨说话人泛化能力。

This demonstrates that the model learned **universal NV vocalization patterns** rather than merely fitting specific speakers' habits, showcasing excellent cross-speaker generalization.

## 模型性能 | Model Performance

根据我们的[论文](https://arxiv.org/abs/2509.18196)实验结果：

According to our [paper](https://arxiv.org/abs/2509.18196) experimental results:

| 模型 Model | 联合CER | NV识别准确率 | 
|------------|---------|-------------|
| **Qwen2.5-Omni** | **3.60%** | **57.29%** |
| Qwen2-Audio | 4.84% | 56.28% |
| SenseVoice | 8.71% | 57.29% |
| Paraformer | 5.70% | 28.64% |

### 性能亮点 | Performance Highlights

1. **最低联合错误率**: Qwen2.5-Omni 实现了 3.60% 的联合字符错误率，在 ASR 和 NV 识别双重任务中表现最佳
2. **卓越NV识别**: 在严格的完全匹配评估下达到 57.29% 准确率（类型、数量、顺序完全匹配）

1. **Lowest Joint Error Rate**: Qwen2.5-Omni achieved 3.60% joint CER, best performance in dual ASR and NV recognition tasks
2. **Excellent NV Recognition**: 57.29% accuracy under strict exact-match evaluation (type, count, order must all match)

## 数据集特点 | Dataset Characteristics

### MNV-17 数据集优势 | MNV-17 Dataset Advantages

1. **表演式录制**: 避免了自然语音中NV的模糊性，确保高质量标注
2. **类别平衡**: 17个NV类别分布均衡（最大最小比例仅2.7）
3. **说话人多样性**: 49名来自不同地区的中文母语者
4. **语境丰富**: NV自然嵌入在语义丰富的句子中

1. **Performative Recording**: Avoids ambiguity of NVs in spontaneous speech, ensures high-quality annotation
2. **Class Balance**: 17 NV categories with balanced distribution (max/min ratio only 2.7)
3. **Speaker Diversity**: 49 native Mandarin speakers from various regions  
4. **Rich Context**: NVs naturally embedded in semantically rich sentences

### 设计创新 | Design Innovation

- **脚本化方法**: 使用LLM生成自然语境，确保NV的语义合理性
- **多NV组合**: 支持1-3个NV的随机组合，模拟真实场景
- **说话人独立划分**: 严格的训练/验证/测试集划分，确保泛化评估

- **Scripted Approach**: LLM-generated natural contexts ensure semantic reasonableness of NVs
- **Multi-NV Combinations**: Supports random combinations of 1-3 NVs, simulating real scenarios
- **Speaker-Independent Split**: Strict train/validation/test division ensures generalization evaluation

良好的数据集设计和实践是使其能够在时长有限的样本中训练出泛化性强的NV ASR模型的关键原因之一。

The well-designed dataset and practices are one of the key reasons why it can train generalized NV ASR models with strong generalization from limited-duration samples.

## 相关链接 | Related Links

- 论文: [MNV-17: A High-Quality Performative Mandarin Dataset for Nonverbal Vocalization Recognition in Speech](https://arxiv.org/abs/2509.18196)
- 数据集: [maimai11/MNV_17](https://huggingface.co/datasets/maimai11/MNV_17)
- 微调模型: [即将发布 | Coming Soon]

## 引用 | Citation

如果您使用了本数据集或相关工作，请引用：

If you use this dataset or related work, please cite:

```bibtex
@misc{mai2025mnv17highqualityperformativemandarin,
      title={MNV-17: A High-Quality Performative Mandarin Dataset for Nonverbal Vocalization Recognition in Speech}, 
      author={Jialong Mai and Jinxin Ji and Xiaofen Xing and Chen Yang and Weidong Chen and Jingyuan Xing and Xiangmin Xu},
      year={2025},
      eprint={2509.18196},
      archivePrefix={arXiv},
      primaryClass={cs.SD},
      url={https://arxiv.org/abs/2509.18196}
}
```

## 主要贡献 | Key Contributions

1. **高质量数据集**: MNV-17提供了目前类别最全面的中文副语言发声数据集
2. **泛化能力验证**: 证明了基于表演式数据的模型具有优秀的跨说话人泛化能力
3. **协同效应**: 证明NV识别能力在多任务训练下的语音模型中不会损害ASR性能
4. **基准建立**: 为NV感知ASR建立了标准评估基准

1. **High-Quality Dataset**: MNV-17 provides the most comprehensive Chinese nonverbal vocalization dataset
2. **Generalization Verification**: Proves excellent cross-speaker generalization of performative data-based models
3. **Synergy Discovery**: Proves NV recognition can enhance rather than harm ASR performance
4. **Benchmark Establishment**: Establishes standard evaluation benchmark for NV-aware ASR

---

**作者 | Authors**: Jialong Mai, Jinxin Ji, Xiaofen Xing, Chen Yang, Weidong Chen, Jingyuan Xing, Xiangmin Xu

**机构 | Institutions**: 华南理工大学, 香港理工大学, 同济大学, 上海交通大学, 香港中文大学, 佛山大学