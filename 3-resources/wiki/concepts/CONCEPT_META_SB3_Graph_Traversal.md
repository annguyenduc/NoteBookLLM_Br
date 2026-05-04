---
file_id: CONCEPT_META_SB3_GRAPH_TRAVERSAL
title: "Graph Traversal (Truy vết đồ thị tri thức)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-03"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_META_NASHUS_LLMWIKI]]"
  - "[[SOURCE_META_KARPATHY_LLM_WIKI]]"
---

## ## For future Claude
Trang này định nghĩa **Graph Traversal** - một phương pháp truy xuất tri thức dựa trên cấu trúc liên kết đồ thị thay vì chỉ dựa vào từ khóa (Keywords) hay Vector Embeddings. Đây là kỹ thuật cốt lõi giúp AI Agent "nhảy" qua các node liên quan để tìm thấy những mối quan hệ ẩn mà RAG truyền thống thường bỏ lỡ.

## ## Key Claims / Summary
1.  **Topology over Text**: Cấu trúc liên kết (Topology) chứa nhiều thông tin ngữ cảnh hơn là bản thân nội dung văn bản.
2.  **Relational Context**: Một khái niệm được hiểu tốt nhất khi nhìn vào các "hàng xóm" (neighbors) của nó trên đồ thị.
3.  **Discovery of Hidden Links**: Phát hiện các kết nối bất ngờ (Surprising Connections) qua các con đường gián tiếp (2-hop, 3-hop traversal).

## 1. Mô hình 4 Tín hiệu (Relevance Model)
Để thực hiện traversal hiệu quả, hệ thống gán trọng số cho các loại liên kết:
- **Direct Link (x3.0)**: Liên kết trực tiếp `[[link]]`.
- **Source Overlap (x4.0)**: Cùng chung nguồn dữ liệu thô.
- **Adamic-Adar (x1.5)**: Chia sẻ nhiều "hàng xóm" chung.
- **Type Affinity (x1.0)**: Cùng loại đối tượng tri thức.

## 2. Quy trình Traversal
1.  **Seed Selection**: Tìm các node gốc dựa trên keyword search.
2.  **Expansion**: Mở rộng ra các node lân cận trong bán kính 2-3 bước (hops).
3.  **Reranking**: Sắp xếp lại kết quả dựa trên tổng trọng số tín hiệu.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### Ví dụ từ Keppi (Original)
> **Bối cảnh**: Truy vấn về "Transformer Architecture".
> **Ứng dụng**: Ngoài việc tìm các trang có chữ "Transformer", traversal sẽ tự động tìm đến "Attention Mechanism" (Direct link) và "BERT" (Source overlap). Điều này giúp Agent có cái nhìn toàn cảnh về lịch sử và ứng dụng của kiến trúc này.
> **Nguồn**: [[SOURCE_META_KARPATHY_LLM_WIKI]] — Section: Keppi Pattern.

### Ẩn dụ sư phạm (Pedagogical Application)
> **Bối cảnh**: Cách một thám tử điều tra một vụ án.
> **Ứng dụng**: Thay vì chỉ tìm tên nghi phạm trong danh bạ (Keyword search), thám tử sẽ lần theo các mối quan hệ: "Ai là bạn của nghi phạm?", "Họ thường gặp nhau ở đâu?", "Họ có cùng làm việc tại một công ty không?". Việc "traversal" qua mạng lưới quan hệ này giúp tìm ra sự thật mà không cần nghi phạm phải xuất hiện trực tiếp trong tài liệu ban đầu.

## ## Source Tracing
- **Nguồn**: [[SOURCE_META_NASHUS_LLMWIKI]] — Section: 4-Signal Relevance.
- **Nguồn**: [[SOURCE_META_KARPATHY_LLM_WIKI]] — Concept: Keppi Graph Logic.

## ## History / Revisions
- **2026-05-03**: [@engineer] Khởi tạo concept SB3 Graph Traversal.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
