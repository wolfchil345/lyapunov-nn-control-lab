🌐 ภาษา: [English](../en/presentation_outline.md) | [日本語](../ja/presentation_outline.md) | [한국어](../ko/presentation_outline.md) | [ไทย](../th/presentation_outline.md)

# โครงร่างการนำเสนอ

1. **แรงจูงใจ:** Neural controller ยืดหยุ่น แต่ต้องตรวจเสถียรภาพและ robustness
2. **Plant:** Mass-spring-damper state-space model ที่มี position, velocity และ force input
3. **Baseline:** LQR ให้ stabilizing reference และ imitation target
4. **Neural controller:** Zero-at-origin architecture, imitation loss และ Lyapunov penalty
5. **การประเมิน:** Trajectory, settling time, cost, control effort และ sampled `V_dot`
6. **Robustness:** Actuator saturation, measurement noise และ parameter variation
7. **State-space evidence:** Phase portrait, Lyapunov contour และ region-of-attraction map
8. **ผลหลัก:** Neural controller ใกล้ LQR ใน test setting และ sampled Lyapunov violation fraction ที่ติดตามทั้งหมดเป็น zero
9. **ข้อจำกัด:** Simulated linear plant, finite grid, uncertainty case ที่เลือก และไม่มี formal proof
10. **งานอนาคต:** Nonlinear system, formal verification, learned Lyapunov function, KAN และ hardware validation

เมื่อเสนอข้ออ้างเชิงตัวเลข ให้ใช้ figure ที่มี caption อ่านได้และระบุ seed กับ tested region
