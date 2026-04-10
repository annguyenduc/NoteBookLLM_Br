# 🧠 Module: Xây dựng Bộ não AI (High-Depth ID Edition)

> **Tiêu chuẩn**: LOM v3.5 | Bybee 5E | NASA EDP | UNESCO ICT-CFT
> **Đối tượng**: Học sinh THPT (G10-G12)
> **Thời lượng**: 3 Buổi (45 phút/buổi)
> **Năng lực định hướng (ISTE/UNESCO)**: 
> - **Knowledge Constructor**: HS biết cách tổ chức tri thức số.
> - **Computational Thinker**: HS hiểu cách hệ thống AI truy xuất dữ liệu.

---

## 🏛️ 1. Ma trận Thẳng hàng Sư phạm (Alignment Matrix)

| Mục tiêu năng lực (Bloom) | Hoạt động dạy học (Hybrid 5E-EDP) | Công cụ đánh giá |
| :--- | :--- | :--- |
| **Ghi nhớ (Remember)**: Nhắc lại được mô hình 3 lớp của LLM Wiki. | **Engage**: Tình huống "AI bị ảo giác" do thiếu dữ liệu thực tế. | Kiểm tra miệng / Quiz nhanh. |
| **Hiểu (Understand)**: Giải thích được ẩn dụ "Cung điện ký ức" trong quản lý tri thức. | **Explore/Explain**: Thao tác trên NotebookLM để thấy sự khác biệt giữa các Source. | Giải thích sơ đồ (Analogy). |
| **Vận dụng (Apply)**: Thiết kế được một bộ não AI cho một môn học cụ thể. | **Elaborate (EDP - Ask/Plan)**: HS lập kế hoạch nguồn dữ liệu cho môn học yếu nhất. | Bản kế hoạch "Memory Palace". |
| **Sáng tạo (Create)**: Xây dựng hệ thống truy vấn đa tầng trên Gemini. | **Elaborate (EDP - Create/Test)**: HS tạo "Nhạc trưởng" điều phối trên Gemini App. | Rubric sản phẩm cuối khóa. |

---

## 📅 KẾ HOẠCH BÀI DẠY CHI TIẾT

### 🔵 Buổi 1: Thư viện Tri thức Triệu đô (Foundations)
*Trọng tâm: Hiểu về Ingestion & Source Management.*

