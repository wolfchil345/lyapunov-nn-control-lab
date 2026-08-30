🌐 언어: [English](../en/vscode.md) | [日本語](../ja/vscode.md) | [한국어](../ko/vscode.md) | [ไทย](../th/vscode.md)

# VS Code 설정

이 가이드는 VS Code 또는 GitHub Codespaces에서 프로젝트를 사용하는 방법을 설명합니다.

## 권장 확장 기능

이 저장소에는 Python 개발과 GitHub Actions를 위한 권장 확장 기능을 담은 `.vscode/extensions.json`이 포함되어 있습니다.

권장 확장 기능:

- Python
- Pylance
- GitHub Actions

## 프로젝트 열기

리포지토리 루트 폴더를 VS Code에서 여세요. 루트 폴더에는 `README.md`, `main.py`, `src/`, `tests/`, `scripts/`가 있어야 합니다.

## Python 인터프리터 선택

가상 환경을 만든 뒤 VS Code에서 `.venv`의 인터프리터를 선택하세요.

## 터미널에서 검사 실행

```bash
python scripts/run_checks.py
```

## VS Code에서 테스트 실행

이 저장소에는 VS Code가 `tests/` 폴더의 pytest 테스트를 찾을 수 있도록 `.vscode/settings.json`이 포함되어 있습니다.

## Codespaces 참고

Codespaces에서는 터미널을 열고 로컬과 같은 명령을 실행합니다.

```bash
python -m pip install -e ".[dev]"
python scripts/run_checks.py
```

## 일반적인 작업 흐름

```bash
git switch main
git pull origin main
git switch -c feature/my-new-change
python scripts/run_checks.py
git status
```
