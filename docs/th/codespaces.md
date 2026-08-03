🌐 ภาษา: [English](../en/codespaces.md) | [日本語](../ja/codespaces.md) | [한국어](../ko/codespaces.md) | [ไทย](../th/codespaces.md)

# การตั้งค่า GitHub Codespaces

คอนเทนเนอร์พัฒนาใช้ Python 3.11 ติดตั้ง `requirements.txt` เปิดใช้ส่วนขยายที่แนะนำ และตั้งค่าการค้นหาชุดทดสอบของ pytest

## คำสั่งแรก

```bash
python scripts/check_environment.py
python examples/quick_start.py
make checks
```

## ขั้นตอนการพัฒนา

สร้างสาขาสำหรับงาน จำกัดขอบเขตการแก้ไขให้ชัดเจน รัน `make quality-gate` แล้วจึงคอมมิต พุช และเปิดคำขอรวมโค้ด ให้ Git ติดตามรูปที่สร้างขึ้นเฉพาะเมื่อตั้งใจเก็บเป็นผลอ้างอิง

ต้องมี Git LFS ก่อนเช็กเอาต์ไฟล์ไบนารีที่ Git ติดตาม หากสภาพแวดล้อม Codespaces ไม่สอดคล้อง ให้สร้างคอนเทนเนอร์ใหม่แทนการคอมมิตไฟล์ที่สภาพแวดล้อมสร้างขึ้น
