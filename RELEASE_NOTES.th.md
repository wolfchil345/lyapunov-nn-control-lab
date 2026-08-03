🌐 ภาษา: [English](RELEASE_NOTES.md) | [日本語](RELEASE_NOTES.ja.md) | [한국어](RELEASE_NOTES.ko.md) | [ไทย](RELEASE_NOTES.th.md)

# v1.0.1 - การปรับปรุงเอกสารและ Release

Patch release นี้ปรับ installation reliability, documentation หลายภาษา และ result-summary reporting โดยไม่เปลี่ยน core control experiment

## จุดเด่น

- เพิ่ม `python-control` runtime dependency ที่ขาด
- Ignore virtual-environment และ package-metadata file ที่สร้างขึ้น
- เพิ่ม documentation foundation ภาษาอังกฤษ ญี่ปุ่น เกาหลี และไทย
- เพิ่ม localized documentation index สำหรับสี่ภาษา
- Link README แต่ละภาษาไป localized documentation index
- ลบ obsolete และ nonexistent documentation link
- แก้ ablation summary ให้อ่าน `lyapunov_violation_fraction`
- ทำ release checklist ให้ใช้กับ version tag ในอนาคต

## การตรวจสอบ

- 57 test ผ่าน
- Quick-start example ผ่าน
- Quality gate ผ่าน
- สร้าง experiment result ใหม่สำเร็จด้วย fixed random seed
- Figure ที่สร้างใหม่ pixel-identical กับ tracked figure เดิม
- Lyapunov grid check มี zero violation
- Region-of-attraction check ของ test controller มี 100% convergence

## ความเข้ากันได้

Core simulation, controller architecture และ tracked experimental result ไม่เปลี่ยนจาก `v1.0.0`

---

# v1.0.0 - Release สมบูรณ์ครั้งแรก

นี่คือ complete release แรกของ Lyapunov Neural-Network Control Lab

## จุดเด่น

- LQR baseline, imitation-trained neural controller และ Lyapunov-inspired check
- Stability-aware penalty, saturation, noise และ parameter robustness
- Phase portrait, Lyapunov contour และ region-of-attraction analysis
- Stability-weight ablation, automatic report และ model architecture diagram
- Methodology, project summary และ citation metadata

## ผลลัพธ์หลัก

- `results/model_architecture.png`
- `results/position_comparison.png`
- `results/training_loss.png`
- `results/saturation_comparison.png`
- `results/noise_robustness.png`
- `results/parameter_robustness.png`
- `results/phase_portrait.png`
- `results/lyapunov_contours.png`
- `results/region_of_attraction.png`
- `results/region_of_attraction_comparison.png`
- `results/stability_weight_ablation.png`
- `results/experiment_report.md`

## จุดเน้นการวิจัย

ศึกษาว่า neural controller ที่เลียนแบบ stabilizing classical controller สามารถประเมินด้วย Lyapunov-based stability tool ได้หรือไม่
