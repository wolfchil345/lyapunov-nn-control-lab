🌐 Language: [English](../en/security_scanning.md) | [日本語](../ja/security_scanning.md) | [한국어](../ko/security_scanning.md) | [ไทย](../th/security_scanning.md)

# Security Scanning

CodeQL analyzes Python code on pushes to `main`, pull requests targeting `main`, and a weekly schedule.

## Local preparation

```bash
python -m pip check
make checks
make quality-gate
```

Review dependency alerts and CodeQL findings before merge. A clean scan does not prove that a control policy is safe or stable; software security and control-system safety are different review domains.

Report suspected vulnerabilities privately using the repository [security policy](../../SECURITY.md). Never include secrets, private data, or exploit details in a public issue.
