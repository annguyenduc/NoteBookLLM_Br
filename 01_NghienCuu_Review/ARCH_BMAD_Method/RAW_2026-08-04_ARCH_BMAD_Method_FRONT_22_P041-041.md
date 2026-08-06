# HD SOURCE: ARCH_BMAD_Method_FRONT_22_P041-041
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_22
Part Title: NONE
Chapter Title: NONE
Section Title: Tóm tắt chương 2
Chunk Range: Pages 41 to 41
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## Bài tập 3  -  Tạo projectcontext.md đơn giản:

Tạo file \_bmad-output/project-context.md với nội dung đơn giản môtả tech stack của một dự án bạn đang làm. Ít nhất hai phần: Tech Stack và ba quy tắc quan trọng nhất của dự án.

## Tóm tắt chương 2

Hai thưmục chính: \_bmad/ (framework, không được sửa trực tiếp) và \_bmad-output/ (tài liệu dự án, do bạn vàagent cùng tạo) Bốn khái niệm nền tảng: Agent = Nhân vật AI chuyên biệt với vai trò, chuyên môn, và phong cách riêng Skill = Lệnh bạn gõ để tương tác với framework (prefix bmad-* ) Workflow = Quy trình cócấu trúc, tuần tựtừng bước với tài liệu đầu ra định sẵn Task = Đơn vịcông việc nhỏ được điều phối bên trong workflow, ít khi tương tác trực tiếp Nguyên tắc Fresh Chat = Mỗi workflow chạy trong cuộc hội thoại mới  -  tránhônhiễm context `project-context.md` = "Điều lệ" được đọc bởi 8 workflows  nơi duy nhất để định nghĩa quyước và quy tắc toàn dự án Quy tắc vàng: KHÔNG bao giờ sửa \_bmad/ trực tiếp  -  MỌI tùy chỉnh đều phải qua .customize.yaml files trong \_bmad/\_config/agents/ Tên file quan trọng: ux-spec.md (không phải ux-design.md )