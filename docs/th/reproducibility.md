🌐 ภาษา: [English](../en/reproducibility.md) | [日本語](../ja/reproducibility.md) | [한국어](../ko/reproducibility.md) | [ไทย](../th/reproducibility.md)

# คู่มือ Reproducibility

คู่มือนี้อธิบายวิธีทำซ้ำผลลัพธ์หลักของ Lyapunov Neural-Network Control Lab

## 1. Clone repository

```bash
git clone https://github.com/wolfchil345/lyapunov-nn-control-lab.git
cd lyapunov-nn-control-lab
```

## 2. สร้าง Python environment

```bash
python -m venv .venv
source .venv/bin/activate
```

บน Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

## 3. ติดตั้ง dependencies

```bash
python -m pip install -e ".[dev]"
```

## 4. รัน tests

```bash
python -m pytest
```

ควรให้ tests ผ่านทั้งหมดก่อนสร้างผลลัพธ์ใหม่

## 5. สร้างผลการทดลองใหม่

```bash
python main.py
```

คำสั่งนี้จะเผยแพร่ run แบบแยกภายใต้ `results/runs/<run_id>/` ก็ต่อเมื่อ artifacts ถูกสร้าง แฮช ทำ manifest และตรวจสอบเรียบร้อยแล้วเท่านั้น

เอาต์พุตสำคัญภายใน run ได้แก่:

- `manifest.json`
- `SHA256SUMS`
- `report.md`
- `model_architecture.png`
- `performance_metrics.csv`
- paired raw and aggregate ablation/noise CSV files
- normalized-coordinate figures
- `nn_controller.pt`

## 6. เปิด plots ที่สร้างขึ้น

ใน GitHub Codespaces หรือ VS Code ให้เปิดไฟล์จาก run directory ที่เลือกหนึ่งชุด

ตัวอย่าง:

```bash
code results/runs/<run_id>/model_architecture.png
code results/runs/<run_id>/report.md
```

## 7. หมายเหตุด้าน Reproducibility

- Python, NumPy, PyTorch CPU และ PyTorch CUDA generators ที่มีใช้งาน จะถูก seed ผ่าน project utility เดียวกัน fixed seeds ช่วยให้การเทียบผลบน CPU ในสภาพแวดล้อมเดียวกันทำซ้ำได้ดีขึ้น แต่ไม่ใช่การรับประกันแบบสากลสำหรับ bitwise deterministic CUDA หรือการรันข้ามแพลตฟอร์ม
- Stability weights ถูกเปรียบเทียบด้วย paired seeds ครอบคลุมทุก weight โดย raw per-seed trials ถูกแยกจาก aggregate means, sample standard deviations และ standard errors
- Measurement-noise amplitudes ใช้ common random-number realizations: standardized sequence เดียวกันของแต่ละ seed จะถูกสเกลตามแต่ละ amplitude การทำ matched seeds ซ้ำช่วยลดผลกวนจาก noise realization แต่ไม่สามารถกำจัดความไม่แน่นอนเชิงทดลองทั้งหมด
- อาจยังมีความต่างเชิงตัวเลขเล็กน้อยระหว่างระบบปฏิบัติการ, Python versions หรือ dependency versions
- โครงการนี้ใช้ empirical simulation และ grid-based Lyapunov checks ไม่ใช่ full formal proof สำหรับ neural-network controller
- plots ที่สร้างขึ้นมีไว้เป็น diagnostics เชิงปฏิบัติสำหรับ stability และ robustness
- finite-horizon convergence figures ใช้เฉพาะ strict criterion `||x(T)||_2 < epsilon` บน normalized-coordinate grid ที่ระบุไว้เท่านั้น และไม่ใช่ mathematical attraction-region certificates
- tracked files ที่ชื่อขึ้นต้นด้วย `region_of_attraction` เป็น historical pre-migration artifacts และตั้งใจไม่สร้างใหม่ใน terminology-only operation นี้
- official runs ต้องใช้ clean Git tree คำสั่ง `--allow-dirty` จะสร้าง exploratory run แบบชัดเจน โดย manifest จะบันทึก `git_dirty: true`
- `configuration_sha256` แฮช canonical sorted scientific configuration JSON โดย timestamps และ platform metadata ไม่มีผลต่อ configuration identity
- ตรวจสอบ run ด้วย `python scripts/verify_run.py results/runs/<run_id>`

## 8. Recommended verification workflow

ก่อนเชื่อถือผลการทดลองใหม่ ให้รัน:

```bash
python -m pytest
python main.py
python scripts/verify_run.py results/runs/<run_id>
python -m pytest
```

ขั้นตอนนี้ช่วยตรวจโค้ดก่อนการสร้างผล และยืนยันไฟล์ที่เผยแพร่อย่างครบถ้วนแม่นยำ
