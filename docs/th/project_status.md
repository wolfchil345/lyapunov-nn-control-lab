🌐 ภาษา: [English](../en/project_status.md) | [日本語](../ja/project_status.md) | [한국어](../ko/project_status.md) | [ไทย](../th/project_status.md)

# Project Status Guide

คู่มือนี้อธิบายวิธีใช้ project status checker

## Purpose

project status checker ให้ภาพรวมอย่างรวดเร็วของ repository health

ช่วยยืนยันว่า files, folders, scripts, tests, workflows และ documentation ที่สำคัญมีอยู่ครบ

## Command

รัน:

```bash
python scripts/project_status.py
```

หรือ:

```bash
make status
```

## What it checks

checker จะรายงานว่า project files ที่สำคัญมีอยู่หรือไม่

ตัวอย่างที่ตรวจ:

- Core documentation files.
- finite-horizon convergence evaluator และ regression tests ของมัน
- Important scripts.
- Test files.
- GitHub Actions workflow files.
- Legacy result files และ manifest-verified provenance-aware runs.

สำหรับ provenance-aware run แต่ละรายการ checker จะรายงานจำนวน run และจำนวน manifests ที่ผ่าน complete artifact/checksum verification โดย root-level historical files จะถูกจัดแยกเป็น legacy/unverified แทนการนับเป็น current manifest-backed runs

## When to run it

ควรรัน project status checker ในช่วงต่อไปนี้:

- ก่อน commit ฟีเจอร์ใหม่
- ก่อน merge เข้า `main`
- หลังเพิ่ม documentation, scripts, tests หรือ workflows ใหม่
- ก่อนนำเสนอโปรเจกต์ในฐานะ portfolio หรือ research artifact

## Relationship with the quality gate

quality gate จะรัน project status checker โดยอัตโนมัติ

รัน:

```bash
python scripts/quality_gate.py
```

ถ้า quality gate ล้มเหลวที่ project status step ให้รัน `python scripts/project_status.py` โดยตรงเพื่อดูรายการที่ขาด

## How to update it

เมื่อมีไฟล์สำคัญใหม่ที่เป็นส่วนหนึ่งของ project structure ให้เพิ่มไฟล์นั้นใน tracked file list ภายใน:

```text
scripts/project_status.py
```

จากนั้นรัน:

```bash
python scripts/project_status.py
python scripts/quality_gate.py
```

## Portfolio note

script นี้ช่วยแสดงว่า repository ถูกจัดการในรูปแบบ maintained research software project ไม่ใช่เพียงโฟลเดอร์ของโค้ดทดลอง
