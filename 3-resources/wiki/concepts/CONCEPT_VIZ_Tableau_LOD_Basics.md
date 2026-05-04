---
file_id: CONCEPT_VIZ_TABLEAU_LOD_BASICS
title: "Tableau LOD Basics (Cơ bản về Level of Detail trong Tableau)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-04-29"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_VIZ_Analyzing_Data_Power_BI]]"
---

## ## For future Claude
Trang này định nghĩa khái niệm Level of Detail (LOD) - một trong những tính năng mạnh mẽ nhất của Tableau để kiểm soát mức độ tổng hợp dữ liệu độc lập với các chiều (dimensions) đang hiển thị trên biểu đồ. LOD cho phép giải quyết các bài toán so sánh phức tạp mà các hàm tính toán thông thường không thực hiện được.

## ## Key Claims / Summary
1.  **FIXED**: Cố định mức độ tổng hợp tại một chiều cụ thể, bất chấp các bộ lọc trên View.
2.  **INCLUDE**: Thêm chiều vào mức độ tổng hợp mà không cần kéo chiều đó vào biểu đồ.
3.  **EXCLUDE**: Loại bỏ chiều khỏi mức độ tổng hợp để tính toán ở mức độ cao hơn.

## ## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Sử dụng `{ FIXED [Province] : SUM([Sales]) }` để tính tổng doanh thu theo từng Tỉnh. Dù người dùng có đang lọc xem chi tiết theo Quận hay Huyện, con số tổng của Tỉnh vẫn được giữ nguyên để so sánh tỷ trọng.
- **Ẩn dụ sư phạm (Pedagogical)**: LOD giống như việc bạn đeo một chiếc "kính viễn vọng" đặc biệt. Bình thường bạn chỉ thấy được những gì ngay trước mắt (mức độ chi tiết của biểu đồ), nhưng khi đeo kính LOD, bạn có thể nhìn thấy bức tranh tổng thể của cả một khu vực lớn từ xa, ngay cả khi bạn đang đứng ở một góc phố nhỏ hẹp.

## ## Source Tracing
- **Nguồn**: [[SOURCE_VIZ_Analyzing_Data_Power_BI]] — Section: Advanced Visualization Techniques.

## ## History / Revisions
- **2026-05-03**: [@engineer] Pressure Chain Healing. Bổ sung Rule 17, 20 và chuẩn hóa metadata.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
