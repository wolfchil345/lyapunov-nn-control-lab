🌐 ภาษา: [English](../en/vscode.md) | [日本語](../ja/vscode.md) | [한국어](../ko/vscode.md) | [ไทย](../th/vscode.md)

# การตั้งค่า VS Code

## Extension ที่แนะนำ

- Python
- Pylance
- GitHub Actions

เปิดโฟลเดอร์ repository เลือก interpreter จาก `.venv` และรันคำสั่งจาก root ของ repository ใน terminal ที่รวมอยู่ใน VS Code

## Workflow ปกติ

```bash
python scripts/check_environment.py
python -m pytest
python main.py
make quality-gate
```

Pytest discovery ตั้งไว้ที่ `tests/` หาก VS Code ใช้ interpreter อื่น ให้เลือก `.venv` ใหม่และ reload window
