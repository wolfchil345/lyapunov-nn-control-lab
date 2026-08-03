🌐 Language: [English](../en/result_review_checklist.md) | [日本語](../ja/result_review_checklist.md) | [한국어](../ko/result_review_checklist.md) | [ไทย](../th/result_review_checklist.md)

# Result Review Checklist

## Settings

- [ ] Branch, commit, seed, epochs, and model architecture are recorded.
- [ ] Initial conditions, duration, grid density, noise, and parameter cases are recorded.
- [ ] Compared runs differ only in the intended variables.

## Outputs

- [ ] Expected CSV, report, model, and figure files exist.
- [ ] Figures have readable labels and show plausible trajectories.
- [ ] Metrics are finite and interpreted together.
- [ ] Saturation, noise, and parameter cases are clearly labeled.

## Stability claims

- [ ] Sampled Lyapunov checks are described as empirical evidence.
- [ ] Region-of-attraction claims state the tested grid, horizon, and threshold.
- [ ] Failure cases and unexpected behavior are retained and explained.

## Before commit

- [ ] `make quality-gate` passes.
- [ ] `git diff` contains only intentional artifacts.
- [ ] Documentation and the experiment log match the generated results.
