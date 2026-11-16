# Name That LLM

**Prompt-grouped layer readouts, two-stage LoRA, and offline T4 inference**

An evidence-grounded technical report for 18-class LLM source attribution. The best verified configuration, **G07**, scored **0.674 Public Balanced Accuracy**, compared with **0.669** for our V3 baseline (+0.5 percentage points). These are Public scores recorded on 2026-11-15; no Private score, medal or final-rank claim is made.

[Kaggle technical report](https://www.kaggle.com/code/fjnulinweisong/name-that-llm-g07-technical-report) · [方法说明](docs/method.md) · [实验结果](docs/experiments.md) · [部署与失败复盘](docs/runtime-lessons.md) · [来源与评价边界](docs/provenance.md)

## 项目做了什么

在官方 2,699 条、150 个 Prompt 的条件下，按 Prompt 固定五折，关注未见题目泛化。审查并固定 Open Pool V16 的 223,840 条公开文本、61 个来源；用固定 54,000 条来源分层子集搜索 Qwen3.8-27B / Qwen3.5-9B-Base 的多层读出，再以完整外部语料进行两阶段 LoRA。

项目复用署名的公共 P0 集成，用自有 27B final 与 9B 五折替换两个尾部分支。在双 T4 断网环境验证 NF4/FP16、长度组批、离线依赖和输出对齐。公共 Transformer/组头、风格模型、ATLAS 与原共同后处理保留上游归属。

## 已验证结果

| 证据范围 | 27B | 9B |
|---|---:|---:|
| 004 matched frozen 开发 OOF BA | 0.472682 | 0.442670 |
| 004 LoRA 开发 OOF BA | 0.650932 | 0.630907 |
| 同 180 行分支前向耗时减少 | 34.4% | 30.4%（五折合计） |

| Public 版本 | V3 | G01 | G04 | G07 | 27B 单分支 | 9B 五折单分支 |
|---|---:|---:|---:|---:|---:|---:|
| BA | 0.669 | 0.666 | 0.672 | **0.674** | 0.640 | 0.626 |

开发 OOF 经过选层与调参，不能视为无偏独立测试。前向提速比例只来自同一批 180 行，不是完整系统或隐藏测试提速。

## G07 融合

~~~text
P1 = 0.45 P0 + 0.55 P27
Qk = softmax(0.60 log(P1) + 0.40 L9[k]), k = 0..4
Pfinal = mean(postprocess(Qk))
~~~

两个比例处于不同阶段。缺少“27B+9B、无 P0”的同条件 Public 对照，不能把完整融合对单模型的全部差值归因于 P0。

## 本仓库能复核什么

~~~bash
python scripts/verify_results.py
jupyter notebook notebooks/project-report.ipynb
~~~

结果复核 Notebook 自包含，不需要 GPU、权重、原始训练文本或联网。它重现公开汇总表和差值，并导出指标与融合示例代码。src/fusion.py 提供可读的外层公式接口，需要读者提供对齐概率及原后处理。

**本版是方法与结果复核包。** 完整 LoRA 重训、全公共集成重放和隐藏成绩重现需要另行取得原数据与许可允许的模型/适配器，未包含于本包。原始文本、逐行 ID/OOF、权重、凭据和内部运维记录均未打包。

008 的真实 GLM 似然扩展在三行样例上耗时超过三小时；N01 隐藏重跑超时，尚无该分支有效分数。其状态与成本在部署复盘中按时间快照记录。

## 署名与许可

原公共系统：Omer Faruk Merey 固定 V1 / scriptVersionId 367805055 及其上游作者；Open Pool V16：crtproduction 与原始来源贡献者；其他依赖见 [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md)。

新编写的报告与轻量结果复核代码采用 Apache-2.0。此许可不覆盖第三方数据、权重、代码或资产；本仓库没有重新分发这些资产。
