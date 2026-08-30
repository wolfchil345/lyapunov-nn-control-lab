🌐 ภาษา: [English](../en/dependency_updates.md) | [日本語](../ja/dependency_updates.md) | [한국어](../ko/dependency_updates.md) | [ไทย](../th/dependency_updates.md)

# คู่มือ Dependency Updates

โครงการนี้ใช้ Dependabot เพื่อช่วยติดตามการอัปเดต dependency

## สิ่งที่ Dependabot ตรวจสอบ

- Python packages จากไฟล์ dependency หลัก
- GitHub Actions ที่ใช้ใน workflow files

## กำหนดเวลา

Dependabot ตรวจสอบการอัปเดตทุกสัปดาห์

## รายการตรวจทาน

เมื่อ Dependabot เปิด pull request สำหรับอัปเดต:

1. อ่าน package หรือ action ที่ถูกอัปเดต
2. รันการตรวจสอบในเครื่อง
3. ตรวจสอบ version ที่เปลี่ยนไปอย่างรอบคอบ
4. merge เฉพาะเมื่อ tests ผ่าน

```bash
python scripts/check_environment.py
make checks
```

## หมายเหตุด้านความปลอดภัย

สำหรับโค้ดงานวิจัย ควรทดสอบการอัปเดต dependency ก่อนนำไปใช้กับผลลัพธ์การทดลองสุดท้าย
