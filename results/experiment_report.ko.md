🌐 언어: [English](experiment_report.md) | [日本語](experiment_report.ja.md) | [한국어](experiment_report.ko.md) | [ไทย](experiment_report.th.md)

# 실험 보고서

이 보고서는 Lyapunov NN Control Lab에서 생성된 실험 결과를 요약합니다.

## 주요 실험

| 실험 | 출력 |
|---|---|
| 모델 구조 | `model_architecture.png` |
| LQR과 신경망 비교 | `position_comparison.png` |
| 안정성 중심 학습 손실 | `training_loss.png` |
| 여러 초기 조건 | `multiple_initial_conditions.png` |
| 구동기 포화 비교 | `saturation_comparison.png` |
| 측정 잡음 강건성 | `noise_robustness.png` |
| 매개변수 변화 강건성 | `parameter_robustness.png` |
| 위상도 | `phase_portrait.png` |
| Lyapunov 등고선 그림 | `lyapunov_contours.png` |
| 흡인 영역 지도 | `region_of_attraction.png` |
| 제어기별 흡인 영역 비교 | `region_of_attraction_comparison.png` |
| 안정성 가중치 제거 실험 | `stability_weight_ablation.png` |

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

## 성능 지표 미리보기

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

## 안정성 가중치 제거 실험 미리보기

| stability_weight | lyapunov_violation_fraction | final_state_norm | settling_time_s | quadratic_cost | control_energy |
| --- | --- | --- | --- | --- | --- |
| 0.0 | 0.0 | 2.56460257589076e-08 | 2.99 | 14.77627249722799 | 5.410421142108917 |
| 1.0 | 0.0 | 7.738160083800791e-10 | 2.5500000000000003 | 14.834420901355982 | 5.515590194940069 |
| 10.0 | 0.0 | 4.003802800566632e-09 | 2.0300000000000002 | 14.904517715156533 | 5.859179145902849 |
| 50.0 | 0.0 | 1.3967706048153224e-07 | 3.35 | 14.760553849458393 | 3.7422401939648555 |

## 해석 가이드

- `final_state_norm`이 작을수록 제어기가 상태를 평형점에 더 가깝게 만듭니다.
- `settling_time_s`가 짧을수록 제어기가 더 빠르게 안정화합니다.
- `control_energy`가 작을수록 필요한 제어 입력이 적습니다.
- `lyapunov_violation_fraction`이 작을수록 표본 상태에서 Lyapunov 감소 조건을 위반하는 점이 적습니다.
- 흡인 영역 결과는 선택한 설정에서 수렴하는 표본 초기 상태를 추정한 것입니다.
- 이 결과는 경험적 근거이며 형식적인 안정성 증명이 아닙니다.
