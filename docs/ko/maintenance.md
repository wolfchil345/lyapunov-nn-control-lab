🌐 언어: [English](../en/maintenance.md) | [日本語](../ja/maintenance.md) | [한국어](../ko/maintenance.md) | [ไทย](../th/maintenance.md)

# Maintenance Guide

이 가이드는 새 features, docs, tests, workflows를 추가한 뒤 프로젝트를 건강하게 유지하는 방법을 설명합니다.

## Routine maintenance checklist

`main`에 merge하기 전에 다음 checklist를 실행하세요:

```bash
python scripts/check_environment.py
python scripts/project_status.py
python scripts/check_workflow_badges.py
python scripts/quality_gate.py
make checks
```

## Weekly project check

실행:

```bash
git switch main
git pull origin main
python scripts/quality_gate.py
```

그다음 확인:

- GitHub Actions가 통과 중인지.
- README badges가 보이는지.
- 중요한 docs가 `docs/{en,ja,ko,th}/index.md` 아래 적절한 language index에 연결되어 있는지.
- 새 scripts에 가능하면 tests가 있는지.
- 새 중요 파일이 `scripts/project_status.py`에서 추적되는지.

## After adding a new script

1. `scripts/` 아래에 script를 추가합니다.
2. script에 로직이 있으면 `tests/` 아래에 test를 추가합니다.
3. 자주 사용할 명령이면 Makefile shortcut을 추가합니다.
4. 사용자가 이해해야 하면 documentation을 추가합니다.
5. core project structure의 일부가 되면 `scripts/project_status.py`에 추가합니다.

## After adding a new document

1. 파일을 `docs/` 아래에 둡니다.
2. 적절한 `docs/<language>/index.md`에서 링크합니다.
3. 방문자에게 중요하면 `README.md`에서도 링크합니다.
4. core guide라면 `scripts/project_status.py`에 추가합니다.

## After adding or changing a workflow

1. 로컬에서 quality gate를 실행합니다.
2. workflow file이 `.github/workflows/` 아래 있는지 확인합니다.
3. 필요하면 README badges를 추가 또는 업데이트합니다.
4. `python scripts/check_workflow_badges.py`를 실행합니다.
5. Push 후 GitHub Actions 통과를 확인합니다.

## Before a demo or professor meeting

실행:

```bash
python scripts/quality_gate.py
python scripts/project_status.py
```

또한 README를 열어 project goal, badges, docs, quick-start instructions가 잘 보이는지 확인합니다.

## Portfolio note

유지관리되는 repository는 일회성 실험보다 더 강합니다. 이 checklist는 프로젝트가 안정적이고 문서화되어 있으며 리뷰 준비가 되었음을 보여주는 데 도움이 됩니다.
