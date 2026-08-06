"""Render a Learning Pack Markdown file into a static HTML reader."""

from __future__ import annotations

import argparse
import hashlib
import html
import re
import unicodedata
import urllib.parse
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from jinja2 import Environment, FileSystemLoader, select_autoescape


_atom_path_cache: dict[str, str] = {}
_cache_initialized = False


def init_atom_path_cache() -> None:
    """Khởi tạo bản đồ đường dẫn các Atom ID trong wiki để tạo link chính xác."""
    global _cache_initialized
    if _cache_initialized:
        return

    wiki_root = Path("3-resources/wiki")
    if not wiki_root.exists():
        print(f"DEBUG: wiki_root {wiki_root.resolve()} does not exist!")
        _cache_initialized = True
        return

    # Duyệt qua các thư mục con của wiki
    for path in wiki_root.rglob("*.md"):
        atom_id = path.stem
        # Nhận diện các file Atom ID in hoa có gạch dưới hoặc index/overview
        if "_" in atom_id or atom_id in ["index", "overview", "review", "log"]:
            sub_path = path.relative_to(wiki_root).as_posix()
            rel_path = f"3-resources/wiki/{sub_path}"
            _atom_path_cache[atom_id] = rel_path

    print(f"DEBUG: Khởi tạo cache thành công với {len(_atom_path_cache)} keys từ {wiki_root.resolve()}.")
    _cache_initialized = True



def get_obsidian_uri(atom_id: str) -> str | None:
    """Tạo Obsidian URI cho Atom ID nếu tìm thấy file tương ứng trong vault."""
    init_atom_path_cache()
    rel_path = _atom_path_cache.get(atom_id)
    if rel_path:
        encoded_path = urllib.parse.quote(rel_path)
        return f"obsidian://open?vault=NoteBookLLM_Br&file={encoded_path}"
    return None



SECTION_CLASS_MAP = {
    "Big Picture": "section-big-picture",
    "Key Concepts": "section-key-concepts",
    "Concept Map": "section-concept-map",
    "Must-Know Atoms": "section-must-know-atoms",
    "Comparison Table": "section-comparison-table",
    "Failure Modes": "section-failure-modes",
    "Practice Task": "section-practice-task",
    "Review Questions": "section-review-questions",
    "Related Projects": "section-related-projects",
    "Source Trace": "section-source-trace",
    "Missing Context": "section-missing-context",
    "Next Action": "section-next-action",
}


@dataclass(frozen=True)
class Heading:
    level: int
    text: str
    slug: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render a Learning Pack Markdown file into static HTML."
    )
    parser.add_argument("--input", required=True, help="Input Markdown path.")
    parser.add_argument("--output", required=True, help="Output HTML path.")
    parser.add_argument(
        "--template",
        default=None,
        help="Optional template path. Defaults to scripts/learning/templates/learning_pack_reader.html.",
    )
    return parser.parse_args()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def split_frontmatter(markdown: str) -> tuple[dict[str, str], str]:
    if not markdown.startswith("---\n"):
        return {}, markdown

    end = markdown.find("\n---\n", 4)
    if end == -1:
        return {}, markdown

    raw_meta = markdown[4:end]
    body = markdown[end + 5 :]
    metadata: dict[str, str] = {}
    for line in raw_meta.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"')
    return metadata, body


def slugify(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_text).strip("-").lower()
    return slug or "section"


def unique_slug(text: str, used: dict[str, int]) -> str:
    base = slugify(text)
    count = used.get(base, 0)
    used[base] = count + 1
    if count == 0:
        return base
    return f"{base}-{count + 1}"




