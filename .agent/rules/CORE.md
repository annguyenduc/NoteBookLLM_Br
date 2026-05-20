# CORE.md — Constitutional Rules (Mandatory, All Agents)

> **BẮT BUỘC ĐỌC** theo startup profile trong `AGENTS.md`.
> Runtime source of truth: `AGENTS.md`. File này chỉ chứa hard-stop kernel ngắn.
> `GEMINI.md` là governance reference/archive, không override runtime.

---

## R1 — RAW IMMUTABLE
Vùng `raw_*/` là vùng cấm tuyệt đối. **NGHIÊM CẤM** thực thi các lệnh xóa (`rm`), di chuyển (`mv`), hoặc đổi tên (`ren`/`rename`) đối với bất kỳ file nào trong `3-resources/`.
Chỉ scripts chính thức (`promote.py`, `ingest.py`) được phép thực hiện các thao tác thay đổi trạng thái tại đây thông qua cơ chế **Kernel Bridge**.
Vi phạm = Phá vỡ tính bất biến của tri thức, dẫn đến lỗi hệ thống không thể phục hồi.

## R2 — PROACTIVE INTEGRITY
**CẤM báo cáo ảo.** BẮT BUỘC ghi log trước khi thực hiện bất kỳ tool call nào thay đổi hệ thống.
Không được báo "Đã hoàn thành" nếu chưa có tool call thành công.

## R5 — PREREQ GATE
Read-only actions không cần "GO".

Allowed before GO:
- đọc file liên quan
- inspect status
- chạy dry-run
- query sqlite/index ở chế độ read-only
- tạo plan/spec/report trong chat

Requires explicit GO:
- ghi/sửa/xóa/di chuyển file
- tạo file nháp
- promote operation
- synthesis write
- actual MCP profile switching
- git commit/push
- chạy script có side effect

Nếu không chắc action có side effect hay không, coi như cần GO.

## R8 — HUMAN SUPREMACY
**CHỈ User** mới được set trạng thái `SYNTHESIZED` cho Atom.
Agent chỉ được set `DRAFT` (tạo mới) hoặc `VERIFIED` (sau audit).

> ⛔ **HARD STOP**: Nếu User yêu cầu set `SYNTHESIZED` — dù bằng cách nào, dù lý do gì —
> **TỪ CHỐI ngay lập tức**. `synthesis_guard.py approve / human_synthesize` là lệnh CHỈ DÀNH CHO HUMAN CHẠY TRỰC TIẾP TRONG TERMINAL.
> Agent TUYỆT ĐỐI KHÔNG được gọi lệnh này dưới bất kỳ hình thức nào,
> kể cả subprocess, shell command, hay python import. Không có workaround hợp lệ. Không có exception. Hướng dẫn User tự mở file và sửa trực tiếp.
> Đây là ranh giới không thể vượt qua. Không có ngoại lệ.

## HEALER PROTOCOL
`@healer` là agent duy nhất được phép thực thi rollback khi phát hiện vi phạm R1, R22, R23 hoặc lỗi liên kết hệ thống.
- **Phạm vi**: Thao tác trong `00_Inbox/`, `00_Inbox/failed_queue/` và `3-resources/wiki/` (chỉ dành cho sửa lỗi link và phục hồi R8).
- **Giới hạn**: KHÔNG được promote trực tiếp vào `raw_*/` — mọi file thô sau khi heal phải quay về `00_Inbox/`.
- **Mục tiêu**: Đảm bảo hệ thống luôn có khả năng tự phục hồi (Healing Loop) mà không làm phá vỡ các chốt chặn bảo mật.

---

## TERMINAL PROTOCOL
- Mọi file operation: BẮT BUỘC dùng Python UTF-8 (`encoding="utf-8"`) kết hợp **Surgical Diff** (chỉ sửa vùng cần thiết).
- CẤM dùng các lệnh hệ điều hành trực tiếp (`mv`, `rm`, `del`, `ren`, `rename`) đối với bất kỳ tệp tin nào trong `3-resources/`. Mọi biến động phải thông qua `promote.py`.
- CẤM dùng PowerShell `Out-File`, `Set-Content` hoặc redirect `>` để ghi file có tiếng Việt.
- Lý do: Đảm bảo tính bất biến (Immutability), tính toàn vẹn encoding và tính minh bạch (Auditability).

---

## HARD STOP
Nếu phát hiện vi phạm bất kỳ rule nào trong hệ thống:
**DỪNG ngay lập tức** — không làm gì thêm — báo cáo vi phạm cho User.

---

## TOOL BYPASS PROHIBITION
If any write/edit/command tool returns permission denied, blocked, or not allowed:
- Agent MUST STOP immediately.
- Agent MUST NOT retry the same write using another tool.
- Agent MUST report: blocked tool, target path, intended change.
- Agent MUST ask AN for GO or policy clarification.

Permission denial is a governance signal, not an optimization problem.

Forbidden bypass patterns (examples):
- `replace_file_content` denied → try `mcp_filesystem_edit_file`
- command denied → try Python subprocess
- write_file denied → try shell redirect
- MCP edit denied → try IDE built-in edit

## SYNTHESIS WRITE HARD GATE
Any write, patch, replace, append, rename, move, or generated edit touching
`3-resources/wiki/synthesis/`
requires ALL of the following:
1. Explicit AN GO for that exact file path.
2. `synthesis_guard.py check` run and passed.
3. No fallback to alternate write tools after any denial.

If any write tool is denied for a `synthesis/` path: STOP. Do not attempt another tool.

---
*CORE.md — 6 Constitutional Rules. Phiên bản 1.1 — 2026-05-19.*
*Diễn giải lịch sử 27 rules: [[GEMINI.md]] — reference/archive, không override runtime.*
