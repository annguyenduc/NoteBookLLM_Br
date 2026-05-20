from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DOCLING_PYTHON = ROOT / ".venv" / "Scripts" / "python.exe"
DEFAULT_DOCLING_SCRIPT = ROOT / ".agent" / "skills" / "wiki-hd-convert" / "scripts" / "hd_converter.py"
DEFAULT_DOCLING_PYTHONPATH = ROOT / ".venv" / "Lib" / "site-packages"
DEFAULT_MIN_OUTPUT_BYTES = 64


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Benchmark one PDF conversion run for Docling.")
    parser.add_argument("--tool", default="docling", choices=["docling"], help="Conversion tool to invoke.")
    parser.add_argument("--input", required=True, help="Path to the source PDF.")
    parser.add_argument(
        "--page-range",
        default="",
        help="Optional 1-based inclusive page range, e.g. 1-5 or 3. Empty means full document.",
    )
    parser.add_argument("--output", required=True, help="Normalized markdown output path to write.")
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=15,
        help="Docling chunk size forwarded to hd_converter.py.",
    )
    parser.add_argument(
        "--min-output-bytes",
        type=int,
        default=DEFAULT_MIN_OUTPUT_BYTES,
        help="Minimum markdown size before treating a run as false_success.",
    )
    parser.add_argument("--docling-python", default=str(DEFAULT_DOCLING_PYTHON), help="Path to Docling Python runtime.")
    parser.add_argument("--docling-script", default=str(DEFAULT_DOCLING_SCRIPT), help="Path to Docling wrapper script.")
    parser.add_argument(
        "--docling-pythonpath",
        default=str(DEFAULT_DOCLING_PYTHONPATH),
        help="Optional PYTHONPATH for Docling imports when the original venv launcher is broken.",
    )
    return parser.parse_args()


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def parse_page_range(spec: str) -> tuple[int, int] | None:
    cleaned = spec.strip()
    if not cleaned:
        return None
    if "-" in cleaned:
        start_text, end_text = cleaned.split("-", 1)
        start = int(start_text)
        end = int(end_text)
    else:
        start = end = int(cleaned)
    if start < 1 or end < start:
        raise ValueError(f"Invalid page range: {spec}")
    return start, end


def slice_pdf_if_needed(input_pdf: Path, page_range: tuple[int, int] | None, temp_dir: Path) -> tuple[Path, dict]:
    if page_range is None:
        return input_pdf, {"page_range_requested": "", "page_range_applied": "", "pages_tested": None}

    try:
        import fitz
    except ImportError as exc:
        raise RuntimeError("PyMuPDF (fitz) is required to use --page-range.") from exc

    start, end = page_range
    source = fitz.open(str(input_pdf))
    total_pages = source.page_count
    if start > total_pages:
        raise ValueError(f"Page range starts after document end: {start}>{total_pages}")
    actual_end = min(end, total_pages)

    sliced_pdf = temp_dir / f"{input_pdf.stem}__p{start:03d}_{actual_end:03d}.pdf"
    sliced = fitz.open()
    sliced.insert_pdf(source, from_page=start - 1, to_page=actual_end - 1)
    sliced.save(str(sliced_pdf))
    sliced.close()
    source.close()

    return sliced_pdf, {
        "page_range_requested": f"{start}-{end}",
        "page_range_applied": f"{start}-{actual_end}",
        "pages_tested": actual_end - start + 1,
    }


