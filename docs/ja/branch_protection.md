🌐 言語: [English](../en/branch_protection.md) | [日本語](../ja/branch_protection.md) | [한국어](../ko/branch_protection.md) | [ไทย](../th/branch_protection.md)

# ブランチ保護

Activeな `Protect main` rulesetでdefault branchを保護します。

## 推奨ルール

- Merge前にpull requestを必須化。
- Conversation解決を必須化。
- 安定したstatus checkとup-to-date branchを必須化。
- Force pushとbranch deletionをblock。
- Solo repositoryでは独立reviewerがいない限りrequired approvalを0に設定。
- Administrator bypassはpull requestおよびemergencyだけに限定。

GitHubに表示される正確なcheck nameを使います。通常はPython tests、local checks、quality gate、CodeQL analysisです。

Repositoryのmerge strategyも変えない限りlinear historyを有効にしません。Releaseで使う前にdocumentation pull requestでruleをtestします。
