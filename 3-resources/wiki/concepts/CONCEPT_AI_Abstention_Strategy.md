---
file_id: CONCEPT_AI_ABSTENTION_STRATEGY
title: "Abstention Strategy (Hallucination Mitigation)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@scout"
status: "verified"
source: "[[SOURCE_AIMET_AGENTIC_ROADMAP_2026]]"
---

# Abstention Strategy (Hallucination Mitigation)

## Core Principle
Abstention Strategy (Chiến lược giữ im lặng) là cơ chế cho phép Agent từ chối trả lời khi nó nhận thấy không đủ dữ liệu tin cậy hoặc yêu cầu nằm ngoài phạm vi tri thức. Mục tiêu tối thượng là ngăn chặn **Hallucination** (Ảo giác) - một trong những rủi ro lớn nhất của AI.

## Các kỹ thuật triển khai
1. **Threshold-based**: Chỉ trả lời nếu điểm tin cậy (Confidence Score) hoặc độ tương đồng của RAG vượt quá một ngưỡng nhất định.
2. **Explicit Instructions**: Sử dụng System Prompt: "Nếu thông tin không có trong tài liệu được cung cấp, hãy nói 'Tôi không biết', tuyệt đối không dùng kiến thức bên ngoài."
3. **Verification Layer**: Sử dụng một Agent thứ hai (Critic) để kiểm tra xem câu trả lời của Agent thứ nhất có thực sự dựa trên bằng chứng (Grounded) hay không.

## Kỹ thuật nâng cao (Advanced Patterns)
*(Nguồn: [[SOURCE_OFFICIAL_LangGraph_Concepts]] — Section: Recursion limit)*

4. **Recursion Limit (Giới hạn đệ quy)**: Cơ chế đặt ngưỡng tối đa cho số bước (super-steps) mà đồ thị có thể thực hiện trong một lần chạy. Khi chạm ngưỡng, hệ thống sẽ ném ra lỗi `GraphRecursionError`. 
5. **Proactive Recursion Handling (Xử lý chủ động)**: Sử dụng giá trị quản lý `RemainingSteps` để theo dõi số bước còn lại. Điều này cho phép Agent thực hiện chiến lược **Abstention** (từ chối tiếp tục vòng lặp) một cách duyên dáng (Graceful degradation) trước khi bị ép buộc dừng bởi hệ thống.

## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Một Agent nghiên cứu thị trường nhận thấy mình đã thực hiện 98/100 bước cho phép. Thay vì tiếp tục tìm kiếm (có nguy cơ bị ngắt giữa chừng), nó sử dụng `RemainingSteps` để nhận biết và chuyển sang Node "Tổng hợp kết quả cuối cùng" (Fallback Node) để trả về những gì đã có. (Nguồn: [[SOURCE_OFFICIAL_LangGraph_Concepts]] — Section: Proactive recursion handling).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như một **Nhân chứng tại tòa (Witness)**: Họ phải thề rằng "chỉ nói sự thật và không gì khác ngoài sự thật". Nếu họ không trực tiếp chứng kiến sự việc, họ phải trả lời "Tôi không biết" hoặc "Tôi không biết" để tránh làm sai lệch công lý.

## 4F Reflection
- **Facts**: Việc bắt AI thừa nhận "không biết" thực chất khó hơn việc bắt nó trả lời, vì các mô hình thường được huấn luyện để làm hài lòng người dùng.
- **Feelings**: Một Agent biết nói "Không biết" mang lại cảm giác đáng tin cậy hơn nhiều so với một Agent luôn khẳng định mình biết mọi thứ.
- **Findings**: Abstention là tính năng bắt buộc cho các hệ thống Agentic AI trong môi trường doanh nghiệp (Enterprise-grade).
- **Futures**: Xu hướng "Self-Correction" sẽ cho phép Agent sau khi Abstain sẽ tự động đi tìm nguồn tri thức mới để có thể trả lời trong lần sau.

## Nguồn tham khảo
- Web Research — [[SOURCE_META_LLM_WIKI_V2]] — Section: Reliability & Trust.
