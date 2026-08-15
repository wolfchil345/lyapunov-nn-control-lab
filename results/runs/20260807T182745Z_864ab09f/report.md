# Experiment Report

This report summarizes the generated results for the Lyapunov neural-network control lab.

## Run provenance

- Run ID: `20260807T182745Z_864ab09f`
- Source commit: `864ab09f3310b56b0d9993696d9a1cb4d361861d`
- Git working tree dirty: `false`
- Generated at (UTC): `2026-08-07T18:27:45Z`
- Package version: `1.0.1`
- Configuration SHA-256: `644bc3677e599a5a98287c8bc27e0b46189ae919b1befe78d55f520d624b9e53`
- Manifest: [`manifest.json`](manifest.json)
- Stability-weight seeds: `[700, 701, 702]`
- Measurement-noise seeds: `[7, 8, 9]`
- Repeat count: `3`
- Pairing strategies: `['paired seeds across all stability weights', 'common random-number realizations across noise amplitudes']`
- Lyapunov decay margin: `0.05`
- Finite-horizon settings: `{'position_bounds': [-2.5, 2.5], 'velocity_bounds': [-2.5, 2.5], 'horizon': 8.0, 'convergence_tolerance': 0.1, 'single_grid_resolution': 15, 'comparison_grid_resolution': 11}`

## Main experiments

| Experiment | Output |
|---|---|
| Model architecture | `model_architecture.png` |
| LQR and neural-network comparison | `position_comparison.png` |
| Stability-aware training loss | `training_loss.png` |
| Multiple initial conditions | `multiple_initial_conditions.png` |
| Actuator saturation comparison | `saturation_comparison.png` |
| Measurement-noise robustness | `noise_robustness_paired.png` |
| Parameter robustness | `parameter_robustness.png` |
| Phase portrait | `phase_portrait.png` |
| Lyapunov contour plot | `lyapunov_contours.png` |
| Finite-horizon convergence map | `finite_horizon_convergence.png` |
| Finite-horizon convergence comparison | `finite_horizon_convergence_comparison.png` |
| Stability-weight ablation study | `stability_weight_ablation_paired.png` |

## Available plots

- [`model_architecture.png`](model_architecture.png)
- [`position_comparison.png`](position_comparison.png)
- [`training_loss.png`](training_loss.png)
- [`multiple_initial_conditions.png`](multiple_initial_conditions.png)
- [`saturation_comparison.png`](saturation_comparison.png)
- [`noise_robustness_paired.png`](noise_robustness_paired.png)
- [`noise_robustness_paired_trajectories.png`](noise_robustness_paired_trajectories.png)
- [`parameter_robustness.png`](parameter_robustness.png)
- [`phase_portrait.png`](phase_portrait.png)
- [`lyapunov_contours.png`](lyapunov_contours.png)
- [`finite_horizon_convergence.png`](finite_horizon_convergence.png)
- [`finite_horizon_convergence_comparison.png`](finite_horizon_convergence_comparison.png)
- [`stability_weight_ablation_paired.png`](stability_weight_ablation_paired.png)

## Experimental seed design

| Experiment | Base seed | Explicit seeds | Repeats | Pairing strategy |
|---|---:|---|---:|---|
| Stability-weight ablation | 700 | 700;701;702 | 3 | paired seeds across all stability weights |
| Measurement-noise robustness | 7 | 7;8;9 | 3 | common random-number realizations across noise amplitudes |

Fixed seeds support repeatable paired CPU comparisons under the same environment; they do not guarantee fully deterministic execution on every accelerator or platform.

## Finite-horizon convergence sampling

A sampled state is classified as converged only when the strict final-state criterion `||x(T)||_2 < tolerance` holds in normalized coordinates. This finite-time result depends on the horizon, tolerance, and grid; it is not an asymptotic attraction-region certificate.

| Controller | Horizon (normalized time) | Normalized-state tolerance | Normalized-position bounds | Normalized-velocity bounds | Grid | Converged / tested | Fraction |
|---|---:|---:|---|---|---:|---:|---:|
| LQR | 8 | 0.1 | (-2.5, 2.5) | (-2.5, 2.5) | 11 x 11 | 121 / 121 | 100.0% |
| Neural network | 8 | 0.1 | (-2.5, 2.5) | (-2.5, 2.5) | 11 x 11 | 121 / 121 | 100.0% |
| Saturated NN | 8 | 0.1 | (-2.5, 2.5) | (-2.5, 2.5) | 11 x 11 | 121 / 121 | 100.0% |

