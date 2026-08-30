🌐 ภาษา: [English](../en/faq.md) | [日本語](../ja/faq.md) | [한국어](../ko/faq.md) | [ไทย](../th/faq.md)

# Frequently Asked Questions

หน้านี้ตอบคำถามที่พบบ่อยเกี่ยวกับ project

## What is this project about?

project นี้ฝึกและประเมิน neural network controller สำหรับระบบ
mass-spring-damper โดย controller เรียนรู้จาก LQR reference และถูก
ประเมินด้วย simulation metrics, Lyapunov-style checks, robustness tests
และ sampled finite-horizon convergence maps

## Why use LQR as the reference controller?

LQR เป็นวิธีควบคุมมาตรฐานสำหรับ linear systems โดยให้ reference policy ที่มีเสถียรภาพและตีความได้ จึงเหมาะสำหรับใช้ฝึกและเปรียบเทียบ neural network controller

## Does this project prove global stability?

ไม่ใช่ Lyapunov grid check เป็นเครื่องมือประเมินเชิงประจักษ์ สามารถให้ evidence ที่มีประโยชน์บน sampled states ได้ แต่ไม่ควรอธิบายว่าเป็น complete formal proof ของ global stability

## What makes this project different from a normal machine learning demo?

project นี้ไม่ได้แค่ฝึก neural network เท่านั้น แต่ยังประเมิน closed-loop behavior, control cost, robustness, Lyapunov-related quantities, reproducibility และ documentation quality ด้วย

## What should I show first in a presentation?

เริ่มจาก README แล้วตามด้วย five minute demo script, main experiment workflow, results plots และเอกสารด้าน Lyapunov หรือ robustness

## How do I check that the project is working?

```bash
python scripts/check_environment.py
make checks
```

## Where are the main files?

- `src/`: source code
- `tests/`: automated tests
- `scripts/`: repeatable command scripts
- `docs/`: explanations and guides
- `results/`: generated outputs

## What are the current limitations?

นี่เป็น research prototype ผลลัพธ์ขึ้นอยู่กับ system ที่เลือก, controller settings, training setup, random seed, sampled grid และ experiment conditions
