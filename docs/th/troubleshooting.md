🌐 ภาษา: [English](../en/troubleshooting.md) | [日本語](../ja/troubleshooting.md) | [한국어](../ko/troubleshooting.md) | [ไทย](../th/troubleshooting.md)

# การแก้ไขปัญหา

## Import หรือ test ล้มเหลว

ตรวจว่า terminal อยู่ที่ root ของ repository เปิด `.venv` แล้วรัน `python -m pip install -e .` และ `python -m pytest`

## Plot หรือ CSV เก่า

ตรวจ `git status` และ backup artifact ที่ติดตาม จากนั้นจึงรัน `python scripts/clean_results.py` แล้ว `python main.py`

## ค่าตัวเลขต่างเล็กน้อย

ตรวจ Python, dependency version และ seed คงที่ ความต่างเล็กน้อยระหว่าง platform เป็นไปได้ แต่ความต่างมากต้องตรวจสอบ

## การฝึกช้า

ใช้ quick start เพื่อตรวจ setup การทดลองเต็มมีการฝึก robustness sweep และ region-of-attraction simulation

## สับสนเรื่อง Git branch

รัน `git status -sb` และ `git branch --show-current` อย่า commit ไฟล์ environment หรือผลลัพธ์ที่ไม่เกี่ยวข้อง

ปัญหาการติดตั้งดูที่ [การแก้ปัญหา dependency](dependency_troubleshooting.md)
