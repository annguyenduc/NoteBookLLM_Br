---
description: Kích hoạt quy trình chưng cất tri thức tự động (Distillation Pipeline)
---

Lệnh `/distill` điều phối Biệt đội Agent thực hiện chưng cất dữ liệu từ các volume thô thành Knowledge Items.

### Các bước thực hiện:

1. **@pm** kiểm tra trạng thái trong `CONTINUITY.md` và lập kế hoạch đợt chưng cất mới.
2. **@devops** chạy lệnh bộ châm (Rule 7) để đảm bảo không có vi phạm cấu trúc:
// turbo
python scripts/maint/check_depth.py
3. **@scout** (Researcher) thực hiện lệnh chưng cất chính:
// turbo
python tools/pipeline/atomic_distiller.py
4. **@librarian** (Reviewer) sử dụng `cm-quality-gate` để kiểm tra các file mới tạo trong `brain/distilled/` và cập nhật liên kết.
5. **@pm** cập nhật tiến độ vào `task.md`.

> [!TIP]
> Sử dụng `/distill` khi bạn có các file markdown thô mới cần được "chắt lọc" thành tri thức có cấu trúc.
