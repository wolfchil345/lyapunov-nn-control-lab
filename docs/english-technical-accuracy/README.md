# Lyapunov-aware Neural Control Lab — English Technical Accuracy Notes

This document records the authoritative, concise technical statements that
should appear in user-facing English documentation (README and docs/en/*).
It is intentionally compact and focused on accuracy; use it as the basis for
editing the repository README in later operations.

## Project overview

This repository implements tools and experiments for neural controllers that
are trained and evaluated with Lyapunov-aware losses and empirical
verification. The project focuses on controller imitation, transient
performance improvement, and robustness evaluation — not on proving formal
global stability for arbitrary systems.

Key concepts preserved here:
- Controller imitation and learned feedback design
- Sampled, empirical Lyapunov evaluation and decay-condition monitoring
- Finite-horizon convergence maps (legacy files may use older "region_of_attraction" names)
- Reproducible, provenance-aware experiment runs

## Scientific scope and limitations

- The nominal normalized second-order plant used throughout is dimensionless and defined by:

  - MASS = 1.0
  - DAMPING = 0.4
  - STIFFNESS = 2.0

- The linearized open-loop eigenvalues are approximately -0.2 ± 1.4j. The
  nominal linear plant is Hurwitz (as used in examples), so documentation
  must NOT claim the project stabilizes an open-loop unstable nominal plant.

- The coordinates are normalized and dimensionless. The canonical state is
  x = [q, v] with q a normalized position-like coordinate and v = dq/dτ the
  normalized velocity (τ = normalized time). Do not introduce SI units here.

## Normalized-state and API naming

- State norm: ||x||_2 = sqrt(q^2 + v^2)
- The quick-start examples expose a field named `settling_time_s`. This is a
  legacy name; it reports settling time in the code's normalized time units.
  Do not interpret `_s` as a claim of physical seconds unless a dimensional
  model is provided.

## Lyapunov methodology (accurate wording)

- Training uses a sampled Lyapunov-aware penalty of the form
  mean(ReLU(V_dot + α ||x||^2)) with DEFAULT_DECAY_MARGIN = 0.05.
- Evaluation is empirical and grid-sampled. Use terms like "sampled
  Lyapunov evaluation" or "empirical grid-based verification". Avoid
  statements that claim formal or global proofs of stability unless a
  mathematically valid certificate is produced.

## Finite-horizon convergence (terminology)

- The project computes finite-horizon convergence maps that report whether
  ||x(T)||_2 < ε for a chosen horizon T. These are NOT formal regions of
  attraction. Avoid the phrase "certified ROA" in current docs — instead
  refer to "finite-horizon convergence" or a "finite-horizon convergence map".

## Experimental randomization notes

- Stability-weight ablations (paired seeds): 700, 701, 702 (paired across
  compared settings).
- Noise-robustness experiments use seeds: 7, 8, 9 and scale a common
  realization across amplitudes.

## Result provenance and legacy artifacts

- Provenance-aware runs are stored under `results/runs/<run_id>/` and each
  completed run contains `manifest.json`, `report.md`, `SHA256SUMS`, and the
  scientific artifacts (e.g. the canonical committed run
  `20260807T182745Z_864ab09f`). That canonical run contains 20 artifacts.
- There are 15 legacy root-level artifacts in `results/` that predate the
  provenance schema. They are preserved byte-for-byte and marked in
  `results/legacy_SHA256SUMS`.

## CI and required checks (user-facing summary)

- CI uses three concepts: `Tests`, `Quality gate`, and `CodeQL`.
- Stable required checks:
  - `Tests / test` — aggregated test status (matrix: Python 3.10, 3.12)
  - `Quality gate / quality-gate` — single non-matrix job that runs
    provenance and checksum verification, documentation checks, and package
    build validation.
- The Quality gate verifies legacy checksums, provenance-aware runs,
  and runs an offline-capable external-wheel check. It installs the project
  before executing repository scripts.

## Quick start (accurate expectations)

To run the quick-start example locally in the repository virtualenv:

```
env PATH="$PWD/.venv/bin:$PATH" python examples/quick_start.py
```

Expected example outputs (numerical values are verified):

- final_state_norm: 0.001941
- settling_time_s: 3.25
- quadratic_cost: 6.510042

Use these committed values when citing quick-run numeric results.

## Installation (developer)

Install into a virtual environment and install dev dependencies:

```
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m pip check
```

## Results and reproducibility

- Use `scripts/verify_legacy_checksums.py` to check the 15 legacy artifacts.
- Use `scripts/verify_all_runs.py` to validate provenance-aware runs under
  `results/runs/`.

## Badges and workflow names

- Documentation must reference current workflows: `Tests`, `Quality gate`, and
  `CodeQL`. Do not reference any deleted `Local checks` workflow.

## Repository structure (concise)

- `src/lyapunov_nn_control_lab/` — package source
- `tests/` — test suite (pytest)
- `scripts/` — utility and verification scripts
- `examples/` — runnable quick-start examples
- `docs/` — textual documentation
- `results/` — committed experimental artifacts and provenance-aware runs
- `.github/workflows/` — CI workflows (Tests, Quality gate, CodeQL)

## Citations

- See `CITATION.cff` for citation metadata. Do not invent or expand
  bibliographic claims here; improve citations in a later documentation-only
  operation if needed.

---

This file is an accuracy-focused draft intended for integration into the
repository `README.md` in a subsequent operation. It intentionally does not
repeat all tutorial text; its goal is to be the authoritative source of
technical facts and phrasing for English documentation updates.
