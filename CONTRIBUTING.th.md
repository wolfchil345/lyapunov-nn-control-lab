🌐 ภาษา: [English](CONTRIBUTING.md) | [日本語](CONTRIBUTING.ja.md) | [한국어](CONTRIBUTING.ko.md) | [ไทย](CONTRIBUTING.th.md)

# คู่มือการมีส่วนร่วม (Contributing Guide)

ขอบคุณที่สนใจร่วมพัฒนา Lyapunov NN Control Lab ด้านล่างเป็นขั้นตอนการตั้งค่าสภาพแวดล้อมการพัฒนา การทดสอบ และแนวทางการทำงานร่วมกัน

## การตั้งค่าสภาพแวดล้อมการพัฒนา

```bash
git clone https://github.com/wolfchil345/lyapunov-nn-control-lab.git
cd lyapunov-nn-control-lab
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

## การรันเทสต์

```bash
python -m pytest
```

## การรันการทดลอง (บนเครื่อง)

```bash
python main.py
```

## กระบวนการใช้สาขา (Branch workflow)

สร้างฟีเจอร์สาขา (feature branch) ก่อนแก้ไขไฟล์ทุกครั้ง:

```bash
git switch main
git pull origin main
git switch -c feature/your-feature-name
```

## รูปแบบข้อความคอมมิต

ใช้ข้อความสั้นและชัดเจน เช่น:

- Add noise robustness experiment
- Add reproducibility guide
- Fix Lyapunov metric handling

## พื้นที่ที่แนะนำให้ร่วมพัฒนา

- เพิ่ม baseline controllers
- เพิ่มการทดลอง robustness
- ปรับปรุงภาพและเอกสาร
- เพิ่มเทสต์สำหรับยูทิลิตี้เชิงตัวเลข
- เพิ่มตัวอย่างสำหรับผู้เริ่มต้น

## ก่อนส่งการเปลี่ยนแปลง

รันเทสต์และตัวอย่างหลักเพื่อยืนยันว่าไม่เกิดการเบรกของฟังก์ชันเดิม:

```bash
python -m pytest
python main.py
```

โปรดรักษาคำสั่งและชื่อไฟล์ไว้ตามต้นฉบับภาษาอังกฤษเพื่อความสอดคล้อง
