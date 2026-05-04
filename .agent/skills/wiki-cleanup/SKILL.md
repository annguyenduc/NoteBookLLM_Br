# SKILL: wiki-cleanup

Bảo trì và kiểm định chất lượng hệ thống Wiki thông qua bài kiểm tra Steve Jobs và quy trình Linting.

## Context (Bối cảnh)
Một Wiki chất lượng cao không cho phép sự tồn tại của các liên kết hỏng, thông tin cũ (stale) hoặc các Atom thiếu cấu trúc. `wiki-cleanup` là công cụ đảm bảo tính nhất quán và sự hoàn hảo của tri thức.

## Workflow (Quy trình)

### Bước 1: Quality Linting (Kiểm định chất lượng)
Chạy script `lint_engine.py` để phát hiện lỗi.
```bash
python .agent/skills/wiki-cleanup/scripts/lint_engine.py
```
Script sẽ kiểm tra:
- **broken link**: Các liên kết `[[ ]]` không tồn tại.
- **stale**: Các file chưa được cập nhật trong 30 ngày.
- **lint**: Các lỗi định dạng Markdown.

### Bước 2: The Steve Jobs Test
Áp dụng tư duy "Simple and Perfect". Mọi Atom phát hiện có lỗi sẽ được gắn nhãn `human_review_flag` để User phê duyệt lại. Nếu một khái niệm quá phức tạp, cần thực hiện **Refactor** để đơn giản hóa.

### Bước 3: Automatic Healing
Sửa lỗi tự động đối với các lỗi nhỏ như:
- Tự động xóa trailing whitespace.
- Chuẩn hóa Metadata header.

## Keywords
- **broken link**: Liên kết nội bộ bị hỏng.
- **stale**: Nội dung đã cũ hoặc không còn chính xác.
- **lint**: Quy trình kiểm tra lỗi tự động.
- **Steve Jobs**: Tiêu chuẩn vàng về chất lượng và sự đơn giản.

## Constraints
- Tuyệt đối không xóa file trong raw/.
- Mọi thay đổi nội dung tự động phải được ghi vào `3-resources/wiki/log.md`.
