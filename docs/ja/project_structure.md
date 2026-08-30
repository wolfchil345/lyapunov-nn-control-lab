🌐 言語: [English](../en/project_structure.md) | [日本語](../ja/project_structure.md) | [한국어](../ko/project_structure.md) | [ไทย](../th/project_structure.md)

# Project Structure

このページは、Lyapunov Neural-Network Control Lab の主要な files と folders を説明します。

## Top-level files

### `main.py`
controller training、simulation、metrics、plots、robustness tests、report generation を含む main experiment pipeline を実行します。

### `requirements.txt`
development extra をインストールするための薄い互換ラッパーを提供します。依存関係の正式なソースは `pyproject.toml` です。

### `README.md`
project の概要、quick-start commands、results、documentation links を紹介します。

### `CITATION.cff`
project の citation metadata を提供します。

### `LICENSE`
project の利用・共有に関する license を定義します。

## Source code

### `src/lyapunov_nn_control_lab/system.py`
normalized second-order model coefficients、state-space matrices、LQR controller、Lyapunov matrix を定義します。

### `src/lyapunov_nn_control_lab/state_coordinates.py`
normalized coordinate convention と共有 NumPy/Torch state-norm helpers を定義します。

### `src/lyapunov_nn_control_lab/controllers.py`
neural-network controller、dataset generation、stability-aware training、actuator saturation utilities を定義します。

### `src/lyapunov_nn_control_lab/simulation.py`
closed-loop system trajectories をシミュレーションします。

### `src/lyapunov_nn_control_lab/lyapunov.py`
Lyapunov values、Lyapunov derivatives、grid-based stability checks を計算します。

### `src/lyapunov_nn_control_lab/metrics.py`
normalized-state/normalized-time performance metrics、LQR-style cost、integrated squared control effort を計算します。

### `src/lyapunov_nn_control_lab/plotting.py`
simulations、robustness experiments、Lyapunov contours、finite-horizon convergence maps、model architecture の plots を作成します。

### `src/lyapunov_nn_control_lab/reporting.py`
automatic experiment report を生成します。

### `src/lyapunov_nn_control_lab/noise.py`
common random-number realizations を用いた paired measurement-noise robustness simulations を実行し、raw/aggregate result writers を提供します。

### `src/lyapunov_nn_control_lab/experimental_seeds.py`
explicit seed plans、project 全体の RNG seeding、pairing checks、sample-variability aggregation helpers を定義します。

### `src/lyapunov_nn_control_lab/parameter_variation.py`
normalized model coefficients を変更した robustness simulations を実行します。

### `src/lyapunov_nn_control_lab/finite_horizon_convergence.py`
bounded grid 上で、明示的 finite horizon における strict final-state tolerance を評価し、sampling metadata を返します。

### `src/lyapunov_nn_control_lab/region_of_attraction.py`
以前の誤解を招く name に対する deprecated legacy API wrapper のみを提供します。

### `src/lyapunov_nn_control_lab/stability_ablation.py`
stability weights と共有 repeat seeds の Cartesian product を実行し、raw trials と aggregate statistics を分離します。

## Tests

### `tests/`
system model、controllers、simulations、metrics、plots、documentation-related outputs、robustness utilities の自動テストを含みます。

## Examples

### `examples/quick_start.py`
LQR simulation を実行するための小さく初学者向けの例です。

## Results

### `results/`
15 個の preserved legacy historical artifacts と、manifest-backed current runs 用の `results/runs/<run_id>/` directories を保存します。各 current run には report、data、figures、model state、inventory、checksums が含まれます。

### `src/lyapunov_nn_control_lab/result_provenance.py`
安全な run IDs を作成し、Git/environment/configuration provenance を取得し、staging 経由で公開し、実際の artifacts を inventory/hash 化して completed runs を検証します。

## Documentation

### `docs/`
methodology、reproducibility、figures、glossary terms、references、project summary に関するガイドを含みます。
