🌐 ภาษา: [English](../en/maintenance.md) | [日本語](../ja/maintenance.md) | [한국어](../ko/maintenance.md) | [ไทย](../th/maintenance.md)

# Maintenance Guide

คู่มือนี้อธิบายวิธีดูแลให้ project คงความพร้อมหลังจากเพิ่ม features, docs, tests และ workflows ใหม่

## Routine maintenance checklist

รัน checklist นี้ก่อน merge เข้า `main`:

```bash
python scripts/check_environment.py
python scripts/project_status.py
python scripts/check_workflow_badges.py
python scripts/quality_gate.py
make checks
```

## Weekly project check

รัน:

```bash
git switch main
git pull origin main
python scripts/quality_gate.py
```

จากนั้นตรวจสอบว่า:

- GitHub Actions ผ่าน
- README badges แสดงผลได้
- docs สำคัญถูกลิงก์จาก language index ที่เหมาะสมใต้ `docs/{en,ja,ko,th}/index.md`
- scripts ใหม่มี tests เมื่อทำได้
- ไฟล์สำคัญใหม่ถูกติดตามโดย `scripts/project_status.py`

## After adding a new script

1. เพิ่ม script ใต้ `scripts/`
2. เพิ่ม test ใต้ `tests/` หาก script มี logic
3. เพิ่ม Makefile shortcut หากจะใช้ command บ่อย
4. เพิ่ม documentation หากผู้ใช้ต้องทำความเข้าใจ
5. เพิ่ม script ลงใน `scripts/project_status.py` หากกลายเป็นส่วนหนึ่งของ core project structure

## After adding a new document

1. วางไฟล์ใต้ `docs/`
2. ลิงก์จากไฟล์ `docs/<language>/index.md` ที่เหมาะสม
3. ลิงก์จาก `README.md` หากสำคัญต่อผู้เข้าชม
4. เพิ่มลงใน `scripts/project_status.py` หากเป็น core guide

## After adding or changing a workflow

1. รัน quality gate บนเครื่อง
2. ยืนยันว่า workflow file อยู่ใต้ `.github/workflows/`
3. เพิ่มหรืออัปเดต README badges ตามความจำเป็น
4. รัน `python scripts/check_workflow_badges.py`
5. Push และยืนยันว่า GitHub Actions ผ่าน

## Before a demo or professor meeting

รัน:

```bash
python scripts/quality_gate.py
python scripts/project_status.py
```

และเปิด README เพื่อตรวจว่า project goal, badges, docs และ quick-start instructions มองเห็นได้ง่าย

## Portfolio note

repository ที่มีการดูแลต่อเนื่องมีคุณค่ามากกว่าการทดลองครั้งเดียว checklist นี้ช่วยแสดงว่า project มีความเสถียร มีเอกสารครบ และพร้อมต่อการรีวิว
