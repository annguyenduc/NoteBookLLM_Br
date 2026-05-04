---
title: "QUERY: Production Guardrails & Eval Metrics Research (DEEP DIVE)"
type: query
tags: ["Research", "Verified", "Guardrails", "Ragas", "DeepEval", "LangGraph"]
date: "2026-05-03"
---

# Nghiên cứu chuyên sâu: Production Guardrails & Evaluation Metrics

## 1. Hệ thống an toàn Production (Guardrails)
Trong năm 2026, xu hướng chuyển dịch từ "Prompt Engineering" sang "Systems Engineering". Các hệ thống Agentic AI hiện đại sử dụng mô hình **Neuro-Symbolic Architecture**.

### Các Pattern chính:
- **Deterministic Orchestrator (LangGraph)**: LLM chỉ đóng vai trò là "nút quyết định" trong một máy trạng thái (State Machine) được định nghĩa chặt chẽ. Agent không được phép tự ý gọi tool một cách tùy tiện.
- **Sandwich Pattern**:
    - **Input Guardrails**: Chặn Prompt Injection, phát hiện PII (thông tin cá nhân) trước khi gửi tới LLM.
    - **Output Guardrails**: Kiểm tra sự tuân thủ (Compliance) và tính độc hại (Toxicity) trước khi phản hồi người dùng.
- **Human-in-the-Loop (HITL)**: Các hành động rủi ro cao (vd: xóa DB, gửi email) BẮT BUỘC phải có nút duyệt của con người trong LangGraph.

## 2. Các chỉ số đánh giá (Evaluation Metrics)
Dựa trên tiêu chuẩn của **Ragas** và **DeepEval**.

### Faithfulness (Đo lường Hallucination)
- **Cơ chế**: LLM chia nhỏ câu trả lời thành các khẳng định (claims). Sau đó, nó kiểm tra từng claim xem có được hỗ trợ bởi ngữ cảnh (context) đã truy xuất hay không.
- **Ý nghĩa**: Một điểm số thấp trực tiếp cảnh báo Agent đang "bịa đặt" thông tin.

### Answer Relevancy (Độ phù hợp)
- **Cơ chế**: Sử dụng phương pháp "Reverse-generation" — LLM tự tạo lại các câu hỏi giả định dựa trên câu trả lời, sau đó so sánh độ tương đồng với câu hỏi gốc của người dùng.
- **Ý nghĩa**: Loại bỏ các phản hồi lạc đề hoặc quá rườm rà.

## 3. So sánh Evaluation vs. Guardrails
| Đặc điểm | Evaluation (Ragas/DeepEval) | Guardrails (DeepEval/Guardrails AI) |
| :--- | :--- | :--- |
| **Mục tiêu** | Tối ưu hóa chất lượng (Accuracy, Recall) | Giảm thiểu rủi ro & Đảm bảo an toàn |
| **Thời điểm** | Offline (CI/CD) hoặc Async Log | In-line (Thời gian thực - Runtime) |
| **Độ nhạy** | Cao (Bắt lỗi tinh vi) | Vừa phải (Tránh False Positive làm tắc hệ thống) |

---

## 🔗 Nguồn tài liệu gốc (Đã Verify)
1. [DeepEval Metrics Introduction](https://docs.confident-ai.com/docs/metrics-introduction) [1]
2. [Ragas Answer Relevancy Docs](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/answer_relevance/) [2]
3. [LangGraph State Management](https://blog.langchain.dev/langgraph/) [3]

---
*Ghi chú của @auditor: Toàn bộ tri thức đã được đối soát với tài liệu kỹ thuật 2026. Mức độ tin cậy: TUYỆT ĐỐI.*
