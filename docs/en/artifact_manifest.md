🌐 Language: [English](../en/artifact_manifest.md) | [日本語](../ja/artifact_manifest.md) | [한국어](../ko/artifact_manifest.md) | [ไทย](../th/artifact_manifest.md)

# Artifact Manifest

## Source and configuration

- `main.py`: full experiment orchestration.
- `src/`: dynamics, controllers, simulation, validation, reproducibility, metrics, robustness, reporting, and plotting.
- `tests/`: automated behavior checks.
- `pyproject.toml`, `requirements.txt`, `requirements-dev.txt`: package metadata, runtime dependencies, and development tools.

## Operational scripts

- `scripts/run_checks.py`: documentation links, tests, and quick start.
- `scripts/quality_gate.py`: final repository-readiness sequence.
- `scripts/run_full_experiment.py`: cleanup, experiment, and summary pipeline.
- `scripts/check_environment.py`, `scripts/check_package.py`, `scripts/project_status.py`, `scripts/list_results.py`: diagnostics.

## Generated evidence

- `results/*.png`: reference figures.
- `results/performance_metrics.csv`: controller metrics.
- `results/stability_weight_ablation.csv`: ablation metrics.
- `results/experiment_report*.md`: localized reports.
- `results/nn_controller.pt`: generated model state; intentionally not tracked.

Generated files are evidence, not source. Preserve settings and review diffs before replacing tracked artifacts.
