---
file_id: CONCEPT_META_WIKI_CLEANUP_AUDIT
title: "Wiki Cleanup Audit (Kiểm toán và Dọn dẹp Wiki)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-02"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_META_WIKI_GEN_CLONE]]"
---

## ## For future Claude
Trang này định nghĩa chu trình bảo trì toàn cục (Cleanup Audit) để rà soát và làm giàu tri thức sau các đợt Ingest. Mục tiêu của Cleanup không phải là nạp thêm dữ liệu mới, mà là sửa lại "hình dạng" của tri thức hiện có để đảm bảo tính mạch lạc, độ tin cậy và mật độ liên kết của toàn hệ thống.

## ## Key Claims / Summary
1.  **Structure Alignment**: Chuyển đổi các bài viết dạng nhật ký (Diary-driven) thành dạng câu chuyện tri thức (Narrative-driven).
2.  **Enrichment**: Tự động bổ sung bối cảnh, ví dụ đối chiếu và trích dẫn còn thiếu.
3.  **Graph Health**: Sửa lỗi broken links và đồng bộ hóa Backlinks để đảm bảo sự liền mạch của mạng lưới.

## 1. Các pha vận hành
1.  **Build Context**: Lập bản đồ tri thức hiện tại.
2.  **Per-Article Audit**: Đánh giá cấu trúc, độ dài, giọng văn của từng trang.
3.  **Enrichment**: Viết lại và bổ sung nội dung còn thiếu.
4.  **Integration**: Rebuild index và backlinks.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Sau một tuần Ingest dữ liệu, Agent chạy lệnh `/wiki cleanup` để chuyển các bài ghi chú thô về "Lỗi thiết kế" thành một trang Concept hoàn chỉnh có đầy đủ ví dụ và trích dẫn nguồn từ sách. (Nguồn: [[SOURCE_META_WIKI_GEN_CLONE]]).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như việc dọn dẹp thư viện sau một đợt nhập sách lớn. Bạn không chỉ xếp sách lên kệ (Ingest), mà còn phải bọc lại bìa (Formatting), kiểm tra xem sách có bị đặt sai chỗ không (Classification) và cập nhật lại danh mục tra cứu (Index) để người đọc dễ tìm kiếm.

## ## Source Tracing
- **Nguồn**: [[SOURCE_META_WIKI_GEN_CLONE]] — Section: Command: /wiki cleanup.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 20 và chuẩn hóa Source Tracing.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
