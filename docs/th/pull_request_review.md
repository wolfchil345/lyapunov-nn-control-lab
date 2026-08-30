🌐 ภาษา: [English](../en/pull_request_review.md) | [日本語](../ja/pull_request_review.md) | [한국어](../ko/pull_request_review.md) | [ไทย](../th/pull_request_review.md)

# คู่มือ Pull Request Review

คู่มือนี้อธิบายวิธีตรวจทานการเปลี่ยนแปลงก่อน merge เข้า `main`

## เป้าหมายของการตรวจทาน

- ตรวจให้แน่ใจว่าการเปลี่ยนแปลงมีจุดประสงค์ที่ชัดเจน
- ตรวจให้แน่ใจว่า local checks ผ่าน
- ตรวจให้แน่ใจว่าเอกสารถูกอัปเดตเมื่อพฤติกรรมเปลี่ยน
- ตรวจให้แน่ใจว่าไม่เขียนทับผลการทดลองโดยไม่ตั้งใจ
- ตรวจให้แน่ใจว่าไฟล์ที่สร้างขึ้นถูกรวมไว้หรือถูก ignore อย่างตั้งใจ

## คำสั่งในเครื่องก่อน merge

```bash
python scripts/check_environment.py
make checks
git status
```

## รายการตรวจทาน

ก่อน merge pull request หรือ feature branch ให้ตรวจสอบ:

- ชื่อ branch อธิบายการเปลี่ยนแปลงได้
- commit message ชัดเจน
- tests ผ่านในเครื่อง
- GitHub Actions ผ่าน
- README หรือ docs ได้รับการอัปเดตถ้าจำเป็น
- result files ถูก commit เฉพาะเมื่อเป็นตัวอย่างที่มีประโยชน์หรือเป็น artifact สุดท้าย

## จุดตรวจทานเฉพาะงานวิจัย

- การเปลี่ยนแปลงมีผลต่อ numerical results หรือไม่
- การเปลี่ยนแปลงมีผลต่อ Lyapunov analysis หรือไม่
- การเปลี่ยนแปลงมีผลต่อ reproducibility หรือไม่
- การเปลี่ยนแปลงเปลี่ยน random seeds, model architecture หรือ experiment settings หรือไม่

## กฎการ merge

merge เฉพาะหลังจาก checks ผ่านและ working tree สะอาดแล้ว
