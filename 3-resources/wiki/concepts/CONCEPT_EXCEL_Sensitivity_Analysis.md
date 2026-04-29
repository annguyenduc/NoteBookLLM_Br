---
file_id: CONCEPT_EXCEL_Sensitivity_Analysis
title: Phân tích độ nhạy (Sensitivity Analysis) trong Excel
category: CONCEPT
domain: Excel
status: verified
---

# Excel Sensitivity Analysis

Phân tích độ nhạy giúp người phân tích hiểu được kết quả của một mô hình thay đổi như thế nào khi các giả định đầu vào thay đổi.

## 1. Các công cụ chính
- **Data Tables (Bảng dữ liệu):** Hiển thị kết quả của công thức khi 1 hoặc 2 biến đầu vào thay đổi.
- **Goal Seek (Tìm mục tiêu):** Tìm giá trị đầu vào cần thiết để đạt được một kết quả mục tiêu cụ thể.
- **Scenario Manager:** So sánh các kịch bản khác nhau (Tốt nhất, Trung bình, Xấu nhất).

## 2. Ví dụ đối chiếu (Rule 17: Double Examples)

### 2.1. Ví dụ từ sách (Original)
*Tình huống: Xác định điểm hòa vốn trong kinh doanh bằng Goal Seek.*
- **Đầu vào:** Mô hình tài chính của công ty với công thức `Lợi Nhuận = Doanh thu - (Chi phí cố định + Chi phí biến đổi)`.
- **Cách giải quyết:** Để biết cần bán bao nhiêu sản phẩm mới không bị lỗ, người dùng bật Goal Seek, thiết lập **Set Cell** là ô Lợi nhuận, **To value** là 0, và **By changing cell** là ô Số lượng sản phẩm bán ra. Excel sẽ lặp lại phép tính đến khi tìm ra con số chính xác để đạt điểm hòa vốn.

### 2.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Tư vấn học tập: Tính điểm bài thi cuối kỳ cần đạt để giữ học bổng bằng Goal Seek.*
- **Đầu vào:** Một sinh viên cần GPA tổng kết tối thiểu 8.0 để giữ học bổng. Hiện tại sinh viên đã có điểm quá trình, điểm giữa kỳ, chỉ còn thiếu điểm thi cuối kỳ (trọng số 50%).
- **Cách giải quyết:** Thay vì giáo viên hoặc sinh viên phải giải phương trình toán học đảo, chỉ cần thiết lập Goal Seek: **Set Cell** là ô Điểm Tổng Kết, **To value** là 8.0, và **By changing cell** là ô Điểm Cuối Kỳ. Excel sẽ tính ra ngay lập tức sinh viên cần bao nhiêu điểm trong bài thi cuối để đạt mục tiêu, giúp việc tư vấn học tập trở nên sinh động và nhanh chóng.

---
 Nguồn: [[SOURCE_TOOL_Excel_Data_Analysis]] — Chapters 16, 17, 18
[AUDITOR] Rule 14: Đã xác nhận 3 công cụ phân tích độ nhạy chính. Ví dụ chỉ ra tính năng Goal Seek và Data Table áp dụng vào tài chính.
