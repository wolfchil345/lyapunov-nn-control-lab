🌐 언어: [English](../en/dependency_updates.md) | [日本語](../ja/dependency_updates.md) | [한국어](../ko/dependency_updates.md) | [ไทย](../th/dependency_updates.md)

# Dependency Updates 가이드

이 프로젝트는 Dependabot을 사용해 의존성 업데이트를 모니터링합니다.

## Dependabot이 확인하는 내용

- 루트 의존성 파일의 Python 패키지
- workflow 파일에서 사용하는 GitHub Actions

## 일정

Dependabot은 매주 업데이트를 확인합니다.

## 검토 체크리스트

Dependabot이 업데이트 pull request를 열면:

1. 업데이트되는 package 또는 action을 읽습니다.
2. 로컬 체크를 실행합니다.
3. 변경된 version을 신중하게 확인합니다.
4. 테스트가 통과할 때만 merge합니다.

```bash
python scripts/check_environment.py
make checks
```

## 안전 메모

연구 코드에서는 의존성 업데이트를 최종 실험 결과에 사용하기 전에 반드시 테스트해야 합니다.
