file_id: CONCEPT_AIMET_RAG_SYSTEMS
title: "RAG Systems (Retrieval-Augmented Generation)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-02"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_AIMET_AGENTIC_ROADMAP_2026]]"
---

## ## For future Claude
Trang này định nghĩa kiến trúc RAG (Retrieval-Augmented Generation) - giải pháp cốt lõi để giải quyết vấn đề Knowledge Cutoff và Hallucination trong LLM. RAG cho phép Agent truy cập vào các kho tri thức động và khổng lồ mà không cần huấn luyện lại mô hình, tạo ra các câu trả lời có tính xác thực và dẫn nguồn cao.

## ## Key Claims / Summary
1.  **Knowledge Augmentation**: LLM được cung cấp thêm dữ liệu bên ngoài (Context) ngay tại thời điểm thực thi.
2.  **Groundedness**: Ép LLM chỉ trả lời dựa trên những gì tìm thấy trong tài liệu truy xuất được để chống bịa đặt.
3.  **Two-Stage Process**: Gồm giai đoạn Truy xuất (Retrieval - tìm thông tin) và giai đoạn Sinh (Generation - tổng hợp câu trả lời).

## ## Detailed Analysis

# RAG Systems (Retrieval-Augmented Generation)

## 1. Định nghĩa

**RAG** là kiến trúc bổ sung khả năng tra cứu tài liệu ngoài vào quá trình sinh text của LLM. Thay vì chỉ dựa vào training data (có thể cũ hoặc thiếu), agent **retrieve** đoạn văn bản liên quan từ Vector Store và đưa vào context trước khi generate.

```
Query → Embed → Vector Search → Retrieve Chunks → Augment Context → Generate
```

## 2. Nguyên lý / Cấu trúc

| Thành phần | Vai trò | Ví dụ tool |
|---|---|---|
| **Embedder** | Chuyển text → vector | OpenAI Ada, BGE, E5 |
| **Vector Store** | Lưu + tìm kiếm vector | Pinecone, Chroma, Weaviate |
| **Retriever** | Query → top-k chunks | Similarity search, MMR |
| **Reranker** | Sắp xếp lại kết quả | Cohere Rerank, cross-encoder |
| **Generator** | Sinh câu trả lời từ chunks | GPT-4, Gemini, Claude |

**Retrieval Strategies**: Dense (semantic), Sparse (BM25/keyword), Hybrid (cả hai).

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Agent trả lời câu hỏi về tài liệu nội bộ công ty (không có trong training data)
> **Ứng dụng**: Embed toàn bộ tài liệu → lưu vào Chroma → khi user hỏi, retrieve top-5 chunks → LLM generate câu trả lời có citation. "Grounded generation" đảm bảo câu trả lời chỉ dựa trên tài liệu thực
> **Nguồn**: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 8 (RAG Systems)

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Chatbot hỗ trợ giáo viên tra cứu tài liệu chương trình STEAM Quốc gia
> **Ứng dụng**: Embed toàn bộ bộ sách giáo khoa + tài liệu Bộ GD → Vector Store. Giáo viên hỏi "Chuẩn đầu ra lớp 8 môn KHTN" → agent retrieve đúng section liên quan → trả lời có trích dẫn văn bản gốc. Giảm hallucination đáng kể so với dùng LLM thuần.

## 4. Phản tư sư phạm (4F)
- **Facts**: RAG giải quyết 2 vấn đề LLM: knowledge cutoff và hallucination về domain-specific info
- **Feelings**: Phần khó nhất không phải RAG pipeline mà là **chunking strategy** — chunk quá nhỏ mất context, quá lớn mất precision
- **Findings**: Hybrid search (dense + sparse) thường tốt hơn pure semantic search cho domain-specific content
- **Futures**: Kết hợp với [[CONCEPT_AIMET_Memory_Management]] → RAG làm long-term memory có semantic retrieval

## 5. Trích dẫn nguồn (Rule 14)
- **Nguồn**: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 8, trang 17-18
- **Fact-check**: Đã đối chiếu PDF trang 18: "grounded generation and citations in RAG"

---
WRITE REPORT:
  file: "3-resources/wiki/concepts/CONCEPT_AIMET_RAG_Systems.md"
  operation: "create"
  added: "Atomic concept về RAG pipeline, 5 components, retrieval strategies"
  compliance: "Rule 20 OK"


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
