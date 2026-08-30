🌐 ภาษา: [English](../en/presentation_outline.md) | [日本語](../ja/presentation_outline.md) | [한국어](../ko/presentation_outline.md) | [ไทย](../th/presentation_outline.md)

# Presentation Outline

outline นี้ใช้สำหรับนำเสนอ Lyapunov Neural-Network Control Lab ในชั้นเรียน lab meeting หรือ interview

## 1. Project motivation

- neural-network controllers มีความยืดหยุ่น แต่บางครั้งยากต่อการเชื่อถือ
- control engineering ต้องการ stability, robustness และ interpretability
- project นี้สำรวจ neural-network control ที่มี Lyapunov-style stability checks

## 2. System model

- plant คือ mass-spring-damper system
- state ประกอบด้วย normalized position `q` และ normalized velocity `v`
- control input เป็น normalized scalar โดยไม่กำหนด physical force unit

## 3. Baseline controller

- ใช้ LQR เป็น classical control baseline
- neural-network controller ถูกฝึกให้เลียนแบบ LQR

## 4. Neural-network controller

- model ทำ mapping จาก state ไปยัง control input
- training ใช้ imitation loss และ stability-aware penalty
- ถือว่าจุดกำเนิดเป็น target equilibrium

## 5. Stability analysis

- ใช้ Lyapunov-style function เพื่อตรวจสอบ stability behavior
- grid-based checks ประมาณบริเวณที่ Lyapunov derivative เป็นลบ
- finite-horizon convergence map รายงาน sampled initial states ที่ผ่าน `||x(T)||_2 < epsilon` สำหรับ normalized-time horizon และ normalized-state tolerance ที่ระบุ
- map นี้ไม่ใช่ mathematical region of attraction

## 6. Robustness experiments

- actuator saturation ตรวจสอบ input limits
- measurement-noise experiments ตรวจสอบ noisy state feedback
- parameter-variation experiments ตรวจสอบ normalized mass, damping และ stiffness coefficients ที่เปลี่ยนไป

## 7. Main outputs

- `performance_metrics.csv`
- `position_comparison.png`
- `phase_portrait.png`
- `lyapunov_contours.png`
- `finite_horizon_convergence_comparison.png`
- `experiment_report.md`

## 8. Key contribution

- project นี้รวม simulation, neural-network control, Lyapunov-style checks, robustness tests, automatic reports และ documentation ไว้ใน repository เดียวที่ทำซ้ำได้

## 9. Limitations

- system ยังเรียบง่ายเมื่อเทียบกับ plants จริง
- grid checks ให้ empirical evidence แต่ไม่ใช่ full global stability proof
- neural-network controller อาจมีพฤติกรรมไม่ดีนอก training region

## 10. Future work

- ทดสอบ nonlinear systems เพิ่มเติม
- เรียนรู้ neural Lyapunov functions โดยตรง
- เพิ่ม formal verification ที่เข้มขึ้น
- เปรียบเทียบกับ controller types ที่หลากหลายขึ้น
- นำ workflow ไปใช้กับ KAN-based controllers
