🌐 언어: [English](../en/experiment_parameters.md) | [日本語](../ja/experiment_parameters.md) | [한국어](../ko/experiment_parameters.md) | [ไทย](../th/experiment_parameters.md)

# 실험 Parameter

## Parameter 그룹

| 그룹 | 예 | 주요 위치 |
|---|---|---|
| Plant | mass, damping, stiffness | `src/system.py`, `src/parameter_variation.py` |
| Controller | `Q`, `R`, network size, saturation limit | `src/system.py`, `src/controllers.py`, `main.py` |
| Training | seed, epochs, learning rate, dataset size, loss weights | `src/controllers.py`, `main.py` |
| Simulation | initial state, duration, evaluation times | `src/simulation.py`, `main.py` |
| Stability | state range, grid density, decay margin | `src/lyapunov.py`, `main.py` |
| Robustness | noise, parameter cases, ablation weights | `src/noise.py`, `src/parameter_variation.py`, `src/stability_ablation.py` |

## 공정한 비교

한 번에 한 parameter 그룹만 바꿉니다. 변경 자체가 연구 질문이 아니라면 seed, initial state, simulation horizon, evaluation metric을 고정합니다.

새 reference result를 채택하기 전에 정확한 설정을 [실험 로그](experiment_log_template.md)에 기록하십시오.
