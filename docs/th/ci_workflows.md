🌐 ภาษา: [English](../en/ci_workflows.md) | [日本語](../ja/ci_workflows.md) | [한국어](../ko/ci_workflows.md) | [ไทย](../th/ci_workflows.md)

# CI เวิร์กโฟลว์

| เวิร์กโฟลว์ | จุดประสงค์ |
|---|---|
| `tests.yml` | รันชุดทดสอบ Python บน Python 3.12 |
| `local-checks.yml` | รัน `make checks` บน Python 3.11 |
| `quality-gate.yml` | รันการตรวจความพร้อมทั้งหมดบน `main` และ pull request |
| `codeql.yml` | วิเคราะห์โค้ด Python เมื่อ push เปิด pull request และตามตารางรายสัปดาห์ |

## ก่อน Push

```bash
make checks
make quality-gate
```

การตรวจบรานช์ที่บังคับต้องใช้ชื่องานตรงตามที่ GitHub แสดงทุกตัวอักษร หาก workflow ล้มเหลว ให้ดูขั้นตอนแรกที่ล้มเหลว แล้วรันคำสั่งนั้นซ้ำบนเครื่อง

ตรวจป้ายสถานะใน README ด้วย `python scripts/check_workflow_badges.py`
