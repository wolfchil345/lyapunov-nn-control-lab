🌐 言語: [English](../en/dependency_updates.md) | [日本語](../ja/dependency_updates.md) | [한국어](../ko/dependency_updates.md) | [ไทย](../th/dependency_updates.md)

# 依存関係の更新

Dependabotは設定されたスケジュールでPythonパッケージとGitHub Actionsを確認します。

## レビュー チェックリスト

1. 上流のリリースノートを読み、互換性を損なう変更がないか確認します。
2. 一度に一つの依存関係グループだけを更新します。
3. `python -m pip check`、`make checks`、`make quality-gate` を実行します。
4. 数値や図に影響し得る依存関係の場合だけ科学的結果を再生成します。
5. 変更された全成果物を確認し、意味のある数値差を記録します。

CIが成功したという理由だけでマージせず、制御挙動とドキュメント化された結果の妥当性も確認してください。
