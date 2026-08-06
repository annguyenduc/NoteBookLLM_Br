# NoteBookLLM_Br (EduResearch Hub v2.0)

Chào mừng bạn đến với **EduResearch Hub v2.0** — Hệ thống Quản trị Tri thức và Thiết kế Sư phạm Tự động hóa. 

Đây là một Workspace đặc biệt, được thiết kế chuyên biệt để hoạt động như một "Bộ nhớ ngoài" (External Brain) cho con người, đồng thời cung cấp môi trường làm việc trực tiếp cho các AI Agents (như Antigravity, Claude Code, v.v.).

---

## 🏗 Kiến Trúc (Architecture)

Toàn bộ tài nguyên, giáo án, và dữ liệu nghiên cứu trong kho lưu trữ này được quy hoạch chặt chẽ theo 6 luồng chuyên biệt, đảm bảo tính mạch lạc tuyệt đối:

- **📁 01_NghienCuu_Review/**: Khu vực nghiên cứu, review lý thuyết giáo dục (STEM, AI in Ed).
- **📁 02_Khung_ChuyenMon/**: Khung chương trình chuẩn (K-12, Math, Science).
- **📁 03_ThietKe_BaiDay/**: Nơi thiết kế bài dạy, giáo án phân hóa (3 mức độ).
- **📁 04_DanhGia_KiemTra/**: Bộ công cụ đánh giá, ma trận đề, rubric.
- **📁 05_Kho_NguyenLieu/**: Kho chứa dữ liệu thô và Vùng đệm (Staging Buffer) cho AI xử lý.
- **📁 06_LuuTru_Archive/**: Khu vực lưu trữ các đồ án cũ.

Tất cả các công cụ kỹ thuật, script, và cấu hình của AI Agent được ẩn gọn gàng bên trong thư mục **`.agent/`**.

## 🤖 Cách Hệ Thống AI Hoạt Động

Workspace này sử dụng các file Markdown cốt lõi ở thư mục gốc (như `AGENTS.md`, `SOUL.md`) làm "Hiến pháp" (Runtime Source of Truth). Bất kỳ AI Agent nào khi bước vào thư mục này đều bắt buộc phải:
1. Đọc và tuân thủ các ranh giới an toàn (không tự xóa/ghi đè tài nguyên chính thức).
2. Tự động tra cứu và sử dụng các **Kỹ năng (Skills)** đã được định nghĩa trong `.agent/skills/`.
3. Lưu mọi file nháp và tiến trình thực thi vào vùng đệm trước khi trình phê duyệt.

## 🤝 Human-in-the-Loop (Sự Can Thiệp Của Con Người)

Triết lý của EduResearch Hub là **"Sư phạm trước, Công cụ sau"**. AI đảm nhận việc sơ chế (OCR, trích xuất web), nhưng **quyền quyết định cuối cùng và việc tổng hợp tri thức luôn thuộc về Con người**. Mọi thay đổi lớn lên tài nguyên trong luồng 01-06 đều yêu cầu sự phê duyệt rõ ràng từ người dùng.

---
*Thuộc sở hữu và cấu hình bởi NoteBookLLM_Br Team.*