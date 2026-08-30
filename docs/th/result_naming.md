🌐 ภาษา: [English](../en/result_naming.md) | [日本語](../ja/result_naming.md) | [한국어](../ko/result_naming.md) | [ไทย](../th/result_naming.md)

# คู่มือ Result File Naming

เอาต์พุตปัจจุบันยังคงใช้ชื่อไฟล์แบบบอกความหมายภายใน directory ที่แยกเป็น `results/runs/<run_id>/` โดย run ID ให้ข้อมูล identity ด้านเวลา/commit อยู่แล้ว จึงไม่จำเป็นต้องใส่ timestamp ใน filename และ `manifest.json` จะบันทึกไฟล์จริงแต่ละรายการพร้อม role, size และ SHA-256 digest

ใช้คู่มือนี้เพื่อให้เอาต์พุตการทดลองเป็นระเบียบและเปรียบเทียบได้ง่าย

## ทำไม naming จึงสำคัญ

ผลการทดลองจะเปรียบเทียบยากเมื่อชื่อ plots, metrics และ reports ไม่ชัดเจน กฎ naming ที่สม่ำเสมอช่วยเชื่อมแต่ละไฟล์เอาต์พุตกับค่าตั้งต้นที่ใช้สร้างไฟล์นั้น

## รูปแบบที่แนะนำ

ใช้ชื่อที่มี date, controller type, experiment type และ setting ที่สำคัญ

```text
YYYYMMDD_controller_experiment_setting.ext
```

## ตัวอย่าง

```text
20260719_nn_trajectory_seed0.png
20260719_lqr_metrics_baseline.csv
20260719_nn_lyapunov_grid21.csv
20260719_nn_robustness_noise005.png
20260719_nn_finite_horizon_convergence_t8_tol01_grid31.png
20260719_experiment_report_seed0.md
```

## ส่วนประกอบชื่อที่แนะนำ

- Date: `YYYYMMDD`
- Controller: `lqr`, `nn`, `kan` หรือ `comparison`
- Experiment type: `trajectory`, `metrics`, `lyapunov`, `robustness`, `finite_horizon_convergence` หรือ `report`
- Setting: seed, grid size, noise level, epoch count หรือ parameter variation

## ชื่อไฟล์ที่ดี

- ชัดเจน
- ใช้อักษรพิมพ์เล็ก
- ใช้ underscores
- มี setting ที่สำคัญที่สุด
- ไม่มี spaces

## สิ่งที่ควรหลีกเลี่ยง

- `final.png`
- `new_result.csv`
- `test2.md`
- `really_final_plot.png`

## กฎการเปรียบเทียบ

เมื่อเปรียบเทียบสอง runs ให้แน่ใจว่าชื่อไฟล์บอกได้ว่ามีอะไรเปลี่ยนไป

## กฎด้านเอกสาร

หากผลลัพธ์สำคัญพอจะเก็บไว้ ให้บันทึกใน experiment log template

## แสดงรายการ result files ปัจจุบัน

ใช้ result inventory script ก่อนทำ report, demo หรือ release review:

```bash
python scripts/list_results.py
```

หรือใช้ Makefile shortcut:

```bash
make list-results
```
