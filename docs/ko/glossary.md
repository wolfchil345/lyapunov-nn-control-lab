🌐 언어: [English](../en/glossary.md) | [日本語](../ja/glossary.md) | [한국어](../ko/glossary.md) | [ไทย](../th/glossary.md)

# 용어집

- **State(상태)**: 시스템을 설명하는 변수. 여기서는 위치와 속도.
- **Plant(플랜트)**: 제어되는 물리 또는 simulation system.
- **Control input(제어 입력)**: Plant에 적용하는 force command `u`.
- **Closed loop(폐루프)**: State feedback으로 연결된 controller와 plant.
- **LQR**: Linear Quadratic Regulator. 고전적 baseline이자 teacher.
- **Equilibrium(평형점)**: 변하지 않는 상태. 목표는 원점.
- **Lyapunov function**: 안정성을 연구하는 양의 energy-like function.
- **Lyapunov derivative**: 궤적을 따른 변화율 `V_dot`.
- **Actuator saturation**: 가능한 control input의 한계.
- **Region of attraction**: 명시된 조건에서 평형점으로 수렴하는 initial state 집합.
- **Imitation learning**: Teacher action을 재현하도록 model을 학습하는 방법.
- **Stability-aware training**: 표본 Lyapunov penalty를 포함한 학습.
- **Ablation study**: 한 설계 요소만 바꾸는 비교.

Code identifier와 수학 기호는 모든 번역에서 영어로 유지합니다.
