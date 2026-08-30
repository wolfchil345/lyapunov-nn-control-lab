🌐 ภาษา: [English](../en/experiment_workflow.md) | [日本語](../ja/experiment_workflow.md) | [한국어](../ko/experiment_workflow.md) | [ไทย](../th/experiment_workflow.md)

# Experiment Workflow

คู่มือนี้อธิบาย workflow ที่แนะนำสำหรับการรันการทดลองใน Lyapunov Neural-Network Control Lab

## 1. ติดตั้ง dependencies

```bash
python -m pip install -e ".[dev]"
```

## 2. รันตัวอย่างแบบเร็ว

ใช้ quick-start script เพื่อตรวจสอบว่า basic simulation ทำงานได้

```bash
python examples/quick_start.py
```

## 3. รัน local checks

ก่อนรันการทดลองที่ใช้เวลานาน ให้ตรวจสอบว่า tests และ examples ผ่าน

```bash
python scripts/run_checks.py
```

## 4. ล้าง staging directories ที่ไม่สมบูรณ์

คำสั่งเสริมนี้จะลบเฉพาะ staging directories ที่ถูกทิ้งไว้เท่านั้น และจะไม่ลบ completed runs หรือ historical artifacts

```bash
python scripts/clean_results.py
```

## 5. รันการทดลองหลัก

รัน pipeline เต็มรูปแบบของการฝึก, simulation, robustness, plotting และ reporting:

```bash
python main.py
```

## 6. สรุปผลเชิงตัวเลข

แสดงสรุปแบบรวดเร็วของไฟล์ผลลัพธ์ CSV บนเทอร์มินัล:

```bash
python scripts/summarize_results.py
```

## 7. ตรวจสอบเอาต์พุตที่สร้างขึ้น

แต่ละ run ที่สำเร็จจะถูกแยกไว้ใน `results/runs/<run_id>/` ตรวจ `manifest.json`, `report.md` และ `SHA256SUMS` ก่อนนำผลไปใช้

ไฟล์ที่แนะนำให้ตรวจเป็นลำดับแรก:

- `performance_metrics.csv`
- `position_comparison.png`
- `phase_portrait.png`
- `lyapunov_contours.png`
- `finite_horizon_convergence_comparison.png`
- `report.md`
- `manifest.json`
- `SHA256SUMS`

## 8. ตีความผลลัพธ์

ใช้คู่มือเหล่านี้:

- `../th/results_interpretation.md`
- `../th/figures.md`
- `../th/limitations.md`

## 9. ก่อน commit การเปลี่ยนแปลง

รัน checks อีกครั้งก่อน commit:

```bash
python scripts/run_checks.py
git status
```

## Recommended complete workflow

```bash
python scripts/run_checks.py
python main.py
python scripts/list_results.py
python scripts/run_checks.py
```

official runs ต้องใช้ clean Git tree โดย manifest จะบันทึก paired seed sets แบบละเอียดสำหรับการทดลอง ablation และ common-random-number noise
