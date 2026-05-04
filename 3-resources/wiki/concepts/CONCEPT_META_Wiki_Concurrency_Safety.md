---
file_id: CONCEPT_META_WIKI_CONCURRENCY_SAFETY
title: "Wiki Concurrency & Safety (An toàn đồng thời và Quy tắc bảo vệ)"
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
Trang này định nghĩa bộ quy tắc bắt buộc để đảm bảo tính toàn vẹn của dữ liệu khi có nhiều tiến trình (Agent hoặc Script) cùng tác động vào hệ thống Wiki. Việc tuân thủ các quy tắc an toàn này giúp ngăn chặn hiện tượng Race Condition (tranh chấp dữ liệu) và đảm bảo không có tri thức nào bị mất đi do ghi đè vô ý.

## ## Key Claims / Summary
1.  **Read-Before-Write**: Luôn đọc nội dung file trước khi thực hiện bất kỳ chỉnh sửa nào.
2.  **Instant Re-read**: Đọc lại file ngay trước khi ghi để đảm bảo đang làm việc trên phiên bản mới nhất.
3.  **Non-destructive Ingest**: Bảo vệ nguồn thô, tuyệt đối không chỉnh sửa dữ liệu trong thư mục nguồn sau khi đã Ingest.

## 1. Các quy tắc "Bất biến"
- **Read-Before-Write**: Đảm bảo hiểu bối cảnh hiện tại của file.
- **Instant Re-read**: Tránh ghi đè lên thay đổi của Agent khác vừa thực hiện.
- **Log Integrity**: Tuyệt đối không chỉnh sửa thủ công các file log hệ thống.
- **Finalize Sync**: Chỉ cập nhật Index và Backlinks ở bước cuối cùng.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Nếu hai Agent cùng muốn cập nhật trang `CONCEPT_Python`, Agent thứ hai phải đọc lại file sau khi Agent thứ nhất vừa ghi xong để tích hợp cả hai thay đổi thay vì xóa mất công sức của người tiền nhiệm. (Nguồn: [[SOURCE_META_WIKI_GEN_CLONE]]).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như quy tắc của các giáo viên khi cùng soạn giáo án trên Google Docs. "Ai vào sau phải Refresh trang" để đảm bảo mình đang nhìn thấy bản thảo mới nhất, tránh việc hai người cùng sửa một câu dẫn đến mất dữ liệu.

## ## Source Tracing
- **Nguồn**: [[SOURCE_META_WIKI_GEN_CLONE]] — Section: Concurrency Rules.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 20 và chuẩn hóa Source Tracing.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
