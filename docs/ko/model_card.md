🌐 언어: [English](../en/model_card.md) | [日本語](../ja/model_card.md) | [한국어](../ko/model_card.md) | [ไทย](../th/model_card.md)

# 모델 카드

## 모델

Controller는 `[position, velocity]`에서 하나의 force command로 mapping하는 작은 PyTorch multilayer perceptron입니다. Output을 shift해 `u(0) = 0`을 강제합니다.

## 학습

Bounded region에서 state를 sample하고 공칭 LQR controller로 label을 만듭니다. Training은 imitation MSE와 weighted sampled Lyapunov penalty를 최소화합니다. Repository는 fixed random seed를 설정합니다.

## 의도된 사용

- Learning-based control 교육과 research prototyping.
- 포함된 simulation에서 LQR과의 reproducible comparison.
- Stability-aware objective와 robustness diagnostic 탐색.

## 범위 밖

- Safety-critical 또는 hardware 직접 deployment.
- Formal, global, distribution-free stability 주장.
- 검증된 state, actuator, plant range 밖 운용.

## 평가

Closed-loop trajectory, final norm, settling time, cost, control energy, maximum input, sampled `V_dot`, robustness scenario, estimated region of attraction.

Model 재사용 전에 [한계](limitations.md)와 [재현성](reproducibility.md)을 확인하십시오.
