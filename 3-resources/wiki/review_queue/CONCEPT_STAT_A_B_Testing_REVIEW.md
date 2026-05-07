---
title: CONCEPT STAT A B Testing
status: DRAFT
file_id: CONCEPT_STAT_A_B_Testing
---

---
file_id: CONCEPT_STAT_A_B_Testing
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
tags: ["Statistics", "Experimentation", "Product_Development"]
source: "[[SOURCE_STAT_Practical_Statistics_for_Data_Scientists]]"
created: "2026-05-03"
---

# Concept: A/B Testing (Statistical Experimentation)

## 1. Core Principle (Bản chất cốt lõi)
A/B Testing là một phương pháp thực nghiệm so sánh hai phiên bản (A - Đối chứng và B - Thử nghiệm) để đo lường tác động của một thay đổi cụ thể. Nguyên tắc then chốt là **Sự ngẫu nhiên (Randomization)** để loại bỏ nhiễu và **Kiểm định giả thuyết** để phân biệt giữa biến động ngẫu nhiên và tác động thực tế.

## 2. Ví dụ đối chiếu (Rule 17 - Double Examples)

### Ví dụ 1: Trích dẫn kỹ thuật (Original Context)
Trong khoa học dữ liệu, chúng ta không chỉ nhìn vào p-value mà còn phải xem xét **Ý nghĩa thực tế (Practical Significance)**.
- **Kịch bản**: Thử nghiệm màu nút bấm trên 10,000 khách hàng. Nhóm B tăng 0.5% tỷ lệ chuyển đổi.
- **Phân tích**: p-value < 0.05 (có ý nghĩa thống kê), nhưng nếu chi phí kỹ thuật để đổi màu nút lớn hơn lợi nhuận từ 0.5% đó mang lại, thì kết quả này **không có ý nghĩa thực tế**.
**Nguồn**: `SOURCE_STAT_Practical_Statistics_for_Data_Scientists` — Section "Statistical vs Practical Significance"

### Ví dụ 2: Ẩn dụ sư phạm (Pedagogical Application)
Hãy tưởng tượng bạn đang thử nghiệm **"Một loại phân bón mới cho cây lúa"**.
- **Cánh đồng A (Control)**: Dùng phân bón cũ.
- **Cánh đồng B (Treatment)**: Dùng phân bón mới.
Bạn phải đảm bảo hai cánh đồng có cùng loại đất, cùng lượng nước và được gieo hạt ngẫu nhiên. Nếu cuối vụ, cánh đồng B cho năng suất cao hơn đáng kể so với những biến động tự nhiên hàng năm, bạn mới có thể kết luận phân bón mới hiệu quả.

## 3. 4F Reflection
- **Facts**: A/B Testing yêu cầu xác định cỡ mẫu (Sample Size) trước khi thực hiện để đảm bảo sức mạnh thống kê (Statistical Power).
- **Feelings**: Nhiều người thường vội vàng kết luận khi thấy đồ thị nhóm B đi lên, nhưng đó có thể chỉ là sự may mắn ngẫu nhiên.
- **Findings**: Khoảng tin cậy (Confidence Intervals) cung cấp nhiều thông tin hơn là một con số p-value đơn lẻ vì nó cho thấy mức độ không chắc chắn.
- **Futures**: Ứng dụng trong việc tối ưu hóa lộ trình học tập (Learning Path) trên nền tảng giáo dục bằng cách thử nghiệm các trình tự bài giảng khác nhau.

---
Nguồn: [[SOURCE_STAT_Practical_Statistics_for_Data_Scientists]]
[[CONCEPT_STAT_Hypothesis_Testing_PValue]]


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
