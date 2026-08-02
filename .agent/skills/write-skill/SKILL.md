---
name: write-skill
description: "Tạo, chỉnh sửa hoặc nâng cấp file SKILL.md. Kích hoạt khi nhận yêu cầu tạo/sửa/upgrade skill hoặc nhận phản hồi về skill. KHÔNG dùng cho chỉnh sửa wiki thông thường."
---

# Viết Skill

## Khi Nào Dùng
- Tạo skill mới từ đầu
- Chỉnh sửa hoặc nâng cấp SKILL.md hiện có
- Nhận phản hồi/feedback về một skill và cần cập nhật

## Cấu Trúc SKILL.md Chuẩn

```yaml
---
name: tên-skill-tiếng-anh
description: "Mô tả ngắn bằng tiếng Việt — WHEN nào dùng skill này (trigger), không phải mô tả quy trình."
---
```

**Phần body (Markdown):**
- Hướng dẫn chi tiết bằng tiếng Việt
- Quy trình từng bước rõ ràng
- Ví dụ cụ thể nếu cần
- Lỗi phổ biến cần tránh

## Nguyên Tắc Viết Skill Tốt

### Description — Viết đúng
- Mô tả KHI NÀO dùng (trigger), không mô tả QUÁ TRÌNH
- Tối đa 1-2 câu
- ❌ Sai: "Skill này thực hiện việc A, B, C..."
- ✅ Đúng: "Dùng khi cần làm X trước khi làm Y"

### Body — Quy tắc cốt lõi
- Không ẩn safety rules trong ví dụ
- Không dùng link `@file` trong prose — dùng relative path thuần
- Không tóm tắt toàn bộ workflow trong `description`
- Không hardcode absolute path — dùng relative path và forward slash
- Không viết lại skill theo batch mà không kiểm tra từng thư mục

### Tổ Chức Thư Mục
```
.agent/skills/tên-skill/
  SKILL.md          ← file chính (bắt buộc)
  scripts/          ← script hỗ trợ (tùy chọn)
  examples/         ← ví dụ tham chiếu (tùy chọn)
  resources/        ← file template, asset (tùy chọn)
  references/       ← tài liệu bổ sung dài (tùy chọn)
```

## Lưu Ý Quan Trọng
> Mọi skill mới phải tạo trong `.agent/skills/`. Thư mục `.codex/skills/` là Directory Junction trỏ thẳng vào `.agent/skills/` — tự động đồng bộ.
> Nếu junction bị hỏng: `New-Item -ItemType Junction -Path .codex/skills -Value .agent/skills`

## Lỗi Phổ Biến
- `description` mô tả quy trình thay vì trigger → viết lại tập trung vào when/why
- SKILL.md hứa hẹn hành vi chỉ tồn tại trong script đã xóa/thiếu
- Hardcode absolute path cho một máy/OS cụ thể
- Body sao chép nguyên tài liệu tham chiếu dài thay vì link đến nó