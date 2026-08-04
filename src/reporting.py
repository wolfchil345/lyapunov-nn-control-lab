"""Generate localized Markdown summaries for experiment artifacts."""

import csv
from pathlib import Path

REPORT_FILENAMES = {
    "en": "experiment_report.md",
    "ja": "experiment_report.ja.md",
    "ko": "experiment_report.ko.md",
    "th": "experiment_report.th.md",
}

REPORT_COPY = {
    "en": {
        "switcher": "🌐 Language",
        "title": "Experiment Report",
        "intro": "This report summarizes the generated results for the Lyapunov neural-network control lab.",
        "main": "Main experiments",
        "experiment": "Experiment",
        "output": "Output",
        "available": "Available plots",
        "no_plots": "No plot files were found.",
        "no_data": "No data available.",
        "performance": "Performance metrics preview",
        "ablation": "Stability-weight ablation preview",
        "interpretation": "Interpretation guide",
        "performance_labels": [
            "Controller",
            "Initial position",
            "Initial velocity",
            "Final state norm",
            "Settling time [s]",
            "Quadratic cost",
            "Control energy",
            "Maximum control magnitude",
        ],
        "ablation_labels": [
            "Stability weight",
            "Lyapunov violation fraction",
            "Final state norm",
            "Settling time [s]",
            "Quadratic cost",
            "Control energy",
        ],
        "controller_names": {},
        "experiments": [
            "Model architecture",
            "LQR and neural-network comparison",
            "Stability-aware training loss",
            "Multiple initial conditions",
            "Actuator saturation comparison",
            "Measurement-noise robustness",
            "Parameter robustness",
            "Phase portrait",
            "Lyapunov contour plot",
            "Region of attraction map",
            "Region of attraction controller comparison",
            "Stability-weight ablation study",
        ],
        "guidance": [
            "Lower final state norm means the controller drives the state closer to the equilibrium.",
            "Lower settling time means the controller stabilizes faster.",
            "Lower control energy means the controller uses less actuation effort.",
            "Lower Lyapunov violation fraction means fewer sampled states violate the Lyapunov decrease condition.",
            "Region of attraction results estimate which sampled initial states converge under the selected settings.",
            "These sampled results are empirical evidence, not a formal stability proof.",
        ],
    },
    "ja": {
        "switcher": "🌐 言語",
        "title": "実験レポート",
        "intro": "このレポートはLyapunov NN Control Labで生成された実験結果を要約します。",
        "main": "主な実験",
        "experiment": "実験",
        "output": "出力",
        "available": "利用可能な図",
        "no_plots": "図ファイルが見つかりません。",
        "no_data": "利用可能なデータがありません。",
        "performance": "性能指標（抜粋）",
        "ablation": "安定性重みのアブレーション結果（抜粋）",
        "interpretation": "解釈ガイド",
        "performance_labels": [
            "制御器",
            "初期位置",
            "初期速度",
            "最終状態ノルム",
            "整定時間 [s]",
            "二次コスト",
            "制御エネルギー",
            "最大制御入力",
        ],
        "ablation_labels": [
            "安定性重み",
            "Lyapunov違反率",
            "最終状態ノルム",
            "整定時間 [s]",
            "二次コスト",
            "制御エネルギー",
        ],
        "controller_names": {
            "Neural network": "ニューラルネットワーク",
            "Saturated neural network": "飽和ニューラルネットワーク",
        },
        "experiments": [
            "モデル構成",
            "LQRとニューラルネットワークの比較",
            "安定性を意識した学習損失",
            "複数の初期条件",
            "アクチュエータ飽和の比較",
            "観測ノイズに対するロバスト性",
            "パラメータ変動に対するロバスト性",
            "位相図",
            "Lyapunov等高線図",
            "引き込み領域マップ",
            "制御器別の引き込み領域比較",
            "安定性重みのアブレーション試験",
        ],
        "guidance": [
            "`final_state_norm`が小さいほど、制御器は状態を平衡点へ近づけています。",
            "`settling_time_s`が短いほど、制御器は速く安定化しています。",
            "`control_energy`が小さいほど、必要な制御入力は少なくなります。",
            "`lyapunov_violation_fraction`が小さいほど、サンプル状態でLyapunov減少条件に違反する点が少なくなります。",
            "引き込み領域の結果は、選択した設定で収束するサンプル初期状態を推定したものです。",
            "これらの結果は経験的証拠であり、形式的な安定性証明ではありません。",
        ],
    },
    "ko": {
        "switcher": "🌐 언어",
        "title": "실험 보고서",
        "intro": "이 보고서는 Lyapunov NN Control Lab에서 생성된 실험 결과를 요약합니다.",
        "main": "주요 실험",
        "experiment": "실험",
        "output": "출력",
        "available": "사용 가능한 그림",
        "no_plots": "그림 파일을 찾지 못했습니다.",
        "no_data": "사용 가능한 데이터가 없습니다.",
        "performance": "성능 지표 미리보기",
        "ablation": "안정성 가중치 제거 실험 미리보기",
        "interpretation": "해석 가이드",
        "performance_labels": [
            "제어기",
            "초기 위치",
            "초기 속도",
            "최종 상태 노름",
            "정착 시간 [s]",
            "이차 비용",
            "제어 에너지",
            "최대 제어 입력",
        ],
        "ablation_labels": [
            "안정성 가중치",
            "Lyapunov 위반 비율",
            "최종 상태 노름",
            "정착 시간 [s]",
            "이차 비용",
            "제어 에너지",
        ],
        "controller_names": {
            "Neural network": "신경망",
            "Saturated neural network": "포화 신경망",
        },
        "experiments": [
            "모델 구조",
            "LQR과 신경망 비교",
            "안정성 중심 학습 손실",
            "여러 초기 조건",
            "구동기 포화 비교",
            "측정 잡음 강건성",
            "매개변수 변화 강건성",
            "위상도",
            "Lyapunov 등고선 그림",
            "흡인 영역 지도",
            "제어기별 흡인 영역 비교",
            "안정성 가중치 제거 실험",
        ],
        "guidance": [
            "`final_state_norm`이 작을수록 제어기가 상태를 평형점에 더 가깝게 만듭니다.",
            "`settling_time_s`가 짧을수록 제어기가 더 빠르게 안정화합니다.",
            "`control_energy`가 작을수록 필요한 제어 입력이 적습니다.",
            "`lyapunov_violation_fraction`이 작을수록 표본 상태에서 Lyapunov 감소 조건을 위반하는 점이 적습니다.",
            "흡인 영역 결과는 선택한 설정에서 수렴하는 표본 초기 상태를 추정한 것입니다.",
            "이 결과는 경험적 근거이며 형식적인 안정성 증명이 아닙니다.",
        ],
    },
    "th": {
        "switcher": "🌐 ภาษา",
        "title": "รายงานการทดลอง",
        "intro": "รายงานนี้สรุปผลการทดลองที่สร้างจาก Lyapunov NN Control Lab",
        "main": "การทดลองหลัก",
        "experiment": "การทดลอง",
        "output": "ผลลัพธ์",
        "available": "รูปที่พร้อมใช้งาน",
        "no_plots": "ไม่พบไฟล์รูป",
        "no_data": "ไม่มีข้อมูลที่พร้อมใช้งาน",
        "performance": "ตัวอย่างตัวชี้วัดประสิทธิภาพ",
        "ablation": "ตัวอย่างผลการตัดองค์ประกอบน้ำหนักเสถียรภาพ",
        "interpretation": "คู่มือการตีความ",
        "performance_labels": [
            "ตัวควบคุม",
            "ตำแหน่งเริ่มต้น",
            "ความเร็วเริ่มต้น",
            "นอร์มสถานะสุดท้าย",
            "เวลาตั้งตัว [s]",
            "ต้นทุนกำลังสอง",
            "พลังงานควบคุม",
            "ขนาดอินพุตควบคุมสูงสุด",
        ],
        "ablation_labels": [
            "น้ำหนักเสถียรภาพ",
            "สัดส่วนการละเมิด Lyapunov",
            "นอร์มสถานะสุดท้าย",
            "เวลาตั้งตัว [s]",
            "ต้นทุนกำลังสอง",
            "พลังงานควบคุม",
        ],
        "controller_names": {
            "Neural network": "โครงข่ายประสาท",
            "Saturated neural network": "โครงข่ายประสาทแบบอิ่มตัว",
        },
        "experiments": [
            "สถาปัตยกรรมแบบจำลอง",
            "การเปรียบเทียบ LQR และโครงข่ายประสาท",
            "ค่าความสูญเสียในการฝึกที่คำนึงถึงเสถียรภาพ",
            "หลายเงื่อนไขเริ่มต้น",
            "การเปรียบเทียบการอิ่มตัวของตัวกระตุ้น",
            "ความทนทานต่อสัญญาณรบกวนการวัด",
            "ความทนทานต่อการเปลี่ยนพารามิเตอร์",
            "แผนภาพเฟส",
            "กราฟเส้นชั้น Lyapunov",
            "แผนที่บริเวณดึงดูด",
            "การเปรียบเทียบบริเวณดึงดูดของตัวควบคุม",
            "การศึกษาการตัดองค์ประกอบน้ำหนักเสถียรภาพ",
        ],
        "guidance": [
            "ค่า `final_state_norm` ที่ต่ำหมายถึงตัวควบคุมพาสถานะเข้าใกล้จุดสมดุลมากขึ้น",
            "ค่า `settling_time_s` ที่ต่ำหมายถึงตัวควบคุมทำให้ระบบเสถียรเร็วขึ้น",
            "ค่า `control_energy` ที่ต่ำหมายถึงใช้แรงควบคุมน้อยลง",
            "ค่า `lyapunov_violation_fraction` ที่ต่ำหมายถึงจุดตัวอย่างละเมิดเงื่อนไขการลดลงของ Lyapunov น้อยลง",
            "ผลบริเวณดึงดูดเป็นการประมาณสถานะเริ่มต้นตัวอย่างที่ลู่เข้าภายใต้การตั้งค่าที่เลือก",
            "ผลเหล่านี้เป็นหลักฐานเชิงประจักษ์ ไม่ใช่การพิสูจน์เสถียรภาพอย่างเป็นทางการ",
        ],
    },
}

