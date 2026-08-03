🌐 ภาษา: [English](../en/result_naming.md) | [日本語](../ja/result_naming.md) | [한국어](../ko/result_naming.md) | [ไทย](../th/result_naming.md)

# การตั้งชื่อไฟล์ผลลัพธ์

ใช้ตัวระบุภาษาอังกฤษตัวพิมพ์เล็กและขีดล่าง:

```text
YYYYMMDD_controller_experiment_setting.ext
```

ตัวอย่าง:

```text
20260804_nn_trajectory_seed7.png
20260804_comparison_roa_grid15.csv
20260804_nn_noise_sigma005.md
```

ใส่วันที่ ชนิดตัวควบคุม ประเภทการทดลอง และค่าตั้งที่ใช้แยกผลลัพธ์ หลีกเลี่ยงช่องว่างและชื่อที่กำกวมอย่าง `final.png`, `new_result.csv`, `really_final_plot.png`

คงชื่อไฟล์แบบตายตัวที่ `main.py` ใช้สำหรับผลอ้างอิงซึ่ง Git ติดตามอยู่ ส่วนการรันเพิ่มเติมให้ใช้รูปแบบชื่อแบบยาว และเชื่อมโยงผลสำคัญจากบันทึกการทดลอง
