---
name: wiki-web-scrape
description: Use when you need to crawl or scrape technical documentation from URLs at high speed using Lightpanda. This skill acquires raw data only; use wiki-ingest for atomization.
---

# Wiki Web Scrape (Lightpanda Engine)

## Overview
Skill này sử dụng **Lightpanda** (headless browser Rust-based) để thu thập dữ liệu thô từ các website tài liệu kỹ thuật một cách siêu tốc. Đây là công cụ thu thập (Acquisition), không phải công cụ phân rã (Ingestion).

## When to Use
- Khi cần cào dữ liệu từ các trang tài liệu lớn (vd: PyTorch, Pandas, MDN).
- Khi Browser Subagent quá chậm cho việc thu thập hàng loạt.
- Khi cần lưu nội dung trang web thành file `.md` thô vào `00_Inbox/`.

**Dừng lại nếu:**
- Cần tương tác phức tạp (login, kéo thả, captcha) -> Sử dụng `browser_subagent`.
- Cần phân rã tri thức thành các node Concept -> Sử dụng `/ingest` sau khi đã có file thô.

## Core Pattern: Scrape-First
Quy trình chỉ dừng lại ở việc tạo ra file nguồn thô (`raw source`). Việc biến file này thành Wiki Atoms là trách nhiệm của skill `wiki-ingest`.

### 1. Khởi động Lightpanda Server (Terminal)
*Lưu ý: Chỉ thực hiện bởi Main Agent.*
```powershell
wsl /usr/local/bin/lightpanda serve --host 127.0.0.1 --port 9222
```

### 2. Thực thi Scrape
Sử dụng script để trích xuất nội dung văn bản sạch:
```powershell
python .agent/skills/wiki-web-scrape/scripts/lightpanda_scrape.py --url [URL] --output 00_Inbox/WEBSITE_[Name].md
```

## Quick Reference

| Tham số | Ý nghĩa |
|---|---|
| Engine | Lightpanda (via Playwright CDP) |
| Output | `00_Inbox/WEBSITE_*.md` |
| Environment | WSL2 (Debian) |
| Role | Main Agent ONLY |

## Common Mistakes
- **Gộp chung Ingest**: Không cố gắng tạo Concept ngay trong lúc Scrape. Hãy làm sạch dữ liệu thô trước.
- **Dùng sai Agent**: Browser Subagent không chạy được lệnh terminal này.
- **Thiếu prefix**: Mọi file cào từ web BẮT BUỘC có tiền tố `WEBSITE_`.

## Next Step
Sau khi hoàn thành Scrape, hãy sử dụng lệnh `/ingest [file_path]` để bắt đầu quá trình nguyên tử hóa tri thức.
