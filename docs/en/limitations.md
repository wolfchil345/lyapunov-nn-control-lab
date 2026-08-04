🌐 Language: [English](../en/limitations.md) | [日本語](../ja/limitations.md) | [한국어](../ko/limitations.md) | [ไทย](../th/limitations.md)

# Limitations

## Model and data

- The plant is a simulated linear mass-spring-damper system.
- Training states cover a bounded region and use an LQR teacher.
- Results do not establish generalization to nonlinear plants or unseen states.

## Stability evidence

- The quadratic Lyapunov function is inherited from the nominal LQR design.
- `V_dot` and region-of-attraction evaluations use finite grids, thresholds, and simulation horizons.
- Zero sampled violations do not constitute a formal or global proof.

## Robustness evidence

- Actuator limits, noise levels, and parameter variations are selected scenarios, not exhaustive uncertainty sets.
- Most simulations use adaptive ODE integration; the measurement-noise experiment uses fixed-step explicit Euler integration. Solver, device, and dependency differences can change results slightly.
- No hardware, delay, quantization, fault, or adversarial test is included.

## Responsible use

This repository is educational research software, not a safety-certified controller. Validate independently before applying the method to physical equipment.

Future work includes nonlinear plants, formal verification, learned Lyapunov functions, broader uncertainty analysis, and hardware validation.
