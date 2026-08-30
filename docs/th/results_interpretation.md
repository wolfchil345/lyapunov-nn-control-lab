🌐 ภาษา: [English](../en/results_interpretation.md) | [日本語](../ja/results_interpretation.md) | [한국어](../ko/results_interpretation.md) | [ไทย](../th/results_interpretation.md)

# คู่มือ Results Interpretation

คู่มือนี้อธิบายวิธีตีความเอาต์พุตหลักของ Lyapunov Neural-Network Control Lab

## Controller comparison

โครงการนี้เปรียบเทียบตัวควบคุม LQR แบบคลาสสิกกับตัวควบคุม neural-network ที่ฝึกให้เลียนแบบ LQR พร้อมพิจารณาเสถียรภาพแบบ Lyapunov

โดยทั่วไป พฤติกรรมตัวควบคุมที่ดีหมายถึง:

- state เคลื่อนไปทางจุดกำเนิด
- final state norm มีค่าน้อยลง
- settling time สมเหตุสมผล
- control input ไม่ใหญ่เกินจำเป็น
- Lyapunov derivative เป็นค่าลบเป็นส่วนใหญ่ในบริเวณที่ตรวจสอบ

## Important metrics

ขนาด state ทั้งหมดด้านล่างใช้ `||x||_2 = sqrt(q^2 + v^2)` ในพิกัด normalized แบบไร้มิติ และ time กับ control input ก็เป็น normalized เช่นกัน

### `final_state_norm`
วัดระยะ Euclidean ของ normalized-state จากสมดุลเป้าหมาย ค่ายิ่งเล็กยิ่งดี

### `settling_time`
metric แบบ canonical คือ `settling_time`: เวลา normalized ที่สุ่มตัวอย่างได้ครั้งแรกหลังจากตัวอย่างสุดท้ายที่อยู่นอก `||x||_2 <= 0.02` ดังนั้นตัวอย่างที่เหลือทั้งหมดจะอยู่ใน closed tolerance set ส่วน `settling_time_s` เป็น historical compatibility alias และไม่ได้หมายถึงวินาที

### `quadratic_cost`
อินทิเกรต `x^T Q x + u^T R u` ตาม normalized time โดย `Q` และ `R` เป็น dimensionless objective weights จึงไม่ใช่พลังงานทางกายภาพ

### `integrated_squared_control_effort`
อินทิเกรต `u^2` ตาม normalized time ค่าน้อยลงหมายถึงตัวควบคุมก้าวร้าวน้อยลง แต่ค่านี้ไม่ใช่พลังงานทางกายภาพ `control_energy` ถูกคงไว้เป็น historical compatibility alias

### `max_abs_control`
แสดงค่าสัมบูรณ์สูงสุดของ normalized control input ซึ่งมีประโยชน์ต่อการตรวจสอบ saturation

## Sampled Lyapunov checks

โครงการนี้ใช้ฟังก์ชันกำลังสองและอนุพันธ์แบบวงปิดดังนี้:

```text
V(x) = x^T P x
V-dot(x) = 2 x^T P (A x + B pi(x))
```

สอง metrics นี้ตอบคำถามคนละแบบ:

- `derivative_violation_fraction` นับ sampled nonzero states ที่ `V-dot` เกิน numerical tolerance
- `decay_margin_violation_fraction` นับ sampled nonzero states ที่ `V-dot + alpha * ||x||_2^2` เกิน numerical tolerance

เงื่อนไขที่สองเข้มกว่าเมื่อ `alpha > 0` โดยการฝึกและการประเมินใช้ค่าเริ่มต้นเดียวกันคือ `alpha = 0.05` และ numerical tolerance เริ่มต้นคือ `1e-9` ซึ่งใช้จัดการ floating-point noise เท่านั้น ไม่ใช่ส่วนหนึ่งของ scientific decay margin

