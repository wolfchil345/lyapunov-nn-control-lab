🌐 언어: [English](README.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [ไทย](README.th.md)

# Lyapunov NN Control Lab

이 프로젝트는 신경망 제어기를 사용한 제어공학 실험 리포지토리입니다.

질량-스프링-댐퍼 시스템을 대상으로 LQR 제어기의 동작을 신경망으로 학습하고, Lyapunov 함수 기반 안정성 아이디어를 함께 다룹니다.

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

## 주요 문서

- [Project summary](docs/project_summary.md)
- [Methodology](docs/methodology.md)
- [Experiment workflow](docs/experiment_workflow.md)
- [Results interpretation](docs/results_interpretation.md)
- [Onboarding guide](docs/onboarding.md)
- [Maintenance guide](docs/maintenance.md)

## 포트폴리오 목적

이 리포지토리는 제어공학, 머신러닝, 안정성 해석, 연구 소프트웨어 관리를 함께 보여주는 포트폴리오 프로젝트입니다.
