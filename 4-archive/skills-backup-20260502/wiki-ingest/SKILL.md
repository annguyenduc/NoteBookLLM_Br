---
name: wiki-ingest
description: "TRIGGER: ingest, nạp source, add to wiki, process document. Quy trình 2 bước nạp tri thức vào NoteBookLLM_Br wiki, enforce Rule 14/17/20, tạo SOURCE/CONCEPT/ENTITY pages. Do not use for querying or browsing existing wiki pages."
---

# Wiki Ingest Protocol (Local Version)

This skill overrides the global ingest behavior to enforce workspace-specific rules for NoteBookLLM_Br.

## Pre-execution: TRIPLE-VIEW PROTOCOL (Rule 20)
Trước khi tạo hoặc chỉnh sửa bất kỳ tệp tin nào trong `3-resources/wiki/`, agent BẮT BUỘC thực hiện:
1. `view_file` Template tương ứng:
   - `d:\NoteBookLLM_Br\.agent\skills\wiki-ingest\resources\SOURCE_TEMPLATE.md`
   - `d:\NoteBookLLM_Br\.agent\skills\wiki-ingest\resources\CONCEPT_TEMPLATE.md`
   - `d:\NoteBookLLM_Br\.agent\skills\wiki-ingest\resources\ENTITY_TEMPLATE.md`
2. `view_file` Nguồn thô trong `3-resources/raw/sources/` (đảm bảo Rule 14).
3. Chỉ sau khi có 2 tool call trên, mới thực hiện lệnh ghi/sửa file.

## 🔄 Trình tự thực thi bắt buộc (Mandatory Sequence)

Agent KHÔNG ĐƯỢC phép tạo file nếu chưa hoàn thành các bước theo thứ tự sau:

### Bước 0: QUADRUPLE-VIEW GATE (Rule 20 & WIKI_AGENT_GUIDE)
Trước khi ghi bất kỳ file nào, Agent BẮT BUỘC phải thực hiện 3 tool call `view_file` sau để nạp ngữ cảnh:
1.  **Đọc Hướng dẫn Agent**: `view_file d:\NoteBookLLM_Br\.agent\skills\wiki-ingest\resources\WIKI_AGENT_GUIDE.md`.
2.  **Đọc Template**: `view_file` tệp mẫu tương ứng trong thư mục `resources/`.
3.  **Đọc Nguồn thô**: `view_file` tệp nguồn trong `3-resources/raw/sources/`.
*Vi phạm bước này sẽ bị coi là Hallucination (Rule 15).*

### Bước 1: Scan & Identify
Chạy script quét hệ thống:
```powershell
python .agent/skills/wiki-ingest/scripts/wiki_ingest_helper.py --scan
```

### Bước 2: Read & Analyze (Chain-of-Thought)
- Đọc toàn bộ file nguồn.
- Trích xuất các Concepts/Entities nguyên tử.
- Đối soát với Wiki Index để tránh trùng lặp.

### 2. File Naming Standard (Rule 7)
Bắt buộc đặt tên file theo cấu trúc `[DANH_MỤC]_[CHỦ_ĐỀ]_[TÊN_FILE].md`.
- **META**: Dành cho tri thức về LLM Wiki, Quản trị hệ thống (vd: `META_WIKI_Atomic_Methodology.md`).
- **KHMT**: AI_THCS, AI_Tieu_hoc, Python, Scratch, Scratch_Jr, Tynker.
- **Robot**: Codey, GBot, mBot, Rover, Unplugged, xBot.
- **ACAD**: Biology, Math, Physics.

### 🔝 Thứ tự ưu tiên tạo file (Creation Priority)
Để đảm bảo tính toàn vẹn của liên kết (Link Integrity), Agent PHẢI tạo file theo đúng thứ tự:

1.  **Ưu tiên 1 - SOURCE Page**: Luôn luôn tạo trang nguồn trước. Đây là "gốc" của bằng chứng.
2.  **Ưu tiên 2 - CONCEPT / ENTITY Pages**: Tạo sau khi đã có Source. Các trang này phải trỏ link `source:` về trang Source vừa tạo.
3.  **Ưu tiên 3 - SYNTHESIS / QUERY Pages**: Tạo cuối cùng, vì chúng tổng hợp dữ liệu từ nhiều Concept và Source khác nhau.

### 🎯 Chiến lược Ingest (10-15 trang/nguồn)
Theo `WIKI_AGENT_GUIDE`, mỗi nguồn tài liệu mới phải được atomize thành:
- 1 trang `SOURCE_` (Tóm tắt & Phân tích cấu trúc).
- 2-3 trang `ENTITY_` (Công cụ, hệ sinh thái).
- 5-8 trang `CONCEPT_` (Thuật ngữ, kỹ thuật nguyên tử).
- 1-2 trang `SYNTHESIS_` hoặc cập nhật `index.md`.

### 🧠 Nội dung bắt buộc (Content Requirements)
- **4F — Phản tư sư phạm**: Bắt buộc có mục Facts, Feelings, Findings, Futures trong các trang **CONCEPT** và **SYNTHESIS** (không bắt buộc với SOURCE/ENTITY).
- **Mật độ liên kết**: Ít nhất 2 liên kết `[[Wiki_Link]]` nội bộ cho mỗi Atom mới.
- **YAML file_id**: Phải bắt đầu bằng loại thực thể (`CONCEPT_`, `ENTITY_`, `SOURCE_`, `SYNTHESIS_`).
- **SOURCE Page**: Dùng `d:\NoteBookLLM_Br\.agent\skills\wiki-ingest\resources\SOURCE_TEMPLATE.md`.
- **CONCEPT/ENTITY Page**: Dùng `CONCEPT_TEMPLATE.md` hoặc `ENTITY_TEMPLATE.md` trong cùng thư mục resources.
    - **Rule 14 (Source Integrity)**: Phải mở file raw và xác nhận fact. Ghi rõ `Nguồn: [tên file raw] — [section]`.
    - **Rule 17 (Double Examples)**: BẮT BUỘC có khối `## Ví dụ đối chiếu (Rule 17: Double Examples)` gồm:
        1. **Ví dụ từ sách (Original)**: Trích dẫn sát thực tế tài liệu gốc.
        2. **Ứng dụng sư phạm (Pedagogical Application)**: Chuyển đổi sang tình huống dạy học/STEAM/EdTech.

### 4. Finalize & Sync (BẮT BUỘC)
Sau khi tạo xong các file Wiki, chạy script để cập nhật mục lục và vector search:
```powershell
python .agent/skills/wiki-ingest/scripts/wiki_ingest_helper.py --finalize
```

## Reporting Requirement (Rule 18)
Mọi phản hồi sau tool call ghi file phải bao gồm:
```
WRITE REPORT:
  file: "[đường dẫn]"
  operation: "append | patch | create"
  added: "[tóm tắt 1 câu]"
  compliance: "[Rule 20] Đã đối soát Template và Raw thành công."
```

## Non-negotiable Rules
- **Rule 12**: Raw is Immutable.
- **Rule 15**: No Fake Reports.
- **Rule 21**: Self-Audit Integrity Loop (Đọc lại file vừa ghi để đối soát template).
