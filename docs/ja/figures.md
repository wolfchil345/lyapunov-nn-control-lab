🌐 言語: [English](../en/figures.md) | [日本語](../ja/figures.md) | [한국어](../ko/figures.md) | [ไทย](../th/figures.md)

# Figures ガイド

このガイドは、`results/` directory に生成される図を説明します。

新しい図は、検証済み `manifest.json` と `SHA256SUMS` を伴って `results/runs/<run_id>/` に保存されます。root-level PNG files は legacy/unverified historical artifacts として保持されます。詳細は [`../../results/README.md`](../../results/README.md) を参照してください。

今後の図は normalized position、velocity、time、control、state-norm labels を使用します。コミット済み PNG files は historical release artifacts であり、coordinate-semantics change では再生成されません。そのため一部には古い generic labels や `Time [s]` 表記が残ります。

## Main comparison plots

### `position_comparison.png`
LQR controller と neural-network controller の position response を比較します。

### `training_loss.png`
neural-network training loss の epoch 推移を示します。

### `multiple_initial_conditions.png`
複数の初期状態からの neural-network controller の挙動を示します。

## Stability and Lyapunov plots

### `phase_portrait.png`
position-velocity 状態空間での軌道を示します。

### `lyapunov_contours.png`
Lyapunov 関数の等高線と閉ループ軌道を重ねて示します。

### `finite_horizon_convergence.png`
指定された normalized-time horizon、normalized-state tolerance、bounds、grid に対して `||x(T)||_2 < epsilon` を満たす sampled initial states を示します。これは asymptotic attraction-region calculation ではありません。

### `finite_horizon_convergence_comparison.png`
同一 finite-time final-state criterion を controller 間で比較し、converged/tested counts と percentages を報告します。

tracked `region_of_attraction.png` と `region_of_attraction_comparison.png` は、terminology correction 前に生成された historical artifacts です。これらは変更されません。今後の run では上記 2 つの corrected filenames を使用します。

## Robustness plots

### `saturation_comparison.png`
control input limit を適用したときの controller behavior を比較します。

### `noise_robustness.png`
historical single-seed figure として変更せず保持します。今後の paired experiments では、aggregate final-state statistics 用に `noise_robustness_paired.png`、代表的な matched-seed trajectories 用に `noise_robustness_paired_trajectories.png` を出力します。

### `parameter_robustness.png`
normalized model coefficients を変更したときの controller behavior を示します。

## Architecture and ablation plots

### `model_architecture.png`
plant model から controller、simulation、stability checks、reports までの project workflow を示します。

### `stability_weight_ablation.png`
historical figure として変更せず保持します。今後の paired experiments は `stability_weight_ablation_paired.png` を出力し、faint per-seed observations、mean trends、複数反復がある場合の sample variability を示します。

## Data files

### `performance_metrics.csv`
controller の数値 performance metrics を保存します。

### `stability_weight_ablation.csv`
以前の confounded seed design による historical results です。今後の paired runs では `stability_weight_ablation_trials_paired.csv` と `stability_weight_ablation_summary_paired.csv` を分離して出力します。noise trials/summaries は対応する `noise_robustness_*_paired.csv` 命名規則に従います。

### `experiment_report.md`
生成された plots、metrics、experiments を自動要約します。
