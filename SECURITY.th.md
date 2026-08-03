🌐 ภาษา: [English](SECURITY.md) | [日本語](SECURITY.ja.md) | [한국어](SECURITY.ko.md) | [ไทย](SECURITY.th.md)

# นโยบายความปลอดภัย

## Version ที่รองรับ

รองรับ latest version บน `main` ส่วน historical release เก็บไว้เพื่อ reproducibility แต่ไม่ได้รับ fix

## รายงานช่องโหว่

อย่าเผยแพร่ exploit detail ใน issue ติดต่อ repository owner ผ่าน private GitHub channel ที่เหมาะสม และให้ affected version, reproduction step, impact และ safe example ขนาดเล็ก

## ในขอบเขต

- Unsafe dependency หรือ file-handling behavior
- Credential, token หรือ private-data exposure
- Unexpected command execution หรือ untrusted-input handling
- Security problem ใน workflow และ project script

## ประเด็นวิจัยที่แยกต่างหาก

Numerical instability, model limitations, changed experiment result และความเห็นต่างด้าน scientific interpretation ไม่ใช่ software vulnerability ให้รายงานเป็น research หรือ bug issue โดยไม่ใส่ sensitive information

## การใช้อย่างปลอดภัย

ใช้ virtual environment หรือ Codespaces ตรวจการเปลี่ยนจาก fork ห้าม commit secret และรัน test กับ quality-gate workflow ก่อนใช้ experiment code ที่แก้ไข
