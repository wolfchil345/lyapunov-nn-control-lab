🌐 언어: [English](../en/environment.md) | [日本語](../ja/environment.md) | [한국어](../ko/environment.md) | [ไทย](../th/environment.md)

# 환경 설정

## 요구 사항

- Python 3.10 이상. CI에서는 Python 3.10과 3.12를 테스트합니다.
- Git. 현재 추적하는 바이너리 산출물은 일반 Git을 사용하며 Git LFS가 필요하지 않습니다.
- 제공된 실험은 CPU만으로 실행할 수 있습니다.

## 설치

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Windows PowerShell에서는 `.venv\Scripts\Activate.ps1`로 가상 환경을 활성화합니다.

## 환경 확인

```bash
python scripts/check_environment.py
python examples/quick_start.py
make checks
```

명령은 저장소 루트에서 실행하세요. 불러오기에 실패하면 `.venv`를 다시 활성화하고 `python -m pip install -e ".[dev]"`로 재설치하세요.
