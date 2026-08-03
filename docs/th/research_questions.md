🌐 ภาษา: [English](../en/research_questions.md) | [日本語](../ja/research_questions.md) | [한국어](../ko/research_questions.md) | [ไทย](../th/research_questions.md)

# คำถามวิจัย

## คำถามหลัก

Neural controller สามารถเลียนแบบ LQR policy ที่ทำให้เสถียร พร้อมรักษาพฤติกรรม Lyapunov แบบสุ่มตัวอย่างและ robustness ที่ดีในการจำลองวงปิดได้หรือไม่?

## ประสิทธิภาพและเสถียรภาพ

- Settling time, quadratic cost และ control effort ใกล้ LQR เพียงใด?
- Sampled `V_dot` ไม่เป็นลบที่ใด และ training penalty เปลี่ยนอย่างไร?
- Region of attraction โดยประมาณต่างกันอย่างไรระหว่าง LQR, neural และ saturated controller?

## ความทนทาน

- Measurement noise, actuator saturation และ plant uncertainty กระทบการลู่เข้าอย่างไร?
- Test case ใดล้มเหลวก่อน และอยู่ในหรือนอก training region?

## การฝึกและสถาปัตยกรรม

- มี trade-off ใดระหว่าง imitation accuracy กับ stability-loss weight?
- KAN controller จะเปลี่ยน smoothness, interpretability, robustness หรือ region-of-attraction result หรือไม่?

เมื่อรายงานคำตอบให้ระบุ sampled region, threshold, seed และ limitations
