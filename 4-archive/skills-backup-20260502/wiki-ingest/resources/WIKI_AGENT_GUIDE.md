---
file_id: "WIKI_AGENT_GUIDE"
title: "Hướng dẫn Quy trình Ingest cho Agents"
category: "Meta Guide"
prefix: "WIKI"
tags: ["Meta", "Guideline", "Wiki", "Process"]
status: "verified"
created: "2026-04-25"
last_updated: "2026-05-01"
---

# 📖 Hướng dẫn Quy trình Ingest cho Agents

Tài liệu này quy định **quy trình tư duy** và **chiến lược** khi nạp tri thức mới vào hệ thống Wiki.

## 1. Nguyên tắc Template (Single Source of Truth)
Agent KHÔNG ĐƯỢC tự ý sáng tác cấu trúc file. Bắt buộc sử dụng các Template chuẩn trong thư mục `resources/`:
- **Source**: `SOURCE_TEMPLATE.md`
- **Concept**: `CONCEPT_TEMPLATE.md`
- **Entity**: `ENTITY_TEMPLATE.md`

## 2. Quy trình Ingest 2 Bước (CoT Ingest) - BẮT BUỘC
Mọi nguồn tài liệu mới phải đi qua 2 bước tư duy trước khi thực hiện bất kỳ lệnh ghi file nào:

### Bước 1: Phân tích cấu trúc (Analysis)
Agent phải đọc nguồn thô và xác định:
- **Nguyên tử tri thức**: Chia nhỏ tài liệu thành các Concept và Entity độc lập.
- **Mối quan hệ (Typed Graph)**: Xác định cách các Concept kết nối với nhau (is_a, prerequisite_of, ...).
- **Phòng tránh trùng lặp**: Kiểm tra `index.md` để xem Concept đã tồn tại chưa.

### Bước 2: Khởi tạo theo phân tầng (Generation Hierarchy)
Thực hiện ghi file theo đúng thứ tự ưu tiên:
1.  **SOURCE Page**: Tạo gốc của bằng chứng.
2.  **ENTITY & CONCEPT Pages**: Tạo các hạt nhân tri thức (trích dẫn từ Source).
3.  **SYNTHESIS / INDEX**: Đồng bộ hóa toàn bộ hệ thống (`--finalize`).

## 3. Chiến lược Mật độ Tri thức (Density Strategy)
Mỗi khi nạp một nguồn tài liệu mới, Agent phải đảm bảo tạo ra/cập nhật khoảng **10-15 trang Wiki** liên quan để đảm bảo tri thức được bao phủ đủ sâu và rộng.

## 4. Checklist Tuân thủ
- [ ] Đã thực hiện **Quadruple-View Gate** (Đọc Guide, Template, Raw, Index).
- [ ] Đã điền đầy đủ metadata `relationships` và `last_accessed`.
- [ ] Đã áp dụng **Rule 17 (Double Examples)** trong trang Concept.
- [ ] Đã thực hiện **4F Reflection** (chỉ dành cho Concept và Synthesis).

---
*Lưu ý: Mọi vi phạm quy trình này sẽ bị coi là Hallucination (Rule 15).*
