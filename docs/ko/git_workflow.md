🌐 언어: [English](../en/git_workflow.md) | [日本語](../ja/git_workflow.md) | [한국어](../ko/git_workflow.md) | [ไทย](../th/git_workflow.md)

# Git 워크플로

## 표준 작업 흐름

```bash
git switch main
git pull --ff-only origin main
git switch -c docs/short-description
# edit and validate
git status -sb
git diff --check
make quality-gate
git add <intentional-files>
git commit -m "Describe the change"
git push -u origin docs/short-description
```

풀 리퀘스트를 생성하고 필수 검사를 기다리며 conversation을 해결한 뒤 보호된 `main` 브랜치를 통해 병합합니다.

## 규칙

- 브랜치 하나에 목적 하나.
- 명시적 파일을 단계하고 생성 산출물를 별도 검토.
- 명확한 명령형 커밋 메시지 사용.
- `main`에 강제 push하지 않고, 공개된 태그를 덮어쓰지 않으며, 비밀 정보와 환경 파일을 커밋하지 않음.
- `main`을 동기화한 후 병합된 작업 브랜치를 삭제함.
