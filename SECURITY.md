🌐 Language: [English](SECURITY.md) | [日本語](SECURITY.ja.md) | [한국어](SECURITY.ko.md) | [ไทย](SECURITY.th.md)

# Security Policy

## Supported version

The latest version on `main` is supported. Historical releases remain available for reproducibility but do not receive fixes.

## Report a vulnerability

Do not publish exploit details in an issue. Contact the repository owner through an appropriate private GitHub channel and provide the affected version, reproduction steps, impact, and a minimal safe example.

## In scope

- Unsafe dependency or file-handling behavior.
- Credential, token, or private-data exposure.
- Unexpected command execution or untrusted-input handling.
- Security problems in workflows and project scripts.

## Separate research concerns

Numerical instability, model limitations, changed experiment results, and disagreements about scientific interpretation are not software vulnerabilities. Report them as research or bug issues without including sensitive information.

## Safe use

Use a virtual environment or Codespaces, inspect changes from forks, never commit secrets, and run the test and quality-gate workflows before executing modified experiment code.
