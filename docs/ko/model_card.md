🌐 언어: [English](../en/model_card.md) | [日本語](../ja/model_card.md) | [한국어](../ko/model_card.md) | [ไทย](../th/model_card.md)

# Model Card

이 model card는 Lyapunov Neural-Network Control Lab에서 사용하는 neural-network controller를 요약합니다.

## Model purpose

neural-network controller는 system state를 scalar control input 하나로 매핑합니다.

이 모델은 stability-aware training penalty를 사용하면서 LQR controller를 모방하도록 학습됩니다.

## System state

model input은 2차원 state입니다.

- normalized position `q`
- normalized velocity `v = dq/dtau`

## Model output

model output은 scalar control input 하나입니다.

- model에 적용되는 normalized scalar control input `u`

## Training target

training target은 LQR controller에서 생성됩니다.

neural network는 LQR state-to-control mapping을 근사하도록 학습합니다.

## Stability-aware training

training process에는 Lyapunov-style penalty를 포함할 수 있습니다.

이것은 sampled states 주변에서 Lyapunov function을 줄이는 거동을 유도합니다.

## Intended use

이 controller는 simulation-based control experiments, 교육, 연구 탐색을 위한 것입니다.

neural-network control, Lyapunov-style checks, robustness tests, controller comparison 연구에 유용합니다.

## Out-of-scope use

이 model은 safety-certified real-world controller로 사용하면 안 됩니다.

hardware deployment, 위험한 systems, safety-critical environments에 대해 검증되지 않았습니다.

## Evaluation methods

controller는 다음으로 평가됩니다.

- closed-loop simulation
- final normalized-state norm
- normalized settling time
- quadratic LQR-style cost
- integrated squared normalized control effort
- maximum absolute normalized control input
- Lyapunov derivative grid checks
- robustness experiments
- finite-horizon final-state tolerance mapping

## Known limitations

- plant model이 단순합니다.
- controller가 학습 영역 밖으로 일반화되지 않을 수 있습니다.
- grid-based Lyapunov checks는 global stability를 증명하지 않습니다.
- simulation results는 환경에 따라 약간 달라질 수 있습니다.
- robustness tests는 일부 선택된 경우만 다룹니다.

## Recommended reporting

결과 보고 시 다음을 포함하세요.

- training settings
- random seed
- system parameters
- controller type
- evaluation metrics
- Lyapunov check results
- robustness settings
- finite-horizon convergence settings: horizon, tolerance, bounds, grid,
  tested count, and converged count

## Future improvements

- 더 많은 controller architectures 추가
- KAN-based controllers와 비교
- 더 강한 formal verification 추가
- neural Lyapunov functions 직접 학습
- 더 많은 nonlinear systems 테스트
