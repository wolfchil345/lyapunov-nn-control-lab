🌐 ภาษา: [English](../en/glossary.md) | [日本語](../ja/glossary.md) | [한국어](../ko/glossary.md) | [ไทย](../th/glossary.md)

# อภิธานศัพท์

- **State (สถานะ)**: ตัวแปรที่อธิบายระบบ ในที่นี้คือตำแหน่งและความเร็ว
- **Plant**: ระบบจริงหรือระบบจำลองที่ถูกควบคุม
- **Control input**: คำสั่งแรง `u` ที่ใช้กับ plant
- **Closed loop**: Controller และ plant ที่เชื่อมด้วย state feedback
- **LQR**: Linear Quadratic Regulator ซึ่งเป็น baseline และ teacher แบบดั้งเดิม
- **Equilibrium (จุดสมดุล)**: สถานะที่ไม่เปลี่ยน เป้าหมายคือจุดกำเนิด
- **Lyapunov function**: ฟังก์ชันบวกคล้ายพลังงานสำหรับศึกษาเสถียรภาพ
- **Lyapunov derivative**: อัตราการเปลี่ยน `V_dot` ตาม trajectory
- **Actuator saturation**: ขีดจำกัดของ control input ที่ทำได้
- **Region of attraction**: ชุด initial state ที่ลู่เข้าสู่สมดุลภายใต้เงื่อนไขที่ระบุ
- **Imitation learning**: การฝึก model ให้ทำตาม action ของ teacher
- **Stability-aware training**: การฝึกที่มี sampled Lyapunov penalty
- **Ablation study**: การเปรียบเทียบที่เปลี่ยนเพียงหนึ่ง design choice

Code identifier และสัญลักษณ์คณิตศาสตร์คงเป็นภาษาอังกฤษในทุกคำแปล
