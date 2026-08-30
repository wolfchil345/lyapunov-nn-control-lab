🌐 ภาษา: [English](../en/artifact_manifest.md) | [日本語](../ja/artifact_manifest.md) | [한국어](../ko/artifact_manifest.md) | [ไทย](../th/artifact_manifest.md)

# Artifact Manifest

เอกสารนี้อธิบายไฟล์หลักที่โครงการ Lyapunov neural network control lab สร้างขึ้นหรือใช้งาน

## Purpose

โครงการนี้สร้าง plots, reports และ summary files เพื่อประเมินสมรรถนะการควบคุมด้วย neural network, พฤติกรรมเสถียรภาพแบบ Lyapunov, robustness และ reproducibility

## Main source files

| Path | Purpose |
| --- | --- |
| `main.py` | รัน main experiment pipeline |
| `src/system.py` | กำหนดระบบ mass-spring-damper และ LQR reference controller |
| `src/controllers.py` | กำหนด neural network controllers, training data และ Lyapunov-aware training logic |
| `src/simulation.py` | จำลองพฤติกรรมของระบบวงปิด |
| `src/lyapunov.py` | คำนวณค่า Lyapunov และ Lyapunov derivative grid checks |
| `src/metrics.py` | คำนวณ performance metrics เช่น state error, control effort และ cost |
| `src/plotting.py` | สร้าง figures สำหรับ trajectories, phase portraits, robustness และ stability analysis |
| `src/lyapunov_nn_control_lab/finite_horizon_convergence.py` | ทดสอบ strict final-state tolerance บน bounded grid ที่ finite horizon ชัดเจน และบันทึก sampling metadata |

## Main scripts

| Path | Purpose |
| --- | --- |
| `scripts/run_checks.py` | รัน documentation link checks, unit tests และ quick start example |
| `scripts/run_full_experiment.py` | รัน full experiment workflow แบบไม่ทำลายข้อมูล |
| `scripts/verify_run.py` | ตรวจสอบ manifest ที่เสร็จแล้วและ SHA-256 checksums ที่บันทึกไว้ |
| `scripts/summarize_results.py` | สรุปผลลัพธ์การทดลองที่สร้างขึ้น |
| `scripts/clean_results.py` | ลบ result artifacts ที่สร้างขึ้นเมื่อจำเป็นต้องเริ่ม run ใหม่ |
| `scripts/check_docs_links.py` | ตรวจสอบ internal documentation links |

## Result artifacts

Historical files ยังคงเก็บไว้ตรง `results/` โดยตรง ส่วนเอาต์พุตใหม่ถูกแยกเก็บใน `results/runs/<run_id>/` และไม่ผสมกันข้าม run

| Artifact type | Meaning |
| --- | --- |
| Trajectory plots | เปรียบเทียบการตอบสนองสถานะของระบบภายใต้ตัวควบคุมต่างกัน |
| Control plots | เปรียบเทียบพฤติกรรมอินพุตควบคุมและผลของ saturation |
| Lyapunov plots | แสดงพฤติกรรมของฟังก์ชัน Lyapunov และบริเวณอนุพันธ์ |
| Finite-horizon convergence plots | รายงานผล sampled final-state tolerance พร้อม horizon, tolerance, bounds, grid และ counts อย่างชัดเจน; ไม่ใช่ attraction-region certificates |
| Robustness plots | แสดงพฤติกรรมตัวควบคุมภายใต้ noise หรือ parameter variation |
| CSV summaries | เก็บตัวเลข metrics สำหรับเปรียบเทียบและรายงานภายหลัง |
| Experiment reports | อธิบายผลการทดลองเชิงตัวเลขและภาพที่สำคัญ |

## Reproducibility note

ก่อนสร้างรูปสุดท้ายสำหรับ thesis ให้รัน local checks และสร้าง official run จาก clean Git state

```bash
python scripts/run_checks.py
python main.py
python scripts/verify_run.py results/runs/<run_id>
```

`manifest.json` จะบันทึก schema version, Git provenance, runtime versions,
effective configuration, exact seeds, pairing methodology, inventory, sizes และ hashes ดู policy ของ legacy artifacts ได้ที่ [`../../results/README.md`](../../results/README.md)

## How to use this document

ใช้ manifest นี้เมื่อต้องอธิบายโครงสร้างรีโพซิทอรีใน thesis, presentation หรือ research meeting
