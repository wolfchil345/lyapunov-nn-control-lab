🌐 言語: [English](../en/project_structure.md) | [日本語](../ja/project_structure.md) | [한국어](../ko/project_structure.md) | [ไทย](../th/project_structure.md)

# プロジェクト構成

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

## Sourceの責務

`src/system.py` はplantとLQR baselineを定義します。Controller trainingは `src/controllers.py` にあり、simulation、metric、Lyapunov check、robustness study、plotting、reportingは目的別moduleに分かれています。

## 生成ファイル

`results/nn_controller.pt` は生成されignoreされます。選択したplot、CSV、reportはreference evidenceとして追跡します。Commit前に確認してください。
