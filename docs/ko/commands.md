🌐 언어: [English](../en/commands.md) | [日本語](../ja/commands.md) | [한국어](../ko/commands.md) | [ไทย](../th/commands.md)

# 명령어 가이드

## 설정과 진단

```bash
python -m pip install -e ".[dev]"
python scripts/check_environment.py
```

## 실행과 검증

```bash
python examples/quick_start.py
python main.py
python -m pytest
make lint
make checks
make quality-gate
```

## 결과

```bash
python scripts/list_results.py
python scripts/summarize_results.py
python scripts/new_experiment_log.py "short description" --language ko
```

`python scripts/clean_results.py`는 알려진 생성 파일을 나열하는 드라이런입니다. 목록을 확인한 뒤에만 `python scripts/clean_results.py --yes`를 사용하십시오. 알 수 없는 파일과 실험 로그 디렉터리는 보존됩니다.

## Git

```bash
git status -sb
git switch -c feature/short-description
git add <files>
git commit -m "Describe the change"
git push -u origin feature/short-description
```