- **Engage (5')**: 
    - **Tình huống**: "Nếu bạn đưa cho AI một bài toán mới toanh vừa xuất hiện sáng nay, nó có giải được không?" -> Dẫn dắt về khái niệm "Dữ liệu thô" (Raw Data).
- **Explore (10')**:
    - HS truy cập NotebookLM. Nạp 2 file PDF khác nhau vào 1 Notebook.
    - So sánh câu trả lời của AI khi có và không có Source.
- **Explain (15')**: 
    - **Ẩn dụ**: 
        - **Raw**: Giống như "Sách tài liệu" trong kho. AI chỉ đọc, không sửa.
        - **Wiki**: Giống như "Bản đồ tri thức" do thủ thư tóm tắt lại.
        - **Schema**: Giống như "Nội quy mượn sách" để AI biết tìm ở đâu.
    - Giới thiệu mô hình **LLM Wiki 3 lớp**.
- **Elaborate (EDP - Ask/Imagine) (10')**:
    - **Thử thách**: "Xác định mục tiêu: Bạn muốn xây bộ não để thi Đại học hay để làm dự án Khoa học? Bạn cần những 'nguyên liệu' nào?"
- **Evaluate (5')**: 
    - Q&A: "Tại sao không nên nạp quá 50 file vào cùng một lúc?" (Giới thiệu về giới hạn ngữ cảnh - Context Window).

---

### 🔴 Buổi 2: Kiến trúc sư Cung điện ký ức (Architecture)
*Trọng tâm: Chức năng tổ chức & Liên kết tri thức.*

- **Engage (5')**:
    - Trình chiếu một sơ đồ Cung điện ký ức của Sherlock Holmes. Hỏi: "Làm sao AI biết tìm tài liệu ở đâu trong 1 vạn trang giấy?"
- **Explore (10')**:
    - HS dùng tính năng "Saved Notes" trong NotebookLM để tạo ra các "Phòng" (Rooms) tri thức.
- **Explain (10')**:
    - Giải thích về **Vector Database** (Ẩn dụ: Tọa độ của các ngôi sao trên bầu trời tri thức - Các ý tưởng gần nhau sẽ ở gần nhau).
    - Hướng dẫn kỹ thuật **Prompting để chưng cất** (Distillation).
- **Elaborate (EDP - Plan/Create) (15')**:
    - **Kỹ thuật Faded Examples (Gợi ý từng phần)**: 
        - Giáo viên cung cấp một "Cấu trúc Cung điện mẫu" gồm 3 phòng đã có sẵn. 
        - HS thực hiện bước **Plan** để xây dựng thêm 2 phòng mới cho cá nhân.
    - Thực hiện bước **Create**: Tạo ra ít nhất 3 ghi chú chắt lọc liên kết đa chiều.
- **Evaluate (5')**:
    - Trình bày nhanh 1 liên kết "độc đáo" giữa 2 chương học khác nhau (Ví dụ: Sự tương đồng giữa các cuộc cách mạng trong Lịch sử).

---

### 🟢 Buổi 3: Nhạc trưởng Điều phối (Orchestration)
*Trọng tâm: Prompting nâng cao & Kiểm thử hệ thống.*

- **Engage (5')**:
    - Giới thiệu Gemini App. Hỏi: "Nếu ta có thư viện rồi, ai sẽ là người đọc và viết báo cáo cho ta?" -> Vai trò của **Agent/Orchestrator**.
- **Explore (10')**:
    - HS sử dụng Gemini App, yêu cầu nó đóng vai chuyên gia tư vấn dựa trên dữ liệu từ NotebookLM.
- **Explain (10')**:
    - Giới thiệu **Meta-Prompting** & **Socratic Framework**.
    - Tại sao phải có bước **Test** (Thử nghiệm) và **Improve** (Cải tiến) trong EDP?
- **Elaborate (EDP - Test/Improve/Present) (15')**:
    - HS đặt câu hỏi khó cho "Bộ não AI" của mình. 
    - Phát hiện lỗi (Ảo giác, thiếu thông tin).
    - **Improve**: Quay lại NotebookLM bổ sung nguồn hoặc sửa Prompt.
- **Evaluate (5')**:
    - Đánh giá chéo sản phẩm dựa trên Rubric "Độ tin cậy & Tính liên kết".

---

## 📊 3. BỘ CÔNG CỤ ĐÁNH GIÁ (ASSESSMENT PACK)

### Phần A: Câu hỏi tình huống (Concept Test)
- **Tình huống**: AI trả lời sai một công thức vật lý dù bạn đã nạp sách vào. Bạn sẽ làm gì tiếp theo?
    - A) Xóa Notebook làm lại.
    *   B) Kiểm tra lại file Raw xem có mờ không và bổ sung prompt "Check Step-by-step". (Đáp án đúng)
    - C) Bỏ qua vì AI luôn đúng.

### Phần B: Rubric Sản phẩm (Skill Assessment)

| Tiêu chí | Cần cố gắng (1-2đ) | Đạt (3-4đ) | Xuất sắc (5đ) |
| :--- | :--- | :--- | :--- |
| **Tính cấu trúc** | Tài liệu nạp lộn xộn, không phân loại. | Có phân loại theo thư mục/tên file rõ ràng. | Có hệ thống ghi chú (Saved Notes) liên kết đa chiều. |
| **Chất lượng Prompt** | Prompt đơn giản (Làm đi, Giúp tôi). | Sử dụng được cấu trúc V-N-N. | Sử dụng được Socratic Prompt & CoT nâng cao. |
| **Tính ứng dụng** | Không giải quyết được bài tập thực tế. | Giải quyết được các câu hỏi cơ bản trong Source. | Có khả năng tư vấn, gợi mở tư duy cho HS. |

---
*Phát triển bởi @pm | Dựa trên chuẩn NASA EDP & Moore's Law of Learning v3.5*
