---
file_id: CONCEPT_THINK_TF_IDF_Text_Mining
title: CONCEPT Tần suất từ và Nghịch đảo Tần suất văn bản (TF-IDF)
type: concept
status: VERIFIED
tags:
ai-first: true
confidence: 0.8
last_reconciled: 2026-05-08
created: 2026-05-01
last_updated: 2026-05-07
---

# Tần suất từ và Nghịch đảo Tần suất văn bản (TF-IDF)

## 1. Định nghĩa
- **TF (Term Frequency)**: Tần suất xuất hiện của một từ trong một văn bản cụ thể.
- **IDF (Inverse Document Frequency)**: Mức độ hiếm của một từ trên toàn bộ tập hợp các văn bản.
- **TF-IDF**: Trọng số cho biết một từ quan trọng như thế nào đối với một văn bản trong một bộ sưu tập. Nó giúp loại bỏ các từ phổ biến (như "là", "thì", "mà") và làm nổi bật các từ mang tính đặc trưng.

## 2. Tại sao quan trọng?
TF-IDF là nền tảng cho việc tìm kiếm thông tin và phân loại văn bản. Nó giúp máy tính hiểu được "chủ đề" của một văn bản dựa trên những từ đặc trưng nhất của văn bản đó.

## 3. Ví dụ đối chiếu (R18: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Phân loại tin nhắn rác (Spam Detection).
> **Ứng dụng**: Các từ như "Win", "Prize", "Free" có TF cao trong các tin nhắn rác nhưng lại có IDF rất cao (vì chúng ít xuất hiện trong tin nhắn thông thường). Do đó, chỉ số TF-IDF của chúng sẽ rất lớn trong các tin nhắn rác, giúp bộ lọc nhận diện chính xác.
> **Nguồn**: [[SOURCE_Data_Science_For_Business]].

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Tóm tắt các chủ đề thảo luận của học sinh trên diễn đàn.
> **Ứng dụng**: Hệ thống quét hàng nghìn bình luận. Những từ như "Code", "Robot", "Cảm biến" sẽ có TF-IDF cao vì chúng xuất hiện nhiều trong các bài thảo luận chuyên môn nhưng không xuất hiện nhiều trong các cuộc hội thoại xã giao thông thường. Điều này giúp giáo viên biết lớp đang tập trung vào chủ đề kỹ thuật nào.

## 4. Trích dẫn nguồn
- **Nguồn**: [[SOURCE_Data_Science_For_Business]].


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
