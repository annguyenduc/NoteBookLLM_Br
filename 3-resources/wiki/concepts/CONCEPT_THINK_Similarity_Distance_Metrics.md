---
file_id: CONCEPT_THINK_Similarity_Distance_Metrics
title: CONCEPT Độ tương đồng và Các phép đo Khoảng cách (Similarity & Distance Metrics)
type: concept
status: VERIFIED
tags:
ai-first: true
confidence: 0.8
last_reconciled: 2026-05-08
created: 2026-05-01
last_updated: 2026-05-07
---

# Độ tương đồng và Các phép đo Khoảng cách (Similarity & Distance Metrics)

## 1. Định nghĩa
Trong phân tích dữ liệu, độ tương đồng được định nghĩa dựa trên khoảng cách giữa các điểm dữ liệu trong không gian đa chiều. Hai điểm "gần" nhau thì tương đồng với nhau.

## 2. Các phép đo phổ biến
- **Euclidean Distance**: Khoảng cách "đường chim bay" phổ biến nhất.
- **Manhattan Distance**: Khoảng cách theo các trục tọa độ (giống đi trong thành phố bàn cờ).
- **Cosine Similarity**: Đo góc giữa hai vector, thường dùng trong phân tích văn bản (không phụ thuộc vào độ dài văn bản).

## 3. Ví dụ đối chiếu (R18: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Hệ thống gợi ý sản phẩm (Recommender Systems).
> **Ứng dụng**: Tìm các khách hàng có hành vi mua sắm "gần giống" bạn nhất bằng cách tính khoảng cách giữa các giỏ hàng. Nếu khách hàng A và B cùng mua nhiều mặt hàng giống nhau, họ sẽ ở gần nhau trong không gian dữ liệu.
> **Nguồn**: [[SOURCE_Data_Science_For_Business]].

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Phân nhóm học sinh để tổ chức học nhóm (Clustering).
> **Ứng dụng**: Tính khoảng cách giữa các học sinh dựa trên các tiêu chí: (1) Điểm số, (2) Sở thích môn học, (3) Thời gian rảnh. Những học sinh có "khoảng cách" ngắn nhất sẽ được xếp vào cùng một nhóm vì họ có đặc điểm học tập tương đồng, dễ hỗ trợ nhau.

## 4. Trích dẫn nguồn
- **Nguồn**: [[SOURCE_Data_Science_For_Business]].


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
