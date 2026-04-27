description: Tối ưu hóa & Đối soát tri thức Master (Refinement & Reconciliation)
---

Workflow `/distill` giờ đây đóng vai trò là bước **Kiểm định chất lượng cao** sau khi các Master files (`3-resources/distilled/`) đã được bồi đắp qua nhiều lần ingest. 

Karpathy: *"Optimization is as important as extraction."* — `/distill` giúp làm gọn tri thức, loại bỏ sự trùng lặp và hàn gắn các liên kết mâu thuẫn.

---

## 📋 Điều kiện tiên quyết (Prerequisites)

Trước khi chạy `/distill`, kiểm tra bắt buộc:
- [ ] File Master (`KB_[Domain]_Master.md`) đã tồn tại và đã được bồi đắp từ ≥3 nguồn khác nhau.
- [ ] Phát hiện có dấu hiệu **trùng lặp** thông tin hoặc **mâu thuẫn** giữa các lần bồi đắp.

---

## ⚙️ Các bước thực hiện

### Bước 1 — @scout: Nhận diện mâu thuẫn và trùng lặp
- Đọc Master file (`3-resources/distilled/KB_[Domain]_Master.md`).
- So sánh với các Atomic Wiki pages liên quan trong `3-resources/wiki/`.
- Xác định các đoạn văn bản có nội dung tương đồng nhưng cách diễn đạt khác nhau (redundancy) hoặc các fact trái ngược nhau (conflict).

### Bước 2 — @engineer: Thực hiện Refactoring Master
- **Loại bỏ trùng lặp**: Gộp các fact tương đồng vào một mục thống nhất.
- **Giải quyết mâu thuẫn**: Nếu có 2 fact trái ngược, ưu tiên nguồn mới nhất hoặc nguồn có độ tin cậy cao nhất (xác nhận lại với User nếu cần).
- **Làm giàu liên kết**: Thêm các [[Wikilinks]] mới mà quá trình bồi đắp tự động trước đó bỏ lỡ.

### Bước 3 — @auditor: Verify & Lock
- Kiểm tra lại tính xác thực (Source Integrity) của bản Master đã được tối ưu.
- Cập nhật `status: verified` và ghi nhận phiên bản tối ưu hóa vào log.

### Bước 4 — @librarian: Cập nhật Index
```powershell
python scripts/update_wiki_index.py
```

### Bước 5 — @pm: Ghi log
```
## [YYYY-MM-DD HH:MM] distill | @engineer | KB_[Domain]_Master.md
- Tổng hợp từ: [N] trang Wiki
- Lý do: Tạo bản đồ tri thức nhanh cho domain [Domain]
```

---

## 🔗 Vị trí trong Karpathy Pipeline

```
/ingest  →  3-resources/wiki/ (Chi tiết, có thể cập nhật từng phần)
                ↓
/distill →  3-resources/distilled/ (Tóm tắt nhanh, phục vụ Query đơn giản)
                ↓
/lint    →  Health check cả hai tầng
```

> [!TIP]
> Dùng `/distill` khi bạn muốn có 1 file tổng hợp để tra cứu nhanh, thay vì phải đọc nhiều trang Wiki riêng lẻ. Không cần chạy `/distill` sau mỗi lần ingest — chỉ chạy khi domain đã "chín" (có ≥3 trang verified).
