---
file_id: CONCEPT_META_WIKI_INDEX_SYNCHRONIZATION
title: "Wiki Index Synchronization (Đồng bộ danh mục Wiki)"
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
Trang này mô tả cơ chế Đồng bộ danh mục (Wiki Index Synchronization) - hạ tầng tra cứu kép của hệ thống. Việc đồng bộ hóa giữa Danh mục bài viết (`_index.md`) và Đồ thị liên kết ngược (`_backlinks.json`) đảm bảo rằng mọi truy vấn, dọn dẹp hay tái cấu trúc đều dựa trên trạng thái mới nhất và chính xác nhất của mạng tri thức.

## ## Key Claims / Summary
1.  **Dual Infrastructure**: Kết hợp giữa danh mục phân cấp (Index) và mạng lưới liên kết (Backlinks).
2.  **Concurrency Integrity**: Chỉ thực hiện đồng bộ hóa ở bước cuối cùng sau khi mọi sửa đổi nội dung đã hoàn tất.
3.  **Discovery Support**: Cung cấp lớp dữ liệu gốc để AI có thể "du hành" qua đồ thị tri thức một cách thông minh.

## 1. Thành phần cốt lõi
- **Index Catalog**: Danh sách mọi bài viết và tên định danh (alias).
- **Backlink Graph**: Bản đồ ghi nhận mọi mối liên hệ giữa các Node.
- **End-of-Command Rebuild**: Quy tắc chỉ rebuild index sau khi hoàn thành lệnh thực thi chính.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Khi thực hiện lệnh `/wiki query`, hệ thống trước tiên đọc `_index.md` và `_backlinks.json` để định vị bối cảnh trước khi tổng hợp câu trả lời, đảm bảo không bỏ sót các trang liên quan. (Nguồn: [[SOURCE_META_WIKI_GEN_CLONE]]).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như hệ thống thẻ tra cứu trong thư viện. `_index.md` là danh mục sách theo chữ cái. `_backlinks.json` là phần "Xem thêm" ở cuối mỗi cuốn sách. Khi thủ thư (AI) cần tìm tài liệu cho bạn, họ dùng cả hai để đảm bảo tìm đúng và đủ các nguồn liên quan.

## ## Source Tracing
- **Nguồn**: [[SOURCE_META_WIKI_GEN_CLONE]] — Section: Command: /wiki query / rebuild-index.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 20 và chuẩn hóa Source Tracing.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
