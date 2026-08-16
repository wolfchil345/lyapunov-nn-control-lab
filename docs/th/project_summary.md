🌐 ภาษา: [English](../en/project_summary.md) | [日本語](../ja/project_summary.md) | [한국어](../ko/project_summary.md) | [ไทย](../th/project_summary.md)

# ภาพรวมโปรเจกต์

Lyapunov NN Control Lab เป็นโปรเจกต์พอร์ตโฟลิโอเชิงวิจัยที่ผสมผสานวิศวกรรมควบคุมกับ machine learning

โปรเจกต์นี้ใช้ระบบมวล-สปริง-แดมเปอร์เป็นตัวอย่างหลัก โดยฝึก neural network controller ให้เลียนแบบพฤติกรรมของ LQR controller และใช้แนวคิดจาก Lyapunov function เพื่อประเมินเสถียรภาพของระบบวงปิด

## เป้าหมาย

- ฝึก neural network controller
- เปรียบเทียบพฤติกรรมกับ LQR controller
- ตรวจสอบเสถียรภาพด้วย Lyapunov function
- แสดงผลการจำลองด้วยกราฟ
- จัดโปรเจกต์ให้เป็น research software ที่ทำซ้ำได้

## เทคโนโลยีหลัก

- Python
- PyTorch
- LQR control
- Lyapunov stability
- Simulation evaluation
- การตรวจสอบอัตโนมัติด้วย GitHub Actions

## คุณค่าในพอร์ตโฟลิโอ

รีโพซิทอรีนี้แสดงความสามารถในการเชื่อมโยงวิศวกรรมควบคุม machine learning การวิเคราะห์เสถียรภาพ และการดูแล research software อย่างเป็นระบบ

## พืช (公称) และค่าสำคัญ

พารามิเตอร์ปกติที่ใช้ในโปรเจกต์นี้คือ MASS = 1.0, DAMPING = 0.4, STIFFNESS = 2.0. สำหรับพารามิเตอร์เหล่านี้ เมทริกซ์ `A` มี eigenvalues ประมาณ `-0.2 + 1.4j` และ `-0.2 - 1.4j` ซึ่งมีส่วนจริงเป็นลบ ดังนั้นพืช (nominal uncontrolled linear plant) จึงเป็นแบบลู่เข้าเชิงกำกับ (asymptotically stable) อยู่แล้ว LQR จึงทำหน้าที่ปรับ trade-off ของการควบคุม ไม่ได้เป็นการทำให้ระบบที่ไม่เสถียรกลายเป็นเสถียร

## Key outputs

- `results/model_architecture.png`
- `results/position_comparison.png`
- `results/training_loss.png`
- `results/saturation_comparison.png`
- `results/noise_robustness.png`
- `results/parameter_robustness.png`
- `results/phase_portrait.png`
- `results/lyapunov_contours.png`
- `results/region_of_attraction.png` (ชื่อไฟล์เชิงประวัติศาสตร์ — มาจากแผนที่การลู่เข้าแบบเก่า)
- `results/region_of_attraction_comparison.png` (ชื่อไฟล์เชิงประวัติศาสตร์)
- `results/stability_weight_ablation.png`
- `results/experiment_report.md`
