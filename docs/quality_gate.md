# Quality Gate Guide

The quality gate is the final project readiness check before merging, presenting, releasing, or submitting work.

## What it runs

The quality gate runs:

```bash
python scripts/project_status.py
python scripts/check_environment.py
python scripts/list_results.py
python scripts/run_checks.py
```

These commands check project structure, environment health, generated result files, documentation links, tests, and quick-start execution.

## How to run it locally

Run:

```bash
python scripts/quality_gate.py
```

Or use:

```bash
make quality-gate
```

## When to run it

Run the quality gate before:

- Merging a feature branch into `main`.
- Giving a demo.
- Updating important results.
- Preparing a report or presentation.
- Submitting the repository as portfolio evidence.

## How to read failures

The quality gate stops at the first failing command.

If it fails, read the command shown after:

```text
Quality gate failed at:
```

Then run that command by itself to see the detailed error.

## Common fixes

### Environment failure

Run:

```bash
python scripts/check_environment.py
```

Check whether Python packages, PyTorch, or project files are missing.

### Test failure

Run:

```bash
python -m pytest
```

Fix the first failing test before retrying the whole quality gate.

### Documentation link failure

Run:

```bash
python scripts/check_docs_links.py
```

Fix missing or incorrect documentation links.

### Result inventory issue

Run:

```bash
python scripts/list_results.py
```

Check whether generated files are missing, unclear, or not needed.

## GitHub Actions

The workflow `.github/workflows/quality-gate.yml` runs the quality gate automatically on pushes and pull requests to `main`.

## Final rule

Do not merge important changes until the quality gate passes locally.
