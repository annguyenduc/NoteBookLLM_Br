# 📝 Rubric Đánh giá Năng lực: Thiết kế & Lập trình Hệ thống Tưới cây IoT

---
tags: #rubric #tot #assessment #iot
created: 2026-04-08
links: [[ToT_IoT_Smart_Irrigation]], [[rubric-builder]]
---

# Mục tiêu Đánh giá
Đánh giá năng lực của Giáo viên trong việc thiết kế và triển khai một dự án IoT hoàn chỉnh, bám sát các tiêu chuẩn kỹ thuật và sư phạm STEAM.

## 📊 Bảng Tiêu chí Đánh giá (Competency-Based)

| Tiêu chí | Familiarization (Mức 1) | Functional Improvement (Mức 2) | Pedagogical Redesign (Mức 3) |
| :--- | :--- | :--- | :--- |
| **Thiết kế ID (Alignment)** | Mục tiêu còn mơ hồ, chưa khớp với hoạt động thực hành. | Mục tiêu đo lường được nhưng EDP còn rời rạc, chưa thống nhất. | **Hoàn hảo**: Mục tiêu Bloom khớp 100% với EDP và Rubric này. |
| **Logic Phần cứng** | Đấu nối đúng nhưng chưa có Hardware Map hoặc Pinout table. | Có Hardware Map, nhưng chưa bọc chống nhiễu hoặc bảo vệ relay. | **Chuyên nghiệp**: Pinout rõ ràng, có cơ chế an toàn Common Ground. |
| **Kỹ thuật Lập trình** | Code chạy được nhưng dùng `delay()`, gây treo hệ thống. | Code dùng `millis()` nhưng cấu trúc còn lộn xộn, khó bảo trì. | **Tối ưu**: Lập trình Non-blocking hoàn toàn, cấu trúc modular sạch sẽ. |
| **Tính ứng dụng (Pedagogy)** | Bài giảng tập trung quá nhiều vào lý thuyết (> 50%). | Cân bằng lý thuyết/thực hành nhưng chưa có scenario thực tế. | **Sáng tạo**: Tỷ lệ thực hành > 30%, lồng ghép StoryBrand làm Guide. |

## 🚩 Quality Gate (Red Flags - Audit Check)
- [ ] **Mục tiêu**: Có dùng từ "Biết", "Hiểu" không? (Yêu cầu: Không).
- [ ] **Thực hành**: Tỷ lệ thực hành có đạt > 30% không? (Yêu cầu: Đạt 39%).
- [ ] **Kỹ thuật**: Có lệnh `delay()` trong vòng lặp chính không? (Yêu cầu: Không).
- [ ] **An toàn**: Có nhắc nhở về Common Ground không? (Yêu cầu: Đã nhắc trong Lesson Plan).

## 🛡️ Reconciliation
- **Status**: #active
- **Engine**: ECC Reviewer Gate v1.0
