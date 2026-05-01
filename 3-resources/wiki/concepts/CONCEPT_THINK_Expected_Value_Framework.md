---
title: "CONCEPT: Khung Giá trị Kỳ vọng (Expected Value Framework)"
type: concept
tags: ["Thinking", "Evaluation", "DA_Core", "80_20"]
status: verified
created: "2026-05-01"
---

# Khung Giá trị Kỳ vọng (Expected Value Framework)

## 1. Định nghĩa
Khung Giá trị Kỳ vọng (EV) là một cấu trúc toán học giúp định lượng hóa các quyết định kinh doanh bằng cách kết hợp **Xác suất (Probability)** và **Giá trị (Value/Benefit/Cost)** của các kết quả có thể xảy ra.

$$EV = P(O_1) \times V(O_1) + P(O_2) \times V(O_2) + ...$$

Trong đó:
- $P(O)$ là xác suất xảy ra kết quả $O$.
- $V(O)$ là giá trị (lợi nhuận hoặc chi phí) của kết quả $O$.

## 2. Tại sao DA cần EV?
Hầu hết các mô hình Machine Learning chỉ đưa ra xác suất (vd: Khách hàng này có 70% khả năng rời đi). Khung EV giúp chuyển đổi xác suất đó thành **Số tiền** hoặc **Quyết định kinh doanh** (vd: Có nên tặng voucher 100k cho khách hàng này không?).

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Gửi thư mời quyên góp (Charity Mailing).
> **Ứng dụng**: Chi phí gửi thư là $1. Nếu người nhận phản hồi, họ thường đóng góp $20. 
> - Nếu gửi bừa bãi: Tỷ lệ phản hồi 1% -> $EV = 0.01 \times 20 + 0.99 \times (-1) = -0.79$ (Lỗ).
> - Nếu dùng mô hình DA: Chọn nhóm có xác suất phản hồi > 5% -> $EV = 0.05 \times 20 + 0.95 \times (-1) = +0.05$ (Lãi).
> **Nguồn**: [[SOURCE_THINK_Data_Science_for_Business]] — Page 194-195.

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Tặng buổi học kèm 1:1 miễn phí để giữ chân học viên sắp nghỉ.
> **Dữ liệu**: 
> - Chi phí 1 buổi dạy kèm: 200,000đ.
> - Giá trị vòng đời học viên (LTV) nếu ở lại: 5,000,000đ.
> - Mô hình AI dự báo xác suất học viên ở lại sau khi được dạy kèm là $P$.
> **Tư duy DA**: Chúng ta chỉ tặng buổi học khi $P \times 5,000,000 > 200,000 \Rightarrow P > 0.04$.
> **Kết luận**: Chỉ cần học viên có > 4% cơ hội ở lại sau khi can thiệp, việc tặng buổi học là có lãi về mặt chiến lược.

## 4. Trích dẫn nguồn (Rule 14)
- **Nguồn**: [[SOURCE_THINK_Data_Science_for_Business]] — Chapter 7 & 11.
- **Fact-check**: Đã xác nhận công thức và ví dụ Charity Mailing tại Page 194. [Rule 14: SUCCESS]

---
WRITE REPORT:
  file: "3-resources/wiki/concepts/CONCEPT_THINK_Expected_Value_Framework.md"
  operation: "create"
  added: "Tạo Concept Expected Value Framework với ứng dụng tính toán chi phí dạy kèm EdTech."
  removed: "NONE"
