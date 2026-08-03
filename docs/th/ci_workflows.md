🌐 ภาษา: [English](../en/ci_workflows.md) | [日本語](../ja/ci_workflows.md) | [한국어](../ko/ci_workflows.md) | [ไทย](../th/ci_workflows.md)

# CI Workflow

| Workflow | จุดประสงค์ |
|---|---|
| `tests.yml` | รัน Python test suite บน Python 3.12 |
| `local-checks.yml` | รัน `make checks` บน Python 3.11 |
| `quality-gate.yml` | รัน readiness gate เต็มบน `main` และ pull request |
| `codeql.yml` | วิเคราะห์ Python code เมื่อ push, pull request และทุกสัปดาห์ |

## ก่อน Push

```bash
make checks
make quality-gate
```

Required branch check ต้องใช้ job name ตรงกับที่ GitHub แสดง หาก workflow ล้มเหลว ให้ดู failing step แรกและทำซ้ำ command นั้นใน local

ตรวจ README badge ด้วย `python scripts/check_workflow_badges.py`
