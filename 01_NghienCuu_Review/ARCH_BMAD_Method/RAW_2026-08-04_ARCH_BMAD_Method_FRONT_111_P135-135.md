# HD SOURCE: ARCH_BMAD_Method_FRONT_111_P135-135
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_111
Part Title: NONE
Chapter Title: NONE
Section Title: Thực hành ngay
Chunk Range: Pages 135 to 135
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

```
# Phải có đủ bốn: persona: role: '...'               # Không được thiếu identity: '...'           # Không được thiếu communication_style: '...' # Không được thiếu principles:               # Không được thiếu - '...'
```

## Lỗi: Menu item không kích hoạt

Kiểm tra trường trigger -  phải khớp chính xác với những gì bạn gõ. Khoảng cách thừa hoặc dấu gạch ngang thay vì gạch dưới lànguyên nhân phổ biến.

## Lỗi YAML syntax

YAML rất nhạy cảm với:

```
Indentation: Phải dùng spaces, không phải tabs. Hai spaces mỗi level Dấu cách sau dấu hai chấm: key: value không phải key:value Dấu nháy: Chuỗi có kýtự đặc biệt phải trong nháy đơn '...' hoặc nháy kép "..." Dấu gạch đầu dòng: List items phải có -(gạch đầu dòng + space)
```

Dùng một công cụ validate YAML trực tuyến để kiểm tra trước khiáp dụng.

## Thực hành ngay

## Bài tập  -  Tùy Chỉnh PM Agent Thực Tế :

Mởfile \_bmad/\_config/agents/bmm-pm.customize.yaml và thêm:

```
memories: - 'Dự án hiện tại: [Tên dự án của bạn]' - 'Mục tiêu Q2: [Mục tiêu quan trọng nhất]' -'Ưu tiên cao nhất từ stakeholders: [Tính năng hoặc nhu cầu quan trọng nhất]' menu: - trigger: 'week-review' action: '#weekly-review' description: 'Tổng kết tuần và lập kế hoạch tuần tới' prompts: - id: 'weekly-review' content: | Thực hiện tổng kết tuần ngắn gọn theo format: **Đã hoàn thành:** - [Liệt kêtừ sprint-status.yaml] **Đang tiến hành:** -[Stories đang trong progress] **Blocked:** - [Những gì bịchặn và tại sao] **Kế hoạch tuần tới:**
```