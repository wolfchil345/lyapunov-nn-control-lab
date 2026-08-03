# Result Review Checklist

Use this checklist before using generated result files in a report, presentation, thesis chapter, or portfolio.

## 1. Confirm the experiment settings

- The controller type is clear.
- The random seed is recorded.
- The number of epochs is recorded.
- The grid size for Lyapunov or region-of-attraction checks is recorded.
- Noise or parameter variation settings are recorded.

## 2. Confirm the generated files

Run:

```bash
python scripts/list_results.py
```

Check that important files have clear names and are connected to the correct experiment.

## 3. Review plots

- Trajectories move toward the origin when stability is expected.
- Control signals do not show strange spikes unless explained.
- Comparison plots clearly label LQR, neural network, and other controllers.
- Figures are readable enough for slides or reports.

## 4. Review metrics

- Metrics are compared only between experiments with compatible settings.
- Lower cost or error is not treated as proof of stability by itself.
- Control effort is considered together with tracking or stabilization quality.

## 5. Review Lyapunov-related outputs

- Grid-based checks are described as sampled evidence.
- The report does not claim global proof unless a formal proof is actually provided.
- Problem cases are kept and explained, not silently ignored.

## 6. Review robustness outputs

- Noise level or parameter variation is written clearly.
- Failed cases are recorded.
- Robustness results are not mixed with baseline results without labels.

## 7. Before committing results

Run:

```bash
python scripts/check_environment.py
make checks
python scripts/list_results.py
git status
```

Only commit result files that are useful examples, final artifacts, or needed for documentation.

## Final rule

Every important result should be understandable from its file name, experiment log, and related documentation.
