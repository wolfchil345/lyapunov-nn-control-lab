🌐 ภาษา: [English](../en/commands.md) | [日本語](../ja/commands.md) | [한국어](../ko/commands.md) | [ไทย](../th/commands.md)

# ชีตสรุปคำสั่ง

หน้านี้รวบรวมคำสั่งที่มีประโยชน์สำหรับการรันและดูแล Lyapunov Neural-Network Control Lab

## การตั้งค่า

ติดตั้งโครงการพร้อมเครื่องมือสำหรับพัฒนา:

```bash
python -m pip install -e ".[dev]"
```

## เริ่มต้นอย่างรวดเร็ว

รันตัวอย่างขนาดเล็กสำหรับผู้เริ่มต้น:

```bash
python examples/quick_start.py
```

## เรียกใช้การตรวจสอบภายในทั้งหมด

รันทดสอบและตัวอย่าง quick start:

```bash
python scripts/run_checks.py
```

## เรียกใช้เฉพาะการทดสอบ

```bash
python -m pytest
```

## รันการทดลองหลัก

```bash
python main.py
```

## สรุปผลลัพธ์ที่สร้างขึ้น

```bash
python scripts/summarize_results.py
```

## ตรวจสอบ run ที่มี provenance

```bash
python scripts/verify_run.py results/runs/<run_id>
```

## ล้าง staging directory ที่ยังไม่สมบูรณ์

```bash
python scripts/clean_results.py
```

## ตรวจสอบ branch ปัจจุบันของ Git

```bash
git branch --show-current
git status
```

## เริ่ม branch สำหรับฟีเจอร์ใหม่

```bash
git switch main
git pull origin main
git switch -c feature/my-new-feature
```

## commit และ push branch ฟีเจอร์

```bash
git add .
git commit -m "Describe the change"
git push -u origin feature/my-new-feature
```

## รวม branch ฟีเจอร์เข้า main

```bash
git switch main
git pull origin main
git merge --no-ff feature/my-new-feature
python scripts/run_checks.py
git push origin main
```

## ทางลัดใน Makefile

ที่เก็บนี้มี `Makefile` สำหรับคำสั่งที่ใช้บ่อย:

```bash
make check-env
make checks
make test
make quickstart
make experiment
make clean
make summarize
make verify-run RUN_DIR=results/runs/<run_id>
```

## คำสั่ง CI

GitHub Actions ใช้ `make checks` เพื่อรันการตรวจสอบแบบเดียวกับที่ใช้ระหว่างพัฒนา
