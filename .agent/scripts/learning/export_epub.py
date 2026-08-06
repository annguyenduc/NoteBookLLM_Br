#!/usr/bin/env python3
"""
Multi-Format Reader Exporter (HTML & EPUB)
Tự động hóa gộp các Atom tri thức và xuất bản thành HTML/EPUB cho iPad/iPhone.
"""

import os
import sys
import glob
import re
import shutil
import subprocess
import argparse
import yaml
from pathlib import Path

# Thử import các thư viện parser markdown có sẵn trong venv
try:
    from markdown_it import MarkdownIt
    has_markdown_it = True
except ImportError:
    has_markdown_it = False

try:
    import marko
    has_marko = True
except ImportError:
    has_marko = False


def parse_args():
    parser = argparse.ArgumentParser(description="Multi-Format Reader Exporter (HTML & EPUB)")
    parser.add_argument(
        "--manifest",
        required=True,
        help="Đường dẫn tới file cấu hình Manifest (.reader.yml)"
    )
    return parser.parse_args()


def load_yaml(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def split_frontmatter(content: str) -> tuple[dict, str]:
    """Tách frontmatter YAML và nội dung Markdown của Atom."""
    if not content.startswith("---\n"):
        return {}, content

    end = content.find("\n---\n", 4)
    if end == -1:
        return {}, content

    raw_meta = content[4:end]
    body = content[end + 5:]
    try:
        metadata = yaml.safe_load(raw_meta) or {}
    except Exception as e:
        print(f"Cảnh báo: Lỗi parse frontmatter. Chi tiết: {e}")
        metadata = {}
    return metadata, body


def get_atom_type_priority(atom_id: str) -> int:
    """Xác định độ ưu tiên sắp xếp của các Atom theo loại: Source -> Concept -> Entity -> Compare -> Khác."""
    if atom_id.startswith("SOURCE_"):
        return 1
    elif atom_id.startswith("CONCEPT_"):
        return 2
    elif atom_id.startswith("ENTITY_"):
        return 3
    elif atom_id.startswith("COMPARE_"):
        return 4
    return 5


def preprocess_links(
    content: str, 
    published_atoms: dict[str, dict], 
    missing_links_log: list[tuple[str, str, str]]
) -> str:
    """
    Tiền xử lý Wikilinks [[Target]] hoặc [[Target|Label]] và các Atom ID trần.
    Chuyển đổi thành internal markdown links [Label](#target_slug) hoặc plain text warning.
    """
    # Thay thế các đường kẻ ngang --- bằng *** để tránh Pandoc hiểu lầm là YAML metadata block
    content = re.sub(r"(?m)^\s*---\s*$", "***", content)

    # 1. Bảo vệ các đoạn code blocks
    code_blocks = []
    def save_code_block(match):
        code_blocks.append(match.group(0))
        return f"%%CODE_BLOCK_{len(code_blocks)-1}%%"
    
    # Tạm thời thay thế code blocks
    processed = re.sub(r"```[\s\S]*?```", save_code_block, content)
    processed = re.sub(r"`[^`\n]+`", save_code_block, processed)

    # 2. Xử lý Obsidian Wikilinks: [[Target]] hoặc [[Target|Label]]
    def wikilink_repl(match):
        target = match.group(1).strip()
        label = match.group(2).strip() if match.group(2) else target
        
        target_upper = target.upper()
        if target_upper in published_atoms:
            # Internal link hợp lệ
            slug = target_upper.lower()
            return f"[{label}](#{slug})"
        else:
            # Missing Link
            missing_links_log.append((target, label, "Wikilink"))
            return f"{label} (⚠️)"

    processed = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", wikilink_repl, processed)

    # 3. Tự động nhận diện các Atom ID trần (không nằm trong link/code)
    def raw_atom_repl(match):
        atom_id = match.group(0).upper()
        if atom_id in published_atoms:
            slug = atom_id.lower()
            # Tránh tự bọc link nếu nó đã được bọc trong markdown link rồi
            # (Kiểm tra xem trước đó có ký tự '[' và sau đó có ']' không)
            start_idx = match.start()
            if start_idx > 0 and processed[start_idx-1] == '[':
                return atom_id
            return f"[{atom_id}](#{slug})"
        return atom_id

    atom_pattern = r"\b(CONCEPT|SOURCE|ENTITY|COMPARE|QUERY|DECISION)_[a-zA-Z0-9_]+\b"
    processed = re.sub(atom_pattern, raw_atom_repl, processed)

    # 4. Khôi phục các đoạn code blocks
    for i, block in enumerate(code_blocks):
        processed = processed.replace(f"%%CODE_BLOCK_{i}%%", block)

    return processed


def render_html_fallback(markdown_body: str) -> str:
    """Tự render Markdown sang HTML cơ bản nếu không có thư viện ngoài."""
    lines = markdown_body.splitlines()
    html_lines = []
    in_list = False
    in_code = False
    
    for line in lines:
        if line.startswith("```"):
            in_code = not in_code
            html_lines.append("<pre><code>" if in_code else "</code></pre>")
            continue
        if in_code:
            html_lines.append(line)
            continue
            
        if line.startswith("#"):
            match = re.match(r"^(#{1,6})\s+(.+)$", line)
            if match:
                level = len(match.group(1))
                text = match.group(2)
                # Parse inline bold
                text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
                html_lines.append(f"<h{level}>{text}</h{level}>")
        elif line.startswith("- ") or line.startswith("* "):
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            text = line[2:]
            text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
            html_lines.append(f"<li>{text}</li>")
        else:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            if line.strip():
                text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", line)
                html_lines.append(f"<p>{text}</p>")
                
    if in_list:
        html_lines.append("</ul>")
    return "\n".join(html_lines)


def render_markdown_to_html(markdown_body: str) -> str:
    """Parse Markdown sang HTML sử dụng thư viện thích hợp."""
    if has_markdown_it:
        md = MarkdownIt()
        return md.render(markdown_body)
    elif has_marko:
        return marko.convert(markdown_body)
    else:
        print("Cảnh báo: Không tìm thấy thư viện parser markdown chuyên nghiệp. Sử dụng bộ parse dự phòng.")
        return render_html_fallback(markdown_body)


def main():
    args = parse_args()
    manifest_path = Path(args.manifest)
    if not manifest_path.exists():
        print(f"Lỗi: Không tìm thấy file Manifest tại {manifest_path.resolve()}", file=sys.stderr)
        return 1

    # 1. Đọc Manifest
    try:
        manifest = load_yaml(manifest_path)
    except Exception as e:
        print(f"Lỗi: Không thể parse file Manifest YAML. Chi tiết: {e}", file=sys.stderr)
        return 1

    source_id = manifest.get("source_id", manifest_path.stem.split(".")[0])
    title = manifest.get("title", "Reader Book")
    author = manifest.get("author", "AN")
    lang = manifest.get("language", "vi")
    outputs = manifest.get("outputs", {})
    include_patterns = manifest.get("include", [])
    status_policy = manifest.get("status_policy", {})
    link_policy = manifest.get("link_policy", {})
    epub_config = manifest.get("epub", {})

    print(f"=== Bắt đầu xuất bản Reader cho Source ID: {source_id} ===")
    print(f"Tiêu đề: {title}")
    print(f"Tác giả: {author} | Ngôn ngữ: {lang}")

    # Xác định thư mục repo root từ đường dẫn manifest
    repo_root = Path(os.getcwd())
    
    # 2. Quét các file Atom đầu vào
    input_files = []
    for pattern in include_patterns:
        # Glob trong Python hỗ trợ dẫn hướng tương đối từ cwd
        matched = glob.glob(pattern, recursive=True)
        for filepath in matched:
            path = Path(filepath)
            if path.is_file() and path.suffix == ".md":
                input_files.append(path)

    # Loại bỏ trùng lặp
    input_files = list(set(input_files))
    if not input_files:
        print("Lỗi: Không tìm thấy tệp tin Atom nào khớp với cấu hình 'include' trong Manifest.", file=sys.stderr)
        return 1

    print(f"Tìm thấy {len(input_files)} tệp tin Markdown. Bắt đầu lọc theo chính sách trạng thái...")

    # 3. Đọc frontmatter và lọc Atom
    allow_status = status_policy.get("allow", [])
    exclude_status = status_policy.get("exclude", [])
    allow_draft = status_policy.get("allow_draft", False)

    selected_atoms = []
    published_atoms_dict = {}

    for path in input_files:
        atom_id = path.stem
        try:
            content = path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"Cảnh báo: Không thể đọc file {path.name}. Chi tiết: {e}")
            continue

        metadata, body = split_frontmatter(content)
        status = metadata.get("status", "DRAFT")

        # Lọc trạng thái
        if status in exclude_status:
            continue
        if status == "DRAFT" and not allow_draft:
            continue
        if allow_status and (status not in allow_status):
            continue

        # Atom hợp lệ
        selected_atoms.append({
            "id": atom_id,
            "path": path,
            "metadata": metadata,
            "body": body,
            "title": metadata.get("title", atom_id),
            "priority": get_atom_type_priority(atom_id)
        })
        published_atoms_dict[atom_id.upper()] = selected_atoms[-1]

    if not selected_atoms:
        print("Lỗi: Không có Atom nào vượt qua bộ lọc chính sách trạng thái (status_policy).", file=sys.stderr)
        return 1

    # Tìm kiếm file sắp xếp học tập (ưu tiên Learning Pack ở workspaces/learning/dashboard/packs/, sau đó fallback sang workspaces/learning/dashboard/paths/)
    learning_order = []
    learning_file = None
    
    # 1. Tìm ở workspaces/learning/dashboard/packs/
    learning_root = repo_root / "workspaces" / "learning" / "dashboard"
    learning_pack_dir = learning_root / "packs"
    if learning_pack_dir.exists():
        pack_files = list(learning_pack_dir.glob(f"*{source_id}*.md"))
        if pack_files:
            learning_file = pack_files[0]
            print(f"Tìm thấy Learning Pack để sắp xếp: {learning_file.name}")
            
    # 2. Fallback sang workspaces/learning/dashboard/paths/
    if not learning_file:
        learning_path_dir = learning_root / "paths"
        if learning_path_dir.exists():
            path_files = list(learning_path_dir.glob(f"*{source_id}*.md"))
            if path_files:
                learning_file = path_files[0]
                print(f"Fallback tìm thấy Lộ trình học tập tại: {learning_file.name}")
                
    if learning_file:
        try:
            file_content = learning_file.read_text(encoding="utf-8")
            # Tìm tất cả các Atom ID dạng [[ATOM_ID]]
            matches = re.findall(r"\[\[([a-zA-Z0-9_]+)\]\]", file_content)
            for m in matches:
                atom_upper = m.upper()
                if atom_upper not in learning_order:
                    learning_order.append(atom_upper)
            print(f"Đã trích xuất {len(learning_order)} Atom từ {learning_file.name} để làm thứ tự sắp xếp.")
        except Exception as e:
            print(f"Cảnh báo: Không thể đọc file {learning_file.name} để sắp xếp. Chi tiết: {e}")

    # Định nghĩa hàm lấy sort key
    def get_sort_key(atom):
        atom_id_upper = atom["id"].upper()
        if atom_id_upper in learning_order:
            return (0, learning_order.index(atom_id_upper), atom["id"])
        else:
            # Nếu không có trong lộ trình, xếp xuống dưới theo priority và ID
            return (1, atom["priority"], atom["id"])

    selected_atoms.sort(key=get_sort_key)
    print(f"Đã sắp xếp và duyệt {len(selected_atoms)} Atom hợp lệ để xuất bản.")

    # 4. Tiền xử lý liên kết và gộp nội dung Markdown trung gian
    missing_links_log = []
    book_markdown_parts = []
    headings_toc = []

    # Thêm Metadata Block cho Pandoc ở đầu sách
    book_markdown_parts.append("---")
    book_markdown_parts.append(f"title: \"{title}\"")
    book_markdown_parts.append(f"author: \"{author}\"")
    book_markdown_parts.append(f"lang: \"{lang}\"")
    book_markdown_parts.append("---")
    book_markdown_parts.append("")

    for atom in selected_atoms:
        # Rút gọn tiêu đề, loại bỏ phần chú thích tiếng Anh trong ngoặc đơn ở cuối (ví dụ: "Điểm đòn bẩy (Leverage Points)" -> "Điểm đòn bẩy")
        atom_title = re.sub(r"\s*\([^)]+\)\s*$", "", atom['title']).strip()
        
        # Loại bỏ tiêu đề H1 trong body để tránh lặp với tiêu đề chương tự sinh
        cleaned_body = re.sub(r"(?m)^#\s+.+$\n?", "", atom["body"])
        
        # Tiền xử lý nội dung
        preprocessed_body = preprocess_links(cleaned_body, published_atoms_dict, missing_links_log)
        
        # Định danh heading cấp 1 cho từng Atom
        atom_slug = atom["id"].lower()
        
        headings_toc.append({
            "level": 1,
            "text": atom_title,
            "slug": atom_slug
        })

        # Gộp vào Markdown tổng
        book_markdown_parts.append(f"# {atom_title} {{#{atom_slug}}}")
        book_markdown_parts.append("")
        
        # Chèn metadata strip hiển thị ngắn gọn của Atom
        status_val = atom["metadata"].get("status", "UNVERIFIED")
        book_markdown_parts.append("<div class=\"metadata-strip\">")
        book_markdown_parts.append(f"<div><span class=\"metadata-label\">ID:</span> {atom['id']}</div>")
        book_markdown_parts.append(f"<div><span class=\"metadata-label\">Trạng thái:</span> {status_val}</div>")
        book_markdown_parts.append("</div>")
        book_markdown_parts.append("")

        book_markdown_parts.append(preprocessed_body)
        book_markdown_parts.append("")
        # Page break trong EPUB
        book_markdown_parts.append('<div style="page-break-after: always;"></div>')
        book_markdown_parts.append("")

    # Ghi file Markdown trung gian
    tmp_dir = repo_root / "exports" / "reader" / "_tmp"
    tmp_dir.mkdir(parents=True, exist_ok=True)
    tmp_book_path = tmp_dir / f"{source_id}.book.md"
    
    full_markdown_content = "\n".join(book_markdown_parts)
    tmp_book_path.write_text(full_markdown_content, encoding="utf-8")
    print(f"Đã tạo file Markdown gộp tạm thời tại {tmp_book_path.relative_to(repo_root)}")

    # 5. Xuất bản HTML Reader
    html_output_path = repo_root / outputs.get("html", f"exports/reader/{source_id}.html")
    html_output_path.parent.mkdir(parents=True, exist_ok=True)

    # Đọc template HTML
    template_path = repo_root / "scripts" / "learning" / "templates" / "learning_pack_reader.html"
    if template_path.exists():
        template_content = template_path.read_text(encoding="utf-8")
    else:
        # Fallback template nội bộ nếu không tìm thấy template file
        template_content = """<!doctype html>
<html lang="vi">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="color-scheme" content="light dark">
    <title>{{ title }}</title>
    <style>
      body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 0; display: flex; }
      .reader-shell { display: flex; width: 100%; min-height: 100vh; }
      .reader-toc { width: 300px; background: #f8f9fa; border-right: 1px solid #e9ecef; padding: 20px; position: sticky; top: 0; height: 100vh; overflow-y: auto; }
      .reader-main { flex: 1; padding: 40px; max-width: 800px; margin: 0 auto; }
      .toc-link { display: block; margin: 8px 0; color: #495057; text-decoration: none; font-size: 0.9em; }
      .toc-link:hover { color: #007bff; }
      .metadata-strip { font-size: 0.85em; color: #6c757d; border-left: 3px solid #007bff; padding-left: 10px; margin-bottom: 20px; }
      .missing-link { color: #dc3545; background-color: #f8d7da; padding: 2px 4px; border-radius: 3px; font-size: 0.9em; font-style: italic; }
    </style>
  </head>
  <body>
    <div class="reader-shell">
      <aside class="reader-toc">
        <h3>Mục lục</h3>
        <nav>
          {% for heading in headings %}
          <a class="toc-link" href="#{{ heading.slug }}">{{ heading.text }}</a>
          {% endfor %}
        </nav>
      </aside>
      <main class="reader-main">
        <h1>{{ title }}</h1>
        <article class="reader-content">
          {{ content_html | safe }}
        </article>
      </main>
    </div>
  </body>
</html>"""

    # Parse markdown sang HTML
    content_html = render_markdown_to_html(full_markdown_content)
    
    # Đọc nội dung CSS và JS từ assets để nhúng trực tiếp vào file HTML tự chứa (self-contained)
    css_content = ""
    html_css_path = repo_root / "workspaces" / "learning" / "dashboard" / "packs" / "html" / "assets" / "learning-pack.css"
    if html_css_path.exists():
        try:
            css_content = html_css_path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"Cảnh báo: Không thể đọc file CSS. Chi tiết: {e}")

    js_content = ""
    html_js_path = repo_root / "workspaces" / "learning" / "dashboard" / "packs" / "html" / "assets" / "learning-pack.js"
    if html_js_path.exists():
        try:
            js_content = html_js_path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"Cảnh báo: Không thể đọc file JS. Chi tiết: {e}")

    # Render Jinja2 thủ công đơn giản hoặc qua Jinja2 nếu khả dụng
    try:
        from jinja2 import Template
        tmpl = Template(template_content)
        rendered_html = tmpl.render(
            title=title,
            headings=headings_toc,
            content_html=content_html,
            css_href="",  # Không dùng CSS ngoài nếu chạy single-file độc lập
            css_content=css_content,
            js_src="",
            js_content=js_content,
            metadata={"source_id": source_id, "status": "PUBLISHED"}
        )
    except ImportError:
        # Render string replacement thủ công nếu thiếu Jinja2
        rendered_html = template_content.replace("{{ title }}", title)
        # Thay thế danh sách heading
        toc_links_html = []
        for h in headings_toc:
            toc_links_html.append(f'<a class="toc-link" href="#{h["slug"]}">{h["text"]}</a>')
        rendered_html = rendered_html.replace('{% for heading in headings %}\n          <a class="toc-link" href="#{{ heading.slug }}">{{ heading.text }}</a>\n          {% endfor %}', "\n".join(toc_links_html))
        rendered_html = rendered_html.replace("{{ content_html | safe }}", content_html)
        
        # Thay thế CSS nội bộ
        if css_content:
            rendered_html = rendered_html.replace('{% if css_content %}\n    <style>\n      {{ css_content | safe }}\n    </style>\n    {% else %}\n    <link rel="stylesheet" href="{{ css_href }}">\n    {% endif %}', f"<style>{css_content}</style>")
            rendered_html = rendered_html.replace('<link rel="stylesheet" href="{{ css_href }}">', f"<style>{css_content}</style>")
        else:
            rendered_html = rendered_html.replace('{% if css_content %}\n    <style>\n      {{ css_content | safe }}\n    </style>\n    {% else %}\n    <link rel="stylesheet" href="{{ css_href }}">\n    {% endif %}', '<link rel="stylesheet" href="">')
            rendered_html = rendered_html.replace('<link rel="stylesheet" href="{{ css_href }}">', '<link rel="stylesheet" href="">')

        # Thay thế JS nội bộ
        if js_content:
            rendered_html = rendered_html.replace('{% if js_content %}\n    <script>\n      {{ js_content | safe }}\n    </script>\n    {% else %}\n    <script src="{{ js_src }}"></script>\n    {% endif %}', f"<script>{js_content}</script>")
            rendered_html = rendered_html.replace('<script src="{{ js_src }}"></script>', f"<script>{js_content}</script>")
        else:
            rendered_html = rendered_html.replace('{% if js_content %}\n    <script>\n      {{ js_content | safe }}\n    </script>\n    {% else %}\n    <script src="{{ js_src }}"></script>\n    {% endif %}', "")
            rendered_html = rendered_html.replace('<script src="{{ js_src }}"></script>', "")

    html_output_path.write_text(rendered_html, encoding="utf-8")
    print(f"Đã xuất bản HTML Reader tại {html_output_path.relative_to(repo_root)}")

    # 6. Biên dịch EPUB Reader (Sử dụng Pandoc CLI di động)
    epub_output_path = repo_root / outputs.get("epub", f"exports/reader/{source_id}.epub")
    epub_output_path.parent.mkdir(parents=True, exist_ok=True)

    # Tìm executable Pandoc
    # Kiểm tra xem có bản portable trong scripts/learning/bin không
    pandoc_bin_glob = list((repo_root / "scripts" / "learning" / "bin").glob("**/pandoc.exe"))
    if pandoc_bin_glob:
        pandoc_path = str(pandoc_bin_glob[0].resolve())
        print(f"Tìm thấy Pandoc CLI di động tại: {pandoc_path}")
    else:
        # Fallback tìm trong hệ thống
        pandoc_path = shutil.which("pandoc")
        if not pandoc_path:
            print("Lỗi: Không tìm thấy Pandoc CLI hệ thống lẫn di động. Vui lòng kiểm tra lại việc tải Pandoc.", file=sys.stderr)
            return 1
        print(f"Sử dụng Pandoc CLI hệ thống: {pandoc_path}")

    # CSS path cho EPUB
    css_template = epub_config.get("css", "scripts/learning/templates/epub_style.css")
    epub_css_path = repo_root / css_template
    if not epub_css_path.exists():
        # Fallback nếu file css không tồn tại
        epub_css_path = repo_root / "scripts" / "learning" / "templates" / "epub_style.css"

    # Xây dựng câu lệnh Pandoc
    cmd = [
        pandoc_path,
        str(tmp_book_path),
        "-o", str(epub_output_path),
        "--from", "markdown+yaml_metadata_block",
        "--to", "epub3",
    ]

    if epub_config.get("toc", True):
        cmd.append("--toc")
        toc_depth = epub_config.get("toc_depth", 2)
        cmd.append(f"--toc-depth={toc_depth}")

    if epub_css_path.exists():
        cmd.append(f"--css={epub_css_path}")

    cmd.extend([
        "--metadata", f"title={title}",
        "--metadata", f"lang={lang}"
    ])

    print("Đang gọi Pandoc CLI biên dịch EPUB...")
    try:
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"Biên dịch EPUB thành công! Sách được xuất tại {epub_output_path.relative_to(repo_root)}")
    except subprocess.CalledProcessError as e:
        print(f"Lỗi: Pandoc CLI gặp lỗi khi chạy. Lỗi: {e.stderr}", file=sys.stderr)
        return 1

    # 7. Dọn dẹp tệp tin tạm thời
    try:
        if tmp_book_path.exists():
            tmp_book_path.unlink()
        if tmp_dir.exists() and not os.listdir(tmp_dir):
            tmp_dir.rmdir()
        print("Đã dọn dẹp các tệp trung gian tạm thời.")
    except Exception as e:
        print(f"Cảnh báo: Không thể dọn dẹp thư mục tạm. Chi tiết: {e}")

    # 8. Báo cáo Missing Links ra terminal
    if missing_links_log:
        # Loại bỏ trùng lặp log cảnh báo
        unique_missing = list(set(missing_links_log))
        print("\n=== BÁO CÁO CẢNH BÁO: LIÊN KẾT BỊ THIẾU (MISSING LINKS) ===")
        print(f"Tổng số liên kết thiếu được phát hiện: {len(unique_missing)}")
        for target, label, link_type in unique_missing:
            print(f"- [!] Không tìm thấy Atom '{target}' (Nhãn: '{label}') - Loại: {link_type}")
        print("========================================================\n")
    else:
        print("\nKhông phát hiện liên kết thiếu nào. Cấu trúc liên kết Atom hoàn hảo!\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
