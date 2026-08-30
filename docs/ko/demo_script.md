🌐 언어: [English](../en/demo_script.md) | [日本語](../ja/demo_script.md) | [한국어](../ko/demo_script.md) | [ไทย](../th/demo_script.md)

# Five Minute Demo Script

이 script는 교수, reviewer, interviewer, lab member에게 project를 발표할 때 사용합니다.

## 0. Goal

이 repository가 Lyapunov-aware evaluation을 갖춘 neural network control용 재현 가능한 research prototype임을 보여줍니다.

## 1. Opening, 30 seconds

이 project는 mass-spring-damper system을 위한 neural network controller를 다룹니다. controller는 LQR controller를 모방하도록 학습되고, 이후 simulation metrics, Lyapunov analysis, robustness tests, sampled finite-horizon convergence maps로 평가됩니다.

## 2. Repository tour, 60 seconds

- `README.md`: project overview 및 주요 사용법.
- `src/`: system dynamics, controllers, simulation, Lyapunov checks, metrics, robustness, plotting의 핵심 구현.
- `tests/`: 중요한 project behavior에 대한 automated tests.
- `scripts/`: checking, cleaning, summarizing, running experiments를 위한 repeatable commands.
- `docs/`: methodology, troubleshooting, reproducibility, review guides, release process.
- `results/`: 생성된 figures, metrics, reports.

## 3. Run checks, 60 seconds

```bash
python scripts/check_environment.py
make checks
```

`make checks`가 documentation link check, Python tests, quick-start example을 실행한다는 점을 설명하세요.

## 4. Explain research idea, 90 seconds

baseline controller는 LQR이며 linear system에 대해 안정적인 reference controller를 제공합니다. neural network controller는 이 reference behavior를 학습합니다. 학습 후 project는 learned controller가 closed-loop simulation에서 잘 동작하는지와 Lyapunov-related quantities가 grid에서 안전하게 보이는지를 점검합니다.

## 5. Show outputs, 60 seconds

`results/`의 generated plots와 summary files를 보여주세요. trajectory behavior, control signal behavior, performance metrics, Lyapunov checks, robustness results, finite-horizon convergence comparisons에 집중합니다. horizon과 tolerance를 명시하고 이것이 수학적 attraction region이 아님을 설명합니다.

## 6. Closing, 30 seconds

중요한 점은 neural network가 LQR을 모방할 수 있다는 것뿐 아니라, repository에 재현 가능한 checks, documentation, safety-focused evaluation tools가 포함되어 있다는 점입니다.

## Demo safety

실제 demo 전에 다음을 실행하세요:

```bash
python scripts/check_environment.py
make checks
git status
```

clean working tree에서만 demo를 진행하세요.
