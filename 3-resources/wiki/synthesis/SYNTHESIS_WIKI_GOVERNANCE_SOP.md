---
file_id: WIKI_GOVERNANCE_SOP
title: Quy trình Vận hành Tiêu chuẩn Wiki 2.0
type: Synthesis
kwsr_type: "knowledge"  # knowledge | workflow | skill | rule
status: VERIFIED
tags: ["SOP", "Workflow", "Manual", "Architecture"]
ai-first: true
confidence: 0.8
last_reconciled: 2026-05-19
created: 2026-05-08
last_updated: 2026-05-19
sources:
  - "[[SOURCE_GOV_WIKI_V3_MASTER_CONSTITUTION]]"
---

# 📜 Quy trình Vận hành Tiêu chuẩn (SOP) - Wiki 2.0

Tài liệu này hướng dẫn cách tương tác và quản lý tri thức trong hệ thống NoteBookLLM_Br để đảm bảo tính toàn vẹn và sạch sẽ của "Second Brain".

## 1. Nguyên tắc Ghi file (Routing Rules)
Agent và User phải tuân thủ đúng lộ trình di chuyển của file:

| Loại tri thức | Thư mục đích | Template sử dụng |
| :--- | :--- | :--- |
| Nguồn thô (PDF, Web) | `3-resources/raw_sources/` | N/A (Immutable) |
| Tài liệu HD Markdown | `3-resources/raw_ingest/` | N/A |
| Tài nguyên ảnh/biểu đồ | `3-resources/raw_assets/` | N/A |
| Định nghĩa/Khái niệm | `3-resources/wiki/concepts/` | `CONCEPT_TEMPLATE.md` |
| Con người/Công cụ | `3-resources/wiki/entities/` | `ENTITY_TEMPLATE.md` |
| Bảng so sánh/Đối chiếu | `3-resources/wiki/comparisons/` | `COMPARISON_TEMPLATE.md` |
| Bài tổng hợp/Giáo trình | `3-resources/wiki/synthesis/` | `SYNTHESIS_TEMPLATE.md` |
| Báo cáo/Insight | `3-resources/wiki/session_insights/` | N/A |

## 2. Quy trình Xử lý Mâu thuẫn (Conflict Resolution)
Khi phát hiện thông tin trái ngược giữa các nguồn:
1. **Cô lập**: Di chuyển file mới/file lỗi vào `00_Inbox/` hoặc `failed_queue/` (không được đưa trực tiếp vào `3-resources/` theo quy tắc R22).
2. **Đánh dấu**: Chuyển `status` thành `DRAFT` và thêm tag `conflict`.
3. **Phân xử**: Triển khai `wiki-council` để phân tích mâu thuẫn hoặc kích hoạt User review tạo bài so sánh trong `comparisons/`.
4. **Giải phóng**: Chỉ có Human được set `status: SYNTHESIZED` để đưa tri thức chính thức vào Wiki (R8).

## 3. Quy trình File-back (Knowledge Promotion)
Dùng để biến nội dung chat hoặc kết quả phân tích thành trang Wiki:
1. **Gọi lệnh**: Sử dụng workflow `/file-back` để tự động hóa quá trình chuẩn hóa.
2. **Kiểm tra trùng lặp**: Agent rà soát Index hoặc query SQLite để tránh tạo file trùng lặp.
3. **Đảm bảo mật độ (R11)**: Nội dung phải > 200 bytes và có mật độ tri thức cao.
4. **Dán nhãn**: Luôn bắt đầu bằng `status: DRAFT` để chuyển vào `review_queue/` hoặc chờ bước Human Review.

## 4. Bảo trì định kỳ (Maintenance)
- **Hàng ngày**: Ghi log vào `logs/log_YYYY_MM_DD.md`.
- **Sau mỗi phiên**: Đúc kết Insight quan trọng vào `session_insights/`.
- **Khi lệch Index / Kiểm tra sức khỏe**: Chạy lệnh `/rebuild` để đồng bộ DB & Filesystem, `/status` để xem Link Density Dashboard, và `/cleanup` để dọn dẹp broken links.

---
**Lưu ý:** Mọi hành động vi phạm SOP này sẽ bị Agent cảnh báo dựa trên Luật R8 (Human Supremacy).
