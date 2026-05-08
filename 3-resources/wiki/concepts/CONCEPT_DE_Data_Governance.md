---
file_id: CONCEPT_DE_Data_Governance
title: Data Governance (Quản trị dữ liệu)
type: concept
status: VERIFIED
tags:
  - Wiki Page
ai-first: true
confidence: 0.8
last_reconciled: 2026-05-08
created: 2026-05-02
last_updated: 2026-05-03
---

## ## For future Claude
Trang này giải thích về Quản trị dữ liệu (Data Governance) - tập hợp các quy tắc và quy trình để đảm bảo tài sản dữ liệu của tổ chức luôn an toàn, chính xác và có thể truy xuất nguồn gốc. Đây là yếu tố sống còn để xây dựng sự tin tưởng vào các báo cáo và mô hình ML trong môi trường doanh nghiệp.

## ## Key Claims / Summary
1.  **Trust & Accountability**: Xác định rõ ai sở hữu dữ liệu và ai chịu trách nhiệm về chất lượng dữ liệu.
2.  **Compliance**: Đảm bảo tuân thủ các quy định pháp luật về bảo mật (GDPR, HIPAA).
3.  **Data Lineage**: Khả năng truy xuất nguồn gốc từ lúc dữ liệu sinh ra đến lúc hiển thị trên báo cáo.

## 1. Các trụ cột chính
- **Data Quality**: Đảm bảo dữ liệu chính xác, đầy đủ và đáng tin cậy.
- **Data Security**: Bảo vệ dữ liệu khỏi truy cập trái phép.
- **Data Privacy**: Tuân thủ các quy định bảo mật thông tin cá nhân.
- **Data Lineage**: Theo dõi nguồn gốc và sự biến đổi của dữ liệu.

## ## Ví dụ đối chiếu (R18)
- **Ví dụ thực tế (Original)**: Sử dụng Metadata Catalog để ghi chú: "Cột `user_email` là dữ liệu nhạy cảm (PII), chỉ người có quyền Admin mới được xem". Nếu không có Governance, dữ liệu này có thể bị rò rỉ ra bên ngoài.
- **Ẩn dụ sư phạm (Pedagogical)**: [Phóng tác] Giống như nội quy của một thư viện. Nếu không có thủ thư (Data Steward) và các quy định mượn trả (Governance), sách (Dữ liệu) sẽ bị mất, hư hỏng hoặc đặt sai chỗ, khiến người sau không thể tìm thấy thông tin mình cần.

## ## Source Tracing
- **Nguồn**: SOURCE_DE_FUNDAMENTALS_OF_DATA_ENGINEERING — Chapter 12.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung R18, 20 và chuẩn hóa metadata.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
