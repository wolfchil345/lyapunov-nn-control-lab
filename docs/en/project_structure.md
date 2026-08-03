🌐 Language: [English](../en/project_structure.md) | [日本語](../ja/project_structure.md) | [한국어](../ko/project_structure.md) | [ไทย](../th/project_structure.md)

# Project Structure

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

## Source responsibilities

`src/system.py` defines the plant and LQR baseline. Controller training is in `src/controllers.py`; simulation, metrics, Lyapunov checks, robustness studies, plotting, and reporting are separated into focused modules.

## Generated files

`results/nn_controller.pt` is generated and ignored. Selected plots, CSV files, and reports are tracked as reference evidence. Review them before committing.
