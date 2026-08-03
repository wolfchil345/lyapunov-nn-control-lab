🌐 ภาษา: [English](../en/result_review_checklist.md) | [日本語](../ja/result_review_checklist.md) | [한국어](../ko/result_review_checklist.md) | [ไทย](../th/result_review_checklist.md)

# Checklist ตรวจผลลัพธ์

## การตั้งค่า

- [ ] บันทึก branch, commit, seed, epochs และ model architecture
- [ ] บันทึก initial condition, duration, grid density, noise และ parameter case
- [ ] Run ที่เปรียบเทียบต่างกันเฉพาะตัวแปรที่ตั้งใจ

## ผลลัพธ์

- [ ] มี CSV, report, model และ figure ที่คาดหวัง
- [ ] Figure มี label อ่านได้และ trajectory สมเหตุผล
- [ ] Metric เป็นค่าจำกัดและตีความร่วมกัน
- [ ] Saturation, noise และ parameter case มี label ชัดเจน

## การอ้างเรื่องเสถียรภาพ

- [ ] อธิบาย sampled Lyapunov check ว่าเป็นหลักฐานเชิงประจักษ์
- [ ] การกล่าวถึง region of attraction ระบุ test grid, horizon และ threshold
- [ ] เก็บและอธิบาย failure case กับพฤติกรรมที่ไม่คาดหมาย

## ก่อน Commit

- [ ] `make quality-gate` ผ่าน
- [ ] `git diff` มีเฉพาะ artifact ที่ตั้งใจ
- [ ] Documentation และ experiment log ตรงกับผลที่สร้าง
