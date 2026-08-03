🌐 Language: [English](../en/results_interpretation.md) | [日本語](../ja/results_interpretation.md) | [한국어](../ko/results_interpretation.md) | [ไทย](../th/results_interpretation.md)

# Results Interpretation

## Performance metrics

- `final_state_norm`: distance from the target equilibrium at the final time.
- `settling_time_s`: first time after which the state remains within the threshold.
- `quadratic_cost`: integrated LQR-style state and control penalty.
- `control_energy`: integrated squared control input.
- `max_abs_control`: largest absolute actuator command.

No single metric establishes stability or controller quality. Compare convergence, effort, cost, and robustness together.

## Stability evidence

A negative sampled `V_dot` supports local decay within the evaluated grid. It does not prove behavior between grid points, outside the region, or under untested uncertainty.

## Robustness and region of attraction

Noise, parameter variation, and actuator saturation are scenario tests. Region-of-attraction maps classify only the sampled initial conditions under the selected horizon and threshold.

## Reading order

1. Confirm settings and seed.
2. Inspect trajectories and control limits.
3. Compare quantitative metrics.
4. Review Lyapunov and region-of-attraction diagnostics.
5. Read [limitations](limitations.md) and record failure cases.
