🌐 ภาษา: [English](../en/experiment_parameters.md) | [日本語](../ja/experiment_parameters.md) | [한국어](../ko/experiment_parameters.md) | [ไทย](../th/experiment_parameters.md)

# Parameter การทดลอง

## กลุ่ม Parameter

| กลุ่ม | ตัวอย่าง | ตำแหน่งหลัก |
|---|---|---|
| Plant | mass, damping, stiffness | `src/system.py`, `src/parameter_variation.py` |
| Controller | `Q`, `R`, network size, saturation limit | `src/system.py`, `src/controllers.py`, `main.py` |
| Training | seed, epochs, learning rate, dataset size, loss weights | `src/controllers.py`, `main.py` |
| Simulation | initial state, duration, evaluation times | `src/simulation.py`, `main.py` |
| Stability | state range, grid density, decay margin | `src/lyapunov.py`, `main.py` |
| Robustness | noise, parameter cases, ablation weights | `src/noise.py`, `src/parameter_variation.py`, `src/stability_ablation.py` |

## การเปรียบเทียบที่ยุติธรรม

เปลี่ยนทีละหนึ่งกลุ่ม parameter ให้คง seed, initial state, simulation horizon และ evaluation metric เว้นแต่สิ่งนั้นคือคำถามวิจัย

บันทึกค่าที่แน่นอนใน [บันทึกการทดลอง](experiment_log_template.md) ก่อนยอมรับ reference result ใหม่
