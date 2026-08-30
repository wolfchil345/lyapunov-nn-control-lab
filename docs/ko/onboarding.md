🌐 언어: [English](../en/onboarding.md) | [日本語](../ja/onboarding.md) | [한국어](../ko/onboarding.md) | [ไทย](../th/onboarding.md)

# 온보딩 가이드

이 가이드는 새 사용자가 프로젝트를 시작하는 데 도움을 줍니다.

## 대상 독자

처음으로 리포지토리를 열어 보는 경우, 포트폴리오 프로젝트로 검토하는 경우, 또는 실험을 실행할 준비를 하는 경우에 이 가이드를 사용하세요.

## 1. 프로젝트 열기

권장 항목:

- 브라우저 기반 개발에는 GitHub Codespaces.
- 로컬 개발에는 VS Code.

## 2. 환경 확인

다음을 실행합니다.

```bash
python scripts/check_environment.py
```

이 명령은 Python과 주요 의존성이 사용 가능한지 확인합니다.

## 3. 빠른 시작 실행

다음을 실행합니다.

```bash
python examples/quick_start.py
```

이 quick start 예제는 주요 프로젝트 모듈을 import하고 실행할 수 있는지 확인합니다.

## 4. 테스트 실행

다음을 실행합니다.

```bash
python -m pytest
```

또는:

```bash
make test
```

## 5. quality gate 실행

다음을 실행합니다.

```bash
python scripts/quality_gate.py
```

또는:

```bash
make quality-gate
```

quality gate는 리포지토리 상태, workflow badge, 환경 상태, 결과 목록, 4개 언어 i18n 구조 정합성, 테스트, docs 링크, quick start 실행을 확인합니다.

## 6. 핵심 문서 읽기

처음 읽기를 권장하는 문서:

- `project_summary.md`는 프로젝트 개요.
- `methodology.md`는 제어와 학습 방법.
- `experiment_workflow.md`는 실험 절차.
- `results_interpretation.md`는 출력 해석.
- `git_workflow.md`는 브랜치와 병합 규칙.
- `maintenance.md`는 정기 점검.

## 7. 변경하기 전에

feature 브랜치를 만듭니다.

```bash
git switch main
git pull origin main
git switch -c feature/example-name
```

편집 후에는 다음을 실행합니다.

```bash
python scripts/quality_gate.py
make checks
```

## 포트폴리오 메모

이 온보딩 가이드는 리포지토리가 다른 사람이 이해하고, 실행하고, 검토하고, 확장할 수 있는 상태임을 보여 주는 데 도움이 됩니다.
