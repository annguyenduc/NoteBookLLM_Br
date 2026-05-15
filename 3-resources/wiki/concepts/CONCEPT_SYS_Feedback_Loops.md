---
file_id: "CONCEPT_SYS_Feedback_Loops"
title: "Feedback Loops (Vòng lặp phản hồi)"
type: "concept"
status: "DRAFT"
tags:
  - "Systems_Thinking"
  - "Architecture"
  - "Control_Theory"
ai-first: true
confidence: 0.9
learning_source: true
source_file: "ARCH_Thinking_in_Systems.pdf"
source_ref: "Chapter 1: The Basics"
last_reconciled: "2026-05-10"
created: "2026-05-10"
last_updated: "2026-05-10"
---

## For future Claude (AI Preamble)
> Vòng lặp phản hồi là cơ chế tự điều chỉnh của mọi hệ thống. Trong Agentic Systems, đây chính là "Self-Correction" hoặc "Reflection Loop". Nếu không có vòng lặp cân bằng, Agent có thể rơi vào trạng thái ảo giác (hallucination) vô hạn.

# Feedback Loops (Vòng lặp phản hồi)

## 1. Định nghĩa (Definition)
Vòng lặp phản hồi là một cấu trúc đóng (closed chain) của các mối quan hệ nguyên nhân - kết quả, trong đó thông tin về kết quả của một hành động được đưa ngược trở lại để ảnh hưởng đến hành động tiếp theo.

## 2. Hai loại vòng lặp chính (Two Types of Loops)
- **Balancing Feedback Loop (Vòng lặp cân bằng)**:
    - Mục tiêu: Duy trì sự ổn định hoặc hướng tới một mục tiêu xác định.
    - Ví dụ: Bộ nhiệt độ (thermostat), cơ chế kiểm soát lỗi (error correction).
- **Reinforcing Feedback Loop (Vòng lặp tăng cường)**:
    - Mục tiêu: Tạo ra sự tăng trưởng hoặc suy giảm theo cấp số nhân.
    - Ví dụ: Lãi suất kép, sự lan truyền của tin đồn, hiệu ứng mạng.

## 3. Vai trò trong thiết kế hệ thống (Role in Architecture)
Hệ thống bền vững cần sự kết hợp khéo léo giữa cả hai:
- Tăng cường để phát triển.
- Cân bằng để không bị mất kiểm soát (overshoot).

## 4. Ví dụ đối chiếu (R18: Double Examples)
### Ví dụ từ nguồn (Original)
> "A feedback loop is a closed chain of causal connections from a stock, through a set of decisions or physical laws that control a flow, and back to the stock." (Meadows, Thinking in Systems).

### Ứng dụng sư phạm (Pedagogical)
Khi triển khai một Agent giải quyết bài toán code (Coder Agent):
- **Reinforcing Loop**: Agent viết code -> Test pass -> Agent tự tin tiếp tục viết module tiếp theo (Tăng trưởng tiến độ).
- **Balancing Loop**: Agent viết code -> Test fail -> Agent nhận lỗi (feedback) -> Agent sửa code (Duy trì tính đúng đắn).

## 5. Các khái niệm liên quan (Related Atoms)
- [[CONCEPT_SYS_Stocks_And_Flows]]: Thành phần cấu tạo nên vòng lặp.
- [[CONCEPT_SYS_Leverage_Points]]: Nơi vòng lặp có thể bị tác động mạnh nhất.

---
*Phiên bản Template V3.0 (Language Aligned).*
