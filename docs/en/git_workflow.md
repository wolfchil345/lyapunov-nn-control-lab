🌐 Language: [English](../en/git_workflow.md) | [日本語](../ja/git_workflow.md) | [한국어](../ko/git_workflow.md) | [ไทย](../th/git_workflow.md)

# Git Workflow

## Standard flow

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

Open a pull request, wait for required checks, resolve conversations, and merge through the protected `main` branch.

## Rules

- One branch and one purpose per change.
- Stage explicit files; review generated artifacts separately.
- Use clear imperative commit messages.
- Never force-push `main`, rewrite published tags, or commit secrets and environment files.
- Delete merged feature branches after synchronizing `main`.
