🌐 언어: [English](../en/portfolio_pitch.md) | [日本語](../ja/portfolio_pitch.md) | [한국어](../ko/portfolio_pitch.md) | [ไทย](../th/portfolio_pitch.md)

# Portfolio Pitch

이 페이지는 CV, interview, 교수 미팅, research discussion, 대학원 지원에서 project를 설명할 때 사용합니다.

## One sentence summary

LQR imitation, Lyapunov-aware analysis, robustness tests, 명시적 finite-horizon convergence maps를 사용해 mass-spring-damper system용 neural network controller를 학습 및 평가하는 재현 가능한 Python research prototype.

## 30 second pitch

이 project는 neural network controller가 LQR controller를 모방할 수 있는지를 control-oriented diagnostic tools로 평가하며 연구합니다. nominal uncontrolled plant는 이미 asymptotically stable입니다. 따라서 repository는 imitation, transient performance, robustness, sampled Lyapunov checks, finite-horizon final-state tolerance maps에 초점을 두며 automated tests와 reproducible documentation을 제공합니다.

## Technical keywords

- Neural network control
- LQR imitation
- Lyapunov analysis
- Closed-loop simulation
- Robustness evaluation
- horizon 및 tolerance metadata를 포함한 finite-horizon convergence mapping
- Reproducible research code
- Python and PyTorch

## What makes the project strong

- machine learning과 control engineering을 연결합니다.
- automated tests와 local checks를 포함합니다.
- methodology, limitations, reproducibility, troubleshooting을 문서화합니다.
- source code, scripts, tests, documentation, results를 분리합니다.
- stability와 robustness를 부가 요소가 아닌 평가 주제로 다룹니다.

## What to show first

1. README overview
2. Five minute demo script
3. Main experiment workflow
4. Results plots and summary report
5. Lyapunov and robustness documentation

## Interview talking points

- LQR을 reference controller로 사용하는 이유
- neural network controller 학습 방법
- Lyapunov-style evaluation이 유용한 이유
- robustness tests가 평가를 더 현실적으로 만드는 방식
- 연구 코드에서 reproducibility가 중요한 이유

## Honest limitation statement

이 project는 research prototype입니다. Lyapunov grid check는 empirical evaluation tool이며 global stability의 complete formal proof로 설명하면 안 됩니다.
