🌐 언어: [English](../en/experiment_parameters.md) | [日本語](../ja/experiment_parameters.md) | [한국어](../ko/experiment_parameters.md) | [ไทย](../th/experiment_parameters.md)

# 실험 매개변수

## 매개변수 그룹

| 그룹 | 예 | 주요 위치 |
|---|---|---|
| 플랜트 | 질량, 감쇠 계수, 스프링 상수 | `src/system.py`, `src/parameter_variation.py` |
| 제어기 | `Q`, `R`, 네트워크 크기, 포화 제한 | `src/system.py`, `src/controllers.py`, `main.py` |
| 학습 | 시드, 에포크 수, 학습률, 데이터셋 크기, 손실 가중치 | `src/controllers.py`, `main.py` |
| 시뮬레이션 | 초기 상태, 시뮬레이션 시간, 평가 시점 | `src/simulation.py`, `main.py` |
| 안정성 | 상태 범위, 격자 밀도, 감소 여유 | `src/lyapunov.py`, `main.py` |
| 강인성 | 잡음, 매개변수 사례, 제거 실험 가중치 | `src/noise.py`, `src/parameter_variation.py`, `src/stability_ablation.py` |

## 공정한 비교

한 번에 한 매개변수 그룹만 바꿉니다. 변경 자체가 연구 질문이 아니라면 시드, 초기 상태, 시뮬레이션 평가 시간, 평가 지표을 고정합니다.

새 참조 결과를 채택하기 전에 정확한 설정을 [실험 로그](experiment_log_template.md)에 기록하십시오.
