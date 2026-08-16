🌐 언어: [English](../en/project_summary.md) | [日本語](../ja/project_summary.md) | [한국어](../ko/project_summary.md) | [ไทย](../th/project_summary.md)

# 프로젝트 개요

Lyapunov NN Control Lab은 제어공학과 머신러닝을 결합한 연구용 포트폴리오 프로젝트입니다.

이 프로젝트는 질량-스프링-댐퍼 시스템을 대상으로 LQR 제어기의 동작을 신경망 제어기로 근사합니다. 또한 Lyapunov 함수 기반 아이디어를 사용하여 폐루프 시스템의 안정성을 평가합니다.

## 목적

- 신경망 제어기를 학습한다
- LQR 제어기와 동작을 비교한다
- Lyapunov 함수를 사용하여 안정성을 확인한다
- 시뮬레이션 결과를 시각화한다
- 재현 가능한 연구 소프트웨어로 정리한다

## 주요 기술

- Python
- PyTorch
- LQR control
- Lyapunov stability
- Simulation evaluation
- GitHub Actions 자동 검사

## 포트폴리오 가치

이 리포지토리는 제어공학, 머신러닝, 안정성 해석, 연구 소프트웨어 관리를 하나의 흐름으로 보여주기 위한 프로젝트입니다.

## 공칭 플랜트(참고)

이 프로젝트의 공칭 정규화 파라미터는 MASS = 1.0, DAMPING = 0.4, STIFFNESS = 2.0입니다. 이 파라미터에서 상태행렬 `A`의 고유값은 대략 `-0.2 + 1.4j` 및 `-0.2 - 1.4j`이며, 두 고유값의 실수부가 음수이므로 공칭 무제어 선형 플랜트는 이미 점근 안정입니다. LQR은 불안정한 플랜트를 안정화하려는 것이 아니라 과도 응답과 제어 트레이드오프를 조정하는 기준 제어기입니다.

## Key outputs

- `results/model_architecture.png`
- `results/position_comparison.png`
- `results/training_loss.png`
- `results/saturation_comparison.png`
- `results/noise_robustness.png`
- `results/parameter_robustness.png`
- `results/phase_portrait.png`
- `results/lyapunov_contours.png`
- `results/region_of_attraction.png` (역사적 파일명 — 유한시간 수렴 맵에서 계승된 이름)
- `results/region_of_attraction_comparison.png` (역사적 파일명)
- `results/stability_weight_ablation.png`
- `results/experiment_report.md`
