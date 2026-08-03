🌐 언어: [English](../en/vscode.md) | [日本語](../ja/vscode.md) | [한국어](../ko/vscode.md) | [ไทย](../th/vscode.md)

# VS Code 설정

## 권장 확장 기능

- Python
- Pylance
- GitHub Actions

저장소 폴더를 열고 `.venv` interpreter를 선택한 뒤 통합 terminal에서 저장소 root 기준으로 명령을 실행합니다.

## 일반 workflow

```bash
python scripts/check_environment.py
python -m pytest
python main.py
make quality-gate
```

Pytest discovery는 `tests/`로 설정됩니다. VS Code가 다른 interpreter를 사용하면 `.venv`를 다시 선택하고 window를 reload하십시오.
