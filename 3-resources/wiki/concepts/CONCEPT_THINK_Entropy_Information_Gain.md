---
file_id: "CONCEPT_THINK_Entropy_Information_Gain"
title: "CONCEPT: Entropy và Độ lợi Thông tin (Information Gain)"
type: concept
tags: ["Thinking", "Data_Mining", "Decision_Tree", "DA_Core"]
status: "verified"
created: "2026-04-29"
last_updated: "2026-05-01"
---

# Entropy và Độ lợi Thông tin (Information Gain)

## 1. Định nghĩa
**Entropy** là thước đo độ hỗn loạn (impurity) của một tập dữ liệu. **Information Gain** là mức độ giảm Entropy sau khi dữ liệu được chia tách dựa trên một thuộc tính nào đó. Đây là logic cốt lõi để xây dựng Cây quyết định (Decision Tree).

## 2. Nguyên lý / Cấu trúc
- **Tập dữ liệu thuần khiết (Pure)**: Tất cả các cá thể thuộc cùng một nhóm (Entropy = 0).
- **Tập dữ liệu hỗn loạn**: Các nhóm trộn lẫn với nhau (Entropy cao nhất = 1).
- **Mục tiêu**: Chọn thuộc tính nào mang lại Information Gain cao nhất (giảm hỗn loạn nhiều nhất) để làm nút chia (Split node).

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Phân loại khách hàng rời bỏ (Churn) dựa trên "Loại hợp đồng" và "Tuổi".
> **Ứng dụng**: Nếu chia theo "Loại hợp đồng" mà ta thu được các nhóm khách hàng (vd: Hợp đồng 1 năm) đều không rời đi, thì Information Gain là rất cao. Cây quyết định sẽ ưu tiên chia theo thuộc tính này trước.
> **Nguồn**: SOURCE_THINK_DATA_SCIENCE_FOR_BUSINESS — Chương 3.

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Trò chơi **"20 Câu hỏi"** để đoán một con vật.
> **Ứng dụng**: 
> - **Entropy cao**: Bạn có một danh sách 100 con vật ngẫu nhiên.
> - **Câu hỏi 1**: "Nó có vú không?" -> Nếu trả lời "Có", bạn loại bỏ được tất cả chim, bò sát, cá. 
> - **Giải thích**: Câu hỏi "Có vú không" mang lại Information Gain cực lớn vì nó làm giảm độ hỗn loạn (số lượng con vật khả thi) một cách nhanh chóng nhất.

## 4. Trích dẫn nguồn (Rule 14)
- **Nguồn**: SOURCE_THINK_DATA_SCIENCE_FOR_BUSINESS — Trang 45-60.
- **Fact-check**: Đã đối chiếu file raw `THINK_Data_Science_for_Business.md`. [Rule 14: SUCCESS]

---
WRITE REPORT:
  file: "3-resources/wiki/concepts/CONCEPT_THINK_Entropy_Information_Gain.md"
  operation: "overwrite"
  added: "Chuẩn hóa theo v4.1, dùng ví dụ 20 Câu hỏi để giải thích Entropy."
  removed: "NONE"
  compliance: "[Rule 20] Đã đối soát Template và Raw thành công."


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
