🌐 언어: [English](RELEASE_NOTES.md) | [日本語](RELEASE_NOTES.ja.md) | [한국어](RELEASE_NOTES.ko.md) | [ไทย](RELEASE_NOTES.th.md)

# v1.0.1 - 문서 및 릴리스 마무리

이 패치 릴리스는 핵심 제어 실험을 변경하지 않으면서 설치 신뢰성, 다국어 문서, 결과 요약 보고를 개선합니다.

## 주요 내용

- 누락되어 있던 런타임 의존성 `python-control` 추가
- 생성되는 가상환경 파일 및 패키지 메타데이터 파일을 무시 대상으로 추가
- 영어, 일본어, 한국어, 태국어 문서 기반 추가
- 4개 언어 모두에 대해 로컬라이즈된 문서 색인 추가
- 각 README가 해당 언어의 로컬라이즈된 문서 색인을 가리키도록 업데이트
- 오래되었거나 존재하지 않는 문서 링크 제거
- 아블레이션 요약이 `lyapunov_violation_fraction`을 읽도록 수정
- 향후 버전 태그를 위해 릴리스 체크리스트를 일반화

## 검증

- 테스트 57개 통과
- 퀵스타트 예제 통과
- 품질 게이트 통과
- 고정 난수 시드로 실험 결과 재생성 성공
- 재생성된 결과 그림이 기존 추적 그림과 픽셀 단위로 동일
- Lyapunov 그리드 체크에서 위반 0건 보고
- 과거 유한시간 체크에서, 테스트된 컨트롤러와 설정에 대해 최종 상태 허용오차 만족률 100%를 보고했음. 이는 수학적 attraction-region 보증이 아님

## 호환성

핵심 시뮬레이션, 컨트롤러 아키텍처, 추적된 실험 결과는 `v1.0.0` 대비 변경되지 않았습니다.

---

# v1.0.0 - 첫 번째 완전 릴리스

이 릴리스는 Lyapunov Neural-Network Control Lab의 첫 번째 완전 릴리스입니다.

## 주요 내용

- LQR 기준 컨트롤러
- 모방학습으로 학습된 신경망 컨트롤러
- Lyapunov 기반 안정성 점검
- 안정성 인식 학습 페널티
- 액추에이터 포화 실험
- 측정 잡음 강건성 실험
- 파라미터 강건성 실험
- 위상 궤적 시각화
- Lyapunov 등고선 시각화
- 표본 기반 유한시간 수렴 맵핑(원래 릴리스에서는 레거시 용어로 설명)
- 유한시간 컨트롤러 비교(원래 릴리스에서는 레거시 용어로 설명)
- 안정성 가중치 아블레이션 연구
- 자동 실험 보고서 생성
- 모델 아키텍처 다이어그램
- 방법론 문서
- 프로젝트 요약 문서
- 인용 메타데이터

## 주요 산출물

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

이 프로젝트는 신경망 컨트롤러가 LQR 기준을 모방할 수 있는지를 과도응답, 강건성, 표본 기반 Lyapunov 진단으로 평가합니다. 공칭 무제어 플랜트는 이미 점근 안정입니다.
