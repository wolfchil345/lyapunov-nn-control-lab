🌐 言語: [English](../en/artifact_manifest.md) | [日本語](../ja/artifact_manifest.md) | [한국어](../ko/artifact_manifest.md) | [ไทย](../th/artifact_manifest.md)

# Artifact一覧

## Sourceと設定

- `main.py`: 完全な実験orchestration。
- `src/`: dynamics、controller、simulation、metric、robustness、reporting、plotting。
- `tests/`: 自動化されたbehavior check。
- `pyproject.toml`, `requirements.txt`: package metadataとdependency。

## 運用スクリプト

- `scripts/run_checks.py`: documentation link、test、quick start。
- `scripts/quality_gate.py`: 最終的なrepository readiness sequence。
- `scripts/run_full_experiment.py`: cleanup、experiment、summary pipeline。
- `scripts/check_environment.py`, `scripts/project_status.py`, `scripts/list_results.py`: 診断。

## 生成された証拠

- `results/*.png`: reference figure。
- `results/performance_metrics.csv`: controller metric。
- `results/stability_weight_ablation.csv`: ablation metric。
- `results/experiment_report*.md`: 多言語report。
- `results/nn_controller.pt`: 生成model state。意図的に追跡しません。

生成ファイルはsourceではなく証拠です。追跡artifactを置き換える前に設定を保存しdiffを確認してください。
