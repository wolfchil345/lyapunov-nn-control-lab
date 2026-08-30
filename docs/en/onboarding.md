🌐 Language: [English](../en/onboarding.md) | [日本語](../ja/onboarding.md) | [한국어](../ko/onboarding.md) | [ไทย](../th/onboarding.md)

# Onboarding Guide

This guide helps a new user start working with the project.

## Who this guide is for

Use this guide if you are opening the repository for the first time, reviewing it as a portfolio project, or preparing to run the experiments.

## 1. Open the project

Recommended options:

- GitHub Codespaces for browser-based development.
- VS Code for local development.

## 2. Check the environment

Run:

```bash
python scripts/check_environment.py
```

This confirms that Python and key dependencies are available.

## 3. Run the quick start

Run:

```bash
python examples/quick_start.py
```

The quick-start example confirms that the main project modules can be imported and executed.

## 4. Run tests

Run:

```bash
python -m pytest
```

Or:

```bash
make test
```

## 5. Run the quality gate

Run:

```bash
python scripts/quality_gate.py
```

Or:

```bash
make quality-gate
```

The quality gate checks repository status, workflow badges, environment health, result inventory, structural four-language i18n parity, tests, docs links, and quick-start execution.

## 6. Read the key docs

Recommended first documents:

- `project_summary.md` for the project overview.
- `methodology.md` for the control and learning method.
- `experiment_workflow.md` for the experiment process.
- `results_interpretation.md` for reading outputs.
- `git_workflow.md` for branch and merge rules.
- `maintenance.md` for routine checks.

## 7. Before making changes

Create a feature branch:

```bash
git switch main
git pull origin main
git switch -c feature/example-name
```

After editing, run:

```bash
python scripts/quality_gate.py
make checks
```

## Portfolio note

This onboarding guide helps show that the repository is ready for other people to understand, run, review, and extend.
