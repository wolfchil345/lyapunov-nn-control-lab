🌐 언어: [English](../en/thesis_plan.md) | [日本語](../ja/thesis_plan.md) | [한국어](../ko/thesis_plan.md) | [ไทย](../th/thesis_plan.md)

# Thesis Plan

이 문서는 Lyapunov Neural-Network Control Lab을 가능한 졸업 연구 계획과 연결합니다.

## Tentative title

Lyapunov-style stability evaluation of neural-network controllers for a mass-spring-damper system

## Background

neural-network controllers는 nonlinear control policies를 근사할 수 있지만, 그 stability behavior를 보장하기는 어렵습니다.

LQR 같은 classical control methods는 linear systems에 신뢰할 수 있는 baseline을 제공합니다.

이 project는 LQR teacher로부터 학습한 neural-network controller를 Lyapunov-style checks로 평가합니다.

## Research objective

목표는 neural-network controller가 LQR을 모방하면서 simulation에서 유의미한 closed-loop stability behavior를 유지할 수 있는지 평가하는 것입니다.

## Proposed method

1. mass-spring-damper system을 정의한다.
2. baseline으로 LQR controller를 설계한다.
3. LQR controller로부터 training data를 생성한다.
4. neural-network controller를 학습한다.
5. stability-aware training penalty를 추가한다.
6. closed-loop responses를 시뮬레이션한다.
7. performance, robustness, Lyapunov-style stability behavior를 평가한다.

## Evaluation items

- final normalized-state norm
- normalized settling time
- quadratic LQR-style cost
- integrated squared control effort
- maximum absolute normalized control input
- Lyapunov derivative behavior
- robustness under noise
- robustness under parameter variation
- actuator saturation behavior
- explicit sampling metadata를 포함한 finite-horizon convergence counts 및 fractions

## Expected contribution

예상 기여는 performance metrics, robustness tests, Lyapunov-style stability checks를 사용해 classical controllers와 neural-network controllers를 비교하는 재현 가능한 Python research workflow입니다.

## Possible KAN extension

표준 neural-network controller가 동작한 뒤 동일한 pipeline을 KAN-based controller 비교로 확장할 수 있습니다.

비교를 통해 동일 설정에서 KAN이 imitation accuracy,
smoothness, robustness, finite-horizon convergence를 개선하는지 조사할 수 있습니다.

## Risks and limitations

- 현재 plant는 단순합니다.
- grid-based checks는 global stability를 증명하지 않습니다.
- training region 밖에서 neural-network behavior는 신뢰하기 어려울 수 있습니다.
- simulation results는 hardware validation과 동일하지 않습니다.

## Possible final thesis structure

1. Introduction
2. LQR, neural-network control, Lyapunov stability 배경
3. System model 및 baseline controller
4. Neural-network controller design
5. Stability-aware training method
6. Simulation experiments
7. Robustness and finite-horizon convergence analysis
8. Discussion and limitations
9. Conclusion and future work
