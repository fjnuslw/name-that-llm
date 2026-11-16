# 证据、复用与公开边界

本报告以 2026-11-16 的本地证据快照为基础；Public 分数回执核对日期为 2026-11-15。OOF 为开发诊断，Public 为平台隐藏重跑结果，三行/180 行为工程验证，各自分开记录。

## 已复核

- 官方 2,699 行、150 Prompt、18 类；固定 CV 五折各 30 Prompt。
- 54,000 个唯一外部 ID，每类 3,000。
- 20 份关键 OOF 的完整 ID、标签、Prompt、逐行固定折号、有限 logits、argmax 与 BA。
- 已得分版本 V3/G01/G04/G07/A27/A09 的本地官方 API 回执。
- 同输入分支效率与 008 实际执行审查记录。

公开包不含原始文本、逐行 ID/预测、训练权重、凭据或内部运维文件。指纹可用于获得合法原始归档后的身份核验；本包的轻量脚本只验证已公开汇总的完整性与算术，不声称重跑 OOF、训练或平台评分。

## 本赛分享要求

发布前通过官方 Competition API 读取本赛 rules、foundational-rules 与 Code Requirements。公开相关代码须兼顾第三方权利，并在本赛关联的 Kaggle Notebook 或讨论中向所有参赛者提供。本包通过自包含的关联 Notebook 公开同一报告和轻量代码，采用 Apache-2.0；不重新分发官方原文或第三方权重。

[本赛规则](https://www.kaggle.com/competitions/name-that-llm/rules) · [本赛说明](https://www.kaggle.com/competitions/name-that-llm)

## 第三方来源

公共 P0、Gaussian/twin、TF-IDF/风格分支、ATLAS 与共同后处理保留原始署名。项目贡献范围说明不自动认定为单人独立完成全部工作，也不认领上游预拟合模型为原创。具体来源见 THIRD-PARTY-NOTICES.md。

报告一致性摘要 SHA256：3648407ad220e9b5f7770c11e0a8deb4c4c808b77e8b0d039129ad4766f31d04
