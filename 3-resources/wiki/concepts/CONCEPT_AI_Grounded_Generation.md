---
file_id: CONCEPT_AI_GROUNDED_GENERATION
title: "Grounded Generation (Sinh nội dung có căn cứ)"
category: "Wiki Page"
prefix: "AI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-03"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_AIMET_AGENTIC_ROADMAP_2026]]"
---

## ## For future Claude
Trang này định nghĩa nguyên tắc Grounding (Căn cứ hóa) - kỹ thuật đảm bảo câu trả lời của AI luôn dựa trên bằng chứng thực tế từ nguồn dữ liệu được cung cấp. Trong hệ thống Wiki của chúng ta, Grounding là xương sống giúp duy trì tính xác thực và khả năng truy vết nguồn (Source Tracing - Rule 14). Mục tiêu là biến AI từ một kẻ "biết tuốt" mang tính phỏng đoán thành một trợ lý nghiên cứu trung thực.

## ## Key Claims / Summary
1.  **Citation Integrity**: Mọi khẳng định của AI phải đi kèm với tham chiếu trực tiếp đến đoạn văn bản nguồn (ví dụ: `[[SOURCE_...]]: Section 1.2`).
2.  **Hallucination Check**: Ép Agent phải thừa nhận "Tôi không tìm thấy thông tin trong nguồn được cung cấp" thay vì tự ý bịa đặt.
3.  **Strict Delimiters**: Sử dụng các rào chắn kỹ thuật (như XML tags) để tách biệt tri thức nội tại của LLM và tri thức từ RAG.

## 1. Các kỹ thuật áp dụng
- **Source Verification**: Agent tự kiểm tra lại xem nội dung nó vừa viết có thực sự nằm trong nguồn không trước khi trình bày.
- **Fact Extraction**: Trích xuất các sự kiện (facts) từ nguồn trước khi bắt đầu tổng hợp câu trả lời.
- **Negative Constraints**: "Chỉ trả lời dựa trên nội dung trong ngoặc đơn, nếu không có hãy trả về [NONE]".

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ kỹ thuật (Original)**: Trong hệ thống Wiki 2.0, Agent được yêu cầu viết Concept. Nó phải trích xuất các câu trích dẫn (Quotes) từ file raw PDF và dán vào mục "Source Tracing". Nếu Agent không tìm thấy đoạn văn nào phù hợp, nó sẽ đánh dấu trang đó là `status: stub` để người dùng kiểm tra lại. (Nguồn: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 5).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như một luật sư đang tranh tụng tại tòa. Mọi cáo buộc hoặc lý lẽ đưa ra phải đi kèm với "Bằng chứng số..." (Source). Nếu luật sư tự ý kể một câu chuyện hấp dẫn nhưng không có bằng chứng, thẩm phán (Hệ thống) sẽ bác bỏ ngay lập tức.

## ## Source Tracing
- **Nguồn**: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 5: RAG Systems.

## ## History / Revisions
- **2026-05-03**: [@engineer] Ingested from Agentic AI Roadmap 2026.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
