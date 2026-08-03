🌐 ภาษา: [English](../en/security_scanning.md) | [日本語](../ja/security_scanning.md) | [한국어](../ko/security_scanning.md) | [ไทย](../th/security_scanning.md)

# การสแกนความปลอดภัย

CodeQL วิเคราะห์ Python code เมื่อ push ไป `main`, pull request ที่เป้าหมายเป็น `main` และตาม weekly schedule

## การเตรียม Local

```bash
python -m pip check
make checks
make quality-gate
```

Review dependency alert และ CodeQL finding ก่อน merge Clean scan ไม่ได้พิสูจน์ว่า control policy safe หรือ stable เพราะ software security และ control-system safety เป็นคนละ review domain

รายงานช่องโหว่ที่สงสัยแบบ private ตาม [security policy](../../SECURITY.th.md) ของ repository ห้ามใส่ secret, private data หรือ exploit detail ใน public issue
