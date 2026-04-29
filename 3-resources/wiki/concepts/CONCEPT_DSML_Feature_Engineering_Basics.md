---
file_id: "WIKI_CONCEPT_DSML_FEATURE_ENGINEERING"
title: "Kỹ nghệ đặc trưng cơ bản (Feature Engineering Basics)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Data_Analysis", "DSML", "Preprocessing"]
source: "`DSML_Data_Analytics_Concepts`"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# Kỹ nghệ đặc trưng cơ bản (Feature Engineering Basics)

"Dữ liệu tốt đánh bại thuật toán tốt." Kỹ nghệ đặc trưng là quá trình biến đổi dữ liệu thô thành các đặc trưng giúp mô hình học hiệu quả hơn.

## 核心 (Core Principle)
1. **One-Hot Encoding:** Biến đổi dữ liệu chữ (Categorical) thành các cột số 0 và 1.
2. **Scaling/Normalization:** Đưa các số có đơn vị khác nhau về cùng một khoảng (ví dụ: 0 đến 1) để thuật toán không bị thiên lệch.
3. **Feature Creation:** Tạo biến mới từ biến cũ (ví dụ: từ "Ngày sinh" tạo ra biến "Tuổi").
4. **Handling Missing Values:** Điền giá trị thiếu bằng Mean/Median hoặc xóa bỏ.

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Trang 70-80 giải thích rằng nếu bạn để "Lương" (đơn vị hàng triệu) và "Số con" (đơn vị hàng đơn vị) vào cùng một mô hình mà không Scaling, mô hình sẽ coi "Lương" quan trọng gấp triệu lần "Số con".

### 2. Ứng dụng sư phạm (Pedagogical Application)
Giả sử học sinh có danh sách "Thời gian vào lớp" (ví dụ: 07:05, 07:10).
- Máy tính không hiểu giờ phút.
- **Kỹ nghệ:** Chuyển đổi thành "Số phút đi muộn" (5 phút, 10 phút). Con số này máy tính sẽ xử lý được ngay để tính toán độ chuyên cần.

## Liên kết tư duy
- [[CONCEPT_DSML_Supervised_vs_Unsupervised]]
- [[CONCEPT_DSML_Overfitting_Prevention]]

## 4F — Phản tư sư phạm
- **Facts:** Kỹ nghệ đặc trưng là phần tốn nhiều công sức và sự sáng tạo nhất trong khoa học dữ liệu.
- **Feelings:** Người học thường muốn nhảy thẳng vào chạy Model mà quên mất việc tinh chỉnh đặc trưng (Preprocessing).
- **Findings:** Hiểu biết về lĩnh vực (Domain Knowledge) quan trọng hơn kỹ năng code trong bước này.
- **Futures:** "Deep Learning" đang cố gắng tự động hóa kỹ nghệ đặc trưng, nhưng với dữ liệu bảng (Tabular data), con người vẫn làm tốt hơn.

---
Nguồn: [[SOURCE_DSML_Data_Analytics_Concepts]] (Page 70-85) (Xác nhận Rule 14 từ: `DSML_Data_Analytics_Concepts`)
