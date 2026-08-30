🌐 언어: [English](../en/quality_gate.md) | [日本語](../ja/quality_gate.md) | [한국어](../ko/quality_gate.md) | [ไทย](../th/quality_gate.md)

# Quality Gate 가이드

quality gate는 병합, 발표, 릴리스, 제출 전에 수행하는 최종 준비 상태 검사입니다.

## 실행 내용

quality gate는 다음을 실행합니다.

```bash
python scripts/project_status.py
python scripts/check_workflow_badges.py
python scripts/check_environment.py
python scripts/list_results.py
python scripts/check_docs_i18n_parity.py
python scripts/run_checks.py
```

이 명령들은 프로젝트 구조, 환경 상태, 생성된 결과 파일, 4개 언어 i18n 구조 정합성, 문서 링크, 테스트, quick-start 실행을 확인합니다.

## 로컬에서 실행하는 방법

다음을 실행합니다.

```bash
python scripts/quality_gate.py
```

또는:

```bash
make quality-gate
```

## 실행 시점

다음 전에 quality gate를 실행하세요.

- feature 브랜치를 `main`에 병합하기 전
- 데모를 하기 전
- 중요한 결과를 업데이트하기 전
- 보고서나 발표 자료를 준비하기 전
- 리포지토리를 포트폴리오 증거로 제출하기 전

## 실패를 읽는 방법

quality gate는 처음 실패한 명령에서 멈춥니다.

실패하면 다음 뒤에 표시된 명령을 읽으세요.

```text
Quality gate failed at:
```

그 명령만 단독으로 실행하면 자세한 오류를 확인할 수 있습니다.

## 흔한 해결책

### 환경 실패

다음을 실행합니다.

```bash
python scripts/check_environment.py
```

Python 패키지, PyTorch, 프로젝트 파일이 빠져 있는지 확인하세요.

### 테스트 실패

다음을 실행합니다.

```bash
python -m pytest
```

quality gate 전체를 다시 실행하기 전에 먼저 실패한 테스트를 고치세요.

### 문서 링크 실패

다음을 실행합니다.

```bash
python scripts/check_docs_links.py
```

누락되었거나 잘못된 문서 링크를 수정하세요.

### 결과 목록 문제

다음을 실행합니다.

```bash
python scripts/list_results.py
```

생성된 파일이 누락되었는지, 불분명한지, 또는 필요 없는지 확인하세요.

## GitHub Actions

워크플로 `.github/workflows/quality-gate.yml`는 `main`으로의 push와 pull request에 대해 quality gate를 자동으로 실행합니다.

## 최종 규칙

중요한 변경은 로컬에서 quality gate가 통과할 때까지 병합하지 마세요.

## workflow badge 실패

다음을 실행합니다.

```bash
python scripts/check_workflow_badges.py
```

README에 `tests.yml`과 `quality-gate.yml` 배지가 포함되어 있는지 확인하세요.
