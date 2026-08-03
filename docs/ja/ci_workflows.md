🌐 言語: [English](../en/ci_workflows.md) | [日本語](../ja/ci_workflows.md) | [한국어](../ko/ci_workflows.md) | [ไทย](../th/ci_workflows.md)

# CIワークフロー

| Workflow | 目的 |
|---|---|
| `tests.yml` | Python 3.12でPython test suiteを実行 |
| `local-checks.yml` | Python 3.11で `make checks` を実行 |
| `quality-gate.yml` | `main` とpull requestで完全なreadiness gateを実行 |
| `codeql.yml` | Push、pull request、weekly scheduleでPython codeを解析 |

## Push前

```bash
make checks
make quality-gate
```

Required branch checkにはGitHub表示と同じjob nameを使います。Workflowが失敗したら最初のfailing stepを確認し、そのcommandをlocalで再現します。

README badgeは `python scripts/check_workflow_badges.py` で検証します。
