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

เปิด pull request รอให้การตรวจที่บังคับผ่าน แก้ไขบทสนทนา แล้วรวมผ่านบรานช์ `main` ที่ได้รับการป้อง

## กฎ

- หนึ่ง บรานช์ ต่อหนึ่งจุดประสงค์
- เลือกไฟล์เข้าพื้นที่จัดเก็บอย่างชัดเจน และทบทวนผลลัพธ์ที่สร้างขึ้นแยกต่างหาก
- ใช้ คอมมิต ข้อความ แบบคำสั่งที่ชัดเจน
- ห้ามบังคับ push ไปยัง `main` เขียนทับแท็กที่เผยแพร่แล้ว หรือคอมมิตความลับและไฟล์สภาพแวดล้อม
- ลบบรานช์งานที่รวมแล้วหลังจากซิงค์ `main`
