🌐 ภาษา: [English](../en/limitations.md) | [日本語](../ja/limitations.md) | [한국어](../ko/limitations.md) | [ไทย](../th/limitations.md)

# Limitations

หน้านี้อธิบายข้อจำกัดสำคัญของ Lyapunov Neural-Network Control Lab

## โครงการวิจัยเชิงการเรียนรู้

รีโพซิทอรีนี้ออกแบบมาเพื่อการเรียนรู้ การทดลอง และการสำรวจงานวิจัย

ไม่ควรถูกมองว่าเป็นระบบควบคุมที่ผ่านการรับรองความปลอดภัยครบถ้วน

## แบบจำลองทางกายภาพอย่างง่าย

พืชหลักคือระบบ mass-spring-damper

แม้จะมีประโยชน์ต่อการทดลองควบคุม แต่ยังง่ายกว่าระบบกลจริงจำนวนมากมาก

## ข้อจำกัดของพิกัด normalized

โมเดลนี้เป็นไร้มิติและไม่ได้กำหนดการแมปจาก `q`, `v`, `tau`, หรือ `u` ไปยังหน่วย SI ดังนั้นผลลัพธ์จึงรองรับการเปรียบเทียบการจำลองแบบ normalized แต่ไม่รองรับการอ้างโดยตรงเกี่ยวกับ metres, seconds, newtons หรือพลังงานฮาร์ดแวร์

## ข้อจำกัดของการตรวจเสถียรภาพแบบกริด

Lyapunov checks ถูกประเมินบน sampled grid points

การผ่าน grid check ไม่ได้พิสูจน์ global stability สำหรับทุกสถานะที่เป็นไปได้

มันให้เพียงหลักฐานเชิงประจักษ์ในบริเวณที่ตรวจเท่านั้น

## ข้อจำกัดของตัวควบคุม neural-network

ตัวควบคุม neural-network ฝึกจากข้อมูล และอาจทำงานไม่ดีนอก training distribution

การเลียนแบบ LQR ได้ดีไม่ได้รับประกันเสถียรภาพในทุกบริเวณโดยอัตโนมัติ

## ข้อจำกัดของการจำลองเชิงตัวเลข

ผลการจำลองอาจขึ้นกับ solver settings, การเลือก time step, package versions และ numerical tolerances

จึงอาจมีความแตกต่างเล็กน้อยระหว่างเครื่อง

## ข้อจำกัดของ finite-horizon convergence

convergence map ทดสอบเพียงว่าสถานะที่สุ่มตัวอย่างผ่านเกณฑ์เข้มงวด `||x(T)||_2 < epsilon` ที่หนึ่ง normalized-time horizon หรือไม่ tolerance นี้เป็น Euclidean normalized-state tolerance ผลลัพธ์ขึ้นกับ horizon, tolerance, grid bounds และ resolution การไม่ผ่านการทดสอบนี้ไม่ได้แปลว่าสถานะอยู่นอก mathematical region of attraction และการผ่านก็ไม่ได้รับรอง asymptotic convergence

sampled Lyapunov checks ที่แยกต่างหากก็ไม่ได้สร้าง formal continuous-state attraction-region certificate เช่นกัน Lyapunov sublevel set ไม่ได้รับการรับรองเพียงเพราะถูกพล็อต

## ข้อจำกัดของการทดลอง robustness

การทดลอง noise, saturation และ parameter variation ครอบคลุมเฉพาะกรณีที่เลือกไว้เท่านั้น

ไม่ได้ครอบคลุมทุกความไม่แน่นอนหรือการรบกวนที่เป็นไปได้

## ข้อจำกัดของฟังก์ชัน Lyapunov

โครงการนี้ใช้การวิเคราะห์ quadratic Lyapunov-style ที่อิงจากการตั้งค่าระบบ

ระบบไม่เชิงเส้นที่ซับซ้อนขึ้นอาจต้องใช้ learned, non-quadratic หรือ problem-specific Lyapunov functions

## ทิศทางการปรับปรุงในอนาคต

- เพิ่ม formal verification สำหรับตัวควบคุม neural-network
- ทดสอบระบบที่ใหญ่และไม่เชิงเส้นมากขึ้น
- เปรียบเทียบตัวควบคุมหลายประเภทมากขึ้น
- เรียนรู้ neural Lyapunov functions โดยตรง
- เพิ่มการวิเคราะห์ robustness และความไม่แน่นอนที่เข้มขึ้น
- ศึกษา safety constraints ที่เกินกว่าการอิ่มตัวของแอคชูเอเตอร์
