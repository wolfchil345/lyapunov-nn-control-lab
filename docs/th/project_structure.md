🌐 ภาษา: [English](../en/project_structure.md) | [日本語](../ja/project_structure.md) | [한국어](../ko/project_structure.md) | [ไทย](../th/project_structure.md)

# โครงสร้างโครงการ

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

## หน้าที่ของ Source

`src/system.py` กำหนด plant และ LQR baseline ส่วน controller training อยู่ใน `src/controllers.py`; simulation, metric, Lyapunov check, robustness study, plotting และ reporting แยกเป็น module ตามหน้าที่

## ไฟล์ที่สร้างขึ้น

`results/nn_controller.pt` ถูกสร้างและ ignore ส่วน plot, CSV และ report ที่เลือกจะติดตามเป็น reference evidence ให้ตรวจก่อน commit
