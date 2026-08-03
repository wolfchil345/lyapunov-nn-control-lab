🌐 言語: [English](../en/experiment_workflow.md) | [日本語](../ja/experiment_workflow.md) | [한국어](../ko/experiment_workflow.md) | [ไทย](../th/experiment_workflow.md)

# 実験ワークフロー

## 安全な手順

1. Projectをinstallし、`python scripts/check_environment.py` を実行します。
2. `python examples/quick_start.py` と `make checks` を実行します。
3. Branch、commit、seed、変更予定のparameterを記録します。
4. Cleanup前に `results/` の追跡ファイルをbackupします。
5. `python main.py` または `python scripts/run_full_experiment.py` を実行します。
6. `python scripts/summarize_results.py` を実行し、全plotとCSVを確認します。
7. 設定が互換の場合だけmetricを比較します。
8. Commit前に `make quality-gate` を実行します。

## 期待される出力

完全なpipelineは制御器比較、robustness plot、Lyapunov診断、region-of-attraction推定、2つのCSV、`nn_controller.pt`、実験レポートを生成します。

## Reviewルール

低error、サンプル点で負の `V_dot`、grid収束を形式的証明として扱わないでください。失敗や予想外の結果を削除せず記録します。
