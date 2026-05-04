# SKILL: wiki-status

Báo cáo sức khỏe hệ thống thông qua Health Dashboard và các chỉ số tri thức.

## Context (Bối cảnh)
Để duy trì một Wiki bền vững, User cần biết hệ thống đang phát triển như thế nào. `wiki-status` cung cấp các số liệu thống kê về tính kết nối và mức độ tin cậy của tri thức.

## Workflow (Quy trình)

### Bước 1: Dashboard Overview
Báo cáo tổng quan về số lượng Atoms theo trạng thái:
- **verified**: Số lượng Atom đã được kiểm định.
- **draft**: Số lượng Atom mới nạp chưa qua hòa giải.
- **synthesized**: Số lượng tri thức đã được tổng hợp bởi Human.

### Bước 2: Link Density Analysis
Tính toán chỉ số **density** (Mật độ liên kết).
- LDI = Tổng số Edges / Tổng số Atoms.
- Mục tiêu: LDI > 2.0 để đảm bảo mạng lưới tri thức không bị rời rạc.

### Bước 3: Error Rate Tracking
Theo dõi số lượng lỗi phát hiện bởi `wiki-cleanup` trong các phiên làm việc gần nhất.

## Keywords
- **density**: Mật độ liên kết đồ thị.
- **verified**: Trạng thái tri thức đã được xác thực.
- **draft**: Trạng thái tri thức thô.
- **dashboard**: Bảng điều khiển sức khỏe Wiki.

## Constraints
- Báo cáo phải được tạo ra dựa trên dữ liệu thực tế từ `wiki_brain.db`.
- Không được làm giả số liệu (Rule 2).
