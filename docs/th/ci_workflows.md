🌐 ภาษา: [English](../en/ci_workflows.md) | [日本語](../ja/ci_workflows.md) | [한국어](../ko/ci_workflows.md) | [ไทย](../th/ci_workflows.md)

# CI เวิร์กโฟลว์

| เวิร์กโฟลว์ | จุดประสงค์ |
|---|---|
| `tests.yml` | รันชุดทดสอบ Python บน Python 3.10 และ 3.12 |
| `local-checks.yml` | ตรวจแพ็กเกจ เอกสาร lint การทดสอบ และตัวอย่างเริ่มต้นบน Python 3.12 |
| `quality-gate.yml` | รันการตรวจความพร้อมทั้งหมดบน `main` และ pull request |
| `codeql.yml` | วิเคราะห์โค้ด Python เมื่อ push เปิด pull request และตามตารางรายสัปดาห์ |

## ก่อน Push

```bash
make checks
make quality-gate
```

เวิร์กโฟลว์ใช้สิทธิ์เริ่มต้นแบบอ่านอย่างเดียว แคช dependencies การยกเลิกงานซ้ำ และเวลาจำกัดที่ระบุชัดเจน การตรวจบรานช์ที่บังคับต้องใช้ชื่องานตรงตามที่ GitHub แสดงทุกตัวอักษร หากล้มเหลว ให้ดูขั้นตอนแรกที่ล้มเหลว แล้วรันคำสั่งนั้นซ้ำบนเครื่อง

ตรวจป้ายสถานะใน README ด้วย `python scripts/check_workflow_badges.py`
