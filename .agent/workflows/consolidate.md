---
description: Kích hoạt quy trình tổng hợp tri thức (Consolidation Pipeline)
---

Lệnh `/consolidate` thực hiện gom nhóm và tối ưu hóa các Knowledge Item đã chưng cất thành một tài liệu tri thức tập trung.

### Các bước thực hiện:

1. **@pm** lọc danh sách các Knowledge Item mới trong `brain/distilled/`.
2. **@devops** chạy lệnh kiểm toán độ sâu thư mục (Rule 7):
// turbo
python scripts/maint/check_depth.py
3. **@engineer** thực hiện lệnh tổng hợp Map-Reduce:
// turbo
python tools/pipeline/consolidator.py
4. **@librarian** (Reviewer) kiểm tra tính hợp lệ của file `brain/optimized_context.md`.
5. **@pm** báo cáo tỉ lệ nén và chất lượng cho người dùng.

> [!IMPORTANT]
> Nên chạy `/consolidate` sau mỗi đợt `/distill` lớn để giữ cho ngữ cảnh dự án luôn được tối ưu.
