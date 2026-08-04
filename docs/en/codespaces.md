🌐 Language: [English](../en/codespaces.md) | [日本語](../ja/codespaces.md) | [한국어](../ko/codespaces.md) | [ไทย](../th/codespaces.md)

# GitHub Codespaces Setup

The dev container uses Python 3.12, installs the editable project with the `dev` extra, recommends the project extensions, and enables pytest discovery.

## First commands

```bash
python scripts/check_environment.py
python examples/quick_start.py
make checks
```

## Development workflow

Create a feature branch, make focused changes, run `make quality-gate`, commit, push, and open a pull request. Store generated plots only when they are intentional reference artifacts.

Tracked reference images use normal Git; Git LFS is not required. If a Codespace becomes inconsistent, rebuild the container instead of committing environment-generated files.
