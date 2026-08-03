🌐 Language: [English](../en/kan_extension.md) | [日本語](../ja/kan_extension.md) | [한국어](../ko/kan_extension.md) | [ไทย](../th/kan_extension.md)

# KAN Extension

## Question

Can a Kolmogorov-Arnold Network controller match or improve the current MLP controller while retaining closed-loop stability and robustness in the tested region?

## Implementation plan

1. Add a KAN controller behind the same state-to-force interface in `src/controllers.py`.
2. Keep the dataset, seed, training region, initial states, and evaluation pipeline fixed.
3. Add tests for shape, `u(0) = 0`, serialization, and simulation compatibility.
4. Compare LQR, MLP, and KAN with identical metrics and plots.

## Evaluation

Compare imitation loss, settling time, quadratic cost, control energy, maximum input, sampled Lyapunov violation fraction, robustness, and estimated region of attraction.

## Caution

A more interpretable architecture is not automatically a more stable controller. Apply the same limitations, review process, and formal-proof caveat used for the MLP.
