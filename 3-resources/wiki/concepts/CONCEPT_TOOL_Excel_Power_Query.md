---
file_id: CONCEPT_TOOL_Excel_Power_Query
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
tags: ["Power_Query", "ETL", "Excel"]
source: "[[SOURCE_TOOL_Excel_PowerQuery]]"
created: "2026-05-03"
---

# Concept: Power Query (Get & Transform)

## 1. Core Principle (Bản chất cốt lõi)
Power Query là động cơ kết nối và biến đổi dữ liệu (ETL - Extract, Transform, Load) tích hợp trong Excel. Nó cho phép người dùng tự động hóa các thao tác làm sạch dữ liệu lặp đi lặp lại mà không cần viết code VBA. Mọi thao tác được ghi lại thành các "bước" (steps) có thể tái sử dụng.

## 2. Ví dụ đối chiếu (Rule 17 - Double Examples)

### Ví dụ 1: Trích dẫn tài liệu (Original Context)
> "Power Query records each step you take in the editor... Once defined, these steps form a repeatable process."
- **Thao tác**: Chọn "Remove Columns", "Filter Rows", "Change Type".
- **Kết quả**: Một Query được lưu lại, chỉ cần nhấn "Refresh" để áp dụng cho dữ liệu mới.
**Nguồn**: `WEBSITE_TOOL_Excel_PowerQuery` — Section "Key Capabilities"

### Ví dụ 2: Ẩn dụ sư phạm (Pedagogical Application)
Hãy tưởng tượng Power Query giống như một **"Dây chuyền sản xuất nước ép tự động"**:
1. **Connect (Input)**: Bạn đưa trái cây thô vào (Dữ liệu gốc).
2. **Transform (Process)**: Máy tự động Rửa (Remove nulls), Gọt vỏ (Split columns), Ép lấy nước (Aggregate).
3. **Load (Output)**: Nước ép sạch chảy vào chai (Bảng Excel đã làm sạch).
Lần sau, bạn chỉ cần đổ thêm trái cây vào và nhấn nút, máy sẽ làm y hệt các bước đó.

## 3. 4F Reflection
- **Facts**: Power Query sử dụng ngôn ngữ công thức **M** đằng sau giao diện kéo thả.
- **Feelings**: Cảm giác "giải phóng" khi không còn phải Copy-Paste thủ công hàng ngày.
- **Findings**: Power Query mạnh hơn rất nhiều so với các hàm Excel thông thường khi xử lý dữ liệu lớn.
- **Futures**: Cần dạy học sinh cách tư duy theo "Luồng dữ liệu" (Data Flow) thay vì tư duy theo "Ô" (Cell).

---
Nguồn: [[SOURCE_TOOL_Excel_PowerQuery]]
[[CONCEPT_TOOL_Excel_Pivot_Tables]]


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
