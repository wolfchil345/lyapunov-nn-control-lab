🌐 ภาษา: [English](../en/kan_extension.md) | [日本語](../ja/kan_extension.md) | [한국어](../ko/kan_extension.md) | [ไทย](../th/kan_extension.md)

# คู่มือ KAN Extension

คู่มือนี้อธิบายว่า Lyapunov Neural-Network Control Lab ปัจจุบันสามารถขยายไปสู่การทดลองตัวควบคุมแบบ Kolmogorov-Arnold Network ได้อย่างไร

## Motivation

โครงการปัจจุบันใช้ตัวควบคุม neural-network มาตรฐานเพื่อเลียนแบบ LQR และประเมินพฤติกรรมที่เกี่ยวข้องกับเสถียรภาพ

ตัวควบคุมแบบ KAN-based สามารถนำมาทดสอบเป็น function approximator ทางเลือกสำหรับการแมประหว่างสถานะระบบกับอินพุตควบคุม

## Current controller pipeline

workflow ปัจจุบันคือ:

1. กำหนดระบบ mass-spring-damper
2. สร้างข้อมูลฝึกจากตัวควบคุม LQR
3. ฝึกตัวควบคุม neural-network
4. จำลองพฤติกรรมวงปิด
5. คำนวณ performance metrics
6. ตรวจสอบ Lyapunov-style stability behavior
7. รันการทดลอง robustness และ finite-horizon convergence

## KAN controller idea

แนวคิดของ KAN controller คือแทนที่โมเดล neural-network มาตรฐานด้วยโมเดลแบบ KAN-style

อินพุตยังคงเป็นสถานะของระบบ:

- position
- velocity

เอาต์พุตยังคงเป็นอินพุตควบคุม:

- normalized scalar control input

## Files that may need changes

### `src/controllers.py`
เพิ่ม KAN controller class หรือ wrapper function

### `main.py`
เพิ่มการฝึก, simulation, metrics และ plotting ของ KAN ควบคู่กับ LQR และตัวควบคุม neural-network ปัจจุบัน

### `src/plotting.py`
เพิ่ม plots สำหรับเปรียบเทียบ LQR, standard neural network และ KAN

### `tests/`
เพิ่ม tests เพื่อตรวจว่า KAN controller ให้ scalar control ที่ถูกต้องและสามารถรันในการจำลองได้

## Suggested experiment design

เปรียบเทียบตัวควบคุมสามแบบ:

- LQR baseline
- standard neural-network controller
- KAN controller

ใช้ initial states, metrics และ Lyapunov checks ชุดเดียวกันสำหรับทุกตัวควบคุม

## Suggested metrics

- final normalized-state norm
- normalized settling time
- quadratic LQR-style cost
- integrated squared control effort
- maximum absolute normalized control input
- Lyapunov derivative violation fraction
- finite-horizon convergence count and fraction

## Suggested plots

- position comparison
- control input comparison
- phase portrait comparison
- Lyapunov contour comparison
- finite-horizon convergence comparison
- robustness comparison ภายใต้ noise และ parameter variation

## Research questions

- KAN controller เลียนแบบ LQR ได้ดีกว่า standard neural network หรือไม่
- KAN controller ให้สัญญาณควบคุมที่เรียบกว่าไหม
- KAN controller ปรับปรุง Lyapunov derivative behavior ได้หรือไม่
- KAN controller ปรับปรุง finite-horizon convergence fraction ภายใต้ horizon, tolerance, bounds และ grid เดียวกันได้หรือไม่
- KAN controller ยังคง robust ภายใต้ noise, saturation และการเปลี่ยนพารามิเตอร์หรือไม่

## Important caution

การเปลี่ยนสถาปัตยกรรมโมเดลไม่ได้รับประกันเสถียรภาพโดยอัตโนมัติ

ผลของ KAN ยังคงต้องตรวจด้วย simulations, Lyapunov-style grid checks, robustness experiments และ finite-horizon convergence analysis โดย sampled checks เหล่านี้เพียงอย่างเดียวไม่สามารถยืนยัน mathematical attraction region ได้
