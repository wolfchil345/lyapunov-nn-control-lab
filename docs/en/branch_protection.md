🌐 Language: [English](../en/branch_protection.md) | [日本語](../ja/branch_protection.md) | [한국어](../ko/branch_protection.md) | [ไทย](../th/branch_protection.md)

# Branch Protection

Protect the default branch with the active `Protect main` ruleset.

## Recommended rules

- Require a pull request before merging.
- Require conversations to be resolved.
- Require stable status checks and an up-to-date branch.
- Block force pushes and branch deletion.
- Use zero required approvals for a solo repository unless an independent reviewer is available.
- Allow an administrator bypass only for pull requests and emergencies.

Use the exact check names displayed by GitHub, normally the Python tests, local checks, quality gate, and CodeQL analysis.

Do not enable linear history unless the repository also changes its merge strategy. Test rules on a documentation pull request before relying on them for a release.