PLOT_FILES = [
    "model_architecture.png",
    "position_comparison.png",
    "training_loss.png",
    "multiple_initial_conditions.png",
    "saturation_comparison.png",
    "noise_robustness.png",
    "parameter_robustness.png",
    "phase_portrait.png",
    "lyapunov_contours.png",
    "region_of_attraction.png",
    "region_of_attraction_comparison.png",
    "stability_weight_ablation.png",
]


def read_csv_rows(
    csv_path: Path,
    max_rows: int = 8,
) -> list[dict[str, str]]:
    """Read a small number of rows from a CSV file."""

    if not csv_path.exists():
        return []

    with csv_path.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        return list(reader)[:max_rows]


def format_markdown_table(
    rows: list[dict[str, str]],
    columns: list[str],
    labels: list[str] | None = None,
    value_maps: dict[str, dict[str, str]] | None = None,
    no_data: str = "No data available.",
) -> list[str]:
    """Format selected CSV columns as a Markdown table."""

    if not rows:
        return [no_data]

    labels = labels or columns
    value_maps = value_maps or {}
    if len(labels) != len(columns):
        raise ValueError("Table labels must match the number of columns")

    lines = [
        "| " + " | ".join(labels) + " |",
        "| " + " | ".join(["---"] * len(columns)) + " |",
    ]

    for row in rows:
        values = [
            value_maps.get(column, {}).get(row.get(column, ""), row.get(column, ""))
            for column in columns
        ]
        lines.append("| " + " | ".join(values) + " |")

    return lines


