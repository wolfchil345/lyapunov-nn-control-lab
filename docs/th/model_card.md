🌐 ภาษา: [English](../en/model_card.md) | [日本語](../ja/model_card.md) | [한국어](../ko/model_card.md) | [ไทย](../th/model_card.md)

# Model Card

model card นี้สรุป neural-network controller ที่ใช้ใน Lyapunov Neural-Network Control Lab

## Model purpose

neural-network controller ทำหน้าที่แมป system state ไปเป็น scalar control input

โมเดลนี้ถูกฝึกให้เลียนแบบ LQR controller พร้อมใช้ stability-aware training penalty

## System state

model input เป็น state สองมิติ:

- normalized position `q`
- normalized velocity `v = dq/dtau`

## Model output

model output เป็น scalar control input หนึ่งค่า:

- normalized scalar control input `u` ที่ป้อนให้กับ model

## Training target

training target ถูกสร้างจาก LQR controller

neural network เรียนรู้เพื่อประมาณ LQR state-to-control mapping

## Stability-aware training

training process สามารถรวม Lyapunov-style penalty ได้

สิ่งนี้ช่วยส่งเสริมพฤติกรรมที่ลด Lyapunov function รอบ sampled states

## Intended use

controller นี้มีไว้สำหรับ simulation-based control experiments, การศึกษา และการสำรวจเชิงวิจัย

เหมาะสำหรับการศึกษาด้าน neural-network control, Lyapunov-style checks, robustness tests และ controller comparison

## Out-of-scope use

model นี้ไม่ควรถูกใช้เป็น safety-certified real-world controller

ยังไม่ได้รับการยืนยันสำหรับ hardware deployment, systems ที่อันตราย หรือ safety-critical environments

## Evaluation methods

controller ถูกประเมินด้วย:

- closed-loop simulation
- final normalized-state norm
- normalized settling time
- quadratic LQR-style cost
- integrated squared normalized control effort
- maximum absolute normalized control input
- Lyapunov derivative grid checks
- robustness experiments
- finite-horizon final-state tolerance mapping

## Known limitations

- plant model มีความเรียบง่าย
- controller อาจไม่ generalize นอก training region
- grid-based Lyapunov checks ไม่ได้พิสูจน์ global stability
- simulation results อาจต่างกันเล็กน้อยตาม environment
- robustness tests ครอบคลุมเฉพาะบางกรณีที่เลือกไว้

## Recommended reporting

เมื่อรายงานผล ควรระบุ:

- training settings
- random seed
- system parameters
- controller type
- evaluation metrics
- Lyapunov check results
- robustness settings
- finite-horizon convergence settings: horizon, tolerance, bounds, grid,
  tested count, and converged count

## Future improvements

- เพิ่ม controller architectures ให้มากขึ้น
- เปรียบเทียบกับ KAN-based controllers
- เพิ่ม formal verification ที่เข้มแข็งขึ้น
- เรียนรู้ neural Lyapunov functions โดยตรง
- ทดสอบ nonlinear systems เพิ่มเติม
