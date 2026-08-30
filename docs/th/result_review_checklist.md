🌐 ภาษา: [English](../en/result_review_checklist.md) | [日本語](../ja/result_review_checklist.md) | [한국어](../ko/result_review_checklist.md) | [ไทย](../th/result_review_checklist.md)

# Result Review Checklist

ใช้ checklist นี้ก่อนนำ result files ที่สร้างแล้วไปใช้ใน report, presentation, thesis chapter หรือ portfolio

## 1. ยืนยันการตั้งค่าการทดลอง

- controller type ชัดเจน
- random seed ถูกบันทึก
- number of epochs ถูกบันทึก
- Lyapunov grid size ถูกบันทึก
- ผล finite-horizon convergence บันทึก horizon, strict final-state tolerance, bounds, resolution, tested count และ converged count
- การตั้งค่า noise หรือ parameter variation ถูกบันทึก

## 2. ยืนยันไฟล์ที่สร้างขึ้น

รัน:

```bash
python scripts/list_results.py
```

ตรวจว่าไฟล์สำคัญมีชื่อชัดเจนและเชื่อมกับการทดลองที่ถูกต้อง

## 3. รีวิว plots

- trajectories เคลื่อนเข้าหาจุดกำเนิดเมื่อคาดว่าเสถียร
- control signals ไม่มี spike แปลกๆ โดยไม่มีคำอธิบาย
- comparison plots ติดป้าย LQR, neural network และ controllers อื่นชัดเจน
- figures อ่านได้ชัดพอสำหรับ slides หรือ reports

## 4. รีวิว metrics

- เปรียบเทียบ metrics เฉพาะระหว่างการทดลองที่มีการตั้งค่าที่เข้ากันได้
- ไม่ตีความว่า cost หรือ error ที่ต่ำกว่าเป็นหลักฐานเสถียรภาพโดยลำพัง
- พิจารณา control effort ร่วมกับคุณภาพ tracking หรือ stabilization

## 5. รีวิวเอาต์พุตที่เกี่ยวข้องกับ Lyapunov

- อธิบาย grid-based checks ว่าเป็น sampled evidence
- ไม่อ้าง global proof เว้นแต่มี formal proof จริง
- เก็บและอธิบายเคสที่มีปัญหา ไม่ละทิ้งเงียบๆ

## 6. รีวิวเอาต์พุต finite-horizon convergence

- รายงาน percentages พร้อม horizon, tolerance และ sampled grid
- ไม่เรียก finite-time pass ว่า formal attraction region
- ไม่มอง finite-time failure เป็นหลักฐานของ asymptotic divergence
- แยก convergence map ออกจาก sampled Lyapunov checks ในเชิงแนวคิด

## 7. รีวิวเอาต์พุต robustness

- เขียน noise level หรือ parameter variation ให้ชัดเจน
- บันทึก failed cases
- ไม่ปะปน robustness results กับ baseline results โดยไม่มี labels

## 8. ก่อน commit ผลลัพธ์

รัน:

```bash
python scripts/check_environment.py
make checks
python scripts/list_results.py
git status
```

commit เฉพาะ result files ที่เป็นตัวอย่างที่มีประโยชน์, final artifacts หรือจำเป็นต่อเอกสาร

## กฎสุดท้าย

ผลลัพธ์สำคัญทุกชิ้นควรเข้าใจได้จาก file name, experiment log และเอกสารที่เกี่ยวข้อง
