---
file_id: "CONCEPT_THINK_Similarity_Distance_Metrics"
title: "CONCEPT: Độ tương đồng và Khoảng cách (Similarity & Distance)"
type: concept
tags: ["Thinking", "Data_Mining", "Math", "DA_Core"]
status: "verified"
created: "2026-04-29"
last_updated: "2026-05-01"
---

# Độ tương đồng và Khoảng cách (Similarity & Distance)

## 1. Định nghĩa
Trong khai thác dữ liệu, "Độ tương đồng" là cách chúng ta định lượng việc hai cá thể giống nhau đến mức nào. "Khoảng cách" là nghịch đảo của độ tương đồng: khoảng cách càng nhỏ, hai cá thể càng giống nhau.

## 2. Các độ đo phổ biến
- **Euclidean Distance**: Khoảng cách "đường chim bay" giữa hai điểm trong không gian.
- **Manhattan Distance**: Khoảng cách đi theo các khối (như đi trong thành phố).
- **Cosine Similarity**: Đo góc giữa hai vector (phổ biến trong Text mining để so sánh nội dung văn bản).

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Hệ thống gợi ý bài hát (vd: Spotify).
> **Ứng dụng**: Nếu bài hát A và bài hát B có cùng thể loại (Pop), cùng nhịp độ (BPM), và cùng nghệ sĩ, khoảng cách giữa chúng trong không gian đặc trưng (Feature space) sẽ rất nhỏ. Hệ thống sẽ gợi ý bài B cho người vừa nghe bài A.
> **Nguồn**: SOURCE_THINK_DATA_SCIENCE_FOR_BUSINESS — Chương 6.

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Giáo viên tìm kiếm các tài liệu học tập tương đồng để gợi ý cho học sinh.
> **Ứng dụng**: 
> - Nếu học sinh đang đọc một bài báo về "Robot cứu hộ", hệ thống dùng **Cosine Similarity** để tìm các bài báo khác có tập hợp từ khóa (keywords) tương tự như "Cảm biến", "Động cơ servo", "Tự hành" để giới thiệu thêm.

## 4. Trích dẫn nguồn (Rule 14)
- **Nguồn**: SOURCE_THINK_DATA_SCIENCE_FOR_BUSINESS — Trang 141-155.
- **Fact-check**: Đã đối chiếu file raw `THINK_Data_Science_for_Business.md`. [Rule 14: SUCCESS]

---
WRITE REPORT:
  file: "3-resources/wiki/concepts/CONCEPT_THINK_Similarity_Distance_Metrics.md"
  operation: "overwrite"
  added: "Chuẩn hóa theo v4.1, đồng bộ các độ đo khoảng cách cơ bản."
  removed: "NONE"
  compliance: "[Rule 20] Đã đối soát Template và Raw thành công."


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
