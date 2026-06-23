from __future__ import annotations

import subprocess
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION_START
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(
    r"D:\_agent_worktrees\20260615_exam_workflow_spec\workspaces\source-lab\converted\test-lms\INT_HCM_AI_Trung_hoc"
)
SOURCE_MD = ROOT / "GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2.md"
OUT_DIR = ROOT / "documents_output"
TRIMMED_MD = OUT_DIR / "AI_THCS_1_30_cau_trac_nghiem_gdocs.md"
REFERENCE_DOCX = OUT_DIR / "google_docs_reference.docx"
RAW_DOCX = OUT_DIR / "AI_THCS_1_30_cau_trac_nghiem_raw.docx"
FINAL_DOCX = OUT_DIR / "AI_THCS_1_30_cau_trac_nghiem_google_docs.docx"

PANDOC = Path(r"D:\NoteBookLLM_Br\scripts\learning\bin\pandoc-3.1.12.3\pandoc.exe")
SANITIZER_CANDIDATES = [
    Path(
        r"D:\anngu\.codex\plugins\cache\openai-primary-runtime\documents\26.619.11828\skills\documents\scripts\google_docs_title_sanitize.py"
    ),
    Path(
        r"C:\Users\anngu\.cache\codex-runtimes\codex-primary-runtime\plugins\openai-primary-runtime\plugins\documents\skills\documents\scripts\google_docs_title_sanitize.py"
    ),
]


def get_sanitizer() -> Path:
    for candidate in SANITIZER_CANDIDATES:
        if candidate.exists():
            return candidate
    raise FileNotFoundError("Could not find google_docs_title_sanitize.py")


def set_run_font(style, font_name: str, size_pt: int, color: str = "000000") -> None:
    style.font.name = font_name
    style.font.size = Pt(size_pt)
    style.font.color.rgb = RGBColor.from_string(color)
    style.element.rPr.rFonts.set(qn("w:ascii"), font_name)
    style.element.rPr.rFonts.set(qn("w:hAnsi"), font_name)
    style.element.rPr.rFonts.set(qn("w:eastAsia"), font_name)


def build_reference_docx(path: Path) -> None:
    doc = Document()
    section = doc.sections[0]
    section.start_type = WD_SECTION_START.NEW_PAGE
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)
    section.header_distance = Inches(0.492)
    section.footer_distance = Inches(0.492)

    normal = doc.styles["Normal"]
    set_run_font(normal, "Arial", 11)
    normal.paragraph_format.space_before = Pt(0)
    normal.paragraph_format.space_after = Pt(8)
    normal.paragraph_format.line_spacing = 1.15

    heading1 = doc.styles["Heading 1"]
    set_run_font(heading1, "Arial", 20)
    heading1.font.bold = False
    heading1.paragraph_format.space_before = Pt(20)
    heading1.paragraph_format.space_after = Pt(6)
    heading1.paragraph_format.line_spacing = 1.15

    heading2 = doc.styles["Heading 2"]
    set_run_font(heading2, "Arial", 16)
    heading2.font.bold = False
    heading2.paragraph_format.space_before = Pt(18)
    heading2.paragraph_format.space_after = Pt(6)
    heading2.paragraph_format.line_spacing = 1.15

    heading3 = doc.styles["Heading 3"]
    set_run_font(heading3, "Arial", 14, "434343")
    heading3.font.bold = False
    heading3.paragraph_format.space_before = Pt(16)
    heading3.paragraph_format.space_after = Pt(4)
    heading3.paragraph_format.line_spacing = 1.15

    for style_name in ("List Bullet", "List Number", "Body Text", "Table Grid"):
        if style_name in doc.styles:
            style = doc.styles[style_name]
            set_run_font(style, "Arial", 11)
            style.paragraph_format.space_before = Pt(0)
            style.paragraph_format.space_after = Pt(4)
            style.paragraph_format.line_spacing = 1.15

    doc.add_paragraph("Reference document for Google Docs-targeted exam export.")
    doc.save(path)


def build_trimmed_markdown(source: Path, target: Path) -> None:
    text = source.read_text(encoding="utf-8")
    end_marker = "## **PHẦN II: ĐỀ THI THỰC HÀNH**"
    if end_marker not in text:
        raise ValueError("Could not find the practical-section marker.")
    trimmed = text.split(end_marker, 1)[0].rstrip() + "\n"
    target.write_text(trimmed, encoding="utf-8")


def run(cmd: list[str], cwd: Path | None = None) -> None:
    subprocess.run(cmd, check=True, cwd=str(cwd) if cwd else None)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    build_trimmed_markdown(SOURCE_MD, TRIMMED_MD)
    build_reference_docx(REFERENCE_DOCX)
    sanitizer = get_sanitizer()

    run(
        [
            str(PANDOC),
            str(TRIMMED_MD),
            "--from",
            "gfm",
            "--reference-doc",
            str(REFERENCE_DOCX),
            "--resource-path",
            str(ROOT),
            "-o",
            str(RAW_DOCX),
        ],
        cwd=ROOT,
    )

    run(
        [
            r"C:\Users\anngu\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe",
            str(sanitizer),
            str(RAW_DOCX),
            "--out",
            str(FINAL_DOCX),
        ]
    )
    run(
        [
            r"C:\Users\anngu\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe",
            str(sanitizer),
            str(FINAL_DOCX),
            "--check",
        ]
    )


if __name__ == "__main__":
    main()
