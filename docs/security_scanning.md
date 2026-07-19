# Security Scanning

This project uses GitHub CodeQL to scan Python code for security issues.

## What CodeQL checks

CodeQL performs static analysis on the repository source code.

## When it runs

- On pushes to `main`.
- On pull requests targeting `main`.
- Weekly by schedule.

## Local checks before security review

Before merging changes, run:

```bash
python scripts/check_environment.py
make checks
```

## Review note

If CodeQL reports an alert, inspect the affected file and confirm whether the finding applies to this research code.
