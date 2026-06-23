from __future__ import annotations

import pathlib
import subprocess
import sys

try:
    import markdown as markdown_lib
except ModuleNotFoundError:
    markdown_lib = None

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Đề kiểm tra AI Trung học</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700&family=Arial:wght@400;700&display=swap');
:root { --primary-color: #002060; --secondary-color: #0081bd; --bg-color: #f0f2f5; --paper-color: #ffffff; --text-color: #333333; }
body { font-family: 'Arial', sans-serif; background-color: var(--bg-color); color: var(--text-color); margin: 0; padding: 40px 20px; line-height: 1.6; }
.a4-container { max-width: 210mm; margin: 0 auto; background-color: var(--paper-color); padding: 25mm; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1); border-radius: 4px; text-align: justify; }
h1, h2, h3, h4, h5, h6 { font-family: 'Montserrat', sans-serif; color: var(--primary-color); margin-top: 1.5em; margin-bottom: 0.5em; }
h1 { text-align: center; font-size: 24pt; text-transform: uppercase; border-bottom: 2px solid var(--secondary-color); padding-bottom: 10px; margin-bottom: 30px; }
h2 { font-size: 16pt; border-bottom: 1px solid #eeeeee; padding-bottom: 5px; }
ul { list-style-type: none; padding-left: 20px; margin-top: 10px; margin-bottom: 10px; }
ul li { margin-bottom: 8px; position: relative; display: block; }
ul li::before { content: "○"; color: var(--secondary-color); position: absolute; left: -20px; font-weight: bold; }
ul li:has(strong:contains("Đáp án đúng:")), ul li:has(strong:contains("Giải thích:")), ul li:has(strong:contains("Trích dẫn:")) { list-style-type: none; }
ul li:has(strong:contains("Đáp án đúng:"))::before, ul li:has(strong:contains("Giải thích:"))::before, ul li:has(strong:contains("Trích dẫn:"))::before { content: "►"; color: var(--primary-color); }
img { max-width: 80%; height: auto; display: block; margin: 20px auto; border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.05); }
table { border-collapse: collapse; width: 100%; margin: 25px 0; font-size: 11pt; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
th, td { border: 1px solid #dddddd; padding: 12px 15px; }
th { background-color: var(--primary-color); color: white; font-family: 'Montserrat', sans-serif; font-weight: 600; text-align: center; }
td { vertical-align: top; }
tr:nth-child(even) { background-color: #f9f9f9; }
hr { border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 32, 96, 0.75), rgba(0, 0, 0, 0)); margin: 40px 0; }
</style>
</head>
<body>
    <div class="a4-container">
        <!--CONTENT_PLACEHOLDER-->
    </div>
</body>
</html>
"""

PANDOC_PATH = (
    pathlib.Path(__file__).resolve().parents[1]
    / "learning"
    / "bin"
    / "pandoc-3.1.12.3"
    / "pandoc.exe"
)


def render_markdown_to_html(md_text: str) -> str:
    if markdown_lib is not None:
        return markdown_lib.markdown(md_text, extensions=["tables", "fenced_code"])

    if not PANDOC_PATH.exists():
        raise RuntimeError("Missing both python-markdown and bundled pandoc.")

    result = subprocess.run(
        [str(PANDOC_PATH), "--from", "gfm", "--to", "html"],
        input=md_text,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    return result.stdout


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: python generate_exam_html.py <input_md> <output_html>")
        return 1

    input_path = pathlib.Path(sys.argv[1])
    output_path = pathlib.Path(sys.argv[2])

    if not input_path.exists():
        print(f"Error: {input_path} does not exist.")
        return 1

    md_text = input_path.read_text(encoding="utf-8")
    html_content = render_markdown_to_html(md_text)
    full_html = HTML_TEMPLATE.replace("<!--CONTENT_PLACEHOLDER-->", html_content)
    output_path.write_text(full_html, encoding="utf-8")
    print(f"Successfully generated HTML: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
