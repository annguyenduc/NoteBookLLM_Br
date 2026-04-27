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

### Bước 1 — @scout: Đọc và Thảo luận
- Đọc toàn bộ file raw mới.
- Trình bày cho User **3-5 key takeaways** quan trọng nhất.
- Xác nhận phạm vi khai thác và những gì **KHÔNG** khai thác (negative scope).
- **Dừng** và đợi User xác nhận trước khi tiếp tục.

### Bước 2 — @scout: Tạo Process file
- Tạo `3-resources/process/[PREFIX]_Deep_Mining.md` theo chuẩn `PROCESS_TEMPLATE.md`.
- Điền đầy đủ **Mining Stats table** (tổng concept, phạm vi, trạng thái).
- **MỚI**: Liệt kê các Master Files (`3-resources/distilled/`) dự kiến sẽ được bồi đắp.

### Bước 3 — @engineer: Tạo/Cập nhật Atomic Wiki pages
Với mỗi concept chính được @scout xác định:
1. Kiểm tra CONCEPT PAGES trong `3-resources/WIKI_INDEX.md` xem trang đã tồn tại chưa.
2. **Nếu đã có** → Cập nhật (update) trang hiện tại trong `3-resources/wiki/`, ghi rõ nguồn mới.
3. **Nếu chưa có** → Tạo trang mới theo `3-resources/wiki/WIKI_TEMPLATE.md`.

### Bước 4 — @engineer: Direct Compounding (Bồi đắp Master)
*Đây là bước quan trọng nhất của llm-wiki standard:*
- Dựa trên các concept vừa trích xuất, thực hiện cập nhật ngay vào các tệp Master tương ứng trong `3-resources/distilled/`.
- **Yêu cầu**: Nén tri thức, loại bỏ trùng lặp và tạo liên kết đa chiều giữa các Master pages.

### Bước 5 — @librarian: Cập nhật Index
```powershell
python scripts/update_wiki_index.py
```
Chạy script sau khi đã bồi đắp xong cả Wiki và Master.

### Bước 6 — @pm: Ghi log
Append vào `3-resources/log.md`:
```
## [YYYY-MM-DD HH:MM] ingest | @pm | [Tên file raw]
- Atomic Files: [danh sách N file wiki]
- Master Compounded: [danh sách M file distilled]
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

- Template quy trình: `3-resources/process/PROCESS_TEMPLATE.md`
- Template Wiki: `3-resources/wiki/WIKI_TEMPLATE.md`
- Kiểm tra sức khỏe sau ingest: `/lint`
