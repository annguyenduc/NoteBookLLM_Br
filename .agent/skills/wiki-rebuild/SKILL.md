# SKILL: wiki-rebuild

Đồng bộ hóa hạ tầng tri thức, cập nhật file chỉ mục (Index) và hệ thống liên kết ngược (Backlinks).

## Context (Bối cảnh)
Khi số lượng Atoms lớn, việc tìm kiếm thủ công trở nên khó khăn. `wiki-rebuild` giúp duy trì một bản đồ tri thức sống động, đảm bảo mọi Atom đều có thể được truy vết từ Index hoặc từ các liên kết ngược.

## Workflow (Quy trình)

### Bước 1: Structural Sync (Đồng bộ cấu trúc)
Chạy script `rebuild.py` để đồng bộ hóa trạng thái giữa file hệ thống và Database.
```bash
python .agent/skills/wiki-rebuild/scripts/rebuild.py
```
Quy trình này thường được thiết lập chạy **nightly** (hàng đêm) để đảm bảo dữ liệu luôn tươi mới.

### Bước 2: Index Generation
Tự động tạo hoặc cập nhật file `index.md` tại `3-resources/wiki/index.md`. File này phân loại Atoms theo các nhóm: Concepts, Entities, Sources, Synthesis.

### Bước 3: Backlinks Injection
Sử dụng `indexer.py` để quét các cạnh `edges` và tiêm (inject) danh sách các file đang trỏ tới Atom hiện tại vào section `_backlinks` ở cuối file.

## Keywords
- **index.md**: File chỉ mục trung tâm của hệ thống Wiki.
- **_backlinks**: Danh sách các liên kết ngược giúp truy vết quan hệ.
- **sync**: Quy trình đồng bộ hóa giữa File System và DB.
- **nightly**: Tần suất thực thi lý tưởng để bảo trì hệ thống.

## Constraints
- Không làm thay đổi nội dung chính của Atom khi tiêm Backlinks.
- Luôn kiểm tra tính toàn vẹn của Database trước khi thực hiện **sync**.
