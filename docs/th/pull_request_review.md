🌐 ภาษา: [English](../en/pull_request_review.md) | [日本語](../ja/pull_request_review.md) | [한국어](../ko/pull_request_review.md) | [ไทย](../th/pull_request_review.md)

# การ Review Pull Request

## Review ทั่วไป

- [ ] Title และ summary อธิบายการเปลี่ยนแปลงที่มีจุดประสงค์เดียว
- [ ] Test และ required check ผ่าน
- [ ] อัปเดตเอกสารทั้งสี่ภาษาเมื่อ user-facing behavior เปลี่ยน
- [ ] Generated file ถูก include หรือ ignore โดยตั้งใจ
- [ ] แก้ conversation ก่อน merge

## Scientific review

- [ ] การเปลี่ยน seed, plant parameter, controller architecture, loss หรือ evaluation setting ชัดเจน
- [ ] อธิบาย diff ของตัวเลขและ figure
- [ ] ไม่เสนอ sampled check เป็น formal proof
- [ ] เก็บ failure case และ limitations

## Local commands

```bash
git diff --check
make checks
make quality-gate
```

Merge ผ่าน protected `main` branch เท่านั้นหลัง latest commit ผ่าน required check ทั้งหมด
