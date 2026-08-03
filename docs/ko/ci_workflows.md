🌐 언어: [English](../en/ci_workflows.md) | [日本語](../ja/ci_workflows.md) | [한국어](../ko/ci_workflows.md) | [ไทย](../th/ci_workflows.md)

# CI 워크플로

| 워크플로 | 목적 |
|---|---|
| `tests.yml` | Python 3.12에서 Python 테스트 모음 실행 |
| `local-checks.yml` | Python 3.11에서 `make checks` 실행 |
| `quality-gate.yml` | `main`과 풀 리퀘스트에서 전체 준비 상태 검사 실행 |
| `codeql.yml` | 푸시, 풀 리퀘스트, 주간 스케줄에서 Python 코드 분석 |

## 푸시 전

```bash
make checks
make quality-gate
```

필수 브랜치 검사에는 GitHub에 표시되는 작업 이름을 정확히 사용해야 합니다. 워크플로가 실패하면 처음 실패한 단계를 확인하고 그 명령을 로컬에서 재현합니다.

README 배지는 `python scripts/check_workflow_badges.py`로 검증합니다.
