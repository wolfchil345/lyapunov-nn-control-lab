🌐 ภาษา: [English](../en/release_checklist.md) | [日本語](../ja/release_checklist.md) | [한국어](../ko/release_checklist.md) | [ไทย](../th/release_checklist.md)

# รายการตรวจสอบก่อนเผยแพร่

1. ซิงก์ `main` ที่สะอาด และยืนยันเวอร์ชันที่ต้องการใน `pyproject.toml`
2. รัน `python scripts/check_environment.py`, `make checks` และ `make quality-gate`
3. สำรองผลลัพธ์ที่ Git ติดตามก่อนสร้างใหม่แบบสะอาด และตรวจความแตกต่างทุกรายการ
4. ทบทวน README ทั้งสี่ภาษา ดัชนีเอกสาร บันทึกการเผยแพร่ ข้อจำกัด และคำแนะนำด้านความปลอดภัย
5. ยืนยัน `git status -sb` คอมมิตล่าสุด และตรวจว่ายังไม่มีแท็กนั้นทั้งในเครื่องและบนรีโมต
6. รวมคำขอเผยแพร่ แล้วรันด่านคุณภาพอีกครั้งบน `main` สุดท้าย
7. สร้างแท็กแบบมีคำอธิบาย และพุชเฉพาะแท็กนั้น

```bash
VERSION=vX.Y.Z
git tag -a "$VERSION" -m "Release $VERSION"
git push origin "$VERSION"
```

ห้ามย้ายหรือลบแท็กเวอร์ชันที่เผยแพร่แล้ว ให้ใช้เวอร์ชันแพตช์ใหม่สำหรับการแก้ไข
