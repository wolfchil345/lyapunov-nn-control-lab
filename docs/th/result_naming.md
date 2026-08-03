🌐 ภาษา: [English](../en/result_naming.md) | [日本語](../ja/result_naming.md) | [한국어](../ko/result_naming.md) | [ไทย](../th/result_naming.md)

# การตั้งชื่อไฟล์ผลลัพธ์

ใช้ identifier ภาษาอังกฤษตัวเล็กและ underscore:

```text
YYYYMMDD_controller_experiment_setting.ext
```

ตัวอย่าง:

```text
20260804_nn_trajectory_seed7.png
20260804_comparison_roa_grid15.csv
20260804_nn_noise_sigma005.md
```

ใส่วันที่ controller, experiment type และ setting ที่ทำให้ผลแตกต่าง หลีกเลี่ยงช่องว่างและชื่ออย่าง `final.png`, `new_result.csv`, `really_final_plot.png`

รักษา filename แบบคงที่ที่ `main.py` ใช้สำหรับ reference artifact ที่ติดตาม ใช้ pattern แบบยาวกับ run เพิ่มเติมและ link ผลสำคัญจาก experiment log
