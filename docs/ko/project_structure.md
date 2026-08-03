🌐 언어: [English](../en/project_structure.md) | [日本語](../ja/project_structure.md) | [한국어](../ko/project_structure.md) | [ไทย](../th/project_structure.md)

# 프로젝트 구조

```text
lyapunov-nn-control-lab/
├── main.py                    # Full experiment pipeline
├── src/                       # Control, simulation, analysis, reporting
├── tests/                     # Automated tests
├── scripts/                   # Checks, maintenance, experiment helpers
├── examples/                  # Minimal runnable example
├── docs/{en,ja,ko,th}/        # Localized documentation
├── results/                   # Reference figures, CSV data, reports
├── .github/                   # Workflows and contribution templates
├── pyproject.toml             # Package metadata and dependencies
└── README*.md                 # Four localized entry pages
```

## Source 역할

`src/system.py`는 plant와 LQR baseline을 정의합니다. Controller training은 `src/controllers.py`에 있고 simulation, metric, Lyapunov check, robustness study, plotting, reporting은 집중된 module로 나뉩니다.

## 생성 파일

`results/nn_controller.pt`는 생성되며 ignore됩니다. 선택한 plot, CSV, report는 reference evidence로 추적합니다. Commit 전에 검토하십시오.
