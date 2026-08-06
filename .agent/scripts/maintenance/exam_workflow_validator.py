from __future__ import annotations

import argparse
import json
import pathlib
import re
from typing import Any

PRACTICAL_HEADING_RE = re.compile(r"^## \*\*Bài tập\s+\d+\s*:", re.MULTILINE)
VIDEO_DELIVERABLE_RE = re.compile(r"video demo", re.IGNORECASE)
CODE_DELIVERABLE_RE = re.compile(r"\.sb3|\.ino|\.py|\.js|file dự án|project file", re.IGNORECASE)
CODE_FILE_SUFFIXES = {".sb3", ".xml", ".ino", ".py", ".js", ".json"}
VIDEO_FILE_SUFFIXES = {".mp4", ".mov", ".avi", ".webm", ".gif"}
LOADABLE_PROJECT_SUFFIXES = {".sb3", ".json"}


def _read_text(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


def _extract_practical_sections(text: str) -> list[str]:
    matches = list(PRACTICAL_HEADING_RE.finditer(text))
    sections: list[str] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append(text[start:end])
    return sections


def _collect_code_image_checks(media_files: list[pathlib.Path]) -> list[dict[str, Any]]:
    by_stem: dict[str, set[str]] = {}
    for path in media_files:
        by_stem.setdefault(path.stem, set()).add(path.suffix.lower())

    checks: list[dict[str, Any]] = []
    for stem, suffixes in sorted(by_stem.items()):
        # Current exam packages keep the rendered image and source xml under the same stem.
        if ".png" not in suffixes or ".xml" not in suffixes:
            continue
        loadable_suffixes = sorted(suffix for suffix in suffixes if suffix in LOADABLE_PROJECT_SUFFIXES)
        checks.append(
            {
                "asset_stem": stem,
                "has_loadable_program": bool(loadable_suffixes),
                "loadable_suffixes": loadable_suffixes,
            }
        )
    return checks


def validate_exam_package(exam_path: pathlib.Path, media_dir: pathlib.Path) -> dict[str, Any]:
    text = _read_text(exam_path)
    practicals = _extract_practical_sections(text)
    media_files = [path for path in media_dir.rglob("*") if path.is_file()] if media_dir.exists() else []
    code_files = [path for path in media_files if path.suffix.lower() in CODE_FILE_SUFFIXES]
    video_files = [path for path in media_files if path.suffix.lower() in VIDEO_FILE_SUFFIXES]
    loadable_project_files = [path for path in media_files if path.suffix.lower() in LOADABLE_PROJECT_SUFFIXES]
    code_image_checks = _collect_code_image_checks(media_files)
    missing_loadable_programs = [item["asset_stem"] for item in code_image_checks if not item["has_loadable_program"]]

    practical_checks = []
    for index, section in enumerate(practicals, start=1):
        practical_checks.append(
            {
                "practical_number": index,
                "requires_video_demo": bool(VIDEO_DELIVERABLE_RE.search(section)),
                "requires_code_deliverable": bool(CODE_DELIVERABLE_RE.search(section)),
            }
        )

    return {
        "exam_path": str(exam_path),
        "media_dir": str(media_dir),
        "practical_count": len(practicals),
        "all_practicals_require_video_demo": all(item["requires_video_demo"] for item in practical_checks)
        if practical_checks
        else False,
        "all_practicals_require_code_deliverable": all(item["requires_code_deliverable"] for item in practical_checks)
        if practical_checks
        else False,
        "media_has_physical_code_sample": bool(code_files),
        "media_code_file_count": len(code_files),
        "media_video_file_count": len(video_files),
        "media_loadable_project_file_count": len(loadable_project_files),
        "code_files": [path.name for path in code_files],
        "video_files": [path.name for path in video_files],
        "loadable_project_files": [path.name for path in loadable_project_files],
        "all_code_images_have_loadable_program": all(item["has_loadable_program"] for item in code_image_checks)
        if code_image_checks
        else True,
        "missing_loadable_programs": missing_loadable_programs,
        "code_image_checks": code_image_checks,
        "practical_checks": practical_checks,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("exam_path", type=pathlib.Path)
    parser.add_argument("media_dir", type=pathlib.Path)
    args = parser.parse_args()

    report = validate_exam_package(args.exam_path, args.media_dir)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