## Performance metrics preview

| controller | initial_position | initial_velocity | final_state_norm | settling_time | quadratic_cost | integrated_squared_control_effort | max_abs_control |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LQR | 1.5 | 0.0 | 3.3512211263852907e-06 | 3.37 | 14.648088325259712 | 4.456642635355885 | 4.348469228349529 |
| LQR | -1.5 | 0.0 | 3.3512211263852907e-06 | 3.37 | 14.648088325259712 | 4.456642635355885 | 4.348469228349529 |
| LQR | 1.0 | 1.5 | 3.0970423618290686e-06 | 3.5 | 13.582997380405825 | 7.576846237440819 | 6.530457677055536 |
| LQR | -1.0 | -1.5 | 3.0970423618290686e-06 | 3.5 | 13.582997380405825 | 7.576846237440819 | 6.530457677055536 |
| LQR | 0.5 | -2.0 | 5.018394958296524e-07 | 2.56 | 3.5708128507878527 | 4.151303514719733 | 3.392481179202401 |
| Neural network | 1.5 | 0.0 | 2.7936295959393497e-07 | 3.25 | 14.680261436766918 | 4.733569645274229 | 4.450384616851807 |
| Neural network | -1.5 | 0.0 | 2.652795540386125e-07 | 3.2600000000000002 | 14.674752257886176 | 4.693609298382431 | 4.505607604980469 |
| Neural network | 1.0 | 1.5 | 1.8067063453035617e-07 | 3.34 | 13.625494208697683 | 8.35334429655788 | 6.9777679443359375 |

## Stability-weight ablation preview

| stability_weight | decay_margin | derivative_violation_fraction | decay_margin_violation_fraction | max_vdot | max_decay_residual | final_state_norm | settling_time | quadratic_cost | integrated_squared_control_effort |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.0 | 0.05 | 0.0 | 0.0 | -0.03204738331856237 | -0.031641133318562366 | 1.2122031527062004e-08 | 2.99 | 14.776272435128401 | 5.410421045046052 |
| 0.0 | 0.05 | 0.0 | 0.0 | -0.032489173143964566 | -0.03208292314396456 | 1.0900595181635867e-08 | 2.87 | 14.782773201358243 | 5.251558294415672 |
| 0.0 | 0.05 | 0.0 | 0.0 | -0.03235575373930921 | -0.03194950373930921 | 1.9476724176486353e-08 | 2.89 | 14.7717855272946 | 5.22392519677272 |
| 1.0 | 0.05 | 0.0 | 0.0 | -0.03206120044709142 | -0.03165495044709142 | 2.021903802446474e-08 | 2.88 | 14.819042252803364 | 5.5973176854465745 |
| 1.0 | 0.05 | 0.0 | 0.0 | -0.03273720963424298 | -0.03233095963424298 | 5.967745336427627e-09 | 2.5500000000000003 | 14.834420908021619 | 5.51559010362884 |
| 1.0 | 0.05 | 0.0 | 0.0 | -0.03246681441857056 | -0.03206056441857055 | 1.311097801993414e-08 | 2.63 | 14.829099883310322 | 5.500510283291822 |
| 10.0 | 0.05 | 0.0 | 0.0 | -0.03213438934167357 | -0.031728139341673574 | 7.975140887557462e-09 | 2.13 | 14.996997064650204 | 6.071697544422928 |
| 10.0 | 0.05 | 0.0 | 0.0 | -0.0327650029786119 | -0.0323587529786119 | 6.792823680946157e-09 | 2.12 | 14.970938807081808 | 6.028176094425327 |

## Interpretation guide

- The final normalized-state norm is the Euclidean norm of normalized position and velocity.
- Settling time is measured in normalized time and requires all later samples to remain inside the tolerance.
- Integrated squared control effort is the integral of normalized control squared; it is not physical energy.
- The derivative violation fraction counts sampled states with V-dot above numerical tolerance.
- The decay-margin violation fraction counts sampled states where V-dot + alpha ||x||_2^2 exceeds numerical tolerance.
- Both Lyapunov metrics cover only the finite sampled grid and are not a formal continuous-state certificate.
- Finite-horizon convergence percentages report only the sampled states that meet the stated normalized Euclidean final-state tolerance after the stated normalized-time horizon.
