🌐 언어: [English](../en/experiment_workflow.md) | [日本語](../ja/experiment_workflow.md) | [한국어](../ko/experiment_workflow.md) | [ไทย](../th/experiment_workflow.md)

# Experiment Workflow

이 가이드는 Lyapunov Neural-Network Control Lab에서 실험을 수행하기 위한 권장 워크플로를 설명합니다.

## 1. 의존성 설치

```bash
python -m pip install -e ".[dev]"
```

## 2. 빠른 예제 실행

기본 시뮬레이션이 동작하는지 quick-start script로 확인합니다.

```bash
python examples/quick_start.py
```

## 3. 로컬 체크 실행

긴 실험을 돌리기 전에 tests와 examples가 통과하는지 확인합니다.

```bash
python scripts/run_checks.py
```

## 4. 미완성 staging directory 정리

이 선택 명령은 버려진 staging directories만 제거합니다. completed runs나 historical artifacts는 삭제하지 않습니다.

```bash
python scripts/clean_results.py
```

## 5. 메인 실험 실행

학습, 시뮬레이션, 강건성, 플로팅, 리포팅 전체 파이프라인을 실행합니다.

```bash
python main.py
```

## 6. 수치 결과 요약

CSV 결과 파일의 빠른 터미널 요약을 출력합니다.

```bash
python scripts/summarize_results.py
```

## 7. 생성된 출력 확인

성공한 각 run은 `results/runs/<run_id>/` 아래에 분리 저장됩니다. 결과를 사용하기 전에 `manifest.json`, `report.md`, `SHA256SUMS`를 점검하세요.

먼저 확인할 권장 파일:

- `performance_metrics.csv`
- `position_comparison.png`
- `phase_portrait.png`
- `lyapunov_contours.png`
- `finite_horizon_convergence_comparison.png`
- `report.md`
- `manifest.json`
- `SHA256SUMS`

## 8. 결과 해석

다음 가이드를 사용합니다.

- `../ko/results_interpretation.md`
- `../ko/figures.md`
- `../ko/limitations.md`

## 9. 변경 commit 전

commit 전에 체크를 다시 실행합니다.

```bash
python scripts/run_checks.py
git status
```

## 권장 전체 워크플로

```bash
python scripts/run_checks.py
python main.py
python scripts/list_results.py
python scripts/run_checks.py
```

official runs는 clean Git tree를 요구합니다. manifest에는 ablation 및 common-random-number noise experiments의 정확한 paired seed sets가 기록됩니다.
