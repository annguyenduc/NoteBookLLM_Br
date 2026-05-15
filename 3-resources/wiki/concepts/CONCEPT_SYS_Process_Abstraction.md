---
file_id: "CONCEPT_SYS_Process_Abstraction"
title: "The Process Abstraction (Sự trừu tượng hóa tiến trình)"
type: "concept"
status: "DRAFT"
tags:
  - "Operating_Systems"
  - "Abstraction"
  - "Isolation"
ai-first: true
confidence: 0.9
learning_source: true
source_file: "ARCH_Operating_Systems_Three_Easy_Pieces.pdf"
source_ref: "Chapter 2: The Process Abstraction"
last_reconciled: "2026-05-10"
created: "2026-05-10"
last_updated: "2026-05-10"
---

## For future Claude (AI Preamble)
> Khái niệm này là "chìa khóa" để giải quyết vấn đề No Isolation trong các hệ thống Agentic. Một tiến trình không chỉ là mã đang chạy; nó là một thực thể bị giới hạn (sandbox) bởi hệ điều hành. Khi áp dụng vào thiết kế Agent, mỗi Agent nên được coi như một "Process" riêng biệt với không gian ngữ cảnh (Context Space) bị cô lập.

# The Process Abstraction (Sự trừu tượng hóa tiến trình)

## 1. Định nghĩa (Definition)
Sự trừu tượng hóa tiến trình (Process Abstraction) là cơ chế của hệ điều hành nhằm tạo ra ảo giác (illusion) cho một chương trình rằng nó đang sở hữu toàn bộ tài nguyên của máy tính (CPU, bộ nhớ), trong khi thực tế nó đang chia sẻ chúng với nhiều tiến trình khác.

## 2. Đặc điểm cốt lõi (Core Principles)
- **Cơ chế Bảo vệ (Protection)**: Ngăn chặn một tiến trình truy cập hoặc sửa đổi bộ nhớ/trạng thái của tiến trình khác hoặc của chính nhân hệ điều hành (Kernel).
- **Cô lập (Isolation)**: Nếu một tiến trình bị lỗi (crash), nó không làm ảnh hưởng đến sự ổn định của các tiến trình khác hoặc hệ thống.
- **Hạn chế quyền (Restricted Execution)**: Tiến trình chạy trong một môi trường có giới hạn quyền truy cập trực tiếp vào phần cứng.

## 3. Liên hệ kiến trúc Agentic (R18: Pedagogical Application)
| Đặc tính OS | Ứng dụng vào Agent Design |
|---|---|
| **Process** | **Isolated Agent Instance** (Mỗi Agent có vùng nhớ/context riêng). |
| **Address Space** | **Context Window** (Giới hạn thông tin Agent có thể truy cập). |
| **Limited Rights** | **Tool Permissions** (Agent không được gọi Tool trực tiếp mà phải qua Gateway). |

## 4. Ví dụ đối chiếu (R18: Double Examples)
### Ví dụ từ nguồn (Original)
> "A process is a program in execution. To provide protection, the operating system must limit what a process can do... This is achieved by running the process in a restricted environment." (OSTEP, Chapter 2).

### Ứng dụng sư phạm (Pedagogical)
Khi thiết kế một hệ thống Multi-Agent, thay vì để các Agent "nhìn thấy" toàn bộ lịch sử hội thoại của nhau (gây ô nhiễm ngữ cảnh), chúng ta nên áp dụng **Process Abstraction**: Mỗi Agent chỉ nhận được phần Context cần thiết để thực hiện nhiệm vụ của mình, tương tự như cách một Process chỉ nhìn thấy Address Space của riêng nó.

## 5. Các khái niệm liên quan (Related Atoms)
- [[CONCEPT_SYS_Dual_Mode_Operation]]: Cơ chế hỗ trợ cô lập.
- [[CONCEPT_SYS_Secure_System_Calls]]: Giao diện giao tiếp an toàn.

---
*Phiên bản Template V3.0 (Language Aligned).*