จุดกำเนิดที่แน่นอนถูกตัดออกเพราะ `V(0) = V-dot(0) = 0` ส่วน grid point อื่นทั้งหมดถูกรวมไว้ ทั้งสอง fractions อธิบายเฉพาะ finite sampled grid และไม่ใช่ใบรับรองเชิงทางการบน continuous state space

## Finite-horizon convergence map

สำหรับ initial state แต่ละจุดบน finite grid ตัวประเมินจะจำลองถึง horizon `T` ที่ระบุ และจัดประเภทสถานะก็ต่อเมื่อ strict final-state criterion `||x(T)||_2 < epsilon` เป็นจริง โดย `T` คือ normalized-time horizon และ `epsilon` คือ normalized-state Euclidean tolerance ดังนั้นเปอร์เซ็นต์ที่รายงานต้องตีความร่วมกับ `T`, `epsilon`, state bounds, grid resolution และ tested/converged counts

เปอร์เซ็นต์ที่มากขึ้นหมายถึง sampled states จำนวนมากขึ้นผ่านเกณฑ์ finite-time เฉพาะนั้น แต่ไม่ได้ยืนยัน asymptotic convergence, stable region หรือ mathematical attraction basin สถานะที่ลู่เข้าช้าอาจไม่ผ่านที่ `T` แม้จะลู่เข้าในภายหลัง

map นี้ยังแตกต่างจาก sampled Lyapunov checks ข้างต้น และทั้งสองการทดสอบไม่ใช่ formal continuous-state attraction-region certificate

## Robustness experiments

### Measurement noise
noise robustness ใช้ scalar Gaussian standard deviation เดียวกันอย่างอิสระกับ normalized measurements ของ `q` และ `v`

future runs จะจับคู่ทุก noise amplitude ตาม seed ด้วย common random numbers สำหรับ seed เดียว จะใช้ standardized Gaussian sequence เดียวกันแล้วสเกลด้วยแต่ละ amplitude ควรตีความแถว raw `noise_std x seed` ก่อน aggregate mean, sample standard deviation และ standard error การจับคู่นี้ช่วยลดแหล่ง confounding จาก random-realization หนึ่งส่วน แต่ไม่กำจัดความไม่แน่นอนทั้งหมด

### Parameter variation
parameter robustness ตรวจว่าตัวควบคุมยังทำงานได้เมื่อ normalized mass, damping หรือ stiffness coefficients เปลี่ยนไป

### Actuator saturation
saturation experiments ตรวจว่าตัวควบคุมยังมีประสิทธิภาพเมื่อ normalized control input ถูกจำกัด

## Ablation study

stability-weight ablation เปลี่ยนตัวคูณ Lyapunov penalty ระหว่างการฝึก โดยยังคงรายงาน decay margin อย่างชัดเจน

future runs ใช้ repeated seed set เดียวกันสำหรับทุก weight โดย raw table มีหนึ่งแถวต่อ `stability_weight x seed` และ aggregate table รายงาน `n`, mean, sample standard deviation และ standard error ตาม weight ค่า mean บวกลบ sample standard deviation เป็นเพียง variability summary ไม่ใช่ confidence interval

stability weight ที่ดีควรสมดุลทั้ง imitation accuracy, convergence และ sampled Lyapunov metrics ทั้งสองชนิด ไฟล์ที่ commit แล้ว `results/stability_weight_ablation.csv` ใช้ historical ambiguous violation column และตั้งใจไม่เขียนทับที่นี่ schema ที่สร้างใหม่ก็จะไม่ถูก relabel ย้อนหลัง ส่วน paired files ใหม่จะใช้ชื่อที่แก้แล้วของ sampled derivative และ sampled decay-margin violation

## Practical reading order

1. ตรวจ `performance_metrics.csv`
2. เปิด `position_comparison.png`
3. เปิด `phase_portrait.png`
4. เปิด `lyapunov_contours.png`
5. หลัง run ใหม่ เปิด `finite_horizon_convergence_comparison.png` โดยไฟล์ tracked `region_of_attraction_comparison.png` เป็น historical pre-migration artifact
6. อ่าน `experiment_report.md`
