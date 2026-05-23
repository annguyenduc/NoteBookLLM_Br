# Workflow: Source-First Atomization (Chiến lược "Bản đồ trước, Atom sau")

Workflow này định nghĩa quy trình tối ưu để nạp một tài liệu phức tạp (PDF/Sách) vào Wiki 2.0 sau khi đã hoàn thành bước Ingest kỹ thuật.

## 1. Mục tiêu
- Đảm bảo tính nhất quán của Metadata và định danh (Prefix).
- Tránh trùng lặp các thực thể xuất hiện nhiều lần trong tài liệu.
- Xây dựng khung ngữ cảnh (Context) vững chắc trước khi đi vào chi tiết.

## 2. Các bước thực hiện

### Bước 1: Khởi tạo Source Node (Bản đồ)
- **Hành động**: Tạo file `SOURCE_[ID]_[TITLE].md` tại `3-resources/wiki/sources/`.
- **Nội dung**: Điền đầy đủ Metadata, Tóm tắt cốt lõi và Mục lục (ToC). Liệt kê các [[Thực thể chính]] xuất hiện trong toàn bộ tài liệu.

### Bước 2: Khởi tạo Thực thể nền tảng (Foundation Entities)
- **Hành động**: Tạo các file `ENTITY_[ID]_*.md` cho các Tác giả, Tổ chức, Nhân vật quan trọng đã liệt kê ở Bước 1.
- **Mục tiêu**: Làm sạch các "điểm neo" nhân sự và tổ chức để các trích dẫn sau này có chỗ để liên kết.

### Bước 3: Thiết lập Bàn làm việc (Analysis Project)
- **Hành động**: Tạo các file `Analysis_[ID]_CHUNK_XX.md` tại `1-projects/` (Cấu trúc phẳng).
- **Mục tiêu**: Chia nhỏ tài liệu thành các phiên làm việc (Session) có thể quản lý được.

### Bước 4: Bóc tách tri thức nguyên tử (Atomic Extraction)
- **Hành động**: Đi qua từng Chunk, trích xuất `CONCEPT_[ID]_*.md`.
- **Nguyên tắc**: Luôn trỏ ngược `source_ref` về Source Node đã tạo ở Bước 1.

## 3. Lưu ý quan trọng
- **Flat Structure**: Tuyệt đối không tạo thư mục con trong `1-projects/`.
- **Prefix Consistency**: Dùng mã định danh nguồn (như `ARCH_TIS`) xuyên suốt cho mọi file liên quan.
- **Human Approval**: Mọi Atom mới phải qua `review_queue` và được Human duyệt (R8).

---
*Cấu chuẩn hóa bởi @pm & @engineer | 2026-05-14*
