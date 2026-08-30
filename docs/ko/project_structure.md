🌐 언어: [English](../en/project_structure.md) | [日本語](../ja/project_structure.md) | [한국어](../ko/project_structure.md) | [ไทย](../th/project_structure.md)

# Project Structure

이 페이지는 Lyapunov Neural-Network Control Lab의 주요 files와 folders를 설명합니다.

## Top-level files

### `main.py`
controller training, simulation, metrics, plots, robustness tests, report generation을 포함한 main experiment pipeline을 실행합니다.

### `requirements.txt`
development extra 설치를 위한 얇은 호환성 래퍼를 제공합니다. 의존성의 기준 소스는 `pyproject.toml`입니다.

### `README.md`
project 소개, quick-start commands, results, documentation links를 제공합니다.

### `CITATION.cff`
project의 citation metadata를 제공합니다.

### `LICENSE`
project 사용 및 공유를 위한 license를 정의합니다.

## Source code

### `src/lyapunov_nn_control_lab/system.py`
normalized second-order model coefficients, state-space matrices, LQR controller, Lyapunov matrix를 정의합니다.

### `src/lyapunov_nn_control_lab/state_coordinates.py`
normalized coordinate convention과 공용 NumPy/Torch state-norm helpers를 정의합니다.

### `src/lyapunov_nn_control_lab/controllers.py`
neural-network controller, dataset generation, stability-aware training, actuator saturation utilities를 정의합니다.

### `src/lyapunov_nn_control_lab/simulation.py`
closed-loop system trajectories를 시뮬레이션합니다.

### `src/lyapunov_nn_control_lab/lyapunov.py`
Lyapunov values, Lyapunov derivatives, grid-based stability checks를 계산합니다.

### `src/lyapunov_nn_control_lab/metrics.py`
normalized-state/normalized-time performance metrics, LQR-style cost, integrated squared control effort를 계산합니다.

### `src/lyapunov_nn_control_lab/plotting.py`
simulations, robustness experiments, Lyapunov contours,
finite-horizon convergence maps, model architecture용 plots를 생성합니다.

### `src/lyapunov_nn_control_lab/reporting.py`
automatic experiment report를 생성합니다.

### `src/lyapunov_nn_control_lab/noise.py`
common random-number realizations를 사용한 paired measurement-noise robustness simulations를 실행하고 raw/aggregate result writers를 제공합니다.

### `src/lyapunov_nn_control_lab/experimental_seeds.py`
explicit seed plans, 프로젝트 전체 RNG seeding, pairing checks, sample-variability aggregation helpers를 정의합니다.

### `src/lyapunov_nn_control_lab/parameter_variation.py`
변경된 normalized model coefficients 하에서 robustness simulations를 실행합니다.

### `src/lyapunov_nn_control_lab/finite_horizon_convergence.py`
bounded grid에서 명시적 finite horizon의 strict final-state tolerance를 평가하고 sampling metadata를 반환합니다.

### `src/lyapunov_nn_control_lab/region_of_attraction.py`
이전의 오해를 부르는 name에 대한 deprecated legacy API wrapper만 제공합니다.

### `src/lyapunov_nn_control_lab/stability_ablation.py`
stability weights와 공유 repeat seeds의 Cartesian product를 실행한 뒤 raw trials와 aggregate statistics를 분리합니다.

## Tests

### `tests/`
system model, controllers, simulations, metrics, plots, documentation-related outputs, robustness utilities에 대한 자동화 테스트를 포함합니다.

## Examples

### `examples/quick_start.py`
LQR simulation 실행을 위한 작은 초보자 친화 예제를 제공합니다.

## Results

### `results/`
15개의 preserved legacy historical artifacts와 manifest-backed current runs용 `results/runs/<run_id>/` directories를 저장합니다. 각 current run에는 report, data, figures, model state, inventory, checksums가 포함됩니다.

### `src/lyapunov_nn_control_lab/result_provenance.py`
안전한 run IDs를 생성하고, Git/environment/configuration provenance를 수집하고, staging을 통해 게시하고, 실제 artifacts를 inventory/hash 처리하며, completed runs를 검증합니다.

## Documentation

### `docs/`
methodology, reproducibility, figures, glossary terms, references, project summary 가이드를 포함합니다.
