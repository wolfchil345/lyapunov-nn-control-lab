🌐 언어: [English](../en/faq.md) | [日本語](../ja/faq.md) | [한국어](../ko/faq.md) | [ไทย](../th/faq.md)

# Frequently Asked Questions

이 페이지는 project에 대한 자주 묻는 질문에 답합니다.

## What is this project about?

이 project는 mass-spring-damper system용 neural network controller를 학습하고 평가합니다. controller는 LQR reference로부터 학습하며 simulation metrics, Lyapunov-style checks, robustness tests, sampled finite-horizon convergence maps로 평가됩니다.

## Why use LQR as the reference controller?

LQR은 선형 systems를 위한 표준 제어 방법입니다. 안정적이고 해석 가능한 reference policy를 제공하므로 neural network controller의 학습 및 비교에 유용합니다.

## Does this project prove global stability?

아니요. Lyapunov grid check는 경험적 평가 도구입니다. sampled states에서 유용한 evidence를 제공할 수 있지만, global stability의 완전한 formal proof로 설명해서는 안 됩니다.

## What makes this project different from a normal machine learning demo?

이 project는 neural network를 학습하는 것에 그치지 않습니다. closed-loop behavior, control cost, robustness, Lyapunov-related quantities, reproducibility, documentation quality도 함께 평가합니다.

## What should I show first in a presentation?

README부터 시작한 뒤 five minute demo script, main experiment workflow, results plots, Lyapunov 또는 robustness documentation을 보여주세요.

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

이것은 연구 프로토타입입니다. 결과는 선택한 system, controller settings, training setup, random seed, sampled grid, experiment conditions에 따라 달라집니다.
