---
id: THINK_Data_Story_Structure
type: concept
aliases: ["Data Story Structure", "CoNVO", "Cấu trúc Kể chuyện Dữ liệu", "Scoping"]
tags: ["data-thinking", "storytelling", "scoping", "communication"]
---

# Cấu trúc Kể chuyện Dữ liệu (Data Story Structure / CoNVO)

Nguồn: [[SOURCE_THINK_Thinking_with_Data]] (Xác nhận Rule 14 từ: [[\THINK_Thinking_with_Data]])

## 1. Khái niệm cốt lõi
Một dự án khoa học dữ liệu không chỉ là quá trình chạy các thuật toán, mà cốt lõi là việc **kể một câu chuyện** thuyết phục thông qua dữ liệu. Tác giả khẳng định: "Một câu chuyện hay về một dự án và một phạm vi dự án (scope) tốt là khó có thể phân biệt được."

Để cấu trúc câu chuyện dữ liệu, ta sử dụng khung **CoNVO**, bao gồm 4 thành phần kết nối chặt chẽ với nhau (như đã thấy trong các case study ở Chương 6):
1. **Context (Bối cảnh):** Mô tả tổ chức, bối cảnh kinh doanh hoặc tình huống hiện tại.
2. **Need (Nhu cầu):** Vấn đề cụ thể cần giải quyết hoặc quyết định cần đưa ra (Ví dụ: Công ty đang tốn quá nhiều tiền quảng cáo vào những người dùng không chuyển đổi).
3. **Vision (Tầm nhìn):** Bản phác thảo (mockup) về những gì sẽ được tạo ra (biểu đồ, mô hình, ứng dụng) và nó sẽ trông như thế nào.
4. **Outcome (Kết quả):** Hành động thực tế sẽ xảy ra sau khi sản phẩm dữ liệu được giao (Ai sẽ dùng nó? Dùng như thế nào để thay đổi thực tế?).

 Nguồn: `[[SOURCE_THINK_Thinking_with_Data]]` — Chương 1: Scoping (Trang 16) & Chương 6: Putting It All Together.

## 2. Ứng dụng & Ví dụ (Double Examples)

**Ví dụ Gốc (Original):**
Trong dự án dự đoán tỷ lệ chuyển đổi cho công ty phần mềm (Chương 6):
- *Context:* Công ty cho dùng thử 30 ngày và chạy quảng cáo nhắm mục tiêu.
- *Need:* Cần rút ngắn vòng lặp phản hồi 30 ngày xuống vài ngày để cắt giảm quảng cáo vô ích.
- *Vision:* Một mô hình dự đoán giá trị vòng đời (LTV) của user trong những ngày đầu tiên và xuất ra một báo cáo ước tính.
- *Outcome:* Đội ngũ kỹ sư tích hợp mô hình, tự động dừng các chiến dịch quảng cáo kém hiệu quả, tiết kiệm hàng ngàn đô la.
 Nguồn: `[[SOURCE_THINK_Thinking_with_Data]]` — Chương 6: Putting It All Together (Trang 67-69).

**Ví dụ Sư phạm (Pedagogical) [Phóng tác]:**
Trong dự án học tập Project-Based Learning (PBL) về rác thải trường học:
Học sinh thường có xu hướng nhảy ngay vào vẽ biểu đồ tròn các loại rác. Giáo viên hướng dẫn học sinh dùng khung CoNVO để kể chuyện:
- *Context:* Trường đang trả phí thu gom rác rất cao.
- *Need:* Cần bằng chứng để biết khu vực nào vứt nhiều rác tái chế nhất.
- *Vision:* Một bản đồ nhiệt (heatmap) thể hiện sự lãng phí rác tái chế tại các thùng rác.
- *Outcome:* Trình bày bản đồ này cho Ban Giám hiệu để xin ngân sách mua thêm thùng rác phân loại đặt đúng điểm "nóng".

## 3. Liên kết liên quan
- `[[CONCEPT_THINK_Audience_Framing]]`: Đặt câu chuyện vào đúng khung nhận thức của khán giả.
- `[[CONCEPT_THINK_Exploration_vs_Confirmation]]`: Tầm nhìn (Vision) là kim chỉ nam trong quá trình thăm dò dữ liệu.
