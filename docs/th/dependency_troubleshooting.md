🌐 ภาษา: [English](../en/dependency_troubleshooting.md) | [日本語](../ja/dependency_troubleshooting.md) | [한국어](../ko/dependency_troubleshooting.md) | [ไทย](../th/dependency_troubleshooting.md)

# การแก้ปัญหา Dependency

เริ่มด้วย:

```bash
python scripts/check_environment.py
python -m pip check
```

## Package หายหรือ PyTorch import error

เปิด `.venv` upgrade pip และติดตั้งโครงการใหม่ด้วย `python -m pip install -e .` อย่าผสม package ของ system Python กับ virtual environment

## Git LFS error

ติดตั้ง Git LFS รัน `git lfs install` และใช้ `git lfs pull` เพื่อคืน binary asset ที่ติดตาม

## Clean reset

สร้าง virtual environment ใหม่แทนการแก้ system interpreter ใน Codespaces ให้ rebuild dev container หาก environment ยังไม่สอดคล้อง

เมื่อขอความช่วยเหลือให้แนบผล `python scripts/check_environment.py`, `python --version` และ `python -m pip check`
