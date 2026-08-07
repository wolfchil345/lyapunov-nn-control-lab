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

## Sampled Lyapunov checks

The project uses the quadratic function and its closed-loop derivative:

```text
V(x) = x^T P x
V-dot(x) = 2 x^T P (A x + B pi(x))
```

Two metrics answer different questions:

- `derivative_violation_fraction` counts sampled nonzero states where `V-dot`
  exceeds the numerical tolerance.
- `decay_margin_violation_fraction` counts sampled nonzero states where
  `V-dot + alpha * ||x||^2` exceeds the numerical tolerance.

The second condition is stronger when `alpha > 0`. Training and evaluation use
the same default `alpha = 0.05`. The default numerical tolerance is `1e-9`; it only handles
floating-point noise and must not be interpreted as part of the scientific
decay margin.

The exact origin is excluded because `V(0) = V-dot(0) = 0`; every other grid
point is included. Both fractions describe only the finite sampled grid. Neither
is a formal certificate over the continuous state space.

## Finite-horizon convergence map

For each initial state on a finite grid, the evaluator simulates to a stated
horizon `T` and classifies the state only when the strict final-state criterion
`||x(T)|| < epsilon` holds. Interpret a reported percentage together with `T`,
`epsilon`, the state bounds, grid resolution, and tested/converged counts.

A larger percentage means that more of the sampled states met that specific
finite-time criterion. It does not establish asymptotic convergence, a stable
region, or a mathematical attraction basin. A slowly converging state may fail
at `T` even if it converges later.

This map is also distinct from the sampled Lyapunov checks above. Neither test
is a formal continuous-state attraction-region certificate.

## Robustness experiments

### Measurement noise
Noise robustness checks whether the controller still works when the measured state is imperfect.

### Parameter variation
Parameter robustness checks whether the controller still works when mass, damping, or stiffness changes.

### Actuator saturation
Saturation experiments check whether the controller remains effective when control force is limited.

## Ablation study

The stability-weight ablation changes the multiplier applied to the Lyapunov
penalty during training while keeping the reported decay margin explicit.

A useful stability weight should balance imitation accuracy, convergence, and
both sampled Lyapunov metrics. The committed
`results/stability_weight_ablation.csv` uses the historical ambiguous violation
column and is intentionally not overwritten here. Its regenerated schema will
include both violation fractions in the later result-provenance operation.

## Practical reading order

1. Check `performance_metrics.csv`.
2. Open `position_comparison.png`.
3. Open `phase_portrait.png`.
4. Open `lyapunov_contours.png`.
5. Open `finite_horizon_convergence_comparison.png` after a new run. The
   tracked `region_of_attraction_comparison.png` is the historical pre-migration
   artifact.
6. Read `experiment_report.md`.
