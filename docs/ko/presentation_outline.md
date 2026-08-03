🌐 언어: [English](../en/presentation_outline.md) | [日本語](../ja/presentation_outline.md) | [한국어](../ko/presentation_outline.md) | [ไทย](../th/presentation_outline.md)

# 발표 구성

1. **동기:** Neural controller는 유연하지만 안정성과 robustness를 평가해야 함.
2. **Plant:** Position, velocity, force input이 있는 mass-spring-damper state-space model.
3. **Baseline:** LQR이 안정화 reference와 imitation target을 제공.
4. **Neural controller:** Zero-at-origin architecture, imitation loss, Lyapunov penalty.
5. **평가:** Trajectory, settling time, cost, control effort, sampled `V_dot`.
6. **Robustness:** Actuator saturation, measurement noise, parameter variation.
7. **State-space evidence:** Phase portrait, Lyapunov contour, region-of-attraction map.
8. **주요 결과:** Test setting에서 neural controller가 LQR을 가깝게 따르고 추적된 sampled Lyapunov violation fraction이 모두 zero.
9. **한계:** Simulated linear plant, finite grid, 선택된 uncertainty case, formal proof 없음.
10. **향후 연구:** Nonlinear system, formal verification, learned Lyapunov function, KAN, hardware validation.

수치 주장을 발표할 때 읽기 쉬운 caption이 있는 figure를 사용하고 seed와 tested region을 명시합니다.
