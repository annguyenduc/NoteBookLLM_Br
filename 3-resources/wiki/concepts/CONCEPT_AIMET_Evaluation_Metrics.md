---
file_id: CONCEPT_AIMET_EVALUATION_METRICS
title: "Evaluation Metrics (Agentic AI)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-02"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_AIMET_Agentic_AI_Roadmap_2026]]"
  - "[[QUERY_Production_Guardrails_Research]]"
---

## ## For future Claude
Trang này định nghĩa các chỉ số đo lường (metrics) chuyên biệt cho Agentic AI, vượt xa các chỉ số NLP truyền thống như BLEU hay ROUGE. Chúng ta tập trung vào việc đánh giá "Khả năng suy luận" (Reasoning) thông qua Lộ trình (Trajectory) và "Độ tin cậy" (Faithfulness) thông qua các framework như RAGAS và DeepEval. Đây là "la bàn" để điều chỉnh prompt và kiến trúc hệ thống Agent.

## ## Key Claims / Summary
1.  **Trajectory over Output**: Đánh giá cách Agent đi đến kết quả (Trajectory) quan trọng hơn bản thân kết quả cuối cùng.
2.  **RAGAS/DeepEval Standard**: Sử dụng các chỉ số dựa trên LLM (LLM-as-a-judge) để đánh giá độ trung thực và tính liên quan.
3.  **Continuous Evaluation**: Tích hợp đánh giá vào CI/CD để ngăn chặn sự sụt giảm chất lượng (regression).

## ## Ví dụ đối chiếu (Rule 17)
-   **Ví dụ thực tế (Original)**: Sử dụng chỉ số `Faithfulness` trong RAGAS để đo lường xem bao nhiêu phần trăm câu trả lời của Agent được chứng minh trực tiếp bởi tài liệu truy xuất (Context). Nếu chỉ số < 0.8, Agent đang có dấu hiệu "bịa đặt" (hallucination).
-   **Ẩn dụ sư phạm (Pedagogical)**: Giống như việc chấm điểm một học sinh trong kỳ thi toán. Bạn không chỉ nhìn vào "đáp số" (Output) mà còn phải chấm điểm từng "bước giải" (Trajectory). Nếu đáp số đúng nhưng bước giải sai hoặc không có chứng cứ, bài làm đó vẫn không đạt yêu cầu cao nhất về tư duy logic.

## 1. Tổng quan
Đánh giá Agentic AI yêu cầu một hệ thống chỉ số đa chiều, không chỉ tập trung vào câu trả lời cuối cùng mà còn phải đánh giá cả **Lộ trình suy luận (Trajectory)** của Agent.

## 2. Hệ thống chỉ số (Mô hình 2026)

### Chỉ số Lộ trình (Trajectory Metrics)
Đánh giá cách Agent suy nghĩ và sử dụng công cụ:
- **Plan Quality**: Kế hoạch được tạo ra có logic và đầy đủ các bước không?
- **Tool Correctness**: Agent có chọn đúng công cụ và truyền đúng tham số không?
- **Task Success Rate**: Tỷ lệ hoàn thành nhiệm vụ cuối cùng sau nhiều bước.

### Chỉ số Kết quả (Outcome Metrics - RAG focused)
Đánh giá chất lượng nội dung tạo ra (thường dùng framework RAGAS):
- **Faithfulness (Độ trung thực)**: Câu trả lời có dựa hoàn toàn vào tài liệu nguồn không? (Chống Hallucination).
- **Answer Relevancy (Độ phù hợp)**: Câu trả lời có giải quyết trực tiếp câu hỏi của người dùng không?
- **Context Recall**: Tài liệu được truy xuất có chứa đầy đủ thông tin cần thiết không?

## 3. Frameworks & Implementation

### DeepEval (Kiểm định CI/CD)
- **Sử dụng**: Tích hợp vào pipeline `pytest`.
- **Mục tiêu**: Ngăn chặn sự sụt giảm chất lượng (regression) trước khi merge code.
- **Mẫu**: Chạy `ToolCorrectnessMetric` mỗi khi cập nhật logic Agent.

### RAGAS (Giám sát vận hành)
- **Sử dụng**: Chạy định kỳ trên dữ liệu thực tế (Production Traces).
- **Mục tiêu**: Phát hiện sự thay đổi về hiệu năng (performance drift) theo thời gian.

## 4. Quy trình tối ưu hóa 2026
1. **Accuracy First**: Tối ưu hóa retrieval và prompt.
2. **Evaluation Gates**: Thiết lập các "Cổng chất lượng" tự động trong CI/CD bằng DeepEval.
3. **Live Monitoring**: Giám sát liên tục bằng RAGAS kết hợp với các nền tảng Observability (Langfuse/Arize).

---
**Liên kết**:
- Đối soát với: [[SOURCE_AIMET_Agentic_AI_Roadmap_2026]]
- Thực thi qua: [[CONCEPT_AIMET_Production_Guardrails]]

---
## ## Source Tracing
- **Nguồn**: [[QUERY_Production_Guardrails_Research]] — Section 2: Metrics.
- **Nguồn**: [[SOURCE_AIMET_Agentic_AI_Roadmap_2026]] — Section 5: Evaluation.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 17, 20 và chuẩn hóa metadata.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
