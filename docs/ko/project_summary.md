🌐 언어: [English](../en/project_summary.md) | [日本語](../ja/project_summary.md) | [한국어](../ko/project_summary.md) | [ไทย](../th/project_summary.md)

# 프로젝트 요약

## Overview

이 프로젝트는 Lyapunov 영감을 받은 안정성 분석을 포함한 neural-network control용 Python 연구 랩입니다.

대상 시스템은 질량-스프링-댐퍼 플랜트입니다. 이 프로젝트는 고전적 LQR 제어기와 모방 학습으로 학습된 neural-network 제어기를 비교합니다.

## Main goal

주요 목표는 neural-network 제어기가 LQR 참조를 모방하면서 유용한 과도응답, 강건성, 샘플 Lyapunov 거동을 유지할 수 있는지 연구하는 것입니다. 공칭 무제어 선형 플랜트는 이미 점근 안정이며, 제어기는 폐루프 성능을 바꿉니다.

## Nominal plant (canonical)

저장소 전반에서 사용하는 canonical normalized plant 파라미터는 다음과 같습니다.

- MASS = 1.0
- DAMPING = 0.4
- STIFFNESS = 2.0

이 파라미터에서 상태행렬 `A`의 고유값은 대략 `-0.2 + 1.4j`와 `-0.2 - 1.4j`이며 실수부가 음수입니다. 이 값들은 canonical baseline의 일부이며, 이 파일의 모든 언어 버전에서 그대로 보존되어야 합니다.

## Main features

- LQR baseline controller
- neural-network controller
- stability-aware training penalty
- Lyapunov grid check
- actuator saturation experiment
- measurement-noise robustness experiment
- parameter robustness experiment
- phase portrait visualization
- Lyapunov contour visualization
- finite-horizon convergence mapping with explicit sampling metadata
- controller comparison using an explicit finite-horizon final-state tolerance
- stability-weight ablation study
- automatic experiment report generation

## Key outputs

- `results/model_architecture.png`
- `results/position_comparison.png`
- `results/training_loss.png`
- `results/saturation_comparison.png`
- `results/noise_robustness.png`
- `results/parameter_robustness.png`
- `results/phase_portrait.png`
- `results/lyapunov_contours.png`
- `results/region_of_attraction.png` (finite-horizon map의 historical filename)
- `results/region_of_attraction_comparison.png` (finite-horizon comparison의 historical filename)
- `results/stability_weight_ablation.png`
- `results/experiment_report.md`

## Why this project matters

neural-network 제어기는 강력하지만, 안정성은 제어공학에서 핵심 우려 사항입니다.

이 프로젝트는 학습 기반 제어와 고전적 안정성 분석 아이디어를 결합합니다. neural-network 제어기에 대한 완전한 형식 증명을 제공한다고 주장하지 않지만, 안정 거동을 연구할 수 있는 실용적 경험 도구를 제공합니다.

## Portfolio value

이 저장소는 제어공학, Python, PyTorch, 수치 시뮬레이션, 테스트, 시각화, GitHub Actions, 문서화, 재현 가능한 연구 워크플로 역량을 보여줍니다.
