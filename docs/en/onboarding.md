🌐 Language: [English](../en/onboarding.md) | [日本語](../ja/onboarding.md) | [한국어](../ko/onboarding.md) | [ไทย](../th/onboarding.md)

# Onboarding Guide

## First hour

1. Read the localized README and [project summary](project_summary.md).
2. Follow the [environment guide](environment.md).
3. Run `python examples/quick_start.py`.
4. Run `make checks` and inspect `results/`.
5. Read the [methodology](methodology.md), [experiment workflow](experiment_workflow.md), and [limitations](limitations.md).

## Before changing code

```bash
git switch main
git pull --ff-only origin main
git switch -c feature/short-description
```

Keep scientific changes separate from documentation changes, record experiment settings, and run `make quality-gate` before requesting review.

Use the [Git workflow](git_workflow.md) and [contribution guide](../../CONTRIBUTING.md) for the complete process.
