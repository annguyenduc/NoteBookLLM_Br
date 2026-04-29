---
id: THINK_Exploration_vs_Confirmation
type: concept
aliases: ["Exploration vs Confirmation", "Khám phá vs Xác nhận", "Scaffolding"]
tags: ["data-thinking", "exploration", "planning", "scaffolding"]
---

# Khám phá và Xác nhận (Exploration vs Confirmation)

<!-- [AUDITOR] Rule 14: Nguồn được lấy trực tiếp từ 3-resources/raw/THINK_Thinking_with_Data.md, tại Chương 2 (What Next?), trang 17-26, line 818-1194. -->

## 1. Khái niệm cốt lõi
Khi làm việc với dữ liệu, luôn tồn tại một sự giằng co tự nhiên (natural tension) giữa hai thái cực:
1. **Khám phá (Exploration):** Sự thôi thúc lao ngay vào phân tích dữ liệu, bị cuốn theo "bài ca nàng tiên cá" (siren song) của những con số và phát hiện mới lạ.
2. **Xác nhận / Lập kế hoạch (Confirmation/Planning):** Việc dành thời gian cẩn thận ngay từ đầu để suy nghĩ, phác thảo vấn đề và đặt ra mục tiêu.

Theo tác giả, sự cân bằng giữa hai thái cực này là bắt buộc. Để không bị chìm sâu vào các "hố thỏ" (rabbit holes) phân tích vô ích, người phân tích cần triển khai **Scaffolding (Giàn giáo lập kế hoạch)**. Scaffolding là nghệ thuật ưu tiên các mục tiêu nhỏ gọn, sử dụng các công cụ đơn giản (tabulations, biểu đồ phân tán cơ bản) để nhanh chóng xây dựng trực giác (intuition) trước khi áp dụng các mô hình phức tạp. 

Quá trình "Refining the Vision" (Làm mịn tầm nhìn) sử dụng kỹ thuật *Kitchen sink interrogation* (Hỏi tất cả các câu hỏi có thể nghĩ ra) và *Working backward* (Tư duy ngược từ kết quả đầu ra).

📖 Nguồn: `[[SOURCE_THINK_Thinking_with_Data]]` — Chương 2: What Next? (Trang 17-26).

## 2. Ứng dụng & Ví dụ (Double Examples)

**Ví dụ Gốc (Original):**
Công ty bất động sản muốn biết mối quan hệ giữa giá thuê nhà và khả năng tiếp cận phương tiện giao thông công cộng.
- Thay vì lao vào xây dựng một mô hình học máy phức tạp kết hợp hàng chục nguồn dữ liệu (điều sẽ ngốn hàng tuần làm việc), phân tích viên xây dựng "Scaffolding" bằng cách trước tiên chỉ vẽ một bản đồ scatterplot hiển thị giá nhà xung quanh các ga tàu điện ngầm.
- Việc "Khám phá" nhanh này giúp "Xác nhận" xem trực giác có đúng không, trước khi đổ thêm nguồn lực vào các mô hình sâu hơn.
📖 Nguồn: `[[SOURCE_THINK_Thinking_with_Data]]` — Chương 2: What Next? (Trang 25-26).

**Ví dụ Sư phạm (Pedagogical) [Phóng tác]:**
Trong quá trình hướng dẫn học sinh làm dự án Khoa học (Science Fair):
Học sinh thường mang máy đo nhiệt độ đi khắp trường để lấy hàng ngàn điểm dữ liệu mà không có định hướng (Quá thiên về Exploration). Giáo viên hướng dẫn các em xây dựng Scaffolding:
1. (Planning) Lập giả thuyết "Phòng học ở hướng Tây sẽ nóng hơn". 
2. (Exploration nhanh) Đo thử 2 phòng đại diện trong 1 ngày.
3. (Confirmation) Nếu dữ liệu ban đầu cho thấy xu hướng rõ ràng, mới tiến hành đo quy mô lớn. Điều này giúp học sinh tránh lãng phí thời gian thu thập dữ liệu rác.

## 3. Liên kết liên quan
- `[[CONCEPT_THINK_Data_Story_Structure]]`: Tư duy ngược (Working backward) từ Outcome là chìa khóa để điều hướng việc khám phá.
- `[[CONCEPT_THINK_Correlation_vs_Causation]]`: Sự khác biệt giữa việc tình cờ khám phá ra sự tương quan so với việc lập kế hoạch để kiểm định quan hệ nhân quả.
