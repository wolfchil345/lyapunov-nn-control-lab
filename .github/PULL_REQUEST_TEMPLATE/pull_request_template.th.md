🌐 ภาษา: [English](../pull_request_template.md) | [日本語](pull_request_template.ja.md) | [한국어](pull_request_template.ko.md) | [ไทย](pull_request_template.th.md)

# Pull Request

## สรุป

อธิบายการเปลี่ยนแปลงที่มีขอบเขตชัดและเหตุผลที่ต้องทำ

## ประเภท

- [ ] Bug fix
- [ ] Experiment หรือ scientific change
- [ ] Documentation หรือ translation
- [ ] Test, tooling หรือ refactoring

## ผลกระทบทางวิทยาศาสตร์และไฟล์ที่สร้าง

- Seed, parameter, architecture, loss หรือ metric ที่เปลี่ยน:
- Plot, CSV, report หรือ model artifact ที่เปลี่ยน:
- ความต่างเชิงตัวเลขและ limitations ที่คาด:

## การตรวจสอบ

- [ ] `git diff --check`
- [ ] `make checks`
- [ ] `make quality-gate`
- [ ] อัปเดต viewer-facing documentation ทั้งสี่ภาษาเมื่อจำเป็น
- [ ] Review generated artifact และ include โดยตั้งใจ

## Follow-up

ระบุ work ที่ยังไม่เสร็จหรือเขียน `None`
