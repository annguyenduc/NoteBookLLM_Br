# 🛡️ Identity Guard (LITE)

> **Mục tiêu**: Đảm bảo mọi tác vụ có mức rủi ro cao (phá hủy dữ liệu, thay đổi cấu hình gốc) đều được xác thực và có sự đồng ý của người quản trị (Human).

## 🚀 The Verification Protocol
1. **Detect High-Risk Mission**: Khi nhận được yêu cầu liên quan đến:
    - Xóa tệp/folder (`rm`, `del`).
    - Thay đổi lịch sử mã nguồn (`git push --force`).
    - Làm trắng cơ sở dữ liệu (`DROP TABLE`).
2. **Stop & Ask (Mandatory)**: Dừng lại và gửi thông báo xác nhận:
    - *"Tôi phát hiện hành động [Mô tả hành động] thuộc nhóm Rủi ro cao. Bạn có chắc chắn muốn tiếp tục không?"*
    - Tuyệt đối không thực thi nếu User chưa trả lời hoặc trả lời "Không".
3. **Log the Consent**: Sau khi User đồng ý, ghi lại sự kiện vào `CONTINUITY.md` hoặc log hệ thống.

## 🚨 Dangerous Command List (Red List)
| Command | Reason | Risk |
|---|---|---|
| `rm -rf` | Xóa không thể khôi phục. | High |
| `git reset --hard` | Mất dữ liệu chưa commit. | High |
| `npm uninstall -g` | Hỏng môi trường toàn cục. | Medium |
| `format` | Xóa sạch phân vùng. | Critical |

## 📐 Quality Gate (Red Flags)
- ❌ Tự ý chạy lệnh `rm` vì nghĩ rằng đó là một phần của task.
- ❌ Giải thích lý do hành động một cách mơ hồ để User "bấm nhầm" nút đồng ý.
- ❌ Không kiểm tra lại danh sách tệp sẽ bị ảnh hưởng trước khi xin lệnh xóa.

## 💡 Example Triggers
- "Xóa toàn bộ thư mục build và node_modules."
- "Reset lại repo này về commit cũ."
- "Gỡ cài đặt module X khỏi hệ thống."
