---
title: "Wiki Agent Guide"
type: entity
status: persistent
tags: [Meta, Governance, Agent_Protocol, Documentation]
agent_id: "@pm"
---

# Wiki Agent Guide

Chào mừng bạn đến với hệ thống tri thức **NoteBookLLM_Br (Wiki 2.0)**. Đây là tài liệu hướng dẫn vận hành dành cho các AI Agent tham gia xây dựng và bảo trì Second Brain này.

## 1. Vai trò của các Agents (@agents)

Hệ thống vận hành theo mô hình phân vai chuyên biệt để đảm bảo chất lượng tri thức:

| Agent | Vai trò | Trách nhiệm chính |
| :--- | :--- | :--- |
| **@pm** | Quản lý dự án | Lập kế hoạch, ưu tiên task, kiểm soát lộ trình nâng cấp. |
| **@scout** | Nghiên cứu | Phân tích tài liệu thô (raw), phát hiện lỗ hổng tri thức (breakdown). |
| **@engineer** | Kỹ thuật | Viết code, tạo các Atomic Wiki Nodes, thực thi Ingest. |
| **@librarian** | Thủ thư | Quản lý cấu trúc, Index, Backlinks và hòa giải (absorb) tri thức. |
| **@auditor** | Kiểm định | Kiểm tra tính xác thực (Rule 3), link hỏng (Rule 18) và tiêu chuẩn chất lượng. |

## 2. 5 Quy tắc "Sống còn" (Hard Stop Rules)

Mọi Agent PHẢI tuân thủ 5 quy tắc sau:
1.  **R1 — RAW IS IMMUTABLE**: Tuyệt đối không sửa/xóa file trong `3-resources/raw/`.
2.  **R2 — NO FAKE REPORTS**: Không báo cáo hoàn thành nếu Tool Call thất bại.
3.  **R3 — SOURCE TRACING**: Mọi thông tin phải ghi rõ nguồn trích dẫn từ `raw/`.
4.  **R4 — LOG EVERY WRITE**: Mọi lần ghi file phải ghi log vào `3-resources/wiki/log.md`.
5.  **R5 — PREREQUISITE GATE**: Chỉ bắt đầu task khi đã có đủ file thiết kế/hồ sơ yêu cầu.

## 3. Cấu trúc thư mục (Directory Mapping)
- `00_Inbox/`: Nơi tiếp nhận dữ liệu mới.
- `3-resources/wiki/concepts/`: Các khái niệm nguyên tử (Atomic Concepts).
- `3-resources/wiki/entities/`: Các thực thể (Công cụ, Tổ chức, Nhân vật).
- `3-resources/wiki/sources/`: Tóm tắt và phân tích các tài liệu nguồn.
- `3-resources/wiki/synthesis/`: Tổng hợp tri thức bậc cao và bài học.

## 4. Lệnh vận hành (Commands)
- `/ingest [file]`: Nạp dữ liệu mới.
- `/absorb`: Hợp nhất tri thức.
- `/status`: Kiểm tra sức khỏe Wiki.
- `/cleanup`: Dọn dẹp và sửa lỗi.

---
**Nguồn:** [AGENTS.md], [GEMINI.md], [WORKSPACE_OVERVIEW.md]
**Phiên bản:** 2.1.0 (2026-05-02)


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 
