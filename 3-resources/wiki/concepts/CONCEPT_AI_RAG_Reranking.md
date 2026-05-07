---
file_id: CONCEPT_AI_RAG_RERANKING
title: "RAG Reranking (Optimizing Retrieval Quality)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@scout"
status: "verified"
source: "[[SOURCE_AIMET_AGENTIC_ROADMAP_2026]]"
---

# RAG Reranking (Optimizing Retrieval Quality)

## Core Principle
Reranking là bước xử lý hậu kỳ sau khi truy xuất ban đầu (Initial Retrieval). Nó sử dụng một mô hình chuyên biệt (Cross-Encoder) để đánh giá lại độ liên quan giữa Query và các đoạn văn bản (Chunks), giúp đưa những thông tin quan trọng nhất lên đầu danh sách.

## Tại sao Reranking lại quan trọng?
1. **Xử lý lỗi "Lost in the Middle"**: LLM thường bỏ sót thông tin ở giữa Context Window. Reranking đẩy thông tin quan trọng nhất lên đầu (hoặc cuối) để LLM chú ý hơn.
2. **Giảm nhiễu (Noise Reduction)**: Loại bỏ các đoạn văn bản có độ tương đồng vector cao nhưng nội dung thực tế không liên quan.
3. **Cải thiện độ chính xác**: Giúp Agent đưa ra câu trả lời dựa trên bằng chứng (Evidence) mạnh mẽ nhất.

## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Sử dụng **Cohere Rerank API** hoặc mô hình **BGE-Reranker** sau khi lấy ra Top 10 chunks từ ChromaDB, sau đó chỉ lấy Top 3 chunks có điểm cao nhất để nạp vào LLM.
- **Ẩn dụ sư phạm (Pedagogical)**: [Phóng tác] Giống như một **Bộ lọc của Giám khảo (Jury Filter)**: Vòng sơ tuyển (Vector Search) chọn ra 100 thí sinh có ngoại hình phù hợp. Nhưng vòng phỏng vấn chuyên sâu (Reranking) mới thực sự tìm ra 3 người có năng lực chuyên môn tốt nhất để vào vòng chung kết.

## 4F Reflection
- **Facts**: Reranking tốn tài nguyên và thời gian hơn Vector Search nhưng mang lại hiệu quả vượt trội về chất lượng câu trả lời.
- **Feelings**: Việc nhìn thấy Agent trả lời trúng đích hơn sau khi thêm Reranker mang lại cảm giác hệ thống "thực sự hiểu" dữ liệu.
- **Findings**: Hybrid Search (BM25 + Vector) kết hợp với Reranking là "Tiêu chuẩn vàng" (Gold Standard) cho RAG hiện nay.
- **Futures**: Các mô hình nhúng (Embeddings) thế hệ mới sẽ tích hợp sẵn khả năng Reranking ngay trong một lần gọi.

## Nguồn tham khảo
- [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 7 (RAG: chunks, re-ranking).
