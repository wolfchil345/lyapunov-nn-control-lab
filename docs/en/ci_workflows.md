🌐 Language: [English](../en/ci_workflows.md) | [日本語](../ja/ci_workflows.md) | [한국어](../ko/ci_workflows.md) | [ไทย](../th/ci_workflows.md)

# CI Workflows

| Workflow | Purpose |
|---|---|
| `tests.yml` | Run the Python test suite on Python 3.12 |
| `local-checks.yml` | Run `make checks` on Python 3.11 |
| `quality-gate.yml` | Run the full readiness gate on `main` and pull requests |
| `codeql.yml` | Analyze Python code on pushes, pull requests, and a weekly schedule |

## Before pushing

```bash
make checks
make quality-gate
```

Required branch checks should use the exact job names shown by GitHub. If a workflow fails, inspect the first failing step and reproduce its command locally.

Badges in the README are validated by `python scripts/check_workflow_badges.py`.
