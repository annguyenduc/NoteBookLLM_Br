# 🎓 Bài giảng ToT: Hệ thống Tưới cây Thông minh IoT

---
tags: #lesson-plan #tot #iot #yolo-uno #steam
created: 2026-04-08
last_updated: 2026-04-08
links: [[Pedagogical_Master_DNA]], [[Engineering_Robotics_Master]]
---

# Title: Thiết kế & Triển khai Hệ thống Tưới cây Tự động với Yolo Uno (ESP32-S3)

## 🎯 Context & Purpose
**Mục tiêu**: Trang bị cho Giáo viên năng lực thiết kế dự án IoT thực tế, từ việc hiểu bản chất logic cảm biến đến việc tối ưu hóa code điều khiển máy bơm mà không làm đóng băng hệ thống.
**Vấn đề giải quyết**: Khắc phục tình trạng "copy-paste code" và thiết kế bài giảng thiếu tính căn chỉnh (misalignment) giữa mục tiêu và đánh giá.

## 🧠 Core Principles (ID Expert Heritage)
- **Alignment**: Mục tiêu Bloom -> EDP (Ask, Imagine, Plan, Create, Test, Improve) -> Rubric hành vi.
- **DNA**: 90 phút (37-39-17-7 Ratio).
- **Yêu cầu kỹ thuật**: Code non-blocking, Hardware map chuẩn.

## 🛠️ Implementation / Details

### 1. Mục tiêu học tập (Learning Objectives) - Mapping Bloom
| Bloom Level | Objective (Mục tiêu đo lường được) |
|-------------|-----------------------------------|
| **Remembering** | Nêu đúng các chân kết nối (Pinout) của cảm biến độ ẩm và máy bơm trên Yolo Uno. |
| **Understanding** | Giải thích lược đồ hoạt động của rơ-le (Relay) trong việc điều khiển thiết bị AC/DC công suất cao. |
| **Applying** | Lập trình thành công logic tưới nước tự động dựa trên ngưỡng độ ẩm định trước. |
| **Analyzing** | Phân biệt sự khác biệt về hiệu suất giữa code dùng `delay()` và code dùng `millis()`. |
| **Evaluating** | Đánh giá tính an toàn của hệ thống khi chạy thực tế (Common Ground, Chống nhiễu). |
| **Creating** | Cải tiến hệ thống để thêm tính năng cảnh báo (Đèn Led hoặc Còi Buzz) khi bồn nước cạn. |

### 2. Cấu trúc chương trình (90 Phút) - Ratio Audit
| Thời lượng | Hoạt động | Giai đoạn EDP |
|-----------|-----------|---------------|
| **10' (11%)** | **Mở đầu**: Scenario cày nát cây do quên tưới. Phân tích nhu cầu. | Ask |
| **23' (26%)** | **Lý thuyết**: Nguyên lý cảm biến điện trở & Logic điều khiển rơ-le. | Imagine |
| **35' (39%)** | **Thực hành**: Đấu nối mạch & Lập trình MicroPython (Non-blocking). | Plan & Create |
| **15' (17%)** | **Thảo luận**: Tối ưu hóa ngưỡng tưới cho từng loại cây khác nhau. | Test & Improve |
| **7' (7%)** | **Tổng kết**: Q&A và hướng dẫn mở rộng sang IoT MQTT. | Communication |

### 3. Sơ đồ phần cứng (Hardware Map)
- **Cảm biến độ ẩm đất**: Chân A0 (Yolo Uno).
- **Máy bơm (Relay)**: Chân P1 (Dự kiến).
- **Đèn báo trạng thái**: Led RGB tích hợp sẵn trên Yolo Uno.

## 🔗 Relations & Dependencies
- Cấp trên: [[Education_AI_Handbook]]
- Liên quan: [[k12-iot-scaffold]], [[rubric-builder]]

## 🛡️ Reconciliation
- **Status**: #active
- **Lưu ý**: Sử dụng thư viện `YoloUno` của Ohstem để tương thích tốt nhất.
