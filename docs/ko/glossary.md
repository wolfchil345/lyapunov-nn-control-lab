🌐 언어: [English](../en/glossary.md) | [日本語](../ja/glossary.md) | [한국어](../ko/glossary.md) | [ไทย](../th/glossary.md)

# 용어집

- **상태(State)**: 시스템을 설명하는 변수. 이 프로젝트에서는 위치와 속도입니다.
- **플랜트(Plant)**: 제어 대상이 되는 물리 또는 시뮬레이션 시스템입니다.
- **제어 입력(Control input)**: 플랜트에 적용하는 힘 명령 `u`입니다.
- **폐루프(Closed loop)**: 상태 피드백을 통해 제어기와 플랜트가 연결된 구성입니다.
- **LQR**: 선형 이차 조절기(Linear Quadratic Regulator). 고전적인 기준 제어기이자 학습 교사입니다.
- **평형점(Equilibrium)**: 시간이 지나도 변하지 않는 상태. 이 프로젝트의 목표는 원점입니다.
- **Lyapunov 함수**: 안정성 분석에 사용하는 양의 에너지 형태 함수입니다.
- **Lyapunov 도함수**: 깤적을 따라 변하는 Lyapunov 함수의 속도 `V_dot`입니다.
- **구동기 포화(Actuator saturation)**: 제어 입력이 달성할 수 있는 크기에 제한이 있는 현상입니다.
- **흡인 영역(Region of attraction)**: 정해진 조건에서 평형점으로 수렴하는 초기 상태의 집합입니다.
- **모방 학습(Imitation learning)**: 교사의 행동을 재현하도록 모델을 학습하는 방법입니다.
- **안정성 고려 학습(Stability-aware training)**: 표본 기반 Lyapunov 패널티를 포함하는 학습입니다.
- **제거 실험(Ablation study)**: 하나의 설계 선택만 변경하여 영향을 비교하는 실험입니다.

코드 식별자와 수학 기호는 모든 번역본에서 영어 표기를 유지합니다.
