🌐 ภาษา: [English](README.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [ไทย](README.th.md)

# Lyapunov NN Control Lab

โปรเจกต์นี้เป็นรีโพซิทอรีทดลองด้านวิศวกรรมควบคุม โดยใช้ตัวควบคุมแบบโครงข่ายประสาทเทียม

ระบบหลักที่ใช้คือระบบมวล-สปริง-แดมเปอร์ โดยให้ neural network เรียนรู้พฤติกรรมของตัวควบคุม LQR และผสมแนวคิดเสถียรภาพแบบ Lyapunov

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

## เอกสารสำคัญ

- [Project summary](docs/th/project_summary.md)
- [Methodology](docs/methodology.md)
- [Experiment workflow](docs/experiment_workflow.md)
- [Results interpretation](docs/results_interpretation.md)
- [Onboarding guide](docs/onboarding.md)
- [Maintenance guide](docs/maintenance.md)

## จุดประสงค์ด้านพอร์ตโฟลิโอ

รีโพซิทอรีนี้แสดงความสามารถในการผสมผสานวิศวกรรมควบคุม machine learning การวิเคราะห์เสถียรภาพ และการดูแล research software อย่างเป็นระบบ
