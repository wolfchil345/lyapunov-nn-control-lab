🌐 ภาษา: [English](RELEASE_NOTES.md) | [日本語](RELEASE_NOTES.ja.md) | [한국어](RELEASE_NOTES.ko.md) | [ไทย](RELEASE_NOTES.th.md)

# v1.0.1 - ปรับแต่งเอกสารและการปล่อยรุ่น

แพตช์รีลีสนี้ปรับปรุงความน่าเชื่อถือในการติดตั้ง เอกสารหลายภาษา และรายงานสรุปผล โดยไม่เปลี่ยนแปลงการทดลองควบคุมหลัก

## ไฮไลต์

- เพิ่ม dependency รันไทม์ที่ขาดไปคือ `python-control`
- เพิ่มการ ignore ไฟล์ virtual environment และไฟล์ package metadata ที่ถูกสร้างขึ้น
- เพิ่มฐานเอกสารภาษาอังกฤษ ญี่ปุ่น เกาหลี และไทย
- เพิ่มดัชนีเอกสารที่แปลแล้วสำหรับทั้ง 4 ภาษา
- อัปเดต README แต่ละภาษาให้ลิงก์ไปยังดัชนีเอกสารของภาษานั้น
- ลบลิงก์เอกสารที่เลิกใช้หรือไม่มีอยู่จริง
- แก้สรุป ablation ให้ระบุ `lyapunov_violation_fraction`
- ทำให้ release checklist ใช้กับแท็กเวอร์ชันในอนาคตได้

## การตรวจสอบ

- ทดสอบผ่าน 57 รายการ
- ตัวอย่าง quick-start ผ่าน
- quality gate ผ่าน
- สร้างผลการทดลองซ้ำได้สำเร็จด้วย fixed random seeds
- รูปผลลัพธ์ที่สร้างใหม่ตรงกับรูปเดิมที่ติดตามไว้ในระดับพิกเซล
- การตรวจ Lyapunov บนกริดรายงานการละเมิดเป็นศูนย์
- การตรวจ finite-horizon แบบประวัติศาสตร์รายงานว่า controller และการตั้งค่าที่ทดสอบผ่านเกณฑ์ final-state tolerance ได้ 100% แต่ไม่ใช่ใบรับรองทางคณิตศาสตร์ของบริเวณดึงดูด

## ความเข้ากันได้

แกนของการจำลอง สถาปัตยกรรมคอนโทรลเลอร์ และผลการทดลองที่ติดตามไว้ ยังคงไม่เปลี่ยนจาก `v1.0.0`

---

# v1.0.0 - รีลีสสมบูรณ์ครั้งแรก

นี่คือรีลีสสมบูรณ์ครั้งแรกของ Lyapunov Neural-Network Control Lab

## ไฮไลต์

- คอนโทรลเลอร์ baseline แบบ LQR
- คอนโทรลเลอร์โครงข่ายประสาทเทียมที่ฝึกด้วย imitation learning
- การตรวจสอบเสถียรภาพที่ได้แรงบันดาลใจจาก Lyapunov
- stability-aware training penalty
- การทดลอง actuator saturation
- การทดลองความทนทานต่อ measurement noise
- การทดลองความทนทานต่อพารามิเตอร์
- การแสดงภาพ phase portrait
- การแสดงภาพ Lyapunov contours
- การทำแผนที่ sampled finite-horizon convergence (อธิบายด้วยศัพท์แบบเดิมในรีลีสต้นฉบับ)
- การเปรียบเทียบคอนโทรลเลอร์แบบ finite-horizon (อธิบายด้วยศัพท์แบบเดิมในรีลีสต้นฉบับ)
- การศึกษา stability-weight ablation
- การสร้างรายงานการทดลองอัตโนมัติ
- แผนภาพสถาปัตยกรรมโมเดล
- เอกสารระเบียบวิธี
- เอกสารสรุปโครงการ
- เมตาดาตาการอ้างอิง

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

## โฟกัสการวิจัย

โปรเจกต์นี้ศึกษาว่าคอนโทรลเลอร์โครงข่ายประสาทเทียมสามารถเลียนแบบตัวอ้างอิง LQR ได้หรือไม่ โดยประเมินด้วยตัวชี้วัดทรานเชียนต์ ความทนทาน และการวินิจฉัย Lyapunov แบบ sampled พืช nominal ที่ไม่มีการควบคุมมีเสถียรภาพแบบลู่เข้าอยู่แล้ว
