🌐 언어: [English](../en/research_questions.md) | [日本語](../ja/research_questions.md) | [한국어](../ko/research_questions.md) | [ไทย](../th/research_questions.md)

# 연구 질문

## 주요 질문

신경망 제어기가 안정화 LQR policy를 모방하면서 폐루프 simulation에서 유리한 표본 Lyapunov 거동과 robustness를 유지할 수 있는가?

## 성능과 안정성

- Settling time, quadratic cost, control effort가 LQR에 얼마나 가까운가?
- 표본 `V_dot`가 어디에서 음이 아니며 training penalty가 이를 어떻게 바꾸는가?
- 추정 region of attraction이 LQR, neural, saturated controller 사이에서 어떻게 달라지는가?

## 강건성

- Measurement noise, actuator saturation, plant uncertainty가 수렴에 어떤 영향을 주는가?
- 어떤 test case가 먼저 실패하며 training region 안인가 밖인가?

## 학습과 아키텍처

- Imitation accuracy와 stability-loss weight 사이의 trade-off는 무엇인가?
- KAN controller가 smoothness, interpretability, robustness, region-of-attraction result를 바꾸는가?

답을 보고할 때 sampled region, threshold, seed, limitations를 명시합니다.
