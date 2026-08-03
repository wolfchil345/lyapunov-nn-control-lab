🌐 언어: [English](../en/project_structure.md) | [日本語](../ja/project_structure.md) | [한국어](../ko/project_structure.md) | [ไทย](../th/project_structure.md)

# 프로젝트 구조

```text
lyapunov-nn-control-lab/
├── main.py                    # 전체 실험 파이프라인
├── src/                       # 제어, 시뮬레이션, 분석, 보고서 생성
├── tests/                     # 자동 테스트
├── scripts/                   # 검사, 유지관리, 실험 보조 도구
├── examples/                  # 실행 가능한 최소 예제
├── docs/{en,ja,ko,th}/        # 언어별 문서
├── results/                   # 참조 그림, CSV 데이터, 보고서
├── .github/                   # workflow와 기여 템플릿
├── pyproject.toml             # 패키지 정보와 의존성
└── README*.md                 # 4개 언어의 시작 페이지
```

## 소스의 역할

`src/system.py`는 플랜트와 LQR 기준 제어기를 정의합니다. 제어기 학습은 `src/controllers.py`에 있으며, 시뮬레이션, 평가 지표, Lyapunov 검사, 강인성 실험, 그림 작성, 보고서 생성은 목적별 모듈로 나뉘어 있습니다.

## 생성 파일

`results/nn_controller.pt`는 실행 중 생성되며 Git에서 무시됩니다. 일부 그림, CSV 파일, 보고서는 참조 검증 자료로 추적합니다. 커밋하기 전에 내용을 검토하세요.
