🌐 ภาษา: [English](../en/limitations.md) | [日本語](../ja/limitations.md) | [한국어](../ko/limitations.md) | [ไทย](../th/limitations.md)

# ข้อจำกัด

## แบบจำลองและข้อมูล

- Plant เป็น simulated linear mass-spring-damper system
- Training state ครอบคลุม bounded region และใช้ LQR teacher
- ผลไม่ยืนยัน generalization ไปยัง nonlinear plant หรือ unseen state

## หลักฐานเสถียรภาพ

- Quadratic Lyapunov function มาจากการออกแบบ LQR ค่าปกติ
- การประเมิน `V_dot` และ region of attraction ใช้ finite grid, threshold และ simulation horizon
- Zero sampled violation ไม่ใช่ formal หรือ global proof

## หลักฐานความทนทาน

- Actuator limit, noise level และ parameter variation เป็น scenario ที่เลือก ไม่ใช่ uncertainty set ครบถ้วน
- Numerical solver และ dependency version อาจสร้างความต่างเล็กน้อย
- ไม่มี hardware, delay, quantization, fault หรือ adversarial test

## การใช้อย่างรับผิดชอบ

Repository นี้เป็น educational research software ไม่ใช่ controller ที่ผ่านการรับรองความปลอดภัย ให้ตรวจสอบอย่างอิสระก่อนใช้กับ physical equipment

งานอนาคตมี nonlinear plant, formal verification, learned Lyapunov function, uncertainty analysis ที่กว้างขึ้น และ hardware validation
