🌐 ภาษา: [English](../en/branch_protection.md) | [日本語](../ja/branch_protection.md) | [한국어](../ko/branch_protection.md) | [ไทย](../th/branch_protection.md)

# คู่มือการป้องกัน branch

คู่มือนี้อธิบายการตั้งค่า branch protection ที่แนะนำสำหรับ repository

## เป้าหมาย

ปกป้อง `main` เพื่อให้โค้ดวิจัยที่สำคัญได้รับการตรวจทานและตรวจสอบก่อน merge

## การตั้งค่าที่แนะนำ

- ต้องมี pull request ก่อน merge
- ต้องผ่าน status checks ก่อน merge
- ต้องให้ branch เป็นเวอร์ชันล่าสุดก่อน merge
- รวม administrator ด้วยหากใช้สำหรับงานวิทยานิพนธ์หรือพอร์ตโฟลิโอสุดท้าย
- จำกัด force push ไปยัง `main`
- จำกัดการลบ branch ของ `main`

## การตรวจสอบที่ควรกำหนดเป็น required

- Local checks
- CodeQL

## รายการตรวจสอบในเครื่องก่อน merge

```bash
python scripts/check_environment.py
make checks
git status
```

## เวิร์กโฟลว์ที่แนะนำ

สร้าง feature branch สำหรับแต่ละการเปลี่ยนแปลง รันการตรวจสอบในเครื่อง แล้ว merge ก็ต่อเมื่อ GitHub checks ผ่านแล้วเท่านั้น

## หมายเหตุ

เอกสารนี้เป็นเพียงคำแนะนำ การตั้งค่า branch protection จริงต้องกำหนดใน GitHub repository settings
