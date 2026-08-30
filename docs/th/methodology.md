🌐 ภาษา: [English](../en/methodology.md) | [日本語](../ja/methodology.md) | [한국어](../ko/methodology.md) | [ไทย](../th/methodology.md)

# ระเบียบวิธี

เอกสารนี้อธิบายแนวคิดหลักทางวิศวกรรมควบคุมที่ใช้ใน Lyapunov neural-network control lab

## ข้อตกลงพิกัด

รีโพซิทอรีนี้ใช้แบบจำลองอันดับสองแบบ normalized และไร้มิติ โดยเวลา normalized คือ `tau`, พิกัดตำแหน่งแบบ normalized คือ `q`, ความเร็ว normalized คือ `v = dq/dtau`, อินพุตควบคุม normalized คือ `u`, และสถานะคือ `x = [q, v]` ดังนั้น `||x||_2 = sqrt(q^2 + v^2)` และ `||x||_2^2 = q^2 + v^2` จึงเป็นขนาดแบบ Euclidean ในพิกัดสถานะ normalized ไม่ใช่การผสมการวัดตำแหน่ง/ความเร็วแบบ SI

## 1. ระบบมวล-สปริง-แดมเปอร์

โครงการนี้ศึกษาระบบมวล-สปริง-แดมเปอร์อันดับสอง

```text
x = [q, v]
```

ระบบเขียนในรูป state-space ดังนี้

```text
dx/dtau = A x + B u
```

โดย x คือสถานะ, u คืออินพุตควบคุม, A อธิบายพลวัตของพืช, และ B อธิบายผลของอินพุตต่อพืช

สำหรับพารามิเตอร์ nominal, `A` มี eigenvalues เป็น `-0.2 + 1.4j` และ `-0.2 - 1.4j` ซึ่งมีส่วนจริงเป็นลบทั้งคู่ ดังนั้นพืชเชิงเส้น nominal แบบไม่ควบคุมจึง asymptotically stable อยู่แล้ว LQR เปลี่ยน transient response และ control trade-off; โครงการนี้ศึกษาการเลียนแบบ สมรรถนะ ความทนทาน และการคงพฤติกรรมที่เสถียร ไม่ใช่การทำให้ nominal plant ที่ open-loop ไม่เสถียรกลับมาเสถียร

## 2. ตัวควบคุมอ้างอิง LQR

ใช้ Linear Quadratic Regulator เป็น baseline ของการควบคุมเชิงเหมาะที่สุดแบบคลาสสิก

```text
u = -Kx
```

`Q` และ `R` เป็นน้ำหนักวัตถุประสงค์แบบไร้มิติ ค่าอินทิกรัลที่ได้เป็น quadratic LQR-style cost ไม่ใช่พลังงานทางกายภาพ LQR เป็นตัวอ้างอิงที่แข็งแรงให้ neural network เลียนแบบ

## 3. ตัวควบคุม neural network

ตัวควบคุม neural network รับ `q` และ `v` แบบ normalized เป็นอินพุต และส่งออกอินพุตควบคุม normalized แบบสเกลาร์หนึ่งค่า

```text
NN(x) ≈ LQR(x)
```

นี่คือ imitation learning: neural network เรียนรู้พฤติกรรมของ LQR controller บนสถานะที่สุ่มตัวอย่าง

## 4. การตรวจสอบเสถียรภาพแบบ Lyapunov

ฟังก์ชัน Lyapunov คือฟังก์ชันคล้ายพลังงานที่ใช้ให้เหตุผลเรื่องเสถียรภาพ

```text
V(x) = x^T P x
```

ตามพลวัตวงปิด อนุพันธ์คือ

```text
V-dot(x) = 2 x^T P (A x + B pi(x))
```

ตัวประเมินรายงานสองเงื่อนไขตัวอย่างที่ต่างกันอย่างชัดเจน

```text
basic decrease: V-dot(x) <= 0
decay margin:   V-dot(x) + alpha * ||x||_2^2 <= 0
```

เงื่อนไขที่สองเข้มกว่าเมื่อ `alpha > 0` จุดสมดุลที่แน่นอนถูกยกเว้นเพราะ `V(0) = V-dot(0) = 0`; ไม่ได้ซ่อนบริเวณรอบข้าง ค่าคลาดเคลื่อนเชิงตัวเลขเริ่มต้น `1e-9` ใช้จัดการ floating-point noise แยกจาก `alpha` ผลบนกริดครอบคลุมเฉพาะบริเวณตัวอย่างจำกัด และไม่ใช่ใบรับรองเสถียรภาพแบบต่อเนื่องอย่างเป็นทางการ

## 5. การฝึกที่คำนึงถึงเสถียรภาพ

neural network ถูกฝึกด้วยทั้ง imitation loss และ Lyapunov stability penalty

```text
total loss = imitation loss + stability penalty
```

ที่ `alpha = 0.05` การฝึกลดส่วนบวกของ decay residual เดียวกับที่ใช้ในการประเมิน

```text
decay residual = V-dot(x) + alpha * ||x||_2^2
stability penalty = mean(ReLU(decay residual))
```

## 6. การอิ่มตัวของแอคชูเอเตอร์

โครงการนี้ทดสอบขีดจำกัดของอินพุตควบคุม normalized ด้วย

```text
u = clip(u, -u_max, u_max)
```

สิ่งนี้แสดงผลของข้อจำกัดแอคชูเอเตอร์ต่อเสถียรภาพและสมรรถนะแบบวงปิด

