🌐 Language: [English](../en/quality_gate.md) | [日本語](../ja/quality_gate.md) | [한국어](../ko/quality_gate.md) | [ไทย](../th/quality_gate.md)

# Quality Gate

Run the final readiness check with:

```bash
make quality-gate
```

It runs project status, workflow-badge validation, environment checks, result inventory, Markdown-link checks, the complete test suite, and the quick-start example.

## Use it before

- Opening or merging a pull request.
- Replacing tracked experiment results.
- A demo, submission, or release.

## Failure handling

Read the first failed command, fix that cause, and rerun the gate. Do not skip a failed stage or broaden the change unnecessarily. A passing gate confirms repository consistency; it does not validate scientific claims beyond the implemented tests.

GitHub Actions runs the same command through `.github/workflows/quality-gate.yml`.
