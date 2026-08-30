🌐 言語: [English](../en/portfolio_pitch.md) | [日本語](../ja/portfolio_pitch.md) | [한국어](../ko/portfolio_pitch.md) | [ไทย](../th/portfolio_pitch.md)

# Portfolio Pitch

このページは、CV、interview、教授との面談、research discussion、大学院出願で project を説明する際に使用します。

## One sentence summary

LQR imitation、Lyapunov-aware analysis、robustness tests、明示的 finite-horizon convergence maps を用いて、mass-spring-damper system 向け neural network controller を学習・評価する、再現可能な Python research prototype。

## 30 second pitch

この project は、neural network controller が LQR controller を模倣できるかを、control-oriented diagnostic tools で評価しながら検討します。nominal uncontrolled plant はすでに asymptotically stable です。したがって repository は、imitation、transient performance、robustness、sampled Lyapunov checks、finite-horizon final-state tolerance maps に焦点を当て、automated tests と再現可能な documentation を備えています。

## Technical keywords

- Neural network control
- LQR imitation
- Lyapunov analysis
- Closed-loop simulation
- Robustness evaluation
- horizon と tolerance metadata を伴う finite-horizon convergence mapping
- Reproducible research code
- Python and PyTorch

## What makes the project strong

- machine learning と control engineering を接続している。
- automated tests と local checks を含む。
- methodology、limitations、reproducibility、troubleshooting を文書化している。
- source code、scripts、tests、documentation、results を分離している。
- stability と robustness を後付けでなく評価テーマとして扱っている。

## What to show first

1. README overview
2. Five minute demo script
3. Main experiment workflow
4. Results plots and summary report
5. Lyapunov and robustness documentation

## Interview talking points

- LQR を reference controller にする理由
- neural network controller の training 方法
- Lyapunov-style evaluation が有用な理由
- robustness tests が評価をより現実的にする理由
- research code における reproducibility の重要性

## Honest limitation statement

この project は research prototype です。Lyapunov grid check は empirical evaluation tool であり、global stability の完全な formal proof として記述すべきではありません。
