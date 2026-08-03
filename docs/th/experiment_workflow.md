🌐 ภาษา: [English](../en/experiment_workflow.md) | [日本語](../ja/experiment_workflow.md) | [한국어](../ko/experiment_workflow.md) | [ไทย](../th/experiment_workflow.md)

# ขั้นตอนการทดลอง

## ลำดับที่ปลอดภัย

1. ติดตั้ง project และรัน `python scripts/check_environment.py`
2. รัน `python examples/quick_start.py` และ `make checks`
3. บันทึก branch, commit, seed และ parameter ที่จะเปลี่ยน
4. Backup ไฟล์ที่ติดตามใน `results/` ก่อน cleanup
5. รัน `python main.py` หรือ `python scripts/run_full_experiment.py`
6. รัน `python scripts/summarize_results.py` และตรวจทุก plot กับ CSV
7. เปรียบเทียบ metric เมื่อการตั้งค่าเข้ากันได้เท่านั้น
8. รัน `make quality-gate` ก่อน commit

## ผลลัพธ์ที่คาดหวัง

Pipeline เต็มสร้างการเปรียบเทียบตัวควบคุม robustness plot การวินิจฉัย Lyapunov การประมาณ region of attraction ไฟล์ CSV สองไฟล์ `nn_controller.pt` และรายงานการทดลอง

## กฎการ Review

อย่าถือ error ต่ำ ค่า `V_dot` เป็นลบบนจุดตัวอย่าง หรือการลู่เข้าบน grid ว่าเป็นการพิสูจน์อย่างเป็นทางการ ให้บันทึก failure และผลที่ไม่คาดหมายแทนการลบ
