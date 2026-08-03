🌐 言語: [English](../en/ci_workflows.md) | [日本語](../ja/ci_workflows.md) | [한국어](../ko/ci_workflows.md) | [ไทย](../th/ci_workflows.md)

# CIワークフロー

| ワークフロー | 目的 |
|---|---|
| `tests.yml` | Python 3.12でPythonテストスイートを実行 |
| `local-checks.yml` | Python 3.11で `make checks` を実行 |
| `quality-gate.yml` | `main` とプルリクエストで完全な準備状況チェックを実行 |
| `codeql.yml` | プッシュ、プルリクエスト、週次スケジュールでPythonコードを解析 |

## プッシュ前

```bash
make checks
make quality-gate
```

必須のブランチチェックには、GitHubに表示されるジョブ名を正確に使います。ワークフローが失敗した場合は、最初に失敗した手順を確認し、そのコマンドをローカルで再現します。

READMEのバッジは `python scripts/check_workflow_badges.py` で検証します。
