🌐 언어: [English](../en/git_workflow.md) | [日本語](../ja/git_workflow.md) | [한국어](../ko/git_workflow.md) | [ไทย](../th/git_workflow.md)

# Git 워크플로 가이드

이 가이드는 이 프로젝트에서 사용하는 브랜치 워크플로를 설명합니다.

## 기본 규칙

`main`에서 직접 작업하지 마세요.

feature 브랜치를 만들고, 하나의 집중된 개선을 수행한 뒤 테스트하고, 그 다음 `main`에 병합하세요.

## 표준 브랜치 흐름

```bash
git switch main
git pull origin main
git switch -c feature/example-name
```

파일을 수정한 뒤에는 다음 검사를 실행합니다.

```bash
python scripts/check_environment.py
python scripts/project_status.py
python scripts/check_workflow_badges.py
python scripts/quality_gate.py
make checks
```

커밋하고 push 합니다.

```bash
git add path/to/changed_file.md
git commit -m "Describe the focused change"
git push -u origin feature/example-name
```

`main`에 병합합니다.

```bash
git switch main
git pull origin main
git merge --no-ff feature/example-name
python scripts/quality_gate.py
make checks
git push origin main
```

feature 브랜치를 삭제합니다.

```bash
git branch -d feature/example-name
git push origin --delete feature/example-name
```

## 브랜치 이름 스타일

목적이 드러나는 짧은 이름을 사용하세요.

- `feature/add-new-guide`
- `feature/test-new-script`
- `feature/status-new-file`
- `feature/update-quality-gate`

## 커밋 메시지 스타일

명확한 동작을 나타내는 문구를 사용하세요.

- `Add maintenance guide`
- `Track maintenance guide in project status`
- `Add workflow badge checker tests`

## Git이 commit할 것이 없다고 말할 때

Git이 commit할 것이 없다고 말하면, 변경 사항이 이미 커밋되었을 수 있습니다.

다음을 실행합니다.

```bash
git status
git log --oneline -5
```

정상적인 커밋이 있다면 해당 브랜치를 push 하세요.

```bash
git push -u origin feature/example-name
```

## 포트폴리오 메모

이 워크플로는 프로젝트가 세심한 버전 관리, 분리된 변경, 반복 가능한 검사로 유지되고 있음을 보여 줍니다.