def render_inline(text: str, in_link: bool = False) -> str:
    placeholders: list[str] = []

    def store(fragment: str) -> str:
        token = f"@@LP_PLACEHOLDER_{len(placeholders)}@@"
        placeholders.append(fragment)
        return token

    def wikilink_repl(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        label = match.group(2).strip() if match.group(2) else target
        
        # Nếu target là một Atom ID
        if re.match(r"^(CONCEPT|SOURCE|ENTITY|COMPARE|QUERY|DECISION)_[a-zA-Z0-9_]+$", target):
            uri = get_obsidian_uri(target)
            if uri:
                return store(f'<a href="{uri}" class="obsidian-link" title="Mở trong Obsidian"><code>{html.escape(label)}</code></a>')
        
        # Fallback thành obsidian link chung
        uri = get_obsidian_uri(target)
        if uri:
            return store(f'<a href="{uri}" class="obsidian-link" title="Mở trong Obsidian">{html.escape(label)}</a>')
        
        return store(html.escape(match.group(0)))

    def code_repl(match: re.Match[str]) -> str:
        code_text = match.group(1).strip()
        if not in_link and re.match(r"^(CONCEPT|SOURCE|ENTITY|COMPARE|QUERY|DECISION)_[a-zA-Z0-9_]+$", code_text):
            uri = get_obsidian_uri(code_text)
            if uri:
                return store(f'<a href="{uri}" class="obsidian-link" title="Mở trong Obsidian"><code>{html.escape(code_text)}</code></a>')
        return store(f"<code>{html.escape(match.group(1))}</code>")

    def link_repl(match: re.Match[str]) -> str:
        label = render_inline(match.group(1), in_link=True)
        href = html.escape(match.group(2), quote=True)
        return store(f'<a href="{href}">{label}</a>')

    def raw_atom_repl(match: re.Match[str]) -> str:
        atom_id = match.group(0)
        if not in_link:
            uri = get_obsidian_uri(atom_id)
            if uri:
                return store(f'<a href="{uri}" class="obsidian-link" title="Mở trong Obsidian"><code>{html.escape(atom_id)}</code></a>')
        return atom_id

    # 1. Xử lý Obsidian WikiLinks dạng [[Target]] hoặc [[Target|Label]] trước
    protected = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", wikilink_repl, text)

    # 2. Bảo vệ inline code dạng `...`
    protected = re.sub(r"`([^`]+)`", code_repl, protected)
    
    # 3. Bảo vệ Markdown links dạng [label](href)
    protected = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link_repl, protected)
    
    # 4. Tự động phát hiện các Atom ID không nằm trong backticks/links và bọc thành links
    protected = re.sub(
        r"\b(CONCEPT|SOURCE|ENTITY|COMPARE|QUERY|DECISION)_[a-zA-Z0-9_]+\b",
        raw_atom_repl,
        protected
    )
    
    # 5. Escape phần text còn lại
    escaped = html.escape(protected)
    
    # 6. Render strong **...**
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)

    # 7. Khôi phục placeholders
    for index, fragment in enumerate(placeholders):
        escaped = escaped.replace(f"@@LP_PLACEHOLDER_{index}@@", fragment)
    return escaped


def is_heading(line: str) -> bool:
    return bool(re.match(r"^(#{1,6})\s+(.+)$", line))


def is_fence(line: str) -> bool:
    return line.startswith("```")


def is_list_item(line: str) -> bool:
    return bool(re.match(r"^\s*(?:[-*]|\d+\.)\s+.+$", line))


def is_table_start(lines: list[str], index: int) -> bool:
    if index + 1 >= len(lines):
        return False
    if not lines[index].lstrip().startswith("|"):
        return False
    separator = lines[index + 1].strip()
    return bool(re.match(r"^\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?$", separator))


def split_table_row(line: str) -> list[str]:
    row = line.strip().strip("|")
    return [cell.strip() for cell in row.split("|")]


def render_table(lines: list[str]) -> str:
    header = split_table_row(lines[0])
    body_rows = [split_table_row(line) for line in lines[2:]]
    header_html = "".join(f"<th>{render_inline(cell)}</th>" for cell in header)
    rows_html = []
    for row in body_rows:
        cells = "".join(f"<td>{render_inline(cell)}</td>" for cell in row)
        rows_html.append(f"<tr>{cells}</tr>")
    return (
        '<div class="table-wrap"><table>'
        f"<thead><tr>{header_html}</tr></thead>"
        f"<tbody>{''.join(rows_html)}</tbody>"
        "</table></div>"
    )


def render_list(lines: list[str], current_section: str | None) -> str:
    ordered = bool(re.match(r"^\s*\d+\.", lines[0]))
    tag = "ol" if ordered else "ul"
    items = []
    for line in lines:
        content = re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", line).strip()
        rendered = render_inline(content)
        if current_section == "Must-Know Atoms" and "<code>" in rendered:
            key_source = re.sub(r"<[^>]+>", "", rendered)
            progress_key = hashlib.sha1(key_source.encode("utf-8")).hexdigest()[:12]
            rendered = (
                f'<label class="progress-item">'
                f'<input type="checkbox" data-progress-key="{progress_key}">'
                f"<span>{rendered}</span>"
                f"</label>"
            )
        items.append(f"<li>{rendered}</li>")
    return f"<{tag}>{''.join(items)}</{tag}>"


