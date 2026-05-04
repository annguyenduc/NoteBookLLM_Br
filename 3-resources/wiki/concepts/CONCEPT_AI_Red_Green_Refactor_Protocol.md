    ---
file_id: "CONCEPT_AI_Red_Green_Refactor_Protocol"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
---

# CONCEPT: AI Red-Green-Refactor Protocol

## Core Principle
**Red-Green-Refactor (RGR)** là giao thức bắt buộc trong phát triển phần mềm dựa trên AI, đảm bảo mọi thay đổi code đều được xác minh bởi bằng chứng thực thi. Nguyên tắc cốt lõi: **Không có code nào được viết ra nếu không có một test case đang thất bại trước đó.**

## Quy trình 3 bước (Theo Superpowers)
1.  **RED**: Viết một bài kiểm tra (test) cho tính năng/bug. Chạy test và xác nhận nó **THẤT BẠI** (với lý do mong muốn).
2.  **GREEN**: Viết lượng code tối thiểu cần thiết để làm cho bài kiểm tra đó **VƯỢT QUA**. Không viết dư thừa (YAGNI).
3.  **REFACTOR**: Làm sạch code, tối ưu cấu trúc nhưng vẫn đảm bảo test tiếp tục **VƯỢT QUA**.

## Ví dụ đối chiếu (Rule 17)
- **Ví dụ thực tế (Original)**: Khi thêm hàm `calculate_tax`. Đầu tiên viết test `test_calculate_tax` truyền vào 100$, mong đợi 10$. Test báo lỗi `NameError` (hàm chưa tồn tại) -> **RED**. Sau đó định nghĩa hàm trả về `10` -> **GREEN**. Cuối cùng sửa hàm thành logic chuẩn `price * 0.1` -> **REFACTOR**.
- **Ẩn dụ sư phạm (Pedagogical)**: Giống như việc đóng cọc trước khi leo núi. Bạn không bao giờ tiến lên bước tiếp theo nếu cái cọc bảo hiểm (test) chưa được đóng chắc chắn vào vách đá.

## 4F Reflection
- **Facts**: Giao thức này giúp triệt tiêu hiện trạng AI "code bừa" và hy vọng nó chạy.
- **Feelings**: Đôi khi cảm thấy chậm hơn ban đầu, nhưng cực kỳ an tâm khi codebase lớn dần mà không bị "vỡ".
- **Findings**: Việc quan trọng nhất là bước **RED**. Nếu test không fail lúc đầu, bạn không thể chắc chắn test đó đang kiểm tra đúng thứ cần thiết.
- **Futures**: Áp dụng triệt để cho việc viết Skills (`write-skill`). Skill chỉ được coi là hoàn thiện nếu nó vượt qua bài test "áp lực" (pressure test).

Nguồn: [SOURCE_SUPERPOWERS_README](file:///d:/NoteBookLLM_Br/3-resources/wiki/sources/SOURCE_SUPERPOWERS_README.md) — Section: test-driven-development
