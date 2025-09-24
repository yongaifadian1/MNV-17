# MNV-17 Qwen2.5-Omni Demo

[**中文版本**](#中文版本) | [**English Version**](#english-version)

---

## 中文版本

### MNV-17 Qwen2.5-Omni 演示：非语言发声识别

本仓库展示了在 [MNV-17 数据集](https://huggingface.co/datasets/maimai11/MNV_17) 上微调的 Qwen2.5-Omni 模型在非语言发声（NV）ASR识别任务上的卓越表现。

**[点击这里体验可播放的音频演示](https://yongaifadian1.github.io/MNV-17/)**

### 关键发现

#### 未见说话人泛化能力

**重要说明**: 所有演示样本的说话人在训练过程中完全未见。

这证明了模型学会了**通用的NV发声规律**，而非仅仅拟合特定说话人的发声习惯，展现了优秀的跨说话人泛化能力。

### 模型性能

根据我们的[论文](https://arxiv.org/abs/2509.18196)实验结果：

| 模型 Model | 联合CER | NV识别准确率 |
|------------|---------|-------------|
| **Qwen2.5-Omni** | **3.60%** | **57.29%** |
| Qwen2-Audio | 4.84% | 56.28% |
| SenseVoice | 8.71% | 57.29% |
| Paraformer | 5.70% | 28.64% |

#### 性能亮点

1. **最低联合错误率**: Qwen2.5-Omni 实现了 3.60% 的联合字符错误率，在 ASR 和 NV 识别双重任务中表现最佳。
2. **卓越NV识别**: 在严格的完全匹配评估下达到 57.29% 准确率（类型、数量、顺序完全匹配）。

### 演示样本

以下展示了在MNV-17上指令微调的Qwen2.5-Omni模型在演示样本上的预测结果：

#### 样本 1
- **模型预测**: 这个理论的悖论之处在于 [cough] 请大家原谅，在于它的前提本身——哎呀这粉笔灰真是 [sneeze]——它的前提本身就包含了结论，这听起来是不是很 [chuckle] 荒谬。

#### 样本 2
- **模型预测**: 我给自己泡了杯热茶 [hum]，又从冰箱里拿出那块昨天没舍得吃的提拉米苏 [smack]，然后窝在沙发里刷着搞笑视频 [laugh]，这大概就是最简单的幸福吧。

#### 样本 3
- **模型预测**: 他开着那辆新买的跑车 [whistle] 从我身边呼啸而过，故意在我面前停下 [cough] 做出一个自以为很帅的姿势，我当场 [clap] 就给他鼓了鼓掌，要多敷衍有多敷衍。

#### 样本 4
- **模型预测**: 晚饭时场面一度非常热闹，我家的猫[hiss]不让新来的客人靠近，小侄女表演完节目后大家[applaud]热情鼓掌，而对胡椒粉过敏的爷爷则[sneeze]打起了喷嚏。

#### 样本 5
- **模型预测**: 我一走进那个积满灰尘的阁楼 [sneeze] 就忍不住打了个大喷嚏，面对着堆积如山的杂物 [sigh] 真不知从何下手，但当我从旧箱子里翻出那张绝版黑胶唱片时，我简直想为自己的好运 [clap] 欢呼！

#### 样本 6
- **模型预测**: 老教授讲到他年轻时的糗事，全班 [laugh] 都笑得前仰后合，可他一提到这周末的作业 [moan] 我的头就开始疼了，而且这教室的灰尘也太多了 [sneeze]，真是让人受不了。

#### 样本 7
- **模型预测**: 看着电影里主角牺牲的画面，影院里一片 [sniffle] 的啜泣声，我却在内心为他的壮举 [applaud] 喝彩，然后长叹一口气 [hum]，思考着人性的复杂。

#### 样本 8
- **模型预测**: 回想起那些独自奋斗的夜晚 [sigh]，真不知道是怎么熬过来的，但当我昨天终于攻克那个难题时 [clap]，我知道所有的付出都值得了，最终项目成功发布那一刻 [applaud]，我感受到了前所未有的成就感。

#### 样本 9
- **模型预测**: 他最终 [exhale] 放下了手中的旧照片，心想我们 [sigh] 终究还是走到了这一步，一念及此，又想起她最后那些话 [hiss]，真是刻薄又伤人。

### 数据集特点

#### MNV-17 数据集优势

1. **表演式录制**: 避免了自然语音中NV的模糊性，确保高质量标注。
2. **类别平衡**: 17个NV类别分布均衡（最大最小比例仅2.7）。
3. **说话人多样性**: 49名来自不同地区的中文母语者。
4. **语境丰富**: NV自然嵌入在语义丰富的句子中。

#### 设计创新

- **脚本化方法**: 使用LLM生成自然语境，确保NV的语义合理性。
- **多NV组合**: 支持1-3个NV的随机组合，模拟真实场景。
- **说话人独立划分**: 严格的训练/验证/测试集划分，确保泛化评估。

### 相关链接

- 📄 **论文**: [MNV-17: A High-Quality Performative Mandarin Dataset for Nonverbal Vocalization Recognition in Speech](https://arxiv.org/abs/2509.18196)
- 🤗 **数据集**: [maimai11/MNV_17](https://huggingface.co/datasets/maimai11/MNV_17)
- 🤖 **微调模型**: [即将发布]

### 引用

如果您使用了本数据集或相关工作，请引用：

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

### 主要贡献

1. **高质量数据集**: MNV-17提供了目前类别最全面的中文非语言发声数据集。
2. **泛化能力验证**: 证明了基于表演式数据的模型具有优秀的跨说话人泛化能力。
3. **协同效应**: 证明NV识别能力在多任务训练下的语音模型中不会损害ASR性能。
4. **基准建立**: 为NV感知ASR建立了标准评估基准。

---

**作者**: Jialong Mai, Jinxin Ji, Xiaofen Xing, Chen Yang, Weidong Chen, Jingyuan Xing, Xiangmin Xu

**机构**: 华南理工大学, 香港理工大学, 同济大学, 上海交通大学, 香港中文大学, 佛山大学

---

## English Version

### MNV-17 Qwen2.5-Omni Demo: Nonverbal Vocalization Recognition

This repository demonstrates the excellent performance of Qwen2.5-Omni model fine-tuned on the [MNV-17 dataset](https://huggingface.co/datasets/maimai11/MNV_17) for Nonverbal Vocalization (NV) ASR recognition tasks.

**[Click here for interactive audio demo](https://yongaifadian1.github.io/MNV-17/)**

### Key Findings

#### Unseen Speaker Generalization

**Crucial Note**: All demo samples are from speakers who were completely unseen during training.

This demonstrates that the model learned **universal NV vocalization patterns** rather than merely fitting specific speakers' habits, showcasing excellent cross-speaker generalization.

### Model Performance

According to our [paper](https://arxiv.org/abs/2509.18196) experimental results:

| Model | Joint CER | NV Recognition Accuracy |
|-------|-----------|------------------------|
| **Qwen2.5-Omni** | **3.60%** | **57.29%** |
| Qwen2-Audio | 4.84% | 56.28% |
| SenseVoice | 8.71% | 57.29% |
| Paraformer | 5.70% | 28.64% |

#### Performance Highlights

1. **Lowest Joint Error Rate**: Qwen2.5-Omni achieved 3.60% joint CER, best performance in dual ASR and NV recognition tasks.
2. **Excellent NV Recognition**: 57.29% accuracy under strict exact-match evaluation (type, count, order must all match).

### Demo Samples

The following shows the prediction results of Qwen2.5-Omni model fine-tuned on MNV-17 dataset on demo samples:

#### Sample 1
- **Model Prediction**: 这个理论的悖论之处在于 [cough] 请大家原谅，在于它的前提本身——哎呀这粉笔灰真是 [sneeze]——它的前提本身就包含了结论，这听起来是不是很 [chuckle] 荒谬。

#### Sample 2
- **Model Prediction**: 我给自己泡了杯热茶 [hum]，又从冰箱里拿出那块昨天没舍得吃的提拉米苏 [smack]，然后窝在沙发里刷着搞笑视频 [laugh]，这大概就是最简单的幸福吧。

#### Sample 3
- **Model Prediction**: 他开着那辆新买的跑车 [whistle] 从我身边呼啸而过，故意在我面前停下 [cough] 做出一个自以为很帅的姿势，我当场 [clap] 就给他鼓了鼓掌，要多敷衍有多敷衍。

#### Sample 4
- **Model Prediction**: 晚饭时场面一度非常热闹，我家的猫[hiss]不让新来的客人靠近，小侄女表演完节目后大家[applaud]热情鼓掌，而对胡椒粉过敏的爷爷则[sneeze]打起了喷嚏。

#### Sample 5
- **Model Prediction**: 我一走进那个积满灰尘的阁楼 [sneeze] 就忍不住打了个大喷嚏，面对着堆积如山的杂物 [sigh] 真不知从何下手，但当我从旧箱子里翻出那张绝版黑胶唱片时，我简直想为自己的好运 [clap] 欢呼！

#### Sample 6
- **Model Prediction**: 老教授讲到他年轻时的糗事，全班 [laugh] 都笑得前仰后合，可他一提到这周末的作业 [moan] 我的头就开始疼了，而且这教室的灰尘也太多了 [sneeze]，真是让人受不了。

#### Sample 7
- **Model Prediction**: 看着电影里主角牺牲的画面，影院里一片 [sniffle] 的啜泣声，我却在内心为他的壮举 [applaud] 喝彩，然后长叹一口气 [hum]，思考着人性的复杂。

#### Sample 8
- **Model Prediction**: 回想起那些独自奋斗的夜晚 [sigh]，真不知道是怎么熬过来的，但当我昨天终于攻克那个难题时 [clap]，我知道所有的付出都值得了，最终项目成功发布那一刻 [applaud]，我感受到了前所未有的成就感。

#### Sample 9
- **Model Prediction**: 他最终 [exhale] 放下了手中的旧照片，心想我们 [sigh] 终究还是走到了这一步，一念及此，又想起她最后那些话 [hiss]，真是刻薄又伤人。

### Dataset Characteristics

#### MNV-17 Dataset Advantages

1. **Performative Recording**: Avoids ambiguity of NVs in spontaneous speech, ensures high-quality annotation.
2. **Class Balance**: 17 NV categories with balanced distribution (max/min ratio only 2.7).
3. **Speaker Diversity**: 49 native Mandarin speakers from various regions.
4. **Rich Context**: NVs naturally embedded in semantically rich sentences.

#### Design Innovation

- **Scripted Approach**: LLM-generated natural contexts ensure semantic reasonableness of NVs.
- **Multi-NV Combinations**: Supports random combinations of 1-3 NVs, simulating real scenarios.
- **Speaker-Independent Split**: Strict train/validation/test division ensures generalization evaluation.

### Related Links

- 📄 **Paper**: [MNV-17: A High-Quality Performative Mandarin Dataset for Nonverbal Vocalization Recognition in Speech](https://arxiv.org/abs/2509.18196)
- 🤗 **Dataset**: [maimai11/MNV_17](https://huggingface.co/datasets/maimai11/MNV_17)
- 🤖 **Fine-tuned Model**: [Coming Soon]

### Citation

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

### Key Contributions

1. **High-Quality Dataset**: MNV-17 provides the most comprehensive Chinese nonverbal vocalization dataset.
2. **Generalization Verification**: Proves excellent cross-speaker generalization of performative data-based models.
3. **Synergy Discovery**: Proves NV recognition can enhance rather than harm ASR performance.
4. **Benchmark Establishment**: Establishes standard evaluation benchmark for NV-aware ASR.

---

**Authors**: Jialong Mai, Jinxin Ji, Xiaofen Xing, Chen Yang, Weidong Chen, Jingyuan Xing, Xiangmin Xu

**Institutions**: South China University of Technology, The Hong Kong Polytechnic University, Tongji University, Shanghai Jiao Tong University, The Chinese University of Hong Kong, Foshan University