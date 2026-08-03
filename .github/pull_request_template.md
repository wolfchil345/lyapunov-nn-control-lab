🌐 Language: [English](pull_request_template.md) | [日本語](PULL_REQUEST_TEMPLATE/pull_request_template.ja.md) | [한국어](PULL_REQUEST_TEMPLATE/pull_request_template.ko.md) | [ไทย](PULL_REQUEST_TEMPLATE/pull_request_template.th.md)

# Pull Request

## Summary

Describe the focused change and why it is needed.

## Type

- [ ] Bug fix
- [ ] Experiment or scientific change
- [ ] Documentation or translation
- [ ] Test, tooling, or refactoring

## Scientific and generated-file impact

- Changed seeds, parameters, architecture, losses, or metrics:
- Generated plots, CSV files, reports, or model artifacts changed:
- Expected numerical differences and limitations:

## Validation

- [ ] `git diff --check`
- [ ] `make checks`
- [ ] `make quality-gate`
- [ ] User-facing documentation updated in all four languages when required
- [ ] Generated artifacts reviewed and intentionally included

## Follow-up

List unresolved work or write `None`.
