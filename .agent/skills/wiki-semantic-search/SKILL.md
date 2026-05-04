---
name: wiki-semantic-search
description: "Use when wiki-query (keyword search) returns no results or irrelevant results, when the search intent is conceptual or abstract rather than exact-match, or when the user asks questions using meaning rather than specific terms."
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
description: Use when keyword search misses the concept, the request is abstract or meaning-based, or a hybrid BM25-plus-vector lookup is needed from the local QMD index.
---

# Wiki Semantic Search

## Overview
Use the local QMD search stack for meaning-based retrieval when exact terms are unknown or too brittle. Semantic retrieval is a search aid, not a substitute for source validation.

## Guardrails
- Use this after `wiki-query` fails or when the request is clearly conceptual.
- Validate any strong answer against the returned wiki file and, when needed, the raw source.
- Refresh embeddings after major ingest or rebuild work if the index is stale.
- Do not use semantic search for simple filename lookup or directory browsing.

## Workflow
1. Check index health:
   `qmd status`
2. Choose the search mode:
   `qmd vsearch "<concept question>"` for broader semantic retrieval.
   `qmd query "<complex question>"` for hybrid ranked retrieval.
3. Open the returned file with:
   `qmd get "<wiki/path.md>" --full`
4. Verify the answer against the file contents before citing it.
5. If new knowledge has not been embedded yet, run:
   `qmd embed`

## Quick Reference
- Semantic search:
  `qmd vsearch "agent memory versus knowledge graph"`
- Hybrid query:
  `qmd query "How does the vault separate verified from synthesized knowledge?"`
- Full retrieval:
  `qmd get "wiki/concepts/FILE.md" --full`

## Common Mistakes
- Forgetting to re-embed after large content changes.
- Taking a high-ranking result as proof without opening the source file.
- Using semantic search where a direct keyword query would be faster and clearer.
