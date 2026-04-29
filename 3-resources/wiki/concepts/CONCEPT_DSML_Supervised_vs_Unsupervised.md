---
file_id: "WIKI_CONCEPT_DSML_SUPERVISED_UNSUPERVISED"
title: "Học có giám sát và Học không giám sát (Supervised vs Unsupervised)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Data_Analysis", "DSML", "ML_Basics"]
source: "`DSML_Data_Analytics_Concepts`"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# Học có giám sát và Học không giám sát (Supervised vs Unsupervised)

Đây là hai phương pháp học máy cơ bản, khác nhau ở việc dữ liệu đầu vào có được "gán nhãn" hay không.

## 核心 (Core Principle)
1. **Supervised Learning (Học có giám sát):** Dữ liệu có nhãn (Label/Target). Máy học từ các ví dụ đã biết kết quả để dự báo kết quả mới.
   - *Ví dụ:* Hồi quy, Phân loại.
2. **Unsupervised Learning (Học không giám sát):** Dữ liệu không có nhãn. Máy tự tìm ra các cấu trúc ẩn hoặc các nhóm tự nhiên trong dữ liệu.
   - *Ví dụ:* Phân cụm (Clustering), Giảm chiều dữ liệu.

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Tài liệu (trang 5-10) giải thích rằng Supervised giống như học sinh học với giáo viên có lời giải (Labels), trong khi Unsupervised giống như việc tự mày mò khám phá một vùng đất mới không có bản đồ.

### 2. Ứng dụng sư phạm (Pedagogical Application)
- **Supervised:** Bạn cho máy xem 1000 ảnh "Con Chó" và "Con Mèo" có tên sẵn. Sau đó máy có thể tự nhận diện ảnh mới là Chó hay Mèo.
- **Unsupervised:** Bạn đưa máy một thùng chứa lẫn lộn 1000 món đồ chơi. Máy sẽ tự xếp những món giống nhau (về màu sắc hoặc hình dáng) vào các đống riêng biệt dù không biết tên món đồ đó là gì.

## Liên kết tư duy
- [[CONCEPT_DSML_Clustering_KMeans]]
- [[CONCEPT_DSML_Decision_Trees_Random_Forest]]

## 4F — Phản tư sư phạm
- **Facts:** Hầu hết các ứng dụng thực tế thành công hiện nay là Học có giám sát.
- **Feelings:** Người mới thường cảm thấy Học không giám sát "thông minh" hơn vì nó tự tìm ra quy luật, nhưng thực tế nó khó đánh giá độ chính xác hơn.
- **Findings:** Sự khác biệt nằm ở sự tồn tại của biến mục tiêu ($Y$).
- **Futures:** Kết hợp cả hai (Semi-supervised) là hướng đi tiềm năng cho dữ liệu thiếu nhãn.

---
Nguồn: [[SOURCE_DSML_Data_Analytics_Concepts]] (Page 5-12) (Xác nhận Rule 14 từ: `DSML_Data_Analytics_Concepts`)
