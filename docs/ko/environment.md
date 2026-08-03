🌐 언어: [English](../en/environment.md) | [日本語](../ja/environment.md) | [한국어](../ko/environment.md) | [ไทย](../th/environment.md)

# 환경 설정

## 요구 사항

- Python 3.10 이상. CI는 Python 3.11과 3.12를 사용합니다.
- Git 및 추적되는 binary asset을 위한 Git LFS.
- 포함된 실험은 CPU로 실행할 수 있습니다.

## 설치

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

Windows PowerShell에서는 `.venv\Scripts\Activate.ps1`을 사용합니다.

## 환경 확인

```bash
python scripts/check_environment.py
python examples/quick_start.py
make checks
```

명령은 저장소 root에서 실행하십시오. import가 실패하면 `.venv`를 다시 활성화하고 `python -m pip install -e .`를 실행합니다.
