🌐 Language: [English](../en/results_interpretation.md) | [日本語](../ja/results_interpretation.md) | [한국어](../ko/results_interpretation.md) | [ไทย](../th/results_interpretation.md)

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

All state magnitudes below use `||x||_2 = sqrt(q^2 + v^2)` in normalized,
dimensionless coordinates. Time and control input are normalized as well.

### `final_state_norm`
Measures the Euclidean normalized-state distance from the target equilibrium. Smaller is better.

### `settling_time`
The canonical metric is `settling_time`: the first sampled normalized time after
the last sample outside `||x||_2 <= 0.02`. Thus all later samples remain inside
the closed tolerance set. `settling_time_s` is a historical compatibility alias
and does not mean seconds.

### `quadratic_cost`
Integrates `x^T Q x + u^T R u` over normalized time. `Q` and `R` are
dimensionless objective weights, so this is not physical energy.

### `integrated_squared_control_effort`
Integrates `u^2` over normalized time. Smaller means the controller is less
aggressive, but the value is not physical energy. `control_energy` is retained
as a historical compatibility alias.

### `max_abs_control`
Shows the largest absolute normalized control input. This is useful for checking saturation.

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
	`V-dot + alpha * ||x||_2^2` exceeds the numerical tolerance.

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
`||x(T)||_2 < epsilon` holds. `T` is a normalized-time horizon and `epsilon`
is a normalized-state Euclidean tolerance. Interpret a reported percentage together with `T`,
`epsilon`, the state bounds, grid resolution, and tested/converged counts.

A larger percentage means that more of the sampled states met that specific
finite-time criterion. It does not establish asymptotic convergence, a stable
region, or a mathematical attraction basin. A slowly converging state may fail
at `T` even if it converges later.

This map is also distinct from the sampled Lyapunov checks above. Neither test
is a formal continuous-state attraction-region certificate.

## Robustness experiments

### Measurement noise
Noise robustness applies the same scalar Gaussian standard deviation
independently to normalized `q` and `v` measurements.

Future runs pair every noise amplitude by seed using common random numbers.
For a fixed seed, the same standardized Gaussian sequence is scaled by each
amplitude. Interpret the raw `noise_std x seed` rows before the aggregate mean,
sample standard deviation, and standard error. This pairing reduces one source
of random-realization confounding; it does not remove all uncertainty.

### Parameter variation
Parameter robustness checks whether the controller still works when normalized
mass, damping, or stiffness coefficients change.

### Actuator saturation
Saturation experiments check whether the controller remains effective when normalized control input is limited.

## Ablation study

The stability-weight ablation changes the multiplier applied to the Lyapunov
penalty during training while keeping the reported decay margin explicit.

Future runs use the same repeated seed set for every weight. The raw table has
one row per `stability_weight x seed`; the aggregate table reports `n`, mean,
sample standard deviation, and standard error by weight. Mean plus or minus
sample standard deviation is a variability summary, not a confidence interval.

A useful stability weight should balance imitation accuracy, convergence, and
both sampled Lyapunov metrics. The committed
`results/stability_weight_ablation.csv` uses the historical ambiguous violation
column and is intentionally not overwritten here. Its regenerated schema will
not be retroactively relabelled. New paired files use the corrected sampled
derivative and sampled decay-margin violation names.

## Practical reading order

1. Check `performance_metrics.csv`.
2. Open `position_comparison.png`.
3. Open `phase_portrait.png`.
4. Open `lyapunov_contours.png`.
5. Open `finite_horizon_convergence_comparison.png` after a new run. The
	 tracked `region_of_attraction_comparison.png` is the historical pre-migration
	 artifact.
6. Read `experiment_report.md`.
