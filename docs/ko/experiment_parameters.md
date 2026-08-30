🌐 언어: [English](../en/experiment_parameters.md) | [日本語](../ja/experiment_parameters.md) | [한국어](../ko/experiment_parameters.md) | [ไทย](../th/experiment_parameters.md)

# Experiment Parameters 가이드

이 가이드는 실험 동작과 결과에 영향을 주는 주요 파라미터를 설명합니다.

## 파라미터가 중요한 이유

신경망 제어 실험은 학습 설정, 난수 시드, 격자 범위, 시스템 상수, 강건성 설정이 바뀌면 결과가 달라질 수 있습니다. 결과를 비교하기 전에 중요한 파라미터 변경을 기록하세요.

## 주요 파라미터 그룹

## 좌표 규약

실험은 normalized, dimensionless 체계입니다. `tau`는 normalized time, `x = [q, v]`는 normalized position/velocity, `u`는 normalized control input입니다. 따라서 임곗값과 노이즈 수준도 normalized coordinates를 사용합니다.

## 1. 시스템 파라미터

이 항목은 normalized 2차 모델을 정의합니다. normalized mass, damping, stiffness 계수와 상태공간 행렬이 포함됩니다. 수치 계수는 kg, N/m 같은 SI 물리량이 아닙니다.

중요 파일:

- `src/system.py`
- `src/parameter_variation.py`

## 2. 제어기 파라미터

이 항목은 LQR 기준 제어기, 신경망 제어기, 포화 동작, 학습된 제어 출력에 영향을 줍니다.

중요 파일:

- `src/system.py`
- `src/controllers.py`
- `main.py`

## 3. 학습 파라미터

이 항목은 신경망 학습에 영향을 줍니다.

예시:

- Random seed
- Number of epochs
- Learning rate
- Dataset size
- Loss weights
- Network hidden size

중요 파일:

- `src/controllers.py`
- `main.py`

## 4. 시뮬레이션 파라미터

이 항목은 폐루프 평가에 영향을 줍니다.

예시:

- Initial condition
- Normalized simulation time
- Normalized time step
- Controller saturation limit

중요 파일:

- `src/simulation.py`
- `main.py`

## 5. Lyapunov 격자 파라미터

이 항목은 sampled Lyapunov-style checks에 영향을 줍니다.

예시:

- State range
- Grid density
- Controller used during grid evaluation

중요 파일:

- `src/lyapunov.py`
- `main.py`

## 6. 강건성 파라미터

이 항목은 노이즈 및 모델 변동 실험에 영향을 줍니다.

예시:

- normalized state 두 좌표에 독립 적용되는 scalar noise standard deviation
- Parameter variation range
- Number of tested cases

중요 파일:

- `src/noise.py`
- `src/parameter_variation.py`
- `src/stability_ablation.py`

## 안전한 비교 규칙

두 실험 결과를 비교할 때는 가능하면 한 번에 하나의 파라미터 그룹만 바꾸세요.

stability-weight ablation은 random seed를 반복 nuisance factor로 취급합니다. 모든 weight가 동일한 explicit seed list로 학습됩니다. 기본 연구 워크플로는 연속된 3개 seed를 사용하며, 호출자는 explicit `ExperimentSeedPlan`을 제공하거나 base seed와 repeat count를 설정할 수 있습니다.

measurement-noise 실험도 모든 noise amplitude에 동일한 seed list를 사용합니다. 하나의 seed에 대해 하나의 standardized Gaussian sequence를 생성하고 각 standard deviation으로 스케일합니다. 이 common-random-number 설계는 모든 확률 불확실성이 제거되었다고 주장하지 않으면서 seed 기반 짝비교를 가능하게 합니다.

## 최종 결과 저장 전

다음을 실행하세요.

```bash
python scripts/check_environment.py
make checks
python main.py
python scripts/summarize_results.py
```

그다음 어떤 파라미터를 왜 바꿨는지 기록하세요.
