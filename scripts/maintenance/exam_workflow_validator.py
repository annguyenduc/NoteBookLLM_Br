from __future__ import annotations

import argparse
import json
import pathlib
import re
from typing import Any

PRACTICAL_HEADING_RE = re.compile(r'^## \*\*Bài tập\s+\d+\s*:', re.MULTILINE)
VIDEO_DELIVERABLE_RE = re.compile(r'video demo', re.IGNORECASE)
CODE_DELIVERABLE_RE = re.compile(r'\.sb3|\.ino|\.py|\.js|file dự án|project file', re.IGNORECASE)
CODE_FILE_SUFFIXES = {'.sb3', '.xml', '.ino', '.py', '.js', '.json'}
VIDEO_FILE_SUFFIXES = {'.mp4', '.mov', '.avi', '.webm', '.gif'}


def _read_text(path: pathlib.Path) -> str:
    return path.read_text(encoding='utf-8')


def _extract_practical_sections(text: str) -> list[str]:
    matches = list(PRACTICAL_HEADING_RE.finditer(text))
    sections: list[str] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append(text[start:end])
    return sections


def validate_exam_package(exam_path: pathlib.Path, media_dir: pathlib.Path) -> dict[str, Any]:
    text = _read_text(exam_path)
    practicals = _extract_practical_sections(text)
    media_files = [p for p in media_dir.rglob('*') if p.is_file()] if media_dir.exists() else []
    code_files = [p for p in media_files if p.suffix.lower() in CODE_FILE_SUFFIXES]
    video_files = [p for p in media_files if p.suffix.lower() in VIDEO_FILE_SUFFIXES]

    practical_checks = []
    for index, section in enumerate(practicals, start=1):
        practical_checks.append({
            'practical_number': index,
            'requires_video_demo': bool(VIDEO_DELIVERABLE_RE.search(section)),
            'requires_code_deliverable': bool(CODE_DELIVERABLE_RE.search(section)),
        })

    return {
        'exam_path': str(exam_path),
        'media_dir': str(media_dir),
        'practical_count': len(practicals),
        'all_practicals_require_video_demo': all(item['requires_video_demo'] for item in practical_checks) if practical_checks else False,
        'all_practicals_require_code_deliverable': all(item['requires_code_deliverable'] for item in practical_checks) if practical_checks else False,
        'media_has_physical_code_sample': bool(code_files),
        'media_code_file_count': len(code_files),
        'media_video_file_count': len(video_files),
        'code_files': [p.name for p in code_files],
        'video_files': [p.name for p in video_files],
        'practical_checks': practical_checks,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('exam_path', type=pathlib.Path)
    parser.add_argument('media_dir', type=pathlib.Path)
    args = parser.parse_args()

    report = validate_exam_package(args.exam_path, args.media_dir)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())