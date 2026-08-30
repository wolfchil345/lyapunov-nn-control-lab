🌐 언어: [English](../en/figures.md) | [日本語](../ja/figures.md) | [한국어](../ko/figures.md) | [ไทย](../th/figures.md)

# Figures 가이드

이 가이드는 `results/` directory에 생성되는 그림들을 설명합니다.

새 그림은 검증된 `manifest.json` 및 `SHA256SUMS`와 함께 `results/runs/<run_id>/` 내부에 저장됩니다. 루트 PNG files는 legacy/unverified historical artifacts로 보존됩니다. 자세한 내용은 [`../../results/README.md`](../../results/README.md)를 참고하세요.

향후 그림은 normalized position, velocity, time, control, state-norm labels를 사용합니다. 커밋된 PNG files는 historical release artifacts이며 coordinate-semantics change로 재생성되지 않으므로, 일부는 기존 generic labels 또는 `Time [s]` 문구를 유지합니다.

## Main comparison plots

### `position_comparison.png`
LQR controller와 neural-network controller의 position response를 비교합니다.

### `training_loss.png`
neural-network training loss의 epoch별 변화를 보여줍니다.

### `multiple_initial_conditions.png`
여러 초기 상태에서 neural-network controller가 어떻게 동작하는지 보여줍니다.

## Stability and Lyapunov plots

### `phase_portrait.png`
position-velocity 상태공간의 궤적을 보여줍니다.

### `lyapunov_contours.png`
Lyapunov 함수 등고선과 폐루프 궤적을 함께 보여줍니다.

### `finite_horizon_convergence.png`
명시된 normalized-time horizon, normalized-state tolerance, bounds, grid에서 `||x(T)||_2 < epsilon`을 만족하는 sampled initial states를 보여줍니다. 이는 asymptotic attraction-region calculation이 아닙니다.

### `finite_horizon_convergence_comparison.png`
동일한 finite-time final-state criterion을 controller 간 비교하고 converged/tested counts와 percentages를 보고합니다.

tracked `region_of_attraction.png` 및 `region_of_attraction_comparison.png` 파일은 terminology correction 이전에 생성된 historical artifacts입니다. 이 파일들은 변경되지 않으며, 향후 runs는 위의 두 corrected filenames를 사용합니다.

## Robustness plots

### `saturation_comparison.png`
control input limits 적용 시 controller behavior를 비교합니다.

### `noise_robustness.png`
historical single-seed figure로 변경 없이 유지합니다. 향후 paired experiments는 aggregate final-state statistics용 `noise_robustness_paired.png`와 representative matched-seed trajectories용 `noise_robustness_paired_trajectories.png`를 생성합니다.

### `parameter_robustness.png`
normalized model coefficients를 변경했을 때 controller behavior를 보여줍니다.

## Architecture and ablation plots

### `model_architecture.png`
plant model부터 controller, simulation, stability checks, reports까지 project workflow를 보여줍니다.

### `stability_weight_ablation.png`
historical figure로 변경 없이 유지합니다. 향후 paired experiments는 `stability_weight_ablation_paired.png`를 생성하며, faint per-seed observations, mean trends, 반복이 여러 번일 때 sample variability를 보여줍니다.

## Data files

### `performance_metrics.csv`
controller의 수치 performance metrics를 저장합니다.

### `stability_weight_ablation.csv`
이전 confounded seed design의 historical results입니다. 향후 paired runs는 `stability_weight_ablation_trials_paired.csv`와 `stability_weight_ablation_summary_paired.csv`를 분리 생성합니다. noise trials/summaries도 해당 `noise_robustness_*_paired.csv` naming convention을 따릅니다.

### `experiment_report.md`
생성된 plots, metrics, experiments를 자동으로 요약합니다.
