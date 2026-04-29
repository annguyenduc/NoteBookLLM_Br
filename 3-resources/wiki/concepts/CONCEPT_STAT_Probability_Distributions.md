---
file_id: "WIKI_CONCEPT_STAT_PROBABILITY_DISTRIBUTIONS"
title: "Phân phối xác suất (Probability Distributions)"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Data_Analysis", "STAT", "Distributions"]
source: "`STAT_Practical_Statistics_for_Data_Scientists`"
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# Phân phối xác suất (Probability Distributions)

Phân phối xác suất mô tả tần suất xuất hiện của các giá trị khác nhau trong một tập dữ liệu, giúp chúng ta hiểu về quy luật của dữ liệu đó.

## 核心 (Core Principle)
1. **Normal Distribution (Phân phối chuẩn):** Có hình chuông đối xứng. Đa số các hiện tượng tự nhiên tuân theo quy luật này.
2. **Long-tailed Distribution (Phân phối đuôi dài):** Các giá trị cực lớn xuất hiện với tần suất thấp nhưng có tác động mạnh (ví dụ: thu nhập, kích thước tệp tin).
3. **Binomial Distribution (Phân phối nhị thức):** Dùng cho các sự kiện chỉ có hai kết quả (Thành công/Thất bại).
4. **Poisson Distribution:** Dùng để đếm số sự kiện xảy ra trong một khoảng thời gian/không gian nhất định.

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Trang 65-75 giải thích về việc phân tích lỗi sản phẩm bằng phân phối Poisson. Nếu chúng ta biết trung bình có 2 lỗi trên 100 sản phẩm, Poisson sẽ giúp tính xác suất để một lô hàng có đúng 5 lỗi.

### 2. Ứng dụng sư phạm (Pedagogical Application)
- **Normal Distribution:** Chiều cao của học sinh trong một khối lớp. Đa số sẽ ở mức trung bình, rất ít bạn quá cao hoặc quá thấp.
- **Poisson Distribution:** Đếm số lượng học sinh đi muộn trong một tuần tại cổng trường. Điều này giúp nhà trường sắp xếp nhân sự trực cổng hiệu quả hơn.

## Liên kết tư duy
- [[CONCEPT_STAT_Central_Limit_Theorem]]
- [[CONCEPT_STAT_Data_Taxonomy]]

## 4F — Phản tư sư phạm
- **Facts:** "Dữ liệu lớn" thường làm cho các phân phối trông có vẻ "chuẩn" hơn thực tế.
- **Feelings:** Việc phân biệt giữa xác suất rời rạc và liên tục thường gây khó khăn cho người mới bắt đầu.
- **Findings:** Hầu hết dữ liệu kinh tế là "Đuôi dài", không phải phân phối chuẩn.
- **Futures:** Nên sử dụng các công cụ mô phỏng (Simulations) để học sinh tự "vẽ" ra các phân phối từ dữ liệu ngẫu nhiên.

---
Nguồn: [[SOURCE_STAT_Practical_Statistics_for_Data_Scientists]] (Page 60-80, Chapter 2) (Xác nhận Rule 14 từ: `STAT_Practical_Statistics_for_Data_Scientists`)