def language_switcher(label: str) -> str:
    """Return links to every localized experiment report."""

    return (
        f"{label}: [English]({REPORT_FILENAMES['en']}) | "
        f"[日本語]({REPORT_FILENAMES['ja']}) | "
        f"[한국어]({REPORT_FILENAMES['ko']}) | "
        f"[ไทย]({REPORT_FILENAMES['th']})"
    )


def generate_experiment_report(
    results_dir: Path,
    output_path: Path,
    language: str = "en",
) -> None:
    """Generate one localized Markdown experiment report."""

    if language not in REPORT_COPY:
        raise ValueError(f"Unsupported report language: {language}")

    copy = REPORT_COPY[language]
    performance_rows = read_csv_rows(results_dir / "performance_metrics.csv")
    ablation_rows = read_csv_rows(results_dir / "stability_weight_ablation.csv")
    available_plots = [name for name in PLOT_FILES if (results_dir / name).exists()]

    lines = [
        language_switcher(copy["switcher"]),
        "",
        f"# {copy['title']}",
        "",
        copy["intro"],
        "",
        f"## {copy['main']}",
        "",
        f"| {copy['experiment']} | {copy['output']} |",
        "|---|---|",
    ]

    for experiment, plot_file in zip(copy["experiments"], PLOT_FILES, strict=True):
        lines.append(f"| {experiment} | `{plot_file}` |")

    lines.extend(["", f"## {copy['available']}", ""])
    if available_plots:
        lines.extend(f"- [`{name}`]({name})" for name in available_plots)
    else:
        lines.append(copy["no_plots"])

    lines.extend(["", f"## {copy['performance']}", ""])
    lines.extend(
        format_markdown_table(
            performance_rows,
            [
                "controller",
                "initial_position",
                "initial_velocity",
                "final_state_norm",
                "settling_time_s",
                "quadratic_cost",
                "control_energy",
                "max_abs_control",
            ],
            labels=copy["performance_labels"],
            value_maps={"controller": copy["controller_names"]},
            no_data=copy["no_data"],
        ),
    )

    lines.extend(["", f"## {copy['ablation']}", ""])
    lines.extend(
        format_markdown_table(
            ablation_rows,
            [
                "stability_weight",
                "lyapunov_violation_fraction",
                "final_state_norm",
                "settling_time_s",
                "quadratic_cost",
                "control_energy",
            ],
            labels=copy["ablation_labels"],
            no_data=copy["no_data"],
        ),
    )

    lines.extend(["", f"## {copy['interpretation']}", ""])
    lines.extend(f"- {item}" for item in copy["guidance"])
    lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")


def generate_localized_experiment_reports(results_dir: Path) -> list[Path]:
    """Generate the English, Japanese, Korean, and Thai reports."""

    output_paths = []
    for language, filename in REPORT_FILENAMES.items():
        output_path = results_dir / filename
        generate_experiment_report(results_dir, output_path, language=language)
        output_paths.append(output_path)
    return output_paths
