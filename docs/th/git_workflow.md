🌐 ภาษา: [English](../en/git_workflow.md) | [日本語](../ja/git_workflow.md) | [한국어](../ko/git_workflow.md) | [ไทย](../th/git_workflow.md)

# Git เวิร์กโฟลว์

## ลำดับงานมาตรฐาน

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

เปิดคำขอรวมโค้ด รอให้การตรวจที่บังคับผ่าน แก้ไขบทสนทนาที่ยังค้างอยู่ แล้วรวมผ่านสาขา `main` ที่ได้รับการป้องกัน

## กฎ

- หนึ่งสาขาต่อหนึ่งจุดประสงค์
- เลือกไฟล์เข้าพื้นที่จัดเก็บอย่างชัดเจน และทบทวนผลลัพธ์ที่สร้างขึ้นแยกต่างหาก
- ใช้ข้อความคอมมิตแบบคำสั่งที่ชัดเจน
- ห้ามบังคับพุชไปยัง `main` เขียนทับแท็กที่เผยแพร่แล้ว หรือคอมมิตความลับและไฟล์สภาพแวดล้อม
- ลบสาขางานที่รวมแล้วหลังจากซิงค์ `main`
