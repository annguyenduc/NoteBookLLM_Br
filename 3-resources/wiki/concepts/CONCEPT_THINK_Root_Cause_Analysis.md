---
file_id: "CONCEPT_THINK_Root_Cause_Analysis"
title: "CONCEPT: Phân tích Nguyên nhân Gốc rễ (Root Cause Analysis - RCA)"
type: concept
tags: ["Thinking", "Problem_Solving", "Analysis", "DA_Core"]
status: "verified"
created: "2026-04-29"
last_updated: "2026-05-01"
---

# Phân tích Nguyên nhân Gốc rễ (Root Cause Analysis - RCA)

## 1. Định nghĩa
RCA là một phương pháp giải quyết vấn đề nhằm xác định các nguyên nhân cốt lõi gây ra lỗi hoặc sự cố, thay vì chỉ phản ứng với các triệu chứng bề ngoài. Việc loại bỏ nguyên nhân gốc rễ giúp ngăn chặn vấn đề tái diễn vĩnh viễn.

## 2. Nguyên lý / Cấu trúc
Các kỹ thuật phổ biến trong RCA:
- **5 Whys**: Hỏi "Tại sao" liên tiếp để đào sâu.
- **Biểu đồ Xương cá (Ishikawa)**: Phân loại nguyên nhân theo các nhóm (Con người, Quy trình, Thiết bị, Môi trường).
- **Phân tích sự thay đổi (Change Analysis)**: So sánh trước và sau khi sự cố xảy ra để tìm điểm khác biệt.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Tỷ lệ sản phẩm lỗi tăng đột biến trong dây chuyền sản xuất.
> **Ứng dụng**: Thay vì chỉ loại bỏ sản phẩm lỗi (xử lý triệu chứng), Analyst dùng RCA phát hiện ra một chi tiết máy bị mòn do nhà cung cấp thay đổi chất liệu thép. Việc thay thế nhà cung cấp mới là giải pháp gốc rễ.
> **Nguồn**: SOURCE_THINK_PROBLEM_SOLVING_101 — Chương 2.

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Học sinh làm dự án "Hệ thống tưới cây tự động" nhưng cây vẫn bị héo.
> **Ứng dụng**: 
> - **Triệu chứng**: Đất khô, cây héo.
> - **RCA (Xương cá)**:
>     - Thiết bị: Cảm biến độ ẩm bị hỏng? -> Không.
>     - Quy trình: Code đặt ngưỡng tưới quá thấp? -> **CÓ**.
>     - Môi trường: Trời nắng gắt làm nước bốc hơi nhanh? -> **CÓ**.
> - **Gốc rễ**: Ngưỡng tưới (threshold) trong code chưa linh hoạt theo nhiệt độ môi trường.

## 4. Trích dẫn nguồn (Rule 14)
- **Nguồn**: SOURCE_THINK_PROBLEM_SOLVING_101 — Trang 45-60.
- **Fact-check**: Đã đối chiếu file raw `THINK_Problem_Solving_101.md`. [Rule 14: SUCCESS]

---
WRITE REPORT:
  file: "3-resources/wiki/concepts/CONCEPT_THINK_Root_Cause_Analysis.md"
  operation: "overwrite"
  added: "Chuẩn hóa theo v4.1, bổ sung Biểu đồ Xương cá vào cấu trúc."
  removed: "NONE"
  compliance: "[Rule 20] Đã đối soát Template và Raw thành công."


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
