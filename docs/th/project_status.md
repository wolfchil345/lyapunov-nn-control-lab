🌐 ภาษา: [English](../en/project_status.md) | [日本語](../ja/project_status.md) | [한국어](../ko/project_status.md) | [ไทย](../th/project_status.md)

# สถานะโครงการ

รัน:

```bash
python scripts/project_status.py
```

Command นี้ตรวจ file สำคัญของ repository และรายงานจำนวน documentation, script, test, workflow และ result artifact เป็น inventory check ไม่ใช่สิ่งแทน test หรือ scientific review

## เวลาที่ควรใช้

- หลังจัดโครงสร้าง file ใหม่
- ก่อน pull request, demo หรือ release
- หลังเพิ่ม documentation, script, test หรือ workflow

อัปเดต `KEY_FILES` ใน `scripts/project_status.py` เมื่อ file ใหม่กลายเป็นส่วนสำคัญ [Quality gate](quality_gate.md) รัน status command นี้เป็นส่วนหนึ่งของ validation sequence ที่กว้างกว่า
