🌐 언어: [English](../en/experiment_workflow.md) | [日本語](../ja/experiment_workflow.md) | [한국어](../ko/experiment_workflow.md) | [ไทย](../th/experiment_workflow.md)

# 실험 워크플로

## 안전한 순서

1. 프로젝트를 설치하고 `python scripts/check_environment.py`를 실행합니다.
2. `python examples/quick_start.py`와 `make checks`를 실행합니다.
3. 브랜치, 커밋, 시드, 변경할 매개변수를 기록합니다.
4. 결과를 정리하기 전에 `results/`의 추적 파일을 백업합니다.
5. `python main.py` 또는 `python scripts/run_full_experiment.py`를 실행합니다.
6. `python scripts/summarize_results.py`를 실행하고 모든 그래프과 CSV를 확인합니다.
7. 설정이 호환될 때만 지표을 비교합니다.
8. 커밋 전에 `make quality-gate`를 실행합니다.

## 예상 출력

전체 파이프라인은 제어기 비교, 강건성 그래프, Lyapunov 진단, 인력 영역 추정, CSV 두 개, `nn_controller.pt`, 실험 보고서를 생성합니다.

## 검토 규칙

낮은 오류, 표본에서 음수인 `V_dot`, 격자 수렴을 형식적 증명으로 해석하지 마십시오. 실패와 예상 밖 결과를 삭제하지 말고 기록합니다.
