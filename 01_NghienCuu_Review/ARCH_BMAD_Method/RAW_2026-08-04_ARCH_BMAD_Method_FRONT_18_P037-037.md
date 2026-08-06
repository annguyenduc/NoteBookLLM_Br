# HD SOURCE: ARCH_BMAD_Method_FRONT_18_P037-037
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_18
Part Title: NONE
Chapter Title: NONE
Section Title: Nội dung chuẩn
Chunk Range: Pages 37 to 37
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

Ýnghĩa thực tế : Đây là tập hợp các quy tắc và quyước màmọi agent đều phải tuân theo, trong mọi session, trong suốt toàn bộ dự án.

## Tại sao gọi là "điều lệ "?

Không cóproject-context.md , mỗi session bắt đầu từzero: Developer Agent trong Session 1 cóthể dùng camelCase cho biến số Developer Agent trong Session 2 (cùng dự án nhưng fresh chat) cóthể dùng snake\_case Developer Agent trong Session 3 cóthể dùng PascalCase Kết quả : Codebase không nhất quán, khómaintain, khó đọc. Với project-context.md , mọi agent trong mọi session đều biết: "Dự án này dùng TypeScript strict mode. Biến sốcamelCase. Database columns snake\_case. Không bao giờ dùng fetch() trực tiếp, luôn dùng apiClient singleton."

## Được load bởi 8 workflows khác nhau

## Đây là danh sách đầy đủ các workflows tự động tìm và đọc project-context.md :

bmad-create-architecture -để tôn trọng các quyước kỹ thuật khi thiết kế bmad-create-story -để story cócontext đầy đủ về dự án bmad-dev-story -để code được sinh ra nhất quán với phần còn lại bmad-code-review -để review dựa trên đúng tiêu chuẩn của dự án bmad-quick-dev -để áp dụng đúng mẫu thiết kế khi implement bmad-sprint-planning -để có bối cảnh toàn dự án khi lập kế hoạch bmad-retrospective -để có bối cảnh khi tổng kết bài học bmad-correct-course -đểnhận thức đầy đủ khi xử lýthay đổi

## Vịtrífile

BMad tìm project-context.md theo thứtựưu tiên: Đường dẫn chính: \_bmad-output/project-context.md Fallback: Bất kỳfile nào khớp với **/project-context.md trong project

## Nội dung chuẩn

File này có hai phần chính:

## Phần 1  -  Tech Stack và Phiên Bản: