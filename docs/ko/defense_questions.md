🌐 언어: [English](../en/defense_questions.md) | [日本語](../ja/defense_questions.md) | [한국어](../ko/defense_questions.md) | [ไทย](../th/defense_questions.md)

# Defense Questions

이 문서는 Lyapunov Neural-Network Control Lab을 발표하거나 디펜스할 때 예상 가능한 질문과 답변 포인트를 정리합니다.

## Project motivation

### Why use a neural-network controller?
- neural network는 유연한 control policy를 근사할 수 있습니다.
- nonlinear systems에서는 고전적 controller design이 어려워질 수 있으며, 그럴 때 유용합니다.
- 이 project는 먼저 단순한 system에서 이를 연구합니다.

### Why compare with LQR?
- LQR은 linear systems에 대한 신뢰할 수 있는 고전적 baseline입니다.
- imitation learning을 위한 명확한 teacher controller를 제공합니다.
- LQR과 비교하면 neural controller를 더 쉽게 평가할 수 있습니다.

## Stability

### Why use Lyapunov-style checks?
- stability는 control engineering에서 중요합니다.
- Lyapunov analysis는 system의 energy-like behavior가 감소하는지 추론하는 방법을 제공합니다.
- 이 project는 grid-based checks를 empirical stability evidence로 사용합니다.

### Does this prove global stability?
- 아니요.
- grid check는 sampled states만 평가합니다.
- 분석을 지원하지만 완전한 수학적 증명은 아닙니다.

## Experiments

### Why use a mass-spring-damper system?
- 단순하고 이해하기 쉬우며 control education에서 흔히 사용됩니다.
- position과 velocity states를 가지므로 시각화가 쉽습니다.
- 더 어려운 nonlinear systems로 가기 전의 첫 testbed로 적합합니다.

### Why test robustness?
- 실제 systems에는 noise, actuator limits, parameter uncertainty가 존재합니다.
- robustness experiments는 선택된 불완전 조건에서도 controller가 동작하는지 보여줍니다.

## Neural-network training

### What does the neural network learn?
- state에서 control input으로의 mapping을 학습합니다.
- target control input은 LQR controller에서 생성됩니다.

### Why add a stability-aware penalty?
- 순수 imitation은 LQR 출력을 맞춰도 closed-loop simulation에서 나쁜 거동을 보일 수 있습니다.
- penalty는 sampled states 주변에서 더 나은 Lyapunov-style behavior를 유도합니다.

## Results interpretation

### Which metric is most important?
- 단일 metric만으로는 충분하지 않습니다.
- final normalized-state norm, normalized settling time, LQR-style cost, integrated squared control effort, Lyapunov behavior, robustness를 함께 해석해야 합니다.

### What result would be considered successful?
- neural controller가 원점 근처로 수렴해야 합니다.
- LQR에 가까운 성능을 보여야 합니다.
- 점검 영역에서 Lyapunov derivative 값이 대체로 음수여야 합니다.
- noise, saturation, parameter variation 하에서도 합리적이어야 합니다.

## Limitations

### What are the main limitations?
- plant가 단순합니다.
- simulations는 hardware experiments가 아닙니다.
- grid-based stability checks는 empirical입니다.
- neural network는 training region 밖에서 실패할 수 있습니다.

## Future work

### How can this become stronger research?
- nonlinear plants를 테스트한다.
- formal verification을 추가한다.
- KAN-based controllers와 비교한다.
- neural Lyapunov functions를 직접 학습한다.
- 더 현실적인 control problems에 적용한다.
