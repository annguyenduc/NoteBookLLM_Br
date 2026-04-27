---
file_id: "WIKI_KHMT_SCRATCH_MASTER"
title: "Lập trình trực quan Scratch"
category: "Wiki Page"
prefix: "WIKI"
tags: ["Scratch", "Coding", "Block-based", "Algorithms"]
source: "[[KHMT_Scratch_1_2_Scratch_1_Đề_trắc_nghiệm_1_-_Scratch_M1.md]], [[KHMT_Scratch_1_2_Scratch_1_Đề_trắc_nghiệm_2_-_Scratch_M1.md]], [[KHMT_Scratch_1_2_Scratch_2_Đề_trắc_nghiệm_1_-_Scratch_M2.md]]"
status: "verified"
created: "2026-04-26"
last_updated: "2026-04-26"
---

# 🐱 Lập trình trực quan Scratch

## 📌 Định nghĩa cốt lõi
Scratch là ngôn ngữ lập trình kéo thả (Block-based) giúp học sinh làm quen với tư duy lập trình mà không cần nhớ cú pháp phức tạp. Scratch cho phép tạo ra các câu chuyện tương tác, trò chơi và hoạt hình.

## 🔍 Chi tiết kỹ thuật

### 1. Hệ tọa độ và Không gian (Stage)
*   **Đuôi file**: `.sb3`.
*   **Trục tọa độ**: Sân khấu có kích thước X: -240 đến 240; Y: -180 đến 180. Tâm sân khấu là `(0, 0)`.
*   **Hướng (Direction)**: 0 (lên), 90 (phải), 180 (xuống), -90 (trái).
*   **Chế độ xoay (Rotation Styles)**:
    *   `All around`: Xoay tự do 360 độ.
    *   `Left-right`: Chỉ lật qua trái hoặc phải.
    *   `Don't rotate`: Giữ nguyên hướng hình ảnh dù nhân vật đổi hướng di chuyển.
*   **Thông số nhân vật**: Tên (Sprite), Tọa độ (x, y), Kích thước (Size), Hướng (Direction), Hiển thị (Show/Hide).

### 2. Quản lý Tài khoản và Studio
*   **Tài khoản Giáo viên (Teacher Account)**: 
    *   Chức năng đặc quyền: Tạo lớp học trực tuyến, tạo tài khoản và reset mật khẩu cho học sinh.
    *   Quản lý: Kiểm tra tiến độ hoàn thành bài tập của học sinh qua hệ thống Dashboard.
*   **Studio**: Để thêm một dự án vào Studio, dự án đó **bắt buộc** phải được chia sẻ (Share) công khai.

### 3. Các nhóm lệnh chính (Blocks Categorization)
*   **Hình dáng khối lệnh**:
    *   **Khối lệnh Boolean**: Hình lục giác, trả về giá trị logic `True` hoặc `False`. Dùng trong các câu lệnh điều kiện như `if`, `wait until`.
    *   **Khối lệnh Báo cáo (Reporting)**: Hình oval, trả về giá trị số hoặc chuỗi ký tự. Ví dụ: `answer`, `username`.
*   **Các nhóm lệnh quan trọng**:
    *   **Motion (Chuyển động)**: `move [n] steps`, `goto x:[] y:[]`, `glide [s] to x:[] y:[]`.
    *   **Looks (Hiển thị)**: `say [text] for [s]`, `switch costume to []`, `change size by [n]`.
    *   **Sounds (Âm thanh)**: `start sound []`, `play sound [] until done`.
    *   **Events (Sự kiện)**: `when green flag clicked`, `when [key] pressed`.
    *   **Control (Điều khiển)**: `wait [s]`, `repeat [n]`, `forever`, `if [condition] then`.
    *   **Sensing (Cảm biến)**: 
        *   `touching [sprite]?`: Kiểm tra va chạm.
        *   `ask [question] and wait`: Nhận dữ liệu nhập từ bàn phím, kết quả lưu vào khối `answer`.
    *   **Operators (Phép toán)**: Các phép tính `+ - * /`, `pick random`, và khối `join [string1] [string2]` (dùng để kết nối các chuỗi ký tự).
    *   **Variables (Biến số)**: Lưu trữ giá trị có thể thay đổi (số, chuỗi, boolean). 
        *   `Global`: For all sprites.
        *   `Local`: For this sprite only.
        *   Hiển thị: Normal, Large, Slider.
    *   **Events - Broadcast (Thông điệp)**: `broadcast [message]` và `when I receive [message]`. Dùng để đồng bộ hành động giữa các nhân vật.

