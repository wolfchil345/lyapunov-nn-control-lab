🌐 언어: [English](experiment_report.md) | [日本語](experiment_report.ja.md) | [한국어](experiment_report.ko.md) | [ไทย](experiment_report.th.md)

# 실험 보고서

이 보고서는 Lyapunov neural-network control lab에서 생성된 결과를 요약합니다.

## 주요 실험

| 실험 | 출력 |
|---|---|
| Model architecture | `model_architecture.png` |
| LQR과 neural-network 비교 | `position_comparison.png` |
| Stability-aware training loss | `training_loss.png` |
| 여러 initial condition | `multiple_initial_conditions.png` |
| Actuator saturation 비교 | `saturation_comparison.png` |
| Measurement-noise robustness | `noise_robustness.png` |
| Parameter robustness | `parameter_robustness.png` |
| Phase portrait | `phase_portrait.png` |
| Lyapunov contour plot | `lyapunov_contours.png` |
| Region of attraction map | `region_of_attraction.png` |
| Region of attraction controller comparison | `region_of_attraction_comparison.png` |
| Stability-weight ablation study | `stability_weight_ablation.png` |

## 사용 가능한 그림

- [`model_architecture.png`](model_architecture.png)
- [`position_comparison.png`](position_comparison.png)
- [`training_loss.png`](training_loss.png)
- [`multiple_initial_conditions.png`](multiple_initial_conditions.png)
- [`saturation_comparison.png`](saturation_comparison.png)
- [`noise_robustness.png`](noise_robustness.png)
- [`parameter_robustness.png`](parameter_robustness.png)
- [`phase_portrait.png`](phase_portrait.png)
- [`lyapunov_contours.png`](lyapunov_contours.png)
- [`region_of_attraction.png`](region_of_attraction.png)
- [`region_of_attraction_comparison.png`](region_of_attraction_comparison.png)
- [`stability_weight_ablation.png`](stability_weight_ablation.png)

## 성능 지표 preview

| controller | initial_position | initial_velocity | final_state_norm | settling_time_s | quadratic_cost | control_energy | max_abs_control |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LQR | 1.5 | 0.0 | 3.3512211263851475e-06 | 3.37 | 14.648088325259708 | 4.456642635355886 | 4.348469228349534 |
| LQR | -1.5 | 0.0 | 3.3512211263851475e-06 | 3.37 | 14.648088325259708 | 4.456642635355886 | 4.348469228349534 |
| LQR | 1.0 | 1.5 | 3.097042361828861e-06 | 3.5 | 13.582997380405825 | 7.576846237440828 | 6.530457677055545 |
| LQR | -1.0 | -1.5 | 3.097042361828861e-06 | 3.5 | 13.582997380405825 | 7.576846237440828 | 6.530457677055545 |
| LQR | 0.5 | -2.0 | 5.018394958296208e-07 | 2.56 | 3.5708128507878527 | 4.151303514719738 | 3.3924811792024077 |
| Neural network | 1.5 | 0.0 | 2.7497692462658866e-07 | 3.25 | 14.680261467448672 | 4.733569667999773 | 4.450384140014648 |
| Neural network | -1.5 | 0.0 | 2.845442886644117e-07 | 3.2600000000000002 | 14.674752308656242 | 4.693609391104969 | 4.505607604980469 |
| Neural network | 1.0 | 1.5 | 1.8043428851131705e-07 | 3.34 | 13.62549419698057 | 8.353344458862482 | 6.977767467498779 |

## 안정성 가중치 ablation preview

| stability_weight | lyapunov_violation_fraction | final_state_norm | settling_time_s | quadratic_cost | control_energy |
| --- | --- | --- | --- | --- | --- |
| 0.0 | 0.0 | 2.56460257589076e-08 | 2.99 | 14.77627249722799 | 5.410421142108917 |
| 1.0 | 0.0 | 7.738160083800791e-10 | 2.5500000000000003 | 14.834420901355982 | 5.515590194940069 |
| 10.0 | 0.0 | 4.003802800566632e-09 | 2.0300000000000002 | 14.904517715156533 | 5.859179145902849 |
| 50.0 | 0.0 | 1.3967706048153224e-07 | 3.35 | 14.760553849458393 | 3.7422401939648555 |

## 해석 가이드

- Final state norm이 작을수록 controller가 state를 equilibrium에 더 가깝게 만듭니다.
- Settling time이 짧을수록 controller가 더 빠르게 안정화합니다.
- Control energy가 작을수록 actuation effort가 적습니다.
- Lyapunov violation fraction이 작을수록 sampled state에서 감소 조건 위반이 적습니다.
- Region of attraction result는 선택 setting에서 수렴하는 sampled initial state를 추정합니다.
- 이 sampled result는 경험적 근거이며 형식적 안정성 증명이 아닙니다.
