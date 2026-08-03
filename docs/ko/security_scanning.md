🌐 언어: [English](../en/security_scanning.md) | [日本語](../ja/security_scanning.md) | [한국어](../ko/security_scanning.md) | [ไทย](../th/security_scanning.md)

# 보안 검사

CodeQL은 `main`으로 push할 때, `main`을 대상으로 하는 pull request가 생성될 때, 그리고 매주 정기적으로 Python 코드를 분석합니다.

## 로컬 준비

```bash
python -m pip check
make checks
make quality-gate
```

병합하기 전에 의존성 경고와 CodeQL 검사 결과를 확인하세요. 보안 검사를 통과했다고 해서 제어 정책의 안전성이나 안정성이 증명되는 것은 아닙니다. 소프트웨어 보안과 제어 시스템 안전은 서로 다른 검토 영역입니다.

의심되는 취약점은 저장소의 [보안 정책](../../SECURITY.ko.md)에 따라 비공개로 제보하세요. 공개 issue에 비밀 정보, 개인 데이터, 악용 세부 정보를 포함하지 마세요.
