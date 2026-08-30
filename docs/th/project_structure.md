🌐 ภาษา: [English](../en/project_structure.md) | [日本語](../ja/project_structure.md) | [한국어](../ko/project_structure.md) | [ไทย](../th/project_structure.md)

# Project Structure

หน้านี้อธิบาย files และ folders หลักใน Lyapunov Neural-Network Control Lab

## Top-level files

### `main.py`
รัน main experiment pipeline ซึ่งรวม controller training, simulation, metrics, plots, robustness tests และ report generation

### `requirements.txt`
เป็น compatibility wrapper แบบบางสำหรับติดตั้ง development extra โดย `pyproject.toml` เป็น authoritative dependency source

### `README.md`
แนะนำภาพรวม project, quick-start commands, results และ documentation links

### `CITATION.cff`
ให้ citation metadata ของ project

### `LICENSE`
กำหนด license สำหรับการใช้งานและการเผยแพร่ project

## Source code

### `src/lyapunov_nn_control_lab/system.py`
กำหนด normalized second-order model coefficients, state-space matrices, LQR controller และ Lyapunov matrix

### `src/lyapunov_nn_control_lab/state_coordinates.py`
กำหนด normalized coordinate convention และ shared NumPy/Torch state-norm helpers

### `src/lyapunov_nn_control_lab/controllers.py`
กำหนด neural-network controller, dataset generation, stability-aware training และ actuator saturation utilities

### `src/lyapunov_nn_control_lab/simulation.py`
จำลอง closed-loop system trajectories

### `src/lyapunov_nn_control_lab/lyapunov.py`
คำนวณ Lyapunov values, Lyapunov derivatives และ grid-based stability checks

### `src/lyapunov_nn_control_lab/metrics.py`
คำนวณ normalized-state และ normalized-time performance metrics, LQR-style cost และ integrated squared control effort

### `src/lyapunov_nn_control_lab/plotting.py`
สร้าง plots สำหรับ simulations, robustness experiments, Lyapunov contours,
finite-horizon convergence maps และ model architecture

### `src/lyapunov_nn_control_lab/reporting.py`
สร้าง automatic experiment report

### `src/lyapunov_nn_control_lab/noise.py`
รัน paired measurement-noise robustness simulations ด้วย common random-number realizations และมี raw/aggregate result writers

### `src/lyapunov_nn_control_lab/experimental_seeds.py`
กำหนด explicit seed plans, การตั้งค่า RNG ส่วนกลางของ project, pairing checks และ sample-variability aggregation helpers

### `src/lyapunov_nn_control_lab/parameter_variation.py`
รัน robustness simulations ภายใต้ normalized model coefficients ที่เปลี่ยนไป

### `src/lyapunov_nn_control_lab/finite_horizon_convergence.py`
ประเมิน strict final-state tolerance บน bounded grid ที่ explicit finite horizon และคืน sampling metadata

### `src/lyapunov_nn_control_lab/region_of_attraction.py`
มีเฉพาะ deprecated legacy API wrapper สำหรับชื่อเดิมที่ทำให้เข้าใจผิด

### `src/lyapunov_nn_control_lab/stability_ablation.py`
รัน Cartesian product ของ stability weights และ shared repeat seeds แล้วแยก raw trials ออกจาก aggregate statistics

## Tests

### `tests/`
มี automated tests สำหรับ system model, controllers, simulations, metrics, plots, documentation-related outputs และ robustness utilities

## Examples

### `examples/quick_start.py`
ตัวอย่างขนาดเล็กที่เป็นมิตรกับผู้เริ่มต้นสำหรับรัน LQR simulation

## Results

### `results/`
เก็บ preserved legacy historical artifacts จำนวน 15 ไฟล์ และ `results/runs/<run_id>/` directories สำหรับ manifest-backed current runs แต่ละ current run มี report, data, figures, model state, inventory และ checksums ของตนเอง

### `src/lyapunov_nn_control_lab/result_provenance.py`
สร้าง run IDs ที่ปลอดภัย, เก็บ Git/environment/configuration provenance, เผยแพร่ผ่าน staging, ทำ inventory และ hash ให้ artifacts จริง และ verify completed runs

## Documentation

### `docs/`
มี guides สำหรับ methodology, reproducibility, figures, glossary terms, references และ project summary
