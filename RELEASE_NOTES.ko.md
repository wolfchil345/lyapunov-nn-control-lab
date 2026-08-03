🌐 언어: [English](RELEASE_NOTES.md) | [日本語](RELEASE_NOTES.ja.md) | [한국어](RELEASE_NOTES.ko.md) | [ไทย](RELEASE_NOTES.th.md)

# v1.0.1 - 문서와 릴리스 개선

이 patch release는 core control experiment를 바꾸지 않고 installation reliability, 다국어 documentation, result-summary reporting을 개선합니다.

## 주요 사항

- 누락된 `python-control` runtime dependency 추가
- 생성 virtual-environment와 package-metadata file ignore
- 영어, 일본어, 한국어, 태국어 documentation foundation 추가
- 네 언어 localized documentation index 추가
- 각 README를 localized documentation index에 연결
- Obsolete 또는 nonexistent documentation link 제거
- Ablation summary가 `lyapunov_violation_fraction`을 읽도록 수정
- 향후 version tag를 위한 release checklist 일반화

## 검증

- 57 test pass
- Quick-start example pass
- Quality gate pass
- Fixed random seed로 experiment result 재생성 성공
- 재생성 figure가 이전 추적 figure와 pixel-identical
- Lyapunov grid check zero violation
- Test controller의 region-of-attraction check 100% convergence

## 호환성

Core simulation, controller architecture, 추적 experimental result는 `v1.0.0`에서 변경되지 않았습니다.

---

# v1.0.0 - 첫 완전 릴리스

Lyapunov Neural-Network Control Lab의 첫 complete release입니다.

## 주요 사항

- LQR baseline, imitation-trained neural controller, Lyapunov-inspired check
- Stability-aware penalty, saturation, noise, parameter robustness
- Phase portrait, Lyapunov contour, region-of-attraction analysis
- Stability-weight ablation, automatic report, model architecture diagram
- Methodology, project summary, citation metadata

## 주요 출력

- `results/model_architecture.png`
- `results/position_comparison.png`
- `results/training_loss.png`
- `results/saturation_comparison.png`
- `results/noise_robustness.png`
- `results/parameter_robustness.png`
- `results/phase_portrait.png`
- `results/lyapunov_contours.png`
- `results/region_of_attraction.png`
- `results/region_of_attraction_comparison.png`
- `results/stability_weight_ablation.png`
- `results/experiment_report.md`

## 연구 초점

안정화 고전 controller를 모방하는 neural controller를 Lyapunov-based stability tool로 평가할 수 있는지 연구합니다.
