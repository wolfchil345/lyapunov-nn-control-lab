🌐 언어: [English](../en/commands.md) | [日本語](../ja/commands.md) | [한국어](../ko/commands.md) | [ไทย](../th/commands.md)

# 명령어 가이드

## 설정과 진단

```bash
python -m pip install -e .
python scripts/check_environment.py
```

## 실행과 검증

```bash
python examples/quick_start.py
python main.py
python -m pytest
make checks
make quality-gate
```

## 결과

```bash
python scripts/list_results.py
python scripts/summarize_results.py
python scripts/new_experiment_log.py "short description" --language ko
```

`python scripts/clean_results.py`는 `results/`의 모든 파일을 삭제합니다. 보관할 참조 산출물를 먼저 백업하십시오.

## Git

```bash
git status -sb
git switch -c feature/short-description
git add <files>
git commit -m "Describe the change"
git push -u origin feature/short-description
```
