# 🧠 Prompt Engineering Master Wiki

> **Mô tả**: Kho lưu trữ tri thức chuyên sâu về kỹ thuật đặt câu lệnh (Prompt Engineering), từ cơ bản (Lớp cấu trúc) đến nâng cao (Lớp tư duy). 
> **Tiêu chuẩn**: LOM v3.6 | ECC Mastery

---

## 🏗️ 1. Lớp Cấu trúc (Structural Frameworks)

Đây là khung xương của một câu lệnh. Giúp người dùng không bỏ sót các thông tin quan trọng.

### 🥉 Cấp độ 1: V-N-N (Vai trò - Nhiệm vụ - Ngữ cảnh)
- **Đặc điểm**: Đơn giản, dễ nhớ, phù hợp cho người mới bắt đầu hoặc học sinh K-12.
- **Thành phần**:
    - **V - Vai trò (Role)**: Định danh nhân vật cho AI.
    - **N - Nhiệm vụ (Task)**: Làm rõ yêu cầu cần hỗ trợ (Trọng tâm).
    - **N - Ngữ cảnh (Context)**: Ràng buộc, dữ liệu đi kèm.
- **Trạng thái**: Bản địa hóa (Vietnamese Localization) từ các nguyên lý chuẩn quốc tế.

### 🥈 Cấp độ 2: CREATE (Detailed Framework)
- **Đặc điểm**: Chi tiết hơn V-N-N, giúp kiểm soát đầu ra cực kỳ chính xác.
- **Thành phần**: **C**haracter, **R**equest, **E**xamples, **A**djustment, **T**ype, **E**xtra info.

---

## ⚙️ 2. Lớp Tư duy & Kỹ thuật (Reasoning & Techniques)

Đây là "động cơ" bên trong câu lệnh, giúp AI suy nghĩ sâu và logic hơn.

