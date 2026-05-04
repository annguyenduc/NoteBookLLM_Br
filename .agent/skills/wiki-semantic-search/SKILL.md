---
name: wiki-semantic-search
description: Use when conceptual, abstract, or hybrid (BM25 + Vector) search is required to retrieve and synthesize knowledge from the Wiki 2.0 repository.
---

# Wiki Semantic Search (Local QMD)

Dùng khi cần tìm kiếm các khái niệm trừu tượng hoặc khi `wiki-query` (keyword search) không mang lại kết quả mong muốn. Kỹ năng này sử dụng công cụ **QMD** (Hybrid Search Engine) được cài đặt trên hệ thống.

## When to Use
- Tìm kiếm dựa trên ý nghĩa (Semantic) thay vì chỉ so khớp từ khóa.
- Thực hiện các truy vấn phức tạp kết hợp BM25, Vector Embeddings và Reranking (Hybrid).
- **Trường hợp KHÔNG dùng**: Tìm kiếm file theo tên chính xác hoặc duyệt thư mục (dùng `ls` hoặc `grep`).

## Core Pattern: QMD Hybrid Search

### Search Modes
- **Semantic Search** (Vector-based):
  ```powershell
  qmd vsearch "câu hỏi về khái niệm"
  ```
- **Hybrid Query** (BM25 + Vector + Reranking):
  ```powershell
  qmd query "câu hỏi phức tạp cần độ chính xác cao"
  ```
- **Content Retrieval**:
  ```powershell
  qmd get "wiki/concepts/filename.md" --full
  ```

## Maintenance: Indexing Workflow
Sau mỗi phiên `/ingest` hoặc khi có thay đổi lớn, Agent PHẢI cập nhật Index để tri thức mới được nhúng (embedded) vào Vector Space:

1. **Kiểm tra trạng thái**: `qmd status`
2. **Cập nhật Vector Embeddings**:
   ```powershell
   qmd embed
   ```
   *Lưu ý: Nếu lệnh `qmd` lỗi, hãy dùng đường dẫn tuyệt đối đến file JS của qmd.*

## Quick Reference: Quality Thresholds
- **Confidence Score >= 75%**: Có thể trích dẫn trực tiếp.
- **Confidence Score < 50%**: Cần kiểm tra thủ công kỹ lưỡng hoặc dùng `wiki-query` bổ trợ.

## Common Mistakes
- **Quên Embed**: Nạp file mới nhưng không chạy `qmd embed` dẫn đến search không thấy.
- **Vượt quá Context**: Search trả về quá nhiều kết quả nhưng không lọc (Reranking) trước khi tổng hợp.
- **Thiếu Source Tracing**: Trích dẫn từ QMD nhưng quên đối soát với file gốc trong `3-resources/raw/`.
