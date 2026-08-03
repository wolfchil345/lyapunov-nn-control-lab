🌐 언어: [English](../en/artifact_manifest.md) | [日本語](../ja/artifact_manifest.md) | [한국어](../ko/artifact_manifest.md) | [ไทย](../th/artifact_manifest.md)

# Artifact 목록

## Source와 설정

- `main.py`: 전체 실험 orchestration.
- `src/`: dynamics, controller, simulation, metric, robustness, reporting, plotting.
- `tests/`: 자동 behavior check.
- `pyproject.toml`, `requirements.txt`: package metadata와 dependency.

## 운영 스크립트

- `scripts/run_checks.py`: documentation link, test, quick start.
- `scripts/quality_gate.py`: 최종 repository readiness sequence.
- `scripts/run_full_experiment.py`: cleanup, experiment, summary pipeline.
- `scripts/check_environment.py`, `scripts/project_status.py`, `scripts/list_results.py`: 진단.

## 생성된 근거

- `results/*.png`: reference figure.
- `results/performance_metrics.csv`: controller metric.
- `results/stability_weight_ablation.csv`: ablation metric.
- `results/experiment_report*.md`: 다국어 report.
- `results/nn_controller.pt`: 생성 model state이며 의도적으로 추적하지 않음.

생성 파일은 source가 아니라 근거입니다. 추적 artifact를 교체하기 전에 설정을 보존하고 diff를 검토하십시오.
