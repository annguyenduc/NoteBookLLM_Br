---
name: wiki-rebuild
description: "TRIGGER: rebuild, sync index, update backlinks, refresh graph. Đồng bộ hóa cấu trúc hệ thống: cập nhật index.md, danh sách tag và tệp dữ liệu backlinks ngầm. Đảm bảo đồ thị tri thức luôn khớp với dữ liệu thực tế."
---

# Wiki Rebuild Protocol

Năng lực duy trì hạ tầng (Infrastructure Maintenance).

## Step 1: Index Sync
- Tự động liệt kê mọi file `.md` trong các thư mục con của `3-resources/wiki/`.
- Cập nhật vào `3-resources/wiki/index.md` theo đúng phân loại (Concepts, Entities, Sources...).

## Step 2: Backlink Generation
- Duyệt toàn bộ vault để tìm các kết nối wikilink.
- Cập nhật tệp `_backlinks.json` (nếu dùng) hoặc append mục Backlinks vào cuối mỗi file md.

## Step 3: Map/Tag Refresh
- Cập nhật danh sách các `#tags` đang được sử dụng trong hệ thống.
- Đảm bảo tính nhất quán của cây thư mục và các tệp README.

## Tooling
```powershell
# Thực hiện sync toàn bộ hệ thống (khi đã hoàn thiện logic)
python .agent/skills/wiki-rebuild/scripts/sync_engine.py
```
