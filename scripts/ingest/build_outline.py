import argparse
import json
import re
from collections import OrderedDict
from pathlib import Path


def parse_chunk_metadata(chunk_path: Path):
    text = chunk_path.read_text(encoding="utf-8", errors="replace")
    metadata = {
        "file_name": chunk_path.name,
        "start_page": None,
        "end_page": None,
        "part_title": "NONE",
        "chapter_title": "NONE",
        "section_title": "NONE",
        "headings": [],
    }

    range_match = re.search(r"Chunk Range:\s*Pages\s+(\d+)\s+to\s+(\d+)", text)
    if range_match:
        metadata["start_page"] = int(range_match.group(1))
        metadata["end_page"] = int(range_match.group(2))
    else:
        file_match = re.search(r"_P(\d+)-(\d+)\.md$", chunk_path.name)
        if file_match:
            metadata["start_page"] = int(file_match.group(1))
            metadata["end_page"] = int(file_match.group(2))

    for field in ("Part Title", "Chapter Title", "Section Title"):
        match = re.search(rf"{field}:\s*(.+)", text)
        if match:
            key = field.lower().replace(" ", "_")
            metadata[key] = match.group(1).strip()

    for line in text.splitlines():
        if re.match(r"^(#|##|###)\s+", line):
            metadata["headings"].append(line.strip())

    return metadata


def build_outline_entries(converted_dir: Path):
    md_files = sorted(p for p in converted_dir.glob("RAW_*.md") if not p.name.endswith("_MANIFEST.md"))
    entries = [parse_chunk_metadata(path) for path in md_files]
    return entries


def group_outline(entries):
    grouped = OrderedDict()
    for entry in entries:
        chapter = entry["chapter_title"]
        if chapter == "NONE":
            chapter = "Front Matter"
        if chapter not in grouped:
            grouped[chapter] = {
                "start_page": entry["start_page"],
                "end_page": entry["end_page"],
                "sections": [],
            }
        grouped[chapter]["start_page"] = min(grouped[chapter]["start_page"] or entry["start_page"], entry["start_page"] or 10**9)
        grouped[chapter]["end_page"] = max(grouped[chapter]["end_page"] or 0, entry["end_page"] or 0)
        grouped[chapter]["sections"].append(entry)
    return grouped


def write_outline(entries, output_path: Path, source_id: str, source_file: str = ""):
    grouped = group_outline(entries)
    lines = [
        "---",
        'primary_ingest_contract: "outline"',
        f'source_id: "{source_id}"',
    ]
    if source_file:
        lines.append(f'source_file: "{source_file}"')
    lines.extend(
        [
            "---",
            "",
        ]
    )
    lines.extend(
        [
        f"# Outline - {source_id}",
        "",
        "## Structure Summary",
        ]
    )
    for chapter, data in grouped.items():
        page_range = "?" if data["start_page"] is None else f'{data["start_page"]}-{data["end_page"]}'
        lines.extend(
            [
                "",
                f"## {chapter}",
                f"Pages {page_range}",
                "Chunks:",
            ]
        )
        for section in data["sections"]:
            section_title = section["section_title"]
            chunk_pages = "?" if section["start_page"] is None else f'{section["start_page"]}-{section["end_page"]}'
            lines.append(f'- `{section["file_name"]}` - {section_title} ({chunk_pages})')
        headings = [heading for section in data["sections"] for heading in section["headings"]]
        if headings:
            lines.append("Headings:")
            for heading in headings[:10]:
                lines.append(f"- {heading}")
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Build a deterministic outline from converted chunks.")
    parser.add_argument("--source-id", required=True, help="Canonical source id for the run")
    parser.add_argument("--source-file", help="Physical source file path used for package verification")
    parser.add_argument("--converted-dir", required=True, help="Path to Converted_Sources/<source>/")
    parser.add_argument("--run-dir", required=True, help="Path to runs/ingest_<source>_<date>/")
    args = parser.parse_args()

    converted_dir = Path(args.converted_dir).resolve()
    run_dir = Path(args.run_dir).resolve()
    if not converted_dir.exists():
        raise FileNotFoundError(f"Converted dir not found: {converted_dir}")
    run_dir.mkdir(parents=True, exist_ok=True)

    entries = build_outline_entries(converted_dir)
    outline_path = run_dir / "outline.md"
    write_outline(entries, outline_path, args.source_id, source_file=args.source_file or "")
    print(json.dumps({"outline_path": str(outline_path), "entries": len(entries)}))


if __name__ == "__main__":
    main()
