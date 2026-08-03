🌐 ภาษา: [English](../en/results_interpretation.md) | [日本語](../ja/results_interpretation.md) | [한국어](../ko/results_interpretation.md) | [ไทย](../th/results_interpretation.md)

# การตีความผลลัพธ์

## ตัวชี้วัดประสิทธิภาพ

- `final_state_norm`: ระยะจากสมดุลเป้าหมายเมื่อสิ้นสุดเวลา
- `settling_time_s`: เวลาแรกที่หลังจากนั้นสถานะอยู่ใน threshold
- `quadratic_cost`: อินทิกรัลของ state และ control penalty แบบ LQR
- `control_energy`: อินทิกรัลของ control input ยกกำลังสอง
- `max_abs_control`: actuator command แบบค่าสัมบูรณ์ที่มากที่สุด

Metric เดียวไม่สามารถยืนยันเสถียรภาพหรือคุณภาพตัวควบคุมได้ ต้องเทียบการลู่เข้า effort, cost และ robustness ร่วมกัน

## หลักฐานด้านเสถียรภาพ

ค่า `V_dot` เป็นลบบนจุดตัวอย่างสนับสนุนการลดลงเฉพาะที่ใน grid ที่ประเมิน แต่ไม่พิสูจน์ระหว่างจุด นอกบริเวณ หรือ uncertainty ที่ไม่ได้ทดสอบ

## ความทนทานและ Region of Attraction

Noise, parameter variation และ actuator saturation เป็น scenario test แผนที่ region of attraction จำแนกเฉพาะสถานะเริ่มต้นที่สุ่มตัวอย่างภายใต้ horizon และ threshold ที่เลือก

## ลำดับการอ่าน

1. ตรวจการตั้งค่าและ seed
2. ตรวจ trajectory และ control limit
3. เปรียบเทียบ quantitative metric
4. ตรวจ Lyapunov และ region-of-attraction diagnostic
5. อ่าน [ข้อจำกัด](limitations.md) และบันทึก failure case
