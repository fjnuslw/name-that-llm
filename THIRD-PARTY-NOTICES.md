# Third-party sources and scope

This repository publishes newly written explanatory material, aggregate results
and lightweight reporting/fusion code. It does not redistribute third-party
training data, checkpoints, prefit heads, compiled binaries or full pipelines.
Their original licenses and attribution requirements continue to apply.

- Competition: https://www.kaggle.com/competitions/name-that-llm
- Open Pool Kaggle V16, crtproduction and credited source contributors:
  https://www.kaggle.com/datasets/crtproduction/name-that-llm-open-pool/versions/16
- Qwen3.8-27B, fixed revision 37561816e66b5b9153b1b64c10968c18c1e6f4a0:
  https://huggingface.co/Qwen/Qwen3.8-27B/tree/37561816e66b5b9153b1b64c10968c18c1e6f4a0
- Qwen3.5-9B-Base, revision 68c46c4b3498877f3ef123c856ecfde50c39f404:
  https://huggingface.co/Qwen/Qwen3.5-9B-Base/tree/68c46c4b3498877f3ef123c856ecfde50c39f404
- Omer Faruk Merey, fixed V1, scriptVersionId 367805055:
  https://www.kaggle.com/code/omerfarukmerey/0-682-0-681-qwen3-8-27b-gsq-12-mix-0-50?scriptVersionId=367805055
  Retain the original upstream credits, including lightningv08, heliosli,
  mercurydust, Roman Tamrazov and other contributors.
- Public P0 assets also credit Dhruv Tibarewal, Nishant Dahal, Nuri Dudak,
  Lucas Boesen and the authors of the original model, encoder, style and SVC assets.
  A versioned reference inventory is provided in results/public-dependencies.json.
- ATLAS assets, josephadamski91, V3:
  https://www.kaggle.com/datasets/josephadamski91/ntl-atlas-qwen3-8b-v1/versions/3
- 008 likelihood extension: Lightning V52 / feiyu V1 and their upstream
  feature/classifier/execution contributors:
  https://www.kaggle.com/code/lightningv08/0-694-glm-5-3-likelihood-qwen3-8-27b-lora
  https://www.kaggle.com/code/feiyu26/ntl-0684-v1-graft?scriptVersionId=369151207
  This experiment is not presented as a trained or reliably deployed original expert.

The standalone fusion formula follows the credited arithmetic/log-probability
outer pipeline. Its callback intentionally leaves original common postprocessing
external; this is not the full scoring implementation. The repository's
Apache-2.0 license applies only to newly authored material supplied here.
