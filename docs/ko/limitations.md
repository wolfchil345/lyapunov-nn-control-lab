🌐 언어: [English](../en/limitations.md) | [日本語](../ja/limitations.md) | [한국어](../ko/limitations.md) | [ไทย](../th/limitations.md)

# 한계

## 모델과 데이터

- Plant는 simulated linear mass-spring-damper system입니다.
- Training state는 bounded region을 다루고 LQR teacher를 사용합니다.
- Nonlinear plant나 unseen state에 대한 generalization을 보장하지 않습니다.

## 안정성 근거

- Quadratic Lyapunov function은 공칭 LQR 설계에서 얻습니다.
- `V_dot`와 region-of-attraction 평가는 finite grid, threshold, simulation horizon을 사용합니다.
- Zero sampled violation은 formal 또는 global proof가 아닙니다.

## 강건성 근거

- Actuator limit, noise level, parameter variation은 선택 scenario이며 포괄적 uncertainty set이 아닙니다.
- Numerical solver와 dependency version이 작은 차이를 만들 수 있습니다.
- Hardware, delay, quantization, fault, adversarial test가 포함되지 않습니다.

## 책임 있는 사용

이 repository는 교육 연구 software이며 안전 인증 controller가 아닙니다. 물리 equipment에 적용하기 전에 독립적으로 검증하십시오.

향후 연구에는 nonlinear plant, formal verification, learned Lyapunov function, 더 넓은 uncertainty analysis, hardware validation이 있습니다.
