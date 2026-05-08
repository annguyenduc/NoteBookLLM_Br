---
file_id: CONCEPT_THINK_Entropy_Information_Gain
title: CONCEPT Độ hỗn loạn và Lợi thông tin (Entropy & Information Gain)
type: concept
status: VERIFIED
tags:
ai-first: true
confidence: 0.8
last_reconciled: 2026-05-08
created: 2026-05-01
last_updated: 2026-05-07
---

# Độ hỗn loạn và Lợi thông tin (Entropy & Information Gain)

## 1. Định nghĩa
- **Entropy**: Phép đo độ hỗn loạn hoặc độ không chắc chắn của thông tin trong một tập dữ liệu. Nếu một tập hợp chứa các phần tử hoàn toàn giống nhau, Entropy = 0. Nếu các phần tử chia đều cho các lớp, Entropy đạt cực đại.
- **Information Gain**: Mức độ giảm của Entropy sau khi tập dữ liệu được chia tách dựa trên một thuộc tính nào đó.

## 2. Ứng dụng trong Decision Trees
Các thuật toán cây quyết định sử dụng Lợi thông tin để quyết định xem nên chọn thuộc tính nào làm "nút gốc" hoặc "nút nhánh". Thuộc tính nào mang lại Lợi thông tin lớn nhất (giúp phân loại rõ ràng nhất) sẽ được ưu tiên.

## 3. Ví dụ đối chiếu (R18: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Quyết định xem một người có khả năng trả nợ hay không.
> **Ứng dụng**: Nếu chúng ta chia khách hàng theo "Thu nhập", chúng ta thấy nhóm thu nhập cao hầu hết đều trả nợ (Entropy thấp). Nếu chia theo "Màu tóc", tỷ lệ trả nợ vẫn hỗn loạn trong từng nhóm (Entropy cao). Do đó, "Thu nhập" mang lại Lợi thông tin cao hơn và được chọn để phân loại.
> **Nguồn**: [[SOURCE_Data_Science_For_Business]].

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Phân loại học sinh cần hỗ trợ đặc biệt.
> **Ứng dụng**: 
> - Nếu chia theo "Giới tính": Tỷ lệ học sinh cần hỗ trợ ở hai nhóm nam/nữ vẫn như nhau (Lợi thông tin thấp).
> - Nếu chia theo "Điểm bài kiểm tra đầu vào": Nhóm điểm thấp có tỷ lệ cần hỗ trợ rất cao, nhóm điểm cao có tỷ lệ rất thấp (Lợi thông tin cao).
> **Kết luận**: Nhà trường nên dùng kết quả kiểm tra đầu vào làm tiêu chí hàng đầu để phân bổ nguồn lực hỗ trợ.

## 4. Trích dẫn nguồn
- **Nguồn**: [[SOURCE_Data_Science_For_Business]].


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