def render_code_block(lines: list[str], opener: str, current_section: str | None = None) -> str:
    language = opener.strip().removeprefix("```").strip()
    class_attr = f' class="language-{html.escape(language)}"' if language else ""
    content = "\n".join(lines)
    
    # Nếu là section Concept Map hoặc language là text hoặc rỗng, tự động bọc link cho các Atom ID
    if current_section == "Concept Map" or language in ["text", ""]:
        # Dọn sạch [[ và ]] bao quanh Atom ID để tránh hiển thị dấu ngoặc trong HTML Reader
        content = re.sub(r"\[\[\b((?:CONCEPT|SOURCE|ENTITY|COMPARE|QUERY|DECISION)_[a-zA-Z0-9_]+)\b\]\]", r"\1", content)
        
        def atom_repl(match: re.Match[str]) -> str:
            atom_id = match.group(0)
            uri = get_obsidian_uri(atom_id)
            if uri:
                return f'<a href="{uri}" class="obsidian-link" title="Mở trong Obsidian">{html.escape(atom_id)}</a>'
            return html.escape(atom_id)
            
        escaped_content = html.escape(content)
        pattern = r"\b(CONCEPT|SOURCE|ENTITY|COMPARE|QUERY|DECISION)_[a-zA-Z0-9_]+\b"
        rendered_content = re.sub(pattern, atom_repl, escaped_content)
        return f"<pre><code{class_attr}>{rendered_content}</code></pre>"
        
    return f"<pre><code{class_attr}>{html.escape(content)}</code></pre>"


def render_paragraph(lines: list[str]) -> str:
    text = " ".join(line.strip() for line in lines)
    return f"<p>{render_inline(text)}</p>"


def render_markdown(markdown: str) -> tuple[str, list[Heading], str]:
    lines = markdown.splitlines()
    used_slugs: dict[str, int] = {}
    headings: list[Heading] = []
    parts: list[str] = []
    current_section: str | None = None
    open_section = False
    first_heading = ""
    i = 0

    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue

        heading_match = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading_match:
            level = len(heading_match.group(1))
            text = heading_match.group(2).strip()
            slug = unique_slug(text, used_slugs)
            headings.append(Heading(level=level, text=text, slug=slug))
            if not first_heading:
                first_heading = text
            if level == 1:
                if open_section:
                    parts.append("</section>")
                current_section = text
                section_class = SECTION_CLASS_MAP.get(text, "")
                parts.append(
                    f'<section id="{slug}" class="reader-section {section_class}">'
                    f'<h1><a class="heading-anchor" href="#{slug}">#</a>{render_inline(text)}</h1>'
                )
                open_section = True
            else:
                parts.append(
                    f'<h{level} id="{slug}">'
                    f'<a class="heading-anchor" href="#{slug}">#</a>{render_inline(text)}'
                    f"</h{level}>"
                )
            i += 1
            continue

        if is_fence(line):
            opener = line
            i += 1
            code_lines: list[str] = []
            while i < len(lines) and not is_fence(lines[i]):
                code_lines.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1
            parts.append(render_code_block(code_lines, opener, current_section))
            continue

        if is_table_start(lines, i):
            table_lines = [lines[i], lines[i + 1]]
            i += 2
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            parts.append(render_table(table_lines))
            continue

        if is_list_item(line):
            list_lines = []
            while i < len(lines) and is_list_item(lines[i]):
                list_lines.append(lines[i])
                i += 1
            parts.append(render_list(list_lines, current_section))
            continue

        paragraph_lines = []
        while (
            i < len(lines)
            and lines[i].strip()
            and not is_heading(lines[i])
            and not is_fence(lines[i])
            and not is_list_item(lines[i])
            and not is_table_start(lines, i)
        ):
            paragraph_lines.append(lines[i])
            i += 1
        parts.append(render_paragraph(paragraph_lines))

    if open_section:
        parts.append("</section>")

    return "\n".join(parts), headings, first_heading


def load_template(template_path: Path):
    env = Environment(
        loader=FileSystemLoader(str(template_path.parent)),
        autoescape=select_autoescape(("html", "xml")),
    )
    return env.get_template(template_path.name)


def relative_asset_path(output_path: Path, asset_path: Path) -> str:
    return asset_path.resolve().relative_to(output_path.parent.resolve()).as_posix()


def main() -> int:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)
    template_path = (
        Path(args.template)
        if args.template
        else Path(__file__).resolve().parent / "templates" / "learning_pack_reader.html"
    )

    markdown = read_text(input_path)
    metadata, body = split_frontmatter(markdown)
    content_html, headings, first_heading = render_markdown(body)
    title = metadata.get("title") or first_heading or input_path.stem

    css_path = output_path.parent / "assets" / "learning-pack.css"
    js_path = output_path.parent / "assets" / "learning-pack.js"
    template = load_template(template_path)
    html_output = template.render(
        title=title,
        metadata=metadata,
        content_html=content_html,
        headings=headings,
        css_href=relative_asset_path(output_path, css_path),
        js_src=relative_asset_path(output_path, js_path),
    )
    write_text(output_path, html_output)
    print(f"Rendered {input_path} -> {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
