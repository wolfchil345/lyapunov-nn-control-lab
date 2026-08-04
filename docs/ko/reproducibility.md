🌐 언어: [English](../en/reproducibility.md) | [日本語](../ja/reproducibility.md) | [한국어](../ko/reproducibility.md) | [ไทย](../th/reproducibility.md)

# 재현성

## 검사 재현

```bash
python -m pip install -e ".[dev]"
make checks
make quality-gate
```

## 실험 재현

추적 결과를 백업한 뒤 실행합니다.

```bash
python scripts/run_full_experiment.py
```

코드는 Python, NumPy, PyTorch 및 사용 가능한 CUDA 장치의 난수 시드를 설정합니다. 모든 결과에 커밋, Python 버전, 의존성 버전, 장치, 실험 설정을 기록하십시오.

## 예상 차이

시스템, 장치, 라이브러리 버전에 따라 작은 수치 차이나 PNG 인코딩 차이가 생길 수 있습니다. 고정 시드도 모든 CPU, GPU, BLAS 구현 또는 의존성 릴리스에서 비트 단위 동일성을 보장하지 않습니다. 변경을 채택하기 전에 수치 지표를 비교하고 그림의 픽셀 내용을 확인합니다.

## 범위

재현성은 문서화된 파이프라인이 동등한 근거를 다시 만들 수 있다는 뜻입니다. 표본 Lyapunov 또는 인력 영역 검사를 형식적 안정성 증명으로 바꾸지는 않습니다.
