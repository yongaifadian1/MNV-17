# MNV-17 Qwen2.5-Omni Demo: Nonverbal Vocalization Recognition

**中文副语言识别演示 | Nonverbal Vocalization Recognition Demo**

本仓库展示了在 [MNV-17 数据集](https://huggingface.co/datasets/maimai11/MNV_17) 上微调的 Qwen2.5-Omni 模型在非语言发声（NV）ASR识别任务上的卓越表现。

This repository demonstrates the excellent performance of Qwen2.5-Omni model fine-tuned on the [MNV-17 dataset](https://huggingface.co/datasets/maimai11/MNV_17) for Nonverbal Vocalization (NV) ASR recognition tasks.

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
| Qwen2-Audio | 4.84% | 56.28% | -0.45% |
| SenseVoice | 8.71% | 57.29% | +0.47% |
| Paraformer | 5.70% | 28.64% | +1.22% |

### 性能亮点 | Performance Highlights

1. **最低联合错误率**: Qwen2.5-Omni 实现了 3.60% 的联合字符错误率，在 ASR 和 NV 识别双重任务中表现最佳
2. **卓越NV识别**: 在严格的完全匹配评估下达到 57.29% 准确率（类型、数量、顺序完全匹配）

1. **Lowest Joint Error Rate**: Qwen2.5-Omni achieved 3.60% joint CER, best performance in dual ASR and NV recognition tasks
2. **Excellent NV Recognition**: 57.29% accuracy under strict exact-match evaluation (type, count, order must all match)

## 演示样本 | Demo Samples

以下展示了Qwen2.5-Omni模型在测试集样本上的预测结果：

The following shows the prediction results of Qwen2.5-Omni model on test set samples:

### 样本 1 | Sample 1
<audio controls>
  <source src="audio_samples/speaker_F_02_chuckle_cough_sneeze_00.wav" type="audio/wav">
  Your browser does not support the audio element.
</audio>

- **模型预测**: 这个理论的悖论之处在于 [cough] 请大家原谅，在于它的前提本身——哎呀这粉笔灰真是 [sneeze]——它的前提本身就包含了结论，这听起来是不是很 [chuckle] 荒谬。

### 样本 2 | Sample 2
<audio controls>
  <source src="audio_samples/speaker_F_02_chuckle_hum_smack_00.wav" type="audio/wav">
  Your browser does not support the audio element.
</audio>

- **模型预测**: 我给自己泡了杯热茶 [hum]，又从冰箱里拿出那块昨天没舍得吃的提拉米苏 [smack]，然后窝在沙发里刷着搞笑视频 [laugh]，这大概就是最简单的幸福吧。

### 样本 3 | Sample 3
<audio controls>
  <source src="audio_samples/speaker_F_02_clap_cough_whistle_00.wav" type="audio/wav">
  Your browser does not support the audio element.
</audio>

- **模型预测**: 他开着那辆新买的跑车 [whistle] 从我身边呼啸而过，故意在我面前停下 [cough] 做出一个自以为很帅的姿势，我当场 [clap] 就给他鼓了鼓掌，要多敷衍有多敷衍。

### 样本 4 | Sample 4
<audio controls>
  <source src="audio_samples/speaker_F_03_applaud_hiss_sneeze_00.wav" type="audio/wav">
  Your browser does not support the audio element.
</audio>

- **模型预测**: 晚饭时场面一度非常热闹，我家的猫[hiss]不让新来的客人靠近，小侄女表演完节目后大家[applaud]热情鼓掌，而对胡椒粉过敏的爷爷则[sneeze]打起了喷嚏。

### 样本 5 | Sample 5
<audio controls>
  <source src="audio_samples/speaker_F_03_applaud_sigh_sneeze_00.wav" type="audio/wav">
  Your browser does not support the audio element.
</audio>

- **模型预测**: 我一走进那个积满灰尘的阁楼 [sneeze] 就忍不住打了个大喷嚏，面对着堆积如山的杂物 [sigh] 真不知从何下手，但当我从旧箱子里翻出那张绝版黑胶唱片时，我简直想为自己的好运 [clap] 欢呼！

### 样本 6 | Sample 6
<audio controls>
  <source src="audio_samples/speaker_F_03_laugh_moan_sneeze_00.wav" type="audio/wav">
  Your browser does not support the audio element.
</audio>

- **模型预测**: 老教授讲到他年轻时的糗事，全班 [laugh] 都笑得前仰后合，可他一提到这周末的作业 [moan] 我的头就开始疼了，而且这教室的灰尘也太多了 [sneeze]，真是让人受不了。

### 样本 7 | Sample 7
<audio controls>
  <source src="audio_samples/speaker_M_02_applaud_hum_sniffle_00.wav" type="audio/wav">
  Your browser does not support the audio element.
</audio>

- **模型预测**: 看着电影里主角牺牲的画面，影院里一片 [sniffle] 的啜泣声，我却在内心为他的壮举 [applaud] 喝彩，然后长叹一口气 [hum]，思考着人性的复杂。

### 样本 8 | Sample 8
<audio controls>
  <source src="audio_samples/speaker_M_03_applaud_clap_sigh_00.wav" type="audio/wav">
  Your browser does not support the audio element.
</audio>

- **模型预测**: 回想起那些独自奋斗的夜晚 [sigh]，真不知道是怎么熬过来的，但当我昨天终于攻克那个难题时 [clap]，我知道所有的付出都值得了，最终项目成功发布那一刻 [applaud]，我感受到了前所未有的成就感。

### 样本 9 | Sample 9
<audio controls>
  <source src="audio_samples/speaker_M_03_exhale_hiss_sigh_00.wav" type="audio/wav">
  Your browser does not support the audio element.
</audio>

- **模型预测**: 他最终 [exhale] 放下了手中的旧照片，心想我们 [sigh] 终究还是走到了这一步，一念及此，又想起她最后那些话 [hiss]，真是刻薄又伤人。

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