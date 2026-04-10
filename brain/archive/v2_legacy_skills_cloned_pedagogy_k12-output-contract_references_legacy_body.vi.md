# 📐 STEAM Output Contract (PRO v1.10)

> **Goal:** Áp dụng các tiêu chí định lượng nghiêm ngặt để tự đánh giá (Audit) chất lượng bài học, unit, và rubric. Đảm bảo mọi output đạt chuẩn "System Design for AI" và "Invisible Excellence".

## 📊 1. Quality Scoring Rubric (Thresholds)
*Mọi sản phẩm phải đạt tổng điểm ≥ 80% để được duyệt publish.*

| Tiêu chí | Trọng số | Ngưỡng Đạt (Threshold) | Cách đo lường |
|---|---|---|---|
| **Bloom Level** | 20% | ≥ Level 3 (Apply) | Phải có ít nhất 2 động từ dẫn thuộc mức Áp dụng trở lên. |
| **Active Learning**| 30% | **Quy tắc 37/63** | Trainer nói ≤ 37%. Hoạt động HS ≥ 63%. |
| **EDP/5E Flow** | 20% | 100% logic | Các bước phải có sự kết nối (Vd: Explain phải giải thích được hiện tượng ở Explore). |
| **UNESCO / ISTE** | 20% | Level 2 (Deepen) | Phải tích hợp khung năng lực AI UNESCO hoặc chuẩn ISTE. |
| **Invisible Std.** | 10% | Tuyệt đối | KHÔNG xuất hiện thuật ngữ sư phạm trong nội dung cho HS. |

## 🏗️ 2. Detailed Audit Checklist

### 2.1 Đối với Giáo án (Lesson Plan)
- [ ] **Mục tiêu ABCD:** Có đủ Audience, Behaviour, Condition, Degree?
- [ ] **Tỉ lệ 5E:** Pha **Explore** có chiếm ≥ 40% thời lượng không?
- [ ] **Ẩn dụ (Analogy):** Có ít nhất 1 ẩn dụ cho mỗi khái niệm kỹ thuật khó? (Tham khảo `k12-examples-bank`).

### 2.2 Đối với Hệ thống Đánh giá (Assessment)
- [ ] **MCQ:** Có ít nhất 1 phương án gây nhiễu (Distractor) dựa trên hiểu lầm thực tế?
- [ ] **Rubric:** Các tiêu chí có định lượng (Số lượng, thời gian, bằng chứng) thay vì tính từ cảm tính?
- [ ] **Error Analysis:** Có yêu cầu HS giải thích "Tại sao lỗi xảy ra" thay vì chỉ "Sửa lỗi"?

### 2.3 Tiêu chuẩn UNESCO & Năng lực Giáo viên (ToT)
- [ ] **Human-centric:** Module có phần thảo luận về trách nhiệm của con người khi dùng AI không?
- [ ] **Ready to Teach:** GV có được luyện tập xử lý ít nhất 2 tình huống sư phạm thực tế?
- [ ] **Error Analysis:** Có yêu cầu HS/GV giải thích "Tại sao lỗi xảy ra" thay vì chỉ "Sửa lỗi"?
- [ ] **Assessment:** Bài kiểm tra năng lực có đủ 3 phần: Kiến thức, Kỹ năng Pipeline, và Sư phạm?

## 🚨 3. Quality Gate (Red Flags)
- ❌ **Qualitative words:** Sử dụng từ "tốt", "hay", "đẹp" trong rubric mà không có ranh giới đo lường.
- ❌ **Jargon Leak:** Để lộ các thuật ngữ "Bloom", "SAMR" trong slide dành cho học sinh.
- ❌ **Passive Learning:** Slide thuyết giảng chiếm > 40% thời lượng module.

---
## 💡 Example Triggers
- "audit sản phẩm bài dạy chatbot"
- "kiểm tra chất lượng rubric dự án robot"
- "đánh giá module ToT theo chuẩn UNESCO"
- "self-check tiêu chuẩn ngầm cho bài học AI"
