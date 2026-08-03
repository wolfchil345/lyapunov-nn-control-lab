🌐 언어: [English](../en/git_workflow.md) | [日本語](../ja/git_workflow.md) | [한국어](../ko/git_workflow.md) | [ไทย](../th/git_workflow.md)

# Git Workflow

## 표준 flow

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

Pull request를 open하고 required check를 기다리며 conversation을 해결한 뒤 protected `main` branch를 통해 merge합니다.

## 규칙

- Branch 하나에 목적 하나.
- 명시적 file을 stage하고 생성 artifact를 별도 review.
- 명확한 명령형 commit message 사용.
- `main`을 force-push하지 않고 published tag를 다시 쓰지 않으며 secret과 environment file을 commit하지 않음.
- `main` 동기화 후 merge된 feature branch 삭제.
