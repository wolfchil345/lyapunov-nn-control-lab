🌐 언어: [English](../en/codespaces.md) | [日本語](../ja/codespaces.md) | [한국어](../ko/codespaces.md) | [ไทย](../th/codespaces.md)

# GitHub Codespaces 설정

이 가이드는 GitHub Codespaces에서 이 저장소를 사용하는 방법을 설명합니다.

## 목적

이 저장소에는 `.devcontainer/devcontainer.json`이 포함되어 있어 Codespaces가 Python 개발 환경을 자동으로 준비할 수 있습니다.

## 개발 컨테이너가 하는 일

- Python 3.11을 사용합니다.
- Codespace 생성 후 `pyproject.toml`에서 패키지와 개발 의존성을 설치합니다.
- Python, Pylance, GitHub Actions 확장을 권장합니다.
- `tests/` 폴더에서 pytest 탐지를 활성화합니다.

## Codespaces를 연 뒤 처음 실행할 명령

```bash
python scripts/run_checks.py
```

## 실험 실행

```bash
python main.py
```

## 일반적인 Git 워크플로

```bash
git switch main
git pull origin main
git switch -c feature/my-change
python scripts/run_checks.py
git status
```
