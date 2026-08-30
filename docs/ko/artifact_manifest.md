🌐 언어: [English](../en/artifact_manifest.md) | [日本語](../ja/artifact_manifest.md) | [한국어](../ko/artifact_manifest.md) | [ไทย](../th/artifact_manifest.md)

# Artifact Manifest

이 문서는 Lyapunov neural network control lab에서 생성되거나 사용되는 주요 파일을 설명합니다.

## 목적

프로젝트는 neural network 제어 성능, Lyapunov 안정 거동, 강건성, 재현성을 평가하기 위해 플롯, 리포트, 요약 파일을 생성합니다.

## 주요 소스 파일

| Path | Purpose |
| --- | --- |
| `main.py` | 메인 실험 파이프라인을 실행합니다. |
| `src/system.py` | 질량-스프링-댐퍼 시스템과 LQR 기준 제어기를 정의합니다. |
| `src/controllers.py` | neural network 제어기, 학습 데이터, Lyapunov-aware training logic을 정의합니다. |
| `src/simulation.py` | 폐루프 시스템 거동을 시뮬레이션합니다. |
| `src/lyapunov.py` | Lyapunov 값과 Lyapunov derivative grid checks를 계산합니다. |
| `src/metrics.py` | 상태 오차, 제어 effort, cost 같은 performance metrics를 계산합니다. |
| `src/plotting.py` | 궤적, 위상도, 강건성, 안정성 분석용 그림을 생성합니다. |
| `src/lyapunov_nn_control_lab/finite_horizon_convergence.py` | 명시적 finite horizon에서 bounded grid의 strict final-state tolerance를 평가하고 sampling metadata를 기록합니다. |

## 주요 스크립트

| Path | Purpose |
| --- | --- |
| `scripts/run_checks.py` | 문서 링크 검사, 단위 테스트, quick start example을 실행합니다. |
| `scripts/run_full_experiment.py` | 비파괴 full experiment workflow를 실행합니다. |
| `scripts/verify_run.py` | 완료된 manifest와 기록된 SHA-256 checksums를 검증합니다. |
| `scripts/summarize_results.py` | 생성된 실험 출력을 요약합니다. |
| `scripts/clean_results.py` | 새 실행이 필요할 때 생성된 result artifacts를 제거합니다. |
| `scripts/check_docs_links.py` | 내부 문서 링크를 검사합니다. |

## 결과 아티팩트

Historical files는 `results/` 바로 아래에 유지됩니다. 새 출력은 `results/runs/<run_id>/`에 격리되며 run 사이에 절대 섞이지 않습니다.

| Artifact type | Meaning |
| --- | --- |
| Trajectory plots | 서로 다른 제어기에서 상태 응답을 비교합니다. |
| Control plots | 제어 입력 거동과 saturation 효과를 비교합니다. |
| Lyapunov plots | Lyapunov 함수 거동과 도함수 영역을 시각화합니다. |
| Finite-horizon convergence plots | horizon, tolerance, bounds, grid, counts를 명시한 sampled final-state tolerance 결과를 보여주며 attraction-region certificate는 아닙니다. |
| Robustness plots | noise 또는 parameter variation에서 제어기 거동을 보여줍니다. |
| CSV summaries | 비교 및 후속 보고를 위한 수치 metrics를 저장합니다. |
| Experiment reports | 주요 수치/시각 결과를 설명합니다. |

## Reproducibility note

최종 thesis figure를 만들기 전에 로컬 체크를 실행하고 clean Git 상태에서 official run을 생성하세요.

```bash
python scripts/run_checks.py
python main.py
python scripts/verify_run.py results/runs/<run_id>
```

`manifest.json`에는 schema version, Git provenance, runtime versions, effective configuration, exact seeds, pairing methodology, inventory, sizes, hashes가 기록됩니다. legacy-artifact policy는 [`../../results/README.md`](../../results/README.md)를 참조하세요.

## 이 문서 활용법

thesis, 발표, 연구 미팅에서 저장소 구조를 설명할 때 이 manifest를 사용하세요.
