# HD SOURCE: ARCH_BMAD_Method_FRONT_108_P131-131
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_108
Part Title: NONE
Chapter Title: NONE
Section Title: Dùng inline prompt
Chunk Range: Pages 131 to 131
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## 11.6 section: Memories  -  thêm thông tin bền vững

Memories lànhững thông tin agent "nhớ " từ đầu mỗi session  -  không cần nhắc lại mỗi lần.

```
memories: - 'Dự án: Analytics Dashboard cho E-commerce' - 'Tech stack: React 18.2, Node.js 20 LTS, PostgreSQL 16, TypeScript strict mode' -'Người lãnh đạo kỹ thuật: Nguyễn Văn An' - 'Deadline: Sprint 4 phải hoàn thành trước 30/05/2024' - 'Nguyên tắc: Luônưu tiên mobile -first khi cóconflict vềUX' - 'Quy tắc nhóm: Không có hotfix trực tiếp lên production  -  mọi thứ qua PR' - 'API third-party chính: Stripe (payment), SendGrid (email), Cloudinary (images)'
```

## Trường hợp tốt nhất để dùng Memories:

Thông tin bối cảnh dự án thường xuyên cần thiết

Team agreements và quy tắc quan trọng

Thông tin về stakeholders

Giới hạn và ràng buộc dự án

Lưuý: Memories kết hợp với project-context.md . Project context cho thông tin kỹ thuật chi tiết; memories cho thông tin ngữ cảnh dự ánởmức cao hơn.

## 11.7 section: Menu  -  thêm custom commands

Menu items cho phép bạn tạo các lệnh tắt tùy chỉnh cho agent.

## Dùng workflow từfile YAML

```
menu: - trigger: 'audit-security' workflow: '_bmad/workflows/security-audit.yaml' description: 'Chạy security audit đầy đủ theo checklist của team' - trigger: 'ci-status' workflow: '_bmad/workflows/check-ci.yaml' description: 'Kiểm tra trạng thái CI/CD pipeline hiện tại'
```

## Dùng inline prompt

```
menu: - trigger: 'onboard-review' action: '#onboarding-review-prompt' description: 'Review code theo onboarding checklist cho junior developers'
```