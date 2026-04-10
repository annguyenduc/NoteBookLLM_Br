---
title: Nghệ Thuật Cấu Trúc Thư Mục Trong Kỷ Nguyên AI
date: 2026-04-09
source: NotebookLM - Nghệ Thuật Cấu Trúc Thư Mục
category: Architecture, Knowledge Management
principles: [Conway's Law, Lifecycle Separation, Flatten Hierarchy, Machine-Readability, Process-Driven Change]
---

# 📂 Nghệ Thuật Cấu Trúc Thư Mục Trong Kỷ Nguyên AI

Trong kỷ nguyên AI, khi số lượng tệp tin có thể tăng lên hàng nghìn chỉ trong vài phút, việc quản lý thư mục không còn là vấn đề cá nhân mà là vấn đề **Kiến trúc Hệ thống**.

## 🏗️ 5 Nguyên lý Quản trị Thư mục (v3.6)

### 1. Ánh xạ Tổ chức (Conway's Law)
> "Sơ đồ tổ chức thế nào, cây thư mục chính phải y hệt như thế."
- Tránh tạo ra các "vùng xám" dữ liệu.
- Phân định trách nhiệm rõ ràng: Nhìn vào thư mục gốc là biết ai/phòng ban nào chịu trách nhiệm.

### 2. Phân tách Vòng đời (Lifecycle Separation)
Ngăn chặn ổ đĩa biến thành "bãi rác" bằng ranh giới cứng:
- **WIP (Work In Progress)**: Chứa tệp đang thay đổi liên tục. Sử dụng thư mục `SPRINTS/` hoặc `Drafts/`.
- **SSOT (Single Source of Truth)**: Chỉ chứa tài liệu đã chốt (Final).
- **Z_Archive**: Lưu trữ mọi thứ đã xong, không bao giờ xóa nhưng cũng không bao giờ làm nhiễu kết quả tìm kiếm hiện tại.

### 3. Chống phân mảnh quá sâu (Flatten the Hierarchy)
- **Quy tắc Vàng**: Độ sâu tối đa là **3 cấp**.
- **Giải pháp**: Nếu cần phân loại sâu hơn, hãy sử dụng **File Naming** và **Metadata** (YAML Frontmatter) thay vì tạo thêm folder lồng nhau. Việc này giúp AI Crawler scan dữ liệu nhanh hơn gấp nhiều lần.

### 4. Thân thiện với Máy móc (Machine-Readability)
- **Naming**: Sử dụng `Snake_Case`, `PascalCase`, hoặc `kebab-case`. Không dùng dấu cách hoặc tiếng Việt có dấu trong tên file/folder.
- **Prefix**: Dùng số thứ tự (`01_`, `02_`) để kiểm soát trật tự hiển thị.
- **Header**: Giấu ngữ cảnh vào phần YAML Header thay vì nhét quá nhiều thông tin vào tên file.

### 5. "Phá vỡ là một quy trình" (Breaking is a Process)
- Một cấu trúc thư mục tốt là cấu trúc có quy trình cho sự thay đổi.
- Mọi sự thay đổi cấu trúc lớn phải đi qua một **Sprint đánh giá**, không thay đổi tạt ngang.

## 🔗 Liên kết liên quan
- [[AGENTS.md]] - Quy tắc vận hành Agent Swarm.
- [[DevOps_IT_Automation_Wiki]] - Tự động hóa hạ tầng.
- [[FILE_BACK_SOP]] - Quy trình lưu tri thức.

---
*Được chưng cất bởi @librarian | Phần một của chiến dịch Nâng cấp LLM Wiki v3.6*
