# CI Workflows Guide

This project uses GitHub Actions to check code quality, documentation health, and repository readiness.

## Workflow overview

### Python tests

File:

```text
.github/workflows/tests.yml
```

Purpose:

- Runs the Python test suite.
- Confirms core modules and scripts still work.
- Protects the project from accidental code breakage.

### Local checks

File:

```text
.github/workflows/local-checks.yml
```

Purpose:

- Runs the same checks used during local development.
- Helps confirm that the repository works outside one machine.

### Quality gate

File:

```text
.github/workflows/quality-gate.yml
```

Purpose:

- Runs the final readiness check.
- Checks project status, workflow badges, environment health, result inventory, tests, docs links, and quick-start execution.

### CodeQL

File:

```text
.github/workflows/codeql.yml
```

Purpose:

- Scans code for security and reliability issues.
- Helps make the repository safer as a public portfolio project.

## Badges

The README includes workflow badges so visitors can quickly see project health.

Required badges:

- Python tests badge for `tests.yml`.
- Quality gate badge for `quality-gate.yml`.

Badge presence is checked by:

```bash
python scripts/check_workflow_badges.py
```

## Local command before pushing

Run:

```bash
python scripts/quality_gate.py
```

Or:

```bash
make quality-gate
```

## Recommended merge rule

Before merging a branch into `main`, run the quality gate locally and confirm GitHub Actions also pass after pushing.

## When a workflow fails

1. Open the failed workflow run on GitHub.
2. Find the first failed step.
3. Run the matching local command.
4. Fix the local error.
5. Push again and re-check Actions.

## Portfolio note

Passing workflows show that this project is not just experimental code. It is tested, documented, and maintained like a real research software project.
