🌐 言語: [English](SECURITY.md) | [日本語](SECURITY.ja.md) | [한국어](SECURITY.ko.md) | [ไทย](SECURITY.th.md)

# セキュリティポリシー

## 対応version

`main` のlatest versionをsupportします。Historical releaseはreproducibilityのため残しますがfixを受けません。

## 脆弱性の報告

Exploit detailをissueに公開しないでください。適切なprivate GitHub channelでrepository ownerへ連絡し、affected version、reproduction step、impact、最小限のsafe exampleを提供します。

## 対象

- Unsafe dependencyまたはfile-handling behavior。
- Credential、token、private-data exposure。
- Unexpected command executionまたはuntrusted-input handling。
- Workflowとproject scriptのsecurity problem。

## 別の研究上の問題

Numerical instability、model limitations、changed experiment result、scientific interpretationの意見差はsoftware vulnerabilityではありません。Sensitive informationを含めずresearchまたはbug issueとして報告します。

## 安全な利用

Virtual environmentまたはCodespacesを使用し、forkからの変更を確認し、secretをcommitせず、変更experiment code実行前にtestとquality-gate workflowを実行します。
