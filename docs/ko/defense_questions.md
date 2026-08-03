🌐 언어: [English](../en/defense_questions.md) | [日本語](../ja/defense_questions.md) | [한국어](../ko/defense_questions.md) | [ไทย](../th/defense_questions.md)

# 발표 및 심사 질문

## 동기와 설계

**왜 LQR을 사용하는가?** 투명한 안정화 baseline이며 선형 공칭 plant에 신뢰할 수 있는 imitation target을 제공하기 때문입니다.

**Network는 무엇을 배우는가?** Position과 velocity에서 scalar control force로 가는 mapping입니다.

**왜 `u(0) = 0`을 강제하는가?** 목표에서 nonzero command가 의도한 equilibrium을 깨뜨릴 수 있기 때문입니다.

## 안정성

**Grid check가 global stability를 증명하는가?** 아닙니다. 하나의 Lyapunov candidate로 유한한 sampled state를 평가합니다.

**왜 Lyapunov penalty를 사용하는가?** Imitation error만으로 closed-loop decay를 직접 측정할 수 없습니다. Penalty는 학습 중 sampled decay condition을 유도합니다.

## 평가

**어떤 metric이 가장 중요한가?** 하나만으로 결정할 수 없습니다. Convergence, cost, effort, sampled stability, robustness를 함께 해석합니다.

**왜 saturation, noise, parameter variation을 시험하는가?** 실제 제어기는 입력 제한, sensor 오차, model mismatch를 겪기 때문입니다.

## 한계와 다음 연구

Plant는 단순하고 모든 근거는 simulation이며 training region 밖의 거동은 불확실합니다. Nonlinear plant, formal verification, hardware experiment, KAN 같은 대체 architecture가 강화 방향입니다.
