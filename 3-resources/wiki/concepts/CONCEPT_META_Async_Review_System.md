---
file_id: CONCEPT_META_ASYNC_REVIEW_SYSTEM
title: "Async Review System (Hệ thống Duyệt bất đồng bộ)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-01"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_META_NASHUS_LLMWIKI]]"
---

## ## For future Claude
Trang này mô tả cơ chế Duyệt bất đồng bộ (Async Review) - một yếu tố quan trọng để duy trì sự kiểm soát của con người trong các hệ thống AI tự trị. Bằng cách tách biệt giai đoạn thực thi và giai đoạn phê duyệt, chúng ta cho phép Agent hoạt động tốc độ cao mà vẫn đảm bảo tính chính xác và độ tin cậy của tri thức được nạp vào Wiki.

## ## Key Claims / Summary
1.  **Flagging**: Đánh dấu các node cần sự can thiệp của con người (status: review).
2.  **Review Queue**: Tập hợp các vấn đề để người dùng xử lý tập trung, giảm thiểu gián đoạn.
3.  **Governance**: Đảm bảo mọi thay đổi quan trọng đều được kiểm chứng.

## 1. Cơ chế vận hành
- **Flagging**: Agent đánh dấu trang là `status: review` khi phát hiện mâu thuẫn tri thức hoặc thiếu nguồn.
- **Review Queue**: Một danh sách các vấn đề được tổng hợp lại để User xử lý một lần.
- **Conflict Resolution**: Quy tắc ưu tiên nguồn hoặc User can thiệp thủ công để chốt tri thức chuẩn.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Hai nguồn tài liệu đưa ra hai định nghĩa khác nhau về một thuật ngữ. Agent không tự chọn, mà tạo một `Review_Item` mô tả mâu thuẫn và chờ User quyết định. (Nguồn: [[SOURCE_META_NASHUS_LLMWIKI]]).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như việc soạn thảo bộ câu hỏi thi. Agent tạo ra 10 câu hỏi, nhưng có 2 câu nó không chắc chắn về độ khó. Nó đẩy 2 câu đó vào "Hàng đợi chờ duyệt" để giáo viên xác nhận mức độ phù hợp trước khi xuất bản.

## ## Source Tracing
- **Nguồn**: [[SOURCE_META_NASHUS_LLMWIKI]] — Section: Human-in-the-loop Systems.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 20 và chuẩn hóa Source Tracing.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
