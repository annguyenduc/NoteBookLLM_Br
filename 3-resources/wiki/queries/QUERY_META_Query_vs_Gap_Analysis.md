---
type: query
title: "Phân biệt: Wiki Query Patterns vs [[CONCEPT_META_Wiki_Gap_Analysis|Wiki Gap Analysis]]"
tags: ["Comparison", "Methodology", "Prompt_Engineering", "Governance"]
related: ["CONCEPT_META_Wiki_Query_Patterns", "[[CONCEPT_META_Wiki_Gap_Analysis]]"]
source_tool: "Internal Synthesis (Rule 19)"
status: "verified"
created: "2026-05-01"
---

# Phân biệt: Wiki Query Patterns vs Wiki Gap Analysis

Hai khái niệm này đóng vai trò là hai mặt của một đồng xu trong việc quản trị tri thức tại NoteBookLLM_Br.

## 📊 1. Bảng so sánh chi tiết

| Đặc tính | Wiki Query Patterns (Truy vấn) | Wiki Gap Analysis (Phân tích lỗ hổng) |
| :--- | :--- | :--- |
| **Mục tiêu chính** | **Khai thác** tri thức đã có. | **Phát hiện** tri thức còn thiếu/sai. |
| **Vai trò AI** | Thủ thư (Knowledge Librarian). | Kiểm toán viên (Skeptical Auditor). |
| **Kỹ thuật lõi** | Multi-Step Synthesis, Graph Traversal. | Adversarial Critique, Chain of Verification. |
| **Đầu ra (Output)** | Một câu trả lời tổng hợp, chính xác. | Một danh sách các lỗi, khoảng trống và mâu thuẫn. |
| **Khi nào dùng?** | Khi muốn học hoặc tìm giải pháp từ Wiki. | Khi muốn kiểm tra độ tin cậy của Wiki. |

## 🧩 2. Mối quan hệ tương hỗ (The Feedback Loop)

Trong thực tế, chúng ta nên sử dụng chúng kết hợp theo chu trình:
1.  **Query**: "Tổng hợp cho tôi kiến thức về X từ Wiki."
2.  **Gap Analysis**: "Bắt bẻ lại câu trả lời vừa rồi, tìm xem có giả định nào không có bằng chứng (Rule 14) không?"
3.  **Refinement**: Cập nhật Wiki để lấp đầy lỗ hổng vừa tìm thấy.

## 💡 3. Kết luận
- Dùng **Query Patterns** để **mở rộng** sự hiểu biết.
- Dùng **Gap Analysis** để **thắt chặt** sự chính xác.

---
*Báo cáo được tạo bởi @pm thông qua quy trình @/wiki-query.*
