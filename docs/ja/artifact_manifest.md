🌐 言語: [English](../en/artifact_manifest.md) | [日本語](../ja/artifact_manifest.md) | [한국어](../ko/artifact_manifest.md) | [ไทย](../th/artifact_manifest.md)

# 成果物一覧

## ソースと設定

- `main.py`: 実験全体の実行制御。
- `src/`: ダイナミクス、制御器、シミュレーション、評価指標、ロバスト性、レポート作成、プロット。
- `tests/`: 動作を確認する自動テスト。
- `pyproject.toml`, `requirements.txt`: パッケージ情報と依存関係。

## 運用スクリプト

- `scripts/run_checks.py`: ドキュメントリンク、テスト、クイックスタートの確認。
- `scripts/quality_gate.py`: リポジトリの最終的な準備状況を確認する一連の処理。
- `scripts/run_full_experiment.py`: 結果のクリーンアップ、実験、要約の一括実行。
- `scripts/check_environment.py`, `scripts/project_status.py`, `scripts/list_results.py`: 診断用スクリプト。

## 生成される検証資料

- `results/*.png`: 参照用の図。
- `results/performance_metrics.csv`: 制御器の評価指標。
- `results/stability_weight_ablation.csv`: アブレーション実験の指標。
- `results/experiment_report*.md`: 各言語のレポート。
- `results/nn_controller.pt`: 生成されるモデル状態。意図的にGit管理の対象外です。

生成ファイルは検証資料であり、ソースではありません。追跡中の成果物を置き換える前に、設定を保存して差分を確認してください。
