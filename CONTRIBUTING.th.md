🌐 ภาษา: [English](CONTRIBUTING.md) | [日本語](CONTRIBUTING.ja.md) | [한국어](CONTRIBUTING.ko.md) | [ไทย](CONTRIBUTING.th.md)

# การมีส่วนร่วม

ขอบคุณที่ช่วยพัฒนา Lyapunov NN Control Lab

## การตั้งค่า

```bash
git clone https://github.com/wolfchil345/lyapunov-nn-control-lab.git
cd lyapunov-nn-control-lab
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

## Workflow

1. สร้าง branch ที่มีจุดประสงค์ชัดเจนจาก `main` ปัจจุบัน
2. แยกขอบเขตการเปลี่ยนแปลงด้านวิทยาศาสตร์ code และ documentation
3. เพิ่ม test เมื่อ behavior เปลี่ยน
4. อัปเดต viewer-facing documentation เป็นอังกฤษ ญี่ปุ่น เกาหลี และไทย
5. รัน `git diff --check`, `make checks` และ `make quality-gate`
6. เปิด pull request และรอ required check ทั้งหมดก่อน merge

## ผลลัพธ์ทางวิทยาศาสตร์

อย่าสร้างหรือ commit result ใหม่หากการเปลี่ยนไม่ต้องใช้ บันทึก seed และ experiment setting ตรวจทุก numerical และ figure diff และอธิบาย sampled stability evidence อย่างถูกต้อง

## การมีส่วนร่วมที่ดี

- Controller baseline และ robustness experiment ที่ออกแบบอย่างรอบคอบ
- Test สำหรับ numerical, reporting และ documentation tool
- Plot, example, translation และ methodology explanation ที่ชัดขึ้น
- การปรับปรุง reproducibility, safety และ failure case

ใช้ commit message แบบคำสั่งสั้น เช่น `Add noise robustness test` หรือ `Clarify Lyapunov limitations`
