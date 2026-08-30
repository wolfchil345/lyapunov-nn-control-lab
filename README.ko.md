🌐 언어: [English](README.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [ไทย](README.th.md)

![Python tests](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/tests.yml/badge.svg)
![Quality gate](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/quality-gate.yml/badge.svg)

# Lyapunov NN Control Lab

이 프로젝트는 신경망 제어기를 사용한 제어공학 실험 리포지토리입니다。

질량-스프링-댐퍼 시스템을 대상으로 LQR 제어기의 동작을 신경망으로 학습하고, Lyapunov 함수 기반 안정성 아이디어를 함께 다룹니다。

## 주요 내용

- Python과 PyTorch를 사용한 제어기 학습
- LQR 제어기를 교사로 사용하는 신경망 제어
- Lyapunov penalty를 활용한 안정성 중심 학습
- 시뮬레이션, 평가, 강건성 확인, 결과 시각화
- GitHub Actions, 테스트, quality gate를 통한 재현성 확인

## 시작하기

```bash
python scripts/check_environment.py
python examples/quick_start.py
python scripts/quality_gate.py
```

## 기술적 요약

공칭(normalized) 모델의 표준 파라미터는 다음과 같습니다: MASS = 1.0, DAMPING = 0.4, STIFFNESS = 2.0. 이 공칭값에서 상태행렬 `A`의 고유값은 대략 `-0.2 + 1.4j` 및 `-0.2 - 1.4j`이며, 두 고유값의 실수부가 음수이므로 공칭의 무제어 선형 플랜트는 이미 점근 안정입니다. 따라서 LQR은 불안정한 플랜트를 안정화하는 것이 아니라 과도 응답과 제어 트레이드오フを変えます。

이 저장소는 정규화된 무차원 2차 모델을 사용합니다. `tau`는 정규화 시간, `q`는 정규화된 위치유사 좌표, `v = dq/dtau`는 정규화 속도, `u`는 정규화 제어 입력이며 상태는 `x = [q, v]`입니다. 따라서 `||x||_2 = sqrt(q^2 + v^2)`는 정규화 상태 좌표에서의 Euclidean norm입니다. 기존 CSV 필드명 `settling_time_s`는 호환성을 위해 유지되지만, 이는 정규화 시간을 나타내는 이전 필드명임을 명시합니다.

## 주요 문서

- [문서 색인](docs/ko/index.md)
- [Project summary](docs/ko/project_summary.md)
- [Methodology](docs/ko/methodology.md)
- [Experiment workflow](docs/ko/experiment_workflow.md)
- [Results interpretation](docs/ko/results_interpretation.md)
- [Onboarding guide](docs/ko/onboarding.md)
- [Maintenance guide](docs/ko/maintenance.md)

## Lyapunov 평가 및 학습

샘플링 기반 Lyapunov 평가는 다음과 같은 도함수 표현을 사용합니다:

```text
V-dot(x) = 2 x^T P (A x + B pi(x))
```

평가기는 두 가지 조건을 보고합니다:

```text
기본 감소: V-dot(x) <= 0
감쇠 마진: V-dot(x) + alpha * ||x||_2^2 <= 0
```

학습에서는 양수인 감소 잔차를 페널티로 사용합니다. 구현상 표현은 다음과 같습니다:

```text
decay residual = V-dot(x) + alpha * ||x||_2^2
Lyapunov penalty = mean(ReLU(decay residual))
```

기본 감쇠 마진은 `alpha = 0.05` (`DEFAULT_DECAY_MARGIN = 0.05`)입니다. 수치 허용오차(예: `1e-9`)는 `alpha`와 분리하여 취급됩니다.

## 유한 시간 수렴

유한 시간 수렴 평가는 엄격한 기준을 사용합니다:

```text
||x(T)||_2 < epsilon
```

이는 표본 기반의 경험적 결과이며 연속 상태 공간에 대한 형식적 보증은 아닙니다.

## 결과와 provenance

실행 결과는 `results/runs/<run_id>/`에 수집되며, 매니페스트와 SHA-256 체크섬을 포함합니다: `manifest.json`, `SHA256SUMS`, `report.md` 등. 레거시(역사적) 산출물(예: `results/region_of_attraction.png`)은 재현성을 위해 보존됩니다.


## 포트폴리오 목적

이 리포지토리는 제어공학, 머신러닝, 안정성 해석, 연구 소프트웨어 관리를 함께 보여주는 포트폴리오 프로젝트입니다.
