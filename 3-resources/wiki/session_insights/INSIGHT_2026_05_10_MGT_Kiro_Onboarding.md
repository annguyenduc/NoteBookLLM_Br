---
file_id: "INSIGHT_2026_05_10_MGT_Kiro_Onboarding"
title: "Session Insight: Onboard Kiro & Build Circuit Breaker (Wiki Ingest Pipeline)"
type: "insight"
kwsr_type: "knowledge"  # knowledge | workflow | skill | rule
status: "DRAFT"
tags:
  - "Infrastructure"
  - "Kiro"
  - "Circuit_Breaker"
  - "Wiki_Ingest"
ai-first: true
confidence: 1.0
last_reconciled: "2026-05-10"
created: "2026-05-10"
last_updated: "2026-05-10"
sources:
  - "[[SOURCE_SESSION_2026_05_10]]"
---

# SESSION INSIGHT: ONBOARD KIRO & BUILD CIRCUIT BREAKER

**Chủ đề**: Onboard Kiro + Build Circuit Breaker cho Wiki Ingest Pipeline

## 1. Quyết định kiến trúc (Architecture Decisions)
- **Vị trí Kiro**: Kiro đặt tại thư mục `.kiro/` trong root `NoteBookLLM_Br/` — ngang hàng `.agent/`, không lồng vào nhau. Điều này giúp tách biệt cấu hình và công cụ của hai agent.
- **Phân vai (Agent Roles)**:
    - **Kiro**: Spec-driven build (Tập trung xây dựng các thành phần phức tạp dựa trên tài liệu đặc tả).
    - **Antigravity**: Chỉnh sửa nhỏ + Thực thi Wiki workflow (Hậu cần tri thức).
    - **Terminal**: Thực thi lệnh và kiểm thử (Test/Run).

## 2. Artifacts tạo ra (Artifacts Inventory)
- [[.kiro/SPEC.md]] — Tài liệu đặc tả (Source of Truth) cho hệ thống circuit breaker.
- [[.kiro/steering.md]] — Các chỉ dẫn hành vi (Guardrails) cho Kiro agent.
- [[.kiro/circuit_breaker.py]] — Mã nguồn hoàn chỉnh, hỗ trợ cả giao diện dòng lệnh (CLI) và lập trình (Programmatic).
- [[.kiro/error_log.md]] — Nhật ký lỗi (Append-only), đảm bảo tính kiên định của dữ liệu qua các phiên làm việc.
- **Bug fix**: Cập nhật `promote.py` để chỉ in `[PLAN] Delete` khi đường dẫn chứa `Converted_Sources`, tăng tính minh bạch cho chế độ dry-run.

## 3. Patterns học được (Knowledge Patterns)
- **Kiro Spec workflow**: Quy trình chuẩn: `Prompt -> requirements.md -> design.md -> tasks.md -> "Start task"`.
- **State Persistence**: Sử dụng file nhật ký lỗi (`error_log.md`) làm nơi lưu trữ trạng thái thay vì các file state chuyên biệt, giúp dữ liệu tồn tại bền vững qua các lần khởi động lại tiến trình.
- **Subprocess Isolation**: Gọi `promote.py` thông qua `subprocess` để đảm bảo mã nguồn gốc không bị can thiệp, đồng thời bắt được toàn bộ `stdout/stderr` cho việc phân tích lỗi.
- **Kiro Free Tier Optimization**: Chiến lược tiết kiệm credit: sử dụng Auto model và ưu tiên nút "Start task" thay vì chat nhiều lượt.

## 4. Tình trạng lỗi (Error Taxonomy Status)
- **Nhóm 4 (Agent retry loop)**: Đã giải quyết (**RESOLVED**) nhờ cơ chế Circuit Breaker.
- **Nhóm 3 (Silent failure)**: Đã giải quyết (**RESOLVED**) thông qua `error_log.md`.
- **Nhóm 1 (Context Pollution, LLM Drift)**: Còn mở (**OPEN**) — Sẽ được giải quyết trong Phase 3 Atomization.
- **Nhóm 2 (Trust boundary / sandbox)**: Còn mở (**OPEN**) — Đã đưa vào danh sách chờ (backlog).
- **DDIA audit stamp**: Chưa hoàn thành — Cần thực hiện `md_auditor.py --fix` trước khi bắt đầu Phase 3.

## 5. Kế hoạch tiếp theo (Status Phase 3)
- **Ready to start**: Hiện có 4 file ARCH trong thư mục `raw_ingest/` đang chờ quy trình Atomization (Phân rã tri thức).

---

## Ví dụ đối chiếu (R18: Double Examples)

### 1. Ví dụ từ nguồn (Original)
> "Kiro đặt tại `.kiro/` trong root `NoteBookLLM_Br/` — ngang hàng `.agent/`, không lồng vào nhau — Phân vai rõ: Kiro = spec-driven build, Antigravity = edit nhỏ + wiki workflow"
> -- Trích Nhật ký phiên 2026-05-10.

### 2. Ứng dụng sư phạm (Pedagogical)
Khi triển khai hệ thống AI đa tác nhân (Multi-agent), việc thiết kế "Ranh giới trách nhiệm" (Separation of Concerns) là cực kỳ quan trọng. 
*Ví dụ*: Trong một lớp học STEM, một học sinh chuyên về thiết kế cơ khí (Kiro), một học sinh chuyên về lập trình (Antigravity), và một học sinh chuyên về kiểm thử (Terminal). Việc phân công này giúp tối ưu hóa thế mạnh của từng thành viên và tránh việc dẫm chân lên nhau.

---
*Duyệt bởi: @antigravity*
*Nguồn tham chiếu: [[SOURCE_SESSION_2026_05_10]]*

