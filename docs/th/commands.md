🌐 ภาษา: [English](../en/commands.md) | [日本語](../ja/commands.md) | [한국어](../ko/commands.md) | [ไทย](../th/commands.md)

# คู่มือคำสั่ง

## ติดตั้งและวินิจฉัย

```bash
python -m pip install -e ".[dev]"
python scripts/check_environment.py
```

## รันและตรวจสอบ

```bash
python examples/quick_start.py
python main.py
python -m pytest
make lint
make checks
make quality-gate
```

## ผลลัพธ์

```bash
python scripts/list_results.py
python scripts/summarize_results.py
python scripts/new_experiment_log.py "short description" --language th
```

`python scripts/clean_results.py` เป็นการทดลองแบบไม่ลบจริงและจะแสดงรายการไฟล์ที่สร้างขึ้นซึ่งรู้จัก ใช้ `python scripts/clean_results.py --yes` หลังจากตรวจสอบรายการแล้วเท่านั้น โดยจะเก็บไฟล์ที่ไม่รู้จักและโฟลเดอร์บันทึกการทดลองไว้

## Git

```bash
git status -sb
git switch -c feature/short-description
git add <files>
git commit -m "Describe the change"
git push -u origin feature/short-description
```
