🌐 ภาษา: [English](../en/defense_questions.md) | [日本語](../ja/defense_questions.md) | [한국어](../ko/defense_questions.md) | [ไทย](../th/defense_questions.md)

# คำถามสำหรับการนำเสนอและการสอบ

## แรงจูงใจและการออกแบบ

**ทำไมใช้ LQR?** เพราะเป็น stabilizing baseline ที่โปร่งใสและให้ imitation target ที่เชื่อถือได้สำหรับ linear nominal plant

**Network เรียนรู้อะไร?** Mapping จาก position และ velocity ไปยัง scalar control force

**ทำไมบังคับ `u(0) = 0`?** เพราะ nonzero command ที่เป้าหมายอาจทำลาย equilibrium ที่ต้องการ

## เสถียรภาพ

**Grid check พิสูจน์ global stability หรือไม่?** ไม่ พิจารณา sampled state จำนวนจำกัดด้วย Lyapunov candidate หนึ่งตัว

**ทำไมใช้ Lyapunov penalty?** Imitation error อย่างเดียวไม่วัด closed-loop decay โดยตรง Penalty ช่วยส่งเสริม sampled decay condition ระหว่างฝึก

## การประเมิน

**Metric ใดสำคัญที่สุด?** ไม่มี metric เดียว ต้องตีความ convergence, cost, effort, sampled stability และ robustness ร่วมกัน

**ทำไมทดสอบ saturation, noise และ parameter variation?** ตัวควบคุมจริงมี input limit, sensor error และ model mismatch

## ข้อจำกัดและงานถัดไป

Plant ยังเรียบง่าย หลักฐานทั้งหมดมาจาก simulation และพฤติกรรมนอก training region ไม่แน่นอน งานที่แข็งแรงขึ้นควรมี nonlinear plant, formal verification, hardware experiment หรือ architecture อื่น เช่น KAN
