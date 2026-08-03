🌐 Language: [English](../en/pull_request_review.md) | [日本語](../ja/pull_request_review.md) | [한국어](../ko/pull_request_review.md) | [ไทย](../th/pull_request_review.md)

# Pull Request Review

## General review

- [ ] The title and summary explain one focused change.
- [ ] Tests and required checks pass.
- [ ] Documentation is updated in all four languages when user-facing behavior changes.
- [ ] Generated files are intentionally included or ignored.
- [ ] Conversations are resolved before merge.

## Scientific review

- [ ] Changes to seeds, plant parameters, controller architecture, losses, or evaluation settings are explicit.
- [ ] Numerical and figure diffs are explained.
- [ ] Sampled checks are not presented as formal proofs.
- [ ] Failure cases and limitations remain visible.

## Local commands

```bash
git diff --check
make checks
make quality-gate
```

Merge only through the protected `main` branch after the latest commit passes all required checks.
