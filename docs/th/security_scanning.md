🌐 ภาษา: [English](../en/security_scanning.md) | [日本語](../ja/security_scanning.md) | [한국어](../ko/security_scanning.md) | [ไทย](../th/security_scanning.md)

# คู่มือ Security Scanning

โครงการนี้ใช้ GitHub CodeQL เพื่อสแกนหาปัญหาด้านความปลอดภัยในโค้ด Python

## สิ่งที่ CodeQL ตรวจสอบ

CodeQL ทำ static analysis บนซอร์สโค้ดใน repository

## ช่วงเวลาที่รัน

- เมื่อ push ไปที่ `main`
- เมื่อมี pull request ที่มุ่งไปยัง `main`
- ตามกำหนดทุกสัปดาห์

## การตรวจสอบในเครื่องก่อน security review

ก่อน merge การเปลี่ยนแปลง ให้รัน:

```bash
python scripts/check_environment.py
make checks
```

## หมายเหตุการตรวจทาน

หาก CodeQL รายงาน alert ให้ตรวจไฟล์ที่ได้รับผลกระทบและยืนยันว่าผลนั้นมีผลกับโค้ดงานวิจัยนี้จริงหรือไม่
