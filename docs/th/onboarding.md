🌐 ภาษา: [English](../en/onboarding.md) | [日本語](../ja/onboarding.md) | [한국어](../ko/onboarding.md) | [ไทย](../th/onboarding.md)

# คู่มือเริ่มต้นใช้งาน

คู่มือนี้ช่วยให้ผู้ใช้ใหม่เริ่มทำงานกับโครงการได้

## คู่มือนี้เหมาะกับใคร

ใช้คู่มือนี้หากคุณเพิ่งเปิด repository นี้เป็นครั้งแรก กำลังตรวจดูในฐานะโปรเจกต์พอร์ตโฟลิโอ หรือกำลังเตรียมรันการทดลอง

## 1. เปิดโครงการ

ตัวเลือกที่แนะนำ:

- GitHub Codespaces สำหรับการพัฒนาบนเบราว์เซอร์
- VS Code สำหรับการพัฒนาในเครื่อง

## 2. ตรวจสอบสภาพแวดล้อม

รัน:

```bash
python scripts/check_environment.py
```

คำสั่งนี้จะยืนยันว่า Python และ dependency สำคัญพร้อมใช้งาน

## 3. รัน quick start

รัน:

```bash
python examples/quick_start.py
```

ตัวอย่าง quick start นี้ยืนยันว่าโมดูลหลักของโครงการสามารถ import และรันได้

## 4. รันทดสอบ

รัน:

```bash
python -m pytest
```

หรือ:

```bash
make test
```

## 5. รัน quality gate

รัน:

```bash
python scripts/quality_gate.py
```

หรือ:

```bash
make quality-gate
```

quality gate จะตรวจสอบสถานะ repository, workflow badge, สุขภาพของสภาพแวดล้อม, รายการผลลัพธ์, ความสอดคล้องเชิงโครงสร้างของ i18n 4 ภาษา, การทดสอบ, ลิงก์เอกสาร และการรัน quick start

## 6. อ่านเอกสารสำคัญ

เอกสารที่แนะนำให้อ่านก่อน:

- `project_summary.md` สำหรับภาพรวมของโครงการ
- `methodology.md` สำหรับวิธีการควบคุมและการเรียนรู้
- `experiment_workflow.md` สำหรับขั้นตอนการทดลอง
- `results_interpretation.md` สำหรับการอ่านผลลัพธ์
- `git_workflow.md` สำหรับกฎการทำ branch และ merge
- `maintenance.md` สำหรับการตรวจสอบตามปกติ

## 7. ก่อนทำการเปลี่ยนแปลง

สร้าง feature branch:

```bash
git switch main
git pull origin main
git switch -c feature/example-name
```

หลังแก้ไขเสร็จ รัน:

```bash
python scripts/quality_gate.py
make checks
```

## หมายเหตุสำหรับพอร์ตโฟลิโอ

คู่มือเริ่มต้นใช้งานนี้ช่วยแสดงว่า repository นี้พร้อมให้ผู้อื่นเข้าใจ รัน ตรวจทาน และขยายต่อได้
