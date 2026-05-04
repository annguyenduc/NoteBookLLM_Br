# SKILL: wiki-query

Truy xuất tri thức từ Wiki thông qua Hybrid Search (FTS5 + Graph Discovery).

## Context (Bối cảnh)
Khi cần trả lời câu hỏi, đối chiếu khái niệm hoặc tìm kiếm các mối liên hệ giữa các atoms, `wiki-query` cung cấp các mẫu lệnh để trích xuất thông tin chính xác từ `wiki_brain.db`.

## Workflow (Quy trình)

### Bước 1: Keyword Search (FTS5)
Sử dụng tìm kiếm toàn văn để tìm các Atom có chứa từ khóa trong `title` hoặc `metadata`. Dựa trên **Rule 14**, mọi kết quả phải hiển thị rõ nguồn gốc.
```sql
SELECT file_id, title, status, confidence 
FROM atom_search 
WHERE atom_search MATCH 'từ_khóa' 
ORDER BY rank;
```

### Bước 2: Graph Discovery (Truy vết liên kết)
Sau khi tìm được Atom gốc, mở rộng tìm kiếm sang các Atom liên quan. Luôn tham chiếu **USER.md** để đảm bảo output đúng định dạng.
```sql
-- Tìm các Concept liên quan
SELECT target_id, edge_type 
FROM edges 
WHERE source_id = 'atom_id';

-- Tìm các Atom đã bị thay thế (Supersedes)
SELECT source_id 
FROM edges 
WHERE target_id = 'atom_id' AND edge_type = 'SUPERSEDES';
```

### Bước 3: Content Retrieval
Đọc nội dung thô từ file Markdown tương ứng với `file_id` để tổng hợp câu trả lời.

## Các loại Query chuẩn
1. **Concept Query**: Tìm định nghĩa và ví dụ của một khái niệm.
2. **Entity Query**: Tìm thông tin về công cụ, tác giả hoặc tổ chức.
3. **Traceability Query**: Truy vết nguồn gốc (`learning_source`) của một Atom.

## Constraints
- **Chỉ đọc**: Tuyệt đối không thực hiện lệnh `UPDATE/DELETE/INSERT` trong Skill này.
- **Phân loại**: Ưu tiên các Atom có `status='SYNTHESIZED'` hoặc `VERIFIED`. Cảnh báo nếu sử dụng `DRAFT`.
