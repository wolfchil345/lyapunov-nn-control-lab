🌐 ภาษา: [English](../en/codespaces.md) | [日本語](../ja/codespaces.md) | [한국어](../ko/codespaces.md) | [ไทย](../th/codespaces.md)

# การตั้งค่า GitHub Codespaces

คู่มือนี้อธิบายวิธีใช้ repository นี้ใน GitHub Codespaces

## วัตถุประสงค์

ใน repository มี `.devcontainer/devcontainer.json` เพื่อให้ Codespaces เตรียมสภาพแวดล้อม Python สำหรับพัฒนาได้โดยอัตโนมัติ

## สิ่งที่ dev container ทำ

- ใช้ Python 3.11
- ติดตั้งแพ็กเกจและ dependency สำหรับพัฒนาจาก `pyproject.toml` หลังจากสร้าง Codespace แล้ว
- แนะนำส่วนขยาย Python, Pylance และ GitHub Actions
- เปิดการค้นหา pytest จากโฟลเดอร์ `tests/`

## คำสั่งแรกหลังเปิด Codespaces

```bash
python scripts/run_checks.py
```

## รันการทดลอง

```bash
python main.py
```

## เวิร์กโฟลว์ Git ปกติ

```bash
git switch main
git pull origin main
git switch -c feature/my-change
python scripts/run_checks.py
git status
```
