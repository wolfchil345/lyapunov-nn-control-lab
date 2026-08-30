🌐 ภาษา: [English](../en/git_workflow.md) | [日本語](../ja/git_workflow.md) | [한국어](../ko/git_workflow.md) | [ไทย](../th/git_workflow.md)

# คู่มือเวิร์กโฟลว์ Git

คู่มือนี้อธิบายเวิร์กโฟลว์ของ branch ที่ใช้ในโครงการนี้

## กฎพื้นฐาน

อย่าทำงานโดยตรงบน `main`

สร้าง feature branch ทำการปรับปรุงที่โฟกัสเพียงเรื่องเดียว ทดสอบ แล้วจึง merge กลับเข้า `main`

## ลำดับการทำงานของ branch แบบมาตรฐาน

```bash
git switch main
git pull origin main
git switch -c feature/example-name
```

หลังแก้ไขไฟล์ ให้รันการตรวจสอบ:

```bash
python scripts/check_environment.py
python scripts/project_status.py
python scripts/check_workflow_badges.py
python scripts/quality_gate.py
make checks
```

commit และ push:

```bash
git add path/to/changed_file.md
git commit -m "Describe the focused change"
git push -u origin feature/example-name
```

merge เข้า `main`:

```bash
git switch main
git pull origin main
git merge --no-ff feature/example-name
python scripts/quality_gate.py
make checks
git push origin main
```

ลบ feature branch:

```bash
git branch -d feature/example-name
git push origin --delete feature/example-name
```

## รูปแบบการตั้งชื่อ branch

ใช้ชื่อสั้น ๆ ที่บอกวัตถุประสงค์ได้ชัดเจน:

- `feature/add-new-guide`
- `feature/test-new-script`
- `feature/status-new-file`
- `feature/update-quality-gate`

## รูปแบบข้อความ commit

ใช้วลีที่แสดงการกระทำอย่างชัดเจน:

- `Add maintenance guide`
- `Track maintenance guide in project status`
- `Add workflow badge checker tests`

## เมื่อ Git บอกว่าไม่มีอะไรให้ commit

หาก Git บอกว่าไม่มีอะไรให้ commit การเปลี่ยนแปลงนั้นอาจถูก commit ไปแล้ว

รัน:

```bash
git status
git log --oneline -5
```

ถ้าพบ commit ที่ถูกต้องแล้ว ให้ push branch นั้น:

```bash
git push -u origin feature/example-name
```

## หมายเหตุสำหรับพอร์ตโฟลิโอ

เวิร์กโฟลว์นี้แสดงว่าโครงการได้รับการดูแลด้วยการควบคุมเวอร์ชันอย่างรอบคอบ การเปลี่ยนแปลงที่แยกออกจากกัน และการตรวจสอบที่ทำซ้ำได้
