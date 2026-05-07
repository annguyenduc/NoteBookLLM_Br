---
file_id: "CONCEPT_THINK_Logistic_Regression_Classifier"
title: "CONCEPT: Hồi quy Logistic (Logistic Regression Classifier)"
type: concept
tags: ["Thinking", "Modeling", "Classification", "DA_Core"]
status: "verified"
created: "2026-04-29"
last_updated: "2026-05-01"
---

# Hồi quy Logistic (Logistic Regression Classifier)

## 1. Định nghĩa
Hồi quy Logistic là một mô hình thống kê dùng để dự đoán xác suất của một biến mục tiêu nhị phân (vd: Có/Không, Sống/Chết, Thắng/Thua). Thay vì dự đoán một con số tùy ý, nó đưa ra xác suất nằm trong khoảng từ 0 đến 1.

## 2. Nguyên lý / Cấu trúc
- **Hàm Sigmoid**: Đường cong hình chữ S giúp chuyển đổi kết quả của một phương trình tuyến tính thành giá trị xác suất.
- **Ngưỡng (Threshold)**: Thường là 0.5. Nếu xác suất > 0.5, cá thể được phân loại là 1 (Có), ngược lại là 0 (Không).
- **Log-Odds**: Mô hình tìm cách tối ưu hóa mối quan hệ giữa các biến đầu vào và tỷ lệ logarit của xác suất thành công.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Dự đoán khả năng một người phản hồi lại thư mời mở thẻ tín dụng.
> **Ứng dụng**: Mô hình tính toán dựa trên thu nhập và lịch sử chi tiêu. Kết quả trả về là 0.75 (tức 75% khả năng sẽ phản hồi). Dựa trên con số này, ngân hàng quyết định gửi thư mời.
> **Nguồn**: SOURCE_THINK_DATA_SCIENCE_FOR_BUSINESS — Chương 4.

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Dự đoán khả năng một học sinh nộp bài tập đúng hạn dựa trên số giờ online trên LMS.
> **Ứng dụng**: 
> - **Input**: Số lần đăng nhập hệ thống trong 2 ngày đầu tuần.
> - **Output**: Xác suất nộp bài đúng hạn.
> - **Kết quả**: Nếu mô hình báo xác suất < 0.3, hệ thống tự động gửi tin nhắn nhắc nhở "Đừng quên hạn nộp bài nhé!".

## 4. Trích dẫn nguồn (Rule 14)
- **Nguồn**: SOURCE_THINK_DATA_SCIENCE_FOR_BUSINESS — Trang 90-110.
- **Fact-check**: Đã đối chiếu file raw `THINK_Data_Science_for_Business.md`. [Rule 14: SUCCESS]

---
WRITE REPORT:
  file: "3-resources/wiki/concepts/CONCEPT_THINK_Logistic_Regression_Classifier.md"
  operation: "overwrite"
  added: "Chuẩn hóa theo v4.1, tập trung vào tư duy xác suất."
  removed: "NONE"
  compliance: "[Rule 20] Đã đối soát Template và Raw thành công."


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
