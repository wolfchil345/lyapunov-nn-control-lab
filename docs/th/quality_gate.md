🌐 ภาษา: [English](../en/quality_gate.md) | [日本語](../ja/quality_gate.md) | [한국어](../ko/quality_gate.md) | [ไทย](../th/quality_gate.md)

# คู่มือ Quality Gate

quality gate คือการตรวจสอบความพร้อมขั้นสุดท้ายก่อน merge, นำเสนอ, เผยแพร่ หรือส่งงาน

## สิ่งที่รัน

quality gate จะรัน:

```bash
python scripts/project_status.py
python scripts/check_workflow_badges.py
python scripts/check_environment.py
python scripts/list_results.py
python scripts/check_docs_i18n_parity.py
python scripts/run_checks.py
```

คำสั่งเหล่านี้ตรวจสอบโครงสร้างโครงการ สุขภาพของสภาพแวดล้อม ไฟล์ผลลัพธ์ที่สร้างขึ้น ความสอดคล้องเชิงโครงสร้างของ i18n 4 ภาษา ลิงก์เอกสาร การทดสอบ และการรัน quick-start

## วิธีรันในเครื่อง

รัน:

```bash
python scripts/quality_gate.py
```

หรือใช้:

```bash
make quality-gate
```

## ควรรันเมื่อใด

รัน quality gate ก่อน:

- merge feature branch เข้า `main`
- สาธิตงาน
- อัปเดตผลลัพธ์สำคัญ
- เตรียมรายงานหรือการนำเสนอ
- ส่ง repository เป็นหลักฐานพอร์ตโฟลิโอ

## วิธีอ่านความล้มเหลว

quality gate จะหยุดที่คำสั่งแรกที่ล้มเหลว

ถ้าล้มเหลว ให้อ่านคำสั่งที่แสดงหลัง:

```text
Quality gate failed at:
```

จากนั้นรันคำสั่งนั้นแยกเดี่ยวเพื่อดู error แบบละเอียด

## วิธีแก้ที่พบบ่อย

### ความล้มเหลวของสภาพแวดล้อม

รัน:

```bash
python scripts/check_environment.py
```

ตรวจสอบว่า Python packages, PyTorch หรือไฟล์โครงการหายไปหรือไม่

### ความล้มเหลวของการทดสอบ

รัน:

```bash
python -m pytest
```

แก้ไขการทดสอบแรกที่ล้มเหลวก่อนรัน quality gate ทั้งหมดอีกครั้ง

### ความล้มเหลวของลิงก์เอกสาร

รัน:

```bash
python scripts/check_docs_links.py
```

แก้ไขลิงก์เอกสารที่หายไปหรือไม่ถูกต้อง

### ปัญหาในรายการผลลัพธ์

รัน:

```bash
python scripts/list_results.py
```

ตรวจสอบว่าไฟล์ที่สร้างขึ้นหายไปหรือไม่ ชัดเจนหรือไม่ หรือไม่จำเป็นหรือไม่

## GitHub Actions

workflow `.github/workflows/quality-gate.yml` จะรัน quality gate อัตโนมัติเมื่อ push และ pull request ไปยัง `main`

## กฎสุดท้าย

อย่า merge การเปลี่ยนแปลงสำคัญจนกว่า quality gate จะผ่านในเครื่อง

## ความล้มเหลวของ workflow badge

รัน:

```bash
python scripts/check_workflow_badges.py
```

ตรวจสอบว่า README มี badge สำหรับ `tests.yml` และ `quality-gate.yml`
