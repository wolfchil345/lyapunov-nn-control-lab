🌐 언어: [English](../en/project_status.md) | [日本語](../ja/project_status.md) | [한국어](../ko/project_status.md) | [ไทย](../th/project_status.md)

# Project Status Guide

이 가이드는 project status checker 사용 방법을 설명합니다.

## Purpose

project status checker는 repository health를 빠르게 개요로 보여줍니다.

중요한 files, folders, scripts, tests, workflows, documentation이 존재하는지 확인하는 데 도움이 됩니다.

## Command

실행:

```bash
python scripts/project_status.py
```

또는:

```bash
make status
```

## What it checks

checker는 중요한 project files 존재 여부를 보고합니다.

예시:

- Core documentation files.
- finite-horizon convergence evaluator와 해당 regression tests.
- Important scripts.
- Test files.
- GitHub Actions workflow files.
- Legacy result files와 manifest-verified provenance-aware runs.

각 provenance-aware run에 대해 checker는 run 개수와 complete artifact/checksum verification을 통과한 manifest 개수를 보고합니다. root-level historical files는 current manifest-backed runs로 취급하지 않고 legacy/unverified로 별도 분류됩니다.

## When to run it

다음 시점에 project status checker를 실행하세요:

- 새 기능을 commit하기 전
- `main`에 merge하기 전
- 새 documentation, scripts, tests, workflows를 추가한 후
- 프로젝트를 portfolio 또는 연구 산출물로 보여주기 전

## Relationship with the quality gate

quality gate는 project status checker를 자동으로 실행합니다.

실행:

```bash
python scripts/quality_gate.py
```

quality gate가 project status step에서 실패하면 `python scripts/project_status.py`를 직접 실행해 누락 항목을 확인하세요.

## How to update it

새 중요한 파일이 project structure의 일부가 되면 다음 tracked file list에 추가하세요:

```text
scripts/project_status.py
```

그다음 실행:

```bash
python scripts/project_status.py
python scripts/quality_gate.py
```

## Portfolio note

이 script는 repository가 단순한 실험 코드 폴더가 아니라 유지관리되는 research software project처럼 구성되어 있음을 보여주는 데 도움이 됩니다.
