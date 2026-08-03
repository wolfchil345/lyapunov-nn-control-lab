🌐 Language: [English](../en/research_questions.md) | [日本語](../ja/research_questions.md) | [한국어](../ko/research_questions.md) | [ไทย](../th/research_questions.md)

# Research Questions

## Main question

Can a neural controller imitate a stabilizing LQR policy while retaining favorable sampled Lyapunov behavior and robustness in closed-loop simulation?

## Performance and stability

- How close are settling time, quadratic cost, and control effort to LQR?
- Where is sampled `V_dot` nonnegative, and how does the training penalty change it?
- How does the estimated region of attraction vary across LQR, neural, and saturated controllers?

## Robustness

- How do measurement noise, actuator saturation, and plant uncertainty affect convergence?
- Which test cases fail first, and are those failures inside or outside the training region?

## Training and architecture

- What trade-off exists between imitation accuracy and stability-loss weight?
- Would a KAN controller change smoothness, interpretability, robustness, or region-of-attraction results?

State the sampled region, thresholds, seed, and limitations when reporting any answer.
