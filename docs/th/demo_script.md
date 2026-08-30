🌐 ภาษา: [English](../en/demo_script.md) | [日本語](../ja/demo_script.md) | [한국어](../ko/demo_script.md) | [ไทย](../th/demo_script.md)

# Five Minute Demo Script

ใช้ script นี้เมื่อนำเสนอ project ต่ออาจารย์ reviewer interviewer หรือสมาชิกในแล็บ

## 0. Goal

แสดงว่า repository นี้เป็น reproducible research prototype สำหรับ neural network control ที่มีการประเมินแบบ Lyapunov-aware

## 1. Opening, 30 seconds

project นี้ศึกษาการใช้ neural network controller สำหรับ mass-spring-damper system โดย controller ถูกฝึกให้เลียนแบบ LQR controller แล้วประเมินด้วย simulation metrics, Lyapunov analysis, robustness tests และ sampled finite-horizon convergence maps

## 2. Repository tour, 60 seconds

- `README.md`: project overview และการใช้งานหลัก
- `src/`: implementation หลักของ system dynamics, controllers, simulation, Lyapunov checks, metrics, robustness และ plotting
- `tests/`: automated tests สำหรับพฤติกรรมสำคัญของ project
- `scripts/`: repeatable commands สำหรับ checking, cleaning, summarizing และ running experiments
- `docs/`: methodology, troubleshooting, reproducibility, review guides และ release process
- `results/`: figures, metrics และ reports ที่สร้างขึ้น

## 3. Run checks, 60 seconds

```bash
python scripts/check_environment.py
make checks
```

อธิบายว่า `make checks` รัน documentation link check, Python tests และ quick-start example

## 4. Explain research idea, 90 seconds

baseline controller คือ LQR ซึ่งให้ reference controller ที่มีเสถียรภาพสำหรับ linear system ส่วน neural network controller เรียนรู้จาก reference behavior นี้ หลังการฝึก project จะตรวจว่า learned controller มีพฤติกรรมดีใน closed-loop simulation หรือไม่ และตรวจว่า Lyapunov-related quantities ดูปลอดภัยบน grid หรือไม่

## 5. Show outputs, 60 seconds

แสดง generated plots และ summary files จาก `results/` โดยเน้น trajectory behavior, control signal behavior, performance metrics, Lyapunov checks, robustness results และ finite-horizon convergence comparisons ให้ระบุ horizon และ tolerance พร้อมอธิบายว่าไม่ใช่ mathematical attraction region

## 6. Closing, 30 seconds

ประเด็นสำคัญไม่ใช่แค่ neural network สามารถเลียนแบบ LQR ได้ แต่คือ repository นี้มี reproducible checks, documentation และ safety-focused evaluation tools ครบถ้วน

## Demo safety

ก่อน demo จริง ให้รัน:

```bash
python scripts/check_environment.py
make checks
git status
```

ทำ demo เฉพาะเมื่อ working tree สะอาดเท่านั้น
