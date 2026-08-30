🌐 ภาษา: [English](../en/environment.md) | [日本語](../ja/environment.md) | [한국어](../ko/environment.md) | [ไทย](../th/environment.md)

# การตั้งค่าสภาพแวดล้อม

คู่มือนี้อธิบายวิธีเตรียมสภาพแวดล้อม Python บนเครื่องสำหรับ Lyapunov neural network control lab

## เวอร์ชัน Python ที่แนะนำ

ใช้ Python 3.10 หรือใหม่กว่า

## สร้าง virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

บน Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

## ติดตั้งโครงการ

สำหรับการใช้งานทั่วไป:

```bash
python -m pip install -e .
```

สำหรับการพัฒนา การทดสอบ และการสร้างแพ็กเกจ:

```bash
python -m pip install -e ".[dev]"
```

## รันการตรวจสอบภายใน

```bash
python scripts/run_checks.py
```

คำสั่งนี้จะรันการตรวจสอบลิงก์ในเอกสาร การทดสอบหน่วย และตัวอย่าง quick start

## รันการทดลองหลัก

```bash
python main.py
```

## ปัญหาที่พบบ่อย

- หาก import ล้มเหลว ให้ตรวจสอบว่าคุณรันคำสั่งจากรากของ repository
- หากแพ็กเกจที่ต้องใช้ตอนรันหายไป ให้รัน `python -m pip install -e .` อีกครั้ง
- หากเครื่องมือสำหรับทดสอบหรือ build หายไป ให้รัน `python -m pip install -e ".[dev]"`
- หากผลลัพธ์ที่สร้างไว้น่าจะเก่า ให้ล้างไดเรกทอรี results ก่อนรันการทดลองใหม่

## ตรวจสอบสภาพแวดล้อม

ใช้ตัวตรวจสอบสภาพแวดล้อมเมื่อ Codespaces หรือเครื่อง local มีปัญหาด้าน dependency:

```bash
python scripts/check_environment.py
```

การตรวจสอบนี้จะเช็ก Python, ไฟล์โครงการที่จำเป็น, แพ็กเกจที่ติดตั้งอยู่ และ runtime imports ที่ประกาศไว้ทั้งหมด
