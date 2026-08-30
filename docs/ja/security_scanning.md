🌐 言語: [English](../en/security_scanning.md) | [日本語](../ja/security_scanning.md) | [한국어](../ko/security_scanning.md) | [ไทย](../th/security_scanning.md)

# Security Scanning ガイド

このプロジェクトでは、GitHub CodeQL を使って Python コードのセキュリティ問題をスキャンします。

## CodeQL が確認する内容

CodeQL はリポジトリのソースコードに対して静的解析を行います。

## 実行タイミング

- `main` への push 時。
- `main` 宛ての pull request 時。
- 毎週のスケジュール実行時。

## セキュリティレビュー前のローカル確認

変更をマージする前に次を実行します。

```bash
python scripts/check_environment.py
make checks
```

## レビューノート

CodeQL が alert を報告したら、該当ファイルを確認し、その finding がこの研究コードに当てはまるかどうかを判断してください。
