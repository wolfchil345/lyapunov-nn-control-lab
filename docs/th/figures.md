🌐 ภาษา: [English](../en/figures.md) | [日本語](../ja/figures.md) | [한국어](../ko/figures.md) | [ไทย](../th/figures.md)

# คู่มือ Figures

คู่มือนี้อธิบาย figures ที่ถูกสร้างใน `results/` directory

figures ใหม่จะถูกเก็บไว้ใน `results/runs/<run_id>/` พร้อม `manifest.json` และ `SHA256SUMS` ที่ผ่านการตรวจสอบแล้ว ส่วนไฟล์ PNG ระดับ root จะถูกเก็บไว้เป็น legacy/unverified historical artifacts; ดูเพิ่มเติมที่ [`../../results/README.md`](../../results/README.md)

figures ในอนาคตจะใช้ labels แบบ normalized position, velocity, time, control และ state-norm แต่ไฟล์ PNG ที่ commit อยู่แล้วเป็น historical release artifacts และจะไม่ถูกสร้างใหม่โดยการเปลี่ยนแปลง coordinate-semantics จึงอาจยังเห็น labels แบบเก่าหรือคำว่า `Time [s]`

## Main comparison plots

### `position_comparison.png`
เปรียบเทียบการตอบสนองตำแหน่งของ LQR controller กับ neural-network controller

### `training_loss.png`
แสดง training loss ของ neural-network ตาม epochs

### `multiple_initial_conditions.png`
แสดงพฤติกรรมของ neural-network controller จาก initial states หลายชุด

## Stability and Lyapunov plots

### `phase_portrait.png`
แสดง trajectories ใน state space แบบ position-velocity

### `lyapunov_contours.png`
แสดงเส้นระดับของ Lyapunov function ร่วมกับ trajectories แบบวงปิด

### `finite_horizon_convergence.png`
แสดง sampled initial states ที่ผ่านเงื่อนไข `||x(T)||_2 < epsilon` ภายใต้ normalized-time horizon, normalized-state tolerance, bounds และ grid ที่ระบุไว้ และไม่ใช่การคำนวณ asymptotic attraction-region

### `finite_horizon_convergence_comparison.png`
เปรียบเทียบ finite-time final-state criterion เดียวกันข้าม controllers และรายงาน converged/tested counts กับ percentages

ไฟล์ tracked `region_of_attraction.png` และ `region_of_attraction_comparison.png` เป็น historical artifacts ที่สร้างก่อน terminology correction โดยไฟล์เหล่านี้จะคงเดิม และ runs ในอนาคตจะใช้สอง corrected filenames ด้านบน

## Robustness plots

### `saturation_comparison.png`
เปรียบเทียบพฤติกรรมตัวควบคุมเมื่อมีการจำกัด control input

### `noise_robustness.png`
เป็น historical single-seed figure ที่เก็บไว้โดยไม่เปลี่ยนแปลง ส่วน paired experiments ในอนาคตจะสร้าง `noise_robustness_paired.png` สำหรับ aggregate final-state statistics และ `noise_robustness_paired_trajectories.png` สำหรับ representative matched-seed trajectories

### `parameter_robustness.png`
แสดงพฤติกรรมตัวควบคุมเมื่อเปลี่ยน normalized model coefficients

## Architecture and ablation plots

### `model_architecture.png`
แสดง project workflow ตั้งแต่ plant model ไปจนถึง controller, simulation, stability checks และ reports

### `stability_weight_ablation.png`
เป็น historical figure ที่เก็บไว้โดยไม่เปลี่ยนแปลง ส่วน paired experiments ในอนาคตจะสร้าง `stability_weight_ablation_paired.png` ซึ่งแสดง faint per-seed observations, mean trends และ sample variability เมื่อมี repeats หลายครั้ง

## Data files

### `performance_metrics.csv`
เก็บตัวเลข performance metrics ของ controllers

### `stability_weight_ablation.csv`
เป็น historical results จาก seed design เดิมที่มี confounding โดย paired runs ในอนาคตจะสร้าง `stability_weight_ablation_trials_paired.csv` และ `stability_weight_ablation_summary_paired.csv` แยกกัน ส่วน noise trials และ summaries จะใช้ naming convention ตาม `noise_robustness_*_paired.csv`

### `experiment_report.md`
สรุป plots, metrics และ experiments ที่สร้างขึ้นโดยอัตโนมัติ
