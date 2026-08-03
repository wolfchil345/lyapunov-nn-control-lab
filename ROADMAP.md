🌐 Language: [English](ROADMAP.md) | [日本語](ROADMAP.ja.md) | [한국어](ROADMAP.ko.md) | [ไทย](ROADMAP.th.md)

# Roadmap

## Near term

- Repeat neural training across multiple seeds and report distributions or confidence intervals.
- Add a CLI for selecting experiments and split expensive sweeps into focused commands.
- Record dependency versions and experiment configurations in generated reports.

## Control and robustness

- Compare PID, LQR, MPC, MLP, and KAN controllers under compatible settings.
- Add nonlinear plants, external disturbances, delays, quantization, and broader uncertainty sets.
- Extend region-of-attraction analysis and retain failure-case maps.

## Stability analysis

- Test alternative and learned Lyapunov functions.
- Add adaptive sampling near candidate violations.
- Compare empirical grid checks with formal neural-network verification tools.

## Physical validation

- Build a hardware-in-the-loop stage before operating real equipment.
- Define actuator, sensor, and safety constraints explicitly.
- Separate safety-certified components from research prototypes.

## Communication

- Keep the four-language documentation complete as features change.
- Add a poster and a short technical article backed by the same reproducible results.

The long-term goal is a compact platform for credible learning-based control experiments, not a claim that one neural controller solves control safety in general.
