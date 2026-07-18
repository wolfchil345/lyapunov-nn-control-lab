# Results Interpretation Guide

This guide explains how to interpret the main outputs of the Lyapunov Neural-Network Control Lab.

## Controller comparison

The project compares a classical LQR controller with a neural-network controller trained to imitate LQR while also considering Lyapunov stability.

Good controller behavior usually means:

- the state moves toward the origin;
- the final state norm becomes small;
- the settling time is reasonable;
- the control input is not unnecessarily large;
- the Lyapunov derivative is mostly negative around the checked region.

## Important metrics

### `final_state_norm`
Measures how close the final state is to the target equilibrium. Smaller is better.

### `settling_time_s`
Measures how long the system takes to stay near the target. Smaller is usually better, but very aggressive control may increase energy usage.

### `quadratic_cost`
Measures the overall state error and control effort. Smaller usually indicates better control performance.

### `control_energy`
Measures how much control effort is used over time. Smaller means the controller is less aggressive.

### `max_abs_control`
Shows the largest absolute control input. This is useful for checking actuator saturation.

## Lyapunov checks

The Lyapunov derivative indicates whether the Lyapunov function decreases along system motion.

Negative values are generally good because they suggest that the system is moving toward a stable equilibrium.

Positive values in some grid regions may indicate possible instability, weak training, or regions outside the controller effectiveness area.

## Region of attraction

The region of attraction shows which initial states converge to the target equilibrium.

A larger convergent region usually means the controller is more reliable from different starting conditions.

## Robustness experiments

### Measurement noise
Noise robustness checks whether the controller still works when the measured state is imperfect.

### Parameter variation
Parameter robustness checks whether the controller still works when mass, damping, or stiffness changes.

### Actuator saturation
Saturation experiments check whether the controller remains effective when control force is limited.

## Ablation study

The stability-weight ablation changes the strength of the Lyapunov penalty during training.

A useful stability weight should balance imitation accuracy, convergence, and Lyapunov behavior.

## Practical reading order

1. Check `performance_metrics.csv`.
2. Open `position_comparison.png`.
3. Open `phase_portrait.png`.
4. Open `lyapunov_contours.png`.
5. Open `region_of_attraction_comparison.png`.
6. Read `experiment_report.md`.
