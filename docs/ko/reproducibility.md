🌐 언어: [English](../en/reproducibility.md) | [日本語](../ja/reproducibility.md) | [한국어](../ko/reproducibility.md) | [ไทย](../th/reproducibility.md)

# Reproducibility 가이드

이 가이드는 Lyapunov Neural-Network Control Lab의 주요 결과를 재현하는 방법을 설명합니다.

## 1. 저장소 clone

```bash
git clone https://github.com/wolfchil345/lyapunov-nn-control-lab.git
cd lyapunov-nn-control-lab
```

## 2. Python 환경 생성

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows PowerShell에서는:

```powershell
.venv\Scripts\Activate.ps1
```

## 3. 의존성 설치

```bash
python -m pip install -e ".[dev]"
```

## 4. 테스트 실행

```bash
python -m pytest
```

결과를 다시 생성하기 전에 모든 테스트가 통과해야 합니다.

## 5. 실험 결과 재생성

```bash
python main.py
```

이 명령은 아티팩트가 생성, 해시, 매니페스트 기록, 검증된 뒤에만 `results/runs/<run_id>/` 아래에 분리된 run을 게시합니다.

중요한 run-로컬 출력:

- `manifest.json`
- `SHA256SUMS`
- `report.md`
- `model_architecture.png`
- `performance_metrics.csv`
- paired raw and aggregate ablation/noise CSV files
- normalized-coordinate figures
- `nn_controller.pt`

## 6. 생성된 플롯 열기

GitHub Codespaces 또는 VS Code에서 선택한 run directory의 파일을 엽니다.

예:

```bash
code results/runs/<run_id>/model_architecture.png
code results/runs/<run_id>/report.md
```

## 7. Reproducibility 메모

- Python, NumPy, PyTorch CPU, 사용 가능한 PyTorch CUDA generator는 하나의 project utility로 seed됩니다. 고정 seed는 같은 환경의 CPU 비교 재현성에는 도움이 되지만, bitwise deterministic CUDA 또는 크로스플랫폼 실행을 보편적으로 보장하지는 않습니다.
- Stability weights는 모든 weight에서 paired seeds로 비교됩니다. Raw per-seed trials는 aggregate mean, sample standard deviation, standard error와 분리해 유지됩니다.
- Measurement-noise amplitudes는 common random-number realization을 사용합니다. 하나의 seed에 대해 같은 standardized sequence를 각 amplitude로 스케일합니다. Repeated matched seeds는 noise-realization confounding을 줄이지만, 모든 실험 불확실성을 제거하지는 않습니다.
- 운영체제, Python 버전, dependency 버전에 따라 작은 수치 차이가 발생할 수 있습니다.
- 프로젝트는 neural-network controller에 대한 완전한 형식 증명이 아니라, 경험적 simulation과 grid-based Lyapunov checks를 사용합니다.
- 생성된 플롯은 실용적인 stability/robustness 진단을 위한 것입니다.
- Finite-horizon convergence figure는 명시된 normalized-coordinate grid에서 strict criterion `||x(T)||_2 < epsilon`만 적용합니다. 이는 수학적 attraction-region certificate가 아닙니다.
- 이름이 `region_of_attraction`으로 시작하는 tracked files는 historical pre-migration artifacts이며, 이번 terminology-only operation에서는 의도적으로 재생성하지 않습니다.
- Official runs는 clean Git tree를 요구합니다. `--allow-dirty`는 manifest에 `git_dirty: true`가 기록된 exploratory run을 명시적으로 생성합니다.
- `configuration_sha256`는 canonical sorted scientific configuration JSON을 해시합니다. timestamp와 platform metadata는 configuration identity에 영향을 주지 않습니다.
- `python scripts/verify_run.py results/runs/<run_id>`로 run을 검증하세요.

## 8. 권장 검증 워크플로

새 실험 결과를 신뢰하기 전에 다음을 실행하세요.

```bash
python -m pytest
python main.py
python scripts/verify_run.py results/runs/<run_id>
python -m pytest
```

이 과정은 생성 전 코드를 점검하고, 게시된 파일 집합을 정확히 검증합니다.