def run_command(
    command: list[str],
    cwd: Path,
    extra_env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    env = dict(os.environ)
    if extra_env:
        env.update(extra_env)
    return subprocess.run(
        command,
        cwd=str(cwd),
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )


def docling_command(args: argparse.Namespace, sliced_pdf: Path, artifact_root: Path) -> list[str]:
    return [
        str(Path(args.docling_python)),
        str(Path(args.docling_script)),
        str(sliced_pdf),
        "--output",
        str(artifact_root),
        "--chunk-size",
        str(args.chunk_size),
    ]


def find_primary_markdown(artifact_root: Path) -> Path | None:
    markdown_files = sorted(artifact_root.rglob("*.md"))
    if not markdown_files:
        return None

    non_manifest = [path for path in markdown_files if "MANIFEST" not in path.name.upper()]
    candidates = non_manifest or markdown_files
    return max(candidates, key=lambda path: path.stat().st_size)


def copy_primary_output(primary_markdown: Path | None, normalized_output: Path) -> int:
    if primary_markdown is None:
        return 0
    ensure_parent(normalized_output)
    shutil.copy2(primary_markdown, normalized_output)
    return normalized_output.stat().st_size


def build_metadata(
    args: argparse.Namespace,
    input_pdf: Path,
    sliced_pdf: Path,
    artifact_root: Path,
    normalized_output: Path,
    page_info: dict,
    completed: subprocess.CompletedProcess[str],
    runtime_sec: float,
    output_size_bytes: int,
    primary_markdown: Path | None,
) -> dict:
    crash = completed.returncode != 0
    false_success = completed.returncode == 0 and output_size_bytes < args.min_output_bytes
    return {
        "tool": args.tool,
        "input_file": str(input_pdf),
        "slice_file": str(sliced_pdf),
        "page_range_requested": page_info["page_range_requested"],
        "page_range_applied": page_info["page_range_applied"],
        "pages_tested": page_info["pages_tested"],
        "normalized_output": str(normalized_output),
        "artifact_root": str(artifact_root),
        "primary_markdown": str(primary_markdown) if primary_markdown else "",
        "runtime_sec": round(runtime_sec, 3),
        "output_size_bytes": output_size_bytes,
        "returncode": completed.returncode,
        "crash": crash,
        "false_success": false_success,
        "requires_manual_recheck": crash or false_success,
        "stdout_tail": tail_lines(completed.stdout.splitlines(), 20),
        "stderr_tail": tail_lines(completed.stderr.splitlines(), 20),
    }


def tail_lines(lines: Iterable[str], limit: int) -> list[str]:
    collected = list(lines)
    return collected[-limit:]


def write_metadata_files(normalized_output: Path, metadata: dict) -> None:
    json_path = normalized_output.with_suffix(".benchmark.json")
    md_path = normalized_output.with_suffix(".benchmark.md")

    json_path.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    md_lines = [
        "# CONVERT_BENCHMARK_RUN",
        "",
        f"- tool: `{metadata['tool']}`",
        f"- input_file: `{metadata['input_file']}`",
        f"- slice_file: `{metadata['slice_file']}`",
        f"- page_range_requested: `{metadata['page_range_requested']}`",
        f"- page_range_applied: `{metadata['page_range_applied']}`",
        f"- pages_tested: `{metadata['pages_tested']}`",
        f"- normalized_output: `{metadata['normalized_output']}`",
        f"- artifact_root: `{metadata['artifact_root']}`",
        f"- primary_markdown: `{metadata['primary_markdown']}`",
        f"- runtime_sec: `{metadata['runtime_sec']}`",
        f"- output_size_bytes: `{metadata['output_size_bytes']}`",
        f"- returncode: `{metadata['returncode']}`",
        f"- crash: `{metadata['crash']}`",
        f"- false_success: `{metadata['false_success']}`",
        f"- requires_manual_recheck: `{metadata['requires_manual_recheck']}`",
        "",
        "## stdout_tail",
        "```text",
        *metadata["stdout_tail"],
        "```",
        "",
        "## stderr_tail",
        "```text",
        *metadata["stderr_tail"],
        "```",
        "",
    ]
    md_path.write_text("\n".join(md_lines), encoding="utf-8")


def main() -> int:
    args = parse_args()
    if args.docling_pythonpath and args.docling_pythonpath not in sys.path:
        sys.path.insert(0, args.docling_pythonpath)

    input_pdf = Path(args.input).resolve()
    normalized_output = Path(args.output).resolve()

    if not input_pdf.exists():
        print(f"[ERROR] Input PDF not found: {input_pdf}")
        return 1

    ensure_parent(normalized_output)
    artifact_root = normalized_output.parent / f"{normalized_output.stem}__{args.tool}_artifacts"
    artifact_root.mkdir(parents=True, exist_ok=True)

    page_range = parse_page_range(args.page_range)

    with tempfile.TemporaryDirectory() as temp_dir_text:
        temp_dir = Path(temp_dir_text)
        sliced_pdf, page_info = slice_pdf_if_needed(input_pdf, page_range, temp_dir)

        command = docling_command(args, sliced_pdf, artifact_root)
        extra_env = {}
        if args.docling_pythonpath:
            extra_env["PYTHONPATH"] = args.docling_pythonpath
        started = time.perf_counter()
        completed = run_command(command, ROOT, extra_env=extra_env)
        runtime_sec = time.perf_counter() - started

        primary_markdown = find_primary_markdown(artifact_root)
        output_size_bytes = copy_primary_output(primary_markdown, normalized_output)

        metadata = build_metadata(
            args=args,
            input_pdf=input_pdf,
            sliced_pdf=sliced_pdf,
            artifact_root=artifact_root,
            normalized_output=normalized_output,
            page_info=page_info,
            completed=completed,
            runtime_sec=runtime_sec,
            output_size_bytes=output_size_bytes,
            primary_markdown=primary_markdown,
        )
        write_metadata_files(normalized_output, metadata)

    print(json.dumps(metadata, indent=2, ensure_ascii=False))
    return 2 if metadata["false_success"] else (1 if metadata["crash"] else 0)


if __name__ == "__main__":
    sys.exit(main())
