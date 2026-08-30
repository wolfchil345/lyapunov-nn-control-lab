🌐 언어: [English](../en/ci_workflows.md) | [日本語](../ja/ci_workflows.md) | [한국어](../ko/ci_workflows.md) | [ไทย](../th/ci_workflows.md)

# CI 워크플로 가이드

이 프로젝트는 코드 품질, 문서 상태, 리포지토리 준비 상태를 확인하기 위해 GitHub Actions를 사용합니다.

## 워크플로 개요

### Python 테스트

파일:

```text
.github/workflows/tests.yml
```

목적:

- Python 테스트 스위트를 실행합니다.
- 핵심 모듈과 스크립트가 계속 동작하는지 확인합니다.
- 실수로 인한 코드 손상을 방지합니다.

### Local checks (historical)

참고: 이전의 `local-checks` GitHub Actions 워크플로는 active workflows에서 제거되었습니다. 로컬 pre-push 체크는 로컬 검증용 `quality_gate` 명령과 `scripts/run_checks.py`로 계속 문서화되어 있습니다.

로컬 전용 워크플로를 유지한다면 공유 `.github/workflows/` 디렉터리에 넣지 말고, 기여자를 혼동하지 않도록 개인용 유틸리티라고 명확히 문서화하세요.

### Quality gate

파일:

```text
.github/workflows/quality-gate.yml
```

목적:

- 최종 준비 상태 검사를 실행합니다.
- project status, workflow badges, environment health, result inventory, tests, docs links, quick-start execution을 확인합니다.

### CodeQL

파일:

```text
.github/workflows/codeql.yml
```

목적:

- 보안 및 신뢰성 문제를 코드 스캔합니다.
- 이 저장소를 공개 포트폴리오 프로젝트로 더 안전하게 만듭니다.

## 배지

README에는 workflow badge가 포함되어 있어 방문자가 프로젝트 상태를 빠르게 확인할 수 있습니다.

필수 배지:

- `tests.yml`용 Python tests badge.
- `quality-gate.yml`용 Quality gate badge.

배지 존재 여부는 다음으로 확인합니다.

```bash
python scripts/check_workflow_badges.py
```

## push 전에 실행할 로컬 명령

다음을 실행합니다.

```bash
python scripts/quality_gate.py
```

또는:

```bash
make quality-gate
```

## 권장 병합 규칙

브랜치를 `main`에 병합하기 전에 로컬에서 quality gate를 실행하고, push 후에도 GitHub Actions가 통과하는지 확인합니다.

## 워크플로가 실패했을 때

1. GitHub에서 실패한 workflow run을 엽니다.
2. 가장 먼저 실패한 step을 찾습니다.
3. 해당하는 로컬 명령을 실행합니다.
4. 로컬 오류를 수정합니다.
5. 다시 push하고 Actions를 재확인합니다.

## 포트폴리오 메모

워크플로가 통과한다는 것은 이 프로젝트가 단순한 실험 코드가 아니라, 실제 연구 소프트웨어 프로젝트처럼 테스트되고 문서화되며 유지보수되고 있음을 보여 줍니다.