## 7. การทดลองความทนทาน

โครงการทดสอบว่าตัวควบคุมที่เรียนรู้แล้วยังคงมีประสิทธิภาพภายใต้เงื่อนไขไม่สมบูรณ์หรือไม่

การทดลองความทนทานต่อสัญญาณรบกวนเพิ่ม noise ในการวัด

```text
x_measured = x + noise
```

ใช้ค่าเบี่ยงเบนมาตรฐาน Gaussian แบบสเกลาร์เดียวกันกับ `q` และ `v` ในพิกัด normalized อย่างเป็นอิสระ

ทุกระดับแอมพลิจูดที่ร้องขอจะประเมินด้วย seed list เดียวกันแบบทำซ้ำ สำหรับ seed หนึ่งค่า การจำลองจะสร้าง standardized Gaussian sequence หนึ่งชุด แล้วคูณสเกลด้วยแต่ละแอมพลิจูด (common random numbers) วิธีนี้ทำให้เปรียบเทียบแบบจับคู่ตาม seed ได้ โดยไม่อ้างว่าได้กำจัดความไม่แน่นอนเชิงสุ่มหรือความต่างแพลตฟอร์มทั้งหมดแล้ว

stability-weight ablation ใช้หลักจับคู่แบบเดียวกัน: ทุก weight ใช้ model-initialization seeds แบบ explicit ชุดเดียวกัน แถวผลทดลองราย seed ถูกเก็บแยกจากค่าเฉลี่ยรวม, sample standard deviations และ standard errors

การทดลองความทนทานต่อพารามิเตอร์เปลี่ยนค่าสัมประสิทธิ์มวล การหน่วง และความแข็งแบบ normalized เพื่อจำลอง modeling error

## 8. แผนภาพเฟสและคอนทัวร์ Lyapunov

แผนภาพเฟสพล็อตตำแหน่ง normalized เทียบกับความเร็ว normalized และแสดงว่า trajectory เคลื่อนเข้าหาจุดกำเนิดหรือไม่

กราฟคอนทัวร์ Lyapunov ซ้อน trajectory ลงบนเส้นระดับของฟังก์ชัน Lyapunov

กราฟเหล่านี้ช่วยอธิบายพฤติกรรมเสถียรภาพวงปิดเชิงภาพ

## 9. การวิเคราะห์การลู่เข้าในช่วงเวลาจำกัด

สำหรับสถานะตั้งต้นตัวอย่างทุกค่า `x0` การทดลองจำลอง `x(t; x0)` ในช่วง `0 <= t <= T` และใช้เกณฑ์ strict นี้โดยตรง

```text
||x(T)||_2 < epsilon
```

ตัวประเมินต้องการให้การจำลองสำเร็จถึง `T` พร้อมค่าเวลาและสถานะที่ finite ถ้าล้มเหลวหรือได้ค่าไม่ finite จะยกข้อผิดพลาดแทนการจัดเป็นไม่ลู่เข้าแบบเงียบๆ

`T` คือเวลา normalized และ `epsilon` คือ normalized-state Euclidean tolerance ผลลัพธ์บันทึก horizon `T`, tolerance `epsilon`, ขอบเขตและความละเอียดกริด, จำนวนที่ทดสอบ, จำนวนที่ลู่เข้า, และสัดส่วนการลู่เข้า นี่คือ sampled finite-horizon convergence map สถานะที่ลู่เข้าช้าอาจไม่ผ่านที่ `T` แม้จะลู่เข้าเมื่อ `t -> infinity` ดังนั้นการไม่ผ่านไม่ได้แปลว่าอยู่นอก mathematical attraction region

สำหรับจุดสมดุลที่กำเนิด true region of attraction นิยามเชิงแนวคิดว่า

```text
R = {x0 : x(t; x0) -> 0 as t -> infinity}.
```

การจำลองแบบเวลาจำกัดไม่สามารถยืนยันนิยามนี้ได้ การประเมินที่น่าเชื่อถืออาจต้องใช้ invariant Lyapunov sublevel sets ที่ยืนยันการลดลงแล้ว, วิธี sum-of-squares ที่ใช้ได้, การวิเคราะห์ reachability/invariance, formal verification, หรือผลวิเคราะห์สำหรับระบบเชิงเส้นที่เหมาะสม เซตที่พล็อต `{x : V(x) <= c}` ไม่ได้เป็น attraction region ที่รับรองโดยอัตโนมัติ

finite-horizon map และ sampled Lyapunov checks ที่แยกต่างหากตอบคำถามคนละแบบ และทั้งสองไม่ใช่ใบรับรอง continuous-state attraction region อย่างเป็นทางการ

## 10. Stability-weight ablation study

ablation study ฝึกตัวควบคุมด้วย Lyapunov penalty weights ที่ต่างกัน

รายงาน basic derivative violation fraction และ decay-margin violation fraction ที่เข้มกว่าแยกกัน พร้อม final normalized-state norm, normalized settling time, quadratic LQR-style cost, และ integrated squared control effort โดยรายการสุดท้ายคือ `integral u^2 dtau` ไม่ใช่พลังงานทางกายภาพ

## 11. สรุป

โครงการนี้ผสาน classical control, neural-network imitation learning, Lyapunov analysis, robustness testing และ sampled finite-horizon convergence analysis

คำถามวิจัยหลักคือ

```text
Can a neural-network controller imitate an LQR reference while preserving useful transient, robustness, and sampled Lyapunov behavior?
```
