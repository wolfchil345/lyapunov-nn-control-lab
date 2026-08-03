🌐 ภาษา: [English](ROADMAP.md) | [日本語](ROADMAP.ja.md) | [한국어](ROADMAP.ko.md) | [ไทย](ROADMAP.th.md)

# แผนงาน

## ระยะใกล้

- ทำ neural training ซ้ำหลาย seed และรายงาน distribution หรือ confidence interval
- เพิ่ม CLI สำหรับเลือก experiment และแยก sweep ที่ใช้เวลามากเป็น command ตามหน้าที่
- บันทึก dependency version และ experiment configuration ใน report ที่สร้าง

## การควบคุมและความทนทาน

- เปรียบเทียบ PID, LQR, MPC, MLP และ KAN controller ภายใต้ setting ที่เข้ากันได้
- เพิ่ม nonlinear plant, external disturbance, delay, quantization และ uncertainty set ที่กว้างขึ้น
- ขยาย region-of-attraction analysis และเก็บ failure-case map

## การวิเคราะห์เสถียรภาพ

- ทดสอบ alternative และ learned Lyapunov function
- เพิ่ม adaptive sampling ใกล้ candidate violation
- เปรียบเทียบ empirical grid check กับ formal neural-network verification tool

## การตรวจสอบทางกายภาพ

- สร้าง hardware-in-the-loop stage ก่อนใช้กับอุปกรณ์จริง
- ระบุ actuator, sensor และ safety constraint ให้ชัด
- แยก safety-certified component จาก research prototype

## การสื่อสาร

- รักษา documentation สี่ภาษาให้ครบเมื่อ feature เปลี่ยน
- เพิ่ม poster และ technical article สั้นที่อ้างอิง reproducible result ชุดเดียวกัน

เป้าหมายระยะยาวคือ platform ขนาดเล็กสำหรับ experiment ด้าน learning-based control ที่น่าเชื่อถือ ไม่ใช่ข้ออ้างว่า neural controller หนึ่งตัวแก้ control safety ได้ทั่วไป
