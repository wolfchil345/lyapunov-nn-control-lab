🌐 Language: [English](../en/demo_script.md) | [日本語](../ja/demo_script.md) | [한국어](../ko/demo_script.md) | [ไทย](../th/demo_script.md)

# Five-Minute Demo

## 0:00–0:30 — Purpose

“This project studies a neural controller that imitates LQR and is evaluated with Lyapunov-style and robustness checks.”

## 0:30–1:30 — Repository tour

Show `README.md`, `src/`, `tests/`, `scripts/`, localized `docs/`, and `results/`.

## 1:30–2:15 — Reproducibility

Run `python examples/quick_start.py` or show a completed `make quality-gate` result. Do not start the full experiment during a short demo.

## 2:15–3:30 — Method

Explain the mass-spring-damper model, LQR teacher, neural imitation, `u(0) = 0`, and sampled Lyapunov penalty.

## 3:30–4:30 — Evidence

Show `position_comparison.png`, `training_loss.png`, and `region_of_attraction_comparison.png`. Mention saturation, noise, and parameter tests.

## 4:30–5:00 — Honest conclusion

State that the results are simulation-based and sampled, then describe the next research step.
