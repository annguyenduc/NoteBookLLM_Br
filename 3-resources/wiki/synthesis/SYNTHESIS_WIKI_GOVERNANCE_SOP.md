---
file_id: WIKI_GOVERNANCE_SOP
title: Quy trình Vận hành Tiêu chuẩn Wiki 2.0
type: synthesis
status: verified
tags: ["SOP", "Workflow", "Manual", "Architecture"]
ai-first: true
confidence: 0.8
last_reconciled: 2026-05-08
created: 2026-05-08
last_updated: 2026-05-08
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
| Định nghĩa/Khái niệm | `3-resources/wiki/concepts/` | `CONCEPT_TEMPLATE.md` |
| Con người/Công cụ | `3-resources/wiki/entities/` | `ENTITY_TEMPLATE.md` |
| Bảng so sánh/Đối chiếu | `3-resources/wiki/comparisons/` | `COMPARISON_TEMPLATE.md` |
| Bài tổng hợp/Giáo trình | `3-resources/wiki/synthesis/` | `SYNTHESIS_TEMPLATE.md` |

## 2. Quy trình Xử lý Mâu thuẫn (Conflict Resolution)
Khi phát hiện thông tin trái ngược giữa các nguồn:
1. **Cô lập**: Di chuyển file mới/file lỗi vào `3-resources/wiki/review_queue/`.
2. **Đánh dấu**: Chuyển `status` thành `DRAFT` và thêm tag `conflict`.
3. **Phân xử**: User review và tạo bài so sánh trong `comparisons/` để dung hòa mâu thuẫn.
4. **Giải phóng**: Chuyển file về kho chính và nâng cấp `status: SYNTHESIZED`.

## 3. Quy trình File-back (Knowledge Promotion)
Dùng để biến nội dung chat hoặc kết quả phân tích thành trang Wiki:
1. **Kiểm tra trùng lặp**: Agent rà soát Index để tránh tạo file chồng chéo.
2. **Đảm bảo mật độ (R11)**: Nội dung phải > 200 bytes và có insight mới.
3. **Dán nhãn**: Luôn bắt đầu bằng `status: DRAFT` để ép buộc qua bước Human Review.

## 4. Bảo trì định kỳ (Maintenance)
- **Hàng ngày**: Ghi log vào `logs/log_YYYY_MM_DD.md`.
- **Sau mỗi phiên**: Đúc kết Insight quan trọng vào `session_insights/`.
- **Khi lệch Index**: Chạy lệnh `/rebuild` để đồng bộ Database và Filesystem.

---
**Lưu ý:** Mọi hành động vi phạm SOP này sẽ bị Agent cảnh báo dựa trên Luật R8 (Human Supremacy).
