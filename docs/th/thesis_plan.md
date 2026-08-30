🌐 ภาษา: [English](../en/thesis_plan.md) | [日本語](../ja/thesis_plan.md) | [한국어](../ko/thesis_plan.md) | [ไทย](../th/thesis_plan.md)

# Thesis Plan

เอกสารนี้เชื่อม Lyapunov Neural-Network Control Lab เข้ากับแผนงานวิจัยเพื่อการสำเร็จการศึกษา

## Tentative title

Lyapunov-style stability evaluation of neural-network controllers for a mass-spring-damper system

## Background

neural-network controllers สามารถประมาณ nonlinear control policies ได้ แต่ stability behavior ของมันรับประกันได้ยาก

classical control methods เช่น LQR ให้ baseline ที่เชื่อถือได้สำหรับ linear systems

project นี้ศึกษาการใช้ neural-network controller ที่ฝึกจาก LQR teacher และประเมินด้วย Lyapunov-style checks

## Research objective

วัตถุประสงค์คือประเมินว่า neural-network controller สามารถเลียนแบบ LQR พร้อมรักษา closed-loop stability behavior ที่มีประโยชน์ใน simulation ได้หรือไม่

## Proposed method

1. กำหนด mass-spring-damper system
2. ออกแบบ LQR controller เป็น baseline
3. สร้าง training data จาก LQR controller
4. ฝึก neural-network controller
5. เพิ่ม stability-aware training penalty
6. จำลอง closed-loop responses
7. ประเมิน performance, robustness และ Lyapunov-style stability behavior

## Evaluation items

- final normalized-state norm
- normalized settling time
- quadratic LQR-style cost
- integrated squared control effort
- maximum absolute normalized control input
- Lyapunov derivative behavior
- robustness under noise
- robustness under parameter variation
- actuator saturation behavior
- finite-horizon convergence counts และ fractions พร้อม explicit sampling
	metadata

## Expected contribution

expected contribution คือ reproducible Python research workflow สำหรับเปรียบเทียบ classical controllers และ neural-network controllers โดยใช้ performance metrics, robustness tests และ Lyapunov-style stability checks

## Possible KAN extension

หลังจาก standard neural-network controller ทำงานได้แล้ว สามารถขยาย pipeline เดิมเพื่อเปรียบเทียบ KAN-based controller ได้

การเปรียบเทียบนี้สามารถตรวจว่า KAN ปรับปรุง imitation accuracy,
smoothness, robustness หรือ finite-horizon convergence ภายใต้เงื่อนไขเดียวกันได้หรือไม่

## Risks and limitations

- plant ปัจจุบันยังเรียบง่าย
- grid-based checks ไม่ได้พิสูจน์ global stability
- neural-network behavior นอก training region อาจไม่น่าเชื่อถือ
- simulation results ไม่เท่ากับ hardware validation

## Possible final thesis structure

1. Introduction
2. Background on LQR, neural-network control, and Lyapunov stability
3. System model and baseline controller
4. Neural-network controller design
5. Stability-aware training method
6. Simulation experiments
7. Robustness and finite-horizon convergence analysis
8. Discussion and limitations
9. Conclusion and future work
