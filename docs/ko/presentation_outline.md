🌐 언어: [English](../en/presentation_outline.md) | [日本語](../ja/presentation_outline.md) | [한국어](../ko/presentation_outline.md) | [ไทย](../th/presentation_outline.md)

# Presentation Outline

이 outline은 수업, lab meeting, interview에서 Lyapunov Neural-Network Control Lab을 발표할 때 사용할 수 있습니다.

## 1. Project motivation

- neural-network controllers는 유연하지만 신뢰하기 어려울 수 있습니다.
- control engineering에는 stability, robustness, interpretability가 필요합니다.
- 이 project는 Lyapunov-style stability checks를 포함한 neural-network control을 탐구합니다.

## 2. System model

- plant는 mass-spring-damper system입니다.
- state는 normalized position `q`와 normalized velocity `v`를 포함합니다.
- control input은 normalized scalar이며 물리 force unit은 정의하지 않습니다.

## 3. Baseline controller

- LQR을 고전적 control baseline으로 사용합니다.
- neural-network controller는 LQR을 모방하도록 학습됩니다.

## 4. Neural-network controller

- model은 state를 control input으로 매핑합니다.
- training은 imitation loss와 stability-aware penalty를 사용합니다.
- 원점을 target equilibrium으로 취급합니다.

## 5. Stability analysis

- stability behavior 점검을 위해 Lyapunov-style function을 사용합니다.
- grid-based checks는 Lyapunov derivative가 음수인 영역을 추정합니다.
- finite-horizon convergence map은 주어진 normalized-time horizon과 normalized-state tolerance에서 `||x(T)||_2 < epsilon`을 만족하는 sampled initial states를 보고합니다.
- 이 map은 수학적 region of attraction이 아닙니다.

## 6. Robustness experiments

- actuator saturation은 input limits를 점검합니다.
- measurement-noise experiments는 noisy state feedback을 점검합니다.
- parameter-variation experiments는 변경된 normalized mass, damping, stiffness coefficients를 점검합니다.

## 7. Main outputs

- `performance_metrics.csv`
- `position_comparison.png`
- `phase_portrait.png`
- `lyapunov_contours.png`
- `finite_horizon_convergence_comparison.png`
- `experiment_report.md`

## 8. Key contribution

- 이 project는 simulation, neural-network control, Lyapunov-style checks, robustness tests, automatic reports, documentation을 하나의 재현 가능한 repository에 통합합니다.

## 9. Limitations

- 실제 plants와 비교하면 system이 단순합니다.
- grid checks는 empirical evidence를 제공하지만 완전한 global stability proof는 아닙니다.
- neural-network controller는 training region 밖에서 나쁜 거동을 보일 수 있습니다.

## 10. Future work

- 더 많은 nonlinear systems를 테스트합니다.
- neural Lyapunov functions를 직접 학습합니다.
- 더 강한 formal verification을 추가합니다.
- 더 다양한 controller types와 비교합니다.
- workflow를 KAN-based controllers에 적용합니다.
