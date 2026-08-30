🌐 ภาษา: [English](../en/research_questions.md) | [日本語](../ja/research_questions.md) | [한국어](../ko/research_questions.md) | [ไทย](../th/research_questions.md)

# คำถามวิจัย

เอกสารนี้สรุปคำถามวิจัยที่เป็นไปได้สำหรับ Lyapunov Neural-Network Control Lab

## คำถามวิจัยหลัก

ตัวควบคุม neural-network สามารถเลียนแบบตัวควบคุม LQR พร้อมรักษาพฤติกรรมเสถียรภาพแบบ Lyapunov-style ที่มีประโยชน์ในการจำลองวงปิดได้หรือไม่

## สมรรถนะของตัวควบคุม

- สมรรถนะของตัวควบคุม neural-network ใกล้เคียง LQR baseline แค่ไหน
- ตัวควบคุม neural-network ลด final normalized-state norm ได้อย่างเชื่อถือได้หรือไม่
- normalized settling time, quadratic LQR-style cost และ integrated squared control effort เปรียบเทียบกันระหว่างตัวควบคุมได้อย่างไร

## พฤติกรรมด้านเสถียรภาพ

- Lyapunov derivative ยังคงเป็นค่าลบเป็นส่วนใหญ่ในบริเวณที่ตรวจสอบหรือไม่
- สถานะตั้งต้นที่สุ่มตัวอย่างใดบ้างที่ผ่านเกณฑ์ final-state tolerance หลัง finite horizon ที่กำหนด
- สัดส่วน finite-horizon นี้ไวต่อ horizon, tolerance, bounds และ grid resolution มากเพียงใด

## พฤติกรรมด้านความทนทาน

- measurement noise มีผลต่อตัวควบคุม neural-network อย่างไร
- actuator saturation มีผลต่อการลู่เข้าอย่างไร
- ตัวควบคุมไวต่อการเปลี่ยน normalized mass, damping และ stiffness coefficients มากเพียงใด

## การออกแบบการฝึก

- stability penalty weight มีผลต่อความแม่นยำของการเลียนแบบอย่างไร
- stability penalty weight มีผลต่อ Lyapunov derivative violations อย่างไร
- มี trade-off ที่มีประโยชน์ระหว่าง imitation loss และ stability-aware behavior หรือไม่

## คำถามส่วนขยาย KAN

- KAN controller สามารถเลียนแบบ LQR ได้เท่ากับหรือดีกว่า standard neural network หรือไม่
- KAN controller ให้พฤติกรรมการควบคุมที่เรียบขึ้นหรือตีความได้มากขึ้นหรือไม่
- KAN controller ปรับปรุง robustness หรือผล finite-horizon convergence ภายใต้ sampling settings เดียวกันหรือไม่

## แนวทางวิทยานิพนธ์ที่เป็นไปได้

แนวทางวิจัยระดับจบการศึกษาที่เป็นไปได้คือเปรียบเทียบ standard neural-network controllers กับ KAN-based controllers โดยใช้ Lyapunov-style evaluation pipeline เดียวกัน

## สรุปการประเมินที่แนะนำ

สำหรับแต่ละตัวควบคุม ให้รายงาน:

- performance metrics
- Lyapunov grid-check results
- robustness results
- finite-horizon convergence counts, percentages และ sampling metadata
- limitations และ failure cases
