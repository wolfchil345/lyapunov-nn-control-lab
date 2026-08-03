🌐 언어: [English](../en/artifact_manifest.md) | [日本語](../ja/artifact_manifest.md) | [한국어](../ko/artifact_manifest.md) | [ไทย](../th/artifact_manifest.md)

# 산출물 목록

## 소스와 설정

- `main.py`: 전체 실험의 실행을 조정합니다.
- `src/`: 동역학, 제어기, 시뮬레이션, 평가 지표, 강인성, 보고서 생성, 그림 작성.
- `tests/`: 동작을 확인하는 자동 테스트.
- `pyproject.toml`, `requirements.txt`: 패키지 정보와 의존성.

## 운영 스크립트

- `scripts/run_checks.py`: 문서 링크, 테스트, 빠른 시작 예제를 검사합니다.
- `scripts/quality_gate.py`: 저장소의 최종 준비 상태를 검사하는 절차입니다.
- `scripts/run_full_experiment.py`: 결과 정리, 실험, 요약을 순서대로 실행합니다.
- `scripts/check_environment.py`, `scripts/project_status.py`, `scripts/list_results.py`: 진단용 스크립트.

## 생성되는 검증 자료

- `results/*.png`: 참조 그림.
- `results/performance_metrics.csv`: 제어기 평가 지표.
- `results/stability_weight_ablation.csv`: 제거 실험 지표.
- `results/experiment_report*.md`: 언어별 보고서.
- `results/nn_controller.pt`: 생성된 모델 상태. 의도적으로 Git에서 추적하지 않습니다.

생성 파일은 검증 자료이며 소스가 아닙니다. 추적 중인 산출물을 교체하기 전에 설정을 보존하고 차이를 검토하세요.
