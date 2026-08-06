# HD SOURCE: ARCH_BMAD_Method_FRONT_16_P034-034
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_16
Part Title: NONE
Chapter Title: NONE
Section Title: Khái niệm 3: Workflow
Chunk Range: Pages 34 to 34
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

| Tech Writer Agent   | Sage   | Technical Writer - tập trung vào tài liệu rõ ràng và cóthể sử dụng được     |
|---------------------|--------|--------------------------------------------------------------------------------------|
| TEA Agent           | Murat  | Master Test Architect - tập trung vào chiến lược kiểmthử cấp doanh nghiệp |

Mỗi agent respond in character -  Amelia sẽ luônưu tiên giátrịngười dùng và business outcome, Winston sẽ luôn cẩn thận về scalability và clean architecture, James sẽ luôn xem xét technical debt và độphức tạp.

Khi bạn gọi agent bằng skill command (ví dụ bmad-agent-pm ), bạn đang khởi động một cuộc hội thoại với Amelia  -  một PM có định hướng và phong cách riêng.

## Khái niệm 2: Skill

Skill là điểm vào để tương tác với một workflow hoặc agent cụthể .

Skill cóprefix bmad-* . Có hai loại skill:

Workflow Skill -  Khởi chạy một workflow cócấu trúc. Ví dụ :

bmad-create-prd -  Khởi chạy workflow tạo PRD với PM Agent

bmad-create-architecture -  Khởi chạy workflow tạo architecture với Architect Agent bmad-brainstorming -  Khởi chạy phiên động não sáng tạo

Agent Skill -  Kích hoạt một agent để làm việc trực tiếp trong menu-driven mode. Ví dụ :

bmad-agent-pm -  Khởi động PM Agent v

bmad-agent-architect -  Khởi độ bmad-agent-dev -  Khởi độ

```
ới menu đầy đủng Architect Agent ng Developer Agent
```

Sự khác biệt thực tế : Workflow Skill chạy một quy trình cụthể từ đầu đến cuối. Agent Skill khởi động agentở chế độtương tác, bạn cóthể chọn làm gì tiếp theo từmenu.

## Khái niệm 3: Workflow

Workflow làmột quy trình cócấu trúc, tuần tựtừng bước, với các checkpoint rõ ràng và tài liệu đầu ra được xác định trước.

Ví dụ về bmad-create-prd workflow: