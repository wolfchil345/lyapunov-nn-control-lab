🌐 言語: [English](../en/ci_workflows.md) | [日本語](../ja/ci_workflows.md) | [한국어](../ko/ci_workflows.md) | [ไทย](../th/ci_workflows.md)

# CIワークフロー

| ワークフロー | 目的 |
|---|---|
| `tests.yml` | Python 3.12でPython テスト suiteを実行 |
| `local-checks.yml` | Python 3.11で `make checks` を実行 |
| `quality-gate.yml` | `main` とプルリクエストで完全なreadiness ゲートを実行 |
| `codeql.yml` | push、pull request、週次スケジュールでPythonコードを解析 |

## Push前

```bash
make checks
make quality-gate
```

必須のブランチチェックには、GitHubに表示されるジョブ名を正確に使います。ワークフローが失敗した場合は、最初に失敗した手順を確認し、そのコマンドをローカルで再現します。

README badgeは `python scripts/check_workflow_badges.py` で検証します。
