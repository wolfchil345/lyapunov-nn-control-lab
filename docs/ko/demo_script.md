🌐 언어: [English](../en/demo_script.md) | [日本語](../ja/demo_script.md) | [한국어](../ko/demo_script.md) | [ไทย](../th/demo_script.md)

# 5분 데모

## 0:00–0:30 — 목적

“이 프로젝트는 LQR을 모방하는 신경망 제어기를 연구하고, Lyapunov 방식의 검사와 강인성 시험으로 평가합니다.”

## 0:30–1:30 — 저장소 소개

`README.md`, `src/`, `tests/`, `scripts/`, 다국어 `docs/`, `results/`를 보여 줍니다.

## 1:30–2:15 — 재현성

`python examples/quick_start.py`를 실행하거나 완료된 `make quality-gate` 결과를 보여 줍니다. 짧은 데모 중에는 전체 실험을 시작하지 마세요.

## 2:15–3:30 — 방법

질량-스프링-댐퍼 모델, LQR 교사, 신경망 모방, `u(0) = 0`, 표본 기반 Lyapunov 패널티를 설명합니다.

## 3:30–4:30 — 근거

`position_comparison.png`, `training_loss.png`, `region_of_attraction_comparison.png`를 보여 줍니다. 구동기 포화, 잡음, 매개변수 시험도 언급합니다.

## 4:30–5:00 — 솔직한 결론

결과가 시뮬레이션과 표본점 평가에 기반함을 밝히고, 다음 연구 단계를 설명합니다.
