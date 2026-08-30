🌐 ภาษา: [English](../en/ci_workflows.md) | [日本語](../ja/ci_workflows.md) | [한국어](../ko/ci_workflows.md) | [ไทย](../th/ci_workflows.md)

# คู่มือ CI workflows

โครงการนี้ใช้ GitHub Actions เพื่อตรวจสอบคุณภาพโค้ด สุขภาพของเอกสาร และความพร้อมของ repository

## ภาพรวมของ workflow

### Python tests

ไฟล์:

```text
.github/workflows/tests.yml
```

วัตถุประสงค์:

- รันชุดทดสอบ Python
- ยืนยันว่าโมดูลและสคริปต์หลักยังทำงานอยู่
- ปกป้องโครงการจากการพังของโค้ดโดยไม่ตั้งใจ

### Local checks (historical)

หมายเหตุ: workflow `local-checks` ของ GitHub Actions ในอดีตถูกนำออกจาก active workflows แล้ว การตรวจสอบก่อน push ในเครื่องยังถูกอธิบายไว้ผ่านคำสั่ง `quality_gate` และ `scripts/run_checks.py` สำหรับการตรวจสอบในเครื่อง

หากคุณดูแล workflow เฉพาะเครื่อง ควรเก็บไว้นอกไดเรกทอรี `.github/workflows/` ที่ใช้ร่วมกัน หรืออธิบายให้ชัดเจนว่าเป็นเครื่องมือส่วนตัวเพื่อหลีกเลี่ยงความสับสนของผู้ร่วมงาน

### Quality gate

ไฟล์:

```text
.github/workflows/quality-gate.yml
```

วัตถุประสงค์:

- รันการตรวจสอบความพร้อมขั้นสุดท้าย
- ตรวจสอบ project status, workflow badges, environment health, result inventory, tests, docs links และการรัน quick-start

### CodeQL

ไฟล์:

```text
.github/workflows/codeql.yml
```

วัตถุประสงค์:

- สแกนโค้ดเพื่อหาปัญหาด้านความปลอดภัยและความน่าเชื่อถือ
- ช่วยให้ repository ปลอดภัยขึ้นในฐานะโปรเจกต์พอร์ตโฟลิโอสาธารณะ

## ป้ายสถานะ

README มี workflow badges เพื่อให้ผู้เข้าชมเห็นสุขภาพของโครงการได้อย่างรวดเร็ว

ป้ายที่ต้องมี:

- Python tests badge สำหรับ `tests.yml`
- Quality gate badge สำหรับ `quality-gate.yml`

การมีอยู่ของ badge จะถูกตรวจด้วย:

```bash
python scripts/check_workflow_badges.py
```

## คำสั่งภายในเครื่องก่อน push

รัน:

```bash
python scripts/quality_gate.py
```

หรือ:

```bash
make quality-gate
```

## กฎการ merge ที่แนะนำ

ก่อน merge branch เข้า `main` ให้รัน quality gate ในเครื่อง และยืนยันว่า GitHub Actions ผ่านหลังจาก push แล้ว

## เมื่อ workflow ล้มเหลว

1. เปิด workflow run ที่ล้มเหลวใน GitHub
2. หาสtepแรกที่ล้มเหลว
3. รันคำสั่ง local ที่ตรงกัน
4. แก้ข้อผิดพลาดในเครื่อง
5. push อีกครั้งและตรวจสอบ Actions ใหม่

## หมายเหตุสำหรับพอร์ตโฟลิโอ

การที่ workflow ผ่านแสดงว่าโครงการนี้ไม่ใช่แค่โค้ดทดลอง แต่ได้รับการทดสอบ มีเอกสาร และดูแลเหมือนโปรเจกต์ซอฟต์แวร์วิจัยจริง
