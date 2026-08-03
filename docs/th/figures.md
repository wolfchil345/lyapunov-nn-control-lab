🌐 ภาษา: [English](../en/figures.md) | [日本語](../ja/figures.md) | [한국어](../ko/figures.md) | [ไทย](../th/figures.md)

# รูปและไฟล์ผลลัพธ์

| ไฟล์ | ความหมาย |
|---|---|
| `model_architecture.png` | โครงสร้างการควบคุม neural แบบวงปิด |
| `position_comparison.png` | การตอบสนองตำแหน่งของ LQR และ neural controller |
| `training_loss.png` | Total, imitation และ Lyapunov loss |
| `multiple_initial_conditions.png` | การลู่เข้าของ state norm จากหลายสถานะเริ่มต้น |
| `saturation_comparison.png` | ผลของ actuator limit |
| `noise_robustness.png` | การตอบสนองภายใต้ measurement noise |
| `parameter_robustness.png` | การตอบสนองเมื่อ plant เปลี่ยน |
| `phase_portrait.png` | Trajectory ในปริภูมิตำแหน่ง-ความเร็ว |
| `lyapunov_contours.png` | Lyapunov contour แบบกำลังสองและ trajectory |
| `region_of_attraction.png` | แผนที่การลู่เข้าจากจุดตัวอย่าง |
| `region_of_attraction_comparison.png` | เปรียบเทียบแผนที่การลู่เข้าระหว่างตัวควบคุม |
| `stability_weight_ablation.png` | ผลของน้ำหนัก stability loss |

ข้อมูลตัวเลขอยู่ใน `performance_metrics.csv` และ `stability_weight_ablation.csv` รายงานที่สร้างขึ้นสรุปหลักฐานเดียวกัน

ข้อความใน plot คงเป็นภาษาอังกฤษเพื่อให้เปรียบเทียบ scientific asset ชุดเดียวกันข้ามภาษาได้ เอกสารแต่ละภาษามี caption และคำอธิบายที่แปลแล้ว
