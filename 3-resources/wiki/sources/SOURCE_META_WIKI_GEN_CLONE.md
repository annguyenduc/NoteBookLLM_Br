---
file_id: SOURCE_META_WIKI_GEN_CLONE
title: "WEB: Wiki Generation & Personal Knowledge Master Protocol"
type: source
status: VERIFIED
tags:
  - WEB
ai-first: true
confidence: 0.8
last_reconciled: 2026-05-08
created: 2026-05-01
last_updated: 2026-05-02
---

# WEB: Wiki Generation & Personal Knowledge Master Protocol

## 🔍 1. Phân tích Ingest (Analysis - Step 1)
*Phần này ghi lại kết quả phân tích cấu trúc trước khi tạo các trang Concept.*
- **Thực thể & Khái niệm then chốt:** Writer vs Filing Clerk, Absorption Loop, Anti-Cramming, Concrete Noun Test, Wikipedia Tone.
- **Kết nối Wiki:** Đây là nền tảng kỹ thuật cho toàn bộ hệ thống NoteBookLLM_Br, cung cấp các lệnh `absorb`, `cleanup`, `query`, `breakdown`, `rebuild-index`, và `status`.
- **Điểm khác biệt/Mâu thuẫn:** Nhấn mạnh việc AI phải đóng vai trò "Người viết lách" (Writer) để tổng hợp ý nghĩa, thay vì chỉ "Thư ký" (Filing Clerk) để lưu trữ sự thật.
- **Đề xuất cấu trúc:** Chia nhỏ thành các Concept về: Giao thức hấp thụ, Kiểm soát độ hạt, Hệ thống phân loại (Taxonomy) và Tiêu chuẩn viết lách.

## 📖 2. Tổng quan nguồn (Overview - Step 2)
Tài liệu định nghĩa một bộ Skill hoàn chỉnh cho Claude Code để xây dựng "Bản đồ tâm trí" (Map of a mind). Trọng tâm không nằm ở việc lưu trữ mà ở việc **hấp thụ tri thức** — hiểu rõ ý nghĩa và sự kết nối của từng mẩu thông tin đối với cuộc đời của chủ thể.

## 🚀 3. Các Concept đã trích xuất (R3 & 17)
- [[CONCEPT_META_Wiki_Absorption_Loop]] | **Wiki Absorption Loop** - Giao thức 5 bước để biến entry thô thành bài viết tổng hợp.
- [[CONCEPT_META_Wiki_Granularity_Control]] | **Granularity Control** - Quy tắc Anti-Cramming (chống nhồi nhét) và Anti-Thinning (chống hời hợt).
- [[CONCEPT_META_Wiki_Writing_Tone]] | **Wiki Writing Tone** - Tiêu chuẩn viết kiểu Wikipedia: "khách quan, súc tích, không dùng mỹ từ."
- [[CONCEPT_META_Wiki_Directory_Taxonomy]] | **Wiki Directory Taxonomy** - Hệ thống 30+ thư mục phân loại tri thức từ đời sống đến tư duy.
- [[CONCEPT_META_Wiki_Breakdown_Mining]] | **Wiki Breakdown & Mining** - Kỹ thuật dùng "Concrete Noun Test" để phát hiện lỗ hổng tri thức.
- [[CONCEPT_META_Wiki_Cleanup_Audit]] | **Wiki Cleanup Audit** - Chu trình audit và enrich toàn wiki sau ingest để sửa cấu trúc, tone và liên kết.
- [[CONCEPT_META_Wiki_Index_Synchronization]] | **Wiki Index Synchronization** - Cơ chế đồng bộ index và backlinks để query, cleanup và reorganize hoạt động trên cùng một graph.
- [[CONCEPT_META_Wiki_Status_Metrics]] | **Wiki Status Metrics** - Bộ chỉ số đọc sức khỏe vận hành của wiki sống.
- [[CONCEPT_META_Wiki_Reorganization]] | **Wiki Reorganization** - Tư duy tái cấu trúc wiki ở cấp kiến trúc: "merge, split, reclassify và rebuild."
- [[CONCEPT_META_Wiki_Quote_Discipline]] | **Wiki Quote Discipline** - Quy tắc giữ article voice trung tính bằng cách kiểm soát số lượng quote trực tiếp.
- [[CONCEPT_META_Wiki_Article_Length_Targets]] | **Wiki Article Length Targets** - Bộ ngưỡng độ dài theo type để cân bằng chiều sâu và khả năng đọc.
- [[ENTITY_TOOL_Claude_Code_Wiki_Gen]] | **Claude Code Wiki Gen** - Thực thể công cụ hỗ trợ thực thi toàn bộ giao thức này.

## 🕵️ 4. Review Items (Dành cho Human)
- [ ] Xác nhận xem cấu trúc `3-resources/wiki/` hiện tại có nên áp dụng bộ Taxonomy 30 thư mục này không.
- [ ] Kiểm tra khả năng triển khai `_backlinks.json` tự động bằng Python script.
- [ ] Đánh giá xem `The Golden Rule` có nên được tách thành một concept atom độc lập ở vòng ingest sau hay không.

***
**Nguồn thô:** `MISC_wikiepdia_generate.md, AIMET_wiki-gen-skill.md`
**Deep Research Query:** `Claude Code personal knowledge wiki writer vs filing clerk`

## 4F Reflection
- **Facts**: File bị hỏng nặng do lỗi encoding và đa frontmatter.
- **Feelings**: Đau lòng khi thấy tri thức bị Mojibake.
- **Findings**: Audit v1 quá yếu để phát hiện các lỗi cấu trúc sâu.
- **Futures**: Cần chạy Healer v2.1 trên toàn bộ vault sau khi verify an toàn.