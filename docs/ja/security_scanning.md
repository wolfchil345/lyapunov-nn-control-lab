🌐 言語: [English](../en/security_scanning.md) | [日本語](../ja/security_scanning.md) | [한국어](../ko/security_scanning.md) | [ไทย](../th/security_scanning.md)

# セキュリティスキャン

CodeQLは `main` へのpush、`main` を対象とするpull request、weekly scheduleでPython codeを解析します。

## Local準備

```bash
python -m pip check
make checks
make quality-gate
```

Merge前にdependency alertとCodeQL findingをreviewします。Clean scanはcontrol policyのsafeまたはstableを証明しません。Software securityとcontrol-system safetyは別のreview domainです。

脆弱性の疑いはrepositoryの[security policy](../../SECURITY.ja.md)に従って非公開で報告します。Secret、private data、exploit detailをpublic issueへ書かないでください。
