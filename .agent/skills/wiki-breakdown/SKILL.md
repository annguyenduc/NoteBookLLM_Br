# SKILL: wiki-breakdown

Phát hiện lỗ hổng tri thức (Knowledge Gaps) bằng cách trích xuất danh từ chưa được định nghĩa và tạo các Stubs.

## Context (Bối cảnh)
Trong quá trình nạp dữ liệu (Ingest), nhiều khái niệm mới được nhắc tới nhưng chưa có trang Atoms tương ứng. `wiki-breakdown` giúp tự động hóa việc phát hiện các "Gap" này để lập kế hoạch nghiên cứu tiếp theo.

## Workflow (Quy trình)

### Bước 1: Noun Mining (Khai thác danh từ)
Chạy script `noun_miner.py` để quét toàn bộ Wiki.
```bash
python .agent/skills/wiki-breakdown/scripts/noun_miner.py
```
Script sẽ tìm kiếm các từ khóa được viết hoa hoặc bọc trong `[[ ]]` mà chưa có file tương ứng trong `concepts/` hoặc `entities/`.

### Bước 2: Gap Analysis
Dựa trên kết quả trả về, phân loại các "Gap":
- **Critical Gap**: Được nhắc tới nhiều lần (> 5 lần).
- **Secondary Gap**: Chỉ xuất hiện 1-2 lần.

### Bước 3: Stub Creation
Tạo các file Atom tạm thời (Stub) với metadata cơ bản để đánh dấu sự tồn tại của khái niệm.

## Keywords
- **gap**: Lỗ hổng tri thức cần lấp đầy.
- **stub**: Trang Atom sơ khởi chưa có nội dung chi tiết.
- **noun**: Đối tượng khai thác chính (Danh từ).
- **breakdown**: Quy trình phân rã tri thức từ raw source.

## Constraints
- Không tự ý tạo Atom mà không có nguồn tham chiếu rõ ràng.
- Mọi Gap phát hiện được phải được lưu vào `review_queue` để User phê duyệt.
