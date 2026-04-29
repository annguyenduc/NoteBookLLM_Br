---
id: THINK_Patterns_of_Reasoning
type: concept
aliases: ["Patterns of Reasoning", "Mô hình lập luận"]
tags: ["data-thinking", "logic", "argumentation"]
---

# Các Mô hình Lập luận (Patterns of Reasoning)

<!-- [AUDITOR] Rule 14: Nguồn được lấy trực tiếp từ 3-resources/raw/THINK_Thinking_with_Data.md, tại Chương 3 (Arguments) và Chương 4 (Patterns of Reasoning). -->

## 1. Khái niệm cốt lõi
Trong phân tích dữ liệu, việc đưa ra kết luận đòi hỏi những mô hình lập luận vững chắc để dẫn dắt khán giả từ các niềm tin sẵn có (Prior Beliefs) đến những niềm tin mới (New Beliefs). Một phân tích thiếu đi cấu trúc lập luận rõ ràng sẽ chỉ là một tập hợp các con số vô nghĩa.

## 2. Bốn hình thức lập luận cơ bản (Chapter 3)
Theo tư duy dữ liệu, có 4 hình thức lập luận chính để thuyết phục khán giả:
- **Lập luận về Thực tế (Fact)**: "Điều này có đang xảy ra không?" (Dữ liệu cho thấy doanh thu đang giảm).
- **Lập luận về Định nghĩa (Definition)**: "Hiện tượng này được gọi là gì?" (Việc người dùng rời đi sau 3 ngày được định nghĩa là "Early Churn").
- **Lập luận về Giá trị (Value)**: "Điều này là tốt hay xấu?" (Mức độ Early Churn này là nguy hiểm cho sản phẩm).
- **Lập luận về Chính sách (Policy)**: "Chúng ta nên làm gì?" (Chúng ta cần thiết kế lại luồng Onboarding).

## 3. Các mô hình suy luận đặc thù với dữ liệu (Chapter 4)
Khi làm việc với dữ liệu cụ thể, có các mô hình suy luận (Patterns of Reasoning) thường được dùng:
- **Tối ưu hóa (Optimization)**: Chứng minh rằng một giải pháp nào đó là tốt nhất trong số các lựa chọn có thể (dựa trên một hàm mục tiêu).
- **Phân tích chi phí - lợi ích (Cost/Benefit Analysis)**: So sánh định lượng giữa cái được và cái mất để hỗ trợ quyết định.
- **Trường hợp biên (Bounding Cases)**: Đánh giá kịch bản xấu nhất (Worst-case) và tốt nhất (Best-case) để thiết lập giới hạn kỳ vọng.

## 4. 💡 Ví dụ đối chiếu (Double Examples)
### 4.1. Ví dụ gốc (Original)
Khi một Data Scientist trình bày về việc tối ưu hóa chi phí quảng cáo (Optimization), họ phải lập luận từ **Fact** (Chi phí đang cao) -> **Value** (Hiệu suất hiện tại là chưa đủ tốt) -> **Policy** (Nên dịch chuyển ngân sách sang kênh khác), sử dụng dữ liệu làm bằng chứng (Evidence) cho từng bước.

### 4.2. Ví dụ sư phạm (Pedagogical Application) [Phóng tác]
**Tình huống**: Thuyết phục Ban giám hiệu đầu tư mua thêm kit Arduino cho phòng Lab.
- **Fact**: Hiện tại mỗi nhóm 5 em học sinh mới có 1 kit.
- **Value**: Việc này (Value) làm giảm thời gian thực hành thực tế, khiến các em thiếu kỹ năng lập trình phần cứng.
- **Policy**: Đề xuất mua thêm 10 kit để giảm tỷ lệ xuống còn 2 em/kit. (Dùng **Cost/Benefit Analysis** để chỉ ra chi phí mua kit nhỏ hơn nhiều so với giá trị kỹ năng mang lại).

## 5. Liên kết tư duy
- [[CONCEPT_THINK_Audience_Framing]]
- [[CONCEPT_THINK_Data_Story_Structure]]
- [[SOURCE_THINK_Thinking_with_Data]]
