# HD SOURCE: ARCH_BMAD_Method_FRONT_106_P129-129
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_106
Part Title: NONE
Chapter Title: NONE
Section Title: Quy tắc quan trọng: Appends vs. replaces
Chunk Range: Pages 129 to 129
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

## 11.3 cấu trúc đầy đủ của file .customize.yaml

Dưới đây là cấu trúc hoàn chỉnh với tất cả sáu phần cóthể có:

```
# Tất cả sections là tùy chọn  -  chỉinclude sections bạn muốn thay đổi agent: metadata: name: 'Tên Mới Cho Agent'         # Ghi đè tên mặc định persona:                               # THAY THẾTOÀN BỘpersona  -  phải cótất cả bốn trường role: 'Tiêu đề vai trò' identity: 'Môtảagent làai' communication_style: 'Cách agent giao tiếp' principles: - 'Nguyên tắc 1' - 'Nguyên tắc 2' memories:                              # THÊM VÀO memories hiện có (không thay thế ) - 'Thông tin dự án quan trọng cần nhớ ' -'Quyước hoặc quy tắc cần ghi nhớ ' menu:                                  # THÊM VÀO menu mặc định (không thay thế ) - trigger: 'tên-lệnh' workflow: 'đường/dẫn/đến/workflow.yaml'  # HOẶC action: '#prompt-id' description: 'Môtả lệnh này làm gì' critical_actions:                      # THÊM VÀO actions khởi động (không thay thế ) - 'Kiểm tra CI/CD status khi bắt đầu' - 'Tải sprintstatus.yaml để có bức tranh hiện tại' prompts:                               # Prompts tái sử dụng được tham chiếu từmenu - id: 'id-prompt-cua-toi' content: | Nội dung prompt nhiều dòngở đây. Cóthể bao gồm instructions chi tiết cho agent.
```

## Quy tắc quan trọng: Appends vs. replaces Đây là điểm dễ gây nhầm lẫn nhất:

| Section               | Hành vi                                                            |
|-----------------------|--------------------------------------------------------------------|
| `agent.metadata.name` | **Thay thế ** tênmặc định                                       |
| `persona`             | **Thay thế hoàn toàn** persona - phải cótất cả BỐN trường |
| `memories`            | **Thêm vào** memories hiện cócủa agent                        |
| `menu`                | **Thêm vào** menu mặc định của agent                           |