---
title: LMS Deep Knowledge - Trí tuệ Nhân tạo (A.I)
type: knowledge_base
category: AI
tags: [Machine-Learning, Dataset, Model, Scratch-AI]
last_updated: 2026-04-10
---

# 🤖 LMS Deep Knowledge: Module Trí tuệ Nhân tạo (A.I)

> **Kiểm định bởi**: @auditor (AG-SWARM-006)
> **Trạng thái**: ĐÃ LÀM SẠCH (Loại bỏ 100% kiến thức ngoại lai)

---

## 🏗️ 1. Nền tảng & Công cụ lập trình

| Thành phần | Đặc điểm & Chức năng (Theo LMS) | Trích dẫn nguồn |
| :--- | :--- | :--- |
| **mBlock 5** | Phần mềm chính để lập trình AI. Chia làm 2 khu vực: **Device** (Thiết bị) và **Sprites/Background** (Nhân vật/Phông nền). | [AI_TH_01] |
| **Tài khoản mBlock**| Dùng để: Lưu dự án online, sử dụng các nhóm lệnh mở rộng (AI), chuyển khối lệnh sang Python. | [AI_TH_01] |
| **Phần mở rộng** | Các tính năng AI phải được thêm qua mục **Extension** (Nhận diện giọng nói, Dịch thuật, Teachable Machine). | [AI_TH_01] |

---

## 🧠 2. Các nhóm lệnh AI chuyên sâu (Extensions)

### A. Cognitive Services (Dịch vụ Nhận thức):
- **Chức năng**: Cho phép máy tính nhận diện khuôn mặt, văn bản, giọng nói và dịch thuật. `[Nguồn: AI_TH_01]`
- **Lưu ý**: Cần đăng nhập tài khoản mBlock và có kết nối Internet để sử dụng. `[Nguồn: AI_TH_01]`
- **Các lệnh tiêu biểu**:
    - `Translate [văn bản] to [ngôn ngữ]`: Phiên dịch văn bản.
    - `Speak [văn bản]`: Phát âm thanh từ văn bản (Text-to-Speech).
    - `Recognize [ngôn ngữ] for [số giây]`: Nhận diện giọng nói.

### B. Teachable Machine (Học máy):
- **Quy trình**: Thu thập dữ liệu (Hình ảnh/Âm thanh) -> Huấn luyện model -> Sử dụng model trong lập trình. `[Nguồn: AI_THCS_01]`
- **Cấu trúc Model**: Gồm các **Category (Lớp)**. Ví dụ: Lớp "Trái tim", Lớp "Cây búa".
- **Logic thực thi**: Sử dụng câu lệnh `If [kết quả nhận diện] = [tên lớp] then...`. `[Nguồn: AI_THCS_01]`

---

## 💻 3. Logic lập trình hỗ trợ AI

Hệ thống LMS tập trung vào việc xử lý dữ liệu đầu vào người dùng để tạo ra phản hồi thông minh:

- **Hỏi & Đáp (Ask & Answer)**:
    - Lệnh `Ask [câu hỏi] and wait`: Hiển thị khung nhập liệu.
    - Biến `Answer`: Lưu trữ giá trị người dùng vừa nhập. `[Nguồn: AI_TH_01]`
- **Xử lý chuỗi (Operators)**:
    - `Join [văn bản 1] [văn bản 2]`: Kết nối các chuỗi (VD: "Xin chào " + "An").
    - `[văn bản 1] contains [văn bản 2]?`: Kiểm tra từ khóa trong câu (Dùng cho Chatbot hoặc nhận diện giọng nói). `[Nguồn: AI_TH_01]`
- **Điều kiện (Hexagon Blocks)**: 
    - Các khối lục giác (Boolean) luôn trả về giá trị **True** (Đúng) hoặc **False** (Sai). `[Nguồn: AI_TH_01]`

---

## 🌍 4. Khái niệm AI Tổng quát (LMS Context)

- **Mục tiêu của AI**: Giúp máy tính có khả năng **suy nghĩ và hành động như con người**. `[Nguồn: AI_TH_01]`
- **Ứng dụng thực tế**: Trợ lý ảo (Siri), nhận diện khuôn mặt, hệ thống trả lời tự động.
- **Phân biệt**: Hệ thống quản trị cơ sở dữ liệu (Database) thường **không** được coi là ứng dụng AI trong phạm vi bài học này. `[Nguồn: AI_TH_01]`

---

## 🚩 5. Lỗi thường gặp & An toàn (Misconceptions)

1. **Lỗi logic If-then**: Câu lệnh điều kiện `if` cần nằm trong vòng lặp `forever` để máy tính liên tục kiểm tra trạng thái (VD: liên tục chờ nghe lệnh "on/off"). `[Nguồn: AI_TH_01]`
2. **Lỗi kết nối**: Nhầm lẫn giữa chế độ **Live** (Chạy trực tiếp trên máy) và **Upload** (Tải lên thiết bị). Các lệnh AI extension thường chạy tốt nhất ở chế độ Live.
3. **An toàn bảo mật**: Không chia sẻ mật khẩu tài khoản mBlock, sử dụng mật khẩu mạnh để bảo vệ dự án.

---
*Tình trạng kiểm định: ĐÃ LÀM SẠCH 100% (Verify bởi @pm & @auditor v6.2)*
