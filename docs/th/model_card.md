🌐 ภาษา: [English](../en/model_card.md) | [日本語](../ja/model_card.md) | [한국어](../ko/model_card.md) | [ไทย](../th/model_card.md)

# โมเดลการ์ด

## โมเดล

Controller เป็น PyTorch multilayer perceptron ขนาดเล็กที่ mapping `[position, velocity]` ไปเป็น force command หนึ่งค่า และ shift output เพื่อบังคับ `u(0) = 0`

## การฝึก

Sample state จาก bounded region และสร้าง label ด้วย nominal LQR controller การฝึกลด imitation MSE รวมกับ weighted sampled Lyapunov penalty Repository ตั้ง fixed random seed

## การใช้งานที่ตั้งใจ

- การศึกษาและ research prototyping สำหรับ learning-based control
- Reproducible comparison กับ LQR ใน simulation ที่รวมไว้
- การสำรวจ stability-aware objective และ robustness diagnostic

## นอกขอบเขต

- การ deployment โดยตรงกับ safety-critical หรือ hardware
- ข้ออ้าง formal, global หรือ distribution-free stability
- การทำงานนอก state, actuator และ plant range ที่ตรวจแล้ว

## การประเมิน

Closed-loop trajectory, final norm, settling time, cost, control energy, maximum input, sampled `V_dot`, robustness scenario และ estimated region of attraction

อ่าน [ข้อจำกัด](limitations.md) และ [การทำซ้ำผล](reproducibility.md) ก่อน reuse model
