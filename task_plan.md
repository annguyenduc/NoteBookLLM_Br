# Roadmap NoteBookLLM_Br v5.0 (2026-04-27) — Pivot: Test Bank Only

## ⚠️ PIVOT NOTICE (2026-04-27)
> **Quyết định từ User**: Dự án không cần chiết xuất kiến thức Atom hay xây dựng Wiki nữa.
> **Mục tiêu mới**: Tập trung 100% vào việc trích xuất và duy trì **Test Bank** (MCQ Atoms) từ nguồn LMS.
> **Hành động**: Đã Archive toàn bộ `1-projects/`, `wiki/` và `distilled/`.

---

## ✅ Giai đoạn 0: Dọn dẹp & Lưu trữ (HOÀN TẤT)
- [x] **Archive Projects**: Chuyển `1-projects/2026_Robotics` vào `4-archive/`.
- [x] **Archive Wiki/Distilled**: Chuyển toàn bộ tệp tri thức vào `4-archive/`.
- [x] **Standardize Prefix**: Đổi tên `ROBOT_*` -> `Robot_*` theo đúng Rule 7.
- [x] **WIKI_INDEX Cleanup**: Chỉ giữ lại danh mục `test-bank`.

---

## 🏗️ Giai đoạn 1: Trích xuất LMS (ƯU TIÊN CAO)
- [ ] **Audit Nguồn**: Rà soát 60 đề docx còn lại trong `3-resources/raw/Tổng hợp đề kiểm tra LMS/`.
- [ ] **Extraction Engine**: Sử dụng scripts để trích xuất câu hỏi hàng loạt.
- [ ] **Asset Management**: Đảm bảo toàn bộ ảnh được lưu vào `3-resources/assets/` với prefix `ASSET_[LEVEL1]_[LEVEL2]`.
- [ ] **Link Integrity**: Kiểm tra 100% link ảnh trong `test-bank` không bị broken.

---

## 🧪 Giai đoạn 2: Kiểm định Chất lượng (Quality Gate)
- [ ] **Consistency Check**: Đảm bảo toàn bộ 2500+ câu hỏi (sau khi xong) đều tuân thủ Rule 7.
- [ ] **Metadata Audit**: Kiểm tra tag độ khó và mức độ nhận thức (Bloom) trong từng Atom.

---

*Ghi chú: Không tạo thêm tệp `wiki/` hay `distilled/` trừ khi có yêu cầu mới.*
*Quy tắc prefix: `[CẤP_1]_[CẤP_2]_MCQ_[DE]_[Q].md`*
