🌐 言語: [English](../en/faq.md) | [日本語](../ja/faq.md) | [한국어](../ko/faq.md) | [ไทย](../th/faq.md)

# Frequently Asked Questions

このページでは、project に関するよくある質問に回答します。

## What is this project about?

この project は mass-spring-damper system 向けの neural network controller を学習・評価します。controller は LQR reference から学習し、simulation metrics、Lyapunov-style checks、robustness tests、sampled finite-horizon convergence maps で評価されます。

## Why use LQR as the reference controller?

LQR は線形 systems の標準的な制御手法です。安定で解釈しやすい reference policy を与えるため、neural network controller の学習と比較に有用です。

## Does this project prove global stability?

いいえ。Lyapunov grid check は経験的な評価ツールです。sampled states 上で有用な evidence を提供できますが、global stability の完全な形式証明として記述すべきではありません。

## What makes this project different from a normal machine learning demo?

この project は neural network を学習するだけではありません。closed-loop behavior、control cost、robustness、Lyapunov-related quantities、reproducibility、documentation quality も評価します。

## What should I show first in a presentation?

まず README を示し、その後 five minute demo script、main experiment workflow、results plots、Lyapunov または robustness documentation を示してください。

## How do I check that the project is working?

```bash
python scripts/check_environment.py
make checks
```

## Where are the main files?

- `src/`: source code
- `tests/`: automated tests
- `scripts/`: repeatable command scripts
- `docs/`: explanations and guides
- `results/`: generated outputs

## What are the current limitations?

これは研究プロトタイプです。結果は、選択した system、controller settings、training setup、random seed、sampled grid、experiment conditions に依存します。
