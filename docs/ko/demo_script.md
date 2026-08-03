🌐 언어: [English](../en/demo_script.md) | [日本語](../ja/demo_script.md) | [한국어](../ko/demo_script.md) | [ไทย](../th/demo_script.md)

# 5분 데모

## 0:00–0:30 — 목적

“이 project는 LQR을 모방하는 neural controller를 Lyapunov-style 및 robustness check로 평가합니다.”

## 0:30–1:30 — Repository tour

`README.md`, `src/`, `tests/`, `scripts/`, 다국어 `docs/`, `results/`를 보여줍니다.

## 1:30–2:15 — 재현성

`python examples/quick_start.py`를 실행하거나 완료된 `make quality-gate` result를 보여줍니다. 짧은 demo 중 full experiment를 시작하지 않습니다.

## 2:15–3:30 — 방법

Mass-spring-damper model, LQR teacher, neural imitation, `u(0) = 0`, sampled Lyapunov penalty를 설명합니다.

## 3:30–4:30 — 근거

`position_comparison.png`, `training_loss.png`, `region_of_attraction_comparison.png`를 보여주고 saturation, noise, parameter test를 언급합니다.

## 4:30–5:00 — 정직한 결론

결과가 simulation-based이며 sampled라는 점을 말하고 다음 연구 단계를 설명합니다.
