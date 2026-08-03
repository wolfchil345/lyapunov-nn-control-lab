🌐 언어: [English](../en/thesis_plan.md) | [日本語](../ja/thesis_plan.md) | [한국어](../ko/thesis_plan.md) | [ไทย](../th/thesis_plan.md)

# 졸업논문 계획

## 가제

기계 동역학 시스템을 위한 Lyapunov-aware 신경망 제어

## 목적

LQR teacher로 학습한 neural controller가 선택된 비이상 조건에서 유용한 closed-loop performance, sampled stability behavior, robustness를 유지하는지 평가합니다.

## 방법

1. State-space plant와 LQR baseline 도출.
2. Imitation loss와 stability-aware loss로 neural controller 학습.
3. Trajectory, cost, effort, settling time 비교.
4. Sampled Lyapunov behavior와 추정 region of attraction 평가.
5. Saturation, noise, parameter variation 시험.
6. Limitations와 reproducibility 문서화.

## 권장 장 구성

1. 서론과 관련 연구
2. System model과 LQR 설계
3. Neural controller 학습
4. 안정성과 robustness 평가
5. 결과와 논의
6. 한계, 결론, 향후 연구

현재 system은 simulation testbed입니다. Hardware validation과 formal verification은 향후 확장입니다.
