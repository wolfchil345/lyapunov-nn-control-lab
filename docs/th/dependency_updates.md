🌐 ภาษา: [English](../en/dependency_updates.md) | [日本語](../ja/dependency_updates.md) | [한국어](../ko/dependency_updates.md) | [ไทย](../th/dependency_updates.md)

# การอัปเดต Dependency

Dependabot ตรวจ Python package และ GitHub Actions ตาม schedule ที่กำหนด

## Review checklist

1. อ่าน upstream release note และหา breaking change
2. อัปเดตครั้งละหนึ่ง dependency group
3. รัน `python -m pip check`, `make checks` และ `make quality-gate`
4. สร้างผลการทดลองใหม่เฉพาะเมื่อ dependency อาจกระทบตัวเลขหรือ plot
5. ตรวจ artifact ที่เปลี่ยนทั้งหมดและบันทึกความต่างเชิงตัวเลขที่มีความหมาย

อย่า merge เพียงเพราะ CI เป็น green ต้องยืนยันว่าพฤติกรรมควบคุมและผลที่บันทึกไว้ยังน่าเชื่อถือ
