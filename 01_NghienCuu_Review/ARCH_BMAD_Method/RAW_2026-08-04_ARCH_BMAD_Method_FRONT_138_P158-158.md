# HD SOURCE: ARCH_BMAD_Method_FRONT_138_P158-158
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_138
Part Title: NONE
Chapter Title: NONE
Section Title: 14.3 creative intelligence suite - bảy agents sáng tạo
Chunk Range: Pages 158 to 158
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

Team cần agent chuyên biệt không cótrong cài đặt mặc định (Legal Review Agent, Data Science Agent, DevOps Specialist) Quy trình nội bộcủa công ty cần được encode thành workflow tái sử dụng Muốn chia sẻagents vàworkflows với cộng đồng BMad Muốn publish module lên npm đểngười khác cài được

## Ba thành phần của BMad builder

## Thành phần 1  -  Tạo Agent (Agent Builder):

Quy trình hướng dẫn để tạo agent chuyên biệt: Định nghĩa: vai trò, chuyên môn, phong cách giao tiếp, quyền truy cập công cụ , menu items Cấu hình: custom prompts, startup actions, memories Đầu ra: Agent files sẵn sàng để cài đặt Ví dụuse case: Tạo "Legal Compliance Agent" với kiến thức sâu về GDPR, HIPAA, và các quy định trong lĩnh vực cụthể của công ty bạn. Agent này sẽ review tất cả code xử lý dữ liệu cánhân theo góc nhìn compliance, thứmà Developer Agent thông thường không cóchuyên môn để làm.

## Thành phần 2  -  Tạo Workflow (Workflow Builder):

Thiết kế quy trình cócấu trúc: Định nghĩa: chuỗi bước, các điểm decision, checkpoints Cấu hình: nhánh điều kiện, retry logic, validation gates Đầu ra: Workflow YAML files tương thích với BMad Ví dụuse case: Tạo workflow "Client Onboarding Sprint" riêng cho công ty của bạn  -  thu thập requirements theo cách riêng, cócustom checkpoints phù hợp với quy trình phêduyệt nội bộ .

## Thành phần 3  -  Tạo Module (Module Builder):

Đóng gói agents vàworkflows thành module cóthể publish: Bao gồm: Installation configuration, dependency declarations Hỗ trợ: YAML configuration tương tác + npm publishing support Đầu ra: Module hoàn chỉnh sẵn sàng để cài bằng npx bmad-method install

## 14.3 creative intelligence suite  -  bảy agents sáng tạo