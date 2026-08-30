🌐 언어: [English](../en/result_naming.md) | [日本語](../ja/result_naming.md) | [한국어](../ko/result_naming.md) | [ไทย](../th/result_naming.md)

# Result File Naming 가이드

현재 출력은 분리된 `results/runs/<run_id>/` directory 안에서 설명적인 filename을 유지합니다. run ID가 time/commit identity를 제공하므로 filename에 timestamp는 필요하지 않습니다. `manifest.json`은 각 실제 파일의 role, size, SHA-256 digest를 기록합니다.

이 가이드는 실험 출력을 정리하고 비교하기 쉽게 유지하는 데 사용합니다.

## naming이 중요한 이유

plots, metrics, reports의 이름이 불명확하면 실험 결과를 비교하기 어려워집니다. 일관된 naming 규칙은 각 출력 파일을 생성 설정과 연결하는 데 도움이 됩니다.

## 권장 패턴

date, controller type, experiment type, 중요한 setting을 포함한 이름을 사용하세요.

```text
YYYYMMDD_controller_experiment_setting.ext
```

## 예시

```text
20260719_nn_trajectory_seed0.png
20260719_lqr_metrics_baseline.csv
20260719_nn_lyapunov_grid21.csv
20260719_nn_robustness_noise005.png
20260719_nn_finite_horizon_convergence_t8_tol01_grid31.png
20260719_experiment_report_seed0.md
```

## 권장 name parts

- Date: `YYYYMMDD`
- Controller: `lqr`, `nn`, `kan`, `comparison`
- Experiment type: `trajectory`, `metrics`, `lyapunov`, `robustness`, `finite_horizon_convergence`, `report`
- Setting: seed, grid size, noise level, epoch count, parameter variation

## 좋은 file names

- 명확하다
- lowercase를 사용한다
- underscores를 사용한다
- 가장 중요한 setting을 포함한다
- spaces를 포함하지 않는다

## 피해야 할 이름

- `final.png`
- `new_result.csv`
- `test2.md`
- `really_final_plot.png`

## 비교 규칙

두 run을 비교할 때는 file names만 보고도 무엇이 바뀌었는지 알 수 있어야 합니다.

## 문서화 규칙

보관 가치가 있는 결과는 experiment log template에 기록하세요.

## 현재 result files 목록 보기

report, demo, release review 전에 result inventory script를 실행하세요.

```bash
python scripts/list_results.py
```

또는 Makefile shortcut:

```bash
make list-results
```
