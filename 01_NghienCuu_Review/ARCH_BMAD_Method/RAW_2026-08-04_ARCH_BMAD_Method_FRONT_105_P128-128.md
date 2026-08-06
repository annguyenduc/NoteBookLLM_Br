# HD SOURCE: ARCH_BMAD_Method_FRONT_105_P128-128
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_105
Part Title: NONE
Chapter Title: NONE
Section Title: 11.2 vịtrí và quyước đặt tên
Chunk Range: Pages 128 to 128
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## Chương 11: Tùy chỉnh agents  -  hệthống .customize.yaml

## Bạn sẽ học được gì?

Sau khi đọc chương này, bạn sẽ hiểu:

```
Tại sao phải tùy chỉnh qua .customize.yaml thay vì sửa trực tiếp agents Sáu phần (sections) của file customize và cách dùng từng phần Cách thêm custom menu items với prompts tái sử dụng Cách viết critical actions  -  lệnh tự động khi agent khởi động Quy trìnháp dụng thay đổi: Quick Update Troubleshooting các vấn đề thường gặp
```

## 11.1 tại sao .customize.yaml tồn tại?

Đây là câu hỏi đầu tiên hầu hết người dùng đặt ra: Tại sao không thể sửa trực tiếp file agent trong \_bmad/agents/ ?

Câu trả lời từ tài liệu chính thức:

"Luôn dùng các file \_.customize.yaml\_ thay vì sửa agent files trực tiếp. Installer ghi đèagent files khi cập nhật, nhưng bảo toàn các thay đổi \_.customize.yaml\_ của bạn."

Đơn giản hơn: Khi BMad ra phiên bản mới và bạn chạy nâng cấp:

```
_bmad/agents/*.md bị ghi đè hoàn toàn -  mọi thay đổi trực tiếp bịmất _bmad/_config/agents/*.customize.yaml được bảo toàn nguyên vẹn
```

Đây là thiết kếcóchủ đích để bạn cóthểnâng cấp BMad mà không mất tùy chỉnh của mình.

## 11.2 vịtrí và quyước đặt tên

Mỗi agent cómột file .customize.yaml riêng:

```
_bmad/_config/agents/ ├── bmm -pm.customize.yaml           ← Tùy chỉnh PM Agent (Amelia) ├── bmm -architect.customize.yaml    ← Tùy chỉnh Architect Agent (Winston) ├── bmm -dev.customize.yaml          ← Tùy chỉnh Developer Agent (James) ├── bmm -uxdesigner.customize.yaml  ← Tùy chỉnh UX Designer Agent (Pixel) ├── bmm -techwriter.customize.yaml  ← Tùy chỉnh Tech Writer Agent (Sage) ├── bmm -sm.customize.yaml           ← Tùy chỉnh SM Agent └── tea -murat.customize.yaml        ← Tùy chỉnh TEA Agent Murat (nếu cómodule TEA)
```