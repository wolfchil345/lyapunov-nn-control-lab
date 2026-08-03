🌐 언어: [English](../en/security_scanning.md) | [日本語](../ja/security_scanning.md) | [한국어](../ko/security_scanning.md) | [ไทย](../th/security_scanning.md)

# 보안 스캔

CodeQL은 `main` push, `main` 대상 pull request, weekly schedule에서 Python code를 분석합니다.

## Local 준비

```bash
python -m pip check
make checks
make quality-gate
```

Merge 전에 dependency alert와 CodeQL finding을 review합니다. Clean scan은 control policy의 safe 또는 stable을 증명하지 않습니다. Software security와 control-system safety는 다른 review domain입니다.

의심되는 취약점은 저장소 [security policy](../../SECURITY.ko.md)에 따라 비공개로 보고하십시오. Secret, private data, exploit detail을 public issue에 쓰지 마십시오.
