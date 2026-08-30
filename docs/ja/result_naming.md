🌐 言語: [English](../en/result_naming.md) | [日本語](../ja/result_naming.md) | [한국어](../ko/result_naming.md) | [ไทย](../th/result_naming.md)

# Result File Naming ガイド

現在の出力は、分離された `results/runs/<run_id>/` directory の中で説明的な filename を維持します。run ID が time/commit identity を提供するため、filename に timestamp は不要です。`manifest.json` には各実ファイルの role、size、SHA-256 digest が記録されます。

このガイドを使って、実験出力を整理し、比較しやすく保ちます。

## なぜ naming が重要か

plots、metrics、reports に不明確な名前を使うと、実験結果は比較しづらくなります。一貫した naming ルールは、各出力ファイルを生成設定と結びつけるのに役立ちます。

## 推奨パターン

date、controller type、experiment type、重要 setting を含む名前を使います。

```text
YYYYMMDD_controller_experiment_setting.ext
```

## 例

```text
20260719_nn_trajectory_seed0.png
20260719_lqr_metrics_baseline.csv
20260719_nn_lyapunov_grid21.csv
20260719_nn_robustness_noise005.png
20260719_nn_finite_horizon_convergence_t8_tol01_grid31.png
20260719_experiment_report_seed0.md
```

## 推奨 name parts

- Date: `YYYYMMDD`
- Controller: `lqr`、`nn`、`kan`、`comparison`
- Experiment type: `trajectory`、`metrics`、`lyapunov`、`robustness`、`finite_horizon_convergence`、`report`
- Setting: seed、grid size、noise level、epoch count、parameter variation

## 良い file names

- 明確である
- lowercase を使う
- underscores を使う
- 最重要 setting を含む
- spaces を含まない

## 避けるべき例

- `final.png`
- `new_result.csv`
- `test2.md`
- `really_final_plot.png`

## 比較ルール

2 つの run を比較するとき、file names から何が変わったか分かるようにします。

## ドキュメント化ルール

保持する価値のある結果は、experiment log template に記録します。

## 現在の result files を一覧する

report、demo、release review の前に result inventory script を実行します。

```bash
python scripts/list_results.py
```

または Makefile shortcut:

```bash
make list-results
```
