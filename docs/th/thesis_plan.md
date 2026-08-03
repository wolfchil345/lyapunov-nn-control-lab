🌐 ภาษา: [English](../en/thesis_plan.md) | [日本語](../ja/thesis_plan.md) | [한국어](../ko/thesis_plan.md) | [ไทย](../th/thesis_plan.md)

# แผนวิทยานิพนธ์

## ชื่อเบื้องต้น

การควบคุมโครงข่ายประสาทที่คำนึงถึง Lyapunov สำหรับระบบพลวัตเชิงกล

## วัตถุประสงค์

ประเมินว่า neural controller ที่เรียนจาก LQR teacher สามารถรักษา closed-loop performance, sampled stability behavior และ robustness ที่ดีภายใต้เงื่อนไขไม่สมบูรณ์ที่เลือกได้หรือไม่

## วิธีการ

1. หา state-space plant และ LQR baseline
2. ฝึก neural controller ด้วย imitation loss และ stability-aware loss
3. เปรียบเทียบ trajectory, cost, effort และ settling time
4. ประเมิน sampled Lyapunov behavior และ region of attraction โดยประมาณ
5. ทดสอบ saturation, noise และ parameter variation
6. บันทึก limitations และ reproducibility

## โครงสร้างบทที่แนะนำ

1. บทนำและงานที่เกี่ยวข้อง
2. System model และการออกแบบ LQR
3. การฝึก neural controller
4. การประเมินเสถียรภาพและ robustness
5. ผลลัพธ์และอภิปราย
6. ข้อจำกัด สรุป และงานอนาคต

System ปัจจุบันเป็น simulation testbed ส่วน hardware validation และ formal verification เป็นงานต่อยอด
