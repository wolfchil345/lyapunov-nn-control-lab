🌐 ภาษา: [English](../en/codespaces.md) | [日本語](../ja/codespaces.md) | [한국어](../ko/codespaces.md) | [ไทย](../th/codespaces.md)

# การตั้งค่า GitHub Codespaces

dev container ใช้ Python 3.11 ติดตั้ง `requirements.txt` แนะนำ extension ของโครงการ และเปิด pytest discovery

## คำสั่งแรก

```bash
python scripts/check_environment.py
python examples/quick_start.py
make checks
```

## Workflow การพัฒนา

สร้าง feature branch แก้ไขในขอบเขตที่ชัดเจน รัน `make quality-gate` แล้ว commit, push และเปิด pull request บันทึกรูปที่สร้างขึ้นเฉพาะเมื่อเป็น reference artifact ที่ตั้งใจเก็บ

ต้องมี Git LFS ก่อน checkout binary asset ที่ติดตาม หาก Codespace ไม่สอดคล้อง ให้ rebuild container แทนการ commit ไฟล์ที่ environment สร้างขึ้น
