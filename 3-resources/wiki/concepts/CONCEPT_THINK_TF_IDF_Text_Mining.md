---
title: "CONCEPT: Trọng số TF-IDF trong Khai thác Văn bản"
type: concept
tags: ["Thinking", "Text_Mining", "NLP", "DA_Core"]
status: "verified"
created: "2026-04-29"
last_updated: "2026-05-01"
---

# Trọng số TF-IDF trong Khai thác Văn bản

## 1. Định nghĩa
**TF-IDF** (Term Frequency - Inverse Document Frequency) là một kỹ thuật thống kê dùng để đánh giá mức độ quan trọng của một từ đối với một văn bản trong một tập hợp các văn bản (corpus). Nó giúp lọc bỏ các từ phổ biến nhưng ít ý nghĩa (như "the", "a", "và") và làm nổi bật các từ mang tính đặc trưng.

## 2. Nguyên lý / Cấu trúc
- **TF (Term Frequency)**: Tần suất xuất hiện của từ trong văn bản hiện tại. Từ xuất hiện càng nhiều, TF càng cao.
- **IDF (Inverse Document Frequency)**: Nghịch đảo tần suất văn bản chứa từ đó. Nếu từ xuất hiện ở quá nhiều văn bản khác nhau, IDF sẽ thấp (vì nó không đặc trưng).
- **TF-IDF = TF x IDF**: Trọng số cao nhất dành cho các từ xuất hiện nhiều trong văn bản này nhưng ít xuất hiện ở các văn bản khác.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Phân loại các bài báo theo chủ đề.
> **Ứng dụng**: Từ "Dữ liệu" có thể xuất hiện nhiều trong một bài báo về công nghệ, nhưng vì nó cũng xuất hiện trong hầu hết các bài báo khác cùng tập dữ liệu, nên trọng số TF-IDF của nó sẽ bị hạ thấp. Ngược lại, từ "Hadoop" chỉ xuất hiện trong vài bài, nên nó sẽ có trọng số cao và trở thành từ khóa đặc trưng để phân loại.
> **Nguồn**: [[SOURCE_THINK_Data_Science_for_Business]] — Chương 10.

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Tóm tắt các chủ đề thảo luận chính trong diễn đàn lớp học.
> **Ứng dụng**: 
> - Nếu giáo viên muốn biết học sinh đang quan tâm đến vấn đề gì nhất.
> - Các từ như "Học sinh", "Bài tập", "Thầy" sẽ có TF cao nhưng IDF thấp (vì bài nào cũng có).
> - Từ "Mạch điện", "Arduino" có TF cao trong một số bài cụ thể, giúp giáo viên nhận diện nhanh đây là nhóm thảo luận về chủ đề Kỹ thuật/Robot.

## 4. Trích dẫn nguồn (Rule 14)
- **Nguồn**: [[SOURCE_THINK_Data_Science_for_Business]] — Trang 250-265.
- **Fact-check**: Đã đối chiếu file raw `THINK_Data_Science_for_Business.md`. [Rule 14: SUCCESS]

---
WRITE REPORT:
  file: "3-resources/wiki/concepts/CONCEPT_THINK_TF_IDF_Text_Mining.md"
  operation: "overwrite"
  added: "Chuẩn hóa theo v4.1, giải thích cơ chế lọc từ phổ biến của TF-IDF."
  removed: "NONE"
  compliance: "[Rule 20] Đã đối soát Template và Raw thành công."
