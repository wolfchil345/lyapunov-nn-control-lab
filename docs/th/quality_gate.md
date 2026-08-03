🌐 ภาษา: [English](../en/quality_gate.md) | [日本語](../ja/quality_gate.md) | [한국어](../ko/quality_gate.md) | [ไทย](../th/quality_gate.md)

# Quality Gate

รัน final readiness check:

```bash
make quality-gate
```

ระบบรัน project status, workflow badge validation, environment check, result inventory, Markdown link check, test suite ทั้งหมด และ quick-start example

## ใช้ก่อน

- เปิดหรือ merge pull request
- แทนที่ experiment result ที่ติดตาม
- Demo, submission หรือ release

## การจัดการ Failure

อ่าน command แรกที่ล้มเหลว แก้สาเหตุนั้น แล้วรัน gate ใหม่ อย่าข้าม stage ที่ล้มเหลวหรือขยายขอบเขตการเปลี่ยนโดยไม่จำเป็น Gate ที่ผ่านยืนยัน repository consistency แต่ไม่ยืนยันข้ออ้างวิทยาศาสตร์เกิน implemented test

GitHub Actions รัน command เดียวกันผ่าน `.github/workflows/quality-gate.yml`
