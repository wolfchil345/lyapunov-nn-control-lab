# Contributing Guide

Thank you for your interest in improving the Lyapunov Neural-Network Control Lab.

## Development setup

```bash
git clone https://github.com/wolfchil345/lyapunov-nn-control-lab.git
cd lyapunov-nn-control-lab
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run tests

```bash
python -m pytest
```

## Run experiments

```bash
python main.py
```

## Branch workflow

Create a feature branch before changing files:

```bash
git switch main
git pull origin main
git switch -c feature/your-feature-name
```

## Commit style

Use short, clear commit messages, for example:

```text
Add noise robustness experiment
Add reproducibility guide
Fix Lyapunov metric handling
```

## Suggested contribution areas

- new controller baselines
- additional robustness experiments
- improved plots and documentation
- tests for numerical utilities
- examples for beginners

## Before submitting changes

Run:

```bash
python -m pytest
python main.py
python -m pytest
```

This helps confirm that both tests and generated experiment outputs remain healthy.
