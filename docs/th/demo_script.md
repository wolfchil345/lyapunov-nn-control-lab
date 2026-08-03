🌐 ภาษา: [English](../en/demo_script.md) | [日本語](../ja/demo_script.md) | [한국어](../ko/demo_script.md) | [ไทย](../th/demo_script.md)

# สคริปต์สาธิตห้านาที

## 0:00–0:30 — จุดประสงค์

“Project นี้ศึกษาตัวควบคุม neural ที่เลียนแบบ LQR และประเมินด้วย Lyapunov-style กับ robustness check”

## 0:30–1:30 — Repository tour

แสดง `README.md`, `src/`, `tests/`, `scripts/`, `docs/` หลายภาษา และ `results/`

## 1:30–2:15 — การทำซ้ำผล

รัน `python examples/quick_start.py` หรือแสดงผล `make quality-gate` ที่เสร็จแล้ว อย่าเริ่ม full experiment ระหว่าง demo สั้น

## 2:15–3:30 — วิธีการ

อธิบาย mass-spring-damper model, LQR teacher, neural imitation, `u(0) = 0` และ sampled Lyapunov penalty

## 3:30–4:30 — หลักฐาน

แสดง `position_comparison.png`, `training_loss.png` และ `region_of_attraction_comparison.png` พร้อมกล่าวถึง saturation, noise และ parameter test

## 4:30–5:00 — ข้อสรุปที่ซื่อตรง

ระบุว่าผลเป็น simulation-based และ sampled แล้วอธิบายขั้นวิจัยถัดไป
