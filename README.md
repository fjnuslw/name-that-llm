# Name That LLM

**Prompt-grouped layer readouts, two-stage LoRA, and offline T4 inference**

An evidence-grounded technical report for 18-class LLM source attribution. The best verified configuration, **G07**, scored **0.674 Public Balanced Accuracy**, compared with **0.669** for our V3 baseline (+0.5 percentage points). These are Public scores recorded on 2026-11-15; no Private score, medal or final-rank claim is made.

[Kaggle technical report](https://www.kaggle.com/code/fjnulinweisong/name-that-llm-g07-technical-report) �� [����˵��](docs/method.md) �� [ʵ����](docs/experiments.md) �� [������ʧ�ܸ���](docs/runtime-lessons.md) �� [��Դ�����۱߽�](docs/provenance.md)

## ��Ŀ����ʲô

�ڹٷ� 2,699 ����150 �� Prompt �������£��� Prompt �̶����ۣ���עδ����Ŀ��������鲢�̶� Open Pool V16 �� 223,840 �������ı���61 ����Դ���ù̶� 54,000 ����Դ�ֲ��Ӽ����� Qwen3.8-27B / Qwen3.5-9B-Base �Ķ����������������ⲿ���Ͻ������׶� LoRA��

��Ŀ���������Ĺ��� P0 ���ɣ������� 27B final �� 9B �����滻����β����֧����˫ T4 ����������֤ NF4/FP16����������������������������롣���� Transformer/��ͷ�����ģ�͡�ATLAS ��ԭ��ͬ�����������ι�����

## ����֤���

| ֤�ݷ�Χ | 27B | 9B |
|---|---:|---:|
| 004 matched frozen ���� OOF BA | 0.472682 | 0.442670 |
| 004 LoRA ���� OOF BA | 0.650932 | 0.630907 |
| ͬ 180 �з�֧ǰ���ʱ���� | 34.4% | 30.4%�����ۺϼƣ� |

| Public �汾 | V3 | G01 | G04 | G07 | 27B ����֧ | 9B ���۵���֧ |
|---|---:|---:|---:|---:|---:|---:|
| BA | 0.669 | 0.666 | 0.672 | **0.674** | 0.640 | 0.626 |

���� OOF ����ѡ������Σ�������Ϊ��ƫ�������ԡ�ǰ�����ٱ���ֻ����ͬһ�� 180 �У���������ϵͳ�����ز������١�

## G07 �ں�

~~~text
P1 = 0.45 P0 + 0.55 P27
Qk = softmax(0.60 log(P1) + 0.40 L9[k]), k = 0..4
Pfinal = mean(postprocess(Qk))
~~~

�����������ڲ�ͬ�׶Ρ�ȱ�١�27B+9B���� P0����ͬ���� Public ���գ����ܰ������ں϶Ե�ģ�͵�ȫ����ֵ������ P0��

## ���ֿ��ܸ���ʲô

~~~bash
python scripts/verify_results.py
jupyter notebook notebooks/project-report.ipynb
~~~

������� Notebook �԰���������Ҫ GPU��Ȩ�ء�ԭʼѵ���ı��������������ֹ������ܱ��Ͳ�ֵ��������ָ�����ں�ʾ�����롣src/fusion.py �ṩ�ɶ�����㹫ʽ�ӿڣ���Ҫ�����ṩ������ʼ�ԭ������

**�����Ƿ����������˰���** ���� LoRA ��ѵ��ȫ���������طź����سɼ�������Ҫ����ȡ��ԭ����������������ģ��/��������δ�����ڱ�����ԭʼ�ı������� ID/OOF��Ȩ�ء�ƾ�ݺ��ڲ���ά��¼��δ�����

008 ����ʵ GLM ��Ȼ��չ�����������Ϻ�ʱ������Сʱ��N01 �������ܳ�ʱ�����޸÷�֧��Ч��������״̬��ɱ��ڲ������а�ʱ����ռ�¼��

## ����������

ԭ����ϵͳ��Omer Faruk Merey �̶� V1 / scriptVersionId 367805055 �����������ߣ�Open Pool V16��crtproduction ��ԭʼ��Դ�����ߣ����������� [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md)��

�±�д�ı���������������˴������ Apache-2.0�������ɲ����ǵ��������ݡ�Ȩ�ء�������ʲ������ֿ�û�����·ַ���Щ�ʲ���
