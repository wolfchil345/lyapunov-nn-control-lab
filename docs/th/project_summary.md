🌐 ภาษา: [English](../en/project_summary.md) | [日本語](../ja/project_summary.md) | [한국어](../ko/project_summary.md) | [ไทย](../th/project_summary.md)

# สรุปโครงการ

## Overview

โครงการนี้เป็นห้องปฏิบัติการวิจัยด้วย Python สำหรับ neural-network control ที่มีการวิเคราะห์เสถียรภาพตามแนวคิด Lyapunov

ระบบเป้าหมายคือพืชมวล-สปริง-แดมเปอร์ โครงการนี้เปรียบเทียบตัวควบคุม LQR แบบคลาสสิกกับตัวควบคุม neural-network ที่ฝึกด้วย imitation learning

## Main goal

เป้าหมายหลักคือศึกษาว่าตัวควบคุม neural-network สามารถเลียนแบบ LQR reference พร้อมรักษา transient behavior, robustness และ sampled Lyapunov behavior ที่มีประโยชน์ได้หรือไม่ พืชเชิงเส้น nominal แบบไม่ควบคุมมีเสถียรภาพแบบ asymptotic อยู่แล้ว; ตัวควบคุมเปลี่ยนสมรรถนะวงปิด

## Nominal plant (canonical)

พารามิเตอร์พืช normalized แบบ canonical ที่ใช้ทั่วทั้งรีโพซิทอรีคือ:

- MASS = 1.0
- DAMPING = 0.4
- STIFFNESS = 2.0

สำหรับพารามิเตอร์เหล่านี้ เมทริกซ์สถานะ `A` มี eigenvalues โดยประมาณเป็น `-0.2 + 1.4j` และ `-0.2 - 1.4j` ซึ่งมีส่วนจริงเป็นลบ ค่านี้เป็นส่วนหนึ่งของ canonical baseline และต้องคงไว้แบบตรงตัวในทุกภาษา

## Main features

- LQR baseline controller
- neural-network controller
- stability-aware training penalty
- Lyapunov grid check
- actuator saturation experiment
- measurement-noise robustness experiment
- parameter robustness experiment
- phase portrait visualization
- Lyapunov contour visualization
- finite-horizon convergence mapping with explicit sampling metadata
- controller comparison using an explicit finite-horizon final-state tolerance
- stability-weight ablation study
- automatic experiment report generation

## Key outputs

- `results/model_architecture.png`
- `results/position_comparison.png`
- `results/training_loss.png`
- `results/saturation_comparison.png`
- `results/noise_robustness.png`
- `results/parameter_robustness.png`
- `results/phase_portrait.png`
- `results/lyapunov_contours.png`
- `results/region_of_attraction.png` (historical filename ของ finite-horizon map)
- `results/region_of_attraction_comparison.png` (historical filename ของ finite-horizon comparison)
- `results/stability_weight_ablation.png`
- `results/experiment_report.md`

## Why this project matters

ตัวควบคุม neural-network มีพลังสูง แต่เสถียรภาพเป็นข้อกังวลสำคัญในวิศวกรรมควบคุม

โครงการนี้ผสาน learning-based control เข้ากับแนวคิดการวิเคราะห์เสถียรภาพแบบคลาสสิก โดยไม่ได้อ้างว่ามี formal proof แบบสมบูรณ์สำหรับตัวควบคุม neural-network แต่ให้เครื่องมือเชิงประจักษ์ที่ใช้งานได้จริงสำหรับศึกษาพฤติกรรมเสถียรภาพ

## Portfolio value

รีโพซิทอรีนี้แสดงทักษะด้านวิศวกรรมควบคุม, Python, PyTorch, numerical simulation, testing, visualization, GitHub Actions, documentation และ reproducible research workflow
