---
title: "CONCEPT: Quy trình Khai thác Dữ liệu (CRISP-DM)"
type: concept
tags: ["Thinking", "Process", "Standard", "DA_Core"]
status: "verified"
created: "2026-04-29"
last_updated: "2026-05-01"
---

# Quy trình Khai thác Dữ liệu (CRISP-DM)

## 1. Định nghĩa
**CRISP-DM** (Cross-Industry Standard Process for Data Mining) là quy trình tiêu chuẩn hóa cho các dự án khai thác dữ liệu, giúp đảm bảo tính hệ thống từ khi hiểu bài toán kinh doanh đến khi triển khai mô hình.

## 2. Nguyên lý / Cấu trúc (6 Giai đoạn)
1.  **Business Understanding**: Hiểu mục tiêu và yêu cầu kinh doanh.
2.  **Data Understanding**: Thu thập và làm quen với dữ liệu thô.
3.  **Data Preparation**: Làm sạch và biến đổi dữ liệu (80% thời gian).
4.  **Modeling**: Áp dụng các thuật toán khai thác dữ liệu.
5.  **Evaluation**: Đánh giá kết quả dựa trên mục tiêu kinh doanh.
6.  **Deployment**: Triển khai kết quả vào thực tế.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Dự án giảm tỷ lệ khách hàng rời bỏ (Customer Churn).
> **Ứng dụng**: Bắt đầu bằng việc định nghĩa "Churn" (Business Understanding), sau đó thu thập lịch sử cuộc gọi (Data Understanding), làm sạch dữ liệu (Preparation), chạy mô hình dự báo (Modeling), kiểm tra xem mô hình có giúp tiết kiệm tiền không (Evaluation) và tích hợp vào hệ thống CSKH (Deployment).
> **Nguồn**: [[SOURCE_THINK_Data_Science_for_Business]] — Chương 2.

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Học sinh thực hiện dự án "Tối ưu hóa thực đơn căng tin trường học".
> **Ứng dụng**: 
> 1. **Business**: Mục tiêu là giảm lượng thức ăn thừa.
> 2. **Data**: Thống kê số lượng từng món được mua và lượng rác thải mỗi ngày.
> 3. **Preparation**: Loại bỏ các ngày nghỉ lễ khỏi dữ liệu.
> 4. **Modeling**: Tìm mối tương quan giữa thời tiết và món ăn được yêu thích.
> 5. **Evaluation**: Thử nghiệm thực đơn mới trong 1 tuần và đo lại rác thải.
> 6. **Deployment**: Đề xuất thực đơn cố định hàng tháng cho nhà trường.

## 4. Trích dẫn nguồn (Rule 14)
- **Nguồn**: [[SOURCE_THINK_Data_Science_for_Business]] — Trang 27-34.
- **Fact-check**: Đã đối chiếu file raw `THINK_Data_Science_for_Business.md`. [Rule 14: SUCCESS]

---
WRITE REPORT:
  file: "3-resources/wiki/concepts/CONCEPT_THINK_Data_Mining_Process_CRISP.md"
  operation: "overwrite"
  added: "Chuẩn hóa theo v4.1, đồng bộ cấu trúc 6 giai đoạn."
  removed: "NONE"
  compliance: "[Rule 20] Đã đối soát Template và Raw thành công."


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
