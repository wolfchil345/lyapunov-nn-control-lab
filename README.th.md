🌐 ภาษา: [English](README.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [ไทย](README.th.md)

[![Python tests](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/tests.yml/badge.svg)](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/tests.yml)
[![Local checks](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/local-checks.yml/badge.svg)](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/local-checks.yml)
[![Quality gate](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/quality-gate.yml/badge.svg)](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/quality-gate.yml)
[![Release](https://img.shields.io/github/v/release/wolfchil345/lyapunov-nn-control-lab)](https://github.com/wolfchil345/lyapunov-nn-control-lab/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Lyapunov NN Control Lab

การทดลองด้านการควบคุมด้วย Python และ PyTorch ที่ทำซ้ำได้ โดยฝึกตัวควบคุมโครงข่ายประสาทให้เลียนแบบตัวควบคุม LQR แล้วประเมินพฤติกรรมวงปิดด้วยการวิเคราะห์ Lyapunov บนจุดตัวอย่าง การทดสอบความทนทาน และการประมาณบริเวณดึงดูด

โครงการใช้ระบบมวล-สปริง-แดมเปอร์เป็นระบบทดสอบที่เข้าใจง่าย เพื่อเชื่อมโยงวิศวกรรมเครื่องกล ทฤษฎีการควบคุม และการเรียนรู้ของเครื่อง

## จุดเด่น

- ตัวควบคุม LQR อ้างอิงและตัวควบคุมโครงข่ายประสาทที่เรียนรู้การเลียนแบบ
- การฝึกที่คำนึงถึงเสถียรภาพด้วยบทลงโทษ Lyapunov บนจุดตัวอย่าง
- การประเมินหลายเงื่อนไขเริ่มต้นและตัวชี้วัดเชิงปริมาณ
- การทดสอบการอิ่มตัวของตัวกระตุ้น สัญญาณรบกวนการวัด และการเปลี่ยนพารามิเตอร์
- แผนภาพเฟส เส้นชั้น Lyapunov และการเปรียบเทียบบริเวณดึงดูด
- สคริปต์ที่ทำซ้ำได้ การทดสอบอัตโนมัติ CI เวิร์กโฟลว์ และรายงานที่สร้างอัตโนมัติ
- เอกสารภาษาอังกฤษ ญี่ปุ่น เกาหลี และไทย

## วงรอบการควบคุม

```text
สถานะ x = [position, velocity]
            │
            ▼
 neural-network controller ──► แรงควบคุม u
            ▲                         │
            │                         ▼
            └──── mass-spring-damper plant
```

ตัวควบคุมมีข้อกำหนด `u(0) = 0` เพื่อให้จุดกำเนิดยังคงเป็นจุดสมดุล

## แบบจำลองระบบและเสถียรภาพ

ระบบที่ศึกษาเป็นไปตามสมการ

```text
m q'' + c q' + k q = u
```

และเขียนในรูปสมการปริภูมิสถานะได้เป็น

```text
x_dot = A x + B u
```

ตัวควบคุม LQR ให้เป้าหมายการเลียนแบบ `u = -Kx` สำหรับฟังก์ชัน Lyapunov แบบกำลังสอง `V(x) = x^T P x` โครงการประเมิน

```text
V_dot(x) = 2 x^T P (A x + B u)
```

บนจุดตัวอย่าง และลงโทษการละเมิดเงื่อนไข

```text
V_dot(x) <= -alpha * ||x||^2
```

การตรวจสอบแบบสุ่มตัวอย่างนี้เป็นเพียงหลักฐานเชิงประจักษ์ ไม่ใช่การพิสูจน์อย่างเป็นทางการบนปริภูมิสถานะต่อเนื่องทั้งหมด

## วิธีการ

1. กำหนดระบบมวล-สปริง-แดมเปอร์ค่าปกติและออกแบบตัวควบคุม LQR อ้างอิง
2. สุ่มสถานะและสร้างป้ายกำกับด้วยกฎควบคุม LQR
3. ฝึกตัวควบคุมโครงข่ายประสาทด้วยค่าความสูญเสียจากการเลียนแบบและบทลงโทษ Lyapunov
4. จำลองตัวควบคุม LQR ตัวควบคุมโครงข่ายประสาท และตัวควบคุมที่มีขีดจำกัด จากหลายสถานะเริ่มต้น
5. วัดนอร์มสถานะสุดท้าย เวลาตั้งตัว ต้นทุนกำลังสอง พลังงานควบคุม และอินพุตควบคุมสูงสุด
6. ประเมินพฤติกรรม Lyapunov บนจุดตัวอย่าง ความทนทาน และบริเวณดึงดูดโดยประมาณ
7. บันทึกรูป ตัวชี้วัด CSV โมเดลที่ฝึกแล้ว และรายงานการทดลอง

## การทดลองและผลลัพธ์

| การทดลอง | จุดประสงค์ | ผลลัพธ์ |
|---|---|---|
| สถาปัตยกรรม | อธิบายโครงสร้างการควบคุมวงปิดด้วยโครงข่ายประสาท | `results/model_architecture.png` |
| เปรียบเทียบตัวควบคุม | เปรียบเทียบวิถีของ LQR และตัวควบคุมโครงข่ายประสาท | `results/position_comparison.png` |
| การฝึกที่คำนึงถึงเสถียรภาพ | ติดตามค่าความสูญเสียรวม ค่าความสูญเสียจากการเลียนแบบ และค่าความสูญเสีย Lyapunov | `results/training_loss.png` |
| เงื่อนไขเริ่มต้น | ตรวจสอบการลู่เข้าจากหลายสถานะ | `results/multiple_initial_conditions.png` |
| การอิ่มตัวของตัวกระตุ้น | ประเมินแรงควบคุมที่ถูกจำกัด | `results/saturation_comparison.png` |
| ความทนทานต่อสัญญาณรบกวน | ประเมินการวัดสถานะที่มีสัญญาณรบกวน | `results/noise_robustness.png` |
| ความทนทานต่อพารามิเตอร์ | เปลี่ยนมวล ค่าการหน่วง และค่าความแข็งของสปริง | `results/parameter_robustness.png` |
| การวิเคราะห์ปริภูมิสถานะ | แสดงวิถีเฟสและเส้นชั้น Lyapunov | `results/phase_portrait.png`, `results/lyapunov_contours.png` |
| บริเวณดึงดูด | เปรียบเทียบการลู่เข้าบนกริดของสถานะเริ่มต้น | `results/region_of_attraction_comparison.png` |
| การตัดองค์ประกอบด้านเสถียรภาพ | เปรียบเทียบน้ำหนักบทลงโทษ Lyapunov | `results/stability_weight_ablation.csv` |
| รายงานอัตโนมัติ | สรุปหลักฐานที่สร้างขึ้น | `results/experiment_report.th.md` |

ตัวชี้วัดเชิงตัวเลขทั้งหมดอยู่ใน [`results/performance_metrics.csv`](results/performance_metrics.csv)

## ภาพรวมผลลัพธ์

ผลลัพธ์ที่ติดตามในรีโพซิทอรีสร้างด้วยค่าเมล็ดสุ่มคงที่และการตั้งค่าการทดลองปัจจุบัน

| กรณี | นอร์มสถานะสุดท้าย | เวลาตั้งตัว | ต้นทุนกำลังสอง |
|---|---:|---:|---:|
| LQR, `x0 = [1.5, 0.0]` | `3.35e-06` | `3.37 s` | `14.6481` |
| โครงข่ายประสาท, `x0 = [1.5, 0.0]` | `2.75e-07` | `3.25 s` | `14.6803` |
| โครงข่ายประสาทแบบอิ่มตัว, `x0 = [1.5, 0.0]` | `2.73e-07` | `3.28 s` | `14.8506` |

ผลการตัดองค์ประกอบน้ำหนักเสถียรภาพแสดงว่าสัดส่วนการละเมิด Lyapunov เท่ากับ `0.0` สำหรับทุกน้ำหนักที่ทดสอบ ควรอ่านค่าร่วมกับขอบเขตการทดลองและข้อจำกัดที่ระบุไว้

## แกลเลอรีผลลัพธ์

| สถาปัตยกรรม | การตอบสนองของตัวควบคุม |
|---|---|
| ![สถาปัตยกรรมโมเดลวงปิด](results/model_architecture.png) | ![เปรียบเทียบตำแหน่ง LQR และโครงข่ายประสาท](results/position_comparison.png) |
| **การฝึกที่คำนึงถึงเสถียรภาพ** | **เปรียบเทียบบริเวณดึงดูด** |
| ![ค่าความสูญเสียระหว่างฝึก](results/training_loss.png) | ![เปรียบเทียบบริเวณดึงดูดของตัวควบคุม](results/region_of_attraction_comparison.png) |

รูปที่สร้างทั้งหมดอธิบายไว้ใน [คู่มือรูป](docs/th/figures.md)

## การติดตั้ง

ต้องใช้ Python 3.10 ขึ้นไป และการประมวลผลด้วย CPU เพียงพอ

```bash
git clone https://github.com/wolfchil345/lyapunov-nn-control-lab.git
cd lyapunov-nn-control-lab
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

บน Windows PowerShell ให้เปิดสภาพแวดล้อมด้วย `.venv\Scripts\Activate.ps1`

## การรันและตรวจสอบ

รันตัวอย่างสั้น:

```bash
python examples/quick_start.py
```

รันการทดลองทั้งหมด:

```bash
python main.py
```

รันชุดตรวจสอบมาตรฐานหรือด่านคุณภาพแบบเต็ม:

```bash
make checks
make quality-gate
```

คำสั่งที่มีประโยชน์อยู่ใน [คู่มือคำสั่ง](docs/th/commands.md) คำสั่ง `python scripts/clean_results.py` จะแสดงตัวอย่างไฟล์ที่สร้างขึ้นซึ่งรู้จักก่อน และต้องระบุ `--yes` อย่างชัดเจนจึงจะลบจริง โปรดอ่าน [ขั้นตอนการทดลอง](docs/th/experiment_workflow.md) ก่อน

## โครงสร้างโครงการ

```text
lyapunov-nn-control-lab/
├── main.py                 # ลำดับการทดลองทั้งหมด
├── src/                    # พลวัต ตัวควบคุม การวิเคราะห์ และการวาดกราฟ
├── tests/                  # ชุดทดสอบอัตโนมัติ
├── scripts/                # การตรวจและคำสั่งบำรุงรักษาที่ทำซ้ำได้
├── examples/               # ตัวอย่างขั้นต่ำที่รันได้
├── docs/{en,ja,ko,th}/     # เอกสารแต่ละภาษา
└── results/                # ผลอ้างอิงที่ Git ติดตามและโมเดลที่สร้างขึ้น
```

ดูรายละเอียดใน [คู่มือโครงสร้างโครงการ](docs/th/project_structure.md)

## ข้อจำกัดทางวิทยาศาสตร์

- ระบบเป็นการจำลองระบบมวล-สปริง-แดมเปอร์เชิงเส้น ไม่ใช่ฮาร์ดแวร์จริง
- ตัวควบคุมโครงข่ายประสาทเรียนรู้จากตัวควบคุม LQR ครู และอาจไม่สามารถใช้ได้ดีนอกบริเวณตัวอย่าง
- การประเมิน Lyapunov และบริเวณดึงดูดใช้กริดแบบจำกัดและการจำลอง
- การทดสอบความทนทานครอบคลุมเฉพาะสัญญาณรบกวน ขีดจำกัดอินพุต และการเปลี่ยนพารามิเตอร์ที่เลือก
- อาจเกิดความต่างเชิงตัวเลขเล็กน้อยระหว่างเวอร์ชันของแพ็กเกจหรือแพลตฟอร์ม

ก่อนสรุปผลเชิงวิจัย โปรดอ่าน [ข้อจำกัด](docs/th/limitations.md), [การตีความผลลัพธ์](docs/th/results_interpretation.md) และ [การทำซ้ำผล](docs/th/reproducibility.md)

## เอกสาร

ดัชนีเอกสารฉบับสมบูรณ์มีสี่ภาษา:

- [เอกสารภาษาอังกฤษ](docs/en/index.md)
- [日本語ドキュメント](docs/ja/index.md)
- [한국어 문서](docs/ko/index.md)
- [เอกสารภาษาไทย](docs/th/index.md)

เอกสารสำคัญได้แก่ [ระเบียบวิธี](docs/th/methodology.md), [ขั้นตอนการทดลอง](docs/th/experiment_workflow.md), [การ์ดแบบจำลอง](docs/th/model_card.md) และ [คำถามวิจัย](docs/th/research_questions.md)

## ชุมชนและข้อมูลโครงการ

- [แนวทางการมีส่วนร่วม](CONTRIBUTING.th.md)
- [นโยบายความปลอดภัย](SECURITY.th.md)
- [หลักปฏิบัติของชุมชน](CODE_OF_CONDUCT.th.md)
- [แผนงาน](ROADMAP.th.md)
- [บันทึกประจำรุ่น](RELEASE_NOTES.th.md)
- [ข้อมูลการอ้างอิง](CITATION.cff)

## สัญญาอนุญาตและผู้เขียน

เผยแพร่ภายใต้ [MIT License](LICENSE)

สร้างโดย Sirichet Sriamontham นักศึกษาวิศวกรรมเครื่องกลที่สนใจวิศวกรรมควบคุม โครงข่ายประสาท และการวิเคราะห์เสถียรภาพ
