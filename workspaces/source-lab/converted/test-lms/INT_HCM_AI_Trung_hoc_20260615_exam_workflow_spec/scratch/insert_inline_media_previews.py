from pathlib import Path


ROOT = Path(r"D:\_agent_worktrees\20260615_exam_workflow_spec\workspaces\source-lab\converted\test-lms\INT_HCM_AI_Trung_hoc")
MD_PATH = ROOT / "GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2.md"
HTML_PATH = ROOT / "GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2.html"
MEDIA_DIR = "GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media"


QUESTION_IMAGES = {
    "02": [("Câu 02 - A", "cau_02_a.png"), ("Câu 02 - B", "cau_02_b.png"), ("Câu 02 - C", "cau_02_c.png"), ("Câu 02 - D", "cau_02_d.png")],
    "03": [("Câu 03 - 3.1", "cau_03_1.png"), ("Câu 03 - 3.2", "cau_03_2.png"), ("Câu 03 - 3.3", "cau_03_3.png"), ("Câu 03 - 3.4", "cau_03_4.png")],
    "04": [("Câu 04 - 4.1", "cau_04_1.png")],
    "06": [("Câu 06 - 6.1", "cau_06_1.png")],
    "07": [("Câu 07 - A", "cau_07_a.png"), ("Câu 07 - B", "cau_07_b.png"), ("Câu 07 - C", "cau_07_c.png"), ("Câu 07 - D", "cau_07_d.png")],
    "08": [("Câu 08 - 8.1", "cau_08_1.png")],
    "09": [("Câu 09 - 9.1", "cau_09_1.png")],
    "10": [("Câu 10 - 10.1", "cau_10_1.png")],
    "11": [("Câu 11 - 11.1", "cau_11_1.png"), ("Câu 11 - 11.2", "cau_11_2.png")],
    "12": [("Câu 12 - 12.1", "cau_12_1.png"), ("Câu 12 - 12.2", "cau_12_2.png")],
    "13": [("Câu 13 - 13.1", "cau_13_1.png"), ("Câu 13 - 13.2", "cau_13_2.png"), ("Câu 13 - 13.3", "cau_13_3.png"), ("Câu 13 - 13.4", "cau_13_4.png")],
    "14": [("Câu 14 - 14.1", "cau_14_1.png"), ("Câu 14 - 14.2", "cau_14_2.png")],
    "19": [("Câu 19 - 19.1", "cau_19_1.png")],
    "21": [("Câu 21 - 21.1", "cau_21_1.png"), ("Câu 21 - 21.2", "cau_21_2.png"), ("Câu 21 - 21.3", "cau_21_3.png")],
    "22": [("Câu 22 - A", "cau_22_a.png"), ("Câu 22 - B", "cau_22_b.png"), ("Câu 22 - C", "cau_22_c.png"), ("Câu 22 - D", "cau_22_d.png")],
    "23": [("Câu 23 - A", "cau_23_a.png"), ("Câu 23 - B", "cau_23_b.png"), ("Câu 23 - C", "cau_23_c.png"), ("Câu 23 - D", "cau_23_d.png")],
    "24": [("Câu 24 - A", "cau_24_a.png"), ("Câu 24 - B", "cau_24_b.png"), ("Câu 24 - C", "cau_24_c.png"), ("Câu 24 - D", "cau_24_d.png")],
    "25": [("Câu 25 - A", "cau_25_a.png"), ("Câu 25 - B", "cau_25_b.png"), ("Câu 25 - C", "cau_25_c.png"), ("Câu 25 - D", "cau_25_d.png")],
    "26": [("Câu 26 - 26.1", "cau_26_1.png")],
    "27": [("Câu 27 - A", "cau_27_a.png"), ("Câu 27 - B", "cau_27_b.png"), ("Câu 27 - C", "cau_27_c.png"), ("Câu 27 - D", "cau_27_d.png")],
    "28": [("Câu 28 - A", "cau_28_a.png"), ("Câu 28 - B", "cau_28_b.png"), ("Câu 28 - C", "cau_28_c.png"), ("Câu 28 - D", "cau_28_d.png")],
    "29": [("Câu 29 - A", "cau_29_a.png"), ("Câu 29 - B", "cau_29_b.png"), ("Câu 29 - C", "cau_29_c.png"), ("Câu 29 - D", "cau_29_d.png")],
    "30": [("Câu 30 - A", "cau_30_a.png"), ("Câu 30 - B", "cau_30_b.png"), ("Câu 30 - C", "cau_30_c.png"), ("Câu 30 - D", "cau_30_d.png")],
}


def build_preview_block(question_id: str) -> str:
    lines = ["- Xem nhanh trong đề:"]
    for alt, file_name in QUESTION_IMAGES[question_id]:
        lines.append(f"![{alt}](<{MEDIA_DIR}/{file_name}>)")
    return "\n".join(lines)


def main() -> None:
    text = MD_PATH.read_text(encoding="utf-8")
    lines = text.splitlines()
    output: list[str] = []
    current_question: str | None = None
    skipping_preview = False

    for line in lines:
        if line.startswith("## **Câu "):
            current_question = line.split("## **Câu ", 1)[1][:2]
            skipping_preview = False

        if line == "- Xem nhanh trong đề:":
            skipping_preview = True
            continue

        if skipping_preview:
            if line.startswith("![Câu "):
                continue
            skipping_preview = False

        output.append(line)

        if current_question in QUESTION_IMAGES and line.startswith("- File kiểm tra nguồn:"):
            output.append(build_preview_block(current_question))

    MD_PATH.write_text("\n".join(output) + "\n", encoding="utf-8")
    print(f"updated {MD_PATH}")


if __name__ == "__main__":
    main()
