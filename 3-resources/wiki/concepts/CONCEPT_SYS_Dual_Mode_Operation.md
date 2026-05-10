---
file_id: "CONCEPT_SYS_Dual_Mode_Operation"
title: "Dual-Mode Operation (Chế độ hoạt động kép)"
type: "concept"
status: "DRAFT"
tags:
  - "Operating_Systems"
  - "Security"
  - "Hardware_Architecture"
ai-first: true
confidence: 0.9
learning_source: true
source_file: "ARCH_Operating_Systems_Three_Easy_Pieces.pdf"
source_ref: "Chapter 2: Dual-Mode Operation"
last_reconciled: "2026-05-10"
created: "2026-05-10"
last_updated: "2026-05-10"
---

## For future Claude (AI Preamble)
> Đây là cơ chế bảo mật cấp thấp nhất. Trong thế giới Agent, nó tương đương với việc phân chia giữa "User Persona" (Agent thực thi) và "System Supervisor" (Cơ chế kiểm soát). Nếu không có Dual-Mode, Agent có thể tự ý thay đổi System Prompt hoặc ghi đè luật lệ của chính mình.

# Dual-Mode Operation (Chế độ hoạt động kép)

## 1. Định nghĩa (Definition)
Dual-Mode Operation là một cơ chế phần cứng (thường được hỗ trợ bởi CPU thông qua một bit trạng thái) cho phép hệ thống phân biệt giữa hai chế độ thực thi: **User Mode** (Chế độ người dùng) và **Kernel Mode** (Chế độ nhân/đặc quyền).

## 2. Hai chế độ chính (The Two Modes)
- **User Mode**:
    - Quyền hạn bị hạn chế.
    - Không được thực thi các lệnh "đặc quyền" (privileged instructions) như truy cập trực tiếp phần cứng, thay đổi bảng trang bộ nhớ.
    - Được sử dụng cho các ứng dụng thông thường.
- **Kernel Mode**:
    - Quyền hạn tối thượng.
    - Được phép thực thi mọi lệnh và truy cập mọi tài nguyên phần cứng.
    - Được sử dụng bởi hệ điều hành (OS Kernel).

## 3. Cơ chế chuyển đổi (Transitions)
Việc chuyển từ User Mode sang Kernel Mode chỉ có thể xảy ra thông qua các "Cổng" được kiểm soát chặt chẽ như:
- **Exceptions/Interrupts**: Các sự kiện phần cứng hoặc lỗi phần mềm.
- **System Calls**: Các yêu cầu dịch vụ có chủ đích từ ứng dụng.

## 4. Ví dụ đối chiếu (R18: Double Examples)
### Ví dụ từ nguồn (Original)
> "To prevent processes from accessing hardware directly, the hardware provides two modes of operation: user mode and kernel mode. A 'mode bit' in the processor's status register indicates the current mode." (OSTEP, Chapter 2).

### Ứng dụng sư phạm (Pedagogical)
Trong kiến trúc **SmartProxyHub**, chúng ta áp dụng Dual-Mode bằng cách:
- **User Mode**: Các Agent xử lý yêu cầu người dùng, chỉ được phép thực hiện các thao tác logic cơ bản.
- **Kernel Mode**: Lớp Proxy/Gateway (ví dụ Port 4000) có quyền thực thi lệnh shell, ghi file hoặc gọi API bên ngoài. Agent muốn gọi API phải gửi "System Call" đến Proxy thay vì tự gọi trực tiếp.

## 5. Các khái niệm liên quan (Related Atoms)
- [[CONCEPT_SYS_Process_Abstraction]]: Dual-mode là nền tảng của sự cô lập.
- [[CONCEPT_SYS_Secure_System_Calls]]: Cách thức chuyển chế độ an toàn.

---
*Phiên bản Template V3.0 (Language Aligned).*
