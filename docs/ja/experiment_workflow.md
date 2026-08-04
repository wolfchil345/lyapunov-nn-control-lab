🌐 言語: [English](../en/experiment_workflow.md) | [日本語](../ja/experiment_workflow.md) | [한국어](../ko/experiment_workflow.md) | [ไทย](../th/experiment_workflow.md)

# 実験ワークフロー

## 安全な手順

1. プロジェクトをインストールし、`python scripts/check_environment.py` を実行します。
2. `python examples/quick_start.py` と `make checks` を実行します。
3. ブランチ、コミット、シード、変更予定のパラメータを記録します。
4. `results/` の追跡ファイルをバックアップし、`python scripts/clean_results.py` でクリーンアップ対象をプレビューします。
5. `python main.py` を実行するか、`python scripts/run_full_experiment.py` で既知の生成ファイルの削除を確定して完全なパイプラインを実行します。
6. `python scripts/summarize_results.py` を実行し、全図とCSVを確認します。
7. 設定が互換の場合だけ指標を比較します。
8. コミット前に `make quality-gate` を実行します。

## 期待される出力

完全なパイプラインは、制御器比較、ロバスト性の図、Lyapunov診断、引き込み領域推定、2つのCSV、`nn_controller.pt`、実験レポートを生成します。

## レビュールール

低エラー、サンプル点で負の `V_dot`、グリッド収束を形式的証明として扱わないでください。失敗や予想外の結果を削除せず記録します。
