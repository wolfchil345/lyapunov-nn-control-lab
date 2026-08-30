🌐 ภาษา: [English](../en/dependency_troubleshooting.md) | [日本語](../ja/dependency_troubleshooting.md) | [한국어](../ko/dependency_troubleshooting.md) | [ไทย](../th/dependency_troubleshooting.md)

# การแก้ปัญหา dependency

คู่มือนี้อธิบายวิธีแก้ปัญหาที่พบบ่อยเกี่ยวกับ dependency และสภาพแวดล้อม

## คำสั่งตรวจสอบแรก

รันตัวตรวจสอบสภาพแวดล้อมก่อนเปลี่ยนแพ็กเกจ:

```bash
python scripts/check_environment.py
```

## ข้อผิดพลาดตอน import PyTorch

หาก PyTorch import ไม่ได้และขึ้นข้อผิดพลาด shared library ให้ติดตั้ง CPU wheel ใหม่:

```bash
python -m pip uninstall -y torch torchvision torchaudio
python -m pip cache purge
python -m pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu
python -c "import torch; print(torch.__version__)"
```

หลังติดตั้ง PyTorch ใหม่ ให้รัน:

```bash
python scripts/check_environment.py
python scripts/run_checks.py
```

## รีเซ็ต dependency

หาก virtual environment เริ่มยุ่ง ให้สร้างใหม่:

```bash
rm -rf .venv
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python scripts/run_checks.py
```

## รีเซ็ต Codespaces

หาก Codespaces ทำงานผิดปกติ ให้ rebuild container จาก command palette ของ Codespaces

หลังจาก rebuild แล้ว ให้รัน:

```bash
python scripts/check_environment.py
python scripts/run_checks.py
```

## เมื่อใดควรขอความช่วยเหลือ

หากการตรวจสอบยังล้มเหลว ให้คัดลอก output ทั้งหมดของ terminal ตั้งแต่บรรทัด FAIL แรกเป็นต้นไป
