---
file_id: CONCEPT_AI_AGENT_REASONING_PATTERNS
title: "Agent Reasoning Patterns (Các mẫu suy luận của Agent)"
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
Trang này tổng hợp các Mẫu suy luận (Reasoning Patterns) phổ biến trong kiến trúc Agent. Việc lựa chọn đúng mẫu suy luận quyết định khả năng giải quyết vấn đề phức tạp của AI. Chúng ta chuyển từ việc để AI tự do suy nghĩ sang việc định hướng nó thông qua các cấu trúc như lập kế hoạch trước khi thực hiện (Planning) hoặc kiểm tra chéo kết quả (Verification).

## ## Key Claims / Summary
1.  **ReAct Pattern**: Kết hợp giữa suy luận (Thought), hành động (Action) và quan sát (Observation) theo vòng lặp.
2.  **Planning vs Execution**: Tách biệt pha lập kế hoạch (chọn Tool, dự kiến bước đi) và pha thực thi thực tế để tăng tính an toàn.
3.  **Self-Correction**: Khả năng của Agent trong việc nhận diện lỗi (như sai schema) và tự động sửa đổi đầu vào dựa trên phản hồi của hệ thống.

## 1. Các mẫu tiêu biểu
- **Dry-run pattern**: Agent mô phỏng hành động trước khi thực hiện thật (đặc biệt quan trọng với các tool có tác động vật lý/tài chính).
- **Reflection / Critic**: Một Agent thứ hai hoặc một bước phụ để đánh giá chất lượng câu trả lời trước khi gửi cho người dùng.
- **Decomposition**: Chia nhỏ một yêu cầu phức tạp thành các nhiệm vụ con (Sub-tasks).

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ kỹ thuật (Original)**: Sử dụng mẫu ReAct để Agent có thể vừa suy nghĩ vừa gọi Tool tìm kiếm. Nếu kết quả tìm kiếm không đủ, Agent sẽ tự động điều chỉnh câu truy vấn và thực hiện lại bước quan sát cho đến khi đủ thông tin để trả lời. (Nguồn: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 9).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như một học sinh giải bài toán đố. Thay vì viết ngay đáp số, học sinh được yêu cầu: (1) Phân tích đề bài (Thought), (2) Viết phép tính (Action), (3) Kiểm tra lại xem đáp số có hợp lý không (Observation). Nếu thấy sai, học sinh sẽ làm lại bước 1.

## ## Source Tracing
- **Nguồn**: [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] — Section 9: Agents & Multi-Agents.

## ## History / Revisions
- **2026-05-03**: [@engineer] Ingested from Agentic AI Roadmap 2026.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
