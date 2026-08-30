🌐 ภาษา: [English](../en/troubleshooting.md) | [日本語](../ja/troubleshooting.md) | [한국어](../ko/troubleshooting.md) | [ไทย](../th/troubleshooting.md)

# คู่มือแก้ไขปัญหา

คู่มือนี้รวบรวมปัญหาที่พบบ่อยและวิธีแก้แบบรวดเร็วเมื่อรัน Lyapunov Neural-Network Control Lab

## `ModuleNotFoundError`

หาก Python หาโครงการหรือ runtime dependency ไม่เจอ ให้ติดตั้งโครงการ:

```bash
python -m pip install -e .
```

## การทดสอบล้มเหลวหลังจากแก้โค้ด

รันสคริปต์ตรวจสอบภายใน:

```bash
python scripts/run_checks.py
```

หากมีการทดสอบล้มเหลวเพียงรายการเดียว ให้อ่านข้อความ error แรกอย่างละเอียดและตรวจสอบไฟล์ที่ระบุใน traceback

## ผลลัพธ์เก่าหรือสับสน

สร้าง run ใหม่ที่แยกออกมา แล้วเลือกด้วย run ID อย่าลบ run ที่เสร็จสมบูรณ์แล้วเพียงเพราะต้องการทดลองใหม่

```bash
python main.py
python scripts/list_results.py
```

## ไม่มีสรุป CSV ปรากฏ

ใช้รายงานภายในไดเรกทอรีของ run ที่เลือก ตรวจสอบด้วย:

```bash
python scripts/verify_run.py results/runs/<run_id>
```

## ไม่มีกราฟปรากฏ

กราฟที่สร้างจะถูกบันทึกไว้ใน `results/runs/<run_id>/` เปิดไดเรกทอรีนั้นจาก file explorer หรือรัน:

```bash
find results/runs/<run_id> -maxdepth 1 -type f
```

## การฝึกใช้เวลานาน

การทดลองหลักจะฝึก neural-network controller และอาจรันการทดลองด้าน robustness และ grid-based เพิ่มเติมด้วย จึงอาจใช้เวลาตามสเปกของเครื่อง

สำหรับการตรวจสอบอย่างรวดเร็ว ให้รัน:

```bash
python examples/quick_start.py
```

## ผลลัพธ์เชิงตัวเลขเปลี่ยนไปเล็กน้อย

ความแตกต่างเล็กน้อยอาจเกิดจาก solver tolerance, เวอร์ชันแพ็กเกจ หรือความแตกต่างของฮาร์ดแวร์

## สับสนเรื่อง Git branch

ตรวจสอบ branch ปัจจุบันและการเปลี่ยนแปลงในเครื่อง:

```bash
git branch --show-current
git status
```

ก่อนเริ่มฟีเจอร์ใหม่ ให้กลับไป `main` และดึงเวอร์ชันล่าสุด:

```bash
git switch main
git pull origin main
```
