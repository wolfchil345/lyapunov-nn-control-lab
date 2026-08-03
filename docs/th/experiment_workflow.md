🌐 ภาษา: [English](../en/experiment_workflow.md) | [日本語](../ja/experiment_workflow.md) | [한국어](../ko/experiment_workflow.md) | [ไทย](../th/experiment_workflow.md)

# ขั้นตอนการทดลอง

## ลำดับที่ปลอดภัย

1. ติดตั้งโครงการและรัน `python scripts/check_environment.py`
2. รัน `python examples/quick_start.py` และ `make checks`
3. บันทึกสาขา คอมมิต ค่าเมล็ดสุ่ม และพารามิเตอร์ที่จะเปลี่ยน
4. สำรองไฟล์ที่ Git ติดตามใน `results/` ก่อนล้างผลลัพธ์เก่า
5. รัน `python main.py` หรือ `python scripts/run_full_experiment.py`
6. รัน `python scripts/summarize_results.py` และตรวจกราฟกับไฟล์ CSV ทุกไฟล์
7. เปรียบเทียบตัวชี้วัดเฉพาะเมื่อการตั้งค่าเข้ากันได้
8. รัน `make quality-gate` ก่อนคอมมิต

## ผลลัพธ์ที่คาดหวัง

ลำดับงานเต็มจะสร้างกราฟเปรียบเทียบตัวควบคุม ผลทดสอบความทนทาน การวินิจฉัย Lyapunov การประมาณบริเวณดึงดูด ไฟล์ CSV สองไฟล์ `nn_controller.pt` และรายงานการทดลอง

## กฎการทบทวน

อย่าถือว่าความคลาดเคลื่อนต่ำ ค่า `V_dot` ที่เป็นลบบนจุดตัวอย่าง หรือการลู่เข้าบนกริดเป็นการพิสูจน์อย่างเป็นทางการ ควรบันทึกกรณีล้มเหลวและผลที่ไม่คาดคิดแทนการลบทิ้ง
