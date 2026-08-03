🌐 ภาษา: [English](../en/environment.md) | [日本語](../ja/environment.md) | [한국어](../ko/environment.md) | [ไทย](../th/environment.md)

# การตั้งค่าสภาพแวดล้อม

## ข้อกำหนด

- Python 3.10 หรือใหม่กว่า ระบบ CI ใช้ Python 3.11 และ 3.12
- Git และ Git LFS สำหรับไฟล์ไบนารีที่ Git ติดตาม
- การทดลองที่ให้มาสามารถรันด้วย CPU ได้

## การติดตั้ง

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

บน Windows PowerShell ให้เปิดใช้สภาพแวดล้อมด้วย `.venv\Scripts\Activate.ps1`

## การตรวจสภาพแวดล้อม

```bash
python scripts/check_environment.py
python examples/quick_start.py
make checks
```

ให้รันคำสั่งจากโฟลเดอร์รากของรีโพซิทอรี หากนำเข้าโมดูลไม่ได้ ให้เปิดใช้ `.venv` ใหม่แล้วติดตั้งอีกครั้งด้วย `python -m pip install -e .`
