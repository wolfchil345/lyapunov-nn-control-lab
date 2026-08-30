🌐 언어: [English](../en/branch_protection.md) | [日本語](../ja/branch_protection.md) | [한국어](../ko/branch_protection.md) | [ไทย](../th/branch_protection.md)

# 브랜치 보호 가이드

이 가이드는 리포지토리에 권장되는 브랜치 보호 설정을 설명합니다.

## 목표

`main`을 보호하여 중요한 연구 코드가 병합되기 전에 검토와 확인을 거치도록 합니다.

## 권장 설정

- 병합 전에 pull request를 요구합니다.
- 병합 전에 status check 통과를 요구합니다.
- 병합 전에 브랜치가 최신 상태일 것을 요구합니다.
- 최종 논문이나 포트폴리오 작업에 사용하는 경우 관리자도 포함합니다.
- `main`에 대한 force push를 제한합니다.
- `main`의 브랜치 삭제를 제한합니다.

## 권장 필수 검사

- 로컬 검사
- CodeQL

## 병합 전 로컬 체크리스트

```bash
python scripts/check_environment.py
make checks
git status
```

## 권장 워크플로

각 변경마다 feature 브랜치를 만들고, 로컬에서 검사를 실행한 뒤, GitHub 검사가 통과한 후에만 병합합니다.

## 참고

이 문서는 권장 사항일 뿐입니다. 실제 브랜치 보호는 GitHub 리포지토리 설정에서 구성해야 합니다.
