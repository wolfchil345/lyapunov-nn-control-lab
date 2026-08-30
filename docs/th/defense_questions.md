🌐 ภาษา: [English](../en/defense_questions.md) | [日本語](../ja/defense_questions.md) | [한국어](../ko/defense_questions.md) | [ไทย](../th/defense_questions.md)

# Defense Questions

เอกสารนี้รวบรวมคำถามที่อาจถูกถามและประเด็นคำตอบสำหรับการนำเสนอหรือการสอบป้องกัน Lyapunov Neural-Network Control Lab

## Project motivation

### Why use a neural-network controller?
- neural network สามารถประมาณ control policy ที่ยืดหยุ่นได้
- มีประโยชน์เมื่อการออกแบบ controller แบบคลาสสิกทำได้ยากใน nonlinear systems
- project นี้ศึกษาประเด็นดังกล่าวกับ system ที่เรียบง่ายก่อน

### Why compare with LQR?
- LQR เป็น baseline แบบคลาสสิกที่เชื่อถือได้สำหรับ linear systems
- ทำหน้าที่เป็น teacher controller ที่ชัดเจนสำหรับ imitation learning
- การเปรียบเทียบกับ LQR ช่วยให้ประเมิน neural controller ได้ง่ายขึ้น

## Stability

### Why use Lyapunov-style checks?
- stability เป็นประเด็นสำคัญใน control engineering
- Lyapunov analysis ให้กรอบคิดในการพิจารณาว่า energy-like behavior ของ system ลดลงหรือไม่
- project นี้ใช้ grid-based checks เป็น empirical stability evidence

### Does this prove global stability?
- ไม่
- grid check ประเมินเฉพาะ sampled states
- ช่วยสนับสนุนการวิเคราะห์ แต่ไม่ใช่ full mathematical proof

## Experiments

### Why use a mass-spring-damper system?
- เรียบง่าย เข้าใจได้ง่าย และใช้กันทั่วไปในการเรียนการสอนด้าน control
- มี state แบบ position และ velocity จึงแสดงภาพได้ง่าย
- เป็น testbed แรกที่เหมาะสมก่อนขยับไปยัง nonlinear systems ที่ยากขึ้น

### Why test robustness?
- systems จริงมี noise, actuator limits และ parameter uncertainty
- robustness experiments แสดงว่า controller ยังทำงานได้หรือไม่ภายใต้เงื่อนไขที่ไม่สมบูรณ์ที่เลือกไว้

## Neural-network training

### What does the neural network learn?
- เรียนรู้ mapping จาก state ไปยัง control input
- target control input ถูกสร้างจาก LQR controller

### Why add a stability-aware penalty?
- การทำ imitation อย่างเดียวอาจตรงกับเอาต์พุต LQR แต่ยังมีพฤติกรรมไม่ดีใน closed-loop simulation
- penalty ช่วยส่งเสริม Lyapunov-style behavior ที่ดีขึ้นรอบ sampled states

## Results interpretation

### Which metric is most important?
- ไม่มี metric เดียวที่เพียงพอ
- ควรตีความร่วมกันทั้ง final normalized-state norm, normalized settling time, LQR-style cost, integrated squared control effort, Lyapunov behavior และ robustness

### What result would be considered successful?
- neural controller ควรลู่เข้าใกล้จุดกำเนิด
- ควรมีผลใกล้เคียง LQR
- ควรแสดงค่า Lyapunov derivative ที่เป็นลบเป็นส่วนใหญ่ในบริเวณที่ตรวจ
- ควรยังคงสมเหตุสมผลภายใต้ noise, saturation และ parameter variation

## Limitations

### What are the main limitations?
- plant ยังเรียบง่าย
- simulations ไม่ใช่ hardware experiments
- grid-based stability checks เป็น empirical
- neural network อาจล้มเหลวนอก training region

## Future work

### How can this become stronger research?
- ทดสอบ nonlinear plants
- เพิ่ม formal verification
- เปรียบเทียบกับ KAN-based controllers
- เรียนรู้ neural Lyapunov functions โดยตรง
- ประยุกต์วิธีการกับ control problems ที่สมจริงมากขึ้น
