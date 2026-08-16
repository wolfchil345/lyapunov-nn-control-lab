🌐 ภาษา: [English](README.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [ไทย](README.th.md)

# ![Python tests](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/tests.yml/badge.svg)
# ![Quality gate](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/quality-gate.yml/badge.svg)

# Lyapunov NN Control Lab

โปรเจกต์นี้เป็นรีโพซิทอรีทดลองด้านวิศวกรรมควบคุม โดยใช้ตัวควบคุมแบบโครงข่ายประสาทเทียม

ระบบหลักที่ใช้คือระบบมวล-สปริง-แดมเปอร์ โดยให้ neural network เรียนรู้พฤติกรรมของตัวควบคุม LQR และใช้แนวคิดจาก Lyapunov ในการประเมินเสถียรภาพ

## เนื้อหาหลัก

- การฝึกตัวควบคุมด้วย Python และ PyTorch
- Neural network controller ที่เรียนรู้จาก LQR controller
- การใช้ Lyapunov penalty เพื่อคำนึงถึงเสถียรภาพ
- การจำลองระบบ การประเมินผล การทดสอบความทนทาน และการสร้างกราฟ
- การตรวจสอบคุณภาพด้วย GitHub Actions, tests และ quality gate

## เริ่มใช้งาน

```bash
python scripts/check_environment.py
python examples/quick_start.py
python scripts/quality_gate.py
```

## หมายเหตุทางเทคนิคที่สำคัญ

พารามิเตอร์มาตรฐานของโมเดลที่ใช้เป็นค่า normalized คือ: MASS = 1.0, DAMPING = 0.4, STIFFNESS = 2.0. สำหรับค่าพารามิเตอร์นี้ เมทริกซ์ `A` มี eigenvalues โดยประมาณ `-0.2 + 1.4j` และ `-0.2 - 1.4j` ซึ่งมีส่วนจริงเป็นลบ ดังนั้นพืช (plant) เชิงเส้น nominal ที่ไม่มีการควบคุมอยู่แล้วจะเป็นแบบลู่เข้าเชิงกำกับ (asymptotically stable)。LQR จึงเปลี่ยนเฉพาะการตอบสนองชั่วคราวและ trade-off ในการควบคุม ไม่ได้มีเป้าหมายเพื่อทำให้ระบบที่ไม่เสถียรกลายเป็นเสถียร

รีโพซิทอรีนี้ใช้แบบจำลองอันดับสองแบบ normalized และไร้มิติ: `tau` คือเวลา normalized, `q` คือพิกัดตำแหน่งแบบ normalized, `v = dq/dtau` คือความเร็ว normalized, `u` คืออินพุตควบคุม normalized, และ `x = [q, v]`。

`||x||_2 = sqrt(q^2 + v^2)` เป็น Euclidean norm ในพิกัดสถานะที่ normalized แล้ว ค่า field ชื่อ `settling_time_s` ยังคงถูกเก็บไว้เป็น alias ทางความเข้ากันได้ แต่มันหมายถึงเวลา normalized

## เอกสารสำคัญ

- [ดัชนีเอกสาร](docs/th/index.md)
- [Project summary](docs/th/project_summary.md)
- [Methodology](docs/th/methodology.md)
- [Experiment workflow](docs/experiment_workflow.md)
- [Results interpretation](docs/results_interpretation.md)
- [Onboarding guide](docs/onboarding.md)
- [Maintenance guide](docs/maintenance.md)

## Lyapunov การประเมินและการฝึก

การประเมิน Lyapunov แบบตัวอย่างใช้รูปอนุพันธ์ดังนี้:

```text
V-dot(x) = 2 x^T P (A x + B pi(x))
```

การประเมินรายงานเงื่อนไขสองแบบ:

```text
พื้นฐานการลด: V-dot(x) <= 0
เงื่อนไข decay margin: V-dot(x) + alpha * ||x||_2^2 <= 0
```

การฝึกที่คำนึงถึงเสถียรภาพใช้การลงโทษส่วนบวกของ decay residual:

```text
decay residual = V-dot(x) + alpha * ||x||_2^2
Lyapunov penalty = mean(ReLU(decay residual))
```

ค่าเริ่มต้นของ decay margin คือ `alpha = 0.05` (เทียบเท่ากับ `DEFAULT_DECAY_MARGIN = 0.05`) ค่าความทนทานเชิงตัวเลข (เช่น `1e-9`) ถูกแยกจาก `alpha` และใช้เป็นเกณฑ์การจัดประเภทสำหรับการละเมิดเชิงตัวเลข

## การวิเคราะห์การลู่เข้าในช่วงเวลาจำกัด

เกณฑ์ที่ใช้คือ:

```text
||x(T)||_2 < epsilon
```

ผลลัพธ์นี้เป็นแผนที่เชิงประจักษ์ที่อิงตัวอย่าง ไม่ใช่การพิสูจน์เชิงรูปแบบสำหรับบริเวณดึงดูดทั้งหมด

## ผลลัพธ์และ provenance

รันผลจะถูกเก็บใน `results/runs/<run_id>/` พร้อมไฟล์มานิเฟสต์และ SHA-256 เช่น `manifest.json`, `SHA256SUMS`, `report.md` เป็นต้น ผลลัพธ์รุ่นเก่า (เช่น `results/region_of_attraction.png`) ถูกเก็บไว้เป็นอาร์ติแฟกต์เชิงประวัติศาสตร์เพื่อความสามารถในการทำซ้ำ


## จุดประสงค์ด้านพอร์ตโฟลิโอ

รีโพซิทอรีนี้แสดงความสามารถในการผสมผสานวิศวกรรมควบคุม machine learning การวิเคราะห์เสถียรภาพ และการดูแล research software อย่างเป็นระบบ
