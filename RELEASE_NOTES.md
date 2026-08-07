# v1.0.1 - Documentation and Release Polish

This patch release improves installation reliability, multilingual documentation, and result-summary reporting without changing the core control experiments.

## Highlights

- add the missing `python-control` runtime dependency
- ignore generated virtual-environment and package-metadata files
- add English, Japanese, Korean, and Thai documentation foundations
- add localized documentation indexes for all four languages
- update each README to link to its localized documentation index
- remove obsolete and nonexistent documentation links
- fix the ablation summary to read `lyapunov_violation_fraction`
- generalize the release checklist for future version tags

## Validation

- 57 tests pass
- quick-start example passes
- quality gate passes
- experiment results regenerate successfully with fixed random seeds
- regenerated result figures are pixel-identical to the previous tracked figures
- Lyapunov grid checks report zero violations
- the historical finite-horizon checks report 100% final-state tolerance
  satisfaction for the tested controllers and settings; they are not a
  mathematical attraction-region certificate

## Compatibility

The core simulation, controller architecture, and tracked experimental results remain unchanged from `v1.0.0`.

---

# v1.0.0 - First Complete Release

This is the first complete release of the Lyapunov Neural-Network Control Lab.

## Highlights

- LQR baseline controller
- neural-network controller trained by imitation learning
- Lyapunov-inspired stability checks
- stability-aware training penalty
- actuator saturation experiment
- measurement-noise robustness experiment
- parameter robustness experiment
- phase portrait visualization
- Lyapunov contour visualization
- sampled finite-horizon convergence mapping (described with legacy
  terminology in the original release)
- finite-horizon controller comparison (described with legacy terminology in
  the original release)
- stability-weight ablation study
- automatic experiment report generation
- model architecture diagram
- methodology documentation
- project summary documentation
- citation metadata

## Main outputs

- `results/model_architecture.png`
- `results/position_comparison.png`
- `results/training_loss.png`
- `results/saturation_comparison.png`
- `results/noise_robustness.png`
- `results/parameter_robustness.png`
- `results/phase_portrait.png`
- `results/lyapunov_contours.png`
- `results/region_of_attraction.png`
- `results/region_of_attraction_comparison.png`
- `results/stability_weight_ablation.png`
- `results/experiment_report.md`

## Research focus

This project studies whether a neural-network controller can imitate an LQR
reference while being evaluated using transient, robustness, and sampled
Lyapunov diagnostics. The nominal uncontrolled plant is already asymptotically
stable.
