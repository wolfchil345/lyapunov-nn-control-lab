🌐 Language: [English](../en/codespaces.md) | [日本語](../ja/codespaces.md) | [한국어](../ko/codespaces.md) | [ไทย](../th/codespaces.md)

# GitHub Codespaces Setup

The dev container uses Python 3.11, installs `requirements.txt`, recommends the project extensions, and enables pytest discovery.

## First commands

```bash
python scripts/check_environment.py
python examples/quick_start.py
make checks
```

## Development workflow

Create a feature branch, make focused changes, run `make quality-gate`, commit, push, and open a pull request. Store generated plots only when they are intentional reference artifacts.

Git LFS must be available before checking out tracked binary assets. If a Codespace becomes inconsistent, rebuild the container instead of committing environment-generated files.
