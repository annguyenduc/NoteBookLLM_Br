---
file_id: "WIKI_KHMT_AI_MASTER"
title: "Trí tuệ nhân tạo (AI) & Machine Learning"
category: "Wiki Page"
prefix: "WIKI"
tags: ["AI", "Machine_Learning", "Teachable_Machine", "Extension"]
source: "[[KHMT_AI_THCS_de_trac_nghiem_1_-_ai_thcs.md]], [[KHMT_AI_THCS_de_2_trac_nghiem_-_ai_thcs.md]]"
status: "verified"
created: "2026-04-26"
last_updated: "2026-04-26"
---

# 🤖 Trí tuệ nhân tạo (AI) & Machine Learning

## 📌 Định nghĩa cốt lõi
Trí tuệ nhân tạo (AI) là lĩnh vực khoa học máy tính nhằm tạo ra các hệ thống có khả năng thực hiện các nhiệm vụ thông minh như con người. Trong đó, **Machine Learning (Máy học)** là một dạng AI cho phép hệ thống tự học hỏi và cải thiện từ dữ liệu mà không cần lập trình cụ thể cho từng trường hợp.

## 🔍 Chi tiết kỹ thuật & Công cụ

### 1. Nền tảng huấn luyện: Teachable Machine (Google)
*   **Dữ liệu đầu vào**: Hình ảnh (Webcam/Upload), Âm thanh (Micro/Upload), Tư thế (Pose).
*   **Quy trình**: Thu thập dữ liệu (Classes) -> Huấn luyện (Train) -> Kiểm tra (Test) -> Xuất mô hình (Export).
*   **Lưu ý**: 
    *   Có thể dạy máy tính nhận diện vô số lớp (classes) sự vật khác nhau (không giới hạn 4).
    *   Hỗ trợ nạp tệp tin trực tiếp từ máy tính hoặc link Google Drive.
    *   Sử dụng link mô hình đã export để nạp vào mBlock/Dancing with AI qua extension `Teachable Machine`.

### 2. Nền tảng học tập
*   **MIT Dancing with AI**: Truy cập tại `dancingwithai.media.mit.edu`. Đây là phiên bản Scratch tùy biến của MIT dành riêng cho các dự án AI.

### 3. Phân loại khối lệnh đặc thù
*   **Khối lệnh báo cáo (Reporting Blocks)**: Hình oval, trả về giá trị (số/chuỗi). Ví dụ: `answer`.
*   **Khối lệnh Boolean**: Hình lục giác, trả về `True/False`. Ví dụ: `contains`.

### 4. Các nhóm lệnh AI mở rộng (Extensions)
| Extension | Nhóm lệnh chính | Ứng dụng & Chi tiết |
| :--- | :--- | :--- |
| **Text to Speech** | `speak [text]`, `set voice to [voice]` | Chuyển văn bản thành giọng nói. Tông giọng: Alto, Tenor, Squeak, Giant, Kitten. |
| **Translate** | `translate [text] to [language]` | Dịch thuật đa ngôn ngữ. |
| **Video Sensing** | `video motion on [sprite]`, `turn video on` | Tương tác qua Camera. |
| **Face Detection** | `go to [nose/eye/head]` | Theo dõi vị trí các bộ phận khuôn mặt. |
| **Hand Detection** | `go to [index fingertip/thumb]` | Theo dõi vị trí đầu ngón tay. |
| **Cognitive Services** | `recognize ...`, `... result` | Nhận diện giọng nói, chữ viết, đồ vật (Cần đăng nhập mBlock 5). |

### 5. Xử lý dữ liệu nâng cao (List)
*   **Bản chất**: Biến `answer` (từ lệnh Ask) có thể lưu chuỗi văn bản.
*   **Quản lý danh sách**:
    *   `add [item] to [list]`: Thêm mục mới.
    *   `delete [n] of [list]`: Xóa mục tại vị trí n.
    *   `delete all of [list]`: Xóa toàn bộ danh sách (Clear list).
    *   `[list] contains [item]?`: Kiểm tra sự tồn tại (trả về Boolean).

### 6. Lưu ý về Tài khoản mBlock 5
*   **Chức năng**: Lưu/Chia sẻ dự án online, sử dụng các nhóm lệnh AI nâng cao (Cognitive Services), truy cập thư viện Sprite/Background online.
*   **Kết nối**: Đa số các Extension AI cần kết nối Internet (Wifi) và đăng nhập tài khoản để hoạt động.


## 💡 Ví dụ thực tế
*   **Lọc Email**: Tự động phân loại Spam dựa trên nội dung (Machine Learning).
*   **Sentiment Analysis**: Phân tích cảm xúc con người qua văn bản/giọng nói.
*   **Mở khóa khuôn mặt**: Ứng dụng nhận diện khuôn mặt trên điện thoại thông minh.

## 🤖 3. Công cụ huấn luyện No-Code
Học sinh có thể tự huấn luyện các mô hình AI đơn giản mà không cần lập trình thông qua:
*   **[[WIKI_Teachable_Machine]]**: Công cụ của Google giúp huấn luyện nhận diện Hình ảnh, Âm thanh và Tư thế.

## 🔗 Liên kết tư duy
*   [[WIKI_KHMT_General_Master]] - Tổng quan về KHMT.
*   [[WIKI_AI_THCS_System]] - Chương trình học AI cấp THCS.
*   [[WIKI_KHMT_Scratch_Master]] - Nền tảng lập trình kéo thả.

## 4F — Phản tư sư phạm
*   **Facts**: AI không phải là "phép thuật" mà là kết quả của việc xử lý dữ liệu và thuật toán.
*   **Feelings**: Học sinh thường ngạc nhiên khi thấy máy tính có thể "nhận ra" mình sau vài giây huấn luyện.
*   **Findings**: Độ chính xác của AI phụ thuộc rất lớn vào chất lượng và sự đa dạng của dữ liệu đầu vào (Data Quality).
*   **Futures**: Hướng tới việc tạo ra các dự án AI có ích cho cộng đồng (ví dụ: nhận diện rác thải, hỗ trợ người khiếm thị).

## 📖 Nguồn trích dẫn
*   [[[brain/raw/KHMT_AI_THCS_de_trac_nghiem_1_-_ai_thcs.md]]](file:///d:/NoteBookLLM_Br/brain/raw/[[brain/raw/KHMT_AI_THCS_de_trac_nghiem_1_-_ai_thcs.md]])
*   [[[brain/raw/KHMT_AI_THCS_de_2_trac_nghiem_-_ai_thcs.md]]](file:///d:/NoteBookLLM_Br/brain/raw/[[brain/raw/KHMT_AI_THCS_de_2_trac_nghiem_-_ai_thcs.md]])
*   [Dạy AI với Teachable Machine](https://teachablemachine.withgoogle.com/)
