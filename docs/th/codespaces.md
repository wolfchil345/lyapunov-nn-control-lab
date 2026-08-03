🌐 ภาษา: [English](../en/codespaces.md) | [日本語](../ja/codespaces.md) | [한국어](../ko/codespaces.md) | [ไทย](../th/codespaces.md)

# การตั้งค่า GitHub Codespaces

คอนเทนเนอร์พัฒนาใช้ Python 3.11 ติดตั้ง `requirements.txt` เปิดใช้ส่วนขยายที่แนะนำ และตั้งค่าการค้นหาชุดทดสอบของ pytest

## คำสั่งแรก

```bash
python scripts/check_environment.py
python examples/quick_start.py
make checks
```

## เวิร์กโฟลว์ การพัฒนา

สร้างบรานช์สำหรับงาน จำกัดขอบเขตการแก้ไขให้ชัดเจน รัน `make quality-gate` แล้วจึงคอมมิต พุช และเปิด pull request ให้ Git ติดตามรูปที่สร้างขึ้นเฉพาะเมื่อตั้งใจเก็บเป็นผลอ้างอิง

ต้องมี Git LFS ก่อน checkout ไฟล์ไบนารีที่ Git ติดตาม หาก Codespace ไม่สอดคล้อง ให้สร้างคอนเทนเนอร์ใหม่แทนการคอมมิตไฟล์ที่สภาพแวดล้อมสร้างขึ้น
