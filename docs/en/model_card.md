🌐 Language: [English](../en/model_card.md) | [日本語](../ja/model_card.md) | [한국어](../ko/model_card.md) | [ไทย](../th/model_card.md)

# Model Card

## Model

The controller is a small PyTorch multilayer perceptron that maps `[position, velocity]` to one force command. Its output is shifted to enforce `u(0) = 0`.

## Training

States are sampled from a bounded region and labeled by the nominal LQR controller. Training minimizes imitation MSE plus a weighted sampled Lyapunov penalty. The repository sets fixed random seeds.

## Intended use

- Education and research prototyping for learning-based control.
- Reproducible comparison with LQR under the included simulations.
- Exploration of stability-aware objectives and robustness diagnostics.

## Out of scope

- Direct safety-critical or hardware deployment.
- Claims of formal, global, or distribution-free stability.
- Operation outside validated state, actuator, and plant ranges.

## Evaluation

Closed-loop trajectories, final norm, settling time, cost, control energy, maximum input, sampled `V_dot`, robustness scenarios, and estimated regions of attraction.

See [limitations](limitations.md) and [reproducibility](reproducibility.md) before reusing the model.
