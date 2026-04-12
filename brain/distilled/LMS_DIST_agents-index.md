# 🧠 AI Agents Capacity Index (v4.0 Free Tier)

Tài liệu này đánh giá và phân loại năng lực của các model miễn phí khả dụng qua 9Router để phục vụ Swarm Pedagogical Pipeline.

## 🚀 So sánh Chủ lực: Gemini 3 Flash vs. OSS Models

| Đặc điểm | ag/gemini-3-flash | groq/llama-3.3-70b | groq/qwen/qwen3-32b |
| :--- | :--- | :--- | :--- |
| **Tốc độ** | Rất nhanh (4.0s) | Cực nhanh (2.4s) | Cực nhanh (2.2s) |
| **Lý luận (Reasoning)** | Trung bình (Flash-tier) | **Cao (70B parameter)** | Khá (32B specialized) |
| **Instruction Following** | Tốt | Rất tốt | **Xuất sắc** |
| **Ngữ cảnh** | **Cực dài (1M+)** | Trung bình (128k) | Trung bình (128k) |
| **Ưu tiên Sư phạm** | **Heavy Context Analysis** | **Complex ID Design** | **Scaffold & Structure** |

---

## 🎭 Phân vai Agent Swarm (Recommended)

Dựa trên kết quả Discovery Ping và Benchmark, đây là cấu hình "Free Tier Supreme" được @pm đề xuất:

### 1. @profiler (Learner Profiler)
- **Model**: `groq/llama-3.3-70b-versatile`
- **Lý do**: Cần khả năng lý luận cao của model 70B để phân tích các insight ngầm từ dữ liệu trainer và xác định knowledge gap chính xác. Mạnh hơn Gemini Flash ở khả năng "đọc giữa các dòng".

### 2. @designer (Instructional Designer)
- **Model**: `groq/qwen/qwen3-32b`
- **Backup**: `groq/llama-3.3-70b-versatile`
- **Lý do**: Qwen cực mạnh trong việc tuân thủ cấu trúc (UDL, 5E). Khả năng tạo output JSON/Markdown có cấu trúc chặt chẽ vượt xa Gemini Flash, giúp việc thiết kế chuỗi bài học (learning sequence) không bị "loãng". Llama 70B được dùng làm dự phòng khi cần lý luận phức tạp hơn.

### 3. @engineer (Content Executioner)
- **Model**: `qw/qwen3-coder-plus` (Xác nhận ID: `qw/qwen3-coder-plus`)
- **Lý do**: Model chuyên biệt cho Coding. Khi cần tạo Python code, bài tập Scratch, hoặc IOT scaffold, model này vượt trội về độ chính xác cú pháp so với các model general-purpose.

### 4. @creative (Creative Specialist)
- **Model**: `nvidia/moonshotai/kimi-k2.5`
- **Lý do**: Kimi nổi tiếng với khả năng viết văn tự nhiên, giàu hình ảnh và bối cảnh. Phù hợp tuyệt đối để tạo Case Study, Role-play và các tình huống lớp học thực tế (real-world scenarios).

### 5. @auditor (Integrity Guard)
- **Model**: `groq/llama-3.3-70b-versatile`
- **Lý do**: Cần sự khắt khe và khả năng đối soát logic cực tốt của model 70B để phát hiện hallucination.

### 6. @evaluator (Learning Evaluator)
- **Model**: `groq/qwen/qwen3-32b`
- **Lý do**: Phân tích kết quả đào tạo theo Kirkpatrick cần sự logic và phân loại dữ liệu tốt.

---

## 📌 Tổng kết cho Trainer
- **Gemini 3 Flash**: Chỉ dùng làm fallback hoặc cho các tác vụ cực kỳ đơn giản (Say hello, Identify).
- **Llama 3.3 70B**: Là "bộ não" chính cho thiết kế sư phạm chuyên sâu.
- **Qwen 32B**: Là "kiến trúc sư" cho cấu trúc và định dạng nội dung.
