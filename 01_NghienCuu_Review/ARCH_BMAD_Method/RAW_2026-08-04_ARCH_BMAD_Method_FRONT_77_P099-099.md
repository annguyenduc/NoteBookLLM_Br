# HD SOURCE: ARCH_BMAD_Method_FRONT_77_P099-099
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_77
Part Title: NONE
Chapter Title: NONE
Section Title: Story trong epic vs story sẵn sàng phát triển
Chunk Range: Pages 99 to 99
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

"Sprint planning cung cấp nguồn sựthật duy nhất về tiến độ dự án  -  một nơi để tất cả stakeholders nhìn thấy trạng thái."

## Nội dung sprint-status.yaml

```
project: "Analytics Dashboard" sprint_number: 1 sprint_started: "2024-03-15" epics: - id: epic-1 title: "Xác thực và phân quyền người dùng" status: in_progress stories: - id: story-1-1 title: "Luồng đăng nhập người dùng" status: completed completed_date: "2024-03-16" - id: story-1-2 title: "Làm mới JWT Token" status: in_progress assigned_session: "session-abc123" - id: story-1-3 title: "Đăng xuất và vôhiệu hóa token" status: ready blocked_by: ["story-1-2"] - id: epic-2 title: "Bảng điều khiển dữ liệu" status: not_started stories: - id: story-2-1 title: "Widget hiển thị số liệu" status: not_started
```

## Khởi tạo sprint

Khi chạy bmad-sprint-planning , SM Agent sẽ :

Đọc tất cảfile epics và stories

Hỏi về sprint goals vàưu tiên

Tạo sprint-status.yaml với trạng thái ban đầu của mọi story

Xác nhận đúng thứtựphụthuộc giữa stories

## 8.3 tạo story  giai đoạn chuẩn bị

```
bmad-create-story # Hoặc: bmad-agent-
```

```
dev  → gõ "CS"
```

## Story trong epic vs story sẵn sàng phát triển