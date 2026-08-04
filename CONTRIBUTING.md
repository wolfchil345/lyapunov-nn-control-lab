🌐 Language: [English](CONTRIBUTING.md) | [日本語](CONTRIBUTING.ja.md) | [한국어](CONTRIBUTING.ko.md) | [ไทย](CONTRIBUTING.th.md)

# Contributing

Thank you for helping improve Lyapunov NN Control Lab.

## Setup

```bash
git clone https://github.com/wolfchil345/lyapunov-nn-control-lab.git
cd lyapunov-nn-control-lab
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

## Workflow

1. Create a focused branch from current `main`.
2. Keep scientific, code, and documentation changes clearly scoped.
3. Add tests for behavior changes.
4. Update viewer-facing documentation in English, Japanese, Korean, and Thai.
5. Run `git diff --check`, `make checks`, and `make quality-gate`.
6. Open a pull request and wait for every required check before merging.

## Scientific results

Do not regenerate or commit results unless the change requires it. Record the seed and experiment settings, review every numerical and figure diff, and describe sampled stability evidence accurately.

## Good contributions

- Controller baselines and carefully designed robustness experiments.
- Tests for numerical, reporting, and documentation tools.
- Clearer plots, examples, translations, and methodology explanations.
- Reproducibility, safety, and failure-case improvements.

Use short imperative commit messages, such as `Add noise robustness test` or `Clarify Lyapunov limitations`.
