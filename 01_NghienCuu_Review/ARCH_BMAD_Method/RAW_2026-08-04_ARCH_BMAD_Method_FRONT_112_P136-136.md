# HD SOURCE: ARCH_BMAD_Method_FRONT_112_P136-136
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_112
Part Title: NONE
Chapter Title: NONE
Section Title: Tóm tắt chương 11
Chunk Range: Pages 136 to 136
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

```
-[Ưu tiên top 3] Cuối cùng: Đâu làmột điều cần giải quyết trước tiên để team tăng tốc?
```

Sau đó: npx bmad-method install → Quick Update → Test bằng cách gõweek-review trong agent session.

## Tóm tắt chương 11

Quy tắc vàng: Chỉ tùy chỉnh qua .customize.yaml -  không bao giờ sửa trực tiếp \_bmad/agents/ Vịtrífiles: \_bmad/\_config/agents/{module}-{agent}.customize.yaml Sáu sections: metadata (thay thế ), persona (thay thế ), memories (thêm vào), menu (thêm vào), critical\_actions (thêm vào), prompts (định nghĩa mới) Persona: Phải có đủ BỐN trường: role, identity, communication\_style, principles Memories: Thông tin bền vững qua mọi session  -  không cần nhắc lại mỗi lần Menu + Prompts: Tạo custom commands tái sử dụng  action: '#prompt-id' tham chiếu section prompts Critical actions: Chạy tự động khi khởi động  -  chuẩn hóa startup behaviorÁp dụng: npx bmad-method install → chọn Quick Update sau mỗi lần sửa ng persona, Quick

Troubleshooting: YAML syntax (spaces, colons, dashes), bốn trườUpdate sau khi sửa