🌐 言語: [English](../en/demo_script.md) | [日本語](../ja/demo_script.md) | [한국어](../ko/demo_script.md) | [ไทย](../th/demo_script.md)

# Five Minute Demo Script

この script は、教授・reviewer・interviewer・lab member に project を説明する際に使用します。

## 0. Goal

この repository が、Lyapunov-aware evaluation を備えた neural network control の再現可能な research prototype であることを示します。

## 1. Opening, 30 seconds

この project は mass-spring-damper system に対する neural network controller を扱います。controller は LQR controller を模倣するよう学習され、その後 simulation metrics、Lyapunov analysis、robustness tests、sampled finite-horizon convergence maps で評価されます。

## 2. Repository tour, 60 seconds

- `README.md`: project overview と主な使い方。
- `src/`: system dynamics、controllers、simulation、Lyapunov checks、metrics、robustness、plotting の中核実装。
- `tests/`: 重要な project behavior の automated tests。
- `scripts/`: checking、cleaning、summarizing、experiments 実行のための repeatable commands。
- `docs/`: methodology、troubleshooting、reproducibility、review guides、release process。
- `results/`: 生成された figures、metrics、reports。

## 3. Run checks, 60 seconds

```bash
python scripts/check_environment.py
make checks
```

`make checks` は documentation link check、Python tests、quick-start example を実行することを説明します。

## 4. Explain research idea, 90 seconds

baseline controller は LQR で、線形 system に対する安定な reference controller を提供します。neural network controller はこの reference behavior を学習します。学習後、project は learned controller が closed-loop simulation で良好に振る舞うか、Lyapunov-related quantities が grid 上で安全に見えるかを確認します。

## 5. Show outputs, 60 seconds

`results/` の生成 plots と summary files を示します。trajectory behavior、control signal behavior、performance metrics、Lyapunov checks、robustness results、finite-horizon convergence comparisons に焦点を当てます。horizon と tolerance を明示し、これは数学的 attraction region ではないことを説明します。

## 6. Closing, 30 seconds

重要点は neural network が LQR を模倣できることだけではなく、repository が再現可能な checks、documentation、安全性を意識した evaluation tools を含むことです。

## Demo safety

実際の demo の前に次を実行します。

```bash
python scripts/check_environment.py
make checks
git status
```

clean working tree からのみ demo してください。
