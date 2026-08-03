🌐 ภาษา: [English](../en/release_checklist.md) | [日本語](../ja/release_checklist.md) | [한국어](../ko/release_checklist.md) | [ไทย](../th/release_checklist.md)

# Checklist การ Release

1. Sync `main` branch ที่ clean และตรวจ version ใน `pyproject.toml`
2. รัน `python scripts/check_environment.py`, `make checks` และ `make quality-gate`
3. Backup tracked result ก่อน clean regeneration และ review ทุก diff
4. Review README ทั้งสี่ภาษา documentation index, release note, limitations และ security guide
5. ตรวจ `git status -sb`, recent commit และยืนยันว่า tag ไม่มีทั้ง local และ remote
6. Merge release pull request และรัน gate ใหม่บน `main` ขั้นสุดท้าย
7. สร้าง annotated tag และ push เฉพาะ tag นั้น:

```bash
VERSION=vX.Y.Z
git tag -a "$VERSION" -m "Release $VERSION"
git push origin "$VERSION"
```

ห้ามย้ายหรือลบ published version tag ให้ใช้ patch version ใหม่สำหรับการแก้ไข
