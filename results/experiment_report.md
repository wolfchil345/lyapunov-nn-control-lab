# Experiment Report

This report summarizes the generated results for the Lyapunov neural-network control lab.

## Main experiments

| Experiment | Output |
|---|---|
| Model architecture | `model_architecture.png` |
| LQR and neural-network comparison | `position_comparison.png` |
| Stability-aware training loss | `training_loss.png` |
| Multiple initial conditions | `multiple_initial_conditions.png` |
| Actuator saturation comparison | `saturation_comparison.png` |
| Measurement-noise robustness | `noise_robustness.png` |
| Parameter robustness | `parameter_robustness.png` |
| Phase portrait | `phase_portrait.png` |
| Lyapunov contour plot | `lyapunov_contours.png` |
| Region of attraction map | `region_of_attraction.png` |
| Region of attraction controller comparison | `region_of_attraction_comparison.png` |
| Stability-weight ablation study | `stability_weight_ablation.png` |

## Available plots

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

## Performance metrics preview

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

## Stability-weight ablation preview

| stability_weight | lyapunov_violation_fraction | final_state_norm | settling_time_s | quadratic_cost | control_energy |
| --- | --- | --- | --- | --- | --- |
| 0.0 | 0.0 | 2.56460257589076e-08 | 2.99 | 14.77627249722799 | 5.410421142108917 |
| 1.0 | 0.0 | 7.738160083800791e-10 | 2.5500000000000003 | 14.834420901355982 | 5.515590194940069 |
| 10.0 | 0.0 | 4.003802800566632e-09 | 2.0300000000000002 | 14.904517715156533 | 5.859179145902849 |
| 50.0 | 0.0 | 1.3967706048153224e-07 | 3.35 | 14.760553849458393 | 3.7422401939648555 |

## Interpretation guide

- Lower final state norm means the controller drives the state closer to the equilibrium.
- Lower settling time means the controller stabilizes faster.
- Lower control energy means the controller uses less actuation effort.
- Lower Lyapunov violation fraction means fewer sampled states violate the Lyapunov decrease condition.
- Region of attraction results estimate which initial states converge successfully.
