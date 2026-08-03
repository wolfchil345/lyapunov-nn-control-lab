🌐 Language: [English](../en/dependency_updates.md) | [日本語](../ja/dependency_updates.md) | [한국어](../ko/dependency_updates.md) | [ไทย](../th/dependency_updates.md)

# Dependency Updates

Dependabot checks Python packages and GitHub Actions on the configured schedule.

## Review checklist

1. Read the upstream release notes and identify breaking changes.
2. Update one dependency group at a time.
3. Run `python -m pip check`, `make checks`, and `make quality-gate`.
4. Regenerate scientific results only when the dependency can affect numerics or plotting.
5. Review every changed artifact and record meaningful numerical differences.

Do not merge an update only because CI is green; confirm that control behavior and documented results remain credible.
