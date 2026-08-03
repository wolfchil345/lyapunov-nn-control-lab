🌐 언어: [English](RELEASE_NOTES.md) | [日本語](RELEASE_NOTES.ja.md) | [한국어](RELEASE_NOTES.ko.md) | [ไทย](RELEASE_NOTES.th.md)

# v1.0.1 - 문서와 릴리스 개선

이 패치 릴리스는 핵심 제어 실험을 변경하지 않고 설치 신뢰성, 다국어 문서, 결과 요약 보고를 개선했습니다.

## 주요 변경 사항

- 누락된 런타임 의존성 `python-control` 추가
- 생성된 가상 환경 및 패키지 메타데이터 파일을 Git에서 제외
- 영어, 일본어, 한국어, 태국어 문서 기반 추가
- 네 언어의 현지화된 문서 색인 추가
- 각 README에서 해당 언어의 문서 색인으로 연결
- 오래되었거나 존재하지 않는 문서 링크 제거
- 절제 요약이 `lyapunov_violation_fraction`을 읽도록 수정
- 향후 버전 태그에도 사용할 수 있도록 릴리스 체크리스트 일반화

## 검증

- 57개 테스트 통과
- 빠른 시작 예제 통과
- 품질 게이트 통과
- 고정된 난수 시드로 실험 결과 재생성 성공
- 재생성한 그림은 이전에 Git으로 관리한 그림과 픽셀 단위로 일치
- Lyapunov 격자 검사에서 위반 0건
- 시험한 제어기의 인력 영역 검사에서 100% 수렴

## 호환성

핵심 시뮬레이션, 제어기 아키텍처, Git으로 관리하는 실험 결과는 `v1.0.0`에서 변경되지 않았습니다.

---

# v1.0.0 - 첫 정식 릴리스

Lyapunov Neural-Network Control Lab의 첫 정식 릴리스입니다.

## 주요 기능

- LQR 기준 제어기
- 모방 학습으로 훈련한 신경망 제어기
- Lyapunov 이론에 기반한 안정성 검사
- 안정성을 고려한 학습 패널티
- 구동기 포화 실험
- 측정 잡음 강건성 실험
- 매개변수 강건성 실험
- 위상도 시각화
- Lyapunov 등고선 시각화
- 인력 영역 추정
- 제어기별 인력 영역 비교
- 안정성 가중치 절제 연구
- 실험 보고서 자동 생성
- 모델 아키텍처 도식
- 방법론 문서
- 프로젝트 요약 문서
- 인용 메타데이터

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

이 프로젝트는 신경망 제어기가 안정화 가능한 고전 제어기를 모방하고, 그 거동을 Lyapunov 안정성 도구로 평가할 수 있는지 연구합니다.
