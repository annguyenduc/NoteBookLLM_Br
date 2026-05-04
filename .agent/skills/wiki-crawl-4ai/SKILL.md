---
name: wiki-crawl-4ai
description: Use when high-fidelity, structured Markdown is required from web sources for Wiki ingestion, particularly for RAG or complex document hierarchies.
---

# Wiki Crawl (Crawl4AI Engine)

## Overview
Skill này sử dụng **Crawl4AI** để thu thập dữ liệu từ website và chuyển đổi trực tiếp thành Markdown "LLM-ready". Đây là công cụ ưu tiên cho việc nạp tri thức vào Wiki vì nó bảo toàn cấu trúc phân cấp (headers, tables, links) tốt hơn các công cụ scrape thông thường.

## When to Use
- ✅ Khi cần nạp tài liệu kỹ thuật có cấu trúc phức tạp (headers, bảng biểu).
- ✅ Khi muốn tiết kiệm Token bằng cách loại bỏ rác (menu, footer) ngay từ bước cào.
- ✅ Khi chuẩn bị dữ liệu cho quy trình `/ingest` để tạo các Atomic Nodes chất lượng cao.
- ❌ KHÔNG dùng nếu chỉ cần tìm kiếm nhanh hoặc kiểm tra tồn tại của một trang (Dùng `wiki-web-scrape`).

## Core Pattern (Medium Freedom)
Quy trình tập trung vào việc tạo ra file nguồn sạch nhất có thể để giảm tải cho bước xử lý sau.

### 1. Thực thi Crawl
Luôn lưu kết quả vào `00_Inbox/` để thực hiện audit trước khi nạp chính thức.

```powershell
python .agent/skills/wiki-crawl-4ai/scripts/crawl4ai_run.py --url [URL] --output 00_Inbox/WEBSITE_[Name].md
```

## Quick Reference

| Tham số | Ý nghĩa |
|---|---|
| Engine | Crawl4AI (Playwright based) |
| Output Format | Structured Markdown |
| Destination | `00_Inbox/` |
| Feature | Auto-cleaning, Metadata extraction |

## Red Flags - STOP and Re-evaluate
- **"Dùng Lightpanda cho nhanh"**: Nếu mục tiêu là `ingest`, dùng Lightpanda sẽ làm tăng token dọn dẹp (Cleaning friction).
- **"Markdown quá dài"**: Crawl4AI đã tự động cắt bỏ rác, nếu vẫn dài là do nội dung gốc phong phú -> Giữ nguyên để bảo toàn tri thức.

## Rationalization Table
| Excuse | Reality |
|---|---|
| "Lightpanda nhanh hơn" | Nhanh lúc fetch nhưng chậm lúc xử lý. Crawl4AI "chậm" hơn vài giây nhưng tiết kiệm 10 phút dọn dẹp thủ công. |
| "Markdown không cần thiết" | Headers và Tables là "xương sống" để Agent phân tách Atomic Nodes chính xác. |

## Next Step
Sau khi có file Markdown sạch, sử dụng lệnh `/ingest [file_path]` để bắt đầu quy trình **Red-Green-Refactor** nạp tri thức vào Wiki.
