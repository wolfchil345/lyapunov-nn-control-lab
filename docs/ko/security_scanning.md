🌐 언어: [English](../en/security_scanning.md) | [日本語](../ja/security_scanning.md) | [한국어](../ko/security_scanning.md) | [ไทย](../th/security_scanning.md)

# Security Scanning 가이드

이 프로젝트는 GitHub CodeQL을 사용해 Python 코드의 보안 문제를 스캔합니다.

## CodeQL이 확인하는 내용

CodeQL은 저장소 소스 코드에 대해 정적 분석을 수행합니다.

## 실행 시점

- `main`으로 push할 때
- `main`을 대상으로 하는 pull request일 때
- 매주 일정 실행 시

## 보안 검토 전 로컬 확인

변경 사항을 병합하기 전에 다음을 실행하세요.

```bash
python scripts/check_environment.py
make checks
```

## 검토 메모

CodeQL이 alert를 보고하면 해당 파일을 확인하고, 그 finding이 이 연구 코드에 실제로 적용되는지 판단하세요.
