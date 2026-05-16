import argparse
import json
import shutil
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]
HD_CONVERTER = ROOT_DIR / ".agent" / "skills" / "wiki-hd-convert" / "scripts" / "hd_converter.py"
BUILD_MANIFEST = ROOT_DIR / "scripts" / "ingest" / "build_manifest.py"
BUILD_OUTLINE = ROOT_DIR / "scripts" / "ingest" / "build_outline.py"
PYTHON_BIN = ROOT_DIR / ".venv" / "Scripts" / "python.exe"

STAGES = ["INIT", "CONVERT", "BUILD_MANIFEST", "BUILD_OUTLINE", "PACKAGE_REPORT", "READY_FOR_AUDIT"]


def slugify_source_id(name: str) -> str:
    import re

    slug = re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_").lower()
    return slug or "source"


def log_line(run_dir: Path, message: str):
    logs_dir = run_dir / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().isoformat(timespec="seconds")
    with (logs_dir / "run.log").open("a", encoding="utf-8") as handle:
        handle.write(f"[{timestamp}] {message}\n")


def write_state(run_dir: Path, state: dict):
    (run_dir / "state.json").write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def read_state(run_dir: Path):
    return json.loads((run_dir / "state.json").read_text(encoding="utf-8"))


def detect_converted_dir(source: Path) -> Path:
    return ROOT_DIR / "00_Inbox" / "Converted_Sources" / source.stem


def create_run_dir(source_id: str) -> Path:
    today = date.today().isoformat()
    return ROOT_DIR / "runs" / f"ingest_{source_id}_{today}"


def ensure_run_skeleton(run_dir: Path):
    for folder in ("chunks", "reports", "logs", "failed_queue"):
        (run_dir / folder).mkdir(parents=True, exist_ok=True)


def init_state(source: Path, mode: str, chunk_size: int, ocr: str, max_workers: int, engine: str, run_dir: Path):
    return {
        "source_id": slugify_source_id(source.stem),
        "source_file": str(source),
        "run_dir": str(run_dir),
        "stage": "INIT",
        "mode": mode,
        "engine": engine,
        "chunk_size": chunk_size,
        "ocr": ocr,
        "max_workers": max_workers,
        "converted_dir": str(detect_converted_dir(source)),
        "completed_batches": [],
        "failed_batches": [],
        "completed_chunks": [],
        "failed_chunks": [],
        "last_error": None,
    }


def run_subprocess(args, run_dir: Path, state: dict, stage_name: str):
    log_line(run_dir, f"START {stage_name}: {' '.join(str(arg) for arg in args)}")
    result = subprocess.run(args, capture_output=True, text=True, encoding="utf-8")
    if result.stdout:
        log_line(run_dir, result.stdout.strip())
    if result.stderr:
        log_line(run_dir, result.stderr.strip())
    if result.returncode != 0:
        state["last_error"] = f"{stage_name} failed: {result.stderr.strip() or result.stdout.strip()}"
        write_state(run_dir, state)
        raise RuntimeError(state["last_error"])
    return result


def stage_convert(run_dir: Path, state: dict):
    converted_dir = Path(state["converted_dir"])
    chunk_files = list(converted_dir.glob("RAW_*.md")) if converted_dir.exists() else []
    if chunk_files:
        log_line(run_dir, f"CONVERT reuse existing converted output: {converted_dir}")
    else:
        args = [
            str(PYTHON_BIN),
            str(HD_CONVERTER),
            state["source_file"],
            "--output",
            "00_Inbox/Converted_Sources",
            "--chunk-size",
            str(state["chunk_size"]),
        ]
        run_subprocess(args, run_dir, state, "CONVERT")
    state["stage"] = "CONVERT"
    write_state(run_dir, state)


def stage_build_manifest(run_dir: Path, state: dict):
    args = [
        str(PYTHON_BIN),
        str(BUILD_MANIFEST),
        "--source",
        state["source_file"],
        "--converted-dir",
        state["converted_dir"],
        "--run-dir",
        str(run_dir),
        "--chunk-size",
        str(state["chunk_size"]),
        "--ocr",
        state["ocr"],
        "--mode",
        state["mode"],
    ]
    run_subprocess(args, run_dir, state, "BUILD_MANIFEST")
    state["stage"] = "BUILD_MANIFEST"
    write_state(run_dir, state)


