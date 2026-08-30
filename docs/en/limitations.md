🌐 Language: [English](../en/limitations.md) | [日本語](../ja/limitations.md) | [한국어](../ko/limitations.md) | [ไทย](../th/limitations.md)

# Limitations

This page explains important limitations of the Lyapunov Neural-Network Control Lab.

## Educational research project

This repository is designed for learning, experimentation, and research exploration.

It should not be treated as a complete safety-certified control system.

## Simple physical model

The main plant is a mass-spring-damper system.

This is useful for control experiments, but it is much simpler than many real mechanical systems.

## Normalized-coordinate limitation

The model is dimensionless and does not define a mapping from `q`, `v`, `tau`,
or `u` to SI units. Results therefore support normalized simulation comparisons,
not direct claims about metres, seconds, newtons, or hardware energy.

## Grid-based stability checks

The Lyapunov checks are evaluated on sampled grid points.

Passing a grid check does not prove global stability over every possible state.

It only gives empirical evidence over the checked region.

## Neural-network controller limitations

The neural-network controller is trained from data and may behave poorly outside the training distribution.

Good imitation of LQR does not automatically guarantee stability in all regions.

## Numerical simulation limitations

Simulation results can depend on solver settings, time step choices, package versions, and numerical tolerances.

Small differences between machines are possible.

## Finite-horizon convergence limitation

The convergence map tests only whether sampled states satisfy the strict
criterion `||x(T)||_2 < epsilon` at one normalized-time horizon. The tolerance
is an Euclidean normalized-state tolerance. Results depend on the
horizon, tolerance, grid bounds, and resolution. Failing this test does not
show that a state lies outside the mathematical region of attraction, and
passing it does not certify asymptotic convergence.

The separate sampled Lyapunov checks also do not create a formal
continuous-state attraction-region certificate. A Lyapunov sublevel set is
not certified merely because it is plotted.

## Robustness experiment limitations

Noise, saturation, and parameter variation experiments test selected cases only.

They do not cover every possible uncertainty or disturbance.

## Lyapunov function limitation

The project uses a quadratic Lyapunov-style analysis based on the system setup.

More advanced nonlinear systems may require learned, non-quadratic, or problem-specific Lyapunov functions.

## Future improvement directions

- Add formal verification for neural-network controllers.
- Test larger and more nonlinear systems.
- Compare more controller types.
- Learn neural Lyapunov functions directly.
- Add stronger robustness and uncertainty analysis.
- Study safety constraints beyond actuator saturation.
