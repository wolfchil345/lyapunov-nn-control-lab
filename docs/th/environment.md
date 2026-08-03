🌐 ภาษา: [English](../en/environment.md) | [日本語](../ja/environment.md) | [한국어](../ko/environment.md) | [ไทย](../th/environment.md)

# การตั้งค่าสภาพแวดล้อม

## ความต้องการ

- Python 3.10 ขึ้นไป โดย CI ใช้ Python 3.11 และ 3.12
- Git และ Git LFS สำหรับ binary asset ที่ติดตาม
- การทดลองที่รวมไว้ใช้ CPU ได้

## การติดตั้ง

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

บน Windows PowerShell ใช้ `.venv\Scripts\Activate.ps1`

## ตรวจสอบ environment

```bash
python scripts/check_environment.py
python examples/quick_start.py
make checks
```

ให้รันคำสั่งจาก root ของ repository หาก import ไม่สำเร็จ ให้เปิด `.venv` อีกครั้งและรัน `python -m pip install -e .`
