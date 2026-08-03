🌐 言語: [English](../en/dependency_updates.md) | [日本語](../ja/dependency_updates.md) | [한국어](../ko/dependency_updates.md) | [ไทย](../th/dependency_updates.md)

# 依存関係の更新

Dependabotは設定されたscheduleでPython packageとGitHub Actionsを確認します。

## Review checklist

1. 上流のrelease noteを読み、breaking changeを確認します。
2. 一度に一つのdependency groupだけ更新します。
3. `python -m pip check`、`make checks`、`make quality-gate` を実行します。
4. 数値やplotに影響し得るdependencyの場合だけ科学的結果を再生成します。
5. 変更された全artifactを確認し、意味のある数値差を記録します。

CIがgreenという理由だけでmergeせず、制御挙動とドキュメント化された結果の妥当性を確認してください。
