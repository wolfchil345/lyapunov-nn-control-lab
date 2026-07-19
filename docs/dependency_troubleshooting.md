# Dependency Troubleshooting

This guide explains how to fix common dependency and environment problems.

## First diagnostic command

Run the environment checker before changing packages:

```bash
python scripts/check_environment.py
```

## Git LFS is missing

If Git says `git-lfs was not found on your path`, install Git LFS:

```bash
sudo apt-get update
sudo apt-get install -y git-lfs
git lfs install
```

Then try pushing again:

```bash
git push
```

## PyTorch import error

If PyTorch fails to import with a shared library error, reinstall the CPU wheel:

```bash
python -m pip uninstall -y torch torchvision torchaudio
python -m pip cache purge
python -m pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu
python -c "import torch; print(torch.__version__)"
```

After reinstalling PyTorch, run:

```bash
python scripts/check_environment.py
python scripts/run_checks.py
```

## Dependency reset

If the virtual environment becomes messy, recreate it:

```bash
rm -rf .venv
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/run_checks.py
```

## Codespaces reset

If Codespaces behaves strangely, rebuild the container from the Codespaces command palette.

After rebuilding, run:

```bash
python scripts/check_environment.py
python scripts/run_checks.py
```

## When to ask for help

If checks still fail, copy the full terminal output from the first FAIL line onward.
