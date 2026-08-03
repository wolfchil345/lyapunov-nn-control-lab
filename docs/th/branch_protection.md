🌐 ภาษา: [English](../en/branch_protection.md) | [日本語](../ja/branch_protection.md) | [한국어](../ko/branch_protection.md) | [ไทย](../th/branch_protection.md)

# การป้องกัน Branch

ป้องกัน default branch ด้วย ruleset `Protect main` ที่ Active

## กฎที่แนะนำ

- ต้องมี pull request ก่อน merge
- ต้องแก้ conversation ให้เรียบร้อย
- ต้องมี status check ที่เสถียรและ branch ที่ up to date
- Block force push และ branch deletion
- สำหรับ solo repository ตั้ง required approval เป็น 0 หากไม่มี independent reviewer
- อนุญาต administrator bypass เฉพาะ pull request และ emergency

ใช้ check name ตรงกับที่ GitHub แสดง ปกติคือ Python tests, local checks, quality gate และ CodeQL analysis

อย่าเปิด linear history หากไม่เปลี่ยน merge strategy ของ repository ทดสอบ rule ด้วย documentation pull request ก่อนใช้กับ release
