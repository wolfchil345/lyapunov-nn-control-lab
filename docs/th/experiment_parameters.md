🌐 ภาษา: [English](../en/experiment_parameters.md) | [日本語](../ja/experiment_parameters.md) | [한국어](../ko/experiment_parameters.md) | [ไทย](../th/experiment_parameters.md)

# คู่มือ Experiment Parameters

คู่มือนี้อธิบายพารามิเตอร์หลักที่มีผลต่อพฤติกรรมและผลลัพธ์ของการทดลอง

## ทำไมพารามิเตอร์จึงสำคัญ

การทดลองควบคุมด้วย neural network อาจเปลี่ยนผลได้เมื่อปรับการตั้งค่าการฝึก, random seeds, ช่วงกริด, ค่าคงที่ของระบบ หรือการตั้งค่าความทนทาน ควรบันทึกการเปลี่ยนแปลงพารามิเตอร์สำคัญก่อนเปรียบเทียบผล

## กลุ่มพารามิเตอร์หลัก

## ข้อตกลงพิกัด

การทดลองนี้เป็น normalized และไร้มิติ: `tau` คือ normalized time, `x = [q, v]` คือ normalized position/velocity, และ `u` คือ normalized control input ดังนั้น threshold และระดับ noise จึงใช้ normalized coordinates

## 1. System parameters

พารามิเตอร์กลุ่มนี้กำหนดแบบจำลองอันดับสองแบบ normalized รวมทั้ง normalized mass, damping, stiffness coefficients และ state-space matrices ค่าสัมประสิทธิ์เชิงตัวเลขไม่ใช่ปริมาณ SI เช่น kilograms หรือ newtons per metre

ไฟล์สำคัญ:

- `src/system.py`
- `src/parameter_variation.py`

## 2. Controller parameters

พารามิเตอร์กลุ่มนี้มีผลต่อ LQR reference controller, neural network controller, พฤติกรรม saturation และ learned control output

ไฟล์สำคัญ:

- `src/system.py`
- `src/controllers.py`
- `main.py`

## 3. Training parameters

พารามิเตอร์กลุ่มนี้มีผลต่อการเรียนรู้ของ neural network

ตัวอย่าง:

- Random seed
- Number of epochs
- Learning rate
- Dataset size
- Loss weights
- Network hidden size

ไฟล์สำคัญ:

- `src/controllers.py`
- `main.py`

## 4. Simulation parameters

พารามิเตอร์กลุ่มนี้มีผลต่อการประเมินวงปิด

ตัวอย่าง:

- Initial condition
- Normalized simulation time
- Normalized time step
- Controller saturation limit

ไฟล์สำคัญ:

- `src/simulation.py`
- `main.py`

## 5. Lyapunov grid parameters

พารามิเตอร์กลุ่มนี้มีผลต่อ sampled Lyapunov-style checks

ตัวอย่าง:

- State range
- Grid density
- Controller used during grid evaluation

ไฟล์สำคัญ:

- `src/lyapunov.py`
- `main.py`

## 6. Robustness parameters

พารามิเตอร์กลุ่มนี้มีผลต่อการทดลอง noise และ model variation

ตัวอย่าง:

- Scalar noise standard deviation ที่ใช้แยกอิสระกับทั้งสองพิกัด normalized state
- Parameter variation range
- Number of tested cases

ไฟล์สำคัญ:

- `src/noise.py`
- `src/parameter_variation.py`
- `src/stability_ablation.py`

## กฎการเปรียบเทียบอย่างปลอดภัย

เมื่อเปรียบเทียบผลการทดลองสองชุด ควรเปลี่ยนทีละหนึ่งกลุ่มพารามิเตอร์เท่านั้นเมื่อทำได้

stability-weight ablation ปฏิบัติต่อ random seed เป็น repeated nuisance factor: ทุก weight จะฝึกด้วย explicit seed list เดียวกัน โดย workflow งานวิจัยค่าเริ่มต้นใช้สาม seed ที่เรียงต่อกัน และผู้เรียกสามารถส่ง `ExperimentSeedPlan` แบบ explicit หรือกำหนด base seed กับ repeat count ได้

measurement-noise experiment ก็ใช้ seed list เดียวกันสำหรับทุก noise amplitude เช่นกัน สำหรับ seed หนึ่งค่า ระบบจะสร้าง standardized Gaussian sequence หนึ่งชุด แล้วคูณด้วยแต่ละ standard deviation การออกแบบแบบ common-random-number นี้ทำให้เปรียบเทียบแบบจับคู่ตาม seed ได้ โดยไม่อ้างว่ากำจัดความไม่แน่นอนเชิงสุ่มทั้งหมดแล้ว

## ก่อนบันทึกผลลัพธ์สุดท้าย

รัน:

```bash
python scripts/check_environment.py
make checks
python main.py
python scripts/summarize_results.py
```

จากนั้นบันทึกว่ามีพารามิเตอร์ใดถูกเปลี่ยนและเปลี่ยนเพราะอะไร
