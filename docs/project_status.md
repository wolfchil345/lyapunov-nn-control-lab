# Project Status Guide

This guide explains how to use the project status checker.

## Purpose

The project status checker gives a quick overview of repository health.

It helps confirm that important files, folders, scripts, tests, workflows, and documentation are present.

## Command

Run:

```bash
python scripts/project_status.py
```

Or:

```bash
make status
```

## What it checks

The checker reports whether important project files exist.

Examples include:

- Core documentation files.
- Important scripts.
- Test files.
- GitHub Actions workflow files.
- Result and artifact folders.

## When to run it

Run the project status checker:

- Before committing a new feature.
- Before merging into `main`.
- After adding new documentation, scripts, tests, or workflows.
- Before showing the project as a portfolio or research artifact.

## Relationship with the quality gate

The quality gate runs the project status checker automatically.

Run:

```bash
python scripts/quality_gate.py
```

If the quality gate fails at the project status step, run `python scripts/project_status.py` directly to see the missing item.

## How to update it

When a new important file becomes part of the project structure, add it to the tracked file list inside:

```text
scripts/project_status.py
```

Then run:

```bash
python scripts/project_status.py
python scripts/quality_gate.py
```

## Portfolio note

This script helps show that the repository is organized like a maintained research software project, not just a folder of experiment code.
