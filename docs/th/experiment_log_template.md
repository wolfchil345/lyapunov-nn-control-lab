🌐 ภาษา: [English](../en/experiment_log_template.md) | [日本語](../ja/experiment_log_template.md) | [한국어](../ko/experiment_log_template.md) | [ไทย](../th/experiment_log_template.md)

# Template บันทึกการทดลอง

## ข้อมูลประจำการทดลอง

- วันที่:
- Branch และ commit SHA:
- คำถามวิจัย:
- จุดประสงค์:

## Environment และการตั้งค่า

- Python และ PyTorch version:
- Runtime:
- Random seed:
- Epochs, learning rate, dataset size, network architecture:
- การตั้งค่า plant, controller, simulation, Lyapunov, noise และ parameter:

## คำสั่งและผลลัพธ์

- คำสั่งที่ใช้:
- Metrics CSV:
- Report:
- Figures:

## การตีความ

- อะไรดีขึ้นหรือแย่ลง?
- เปรียบเทียบกับ LQR อย่างไร?
- มี sampled Lyapunov violation หรือ robustness failure หรือไม่?
- การตั้งค่าเทียบกับ run ก่อนหน้าได้หรือไม่?

## การตัดสินใจ

- เก็บเป็น reference result? Yes / No
- ใช้ใน report หรือ presentation? Yes / No
- การทดลองถัดไป:

สร้างสำเนาที่มี timestamp ด้วย `python scripts/new_experiment_log.py "short description" --language th`
