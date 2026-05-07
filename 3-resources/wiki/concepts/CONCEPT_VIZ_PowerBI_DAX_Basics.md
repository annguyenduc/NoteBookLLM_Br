---
file_id: CONCEPT_VIZ_POWERBI_DAX_BASICS
title: "Power BI DAX Basics (Cơ bản về ngôn ngữ DAX)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-04-29"
last_updated: "2026-05-03"
sources:
  - "SOURCE_VIZ_ANALYZING_DATA_POWER_BI"
---

## ## For future Claude
Trang này định nghĩa ngôn ngữ DAX (Data Analysis Expressions) - linh hồn của Power BI. DAX cho phép chúng ta thực hiện các tính toán động và phức tạp trên mô hình dữ liệu, vượt xa các tính toán bảng đơn giản của Excel, giúp tạo ra các chỉ số kinh doanh thông minh và linh hoạt.

## ## Key Claims / Summary
1.  **Row Context vs Filter Context**: Hiểu về ngữ cảnh hàng và ngữ cảnh lọc là chìa khóa để viết DAX đúng.
2.  **Measures vs Calculated Columns**: Ưu tiên sử dụng Measures để tối ưu hóa bộ nhớ và hiệu suất tính toán.
3.  **CALCULATE function**: Hàm quyền lực nhất trong DAX, cho phép thay đổi ngữ cảnh lọc một cách chủ động.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Sử dụng hàm `CALCULATE(SUM(Sales), FILTER(Region = "Hà Nội"))` để tính toán doanh thu chỉ của riêng khu vực Hà Nội, bất kể người dùng đang chọn lọc gì khác trên báo cáo.
- **Ẩn dụ sư phạm (Pedagogical)**: [Phóng tác] DAX giống như các công thức "phép thuật" trên một chiếc máy tính bỏ túi vạn năng. Thay vì cộng trừ tay từng con số, bạn thiết lập một quy tắc thông minh để máy tự động tính toán lại kết quả chính xác mỗi khi bạn thay đổi các điều kiện quan sát (lọc dữ liệu).

## ## Source Tracing
- **Nguồn**: SOURCE_VIZ_ANALYZING_DATA_POWER_BI — Chapter 5: Advanced DAX.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 17, 20 và chuẩn hóa metadata.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
