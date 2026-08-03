🌐 언어: [English](../en/reproducibility.md) | [日本語](../ja/reproducibility.md) | [한국어](../ko/reproducibility.md) | [ไทย](../th/reproducibility.md)

# 재현성

## 검사 재현

```bash
python -m pip install -e .
make checks
make quality-gate
```

## 실험 재현

추적 result를 backup한 뒤 실행합니다.

```bash
python scripts/run_full_experiment.py
```

Code는 Python, NumPy, PyTorch seed를 설정합니다. 모든 result에 commit, Python version, dependency version, experiment setting을 기록하십시오.

## 예상 차이

System과 library version에 따라 작은 수치 또는 PNG encoding 차이가 생길 수 있습니다. 변경을 채택하기 전에 수치 metric을 비교하고 figure의 pixel content를 확인합니다.

## 범위

재현성은 documented pipeline이 동등한 근거를 다시 만들 수 있다는 뜻입니다. 표본 Lyapunov 또는 region-of-attraction check를 형식적 안정성 증명으로 바꾸지는 않습니다.