### 3. Thuật toán vẽ hình cơ bản
Để vẽ các đa giác đều, ta sử dụng công thức xoay: `turn [360 / n] degrees`.
*   **Hình vuông**: turn 90 độ (4 lần).
*   **Tam giác đều**: turn 120 độ (3 lần).
*   **Lục giác đều**: turn 60 độ (6 lần).
*   **Ngôi sao 5 cánh**: turn 144 độ (5 lần).

### 4. Logic Game và Thuật toán nâng cao
*   **Di chuyển bằng phím**: Sử dụng `if <key [arrow] pressed?>` trong vòng lặp `forever` để tạo cảm giác mượt mà hơn.
*   **Hiệu ứng trọng lực (Rơi tự do)**: Thay đổi `y` một lượng âm liên tục. Khi chạm đất, đưa nhân vật về vị trí `y` cao nhất với `x` ngẫu nhiên.
*   **Hệ thống Điểm/Mạng**: Khởi tạo biến (Set score to 0) khi bắt đầu và thay đổi (Change score by 1) khi va chạm.
*   **Đồng bộ hóa**: Sử dụng `Broadcast` để phối hợp nhiều nhân vật hoặc chuyển màn.

## 💡 Ví dụ thực tế
*   **Dự án Điểm danh**: Sử dụng `List` để lưu tên và `Face Detection` để nhận diện.
*   **Dự án Dịch thuật**: Kết hợp `Translate` và `Text to Speech` để tạo ứng dụng học ngoại ngữ.

## 🔗 Liên kết tư duy
*   [[WIKI_KHMT_General_Master]] - Tổng quan KHMT.
*   [[WIKI_KHMT_AI_Master]] - Ứng dụng AI trong Scratch.

## 4F — Phản tư sư phạm
*   **Facts**: Scratch là công cụ mạnh mẽ để dạy về logic `tuần tự`, `vòng lặp` và `điều kiện`.
*   **Feelings**: Sự tương tác trực quan (kéo thả) giúp giảm rào cản tâm lý khi học lập trình.
*   **Findings**: Việc quản lý tài khoản giáo viên (Teacher Account) rất quan trọng để quản lý lớp học và studio.
*   **Futures**: Chuyển đổi từ Scratch sang Python thông qua mBlock là lộ trình tối ưu nhất.

## 📖 Nguồn trích dẫn
*   [[[brain/raw/KHMT_Scratch_1_2_Scratch_1_Đề_trắc_nghiệm_1_-_Scratch_M1.md]]](file:///d:/NoteBookLLM_Br/brain/raw/KHMT_Scratch_1_2_Scratch_1_%C4%90%E1%BB%81_tr%E1%BA%AFc_nghi%E1%BB%87m_1_-_Scratch_M1.md)
*   [[[brain/raw/KHMT_Scratch_1_2_Scratch_1_Đề_trắc_nghiệm_2_-_Scratch_M1.md]]](file:///d:/NoteBookLLM_Br/brain/raw/KHMT_Scratch_1_2_Scratch_1_%C4%90%E1%BB%81_tr%E1%BA%AFc_nghi%E1%BB%87m_2_-_Scratch_M1.md)
*   [[[brain/raw/KHMT_Scratch_1_2_Scratch_2_Đề_trắc_nghiệm_1_-_Scratch_M2.md]]](file:///d:/NoteBookLLM_Br/brain/raw/KHMT_Scratch_1_2_Scratch_2_%C4%90%E1%BB%81_tr%E1%BA%AFc_nghi%E1%BB%87m_1_-_Scratch_M2.md)