### 🥇 Kỹ thuật nâng cao: Chain-of-Thought (CoT)
- **Cơ chế**: Yêu cầu AI "Hãy suy nghĩ từng bước một" (Let's think step by step).
- **Lợi ích**: Giảm thiểu sai số trong các bài toán logic hoặc lập luận phức tạp. Giúp AI "mở" quy trình tư duy của mình ra để người dùng kiểm soát.
- **So sánh**: V-N-N là cái khung (Trình bày), CoT là cách nghĩ (Xử lý).

### 🥇 Kỹ thuật nâng cao: Few-Shot Prompting
- **Cơ chế**: Cung cấp một vài ví dụ (Input -> Output) trước khi yêu cầu kết quả cuối cùng.
- **Lợi ích**: Giúp AI nắm bắt được "phong cách" (Style) và "định dạng" muốn đạt được một cách chính xác tuyệt đối.

### 🥇 Kỹ thuật nâng cao: Context Engineering
- **Cơ chế**: Cung cấp bối cảnh đa tầng (System, User, Tool output) để AI có hệ quy chiếu chính xác.
- **Kỹ thuật "Big Context"**: Nạp toàn bộ tài liệu liên quan vào context (như dự án Antigravity đang làm) để AI không bị ảo giác khi trả lời về hệ thống phức tạp.

### 🥇 Kỹ thuật nâng cao: Tree of Thoughts (ToT)
- **Cơ chế**: AI tạo ra nhiều nhánh suy luận, tự đánh giá và chọn đường đi tối ưu.
- **Ứng dụng**: Lập kế hoạch chiến lược.

### 🥇 Kỹ thuật nâng cao: ReAct (Reason + Act)
- **Cơ chế**: Kết hợp suy luận (Reasoning) với hành động (Acting). Nền tảng cho AI Agent.

> [!NOTE]
> **Phân biệt CREATE vs Few-Shot**: **CREATE** là khung cấu trúc. **Few-Shot** là kỹ thuật ví dụ để AI bắt chước logic.

---

## 🏗️ 3. Framework "AI as a Tutor" (Gia sư thông minh)
Chuyển đổi AI từ "Công cụ giải hộ" sang "Người đồng hành học tập":

- **System Prompt Cốt lõi**: "Bạn là một gia sư am hiểu phương pháp Socratic. Nhiệm vụ của bạn là không bao giờ được đưa ra đáp án trực tiếp cho học sinh. Thay vào đó, hãy đặt các câu hỏi gợi mở, giải thích các lỗi sai một cách hóm hỉnh và khuyến khích học sinh tự suy luận từng bước."
- **Quy tắc 3 Không**:
    1. Không viết code hộ hoàn toàn (trừ khi là ví dụ minh họa siêu nhỏ).
    2. Không đưa kết quả bài toán ngay lập tức.
    3. Không phán xét lỗi sai của học sinh.

---

## 🏰 4. Lớp Kiến trúc Hệ thống (Architectural Layer)
Dành cho việc xây dựng "Bộ não thứ hai" (Second Brain) bằng AI.

### 🏛️ Mô hình LLM Wiki (3 lớp)
- **Lớp Raw (Dữ liệu thô)**: Thư mục chứa tài liệu gốc (PDF, Word, Ảnh). AI chỉ đọc, không sửa.
- **Lớp Wiki (Tri thức chắt lọc)**: Các file Markdown tóm tắt, liên kết dữ liệu thô thành mạng giao dịch tri thức.
- **Lớp Semantic (Tìm kiếm Nâng cao)**: Tích hợp `qmd` để tìm kiếm ý nghĩa (Vector Search), giúp truy xuất nhanh khi Wiki lớn.
- **Lớp Schema (Luật lệ)**: Các hướng dẫn chỉ đạo AI cách tổ chức và cập nhật Wiki.

### 🏰 Mô hình Cung điện ký ức (Memory Palace)
- **Wings (Khu nhà)**: Các chủ đề lớn (Toán, Lý, Robot).
- **Rooms (Phòng)**: Các nhánh nhỏ của chủ đề.
- **Tunnels (Đường hầm)**: Liên kết logic giữa các phòng (ví dụ: Công thức Vật lý ứng dụng trong lập trình Robot).

---

## ⚙️ 5. Lớp Điều hành & Tác nhân (Operational Layer)
Tối ưu hóa cách AI xử lý và phản hồi thông tin.

### ⚡ Prompt động (Dynamic Prompting)
- **Prompt Injection**: Chỉ nạp các quy tắc cần thiết vào đúng thời điểm (qua System Instructions).
- **Progressive Loading**: Tải ngữ cảnh lũy tiến. Bắt đầu bằng prompt ngắn (~170 token), chỉ tải thêm tài liệu nặng khi cần thiết.

### ⚓ Hệ thống Hooks (Nhắc nhở tự động)
- **Pre-action Hook**: Nhắc AI kiểm tra dữ liệu trước khi thực hiện hành động.
- **Stop Hook**: Tự động tóm tắt công việc và bài học kinh nghiệm khi kết thúc phiên làm việc.

---

## 🤖 6. Lớp Tự trị & Meta-Prompting (Autonomous Layer)
Khi AI tự "tiến hóa" các câu lệnh của chính nó.

- **Meta-Prompting**: Sử dụng AI để viết hộ các prompt phức tạp hoặc tạo ra các Kỹ năng (Skills) mới từ kinh nghiệm thực tế.
- **Idea Files**: Cung cấp ý tưởng trừu tượng để AI tự cấu hình chi tiết (SOP, Code, Prompt).

---

## 📚 7. Thư viện Prompt mẫu & Chiến lược đa môn học

Để áp dụng V-N-N hiệu quả cho khối 10, cần tùy biến thành phần **Nhiệm vụ** theo đặc thù môn học:

- **Môn Tự nhiên (Toán, Lý, Hóa)**: Tập trung vào "Giải cấu trúc vấn đề" (Deconstruction) và "Cảnh báo lỗi sai".
- **Môn Xã hội (Văn, Sử, Địa)**: Tập trung vào "Đa chiều quan điểm", "Bối cảnh lịch sử/văn hóa" và "Tư duy phản biện".
- **Ngoại ngữ**: Tập trung vào "Môi trường giả lập" và "Phản hồi sửa lỗi trực tiếp".

---

## ✅ 8. Rubric Đánh giá Chất lượng Prompt (Prompt Quality Checklist)

Dành cho học sinh tự kiểm tra trước khi gửi lệnh cho AI:

1. [ ] **Tính định danh (Role)**: Đã gán vai trò cụ thể cho AI chưa? (Ví dụ: Chuyên gia, Gia sư).
2. [ ] **Tính mục tiêu (Task)**: Nhiệm vụ có rõ ràng không? Có động từ hành động không? (Ví dụ: Giải thích, Phân tích, Viết).
3. [ ] **Tính bối cảnh (Context)**: AI đã biết mình là học sinh lớp mấy, cần định dạng gì chưa?
4. [ ] **Tính quy trình (Reasoning)**: Đã yêu cầu AI "suy nghĩ từng bước" (CoT) chưa?
5. [ ] **Tính đạo đức (Ethics)**: Prompt có yêu cầu AI làm hộ bài tập (gian lận) hay chỉ để hướng dẫn học tập?

---

## 📊 9. Bảng so sánh Độ phức tạp (Complexity Matrix)

| Framework | Độ khó | Đối tượng | Mục đích chính |
| :--- | :--- | :--- | :--- |
| **V-N-N** | ⭐ (Thấp) | HS G1-G10, Người mới. | Làm quen với việc giao tiếp có cấu trúc. |
| **CREATE** | ⭐⭐ (Vừa) | HS G11-G12, Researcher. | Kiểm soát đầu ra chuyên nghiệp, đa mục tiêu. |
| **CoT** | ⭐⭐⭐ (Cao) | Developer, STEM Project. | Giải quyết các bài toán logic, kỹ thuật khó. |

---

## 🔗 10. Tài liệu tham khảo (Citations)
1. **OpenAI Prompt Engineering Guide**: [link] (Base Pillars: Roles, Instructions, Context).
2. **Vietnamese AI Community (VNN Localization)**: Đúc kết từ các quy tắc RTF/RACE của thế giới sang ngôn ngữ tiếng Việt để phổ cập giáo dục AI.

---
*Cập nhật bởi @librarian | Ngày: 2026-04-09 | Ver: 1.1 | LOM v3.6 Sync*
