🌐 ภาษา: [English](../en/glossary.md) | [日本語](../ja/glossary.md) | [한국어](../ko/glossary.md) | [ไทย](../th/glossary.md)

# Glossary

glossary นี้อธิบายคำศัพท์สำคัญที่ใช้ใน Lyapunov Neural-Network Control Lab

## Control engineering terms

### State
พิกัดแบบ normalized และ dimensionless `x = [q, v]` โดย `q` คือ position-like coordinate และ `v = dq/dtau` คือ velocity ใน normalized time

### State norm
Euclidean normalized-state magnitude
`||x||_2 = sqrt(q^2 + v^2)` ซึ่งไม่ใช่ physical displacement หรือ velocity

### Control input
normalized scalar input `u` ที่ป้อนให้ model โดยไม่ได้กำหนด physical force unit

### Plant
system ที่ถูกควบคุม ใน project นี้ plant คือ mass-spring-damper system

### Closed-loop system
system ที่ controller ใช้ feedback จาก current state เพื่อเลือก control input

### LQR
Linear Quadratic Regulator เป็น classical optimal controller ที่ทำให้ quadratic cost ซึ่งรวม state error และ control effort มีค่าน้อยที่สุด

### Actuator saturation
ข้อจำกัดของขนาด normalized control input

## Stability terms

### Equilibrium
state ที่ system สามารถคงอยู่ได้โดยไม่เปลี่ยนแปลง ใน project นี้ target equilibrium คือจุดกำเนิด

### Lyapunov function
energy-like function ที่ใช้ศึกษาความเสถียร หากลดลงตาม trajectories โดยทั่วไปตีความได้ว่า system กำลังเคลื่อนไปสู่ equilibrium

### Lyapunov derivative
อัตราการเปลี่ยนแปลงของ Lyapunov function ตาม system trajectory

### Region of attraction
สำหรับ equilibrium ที่จุดกำเนิด คือเซต
`R = {x0 : x(t; x0) -> 0 as t -> infinity}`
การจำลองแบบ finite หรือกราฟ Lyapunov sublevel set เพียงอย่างเดียวไม่สามารถรับรองเซตนี้ได้

### Finite-horizon convergence map
sampled map ที่จัดประเภท initial state เมื่อ strict final-state criterion
`||x(T)||_2 < epsilon` เป็นจริงสำหรับ normalized-time horizon `T` และ
normalized-state Euclidean tolerance `epsilon` ผลลัพธ์ขึ้นกับพารามิเตอร์เหล่านี้ และไม่ใช่ region of attraction

### Integrated squared control effort
อินทิกรัลของ normalized `u^2` ตาม normalized time โดย historical field
name `control_energy` หมายถึงค่าตัวเดียวกัน แต่ไม่ใช่พลังงานทางกายภาพ

## Machine-learning terms

### Neural-network controller
controller ที่แทนด้วย neural network ซึ่งแมป system state ไปยัง control input

### Imitation learning
การฝึก model ให้คัดลอกพฤติกรรมของ controller อื่น ใน project นี้ neural network เลียนแบบ LQR

### Stability-aware training
การฝึกที่รวม penalty เกี่ยวกับ Lyapunov stability ไม่ได้พิจารณาเพียง imitation accuracy

### Ablation study
การทดลองที่เปลี่ยนหรือถอดปัจจัยการออกแบบหนึ่งอย่างเพื่อดูผลกระทบ โดย project นี้เปลี่ยน stability penalty weight
