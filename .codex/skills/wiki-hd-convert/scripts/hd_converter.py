import argparse
import html
import os
import re
import shutil
import sys
import tempfile
from datetime import date
from pathlib import Path

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    AcceleratorDevice,
    AcceleratorOptions,
    PdfPipelineOptions,
)
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling_core.types.doc.document import PictureItem


def _is_scanned(pdf_path: str) -> bool:
    """Return True if PDF has no extractable text on sample pages."""
    try:
        import pypdf

        reader = pypdf.PdfReader(pdf_path)
        sample_pages = reader.pages[:3]
        text = "".join(page.extract_text() or "" for page in sample_pages)
        return len(text.strip()) < 100
    except Exception:
        return True


def _decode_title(raw_title: str) -> str:
    text = html.unescape(str(raw_title))
    text = text.replace("\u2014", "-").replace("\u2013", "-")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _slugify(text: str) -> str:
    text = _decode_title(text)
    text = re.sub(r"[^A-Za-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text or "UNTITLED"


def _is_outline_node(item) -> bool:
    return isinstance(item, dict) and "/Title" in item and "/Page" in item


def slice_pdf(pdf_path, start_page, end_page, temp_dir):
    """Slice a PDF and return the path to the temporary slice."""
    import pypdf

    reader = pypdf.PdfReader(pdf_path)
    writer = pypdf.PdfWriter()
    actual_end = min(end_page, len(reader.pages))
    for index in range(start_page, actual_end):
        writer.add_page(reader.pages[index])

    slice_name = f"temp_slice_{start_page}_{actual_end}.pdf"
    slice_path = os.path.join(temp_dir, slice_name)
    with open(slice_path, "wb") as handle:
        writer.write(handle)
    return slice_path


def _parse_outline_sequence(sequence, reader):
    nodes = []
    index = 0
    while index < len(sequence):
        item = sequence[index]
        if _is_outline_node(item):
            node = {
                "title": _decode_title(item["/Title"]),
                "page": reader.get_destination_page_number(item),
                "children": [],
            }
            if index + 1 < len(sequence) and isinstance(sequence[index + 1], list):
                node["children"] = _parse_outline_sequence(sequence[index + 1], reader)
                index += 1
            nodes.append(node)
        elif isinstance(item, list):
            nodes.extend(_parse_outline_sequence(item, reader))
        index += 1
    return nodes


def extract_outline_tree(pdf_path: str):
    import pypdf

    reader = pypdf.PdfReader(pdf_path)
    outline = getattr(reader, "outline", None) or []
    if not isinstance(outline, list) or not outline:
        return [], len(reader.pages)
    return _parse_outline_sequence(outline, reader), len(reader.pages)


def assign_end_pages(nodes, exclusive_end_page):
    for idx, node in enumerate(nodes):
        next_start = nodes[idx + 1]["page"] if idx + 1 < len(nodes) else exclusive_end_page
        node["end_page"] = next_start
        if node["children"]:
            assign_end_pages(node["children"], next_start)


def classify_outline_title(title: str) -> str:
    lowered = title.lower()
    if lowered.startswith("part "):
        return "part"
    if lowered.startswith("chapter "):
        return "chapter"
    return "section"


def build_chunk_plan(nodes, total_pages, max_pages):
    assign_end_pages(nodes, total_pages)
    chunk_plan = []
    counters = {"front": 0, "chapter": 0}

    def append_range_chunks(logical_context, unit_title, start_page, end_page):
        if end_page <= start_page:
            return
        span = end_page - start_page
        split_count = max(1, (span + max_pages - 1) // max_pages)
        for split_idx in range(split_count):
            split_start = start_page + split_idx * max_pages
            split_end = min(end_page, split_start + max_pages)
            chunk_plan.append(
                {
                    **logical_context,
                    "unit_title": unit_title,
                    "start_page": split_start,
                    "end_page": split_end,
                    "split_index": split_idx + 1,
                    "split_count": split_count,
                }
            )

    def walk(current_nodes, context):
        local_section = 0
        for node in current_nodes:
            role = classify_outline_title(node["title"])
            next_context = dict(context)
            if role == "part":
                next_context["part_title"] = node["title"]
            elif role == "chapter":
                counters["chapter"] += 1
                next_context["chapter_title"] = node["title"]
                next_context["chapter_index"] = counters["chapter"]
                local_section = 0
            else:
                local_section += 1
                next_context["section_title"] = node["title"]
                next_context["section_index"] = local_section

            if node["children"]:
                first_child_page = node["children"][0]["page"]
                if node["page"] < first_child_page:
                    intro_context = dict(next_context)
                    if role == "part":
                        counters["front"] += 1
                        intro_context["front_index"] = counters["front"]
                        intro_context["section_title"] = f"{node['title']} - Intro"
                    elif role == "chapter":
                        local_section += 1
                        intro_context["section_index"] = local_section
                        intro_context["section_title"] = f"{node['title']} - Intro"
                    append_range_chunks(intro_context, intro_context["section_title"], node["page"], first_child_page)
                walk(node["children"], next_context)
                continue

            start_page = node["page"]
            end_page = node["end_page"]
            if end_page <= start_page:
                continue

            logical_context = dict(next_context)
            if "chapter_title" not in logical_context:
                counters["front"] += 1
                logical_context["front_index"] = counters["front"]
                logical_context["section_title"] = logical_context.get("section_title") or node["title"]
            append_range_chunks(logical_context, node["title"], start_page, end_page)

    if nodes and nodes[0]["page"] > 0:
        counters["front"] += 1
        append_range_chunks(
            {
                "front_index": counters["front"],
                "section_title": "Front Matter Prelude",
            },
            "Front Matter Prelude",
            0,
            nodes[0]["page"],
        )

    walk(nodes, {})

    chunk_plan.sort(key=lambda item: (item["start_page"], item["end_page"], item.get("chapter_index", 0), item.get("section_index", 0)))

    for idx, chunk in enumerate(chunk_plan, start=1):
        chunk["unit_index"] = idx
        if "chapter_index" in chunk and "section_index" in chunk:
            chunk["unit_id"] = f"CH{chunk['chapter_index']:02d}_SEC{chunk['section_index']:02d}"
        elif "chapter_index" in chunk:
            chunk["unit_id"] = f"CH{chunk['chapter_index']:02d}"
        else:
            chunk["unit_id"] = f"FRONT_{chunk.get('front_index', idx):02d}"
        if chunk["split_count"] > 1:
            chunk["unit_id"] = f"{chunk['unit_id']}_P{chunk['split_index']:02d}"

    return chunk_plan


def write_manifest(pdf_path: str, output_dir: str, chunk_plan, chunk_paths):
    pdf_name = os.path.basename(pdf_path)
    base_name = os.path.splitext(pdf_name)[0]
    today = date.today().strftime("%Y-%m-%d")
    manifest_name = f"RAW_{today}_{base_name}_MANIFEST.md"
    manifest_path = os.path.join(output_dir, base_name, manifest_name)

    lines = [
        "---",
        f'source_pdf: "{pdf_name}"',
        'primary_ingest_contract: "manifest"',
        'structure_mode: "pdf_outline"',
        'chunk_order: "chapter>section>page"',
        f'generated_date: "{today}"',
        "---",
        "",
        f"# PRIMARY INGEST MANIFEST: {base_name}",
        "",
        f"Source PDF: {pdf_name}",
        f"Total Units: {len(chunk_plan)}",
        "",
        "## Chunk Index",
    ]

    for chunk, chunk_path in zip(chunk_plan, chunk_paths):
        rel_path = os.path.basename(chunk_path)
        part_title = chunk.get("part_title", "NONE")
        chapter_title = chunk.get("chapter_title", "NONE")
        section_title = chunk.get("section_title", chunk["unit_title"])
        page_range = f"{chunk['start_page'] + 1}-{chunk['end_page']}"
        lines.extend(
            [
                f"### {chunk['unit_id']}",
                f"- part_title: {part_title}",
                f"- chapter_title: {chapter_title}",
                f"- section_title: {section_title}",
                f"- page_range: {page_range}",
                f"- file: {rel_path}",
            ]
        )

    with open(manifest_path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")

    return manifest_path


def convert_pdf_to_hd_markdown(pdf_path, output_dir, chunk_info=None):
    """
    Convert a PDF (or slice) to high-fidelity Markdown.
    chunk_info can include:
      index, start, end, orig_name, unit_id, part_title, chapter_title,
      section_title, manifest_name
    """
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    if chunk_info:
        orig_name = chunk_info["orig_name"]
        final_output_dir = os.path.join(output_dir, orig_name)
        unit_id = chunk_info.get("unit_id", f"CHUNK_{chunk_info['index']:02d}")
        suffix = f"_{unit_id}_P{chunk_info['start'] + 1:03d}-{chunk_info['end']:03d}"
    else:
        final_output_dir = os.path.join(output_dir, base_name)
        suffix = ""

    image_subfolder = "images"
    os.makedirs(os.path.join(final_output_dir, image_subfolder), exist_ok=True)

    do_ocr = _is_scanned(pdf_path)

    pipeline_options = PdfPipelineOptions()
    pipeline_options.images_scale = 1.0
    pipeline_options.generate_page_images = True
    pipeline_options.generate_picture_images = True
    pipeline_options.do_table_structure = True
    pipeline_options.accelerator_options = AcceleratorOptions(
        num_threads=4,
        device=AcceleratorDevice.CUDA if shutil.which("nvidia-smi") else AcceleratorDevice.CPU,
    )
    pipeline_options.do_ocr = do_ocr

    converter = DocumentConverter(
        format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)}
    )

    result = converter.convert(pdf_path)
    doc = result.document
    md_content = doc.export_to_markdown()

    img_count = 0
    for item, level in doc.iterate_items():
        if isinstance(item, PictureItem) and item.image:
            if chunk_info:
                default_unit = f"CHUNK_{chunk_info['index']:02d}"
                img_prefix = f"{chunk_info['orig_name']}_{chunk_info.get('unit_id', default_unit)}_fig_"
            else:
                img_prefix = f"{base_name}_fig_"
            img_name = f"{img_prefix}{img_count:02d}.png"
            img_rel_path = f"{image_subfolder}/{img_name}"
            img_full_path = os.path.join(final_output_dir, img_rel_path)
            item.image.pil_image.save(img_full_path)
            md_link = f"\n![[{img_name}]]\n"
            md_content = md_content.replace("<!-- image -->", md_link, 1)
            img_count += 1

    today = date.today().strftime("%Y-%m-%d")
    final_stem = chunk_info["orig_name"] if chunk_info else base_name
    output_filename = f"RAW_{today}_{final_stem}{suffix}.md"
    output_md_path = os.path.join(final_output_dir, output_filename)

    with open(output_md_path, "w", encoding="utf-8") as handle:
        handle.write(f"# HD SOURCE: {final_stem}{suffix}\n")
        source_pdf_name = f"{chunk_info['orig_name']}.pdf" if chunk_info else os.path.basename(pdf_path)
        handle.write(f"Source PDF: {source_pdf_name}\n")
        handle.write(f"Extracted Images: {img_count}\n")
        if chunk_info:
            handle.write("Structure Mode: chapter>section>page\n")
            handle.write(f"Chunk Unit ID: {chunk_info.get('unit_id', 'UNKNOWN')}\n")
            handle.write(f"Part Title: {chunk_info.get('part_title', 'NONE')}\n")
            handle.write(f"Chapter Title: {chunk_info.get('chapter_title', 'NONE')}\n")
            handle.write(f"Section Title: {chunk_info.get('section_title', 'NONE')}\n")
            handle.write(f"Chunk Range: Pages {chunk_info['start'] + 1} to {chunk_info['end']}\n")
            if chunk_info.get("manifest_name"):
                handle.write(f"Manifest File: {chunk_info['manifest_name']}\n")
        handle.write("---\n\n")
        handle.write(md_content)

    print(f"[OK] Saved: {output_filename} ({img_count} imgs)")
    return output_md_path


def convert_pdf_via_outline(pdf_path, output_dir, max_pages):
    outline_nodes, total_pages = extract_outline_tree(pdf_path)
    if not outline_nodes:
        return None

    chunk_plan = build_chunk_plan(outline_nodes, total_pages, max_pages=max_pages)
    if not chunk_plan:
        return None

    orig_stem = Path(pdf_path).stem
    chunk_paths = []
    manifest_name = f"RAW_{date.today().strftime('%Y-%m-%d')}_{orig_stem}_MANIFEST.md"

    with tempfile.TemporaryDirectory() as tmpdir:
        for chunk in chunk_plan:
            print(
                f"\n[Unit {chunk['unit_index']}] {chunk['unit_id']} "
                f"pages {chunk['start_page'] + 1}-{chunk['end_page']} "
                f"{chunk.get('section_title', chunk['unit_title'])}"
            )
            slice_path = slice_pdf(pdf_path, chunk["start_page"], chunk["end_page"], tmpdir)
            chunk_info = {
                "index": chunk["unit_index"],
                "start": chunk["start_page"],
                "end": chunk["end_page"],
                "orig_name": orig_stem,
                "unit_id": chunk["unit_id"],
                "part_title": chunk.get("part_title", "NONE"),
                "chapter_title": chunk.get("chapter_title", "NONE"),
                "section_title": chunk.get("section_title", chunk["unit_title"]),
                "manifest_name": manifest_name,
            }
            chunk_paths.append(convert_pdf_to_hd_markdown(slice_path, output_dir, chunk_info))

    manifest_path = write_manifest(pdf_path, output_dir, chunk_plan, chunk_paths)
    print(f"[OK] Saved manifest: {os.path.basename(manifest_path)}")
    return manifest_path


def convert_pdf_with_page_windows(pdf_path, output_dir, chunk_size):
    import pypdf

    reader = pypdf.PdfReader(pdf_path)
    total_pages = len(reader.pages)
    if chunk_size > 0 and total_pages > chunk_size:
        print(f"[*] Large PDF detected ({total_pages} pages). Starting page-window chunking (Size: {chunk_size})...")
        orig_stem = Path(pdf_path).stem

        with tempfile.TemporaryDirectory() as tmpdir:
            for start in range(0, total_pages, chunk_size):
                end = min(start + chunk_size, total_pages)
                chunk_idx = (start // chunk_size) + 1
                print(f"\n[Chunk {chunk_idx}] Slicing pages {start + 1} to {end}...")
                slice_path = slice_pdf(pdf_path, start, end, tmpdir)
                chunk_info = {
                    "index": chunk_idx,
                    "start": start,
                    "end": end,
                    "orig_name": orig_stem,
                }
                convert_pdf_to_hd_markdown(slice_path, output_dir, chunk_info)
        return None

    return convert_pdf_to_hd_markdown(pdf_path, output_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Docling HD PDF to Markdown Converter")
    parser.add_argument("pdf_path", help="Path to source PDF file")
    parser.add_argument("--output", default="00_Inbox/Converted_Sources", help="Output root directory")
    parser.add_argument("--chunk-size", type=int, default=15, help="Max pages for page fallback or section split")

    args = parser.parse_args()

    if not os.path.exists(args.pdf_path):
        print(f"[ERROR] File not found: {args.pdf_path}")
        sys.exit(1)

    outline_nodes, total_pages = extract_outline_tree(args.pdf_path)
    if outline_nodes:
        print(f"[*] Outline detected ({len(outline_nodes)} top-level entries, {total_pages} pages). Starting chapter>section>page conversion...")
        manifest = convert_pdf_via_outline(args.pdf_path, args.output, max_pages=args.chunk_size)
        if manifest:
            sys.exit(0)

    convert_pdf_with_page_windows(args.pdf_path, args.output, args.chunk_size)
