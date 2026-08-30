🌐 ภาษา: [English](../en/vscode.md) | [日本語](../ja/vscode.md) | [한국어](../ko/vscode.md) | [ไทย](../th/vscode.md)

# การตั้งค่า VS Code

คู่มือนี้อธิบายวิธีใช้โครงการใน VS Code หรือ GitHub Codespaces

## ส่วนขยายที่แนะนำ

ที่เก็บนี้มี `.vscode/extensions.json` ซึ่งระบุส่วนขยายที่แนะนำสำหรับการพัฒนา Python และ GitHub Actions

ส่วนขยายที่แนะนำ:

- Python
- Pylance
- GitHub Actions

## เปิดโครงการ

เปิดโฟลเดอร์รากของ repository ใน VS Code โฟลเดอร์รากควรมี `README.md`, `main.py`, `src/`, `tests/`, และ `scripts/`

## เลือก Python interpreter

หลังจากสร้าง virtual environment แล้ว ให้เลือก interpreter จาก `.venv` ใน VS Code

## รันการตรวจสอบจาก terminal

```bash
python scripts/run_checks.py
```

## รันทดสอบจาก VS Code

ที่เก็บนี้มี `.vscode/settings.json` เพื่อให้ VS Code ค้นหา pytest tests จากโฟลเดอร์ `tests/` ได้

## หมายเหตุสำหรับ Codespaces

ใน Codespaces ให้เปิด terminal และรันคำสั่งเดียวกับที่ใช้ในเครื่อง local:

```bash
python -m pip install -e ".[dev]"
python scripts/run_checks.py
```

## เวิร์กโฟลว์ทั่วไป

```bash
git switch main
git pull origin main
git switch -c feature/my-new-change
python scripts/run_checks.py
git status
```
