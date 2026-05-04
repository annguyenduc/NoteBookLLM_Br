---
project: 2026_Data_Analyst
task: Mass-Heal Education Case Campaign
status: draft
author: "@pm"
created: "2026-04-29"
---

# Kế hoạch Chiến dịch Mass-Heal: EdTech Data Analytics

**Mục tiêu:** Cập nhật/Vá toàn bộ 82 files trong `3-resources/wiki/concepts/` để tuân thủ Rule 17 (Double Examples). Tất cả các ví dụ phải được xây dựng dựa trên bối cảnh **Data Analysis trong Giáo dục (EdTech/LMS/School Management)**, thay vì Kinh doanh bán lẻ thông thường hay Sư phạm mầm non.

---

## 📅 Các Giai đoạn (Phases)

### Phase 1: Audit & Khởi tạo (Preparation)
- **Mục tiêu:** Quét toàn bộ 82 files và phân loại danh sách chính xác.
- **Hành động:**
  - Dùng script để phân tách 82 files thành 2 nhóm:
    - **Nhóm 1 (36 files):** Chưa có block Double Examples (Gồm `CONCEPT_THINK_*` và `CONCEPT_ACAD_AI_*`).
    - **Nhóm 2 (46 files):** Đã có Double Examples (Business Case cũ - Gồm `SQL`, `EXCEL`, `VIZ`, `PYTHON`).
  - **Agent phụ trách:** `@pm` / `@devops`

### Phase 2: Mass-Heal Nhóm 1 (New Injection)
- **Mục tiêu:** Tiêm (inject) Double Examples mới toanh cho 36 files.
- **Hành động:**
  - Viết Python script tự động tạo và chèn nội dung EdTech Business Case vào trước phần `--- Nguồn:`.
  - **Đợt 2A:** 29 files `CONCEPT_THINK_*` (Framework tư duy phân tích giáo dục).
  - **Đợt 2B:** 7 files `CONCEPT_ACAD_AI_*` (AI trong giáo dục).
  - **Agent phụ trách:** `@engineer`

### Phase 3: Re-Heal Nhóm 2 (Rewrite Old Cases)
- **Mục tiêu:** Đè (Overwrite) các ví dụ kinh doanh cũ bằng ví dụ EdTech mới cho 46 files.
- **Hành động:**
  - Dùng Python script tìm kiếm block `## X. Ví dụ minh họa (Rule 17: Double Examples)` đến trước block `--- Nguồn:`.
  - Thay thế bằng nội dung EdTech mới tương ứng với từng file.
  - **Đợt 3A:** Nhóm SQL (11 files) & Excel (4 files).
  - **Đợt 3B:** Nhóm VIZ (8 files) & Python/Pandas (6+ files).
  - **Agent phụ trách:** `@engineer`

### Phase 4: QA & Đóng gói (Verification)
- **Mục tiêu:** Đảm bảo 100% file qua bài test Rule 17.
- **Hành động:**
  - Chạy `scripts/maintenance/audit_rule17.py` để verify.
  - Ghi báo cáo tổng kết vào `3-resources/wiki/log.md`.
  - Cập nhật `CONTINUITY.md`.
  - **Agent phụ trách:** `@librarian` & `@healer`

---

## 🛠 Tiêu chuẩn Ví dụ (EdTech Standard)
Mỗi file sẽ được inject một block như sau:
```markdown
## X. Ví dụ minh họa (Rule 17: Double Examples)

### Ví dụ 1: [Góc nhìn Hệ thống / Vĩ mô]
*Tình huống: [Tối ưu hóa LMS, Phân tích hành vi bỏ học, Quản lý ngân sách trường học...]*
- **Đầu vào:** [Dữ liệu sinh viên/log hệ thống]
- **Cách giải quyết:** [Áp dụng kỹ thuật của concept]

### Ví dụ 2: [Góc nhìn Vi mô / Học viên]
*Tình huống: [Dự báo điểm số, Cá nhân hóa lộ trình học, Đánh giá giáo viên...]*
- **Đầu vào:** [Dữ liệu điểm thi/tương tác cá nhân]
- **Cách giải quyết:** [Áp dụng kỹ thuật của concept]
```
