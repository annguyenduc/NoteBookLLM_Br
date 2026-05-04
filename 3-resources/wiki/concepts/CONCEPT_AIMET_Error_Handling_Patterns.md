file_id: CONCEPT_AIMET_ERROR_HANDLING_PATTERNS
title: "Error Handling Patterns (Retries, Fallbacks & Guard Edges)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-02"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_AIMET_Agentic_AI_Roadmap_2026]]"
---

## ## For future Claude
Trang này tổng hợp các kỹ thuật xử lý lỗi trong kiến trúc Agentic AI, nơi lỗi không chỉ là crash hệ thống mà còn bao gồm lỗi logic, lỗi parse output và hallucination. Chúng ta xây dựng các hệ thống "Tự phục hồi" (Self-Healing) dựa trên các vòng lặp phản hồi (Feedback Loops) và các đường rẽ nhánh an toàn (Guard Edges).

## ## Key Claims / Summary
1.  **Resilience over Perfection**: Chấp nhận LLM có thể sai và xây dựng hệ thống bao quanh để phát hiện và sửa sai.
2.  **Feedback Loops**: Sử dụng kết quả lỗi làm input cho lượt thực thi tiếp theo (Self-Correction).
3.  **Human-in-the-loop**: Thiết lập các điểm "Escalation" khi hệ thống không thể tự giải quyết sau một số lượt thử nhất định.

## 1. Định nghĩa

## ## Detailed Analysis
**Error Handling Patterns** trong hệ thống Agentic AI là các thiết kế chiến lược nhằm đảm bảo hệ thống không bị sụp đổ khi gặp lỗi (hallucination, API timeout, parsing error) mà có thể tự phục hồi hoặc dừng lại một cách an toàn.

## 2. Các Pattern chính (Rule 3: Knowledge Compounding)

### A. Exponential Backoff (Retry Policy)
- **Cơ chế**: Khi gặp lỗi tạm thời (Transient failures), hệ thống sẽ thử lại với thời gian chờ tăng dần (vd: 1s, 2s, 4s...).
- **Ứng dụng**: Thường được tích hợp sẵn trong [[CONCEPT_AIMET_Runnables]].

### B. Fallback Mechanism
- **Cơ chế**: Nếu Model A thất bại, hệ thống tự động chuyển sang Model B (thường là model rẻ hơn, nhanh hơn hoặc ổn định hơn).
- **Ứng dụng**: Tránh việc dừng toàn bộ pipeline chỉ vì một bước parse JSON lỗi.

### C. Repair Node (Self-Correction)
- **Cơ chế**: Trong một Graph ([[ENTITY_AIMET_LangGraph]]), nếu kết quả không đạt validation, dữ liệu được gửi tới một "Repair Node" kèm theo thông báo lỗi để Agent tự sửa.
- **Ứng dụng**: Agent nhận được feedback: "JSON thiếu trường 'city', hãy tạo lại".

### D. Guard Edges (Loop Prevention)
- **Cơ chế**: Sử dụng điều kiện chặn để kiểm soát số lần lặp. Nếu `retry_count > max_steps`, chuyển sang luồng "Escalation" (hỏi con người).

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Thiết kế workflow cho Agent gọi API thời tiết.
> **Ứng dụng**: Phân loại lỗi: Timeout API -> Retry; Sai tham số -> Repair Node; Model hallucinate -> Fallback to human.
> **Nguồn**: [[SOURCE_AIMET_Agentic_AI_Roadmap_2026]] — Section 4.3 & 4.6

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Dạy học sinh về "Sự kiên trì" thông qua lập trình Robot.
> **Ứng dụng**: Thiết kế code cho Robot gặp chướng ngại vật:
> 1. Thử lại (Retry): Lùi lại và đi tiếp.
> 2. Tìm đường khác (Fallback): Rẽ trái/phải.
> 3. Kêu cứu (Escalation): Phát tiếng beep nếu kẹt quá 3 phút.
> Đây là cách dạy tư duy giải quyết vấn đề (Computational Thinking) một cách trực quan.

---
**Nguồn**: [[SOURCE_AIMET_Agentic_AI_Roadmap_2026]] — Section 4.3, 4.6


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
