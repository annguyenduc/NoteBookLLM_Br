---
name: wiki-hd-convert
description: "Dùng khi PDF nguồn chứa thông tin hình ảnh quan trọng (biểu đồ, sơ đồ, bảng số liệu) cần được chuyển đổi sang Markdown chất lượng cao với ảnh được giữ nguyên."
---

# Chuyển Đổi PDF Chất Lượng Cao (HD Convert)

## Khi Nào Dùng
Dùng khi file PDF có hình ảnh, biểu đồ, bảng số liệu quan trọng không thể mất trong quá trình chuyển đổi sang Markdown.

## Nguyên Tắc Bắt Buộc
- **Không thay đổi nguồn gốc (R1)**: File PDF gốc không được sửa. Sau khi chuyển đổi xong → chuyển vào `3-resources/raw_sources/`.
- **Ảnh phải được giữ**: Mọi hình ảnh, biểu đồ phải được xuất ra thư mục `images/` kèm theo file Markdown.
- **Tổ chức theo cấu trúc**: Ưu tiên chia nhỏ theo `chương → phần → trang` dựa vào mục lục PDF.

## Quy Trình

1. **Xác định PDF** trong `00_Inbox/` — file ở đây cho đến khi chuyển đổi xong
2. **Chạy hd_converter.py** với đường dẫn PDF
3. **Kiểm tra kết quả** — xem manifest và các chunk Markdown, đảm bảo ảnh và bảng được giữ nguyên
4. **Bàn giao sang Phase A** — runner có thể copy output vào `runs/ingest_*/` để build state.json
5. **Lưu trữ** — sau khi chuyển đổi thành công, chuyển PDF gốc từ `00_Inbox/` → `3-resources/raw_sources/`

## Lệnh Thực Thi

```powershell
# Chuyển đổi đơn giản
.\.venv\Scripts\python.exe .agent/skills/wiki-hd-convert/scripts/hd_converter.py "đường/dẫn/file.pdf"

# PDF lớn — chia chunk
.\.venv\Scripts\python.exe .agent/skills/wiki-hd-convert/scripts/hd_converter.py "đường/dẫn/file.pdf" --chunk-size 15
```

## Quy Ước Đặt Tên Output
Trong `00_Inbox/Converted_Sources/`:
- Manifest: `RAW_[YYYY-MM-DD]_[tên-file]_MANIFEST.md`
- Chunk: `RAW_[YYYY-MM-DD]_[tên-file]_[UNIT_ID]_P[đầu]-[cuối].md`

## Chạy Test
```powershell
$env:PYTHONPATH=".agent/skills/wiki-hd-convert"; python .agent/skills/wiki-hd-convert/tests/test_hd_converter.py
```

## Lỗi Phổ Biến
- **Dùng sai công cụ**: MarkItDown tốt cho bảng tính/văn bản thuần; dùng hd_converter cho PDF có hình ảnh
- **Link bị hỏng**: Di chuyển file Markdown mà không mang theo thư mục `images/`
- **Vi phạm R1**: Cố ý ghi output thẳng vào `raw/` bỏ qua staging