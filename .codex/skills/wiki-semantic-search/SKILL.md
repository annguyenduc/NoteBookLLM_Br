---
name: wiki-semantic-search
description: "TRIGGER: semantic search, concept search, vector search, BM25, reranking. Tìm kiếm ngữ nghĩa trong Wiki NoteBookLLM_Br bằng hybrid search để tìm khái niệm trừu tượng hoặc khi keyword search yếu. Do not use for normal ingest or lint."
---

# Wiki Semantic Search (Local Version)

Dùng khi cần tìm kiếm các khái niệm trừu tượng hoặc khi `wiki-query` (keyword search) không mang lại kết quả mong muốn. Kỹ năng này sử dụng công cụ **QMD** (Hybrid Search Engine) được cài đặt trên hệ thống.

## QMD Search Protocol

### 1. Phân loại tìm kiếm
- **Keyword Search** (Nhanh, dùng cho từ khóa Tiếng Việt):
  ```powershell
  # Ưu tiên alias:
  qmd search "từ khóa"
  # Hoặc dùng đường dẫn trực tiếp nếu lỗi:
  node "C:\Users\anngu\AppData\Roaming\npm\node_modules\@tobilu\qmd\dist\cli\qmd.js" search "từ khóa"
  ```
- **Semantic Search** (Tìm theo ý nghĩa, khái niệm trừu tượng):
  ```powershell
  qmd vsearch "câu hỏi về khái niệm"
  ```
- **Hybrid Query** (Chất lượng nhất, kết hợp BM25 + Vector + Reranking):
  ```powershell
  qmd query "câu hỏi phức tạp cần độ chính xác cao"
  ```

### 2. Thu thập nội dung
Sau khi có kết quả search, dùng lệnh `get` để đọc toàn văn trang (nếu cần):
```powershell
qmd get "wiki/concepts/filename.md" --full
```

## Maintenance (Bảo trì Index)

**QUAN TRỌNG**: Sau mỗi phiên `/ingest` hoặc khi có thay đổi lớn trong Wiki, Agent BẮT BUỘC phải cập nhật Index để QMD nhận diện được tri thức mới:

1. **Kiểm tra trạng thái**: `qmd status`
2. **Thêm file mới (nếu cần)**: `qmd collection add "d:\NoteBookLLM_Br\3-resources\wiki" --name wiki`
3. **Cập nhật Vector Embeddings**:
   ```powershell
   qmd embed
   ```

*Lưu ý: Luôn dùng đường dẫn tuyệt đối đến file `.js` của qmd nếu hệ thống báo lỗi không nhận diện lệnh.*

## Workflow Integration
- **Step 1**: Search bằng QMD.
- **Step 2**: Đọc các trang có Score cao (>= 70%).
- **Step 3**: Đối soát ngược với `3-resources/raw/` (Rule 14).
- **Step 4**: Tổng hợp câu trả lời và cite bằng `[[wikilinks]]`.

## Related
- `wiki-query`
- `wiki-ingest` (Sử dụng `qmd embed` sau khi hoàn tất ingest)
