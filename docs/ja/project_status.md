🌐 言語: [English](../en/project_status.md) | [日本語](../ja/project_status.md) | [한국어](../ko/project_status.md) | [ไทย](../th/project_status.md)

# プロジェクト状態

実行:

```bash
python scripts/project_status.py
```

このcommandは重要なrepository fileを確認し、documentation、script、test、workflow、result artifactの数を表示します。Inventory checkであり、testや科学的reviewの代わりではありません。

## 使用時期

- Fileを再編成した後。
- Pull request、demo、release前。
- Documentation、script、test、workflowを追加した後。

新しいfileが必須になったら `scripts/project_status.py` の `KEY_FILES` を更新します。[Quality gate](quality_gate.md)はこのstatus commandをより広いvalidation sequenceの一部として実行します。
