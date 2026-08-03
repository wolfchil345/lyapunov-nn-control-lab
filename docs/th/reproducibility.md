🌐 ภาษา: [English](../en/reproducibility.md) | [日本語](../ja/reproducibility.md) | [한국어](../ko/reproducibility.md) | [ไทย](../th/reproducibility.md)

# การทำซ้ำผล

## ทำซ้ำชุดตรวจ

```bash
python -m pip install -e .
make checks
make quality-gate
```

## ทำซ้ำการทดลอง

Backup result ที่ติดตามแล้วรัน:

```bash
python scripts/run_full_experiment.py
```

Code ตั้ง seed ให้ Python, NumPy และ PyTorch ให้บันทึก commit, Python version, dependency version และ experiment setting กับทุก result

## ความต่างที่คาดได้

อาจมีความต่างเชิงตัวเลขหรือ PNG encoding เล็กน้อยระหว่าง system และ library version ให้เปรียบเทียบ numeric metric และตรวจ pixel content ของ figure ก่อนยอมรับการเปลี่ยนแปลง

## ขอบเขต

Reproducibility หมายถึง documented pipeline สร้างหลักฐานที่เทียบเท่าได้ ไม่ได้เปลี่ยน sampled Lyapunov หรือ region-of-attraction check ให้เป็นการพิสูจน์เสถียรภาพอย่างเป็นทางการ
