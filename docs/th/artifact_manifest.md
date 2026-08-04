🌐 ภาษา: [English](../en/artifact_manifest.md) | [日本語](../ja/artifact_manifest.md) | [한국어](../ko/artifact_manifest.md) | [ไทย](../th/artifact_manifest.md)

# รายการไฟล์และผลลัพธ์

## ซอร์สโค้ดและการตั้งค่า

- `main.py`: ควบคุมลำดับการทดลองทั้งหมด
- `src/`: พลวัต ตัวควบคุม การจำลอง การตรวจสอบอินพุต การทำซ้ำผล ตัวชี้วัด ความทนทาน การสร้างรายงาน และการวาดกราฟ
- `tests/`: การทดสอบพฤติกรรมแบบอัตโนมัติ
- `pyproject.toml`, `requirements.txt`, `requirements-dev.txt`: ข้อมูลแพ็กเกจ dependencies ขณะรัน และเครื่องมือพัฒนา

## สคริปต์สำหรับใช้งาน

- `scripts/run_checks.py`: ตรวจลิงก์เอกสาร รันชุดทดสอบ และตัวอย่างเริ่มต้น
- `scripts/quality_gate.py`: ตรวจความพร้อมขั้นสุดท้ายของรีโพซิทอรี
- `scripts/run_full_experiment.py`: ล้างผลเก่า รันการทดลอง และสรุปผลตามลำดับ
- `scripts/check_environment.py`, `scripts/check_package.py`, `scripts/project_status.py`, `scripts/list_results.py`: สคริปต์สำหรับวินิจฉัยสภาพแวดล้อม แพ็กเกจ และไฟล์

## หลักฐานที่สร้างขึ้น

- `results/*.png`: รูปอ้างอิง
- `results/performance_metrics.csv`: ตัวชี้วัดสมรรถนะของตัวควบคุม
- `results/stability_weight_ablation.csv`: ตัวชี้วัดจากการทดลองแบบตัดองค์ประกอบ
- `results/experiment_report*.md`: รายงานแต่ละภาษา
- `results/nn_controller.pt`: สถานะโมเดลที่สร้างขึ้น โดยตั้งใจไม่ให้ Git ติดตาม

ไฟล์ที่สร้างขึ้นเป็นหลักฐานจากการทดลอง ไม่ใช่ซอร์สโค้ด ควรเก็บค่าตั้งและตรวจความแตกต่างก่อนแทนที่ไฟล์อ้างอิงที่ Git ติดตามอยู่
