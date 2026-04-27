import argparse
import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path
import re
from typing import Any, Dict, List

# Add project root to sys.path to import libs
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from libs.core.llm_client import call_worker
from libs.core.logger import get_logger


logger = get_logger("brain_lint")

BRAIN_DISTILLED_DIR = project_root / "brain" / "distilled"
REPORT_PATH = project_root / "brain" / "lint_report.md"
CACHE_PATH = project_root / "brain" / "process" / "storage" / "cache" / "brain_lint_manifest.json"
PROMPT_VERSION = "brain-lint-v1"
LINT_MODEL = "fast-engine"
CONTENT_CHAR_LIMIT = 3000


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Incremental brain lint with cache.")
    parser.add_argument("--full", action="store_true", help="Ignore cache and lint all files again.")
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Maximum number of files to send to the LLM in this run.",
    )
    parser.add_argument(
        "--report-changed-only",
        action="store_true",
        help="Write report entries only for files freshly linted or deferred this run.",
    )
    return parser.parse_args()


def get_wiki_files() -> List[Path]:
    """Get all markdown files in brain/distilled and brain/wiki, sorted for stable output."""
    BRAIN_ATOMS_DIR = project_root / "brain" / "atoms"
    files = list(BRAIN_DISTILLED_DIR.glob("*.md")) + list(BRAIN_ATOMS_DIR.glob("*.md"))
    return sorted(files, key=lambda path: path.name.lower())


