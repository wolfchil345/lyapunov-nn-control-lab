🌐 Language: [English](../en/presentation_outline.md) | [日本語](../ja/presentation_outline.md) | [한국어](../ko/presentation_outline.md) | [ไทย](../th/presentation_outline.md)

# Presentation Outline

1. **Motivation:** neural controllers are flexible, but stability and robustness must be examined.
2. **Plant:** mass-spring-damper state-space model with position, velocity, and force input.
3. **Baseline:** LQR supplies a stabilizing reference and imitation targets.
4. **Neural controller:** zero-at-origin architecture, imitation loss, and Lyapunov penalty.
5. **Evaluation:** trajectories, settling time, cost, control effort, and sampled `V_dot`.
6. **Robustness:** actuator saturation, measurement noise, and parameter variation.
7. **State-space evidence:** phase portrait, Lyapunov contours, and region-of-attraction maps.
8. **Main result:** the neural controller closely follows LQR in the tested settings and all tracked sampled Lyapunov violation fractions are zero.
9. **Limitations:** simulated linear plant, finite grids, selected uncertainty cases, no formal proof.
10. **Future work:** nonlinear systems, formal verification, learned Lyapunov functions, KAN, and hardware validation.

Use figures with readable captions and state the seed and tested region when presenting numerical claims.
