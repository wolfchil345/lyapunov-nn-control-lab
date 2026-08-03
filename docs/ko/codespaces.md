🌐 언어: [English](../en/codespaces.md) | [日本語](../ja/codespaces.md) | [한국어](../ko/codespaces.md) | [ไทย](../th/codespaces.md)

# GitHub Codespaces 설정

dev container는 Python 3.11을 사용하고 `requirements.txt`를 설치하며 권장 확장 기능과 pytest discovery를 설정합니다.

## 첫 명령

```bash
python scripts/check_environment.py
python examples/quick_start.py
make checks
```

## 개발 workflow

feature branch를 만들고 범위가 명확한 변경을 수행한 뒤 `make quality-gate`, commit, push, pull request 순서로 진행합니다. 생성 그림은 의도한 reference artifact일 때만 저장합니다.

추적되는 binary asset을 checkout하기 전에 Git LFS가 필요합니다. Codespace가 불안정하면 환경 생성 파일을 commit하지 말고 container를 rebuild하십시오.
