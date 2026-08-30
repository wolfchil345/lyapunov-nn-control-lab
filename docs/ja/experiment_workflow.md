🌐 言語: [English](../en/experiment_workflow.md) | [日本語](../ja/experiment_workflow.md) | [한국어](../ko/experiment_workflow.md) | [ไทย](../th/experiment_workflow.md)

# Experiment Workflow

このガイドでは、Lyapunov Neural-Network Control Lab で実験を実行するための推奨ワークフローを説明します。

## 1. 依存関係をインストールする

```bash
python -m pip install -e ".[dev]"
```

## 2. クイック例を実行する

basic simulation が動作することを確認するために quick-start script を使用します。

```bash
python examples/quick_start.py
```

## 3. ローカルチェックを実行する

長時間の実験を実行する前に、tests と examples が通ることを確認します。

```bash
python scripts/run_checks.py
```

## 4. 不完全な staging directory を掃除する

この任意コマンドは、放棄された staging directories のみを削除します。completed runs や historical artifacts は削除しません。

```bash
python scripts/clean_results.py
```

## 5. メイン実験を実行する

学習、シミュレーション、ロバスト性評価、可視化、レポート作成を含む完全パイプラインを実行します。

```bash
python main.py
```

## 6. 数値結果を要約する

CSV result files の簡易サマリーを端末に出力します。

```bash
python scripts/summarize_results.py
```

## 7. 生成出力を確認する

成功した各 run は `results/runs/<run_id>/` に分離保存されます。結果を使う前に `manifest.json`、`report.md`、`SHA256SUMS` を確認してください。

最初に確認する推奨ファイル:

- `performance_metrics.csv`
- `position_comparison.png`
- `phase_portrait.png`
- `lyapunov_contours.png`
- `finite_horizon_convergence_comparison.png`
- `report.md`
- `manifest.json`
- `SHA256SUMS`

## 8. 結果を解釈する

次のガイドを使用します。

- `../ja/results_interpretation.md`
- `../ja/figures.md`
- `../ja/limitations.md`

## 9. 変更を commit する前に

commit 前に再度チェックを実行します。

```bash
python scripts/run_checks.py
git status
```

## 推奨される完全ワークフロー

```bash
python scripts/run_checks.py
python main.py
python scripts/list_results.py
python scripts/run_checks.py
```

official runs には clean な Git tree が必要です。manifest は、ablation と common-random-number noise experiments の正確な paired seed sets を記録します。
