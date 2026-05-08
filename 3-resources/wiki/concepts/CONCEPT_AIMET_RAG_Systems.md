---
file_id: CONCEPT_AIMET_RAG_Systems
title: CONCEPT AIMET RAG Systems Architecture
type: concept
status: VERIFIED
tags:
ai-first: true
confidence: 0.8
last_reconciled: 2026-05-08
created: 2026-05-01
last_updated: 2026-05-07
---

# RAG Systems (Retrieval-Augmented Generation)

| **Embedder** | Chuyển text → vector | OpenAI Ada, BGE, E5 |
| :--- | :--- | :--- |
| **Vector Store** | Lưu + tìm kiếm vector | Pinecone, Chroma, Weaviate |
| **Retriever** | Query → top-k chunks | Similarity search, MMR |
| **Reranker** | Sắp xếp lại kết quả | Cohere Rerank, cross-encoder |
| **Generator** | Sinh câu trả lời từ chunks | GPT-4, Gemini, Claude |

**Retrieval Strategies**: Dense (semantic), Sparse (BM25/keyword), Hybrid (cả hai).

## 3. Ví dụ đối chiếu (R18: Double Examples)

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

## 5. Trích dẫn nguồn (R3)
- **Nguồn**: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 8, trang 17-18
- **Fact-check**: Đã đối chiếu PDF trang 18: "grounded generation and citations in RAG"

***
*Sơ đồ kiến trúc RAG chuẩn Agentic AI.*


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
