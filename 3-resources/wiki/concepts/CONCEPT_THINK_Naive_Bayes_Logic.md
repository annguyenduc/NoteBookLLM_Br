---
title: "CONCEPT: Tư duy Naive Bayes (Naive Bayes Logic)"
type: concept
tags: ["Thinking", "Probability", "Classification", "DA_Core"]
status: "verified"
created: "2026-04-29"
last_updated: "2026-05-01"
---

# Tư duy Naive Bayes (Naive Bayes Logic)

## 1. Định nghĩa
Naive Bayes là một thuật toán phân loại dựa trên Định lý Bayes với giả định "ngây ngô" (naive) rằng: tất cả các đặc điểm (features) đều độc lập với nhau. Dù giả định này thường sai trong thực tế, thuật toán vẫn hoạt động cực kỳ hiệu quả trong việc phân loại văn bản.

## 2. Nguyên lý / Cấu trúc
- **Xác suất hậu nghiệm (Posterior)**: Xác suất một sự kiện xảy ra khi đã biết bằng chứng (evidence).
- **Tính độc lập**: Coi mỗi từ trong một email là một bằng chứng độc lập cho việc email đó là "Spam" hay "Không Spam".
- **Ưu điểm**: Cực nhanh, cần ít dữ liệu huấn luyện, hoạt động tốt với dữ liệu dạng văn bản (Text mining).

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Bộ lọc thư rác (Spam Filter).
> **Ứng dụng**: Nếu email chứa các từ "Viagra", "Free", "Money", Naive Bayes sẽ tính xác suất email đó là Spam dựa trên tần suất các từ này xuất hiện trong tập dữ liệu thư rác đã biết trước đó.
> **Nguồn**: [[SOURCE_THINK_Data_Science_for_Business]] — Chương 9.

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Phân loại cảm xúc (Sentiment Analysis) từ phản hồi của học sinh về buổi học.
> **Ứng dụng**: 
> - **Input**: "Bài giảng hôm nay rất vui và dễ hiểu".
> - **Naive Bayes**: Coi "vui" và "dễ hiểu" là hai bằng chứng độc lập của cảm xúc "Tích cực". 
> - **Kết quả**: Hệ thống tự động dán nhãn "Tích cực" cho phản hồi này để giáo viên tổng hợp nhanh.

## 4. Trích dẫn nguồn (Rule 14)
- **Nguồn**: [[SOURCE_THINK_Data_Science_for_Business]] — Trang 235-245.
- **Fact-check**: Đã đối chiếu file raw `THINK_Data_Science_for_Business.md`. [Rule 14: SUCCESS]

---
WRITE REPORT:
  file: "3-resources/wiki/concepts/CONCEPT_THINK_Naive_Bayes_Logic.md"
  operation: "overwrite"
  added: "Chuẩn hóa theo v4.1, giải thích tính ngây ngô (Naive) của thuật toán."
  removed: "NONE"
  compliance: "[Rule 20] Đã đối soát Template và Raw thành công."


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
