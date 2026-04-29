---
description: Quy trình chuẩn nạp dữ liệu mới vào hệ thống Wiki (Karpathy Ingest Pattern)
---

Workflow `/ingest` chuẩn hóa cách tiếp nhận một nguồn dữ liệu mới và tích hợp nó vào Wiki.
Karpathy: *"A single source might touch 10-15 wiki pages."*

---

## 📋 Điều kiện tiên quyết (Prerequisites)

Trước khi chạy `/ingest`, kiểm tra:
- [ ] File nguồn đã được đặt vào `3-resources/raw/` (Rule 12 — chỉ User mới được thêm vào raw/).
- [ ] File đặt tên đúng chuẩn: `[PREFIX]_[TÊN].md` theo Rule 7 (Snake_Case, Prefix 2 cấp).
- [ ] Không file nào trong `3-resources/raw/` bị ghi đè.

---

## ⚙️ Các bước thực hiện (Flow cố định)

### Bước 1 (Analysis) — @scout: Đọc và Phân tích cấu trúc (Structured Analysis)
- Đọc toàn bộ file raw mới.
- Tạo file phân tích: `1-projects/[Project_Name]/Analysis_[PREFIX].md` bao gồm:
  - **Tóm tắt cốt lõi**: 3-5 key takeaways quan trọng nhất.
  - **Nhận diện thực thể & Khái niệm**: Liệt kê các key entities, concepts, arguments.
  - **Kết nối (Connections)**: Tìm điểm chung với nội dung Wiki hiện có.
  - **Mâu thuẫn (Contradictions & Tensions)**: Chỉ ra sự khác biệt/xung đột với kiến thức đã có.
  - **Gợi ý cấu trúc Wiki (Recommendations)**: Đề xuất cây thư mục và cấu trúc bài viết mới.
  - **Câu hỏi đào sâu (Deep Research Queries)**: Đề xuất các từ khóa/câu hỏi để bổ sung chỗ hổng kiến thức.
- **Dừng** và đợi User xem xét bản phân tích (Analysis) trước khi tiếp tục.

### Bước 2 (Generation) — @engineer: Khởi tạo & Bồi đắp Wiki (Wiki Generation)
Dựa trên bản phân tích của `@scout`, `@engineer` tiến hành sinh file:
1. **Tạo trang Source**: Tạo `3-resources/wiki/sources/SOURCE_[PREFIX].md` (chứa source summary, frontmatter type/title/sources).
2. **Tạo/Cập nhật trang Khái niệm & Thực thể**: 
   - Khởi tạo các trang trong `wiki/concepts/` và `wiki/entities/` theo chuẩn `WIKI_TEMPLATE.md`.
   - Đảm bảo có Cross-references (liên kết chéo) giữa các trang.
3. **Bồi đắp Master (Direct Compounding)**: Cập nhật trực tiếp kiến thức mới vào các Master pages trong `3-resources/wiki/synthesis/`.
4. **Review Items**: Trình bày danh sách các điểm cần User/con người đánh giá lại (human judgment).

### Bước 3 — @librarian: Cập nhật Index & Tổng hợp
```powershell
python scripts/update_wiki_index.py
```
Cập nhật `3-resources/wiki/index.md` và `overview.md` để phản ánh các trang mới.

### Bước 4 — @pm: Ghi log
Append vào `3-resources/wiki/log.md`:
```
## [YYYY-MM-DD HH:MM] ingest | @pm | [Tên file raw]
- Atomic Files: [danh sách N file wiki]
- Master Compounded: [danh sách M file synthesis]
- Số concept: [X]
```

---

## 🔴 Quy tắc bất biến (Non-negotiable Rules)

- **Raw là bất biến**: Tuyệt đối không sửa file trong `3-resources/raw/` (Rule 12).
- **Source Integrity**: Mọi claim trong Wiki PHẢI trích dẫn nguồn từ file raw (Rule 14).
- **Không hallucinate**: Nếu không tìm thấy trong raw → ghi `[KHÔNG TÌM THẤY NGUỒN]`, báo @auditor.
- **@auditor** luôn là chốt chặn cuối: Review ít nhất 20% trang mới tạo sau mỗi đợt ingest lớn.

---

## 🔗 Liên kết hệ thống

- Template phân tích: `3-resources/wiki/sources/` (Sử dụng làm đầu vào)
- Template Wiki: Không có thư mục process, file phân tích lưu ở `1-projects/`.
- Kiểm tra sức khỏe sau ingest: `/lint`
