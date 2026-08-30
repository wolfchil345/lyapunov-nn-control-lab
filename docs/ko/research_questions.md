🌐 언어: [English](../en/research_questions.md) | [日本語](../ja/research_questions.md) | [한국어](../ko/research_questions.md) | [ไทย](../th/research_questions.md)

# 연구 질문

이 문서는 Lyapunov Neural-Network Control Lab에서 가능한 연구 질문을 요약합니다.

## 핵심 연구 질문

neural-network 제어기는 폐루프 시뮬레이션에서 유용한 Lyapunov-style 안정 거동을 유지하면서 LQR 제어기를 모방할 수 있는가?

## 제어 성능

- neural-network 제어기 성능은 LQR baseline에 얼마나 가까운가?
- neural-network 제어기는 final normalized-state norm을 신뢰성 있게 줄이는가?
- normalized settling time, quadratic LQR-style cost, integrated squared control effort는 제어기 간에 어떻게 비교되는가?

## 안정 거동

- Lyapunov derivative는 점검 영역에서 대부분 음수를 유지하는가?
- 어떤 샘플 초기 상태가 정해진 finite horizon 이후 stated final-state tolerance를 만족하는가?
- 해당 finite-horizon 비율은 horizon, tolerance, bounds, grid resolution에 얼마나 민감한가?

## 강건성 거동

- measurement noise는 neural-network 제어기에 어떤 영향을 주는가?
- actuator saturation은 수렴에 어떤 영향을 주는가?
- normalized mass, damping, stiffness 계수 변화에 제어기가 얼마나 민감한가?

## 학습 설계

- stability penalty weight는 모방 정확도에 어떤 영향을 주는가?
- stability penalty weight는 Lyapunov derivative violations에 어떤 영향을 주는가?
- imitation loss와 stability-aware behavior 사이에 유용한 trade-off가 있는가?

## KAN 확장 연구 질문

- KAN 제어기는 표준 neural network만큼 혹은 그 이상으로 LQR을 모방할 수 있는가?
- KAN 제어기는 더 매끄럽거나 더 해석 가능한 제어 거동을 만드는가?
- 동일한 sampling settings에서 KAN 제어기가 robustness 또는 finite-horizon convergence 결과를 개선하는가?

## 가능한 논문 방향

가능한 졸업 연구 방향은, 동일한 Lyapunov-style 평가 파이프라인으로 표준 neural-network 제어기와 KAN-based 제어기를 비교하는 것입니다.

## 권장 평가 요약

각 제어기별 보고 항목:

- performance metrics
- Lyapunov grid-check results
- robustness results
- finite-horizon convergence 개수, 비율, sampling metadata
- limitations and failure cases
