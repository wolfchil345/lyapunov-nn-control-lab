🌐 ภาษา: [English](../en/onboarding.md) | [日本語](../ja/onboarding.md) | [한국어](../ko/onboarding.md) | [ไทย](../th/onboarding.md)

# คู่มือเริ่มต้น

## ชั่วโมงแรก

1. อ่าน README ภาษาไทยและ [สรุปโครงการ](project_summary.md)
2. ทำตาม [คู่มือตั้งค่า สภาพแวดล้อม](environment.md)
3. รัน `python examples/quick_start.py`
4. รัน `make checks` และตรวจ `results/`
5. อ่าน [ระเบียบวิธี](methodology.md), [ขั้นตอนการทดลอง](experiment_workflow.md) และ [ข้อจำกัด](limitations.md)

## ก่อนแก้ไขโค้ด

```bash
git switch main
git pull --ff-only origin main
git switch -c feature/short-description
```

แยกการเปลี่ยนแปลงทางวิทยาศาสตร์ออกจากเอกสาร บันทึกค่าการทดลอง และรัน `make quality-gate` ก่อนขอ การทบทวน

ดูขั้นตอนทั้งหมดใน [Git เวิร์กโฟลว์](git_workflow.md) และ [คู่มือการมีส่วนร่วม](../../CONTRIBUTING.th.md)