def stage_build_outline(run_dir: Path, state: dict):
    args = [
        str(PYTHON_BIN),
        str(BUILD_OUTLINE),
        "--source-id",
        state["source_id"],
        "--converted-dir",
        state["converted_dir"],
        "--run-dir",
        str(run_dir),
    ]
    run_subprocess(args, run_dir, state, "BUILD_OUTLINE")
    state["stage"] = "BUILD_OUTLINE"
    write_state(run_dir, state)


def stage_package_report(run_dir: Path, state: dict):
    reports_dir = run_dir / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    summary_path = reports_dir / "summary.md"
    lines = [
        f"# Ingest Run Summary - {state['source_id']}",
        "",
        f"- Source file: `{state['source_file']}`",
        f"- Converted dir: `{state['converted_dir']}`",
        f"- Stage: `READY_FOR_AUDIT`",
        f"- Mode: `{state['mode']}`",
        f"- Engine: `{state['engine']}`",
        f"- Chunk size: `{state['chunk_size']}`",
        f"- OCR: `{state['ocr']}`",
        "",
        "Artifacts:",
        f"- `state.json`",
        f"- `manifest.md`",
        f"- `outline.md`",
        f"- `logs/run.log`",
        "",
        "Boundary:",
        "- Phase A stopped before audit/promote.",
        "- No direct write to `3-resources/raw_ingest` was performed.",
    ]
    summary_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    state["stage"] = "PACKAGE_REPORT"
    write_state(run_dir, state)
    log_line(run_dir, f"PACKAGE_REPORT wrote {summary_path}")


def copy_chunk_references(run_dir: Path, state: dict):
    converted_dir = Path(state["converted_dir"])
    chunks_dir = run_dir / "chunks"
    for chunk in sorted(converted_dir.glob("RAW_*.md")):
        if chunk.name.endswith("_MANIFEST.md"):
            continue
        target = chunks_dir / chunk.name
        if not target.exists():
            shutil.copy2(chunk, target)


def execute_run(run_dir: Path, state: dict):
    current_stage = state["stage"]
    if current_stage == "INIT":
        stage_convert(run_dir, state)
        current_stage = state["stage"]
    if current_stage == "CONVERT":
        copy_chunk_references(run_dir, state)
        stage_build_manifest(run_dir, state)
        current_stage = state["stage"]
    if current_stage == "BUILD_MANIFEST":
        stage_build_outline(run_dir, state)
        current_stage = state["stage"]
    if current_stage == "BUILD_OUTLINE":
        stage_package_report(run_dir, state)
        current_stage = state["stage"]
    if current_stage == "PACKAGE_REPORT":
        state["stage"] = "READY_FOR_AUDIT"
        write_state(run_dir, state)
        log_line(run_dir, "READY_FOR_AUDIT reached")


def main():
    parser = argparse.ArgumentParser(description="Phase A ingest runner for run-package orchestration.")
    parser.add_argument("--source", help="Path to the source PDF")
    parser.add_argument("--chunk-size", type=int, default=15, help="Chunk size for fallback page windows")
    parser.add_argument("--mode", choices=["dry-run", "review", "apply"], default="review", help="Runner mode")
    parser.add_argument("--resume", help="Resume an existing run directory")
    parser.add_argument("--max-workers", type=int, default=1, help="Reserved for future use; Phase A expects 1")
    parser.add_argument("--ocr", choices=["off", "auto", "force"], default="off", help="OCR mode recorded for this run")
    parser.add_argument("--engine", choices=["docling", "pymupdf", "auto"], default="docling", help="Conversion engine label for the run")
    args = parser.parse_args()

    if args.resume:
        run_dir = Path(args.resume).resolve()
        state = read_state(run_dir)
        ensure_run_skeleton(run_dir)
        execute_run(run_dir, state)
        print(json.dumps({"run_dir": str(run_dir), "stage": read_state(run_dir)["stage"]}))
        return

    if not args.source:
        raise SystemExit("--source is required unless --resume is used")

    source = Path(args.source).resolve()
    if not source.exists():
        raise FileNotFoundError(f"Source file not found: {source}")

    run_dir = create_run_dir(slugify_source_id(source.stem))
    run_dir.mkdir(parents=True, exist_ok=True)
    ensure_run_skeleton(run_dir)
    state = init_state(source, args.mode, args.chunk_size, args.ocr, args.max_workers, args.engine, run_dir)
    write_state(run_dir, state)
    log_line(run_dir, f"INIT source={source}")
    execute_run(run_dir, state)
    print(json.dumps({"run_dir": str(run_dir), "stage": read_state(run_dir)["stage"]}))


if __name__ == "__main__":
    main()
