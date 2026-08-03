🌐 Language: [English](../en/defense_questions.md) | [日本語](../ja/defense_questions.md) | [한국어](../ko/defense_questions.md) | [ไทย](../th/defense_questions.md)

# Defense Questions

## Motivation and design

**Why use LQR?** It is a transparent stabilizing baseline and supplies reliable imitation targets for the linear nominal plant.

**What does the network learn?** A mapping from position and velocity to a scalar control force.

**Why enforce `u(0) = 0`?** A nonzero command at the target could destroy the intended equilibrium.

## Stability

**Does the grid check prove global stability?** No. It evaluates finitely many sampled states with one Lyapunov candidate.

**Why use a Lyapunov penalty?** Imitation error alone does not directly measure closed-loop decay. The penalty encourages a sampled decay condition during training.

## Evaluation

**Which metric matters most?** No single one. Interpret convergence, cost, effort, sampled stability, and robustness together.

**Why test saturation, noise, and parameter variation?** Real controllers face limited inputs, imperfect sensors, and model mismatch.

## Limitations and next work

The plant is simple, all evidence is simulated, and behavior outside the training region is uncertain. Stronger work would add nonlinear plants, formal verification, hardware experiments, or alternative architectures such as KAN.
