---
id: THINK_Correlation_vs_Causation
type: concept
aliases: ["Correlation vs Causation", "Nhân quả và Tương quan", "Causality"]
tags: ["data-thinking", "causality", "logic", "statistics"]
---

# Tương quan và Nhân quả (Correlation vs Causation)

<!-- [AUDITOR] Rule 14: Nguồn được lấy trực tiếp từ 3-resources/raw/THINK_Thinking_with_Data.md, tại Chương 5 (Causality), trang 57-66, line 2246-2630. -->

## 1. Khái niệm cốt lõi
Trong phân tích dữ liệu, mục tiêu của suy luận nhân quả (Causal Analysis) không chỉ là tìm ra sự liên quan (correlation) giữa hai biến số, mà là xác định xem một biến có thực sự *gây ra* sự thay đổi ở biến kia hay không, đồng thời loại trừ các **biến gây nhiễu (confounders)**. 

Theo tác giả, vì chúng ta không có khả năng quan sát "nhiều vũ trụ song song" (multiple universes) để xem cùng một sự kiện diễn ra như thế nào dưới các điều kiện khác nhau, chúng ta buộc phải sử dụng các **Thiết kế nghiên cứu (Designs)** để giảm thiểu sự không chắc chắn về nguyên nhân và kết quả.

Có hai nhóm thiết kế chính:
- **Intervention Designs (Thiết kế can thiệp):** Nổi bật nhất là Thử nghiệm ngẫu nhiên có đối chứng (Randomized Controlled Trials). Việc gán ngẫu nhiên nhằm đảm bảo các biến gây nhiễu tiềm ẩn được phân bổ đều. Tuy nhiên, vẫn có giới hạn về tính khái quát (generalizability) khi áp dụng cho các quần thể mới.
- **Observational Designs (Thiết kế quan sát):** Được sử dụng khi việc can thiệp là phi đạo đức, quá tốn kém hoặc không thực tế. Phương pháp phổ biến là tìm kiếm **Thí nghiệm tự nhiên (Natural Experiments)** hoặc sử dụng các mô hình thống kê như đối sánh điểm xu hướng (Propensity Score Matching) để tạo ra các nhóm so sánh nhân tạo.

📖 Nguồn: `[[SOURCE_THINK_Thinking_with_Data]]` — Chương 5: Causality (Trang 57-66).

## 2. Ứng dụng & Ví dụ (Double Examples)

**Ví dụ Gốc (Original):**
Trong môi trường y tế, để kiểm tra tính nhân quả, việc chọn ngẫu nhiên người tham gia để dùng thuốc hoặc giả dược là một dạng can thiệp (Intervention Design). Nhưng khi nghiên cứu tác động của việc từng bị kết án thời trung học đối với thu nhập lúc 25-40 tuổi, ta không thể ép người khác phạm tội. Do đó, tác giả đề xuất một *Thí nghiệm tự nhiên*: So sánh những người từng bị bắt nhưng *không* bị kết án với những người bị bắt *và* bị kết án, nhằm loại trừ bớt các biến gây nhiễu (confounders).
📖 Nguồn: `[[SOURCE_THINK_Thinking_with_Data]]` — Chương 5: Causality (Trang 63-64).

**Ví dụ Sư phạm (Pedagogical) [Phóng tác]:**
Trong lớp học STEM/Toán: Học sinh nhận thấy "khi lượng kem bán ra tăng thì số vụ đuối nước cũng tăng" (Correlation). Giáo viên yêu cầu học sinh thiết kế một "Observational Design" để tìm ra biến gây nhiễu (Confounder). Học sinh sẽ nhận ra "Nhiệt độ mùa hè tăng cao" chính là nguyên nhân gây ra cả hai hiện tượng trên. Nhờ đó, học sinh hiểu rằng không thể đưa ra chính sách "Cấm bán kem để giảm đuối nước".

## 3. Liên kết liên quan
- `[[THINK_Patterns_of_Reasoning]]`: Các mẫu lập luận bao gồm cả lập luận nhân quả.
- `[[THINK_Exploration_vs_Confirmation]]`: Quá trình khám phá dữ liệu để tìm ra các biến gây nhiễu tiềm năng.
