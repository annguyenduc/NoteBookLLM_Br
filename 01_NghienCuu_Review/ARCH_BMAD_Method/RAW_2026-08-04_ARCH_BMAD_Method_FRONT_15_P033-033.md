# HD SOURCE: ARCH_BMAD_Method_FRONT_15_P033-033
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_15
Part Title: NONE
Chapter Title: NONE
Section Title: Khái niệm 1: Agent
Chunk Range: Pages 33 to 33
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

Quan trọng nhất: Không bao giờ sửa trực tiếp bất cứfile nào trong \_bmad/ . Mọi thay đổi đều sẽ bịmất khi nâng cấp. Thay vào đó, hãy dùng các file .customize.yaml trong \_bmad/\_config/agents/ -  những file này được bảo toàn qua tất cả các lần nâng cấp.

Thưmục `\_bmad-output/` lànơi bạn và các agent cùng nhau tạo ra tài liệu dự án. Thêm vào .gitignore hoặc không  -  tùy quyết định của team. Nhiều team lưu vào version control để có lịch sử và cóthể xem lại các quyết định.

Thưmục `.claude/commands/` (hoặc .cursor/rules/ ) lànơi các skill files được cài đặt, đểIDE nhận điện và cho phép bạn gọi chúng bằng lệnh hoặc slash command.

## 2.3 bốn khái niệm nền tảng

BMad được xây dựng trên bốn khái niệm cốt lõi. Hiểu chính xác sự khác biệt giữa chúng sẽ giúp bạn dùng BMad đúng cách và không bịnhầm lẫn khi đọc tài liệu.

## Khái niệm 1: Agent

Agent làmột nhân vật AI chuyên biệt với vai trò, chuyên môn, phong cách giao tiếp, và tập kỹnăng riêng.

Nghĩ vềagent nhưcác thành viên trong đội dự án thực sự :

| Agent             | Tên nhân vật   | Vai trò và chuyên môn                                                                    |
|-------------------|------------------|------------------------------------------------------------------------------------------|
| PM Agent          | Amelia           | Product Manager - tập trung vào giátrịngười dùng vàmục tiêu kinh doanh          |
| Architect Agent   | Winston          | Software Architect - tập trung vào tính nhất quán kỹ thuật và khảnăng mở rộng |
| Developer Agent   | James            | Senior Developer - tập trung vào implement sạch sẽ , test đầy đủ                    |
| UX Designer Agent | Pixel            | UX Designer - tập trung vào trải nghiệm người dùng và luồng tương tác             |