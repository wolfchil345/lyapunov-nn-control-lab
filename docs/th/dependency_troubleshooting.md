🌐 ภาษา: [English](../en/dependency_troubleshooting.md) | [日本語](../ja/dependency_troubleshooting.md) | [한국어](../ko/dependency_troubleshooting.md) | [ไทย](../th/dependency_troubleshooting.md)

# การแก้ปัญหาไลบรารีที่ต้องใช้

เริ่มด้วย:

```bash
python scripts/check_environment.py
python -m pip check
```

## ไม่พบแพ็กเกจหรือนำเข้า PyTorch ไม่ได้

เปิดใช้ `.venv` อัปเกรด pip แล้วติดตั้งโปรเจกต์ใหม่ด้วย `python -m pip install -e .` หลีกเลี่ยงการปะปนแพ็กเกจจาก Python ของระบบกับสภาพแวดล้อมเสมือน

## ข้อผิดพลาดของ Git LFS

ติดตั้ง Git LFS รัน `git lfs install` และใช้ `git lfs pull` เพื่อกู้คืนไฟล์ไบนารีที่ Git ติดตามอยู่

## สร้างสภาพแวดล้อมใหม่

สร้างสภาพแวดล้อมเสมือนใหม่แทนการแก้ไข Python ของระบบ หาก Codespaces ยังมีความไม่สอดคล้อง ให้สร้างคอนเทนเนอร์พัฒนาใหม่

เมื่อขอความช่วยเหลือ ให้แนบผลลัพธ์ของ `python scripts/check_environment.py`, `python --version` และ `python -m pip check`
