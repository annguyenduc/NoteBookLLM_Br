---
file_id: CONCEPT_AI_KNOWLEDGE_CUTOFF
title: "Knowledge Cutoff (Giới hạn tri thức tĩnh)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-03"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_coursera-AI-essential-Bias_Drift_Knowledge_Cutoff]]"
  - "[[SOURCE_coursera-AI-essential-Stay_up_to_date_with_AI]]"
---

## ## For future Claude
Trang này giải thích khái niệm "Knowledge Cutoff" - thời điểm cuối cùng mà một mô hình LLM được huấn luyện. Mọi sự kiện diễn ra sau thời điểm này sẽ không được mô hình biết đến một cách tự nhiên trừ khi được cung cấp qua RAG hoặc Search. Việc nắm rõ cutoff của từng mô hình là tối quan trọng để tránh hallucination về các sự kiện gần đây.

## ## Key Claims / Summary
1.  **Static Brain**: LLM là các thực thể tri thức tĩnh, không tự cập nhật dữ liệu thời gian thực sau khi quá trình pre-training kết thúc.
2.  **Date Awareness**: Người dùng cần kiểm tra ngày cutoff của mô hình (ví dụ: GPT-4o, Gemini 1.5 Pro) trước khi thực hiện các tác vụ liên quan đến tin tức hoặc công nghệ mới.
3.  **RAG Solution**: Kỹ thuật Retrieval-Augmented Generation (RAG) là giải pháp chính để vượt qua giới hạn cutoff này.

## ## Ví dụ đối chiếu (Rule 17)
-   **Ví dụ thực tế (Original)**: Một mô hình có cutoff vào tháng 1/2024 sẽ không biết về một thư viện Python mới ra mắt vào tháng 3/2024. Nếu hỏi về nó, mô hình có thể bịa đặt (hallucinate) ra cú pháp dựa trên các thư viện tương tự.
-   **Ẩn dụ sư phạm (Pedagogical)**: Giống như một cuốn bách khoa toàn thư đã được in ấn và đóng tập. Bạn có thể tra cứu mọi thứ trong đó, nhưng nếu có một quốc gia mới được thành lập sau ngày cuốn sách được in, bạn sẽ không bao giờ tìm thấy nó trong các trang giấy đó trừ khi bạn kẹp thêm một tờ báo mới vào giữa các trang sách (RAG).

## ## Detailed Analysis
Knowledge Cutoff ảnh hưởng trực tiếp đến độ tin cậy của AI trong các lĩnh vực thay đổi nhanh như:
- **Lập trình**: Các bản cập nhật API, framework mới.
- **Kinh tế/Chính trị**: Chỉ số thị trường, sự kiện thế giới.
- **Y tế/Khoa học**: Các nghiên cứu vừa công bố.

Để đối phó, các Agent hiện đại thường sử dụng:
1. **System Prompt Injection**: Thông báo ngày hiện tại cho mô hình.
2. **Web Search Tools**: Cho phép mô hình truy cập internet.
3. **Internal Wiki (NoteBookLLM_Br)**: Cung cấp ngữ cảnh cục bộ mới nhất.

## ## Relationships
- `relates_to` -> [[CONCEPT_AI_Bias_and_Ethics]]
- `mitigated_by` -> [[CONCEPT_AIMET_RAG_Systems]]
- `causes` -> [[CONCEPT_META_Information_Overload]] (nếu không được kiểm soát)

## ## Source Tracing
- **Nguồn**: [[SOURCE_coursera-AI-essential-Bias_Drift_Knowledge_Cutoff]] — Section: LLM Limitations.
- **Nguồn**: [[SOURCE_coursera-AI-essential-Stay_up_to_date_with_AI]] — Concept: Understanding AI constraints.

## ## History / Revisions
- **2026-05-03**: [@engineer] Chuyển đổi từ stub sang verified, bổ sung Rule 17 và Rule 20.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
