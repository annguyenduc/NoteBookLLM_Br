---
file_id: WIKI_REVIEW_QUEUE
title: "Hòm thư chờ duyệt (Async Review Queue)"
category: "Governance"
prefix: "WIKI"
tags: ["Review", "Audit", "Quality_Control"]
status: "verified"
created: "2026-05-01"
last_updated: "2026-05-01"
---

# 🚩 Hòm thư chờ duyệt (Async Review Queue)

Tài liệu này quản trị các vấn đề tri thức phát hiện bởi Agents, chờ User đưa ra quyết định cuối cùng (Nashsu Pattern).

## 🔴 Mâu thuẫn Tri thức (Conflicts)
*Hiện chưa phát hiện mâu thuẫn trực tiếp giữa các nguồn.*

## 🟡 Lỗ hổng & Cần xác minh (Gaps & Verification)
1. **[QMD Index]**: `qmd embed` báo thành công nhưng hashes không đổi. Cần kiểm tra xem tri thức META mới nạp đã thực sự được vector hóa chưa.
2. **[Rule Migration]**: Cần kiểm tra xem các Skill nội bộ đã bao quát hết 100% logic của file `METAS_AGENTS.md` (263 dòng) cũ chưa.
3. **[Naming Standard]**: Một số file cũ trong `wiki/concepts/` vẫn mang prefix `WIKI_` thay vì `CONCEPT_`. 
   - *Hành động đề xuất*: Chạy script rename hàng loạt.

## 🟢 Đã xử lý (Resolved)
- ✅ Đã di trú Rule cốt lõi vào `GEMINI.md`.
- ✅ Đã đóng gói Skill `wiki-ingest`, `wiki-lint`, `wiki-query`.

---
## Nhật ký Audit nhanh (v1.20.3)
- **Broken Links**: 0
- **Orphan Pages**: 0 (Cảm ơn script finalized)
- **Stale Pages**: ~120 trang (Cần rà soát lại sau khi nạp nguồn mới)
