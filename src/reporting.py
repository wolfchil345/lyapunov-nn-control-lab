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
        "performance": "Performance metrics preview",
        "ablation": "Stability-weight ablation preview",
        "interpretation": "Interpretation guide",
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
        "intro": "このレポートはLyapunov neural-network control labで生成された結果を要約します。",
        "main": "主な実験",
        "experiment": "実験",
        "output": "出力",
        "available": "利用可能な図",
        "no_plots": "Plot fileが見つかりません。",
        "performance": "性能指標のpreview",
        "ablation": "安定性重みablationのpreview",
        "interpretation": "解釈ガイド",
        "experiments": [
            "Model architecture",
            "LQRとneural-networkの比較",
            "Stability-aware training loss",
            "複数initial condition",
            "Actuator saturationの比較",
            "Measurement-noise robustness",
            "Parameter robustness",
            "Phase portrait",
            "Lyapunov contour plot",
            "Region of attraction map",
            "Region of attraction controller comparison",
            "Stability-weight ablation study",
        ],
        "guidance": [
            "Final state normが小さいほど、controllerはstateをequilibriumへ近づけます。",
            "Settling timeが短いほど、controllerは速く安定化します。",
            "Control energyが小さいほど、actuation effortは少なくなります。",
            "Lyapunov violation fractionが小さいほど、sampled stateで減少条件への違反が少なくなります。",
            "Region of attraction resultは選択settingで収束するsampled initial stateを推定します。",
            "これらのsampled resultは経験的証拠であり、形式的安定性証明ではありません。",
        ],
    },
    "ko": {
        "switcher": "🌐 언어",
        "title": "실험 보고서",
        "intro": "이 보고서는 Lyapunov neural-network control lab에서 생성된 결과를 요약합니다.",
        "main": "주요 실험",
        "experiment": "실험",
        "output": "출력",
        "available": "사용 가능한 그림",
        "no_plots": "Plot file을 찾지 못했습니다.",
        "performance": "성능 지표 preview",
        "ablation": "안정성 가중치 ablation preview",
        "interpretation": "해석 가이드",
        "experiments": [
            "Model architecture",
            "LQR과 neural-network 비교",
            "Stability-aware training loss",
            "여러 initial condition",
            "Actuator saturation 비교",
            "Measurement-noise robustness",
            "Parameter robustness",
            "Phase portrait",
            "Lyapunov contour plot",
            "Region of attraction map",
            "Region of attraction controller comparison",
            "Stability-weight ablation study",
        ],
        "guidance": [
            "Final state norm이 작을수록 controller가 state를 equilibrium에 더 가깝게 만듭니다.",
            "Settling time이 짧을수록 controller가 더 빠르게 안정화합니다.",
            "Control energy가 작을수록 actuation effort가 적습니다.",
            "Lyapunov violation fraction이 작을수록 sampled state에서 감소 조건 위반이 적습니다.",
            "Region of attraction result는 선택 setting에서 수렴하는 sampled initial state를 추정합니다.",
            "이 sampled result는 경험적 근거이며 형식적 안정성 증명이 아닙니다.",
        ],
    },
    "th": {
        "switcher": "🌐 ภาษา",
        "title": "รายงานการทดลอง",
        "intro": "รายงานนี้สรุปผลที่สร้างจาก Lyapunov neural-network control lab",
        "main": "การทดลองหลัก",
        "experiment": "การทดลอง",
        "output": "ผลลัพธ์",
        "available": "รูปที่มี",
        "no_plots": "ไม่พบ plot file",
        "performance": "Preview ตัวชี้วัดประสิทธิภาพ",
        "ablation": "Preview stability-weight ablation",
        "interpretation": "คู่มือการตีความ",
        "experiments": [
            "Model architecture",
            "เปรียบเทียบ LQR และ neural network",
            "Stability-aware training loss",
            "หลาย initial condition",
            "เปรียบเทียบ actuator saturation",
            "Measurement-noise robustness",
            "Parameter robustness",
            "Phase portrait",
            "Lyapunov contour plot",
            "Region of attraction map",
            "Region of attraction controller comparison",
            "Stability-weight ablation study",
        ],
        "guidance": [
            "Final state norm ที่ต่ำหมายถึง controller พา state เข้าใกล้ equilibrium มากขึ้น",
            "Settling time ที่ต่ำหมายถึง controller ทำให้เสถียรเร็วขึ้น",
            "Control energy ที่ต่ำหมายถึงใช้ actuation effort น้อยลง",
            "Lyapunov violation fraction ที่ต่ำหมายถึง sampled state ละเมิดเงื่อนไขการลดลงน้อยลง",
            "Region of attraction result ประมาณ sampled initial state ที่ลู่เข้าภายใต้ setting ที่เลือก",
            "Sampled result เหล่านี้เป็นหลักฐานเชิงประจักษ์ ไม่ใช่การพิสูจน์เสถียรภาพอย่างเป็นทางการ",
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
) -> list[str]:
    """Format selected CSV columns as a Markdown table."""

    if not rows:
        return ["No data available."]

    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join(["---"] * len(columns)) + " |",
    ]

    for row in rows:
        values = [row.get(column, "") for column in columns]
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

    for experiment, plot_file in zip(copy["experiments"], PLOT_FILES):
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
