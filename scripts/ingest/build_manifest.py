import argparse
import json
import re
from datetime import datetime
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]


def slugify_source_id(name: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_").lower()
    return slug or "source"


def extract_page_range(chunk_name: str):
    match = re.search(r"_P(\d+)-(\d+)\.md$", chunk_name)
    if not match:
        return None, None
    return int(match.group(1)), int(match.group(2))


def detect_engine(sample_text: str) -> str:
    if "Structure Mode: chapter>section>page" in sample_text:
        return "docling"
    return "unknown"


def scan_converted_chunks(converted_dir: Path):
    md_files = sorted(p for p in converted_dir.glob("RAW_*.md") if not p.name.endswith("_MANIFEST.md"))
    chunks = []
    for path in md_files:
        start_page, end_page = extract_page_range(path.name)
        sample = path.read_text(encoding="utf-8", errors="replace")[:2000]
        lines = sample.splitlines()
        chunks.append(
            {
                "file_name": path.name,
                "path": str(path),
                "start_page": start_page,
                "end_page": end_page,
                "engine": detect_engine(sample),
                "heading": lines[0].strip("# ").strip() if lines else path.stem,
                "status": "READY",
            }
        )
    return chunks


def build_manifest_data(source: Path, converted_dir: Path, run_dir: Path, chunk_size: int, ocr: str, mode: str):
    chunks = scan_converted_chunks(converted_dir)
    source_id = slugify_source_id(source.stem)
    total_pages = max((chunk["end_page"] or 0 for chunk in chunks), default=0)
    engine = next((chunk["engine"] for chunk in chunks if chunk["engine"] != "unknown"), "unknown")
    return {
        "source_id": source_id,
        "source_file": str(source),
        "converted_dir": str(converted_dir),
        "run_dir": str(run_dir),
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "conversion_engine": engine,
        "chunk_size": chunk_size,
        "ocr": ocr,
        "mode": mode,
        "total_chunks": len(chunks),
        "total_pages": total_pages,
        "chunks": chunks,
    }


def write_manifest(manifest_data: dict, output_path: Path):
    lines = [
        "---",
        f'source_id: "{manifest_data["source_id"]}"',
        f'source_file: "{manifest_data["source_file"]}"',
        f'converted_dir: "{manifest_data["converted_dir"]}"',
        f'run_dir: "{manifest_data["run_dir"]}"',
        f'created_at: "{manifest_data["created_at"]}"',
        f'conversion_engine: "{manifest_data["conversion_engine"]}"',
        f'chunk_size: {manifest_data["chunk_size"]}',
        f'ocr: "{manifest_data["ocr"]}"',
        f'mode: "{manifest_data["mode"]}"',
        f'total_pages: {manifest_data["total_pages"]}',
        f'total_chunks: {manifest_data["total_chunks"]}',
        "---",
        "",
        f'# Manifest - {manifest_data["source_id"]}',
        "",
        "## Source",
        f'- Source file: `{manifest_data["source_file"]}`',
        f'- Converted dir: `{manifest_data["converted_dir"]}`',
        f'- Run dir: `{manifest_data["run_dir"]}`',
        f'- Engine: `{manifest_data["conversion_engine"]}`',
        f'- Chunk size: `{manifest_data["chunk_size"]}`',
        f'- OCR: `{manifest_data["ocr"]}`',
        "",
        "## Chunk Inventory",
        "",
        "| Chunk | Pages | File | Status |",
        "|---|---:|---|---|",
    ]
    for index, chunk in enumerate(manifest_data["chunks"], start=1):
        page_range = "?" if chunk["start_page"] is None else f'{chunk["start_page"]}-{chunk["end_page"]}'
        lines.append(f'| {index:03d} | {page_range} | `{chunk["file_name"]}` | {chunk["status"]} |')
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Build a deterministic run-package manifest from converted chunks.")
    parser.add_argument("--source", required=True, help="Path to the source PDF")
    parser.add_argument("--converted-dir", required=True, help="Path to Converted_Sources/<source>/")
    parser.add_argument("--run-dir", required=True, help="Path to runs/ingest_<source>_<date>/")
    parser.add_argument("--chunk-size", type=int, required=True, help="Chunk size used or requested for conversion")
    parser.add_argument("--ocr", default="off", help="OCR mode recorded for the run")
    parser.add_argument("--mode", default="review", help="Runner mode for this run")
    args = parser.parse_args()

    source = Path(args.source).resolve()
    converted_dir = Path(args.converted_dir).resolve()
    run_dir = Path(args.run_dir).resolve()
    if not source.exists():
        raise FileNotFoundError(f"Source file not found: {source}")
    if not converted_dir.exists():
        raise FileNotFoundError(f"Converted dir not found: {converted_dir}")

    run_dir.mkdir(parents=True, exist_ok=True)
    manifest_data = build_manifest_data(source, converted_dir, run_dir, args.chunk_size, args.ocr, args.mode)
    manifest_path = run_dir / "manifest.md"
    write_manifest(manifest_data, manifest_path)
    print(json.dumps({"manifest_path": str(manifest_path), "source_id": manifest_data["source_id"], "chunks": manifest_data["total_chunks"]}))


if __name__ == "__main__":
    main()
