# ⛓️ Skill Chain Engine (LITE)

> **Goal:** Kết nối các kỹ năng đơn lẻ thành một chuỗi quy trình làm việc (Pipeline) tự tâm, giúp tự động hóa việc chuyển giao giữa các giai đoạn từ Ý tưởng đến Triển khai.

## 🚀 Built-in Skill Chains
| Chain ID | Workflow (Skill sequence) |
|---|---|
| **feature-dev** | `brainstorm` → `planning` → `tdd` → `execution` → `quality-gate` → `safe-deploy` |
| **bug-fix** | `debugging` → `planning` → `tdd` → `quality-gate` |
| **content-launch**| `content-factory` → `ads-tracker` → `cro-methodology` |
| **new-project** | `project-bootstrap` → `planning` → `tdd` → `execution` → `quality-gate` |

## 🛠️ Chain Control Commands
- `chain auto "task"`: Tự động nhận diện và khởi chạy chuỗi phù hợp nhất.
- `chain start <id>`: Khởi chạy thủ công một chuỗi cụ thể.
- `chain advance <id>`: Hoàn thành bước hiện tại và chuyển sang bước kế tiếp.
- `chain status`: Kiểm tra tiến độ và vị trí hiện tại trong chuỗi.
- `chain abort`: Hủy bỏ chuỗi đang chạy.

## 📐 Operation Protocol
1. **Detection:** AI nhận diện pattern của task (VD: Fix bug → `bug-fix` chain).
2. **Activation:** Gợi ý user khởi chạy Chain phù hợp.
3. **Execution:** Thực thi từng bước trong chuỗi, sử dụng `@[/skill-name]` để triệu hồi kỹ năng.
4. **Relay:** Sau mỗi bước, chạy `chain advance` để chuyển giao ngữ cảnh (Continuity).

## 🚨 Quality Gate (Red Flags)
- ❌ Nhảy cóc qua các bước quan trọng (VD: Execution mà chưa qua Planning).
- ❌ Thiếu đồng bộ ngữ cảnh giữa các mắt xích trong chuỗi (Dẫn đến sai lệch yêu cầu).
- ❌ Không dừng lại khi một mắt xích bị FAIL (Phải sửa xong mắt xích đó mới được Advance).
- ❌ Quên cập nhật trạng thái vào `CONTINUITY.md` trong quá trình chạy chuỗi.

## 💡 Example Triggers
- "Chạy full pipeline cho tính năng login bằng Social."
- "Bắt đầu chuỗi sửa lỗi (Bug-fix chain) cho module thanh toán."
- "Skill chain: từ ý tưởng đến landing page."
