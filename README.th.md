🌐 ภาษา: [English](README.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [ไทย](README.th.md)

[![Python tests](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/tests.yml/badge.svg)](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/tests.yml)
[![Local checks](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/local-checks.yml/badge.svg)](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/local-checks.yml)
[![Quality gate](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/quality-gate.yml/badge.svg)](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/quality-gate.yml)
[![Release](https://img.shields.io/github/v/release/wolfchil345/lyapunov-nn-control-lab)](https://github.com/wolfchil345/lyapunov-nn-control-lab/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Lyapunov NN Control Lab

การทดลองด้านการควบคุมด้วย Python และ PyTorch ที่ทำซ้ำได้ โดยฝึกตัวควบคุมโครงข่ายประสาทให้เลียนแบบตัวควบคุม LQR แล้วประเมินพฤติกรรมวงปิดด้วยการวิเคราะห์ Lyapunov แบบสุ่มตัวอย่าง การทดสอบความทนทาน และการประมาณ region of attraction

โครงการใช้ระบบมวล-สปริง-แดมเปอร์เป็นระบบทดสอบที่เข้าใจง่ายสำหรับการเชื่อมโยงวิศวกรรมเครื่องกล ทฤษฎีการควบคุม และ machine learning

## จุดเด่น

- ตัวควบคุม LQR อ้างอิงและตัวควบคุมโครงข่ายประสาทที่เรียนรู้การเลียนแบบ
- การฝึกที่คำนึงถึงเสถียรภาพด้วย Lyapunov penalty บนจุดตัวอย่าง
- การประเมินหลายเงื่อนไขเริ่มต้นและตัวชี้วัดเชิงปริมาณ
- การทดสอบ actuator saturation, noise ของการวัด และการเปลี่ยนพารามิเตอร์
- phase portrait, Lyapunov contour และการเปรียบเทียบ region of attraction
- สคริปต์ที่ทำซ้ำได้ การทดสอบอัตโนมัติ CI workflow และรายงานที่สร้างอัตโนมัติ
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

ระบบ plant คือ

```text
m q'' + c q' + k q = u
```

และสมการ state-space คือ

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

1. กำหนดระบบมวล-สปริง-แดมเปอร์ค่าปกติและออกแบบ LQR baseline
2. สุ่มสถานะและสร้าง label ด้วยกฎควบคุม LQR
3. ฝึกตัวควบคุมโครงข่ายประสาทด้วย imitation loss และ Lyapunov penalty
4. จำลอง LQR, neural และ saturated controller จากหลายสถานะเริ่มต้น
5. วัด final state norm, settling time, quadratic cost, control energy และ maximum control input
6. ประเมินพฤติกรรม Lyapunov บนจุดตัวอย่าง ความทนทาน และ region of attraction โดยประมาณ
7. บันทึกรูป ตัวชี้วัด CSV โมเดลที่ฝึกแล้ว และรายงานการทดลอง

## การทดลองและผลลัพธ์

| การทดลอง | จุดประสงค์ | ผลลัพธ์ |
|---|---|---|
| สถาปัตยกรรม | อธิบายโครงสร้างการควบคุมวงปิดด้วย neural network | `results/model_architecture.png` |
| เปรียบเทียบตัวควบคุม | เปรียบเทียบ trajectory ของ LQR และ neural controller | `results/position_comparison.png` |
| การฝึกที่คำนึงถึงเสถียรภาพ | ติดตาม total, imitation และ Lyapunov loss | `results/training_loss.png` |
| เงื่อนไขเริ่มต้น | ตรวจสอบการลู่เข้าจากหลายสถานะ | `results/multiple_initial_conditions.png` |
| Actuator saturation | ประเมินแรงควบคุมที่ถูกจำกัด | `results/saturation_comparison.png` |
| ความทนทานต่อ noise | ประเมินการวัดสถานะที่มี noise | `results/noise_robustness.png` |
| ความทนทานต่อพารามิเตอร์ | เปลี่ยนมวล damping และ stiffness | `results/parameter_robustness.png` |
| การวิเคราะห์ state-space | แสดง phase trajectory และ Lyapunov contour | `results/phase_portrait.png`, `results/lyapunov_contours.png` |
| Region of attraction | เปรียบเทียบการลู่เข้าบน grid ของสถานะเริ่มต้น | `results/region_of_attraction_comparison.png` |
| Stability ablation | เปรียบเทียบน้ำหนัก Lyapunov penalty | `results/stability_weight_ablation.csv` |
| รายงานอัตโนมัติ | สรุปหลักฐานที่สร้างขึ้น | `results/experiment_report.th.md` |

ตัวชี้วัดเชิงตัวเลขทั้งหมดอยู่ใน [`results/performance_metrics.csv`](results/performance_metrics.csv)

## ภาพรวมผลลัพธ์

ผลลัพธ์ที่ติดตามใน repository สร้างด้วย random seed คงที่และการตั้งค่าการทดลองปัจจุบัน

| กรณี | Final state norm | Settling time | Quadratic cost |
|---|---:|---:|---:|
| LQR, `x0 = [1.5, 0.0]` | `3.35e-06` | `3.37 s` | `14.6481` |
| Neural network, `x0 = [1.5, 0.0]` | `2.75e-07` | `3.25 s` | `14.6803` |
| Saturated neural network, `x0 = [1.5, 0.0]` | `2.73e-07` | `3.28 s` | `14.8506` |

ผล stability-weight ablation ที่ติดตามแสดง Lyapunov violation fraction เท่ากับ `0.0` สำหรับทุกน้ำหนักที่ทดสอบ ควรอ่านค่าร่วมกับขอบเขตการทดลองและข้อจำกัดที่ระบุไว้

## แกลเลอรีผลลัพธ์

| สถาปัตยกรรม | การตอบสนองของตัวควบคุม |
|---|---|
| ![สถาปัตยกรรมโมเดลวงปิด](results/model_architecture.png) | ![เปรียบเทียบตำแหน่ง LQR และ neural network](results/position_comparison.png) |
| **การฝึกที่คำนึงถึงเสถียรภาพ** | **เปรียบเทียบ region of attraction** |
| ![ค่าความสูญเสียระหว่างฝึก](results/training_loss.png) | ![เปรียบเทียบ region of attraction ของตัวควบคุม](results/region_of_attraction_comparison.png) |

รูปที่สร้างทั้งหมดอธิบายไว้ใน [คู่มือรูป](docs/th/figures.md)

## การติดตั้ง

ต้องใช้ Python 3.10 ขึ้นไป และการประมวลผลด้วย CPU เพียงพอ

```bash
git clone https://github.com/wolfchil345/lyapunov-nn-control-lab.git
cd lyapunov-nn-control-lab
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

บน Windows PowerShell ให้เปิด environment ด้วย `.venv\Scripts\Activate.ps1`

## การรันและตรวจสอบ

รันตัวอย่างสั้น:

```bash
python examples/quick_start.py
```

รันการทดลองทั้งหมด:

```bash
python main.py
```

รันชุดตรวจสอบมาตรฐานหรือ quality gate แบบเต็ม:

```bash
make checks
make quality-gate
```

คำสั่งที่มีประโยชน์อยู่ใน [คู่มือคำสั่ง](docs/th/commands.md) คำสั่ง `python scripts/clean_results.py` จะลบทุกไฟล์ใน `results/`; โปรดอ่าน [ขั้นตอนการทดลอง](docs/th/experiment_workflow.md) ก่อนใช้งาน

## โครงสร้างโครงการ

```text
lyapunov-nn-control-lab/
├── main.py                 # Full experiment pipeline
├── src/                    # Dynamics, controllers, analysis, and plotting
├── tests/                  # Automated test suite
├── scripts/                # Checks and repeatable maintenance commands
├── examples/               # Minimal runnable example
├── docs/{en,ja,ko,th}/     # Localized documentation
└── results/                # Tracked reference outputs and generated model
```

ดูรายละเอียดใน [คู่มือโครงสร้างโครงการ](docs/th/project_structure.md)

## ข้อจำกัดทางวิทยาศาสตร์

- plant เป็นการจำลองระบบมวล-สปริง-แดมเปอร์เชิงเส้น ไม่ใช่ฮาร์ดแวร์จริง
- neural controller เรียนรู้จาก LQR teacher และอาจไม่ generalize นอกบริเวณตัวอย่าง
- การประเมิน Lyapunov และ region of attraction ใช้ grid แบบจำกัดและการจำลอง
- การทดสอบความทนทานครอบคลุมเฉพาะ noise, input limit และ parameter variation ที่เลือก
- อาจเกิดความต่างเชิงตัวเลขเล็กน้อยระหว่างเวอร์ชัน dependency หรือ platform

ก่อนสรุปผลเชิงวิจัย โปรดอ่าน [ข้อจำกัด](docs/th/limitations.md), [การตีความผลลัพธ์](docs/th/results_interpretation.md) และ [การทำซ้ำผล](docs/th/reproducibility.md)

## เอกสาร

ดัชนีเอกสารฉบับสมบูรณ์มีสี่ภาษา:

- [English documentation](docs/en/index.md)
- [日本語ドキュメント](docs/ja/index.md)
- [한국어 문서](docs/ko/index.md)
- [เอกสารภาษาไทย](docs/th/index.md)

เอกสารสำคัญได้แก่ [ระเบียบวิธี](docs/th/methodology.md), [ขั้นตอนการทดลอง](docs/th/experiment_workflow.md), [model card](docs/th/model_card.md) และ [คำถามวิจัย](docs/th/research_questions.md)

## ชุมชนและข้อมูลโครงการ

- [แนวทางการมีส่วนร่วม](CONTRIBUTING.th.md)
- [นโยบายความปลอดภัย](SECURITY.th.md)
- [หลักปฏิบัติของชุมชน](CODE_OF_CONDUCT.th.md)
- [แผนงาน](ROADMAP.th.md)
- [บันทึกประจำรุ่น](RELEASE_NOTES.th.md)
- [ข้อมูลการอ้างอิง](CITATION.cff)

## สัญญาอนุญาตและผู้เขียน

เผยแพร่ภายใต้ [MIT License](LICENSE)

สร้างโดย Sirichet Sriamontham นักศึกษาวิศวกรรมเครื่องกลที่สนใจวิศวกรรมควบคุม neural networks และการวิเคราะห์เสถียรภาพ
