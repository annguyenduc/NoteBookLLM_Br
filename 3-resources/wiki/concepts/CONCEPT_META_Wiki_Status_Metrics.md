---
file_id: CONCEPT_META_WIKI_STATUS_METRIC
title: "Wiki Status Metrics (Chỉ số sức khỏe Wiki)"
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
Trang này định nghĩa bộ chỉ số Wiki Status Metrics - "bảng điều khiển" sức khỏe của kho tri thức. Các chỉ số này giúp người vận hành thoát khỏi việc "tích trữ file" vô định để chuyển sang quản lý một hệ thống sống có cấu trúc, biết rõ đâu là vùng tri thức đang bị cô lập (Orphans) hay đâu là điểm tắc nghẽn trong quy trình hấp thụ (Pending Entries).

## ## Key Claims / Summary
1.  **System Visibility**: Chuyển từ việc quan sát nội dung từng bài sang quan sát sức khỏe của toàn bộ mạng lưới.
2.  **Structural Health**: Theo dõi mật độ liên kết (Centrality) và sự cân bằng giữa các nhóm chủ đề (Balance).
3.  **Entropy Control**: Phát hiện sớm các trang "mồ côi" (Orphans) để tích hợp lại vào hệ thống.

## 1. Bộ chỉ số nền
- **Entries Absorbed**: Tỷ lệ tri thức thô đã được hấp thụ.
- **Articles by Category**: Phân bổ tri thức theo nhóm chủ đề.
- **Most-Connected Articles**: Các node trung tâm của mạng lưới.
- **Orphans**: Các bài viết thiếu liên kết.
- **Pending Entries**: Hàng đợi tri thức đang chờ xử lý.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Sử dụng lệnh `/wiki status` để hiển thị các chỉ số then chốt như số lượng trang đã hấp thụ, các trang có nhiều liên kết nhất và danh sách các trang mồ côi cần được xử lý ngay. (Nguồn: [[SOURCE_META_WIKI_GEN_CLONE]]).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như dashboard của một giáo viên quản lý lớp học. Thay vì chỉ nhìn vào điểm số (Nội dung), giáo viên nhìn vào biểu đồ tương tác: Những học sinh nào đang cô lập (Orphans), những chủ đề nào học sinh đang thảo luận nhiều nhất (Centrality), từ đó điều chỉnh phương pháp dạy học.

## ## Source Tracing
- **Nguồn**: [[SOURCE_META_WIKI_GEN_CLONE]] — Section: Command: /wiki status.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 20 và chuẩn hóa Source Tracing.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
