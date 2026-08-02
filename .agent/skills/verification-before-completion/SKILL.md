---
name: verification-before-completion
description: "Chạy lệnh xác minh và kiểm tra output TRƯỚC khi tuyên bố công việc hoàn thành, đã sửa xong, hoặc đang pass. Bằng chứng thực tế trước lời khẳng định."
---

# Xác Minh Trước Khi Hoàn Thành

## Nguyên Tắc Cốt Lõi
**Không bao giờ nói "xong rồi" mà không chạy lệnh kiểm tra thực tế.**

## Quy Trình Bắt Buộc

### Bước 1 — Xác định tiêu chí hoàn thành
Trước khi bắt đầu task, định nghĩa rõ:
- Output trông như thế nào khi thành công?
- Lệnh nào sẽ xác nhận điều đó?

### Bước 2 — Chạy lệnh xác minh
Sau khi thực hiện xong, chạy ít nhất một trong:
- Test tự động (nếu có)
- Lệnh kiểm tra trạng thái file/output
- Script dry-run
- Query kết quả

### Bước 3 — Báo cáo bằng chứng thực tế
Trong kết quả cuối, luôn kèm:
```
✅ Xác minh: [lệnh đã chạy]
📋 Output: [kết quả thực tế]
```

## Dấu Hiệu Cần Dừng & Xác Minh
- Vừa chỉnh sửa file quan trọng
- Vừa chạy script có side effect
- Vừa di chuyển/đổi tên file
- Trước khi nói "đã hoàn thành"

## Lỗi Cần Tránh
- Báo "xong" dựa vào cảm giác mà không chạy kiểm tra
- Tuyên bố test pass mà không chạy test
- Giả định output đúng vì không có error message