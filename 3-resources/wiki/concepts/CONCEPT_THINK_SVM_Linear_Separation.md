---
file_id: CONCEPT_THINK_SVM_Linear_Separation
title: CONCEPT Máy Vector Hỗ trợ và Phân tách Tuyến tính (SVM)
type: concept
status: VERIFIED
tags:
ai-first: true
confidence: 0.8
last_reconciled: 2026-05-08
created: 2026-05-01
last_updated: 2026-05-07
---

# Máy Vector Hỗ trợ và Phân tách Tuyến tính (SVM)

## 1. Định nghĩa
SVM (Support Vector Machine) là một thuật toán phân loại mạnh mẽ tìm kiếm một **Siêu phẳng (Hyperplane)** để phân chia các điểm dữ liệu của hai lớp khác nhau với khoảng cách (Margin) lớn nhất có thể.

## 2. Nguyên lý
- **Support Vectors**: Là các điểm dữ liệu nằm gần siêu phẳng phân chia nhất. Nếu thay đổi các điểm này, vị trí siêu phẳng sẽ thay đổi.
- **Maximum Margin**: SVM cố gắng tạo ra "con đường" rộng nhất giữa hai lớp để giảm thiểu sai sót khi có dữ liệu mới.
- **Kernel Trick**: Kỹ thuật biến đổi dữ liệu từ không gian thấp chiều sang không gian cao chiều để có thể phân tách chúng một cách tuyến tính.

## 3. Ví dụ đối chiếu (R18: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Nhận dạng chữ viết tay (Digit Recognition).
> **Ứng dụng**: SVM tìm cách phân biệt giữa chữ số "0" và "8". Mặc dù chúng trông khá giống nhau, SVM tìm ra các đặc trưng hình học tinh vi (các vector hỗ trợ) để tạo ra ranh giới phân chia rõ ràng nhất giữa hai tập hợp ảnh này.
> **Nguồn**: [[SOURCE_Data_Science_For_Business]].

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Phân loại học sinh có năng khiếu nghệ thuật và năng khiếu logic.
> **Ứng dụng**: Dựa trên dữ liệu điểm số các môn học. SVM tìm ra một ranh giới (siêu phẳng) tối ưu để tách biệt hai nhóm. Những học sinh nằm sát ranh giới (Vector hỗ trợ) là những em có năng khiếu hỗn hợp, cần được giáo viên quan tâm định hướng kỹ hơn.

## 4. Trích dẫn nguồn
- **Nguồn**: [[SOURCE_Data_Science_For_Business]].


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
