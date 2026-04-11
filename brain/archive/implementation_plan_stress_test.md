# Implementation Plan: Stress Test Multi-Model Swarm

Kế hoạch này thực hiện quy trình "Stress Test" để xác minh khả năng điều phối nhiều model (Flash & Pro/Sonnet) của Biệt đội Agent, đồng thời đảm bảo mọi kế hoạch được lưu vết vật lý trên ổ đĩa.

## User Review Required

> [!IMPORTANT]
> - Hệ thống sẽ thực hiện 02 lượt gọi API liên tiếp với 02 model khác nhau.
> - Kết quả đối soát sẽ được ghi trực tiếp vào `brain/log.md`.
> - Kế hoạch này giúp xác minh Budget và tính ổn định của Gateway 4000.

## Proposed Changes

### [NEW] `implementation_plan_stress_test.md` (Tệp này)
Lưu vết kế hoạch thực hiện để User có thể Audit vật lý.

### [NEW] `task_stress_test.md`
Theo dõi tiến độ thực hiện của các Agent trong đợt Stress Test.

## Phase 1: Research & Speed Audit (@scout)
- Sử dụng **Gemini 2.0 Flash**.
- Quét nhanh 05 tệp đề thi AI bất kỳ trong `brain/distilled/`.
- Phân tích số lượng câu hỏi và kiểu dữ liệu.

## Phase 2: Cognitive Depth Audit (@designer/@engineer)
- Sử dụng **Claude 3.5 Sonnet** (hoặc model Pro tương đương).
- Phân tích sâu 01 tệp đề thi từ Phase 1.
- Tìm kiếm các lỗi logic sư phạm mà bản Flash không phát hiện được.

## Phase 3: Final Consolidation & Log
- Ghi kết quả so sánh vào `brain/log.md`.
- Báo cáo Budget tiêu tốn.

## Verification Plan
- Kiểm tra file `brain/log.md` có nội dung mới.
- Kiểm tra log của Gateway 4000 để xác nhận model đã được chuyển đổi thành công.
