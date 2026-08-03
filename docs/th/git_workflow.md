🌐 ภาษา: [English](../en/git_workflow.md) | [日本語](../ja/git_workflow.md) | [한국어](../ko/git_workflow.md) | [ไทย](../th/git_workflow.md)

# Git Workflow

## Flow มาตรฐาน

```bash
git switch main
git pull --ff-only origin main
git switch -c docs/short-description
# edit and validate
git status -sb
git diff --check
make quality-gate
git add <intentional-files>
git commit -m "Describe the change"
git push -u origin docs/short-description
```

เปิด pull request รอ required check แก้ conversation และ merge ผ่าน protected `main` branch

## กฎ

- หนึ่ง branch ต่อหนึ่งจุดประสงค์
- Stage file แบบระบุชัดและ review generated artifact แยกกัน
- ใช้ commit message แบบคำสั่งที่ชัดเจน
- ห้าม force-push `main`, rewrite published tag หรือ commit secret และ environment file
- ลบ feature branch ที่ merge แล้วหลัง sync `main`
