---
file_id: "CONCEPT_THINK_SVM_Linear_Separation"
title: "CONCEPT: Máy vector hỗ trợ (Support Vector Machine - SVM)"
type: concept
tags: ["Thinking", "Data_Mining", "Classification", "DA_Core"]
status: "verified"
created: "2026-04-29"
last_updated: "2026-05-01"
---

# Máy vector hỗ trợ (Support Vector Machine - SVM)

## 1. Định nghĩa
**SVM** là một mô hình phân loại tìm kiếm một "siêu phẳng" (hyperplane) tối ưu để phân tách hai nhóm dữ liệu sao cho khoảng cách (margin) từ siêu phẳng đó đến các điểm gần nhất (support vectors) là lớn nhất.

## 2. Nguyên lý / Cấu trúc
- **Margin (Lề)**: Khoảng trống giữa siêu phẳng và các điểm dữ liệu gần nhất. SVM ưu tiên tối đa hóa lề này để tăng khả năng tổng quát hóa của mô hình.
- **Kernel Trick**: Kỹ thuật biến đổi dữ liệu từ không gian thấp chiều sang không gian cao chiều để có thể phân tách tuyến tính các dữ liệu phức tạp.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Phân loại các tế bào là "Lành tính" hay "Ác tính".
> **Ứng dụng**: SVM tìm kiếm đường biên phân tách rõ ràng nhất giữa hai nhóm tế bào dựa trên các đặc điểm sinh học. Những tế bào nằm sát đường biên nhất chính là các "Support Vectors" quyết định vị trí của siêu phẳng.
> **Nguồn**: SOURCE_THINK_DATA_SCIENCE_FOR_BUSINESS — Chương 4.

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Trò chơi phân loại các tấm thẻ "Động vật" và "Thực vật" trên sân trường.
> **Ứng dụng**: 
> - **Siêu phẳng**: Một sợi dây thừng đặt giữa sân.
> - **Mục tiêu**: Đặt sợi dây sao cho nó cách xa các tấm thẻ của cả hai nhóm nhất có thể (để không bị nhầm lẫn). 
> - **Giải thích**: Những tấm thẻ nằm sát sợi dây thừng nhất chính là bằng chứng quan trọng nhất để định hình ranh giới phân loại.

## 4. Trích dẫn nguồn (Rule 14)
- **Nguồn**: SOURCE_THINK_DATA_SCIENCE_FOR_BUSINESS — Trang 95-115.
- **Fact-check**: Đã đối chiếu file raw `THINK_Data_Science_for_Business.md`. [Rule 14: SUCCESS]

---
WRITE REPORT:
  file: "3-resources/wiki/concepts/CONCEPT_THINK_SVM_Linear_Separation.md"
  operation: "overwrite"
  added: "Chuẩn hóa theo v4.1, giải thích Margin qua ví dụ Sợi dây thừng."
  removed: "NONE"
  compliance: "[Rule 20] Đã đối soát Template và Raw thành công."


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
