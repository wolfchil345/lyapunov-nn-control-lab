🌐 ภาษา: [English](../en/kan_extension.md) | [日本語](../ja/kan_extension.md) | [한국어](../ko/kan_extension.md) | [ไทย](../th/kan_extension.md)

# การต่อยอด KAN

## คำถาม

Kolmogorov-Arnold Network controller สามารถเทียบเท่าหรือดีกว่า MLP controller ปัจจุบัน โดยรักษา closed-loop stability และ robustness ใน test region ได้หรือไม่?

## แผนการพัฒนา

1. เพิ่ม KAN controller ที่ใช้ state-to-force interface เดียวกันใน `src/controllers.py`
2. คง dataset, seed, training region, initial state และ evaluation pipeline
3. เพิ่ม test สำหรับ shape, `u(0) = 0`, serialization และ simulation compatibility
4. เปรียบเทียบ LQR, MLP และ KAN ด้วย metric และ plot เดียวกัน

## การประเมิน

เปรียบเทียบ imitation loss, settling time, quadratic cost, control energy, maximum input, sampled Lyapunov violation fraction, robustness และ estimated region of attraction

## ข้อควรระวัง

Architecture ที่ตีความง่ายกว่าไม่ได้หมายความว่า controller จะเสถียรกว่าโดยอัตโนมัติ ใช้ limitations, review process และ formal-proof caveat แบบเดียวกับ MLP
