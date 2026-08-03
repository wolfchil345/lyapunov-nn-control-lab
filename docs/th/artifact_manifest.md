🌐 ภาษา: [English](../en/artifact_manifest.md) | [日本語](../ja/artifact_manifest.md) | [한국어](../ko/artifact_manifest.md) | [ไทย](../th/artifact_manifest.md)

# รายการ Artifact

## Source และการตั้งค่า

- `main.py`: orchestration การทดลองทั้งหมด
- `src/`: dynamics, controller, simulation, metric, robustness, reporting และ plotting
- `tests/`: การตรวจ behavior อัตโนมัติ
- `pyproject.toml`, `requirements.txt`: package metadata และ dependency

## สคริปต์ปฏิบัติงาน

- `scripts/run_checks.py`: ตรวจ documentation link, test และ quick start
- `scripts/quality_gate.py`: ลำดับตรวจ repository readiness ขั้นสุดท้าย
- `scripts/run_full_experiment.py`: cleanup, experiment และ summary pipeline
- `scripts/check_environment.py`, `scripts/project_status.py`, `scripts/list_results.py`: การวินิจฉัย

## หลักฐานที่สร้างขึ้น

- `results/*.png`: reference figure
- `results/performance_metrics.csv`: controller metric
- `results/stability_weight_ablation.csv`: ablation metric
- `results/experiment_report*.md`: report หลายภาษา
- `results/nn_controller.pt`: model state ที่สร้างและไม่ติดตามโดยตั้งใจ

ไฟล์ที่สร้างคือหลักฐานไม่ใช่ source ให้เก็บการตั้งค่าและตรวจ diff ก่อนแทนที่ artifact ที่ติดตาม
