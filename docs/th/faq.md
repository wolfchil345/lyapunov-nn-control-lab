🌐 ภาษา: [English](../en/faq.md) | [日本語](../ja/faq.md) | [한국어](../ko/faq.md) | [ไทย](../th/faq.md)

# คำถามที่พบบ่อย

## Project นี้เกี่ยวกับอะไร?

ฝึก neural controller ให้เลียนแบบ LQR บน mass-spring-damper system และประเมิน performance, sampled Lyapunov behavior และ robustness

## ทำไมใช้ LQR เป็น teacher?

LQR โปร่งใส ทำซ้ำได้ และทำให้ nominal linear plant เสถียร จึงเป็น baseline และแหล่ง label ที่มีประโยชน์

## Project พิสูจน์เสถียรภาพหรือไม่?

ไม่ ให้หลักฐานจาก simulation และ finite grid ด้วย quadratic Lyapunov candidate ส่วน formal continuous-domain verification อยู่นอกขอบเขตปัจจุบัน

## ต่างจาก machine-learning demo ทั่วไปอย่างไร?

ประเมิน closed-loop trajectory, control effort, cost, saturation, noise, model variation, Lyapunov behavior และ estimated region of attraction พร้อม software check ที่ทำซ้ำได้

## ตรวจสอบอย่างไร?

รัน `python examples/quick_start.py`, `make checks` และ `make quality-gate` ใช้ `python main.py` สำหรับการทดลองเต็ม

## เริ่มอ่านที่ไหน?

อ่าน [สรุปโครงการ](project_summary.md), [ระเบียบวิธี](methodology.md), [ขั้นตอนการทดลอง](experiment_workflow.md) และ [ข้อจำกัด](limitations.md)
