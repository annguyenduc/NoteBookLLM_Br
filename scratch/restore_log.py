import os

log_path = r"d:\NoteBookLLM_Br\3-resources\wiki\log.md"

# Nội dung đúng cần ghi vào cuối file (bắt đầu từ vị trí lỗi)
correct_entries = """## [2026-05-03 14:26] REFACTOR | @engineer | Refactor Rebuilding Wiki skill tuân thủ chuẩn V3.2 (CSO & TDD).
- File: .agent/skills/wiki-rebuild/SKILL.md
- Lý do: Nâng cấp cơ sở hạ tầng Smart Spine và chuẩn hóa mô tả kích hoạt.

## [2026-05-03 14:26] REFACTOR | @librarian | Refactor Querying Wiki skill chuẩn V3.2.
- File: .agent/skills/wiki-query/SKILL.md
- Lý do: Tối ưu hóa truy vấn bằng Smart Spine FTS5.

## [2026-05-03 14:26] REFACTOR | @scout | Refactor Ingesting Wiki skill chuẩn V3.2.
- File: .agent/skills/wiki-ingest/SKILL.md
- Lý do: Tích hợp giao thức RGR và Magika routing.

## [2026-05-03 14:27] REFACTOR | @librarian | Refactor Absorbing Wiki skill chuẩn V3.2.
- File: .agent/skills/wiki-absorb/SKILL.md
- Lý do: Tích hợp cơ chế Wiki-Council xử lý mâu thuẫn tri thức.

## [2026-05-03 14:27] REFACTOR | @auditor | Refactor Cleaning Wiki skill chuẩn V3.2.
- File: .agent/skills/wiki-cleanup/SKILL.md
- Lý do: Tự động hóa Audit bằng Knowledge Graph.

## [2026-05-03 14:35] CREATE | @engineer | Triển khai skill wiki-crawl-4ai (Crawl4AI) tối ưu cho Ingestion.
- File: .agent/skills/wiki-crawl-4ai/SKILL.md
- Lý do: Cung cấp engine cào dữ liệu có cấu trúc Markdown sạch cho Wiki 2.0.
"""

# Đọc toàn bộ nội dung hiện tại
with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

# Tìm dòng bắt đầu lỗi (dựa trên timestamp 14:26)
final_lines = []
for line in lines:
    if "## [2026-05-03 14:26]" in line:
        break
    final_lines.append(line)

# Ghi lại file với phần đầu sạch + phần đuôi đã sửa
with open(log_path, "w", encoding="utf-8") as f:
    f.writelines(final_lines)
    f.write(correct_entries)

print("Đã phục hồi log.md về chuẩn UTF-8.")
