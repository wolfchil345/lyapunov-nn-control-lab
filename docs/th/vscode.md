🌐 ภาษา: [English](../en/vscode.md) | [日本語](../ja/vscode.md) | [한국어](../ko/vscode.md) | [ไทย](../th/vscode.md)

# การตั้งค่า VS Code

## ส่วนขยายที่แนะนำ

- Python
- Pylance
- GitHub Actions

เปิดโฟลเดอร์ของรีโพซิทอรี เลือกตัวแปลภาษา Python จาก `.venv` และรันคำสั่งที่รากโครงการผ่านเทอร์มินัลใน VS Code

## ขั้นตอนทำงานทั่วไป

```bash
python scripts/check_environment.py
python -m pytest
python main.py
make quality-gate
```

การค้นหาชุดทดสอบของ pytest กำหนดไว้ที่ `tests/` หาก VS Code ใช้ตัวแปลภาษาอื่น ให้เลือก `.venv` ใหม่แล้วโหลดหน้าต่างอีกครั้ง
