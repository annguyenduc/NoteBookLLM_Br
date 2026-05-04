---
file_id: CONCEPT_META_WIKI_QUERY_PATTERNS
title: "Wiki Query Patterns (Mẫu câu lệnh truy vấn tri thức)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-01"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_TOOL_GEMINI_DEVELOPER_CODEX]]"
  - "[[SOURCE_META_NASHUS_LLMWIKI]]"
---

## ## For future Claude
Trang này định nghĩa các Mẫu câu lệnh truy vấn tri thức (Wiki Query Patterns) - công cụ để khai thác tối đa sức mạnh của một kho tri thức nguyên tử. Bằng cách sử dụng các mẫu truy vấn có cấu trúc (như truy vấn theo đồ thị hay tổng hợp đa bước), Agent có thể vượt qua giới hạn của việc tìm kiếm từ khóa đơn thuần để tiến tới sự tổng hợp tri thức có chiều sâu và không có ảo giác (Hallucination).

## ## Key Claims / Summary
1.  **Syntactic Delimiters**: Sử dụng các rào chắn ngữ pháp để ép AI chỉ sử dụng nguồn tri thức xác thực.
2.  **Multi-Step Synthesis**: Chia quá trình tổng hợp thành các giai đoạn: Thu thập -> Kiểm toán -> Kết nối.
3.  **Graph Traversal**: Khả năng "du hành" qua các liên kết để khám phá các mối quan hệ ẩn giữa các khái niệm.

## 1. Quy trình Truy vấn Chuẩn (Karpathy Workflow)
Để đảm bảo truy xuất chính xác và không có ảo giác, quy trình truy vấn tuân thủ 4 bước:
1.  **Index-First Navigation**: Agent đọc `index.md` trước để xác định các trang liên quan, sau đó mới "khoan sâu" vào nội dung chi tiết. Điều này thay thế cho hạ tầng RAG phức tạp.
2.  **Context Assembly**: Tập hợp các trang đã chọn vào cửa sổ ngữ cảnh theo tỷ lệ ngân sách (60% wiki, 20% history).
3.  **Synthesis with Citations**: Trả lời câu hỏi bằng cách trích dẫn trực tiếp ID trang: `[[CONCEPT_...]]`.
4.  **Save to Wiki Loop**: Các câu trả lời có giá trị cao được lưu lại thành một trang Wiki mới (trong `wiki/queries/`), sau đó được "biên dịch" ngược lại để trích xuất các hạt nhân mới.

## 2. Các mẫu cốt lõi (Patterns)
- **Syntactic Delimiters**: Sử dụng các rào chắn ngữ pháp để ép AI chỉ sử dụng nguồn tri thức xác thực.
- **Multi-Step Synthesis**: Quy trình 3 pha (Retrieve -> Audit -> Connect).
- **Graph Traversal**: Lần theo các liên kết `[[target]]` để tìm kiếm sự ảnh hưởng.
- **Recursive Refinement**: Tự động phát hiện và truy vấn các lỗ hổng tri thức còn thiếu.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Lưu trữ một phân tích phức tạp về "Scaling Laws" từ Chat vào `wiki/queries/QUERY_Scaling_Laws_Comparison.md`. Sau đó Agent tự động cập nhật `index.md` để ghi nhận tri thức mới này.
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như một nhà nghiên cứu ghi chép lại kết quả thí nghiệm vào sổ tay thay vì chỉ nhớ trong đầu. Cuốn sổ tay (Wiki) giúp các nghiên cứu sau này không phải lặp lại những sai lầm cũ.


## ## Source Tracing
- **Nguồn**: [[SOURCE_META_NASHUS_LLMWIKI]] — Section 7.2 & 7.3.
- **Nguồn**: [[SOURCE_TOOL_GEMINI_DEVELOPER_CODEX]] — Section 1.3: Structuring Input for Gemini 3.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 20 và chuẩn hóa Source Tracing.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
