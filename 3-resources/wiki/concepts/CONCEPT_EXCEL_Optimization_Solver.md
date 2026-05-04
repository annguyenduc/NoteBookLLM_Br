---
file_id: CONCEPT_EXCEL_Optimization_Solver
title: Tối ưu hóa bài toán kinh doanh với [[ENTITY_EXCEL|Excel]] Solver
category: CONCEPT
domain: Excel
status: verified
---

# Optimization with Excel Solver

Solver là một Add-in cực mạnh dùng để tìm lời giải tối ưu (Cực đại hoặc Cực tiểu) cho một bài toán dựa trên các ràng buộc (Constraints).

## 1. Thành phần của bài toán Solver
1.  **Objective Cell (Mục tiêu):** Ô chứa công thức bạn muốn tối đa hóa (ví dụ: Lợi nhuận) hoặc tối thiểu hóa (ví dụ: Chi phí).
2.  **Changing Variable Cells (Biến thay đổi):** Các ô mà Solver có thể thay đổi giá trị để đạt được mục tiêu.
3.  **Constraints (Ràng buộc):** Các điều kiện bắt buộc (ví dụ: Tổng nguyên liệu không được vượt quá kho, số lượng sản phẩm phải là số nguyên).

## 2. Các thuật toán chính (Engines)
- **Simplex LP:** Dùng cho các bài toán tuyến tính (Linear). Rất nhanh và chính xác.
- **GRG Nonlinear:** Dùng cho các bài toán phi tuyến tính (mượt mà).
- **Evolutionary Solver:** Dùng cho các bài toán phức tạp nhất (không mượt mà, có chứa các hàm IF, VLOOKUP).

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### 3.1. Ví dụ từ sách (Original)
*Tình huống: Tối đa hóa lợi nhuận với bài toán Product Mix (Phối hợp sản phẩm).*
- **Đầu vào:** Một nhà máy sản xuất cần quyết định số lượng sản phẩm A và B. Sản phẩm A mang lại lợi nhuận $50, B mang lại $30. Tuy nhiên nhà máy bị giới hạn về nguồn lực: tối đa 100 giờ nhân công mộc và 80 giờ nhân công sơn.
- **Cách giải quyết:** Thiết lập Solver với **Mục tiêu (Objective)** là tối đa hóa tổng lợi nhuận, **Biến thay đổi (Changing Cells)** là số lượng từng loại sản phẩm, và **Ràng buộc (Constraints)** là tổng giờ sử dụng không vượt quá quỹ thời gian cho phép (Sử dụng thuật toán Simplex LP).

### 3.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Phân bổ ngân sách mua sắm thiết bị STEAM tối ưu cho trường học.*
- **Đầu vào:** Nhà trường có ngân sách 100 triệu VNĐ. Cần mua Robot (5 triệu/bộ) và Kit Arduino (1 triệu/bộ). Ràng buộc sư phạm yêu cầu: Ít nhất 10 bộ Robot để thi đấu, tổng số Kit Arduino phải gấp đôi số Robot để đủ cho các lớp thực hành. Số lượng bộ thiết bị phải là số nguyên.
- **Cách giải quyết:** Giáo viên quản lý thiết bị dùng Solver thiết lập **Mục tiêu** là mua được tổng số lượng bộ thiết bị nhiều nhất, **Biến thay đổi** là số lượng Robot và Arduino, **Ràng buộc** là (1) Tổng tiền <= 100 triệu, (2) Robot >= 10, (3) Arduino = 2 * Robot, (4) Số lượng là số Integer (Int). Solver sẽ tính ra phương án mua sắm hoàn hảo mà không cần tính nhẩm.

---
 Nguồn: [[SOURCE_TOOL_Excel_Data_Analysis]] — Chapter 28
[AUDITOR] Rule 14: Đã xác nhận 3 thành phần chính và 3 engines của Solver. Ví dụ đại diện cho các bài toán kinh điển của Linear Programming.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
