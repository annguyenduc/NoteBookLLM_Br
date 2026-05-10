---
file_id: "CONCEPT_SYS_Secure_System_Calls"
title: "Implementing Secure System Calls (Thực thi lời gọi hệ thống an toàn)"
type: "concept"
status: "DRAFT"
tags:
  - "Operating_Systems"
  - "Security"
  - "Interface_Design"
ai-first: true
confidence: 0.9
learning_source: true
source_file: "ARCH_Operating_Systems_Three_Easy_Pieces.pdf"
source_ref: "Chapter 2: Implementing Secure System Calls"
last_reconciled: "2026-05-10"
created: "2026-05-10"
last_updated: "2026-05-10"
---

## For future Claude (AI Preamble)
> Đây là giao diện (Interface) giữa thế giới bị hạn chế (Agent) và thế giới đầy quyền năng (System). Một thiết kế System Call tồi (ví dụ: cho phép truyền chuỗi lệnh thô) sẽ dẫn đến các lỗ hổng như Prompt Injection hoặc Unauthorized Tool Use.

# Implementing Secure System Calls (Thực thi lời gọi hệ thống an toàn)

## 1. Định nghĩa (Definition)
System Call (Lời gọi hệ thống) là một giao diện lập trình ứng dụng (API) cho phép các chương trình đang chạy ở User Mode yêu cầu các dịch vụ đặc quyền từ Kernel. "Secure" ở đây nhấn mạnh vào việc kiểm soát tham số và xác thực trước khi thực thi.

## 2. Quy trình thực thi an toàn (Secure Workflow)
1. **Trap Instruction**: Ứng dụng thực thi một lệnh đặc biệt (trap) để chuyển CPU sang Kernel Mode.
2. **Jump to Handler**: Hardware nhảy đến một địa chỉ cố định trong bảng vector ngắt (Interrupt Vector Table) do Kernel quản lý.
3. **Parameter Validation**: Kernel kiểm tra tính hợp lệ của các tham số (ví dụ: địa chỉ bộ nhớ có thuộc quyền sở hữu của tiến trình đó không?).
4. **Execution & Return**: Kernel thực hiện nhiệm vụ và chuyển CPU trở lại User Mode.

## 3. Các lỗi thiết kế cần tránh (Common Pitfalls)
- **Time-of-Check to Time-of-Use (TOCTOU)**: Tham số bị thay đổi sau khi đã được kiểm tra nhưng trước khi được sử dụng.
- **Buffer Overflow**: Không kiểm tra độ dài dữ liệu đầu vào.
- **Direct Pointer Access**: Cho phép User Mode truyền con trỏ trực tiếp vào vùng nhớ Kernel.

## 4. Ví dụ đối chiếu (R18: Double Examples)
### Ví dụ từ nguồn (Original)
> "The kernel must never trust the user. Every parameter passed via a system call must be checked for validity before the kernel acts on it." (OSTEP, Chapter 2).

### Ứng dụng sư phạm (Pedagogical)
Khi xây dựng một Agent có khả năng chạy lệnh Python, chúng ta không nên để Agent truyền chuỗi `os.system(cmd)` trực tiếp. Thay vào đó, hãy dùng **Secure System Call Pattern**:
- Agent gửi yêu cầu: `{"action": "read_file", "path": "data.csv"}`.
- Gateway kiểm tra: "Agent này có quyền đọc file không? File `data.csv` có nằm trong thư mục cho phép không?".
- Gateway thực thi lệnh an toàn thông qua thư viện chuẩn thay vì shell.

## 5. Các khái niệm liên quan (Related Atoms)
- [[CONCEPT_SYS_Dual_Mode_Operation]]: Cơ chế hỗ trợ chuyển đổi chế độ.
- [[CONCEPT_SYS_Process_Abstraction]]: Mục tiêu cuối cùng của việc bảo vệ.

---
*Phiên bản Template V3.0 (Language Aligned).*
