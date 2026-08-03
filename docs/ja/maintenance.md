🌐 言語: [English](../en/maintenance.md) | [日本語](../ja/maintenance.md) | [한국어](../ko/maintenance.md) | [ไทย](../th/maintenance.md)

# メンテナンス

## 定期チェック

- 最新の `main` branchをpullし、open dependency updateを確認。
- `python scripts/project_status.py` と `make quality-gate` を実行。
- Workflow badgeと4つのdocumentation indexを確認。
- 追跡resultが意図せず再生成されていないか確認。
- 新behaviorにはtestを追加し、documentを4言語で更新。

## 新しいfile追加後

- 必要に応じてessential fileを `KEY_FILES` に追加。
- User-facing documentを全localized indexからlink。
- Scriptまたはcheckerにbehaviorを追加したらtestを追加。

## Demoまたはrelease前

Clean branchを使い、Git status、recent commit、limitationsを確認し、表示resultが現在のcodeとrelease noteに一致することを検証します。

Historical tagを削除したりpublished releaseをforce-updateしたりしません。
