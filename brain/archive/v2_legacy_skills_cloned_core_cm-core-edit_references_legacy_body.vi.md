# 🛠️ CM Core Edit: Minimalist Editing Methodology (LITE)

> **Goal:** Sửa đổi mã nguồn một cách "ngoại khoa" (Surgical), chỉ thay thế đoạn cần thiết (Targeted Replacement) thay vì ghi đè toàn bộ (Full Overwrite).

## 🚀 Execution Workflow
1.  **Read & Contextualize**: Sử dụng `FileReadTool` để xác định chính xác số dòng (Line Numbers) và đoạn code cần thay thế.
2.  **Target Selection**: Xác định `TargetContent` là một đoạn văn bản DUY NHẤT và đủ dài để không bị nhầm lẫn với các đoạn khác.
3.  **Diff Validation**: Mô phỏng sự thay đổi trong bộ nhớ trước khi thực thi lệnh `replace_file_content`.
4.  **Verification**: Sau khi sửa, luôn gọi `Terminal` hoặc `TDD` để xác nhận logic không bị gãy.

## 📐 Quality Gates (Red Flags)
- ❌ Không sửa file khi chưa đọc nội dung hiện tại (FileRead).
- ❌ Ghi đè toàn bộ tệp (>100 lines) khi chỉ cần sửa 1-2 dòng logic.
- ❌ Sử dụng `ReplacementContent` không chứa các khoảng trắng (Indentation) phù hợp với bối cảnh.
- ❌ Sửa nhiều khối không liên quan trong 1 lần gọi tool (nếu không cần thiết).

## 💡 Pro Tips (Inspired by Claude Code)
- **Token Efficiency**: Chỉ truyền đoạn `TargetContent` hẹp nhất có thể.
- **Context Preservation**: Giữ nguyên các chú thích (comments) và cấu trúc lân cận.
- **Atomic Operations**: Mỗi bước sửa đổi nên là một đơn vị logic hoàn chỉnh.

## 💡 Example Triggers
- "Sửa lỗi chính tả trong file này."
- "Refactor hàm `calculate_total` để dùng `sum()`."
- "Thêm một dòng comment vào đầu file logic."
- "Cập nhật giá trị biến môi trường trong cấu trúc JSON."
