---
title: "CONCEPT: Kiểm định Giả thuyết (Hypothesis Testing)"
type: concept
tags: ["Thinking", "Statistics", "Logic", "DA_Core"]
status: "verified"
created: "2026-04-29"
last_updated: "2026-05-01"
---

# Kiểm định Giả thuyết (Hypothesis Testing)

## 1. Định nghĩa
Kiểm định giả thuyết là một khung logic dùng để đưa ra kết luận về một quần thể dựa trên dữ liệu mẫu. Nó giúp xác định xem một hiệu ứng quan sát được là có thật (có ý nghĩa thống kê) hay chỉ là do ngẫu nhiên.

## 2. Nguyên lý / Cấu trúc
- **Giả thuyết không (Null Hypothesis - H0)**: Giả định rằng không có sự thay đổi hoặc không có hiệu ứng (vd: Thuốc không có tác dụng).
- **Giả thuyết đối (Alternative Hypothesis - H1)**: Điều bạn muốn chứng minh.
- **Giá trị p (p-value)**: Xác suất quan sát được kết quả này (hoặc cực đoan hơn) nếu H0 là đúng. Nếu p < 0.05, ta bác bỏ H0.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Kiểm tra xem một giao diện website mới có làm tăng tỷ lệ click (CTR) không.
> **Ứng dụng**: 
> - **H0**: Giao diện mới và cũ có CTR như nhau.
> - **Kết quả**: Sau khi chạy thử, p-value = 0.01. Vì p < 0.05, ta bác bỏ H0 và kết luận giao diện mới thực sự có tác động tốt hơn.
> **Nguồn**: [[SOURCE_THINK_Thinking_with_Data]] — Chương 5.

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Học sinh thí nghiệm "Dùng phân bón hữu cơ làm cây cao hơn".
> **Ứng dụng**: 
> - **H0**: Cây dùng phân và không dùng phân cao bằng nhau.
> - **Dữ liệu**: Sau 1 tháng, nhóm dùng phân cao hơn 2cm. Tuy nhiên, khi tính toán p-value = 0.40 (40%). 
> - **Kết luận**: Hiệu ứng "cao hơn 2cm" có thể chỉ là do ngẫu nhiên. Học sinh không đủ bằng chứng để khẳng định phân bón có tác dụng trong thí nghiệm này.

## 4. Trích dẫn nguồn (Rule 14)
- **Nguồn**: [[SOURCE_THINK_Thinking_with_Data]] — Trang 55-65.
- **Fact-check**: Đã đối chiếu file raw `THINK_Thinking_with_Data.md`. [Rule 14: SUCCESS]

---
WRITE REPORT:
  file: "3-resources/wiki/concepts/CONCEPT_THINK_Hypothesis_Testing.md"
  operation: "overwrite"
  added: "Chuẩn hóa theo v4.1, tập trung vào logic bác bỏ Giả thuyết không (H0)."
  removed: "NONE"
  compliance: "[Rule 20] Đã đối soát Template và Raw thành công."


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
