# scout.md — Rules for @scout

> Áp dụng khi: @scout được gọi cho /ingest, phân tích raw file, tạo Scout Analysis.
> Luôn đọc CORE.md trước. Tra cứu thêm: [[GEMINI.md]]

---

## R10 — STRICT URL INGESTION
**CẤM** dùng `sub_browser` hoặc trình duyệt mặc định để đọc tài liệu web.
BẮT BUỘC dùng `.agent/skills/wiki-web-scrape` (static) hoặc `.agent/skills/wiki-crawl-4ai` (screenshot)
để lưu bản nháp vào `00_Inbox/` TRƯỚC KHI tạo Atom.

## R11 — DENSITY FILTER
**KHÔNG tạo Atom** cho file < 200 bytes — đây là nhiễu, không phải tri thức.
Ngoài dung lượng, đánh giá thêm **Knowledge Density**: không chấp nhận Atom chỉ chứa định nghĩa hời hợt
mà không có phân tích sâu hoặc ví dụ minh họa.

## R13 — ATOM LIFECYCLE
Mọi Atom do @scout tạo ra mặc định `status = DRAFT`.
@scout **không được** tự ý set `VERIFIED` hay `SYNTHESIZED`.

## R24 — LOCAL AI AUDIT TRIGGER
Sau mỗi chunk phân tích, @scout **PHẢI** gọi `gap_check.py` thủ công trước khi báo "User Approved".
```bash
python .agent/skills/wiki-ingest/scripts/gap_check.py \
  --source "[SOURCE_NAME]" --chunk [N] --atoms '[JSON_LIST]'
```

## R25 — NON-BLOCKING
Nếu Ollama offline hoặc `gemma3:4b` lỗi → ghi WARNING và **TIẾP TỤC**.
**CẤM block** pipeline chính vì trạng thái của local AI.

---
*scout.md — 5 rules cho @scout. Nguồn: [[GEMINI.md#R10]], [[GEMINI.md#R11]], [[GEMINI.md#R13]], [[GEMINI.md#R24]], [[GEMINI.md#R25]]*
