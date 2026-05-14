# Session Insight: Kiểm định Tài nguyên & Tối ưu Hệ thống (2026-05-14)

## 1. Bối cảnh (Context)
Trong quá trình vận hành Wiki 2.0, hệ thống ghi nhận tình trạng chiếm dụng RAM và ổ cứng bất thường. Cần thực hiện audit sâu để đảm bảo môi trường sạch cho các tác vụ LLM nặng và tránh xung đột tiến trình.

## 2. Các phát hiện quan trọng (Key Discoveries)

### 2.1. "Bóng ma" Tiến trình (Process Bloat)
- **Zombie Python:** Phát hiện nhiều tiến trình `local_ai.py` và `run_mcp.py` bị treo từ các phiên làm việc cũ, chiếm dụng ~1.34 GB RAM.
- **Autodesk ODIS:** Dịch vụ `DownloadManager.exe` tự động khởi chạy 11 tiến trình ngầm mặc dù không sử dụng phần mềm, chiếm thêm ~600 MB RAM.

### 2.2. "Kho ảnh rác" 17GB trong Chrome
- **Định danh:** Thư mục `File System` trong Profile 7 của Chrome (Email: `an.nguyenduc@kdi.edu.vn`) chiếm tới **17.3 GB**.
- **Loại dữ liệu:** Phân tích Header xác nhận chủ yếu là ảnh **PNG**, **JPEG** và **Web Fonts (WOFF2)**.
* **Thủ phạm:** Tiện ích **Google Docs Offline** đã âm thầm cache toàn bộ kho tài liệu Drive sang ổ E dưới dạng hàng triệu mảnh nhỏ để phục vụ làm việc ngoại tuyến.

### 2.3. Minh bạch Kiến trúc Antigravity
- Làm rõ cơ chế đa tiến trình (Multi-process model) để người dùng phân biệt được các tiến trình chuyên biệt: Renderer, Utility (NodeService), và Language Servers (Markdown/JSON).

## 3. Hành động & Kết quả (Actions & Results)
- **Giải phóng tài nguyên:** Đã dọn dẹp triệt để các tiến trình thừa và hướng dẫn người dùng `Disable` dịch vụ Autodesk để duy trì sự ổn định lâu dài.
- **Bảo toàn tiếng Việt:** Tái khẳng định quy tắc **R4 (Surgical UTF-8)**: Tuyệt đối dùng Python làm cầu nối ghi dữ liệu để chống lỗi font do PowerShell gây ra.
- **Xác thực Profile:** Cung cấp thông tin nhận diện "Person 1" để người dùng thực hiện dọn dẹp rác Chrome một cách an toàn.

## 4. Bài học & Khuyến nghị (Learnings)
- **Vệ sinh định kỳ:** Cần thực hiện audit RAM sau mỗi 4 tiếng làm việc hoặc sau khi kết thúc một Ingest Batch lớn.
- **Quản lý Cache:** Đề xuất tắt chế độ Offline của Google Docs nếu không thực sự cần thiết để giải phóng 17GB ổ cứng.
- **Giám sát MCP:** Cần cơ chế tự động đóng các MCP Server khi session kết thúc để tránh tình trạng zombie process.

---
**Trạng thái:** VERIFIED
**Người thực hiện:** @antigravity (Agentic AI)
**Đối chiếu quy tắc:** Tuân thủ R4, R9, R14.
