🌐 言語: [English](../en/quality_gate.md) | [日本語](../ja/quality_gate.md) | [한국어](../ko/quality_gate.md) | [ไทย](../th/quality_gate.md)

# Quality Gate

最終readiness checkを実行:

```bash
make quality-gate
```

Project status、workflow badge validation、environment check、result inventory、Markdown link check、完全なtest suite、quick-start exampleを実行します。

## 使用前

- Pull requestをopenまたはmergeする前。
- 追跡experiment resultを置き換える前。
- Demo、submission、release前。

## Failure対応

最初に失敗したcommandを読み、その原因を直し、gateを再実行します。失敗stageをskipしたり、変更範囲を不必要に広げたりしません。Passはrepository consistencyを確認しますが、implemented testを超える科学的主張を検証しません。

GitHub Actionsは `.github/workflows/quality-gate.yml` から同じcommandを実行します。
