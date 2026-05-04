---
file_id: CONCEPT_DSML_FEATURE_ENGINEERING_BASICS
title: "Feature Engineering Basics (Kỹ nghệ đặc trưng cơ bản)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-04-29"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_DSML_Data_Analytics_Concepts]]"
---

## ## For future Claude
Trang này tổng hợp các kỹ thuật Kỹ nghệ đặc trưng (Feature Engineering) cơ bản. Trong khoa học dữ liệu, việc biến đổi dữ liệu thô thành các đặc trưng có ý nghĩa thường quan trọng hơn bản thân thuật toán, quyết định trực tiếp đến độ chính xác và khả năng học của mô hình trên dữ liệu bảng (Tabular data).

## ## Key Claims / Summary
1.  **Data Quality over Algorithm**: Dữ liệu được xử lý tốt sẽ mang lại hiệu quả cao hơn là sử dụng một thuật toán cực kỳ phức tạp trên dữ liệu thô.
2.  **Encoding & Scaling**: Các kỹ thuật thiết yếu để chuyển đổi dữ liệu phi số và chuẩn hóa đơn vị đo lường.
3.  **Feature Creation**: Khả năng tạo ra các biến mới từ các biến hiện có dựa trên hiểu biết về lĩnh vực (Domain Knowledge).

## 1. Định nghĩa
Kỹ nghệ đặc trưng là quá trình biến đổi dữ liệu thô thành các đặc trưng giúp mô hình học hiệu quả hơn. "Dữ liệu tốt đánh bại thuật toán tốt."

## 2. Các kỹ thuật chính (Core Techniques)
1. **One-Hot Encoding:** Biến đổi dữ liệu chữ (Categorical) thành các cột số 0 và 1.
2. **Scaling/Normalization:** Đưa các số có đơn vị khác nhau về cùng một khoảng để thuật toán không bị thiên lệch.
3. **Feature Creation:** Tạo biến mới từ biến cũ (ví dụ: từ "Ngày sinh" tạo ra biến "Tuổi").
4. **Handling Missing Values:** Điền giá trị thiếu bằng Mean/Median hoặc xóa bỏ.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Nếu để "Lương" (hàng triệu) và "Số con" (đơn vị) vào cùng một mô hình mà không Scaling, mô hình sẽ coi "Lương" quan trọng gấp triệu lần "Số con". (Nguồn: [[SOURCE_DSML_Data_Analytics_Concepts]] Page 70-80).
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như việc bạn đi thi chạy. Nếu một người tính thời gian bằng "Giây" và người kia tính bằng "Phút", bạn không thể so sánh họ trực tiếp. Bạn cần đổi tất cả về cùng một đơn vị (Scaling) để biết ai nhanh hơn.

## ## Source Tracing
- **Nguồn**: [[SOURCE_DSML_Data_Analytics_Concepts]] — Page 70-85.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 17, 20 và chuẩn hóa metadata.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
