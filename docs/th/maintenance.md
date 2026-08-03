🌐 ภาษา: [English](../en/maintenance.md) | [日本語](../ja/maintenance.md) | [한국어](../ko/maintenance.md) | [ไทย](../th/maintenance.md)

# การบำรุงรักษา

## Checklist ประจำ

- Pull `main` branch ปัจจุบันและตรวจ open dependency update
- รัน `python scripts/project_status.py` และ `make quality-gate`
- ตรวจ workflow badge และ documentation index ทั้งสี่ภาษา
- ตรวจ tracked result ว่าไม่ได้สร้างใหม่โดยไม่ตั้งใจ
- เพิ่ม test เมื่อมี behavior ใหม่และอัปเดตเอกสารทั้งสี่ภาษา

## หลังเพิ่ม file ใหม่

- เพิ่ม essential file ใน `KEY_FILES` เมื่อเหมาะสม
- Link user-facing document จาก localized index ทุกภาษา
- เพิ่ม test เมื่อ script หรือ checker มี behavior ใหม่

## ก่อน Demo หรือ release

ใช้ clean branch ตรวจ Git status, recent commit, limitations และยืนยันว่า result ที่แสดงตรงกับ code และ release note ปัจจุบัน

อย่าลบ historical tag หรือ force-update published release