def read_file_content(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def file_sha256(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def check_broken_links(content: str, all_filenames: List[str]) -> List[str]:
    """Check for wikilinks that do not resolve to an existing note."""
    links = re.findall(r"\[\[(.*?)\]\]", content)
    broken = []
    for link in links:
        if link not in all_filenames and f"{link}.md" not in all_filenames:
            broken.append(link)
    return broken


def load_cache() -> Dict[str, Any]:
    if not CACHE_PATH.exists():
        return {"prompt_version": PROMPT_VERSION, "model": LINT_MODEL, "files": {}}
    try:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except Exception as exc:
        logger.warning(f"Cache manifest unreadable, rebuilding from scratch: {exc}")
        return {"prompt_version": PROMPT_VERSION, "model": LINT_MODEL, "files": {}}


def save_cache(cache: Dict[str, Any]) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(
        json.dumps(cache, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )


def build_prompt(filename: str, content: str) -> str:
    return f"""
Báº¡n lÃ  má»™t chuyÃªn gia quáº£n lÃ½ tri thá»©c (Knowledge Librarian).
HÃ£y kiá»ƒm tra tá»‡p tin Wiki sau Ä‘Ã¢y Ä‘á»ƒ tÃ¬m:
1. MÃ¢u thuáº«n logic (Contradictions).
2. ThÃ´ng tin láº·p láº¡i khÃ´ng cáº§n thiáº¿t.
3. CÃ¡c lá»— há»•ng kiáº¿n thá»©c (Knowledge Gaps) quan trá»ng.

TÃªn tá»‡p: {filename}
Ná»™i dung:
---
{content}
---

HÃ£y tráº£ vá» bÃ¡o cÃ¡o ngáº¯n gá»n báº±ng tiáº¿ng Viá»‡t. Náº¿u khÃ´ng cÃ³ lá»—i, hÃ£y ghi "OK".
""".strip()


def lint_file_content(filename: str, content: str) -> str:
    messages = [{"role": "user", "content": build_prompt(filename, content)}]
    try:
        return call_worker(messages, model=LINT_MODEL)
    except Exception as exc:
        return f"Lá»—i gá»i LLM: {exc}"


def should_relint(
    cache_entry: Dict[str, Any] | None,
    file_hash: str,
    file_stat: Any,
    full: bool,
    cache_prompt_version: str,
    cache_model: str,
) -> bool:
    if full or cache_entry is None:
        return True
    if cache_prompt_version != PROMPT_VERSION or cache_model != LINT_MODEL:
        return True
    if cache_entry.get("sha256") != file_hash:
        return True
    if cache_entry.get("mtime") != file_stat.st_mtime:
        return True
    if cache_entry.get("size") != file_stat.st_size:
        return True
    if "lint_result" not in cache_entry:
        return True
    if cache_entry.get("analysis_status") == "deferred":
        return True
    return False


def format_timestamp(value: str | None) -> str:
    return value or "N/A"


def write_report(report_lines: List[str]) -> None:
    REPORT_PATH.write_text("\n".join(report_lines) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    logger.info("START: Brain Linting...")

    files = [path for path in get_wiki_files() if not path.name.startswith("_")]
    all_filenames = [f.name for f in files]

    cache = load_cache()
    cache_files = cache.setdefault("files", {})
    cached_prompt_version = cache.get("prompt_version")
    cached_model = cache.get("model")

    file_records: List[Dict[str, Any]] = []
    stale_paths = {path for path in cache_files.keys()}
    for file_path in files:
        stale_paths.discard(file_path.name)
        file_stat = file_path.stat()
        content = read_file_content(file_path)
        broken_links = check_broken_links(content, all_filenames)
        file_hash = file_sha256(content)
        cache_entry = cache_files.get(file_path.name)
        needs_llm = should_relint(
            cache_entry=cache_entry,
            file_hash=file_hash,
            file_stat=file_stat,
            full=args.full,
            cache_prompt_version=cached_prompt_version,
            cache_model=cached_model,
        )
        file_records.append(
            {
                "path": file_path,
                "name": file_path.name,
                "mtime": file_stat.st_mtime,
                "size": file_stat.st_size,
                "sha256": file_hash,
                "content": content,
                "broken_links": broken_links,
                "cache_entry": cache_entry or {},
                "needs_llm": needs_llm,
            }
        )

    for stale_path in stale_paths:
        cache_files.pop(stale_path, None)

    changed_records = sorted(
        [record for record in file_records if record["needs_llm"]],
        key=lambda record: record["mtime"],
        reverse=True,
    )
    llm_budget = args.limit if args.limit is not None and args.limit >= 0 else None
    selected_names = {
        record["name"] for record in (changed_records[:llm_budget] if llm_budget is not None else changed_records)
    }

    report_lines = [
        f"# Brain Lint Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        f"- Mode: {'full' if args.full else 'incremental'}",
        f"- Files scanned: {len(file_records)}",
        f"- Files needing LLM refresh: {len(changed_records)}",
        f"- Files sent to LLM this run: {len(selected_names)}",
        f"- Prompt version: {PROMPT_VERSION}",
        f"- Model: {LINT_MODEL}",
        "",
    ]

    for record in file_records:
        cached = record["cache_entry"]
        if record["needs_llm"] and record["name"] in selected_names:
            # Sá»­a lá»—i UnicodeEncodeError trÃªn Windows Terminal báº±ng cÃ¡ch xÃ³a kÃ½ tá»± Tiáº¿ng Viá»‡t khi in log
            safe_name = record["name"].encode("ascii", "ignore").decode()
            logger.info(f"LINTING: {safe_name}")
            lint_result = lint_file_content(record["name"], record["content"][:CONTENT_CHAR_LIMIT])
            analysis_status = "fresh"
            analyzed_at = datetime.now().isoformat(timespec="seconds")
        elif record["needs_llm"]:
            lint_result = cached.get("lint_result", "Deferred: file changed but was not linted in this run.")
            analysis_status = "deferred"
            analyzed_at = cached.get("analyzed_at")
        else:
            lint_result = cached.get("lint_result", "Cached result missing.")
            analysis_status = "cached"
            analyzed_at = cached.get("analyzed_at")

        cache_files[record["name"]] = {
            "path": str(record["path"].relative_to(project_root)),
            "mtime": record["mtime"],
            "size": record["size"],
            "sha256": record["sha256"],
            "broken_links": record["broken_links"],
            "lint_result": lint_result,
            "model_used": LINT_MODEL,
            "prompt_version": PROMPT_VERSION,
            "analysis_status": analysis_status,
            "analyzed_at": analyzed_at,
        }

        include_in_report = True
        if args.report_changed_only:
            include_in_report = analysis_status in {"fresh", "deferred"}
        if not include_in_report:
            continue

        report_lines.append(f"## {record['name']}")
        report_lines.append(f"- Analysis status: {analysis_status}")
        report_lines.append(f"- Last analyzed: {format_timestamp(analyzed_at)}")
        if record["broken_links"]:
            report_lines.append(f"- Broken Links: {', '.join(record['broken_links'])}")
        else:
            report_lines.append("- Broken Links: None")
        report_lines.append(f"- AI Analysis:\n{lint_result}\n")
        report_lines.append("---")

    cache["prompt_version"] = PROMPT_VERSION
    cache["model"] = LINT_MODEL
    cache["last_run_at"] = datetime.now().isoformat(timespec="seconds")
    save_cache(cache)
    write_report(report_lines)

    logger.info(f"DONE! Report saved at: {REPORT_PATH}")
    logger.info(f"Cache manifest saved at: {CACHE_PATH}")


if __name__ == "__main__":
    main()

