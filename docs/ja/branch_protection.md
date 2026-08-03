🌐 言語: [English](../en/branch_protection.md) | [日本語](../ja/branch_protection.md) | [한국어](../ko/branch_protection.md) | [ไทย](../th/branch_protection.md)

# ブランチ保護

Activeな `Protect main` rulesetでdefault ブランチを保護します。

## 推奨ルール

- Merge前にプルリクエストを必須化。
- Conversation解決を必須化。
- 安定した状態チェックの通過と、ブランチが最新であることを必須にする。
- 強制プッシュとブランチ削除をブロックする。
- 個人リポジトリで独立したレビュアーがいない場合、必須承認数は0に設定する。
- 管理者によるバイパスは、プルリクエストと緊急時に限定する。

GitHub に表示される正確なチェック名を使います。通常は Python tests、Local checks、Quality gate、CodeQL analysis です。

リポジトリのマージ strategyも変えない限り線形 historyを有効にしません。リリースで使う前にドキュメント プルリクエストでruleをテストします。
