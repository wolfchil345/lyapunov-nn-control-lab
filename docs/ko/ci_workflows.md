🌐 언어: [English](../en/ci_workflows.md) | [日本語](../ja/ci_workflows.md) | [한국어](../ko/ci_workflows.md) | [ไทย](../th/ci_workflows.md)

# CI Workflow

| Workflow | 목적 |
|---|---|
| `tests.yml` | Python 3.12에서 Python test suite 실행 |
| `local-checks.yml` | Python 3.11에서 `make checks` 실행 |
| `quality-gate.yml` | `main`과 pull request에서 전체 readiness gate 실행 |
| `codeql.yml` | Push, pull request, weekly schedule에서 Python code 분석 |

## Push 전

```bash
make checks
make quality-gate
```

Required branch check는 GitHub에 표시되는 정확한 job name을 사용해야 합니다. Workflow가 실패하면 첫 failing step을 확인하고 그 command를 local에서 재현합니다.

README badge는 `python scripts/check_workflow_badges.py`로 검증합니다.
