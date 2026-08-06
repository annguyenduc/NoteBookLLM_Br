# WORKSPACE OVERVIEW
> EduResearch Hub v2.0 - Hệ thống Tổ chức Tri thức Giáo dục

Tài liệu này cung cấp cái nhìn tổng quan về kiến trúc thư mục cốt lõi của NoteBookLLM_Br. Hệ thống được thiết kế theo tư duy 6 luồng sư phạm (Pedagogical Streams), tập trung vào thiết kế khóa học, chuẩn K-12, và STEM.

---

## 1. Bản Đồ Thư Mục (Directory Map)

Mọi tài nguyên và công việc đều phải được quy hoạch gọn gàng vào 6 luồng sau:

```
NoteBookLLM_Br/
│
├── 📁 01_NghienCuu_Review/    ← RESEARCH & EVIDENCE HUB (PRISMA 2020)
│                                Nơi chứa các phân tích tài liệu, nghiên cứu EdTech,
│                                và tác động của AI trong giáo dục.
│
├── 📁 02_Khung_ChuyenMon/     ← CURRICULUM & STANDARDS
│                                Khung chương trình Toán K-12, STEM, chuẩn Bloom.
│
├── 📁 03_ThietKe_BaiDay/      ← INSTRUCTIONAL DESIGN & LESSON LAB
│                                Kế hoạch bài dạy, giáo án phân hóa 3 mức
│                                (Dưới chuẩn, Đạt chuẩn, Vượt chuẩn).
│
├── 📁 04_DanhGia_KiemTra/     ← ASSESSMENT & RUBRICS
│                                Ma trận đề thi, Rubric chấm điểm STEM,
│                                câu hỏi kiểm tra đánh giá.
│
├── 📁 05_Kho_NguyenLieu/      ← LEARNING MEDIA & RESOURCES
│                                Kho lưu trữ nguyên liệu thô (PDF, ảnh, media).
│                                Chứa Vùng đệm (Staging Buffer) cho Agent xử lý.
│
├── 📁 06_LuuTru_Archive/      ← ARCHIVE
│                                Chứa hệ thống PKM cũ, các đồ án đã hoàn thành,
│                                hoặc tài nguyên không còn sử dụng.
│
└── 📁 .agent/                 ← KỸ NĂNG & QUY TRÌNH
                                 "Não bộ" của Workspace. Chứa kỹ năng, scripts,
                                 thư mục nháp (scratch) và log của Agent.
```

## 2. Vùng Đệm Thô (Staging Buffer)
Khác với các hệ thống Zettelkasten cũ (bắt buộc dùng thư mục `00_Inbox`), EduResearch Hub v2.0 áp dụng **Vùng đệm động (Dynamic Buffer)**.

- **Vị trí mặc định**: Được khai báo trong tệp `.agent/config/workspace-routing.yaml`. (Ví dụ: `05_Kho_NguyenLieu/pdf_raw`).
- **Mục đích**: Là nơi cách ly tài liệu thô (từ web scrape, tải PDF). Mọi tài liệu mới phải nằm ở đây để sơ chế (Intake & Triage) trước khi được Con người phê duyệt đưa vào luồng chính.

## 3. Quy Tắc Bất Biến
1. **Không tạo thêm luồng**: Root Workspace chỉ được phép chứa các thư mục từ `01` đến `06` và `.agent`.
2. **Ẩn công cụ kỹ thuật**: Mọi thư mục chứa code (`scripts/`, `libs/`) và file tạm (`scratch/`) phải nằm bên trong `.agent/`.
3. **Không ghi trực tiếp**: Agent không được ghi trực tiếp tài liệu thô vào kho tài nguyên hoàn chỉnh nếu chưa qua khâu kiểm duyệt Markdown (Quality Gate).
