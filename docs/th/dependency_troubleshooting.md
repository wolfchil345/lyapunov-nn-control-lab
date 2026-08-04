🌐 ภาษา: [English](../en/dependency_troubleshooting.md) | [日本語](../ja/dependency_troubleshooting.md) | [한국어](../ko/dependency_troubleshooting.md) | [ไทย](../th/dependency_troubleshooting.md)

# การแก้ปัญหาไลบรารีที่ต้องใช้

เริ่มด้วย:

```bash
python scripts/check_environment.py
python -m pip check
```

## ไม่พบแพ็กเกจหรือนำเข้า PyTorch ไม่ได้

เปิดใช้ `.venv` อัปเกรด pip แล้วติดตั้งโปรเจกต์ใหม่ด้วย `python -m pip install -e ".[dev]"` หลีกเลี่ยงการปะปนแพ็กเกจจาก Python ของระบบกับสภาพแวดล้อมเสมือน

## ข้อผิดพลาดของข้อมูลแพ็กเกจหรือการ import

รัน `python scripts/check_package.py` หากไม่ผ่าน ให้ติดตั้งโปรเจกต์แบบแก้ไขได้พร้อม extra สำหรับการพัฒนาอีกครั้ง ผลลัพธ์ที่ติดตามอยู่ในปัจจุบันไม่ต้องใช้ Git LFS

## สร้างสภาพแวดล้อมใหม่

สร้างสภาพแวดล้อมเสมือนใหม่แทนการแก้ไข Python ของระบบ หาก Codespaces ยังมีความไม่สอดคล้อง ให้สร้างคอนเทนเนอร์พัฒนาใหม่

เมื่อขอความช่วยเหลือ ให้แนบผลลัพธ์ของ `python scripts/check_environment.py`, `python --version` และ `python -m pip check`
