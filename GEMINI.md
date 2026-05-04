# GEMINI.md — NoteBookLLM_Br

> **Antigravity highest-priority rules.** Overrides all other rule files.
> Single Source of Truth for System Governance & Pedagogical Standards.

---

## 🛡️ 5 HARD STOP RULES (Không thể vi phạm)

### R1 — RAW IS IMMUTABLE
`3-resources/raw/` là read-only với mọi agent và tool.
**Vi phạm → DỪNG ngay, ghi incident vào `3-resources/wiki/log.md`.**

### R2 — NO FAKE REPORTS
Tuyệt đối KHÔNG báo "Đã tạo/sửa file" nếu chưa có tool call thành công.
**Vi phạm → Tự phê bình, ghi lỗi vào `CONTINUITY.md`, thông báo user.**

### R3 — SOURCE TRACING (Chứng cứ thép)
Mọi claim trong `3-resources/wiki/` phải ghi:
`Nguồn: [tên file trong raw/] — [section cụ thể]`
Không tìm thấy nguồn → ghi `[KHÔNG TÌM THẤY NGUỒN]`. KHÔNG tự điền thay thế.

### R4 — LOG EVERY WRITE
Mọi lần ghi file → append vào `3-resources/wiki/log.md`:
```
## [YYYY-MM-DD HH:MM] <type> | <agent> | <mô tả>
- File: [đường dẫn]
- Lý do: [1 câu]
```
Encoding bắt buộc: **UTF-8 no BOM**. PowerShell: luôn thêm `-Encoding UTF8`.

### R5 — PREREQUISITE GATE
- `@designer` chỉ bắt đầu khi `2-areas/Profiles/Trainer_Profile_[id].md` tồn tại.
- `@engineer` chỉ bắt đầu khi `1-projects/[Project]/Learning_Design_[module].md` tồn tại.
- File chưa có → DỪNG, báo `@pm`, không tự tiếp tục.

### R6 — SEQUENTIAL FOUNDATION
Tuyệt đối KHÔNG viết bất kỳ dòng code Skill nào cho đến khi Phase 1 (Schema, SOUL, USER) hoàn thành 100% và được xác nhận.

### R7 — PRESSURE TEST MANDATORY
Mỗi Skill/Script sau khi hoàn thành phải vượt qua ít nhất 1 bài kiểm tra áp lực (Stress Test) với dữ liệu thực tế lớn trước khi chuyển sang Skill tiếp theo.

### R8 — HUMAN-ONLY SYNTHESIS
Agent tuyệt đối KHÔNG tự ý thiết lập trạng thái `SYNTHESIZED` cho các concept. Đây là quyền hạn duy nhất của User sau khi review `review_queue/`.

### R9 — SURGICAL MINIMALISM
Tuân thủ nghiêm ngặt **Surgical Changes**: Chỉ thay đổi code tối thiểu để giải quyết vấn đề, không over-engineer, không tự ý refactor code lân cận nếu không liên quan trực tiếp đến task.

### R10 — SEARCH & VISUAL VALIDATION PIPELINE (Quy trình 3 bước)
Mọi hành động thu thập dữ liệu web BẮT BUỘC phải tuân thủ quy trình 3 bước để đảm bảo tính xác thực và tránh rác:
1. **Bước 1: Discovery (Tìm kiếm)**: Sử dụng `Lightpanda` hoặc `search_web` để tìm kiếm và lọc danh sách URL tiềm năng.
2. **Bước 2: Verification (Xác thực nội dung)**: BẮT BUỘC truy cập URL bằng `Lightpanda` hoặc `Crawl4AI` ở chế độ trích xuất **Markdown/Text** để xác nhận URL tồn tại (HTTP 200) và chứa đúng nội dung tri thức cần tìm. **TUYỆT ĐỐI KHÔNG** chụp ảnh ở bước này.
3. **Bước 3: Visual Capture (Chụp ảnh bằng chứng)**: Chỉ thực hiện chụp ảnh (Screenshot) bằng `Crawl4AI` hoặc `Browser Subagent` sau khi Bước 2 xác nhận nội dung **ĐẠT YÊU CẦU**.
- **Cấm 404/Rác**: Tuyệt đối không chụp ảnh trang lỗi 404, trang trắng, CAPTCHA hoặc trang không liên quan.
- **Vi phạm**: Nếu phát hiện ảnh rác, Agent phải tự động rollback, ghi lỗi vào `3-resources/wiki/log.md` và thực hiện lại cho đến khi có bằng chứng thực.

---

## 🏗️ QUY ƯỚC WIKI (WIKI CONVENTIONS)

### 1. Đặt tên & Cấu trúc (Naming)
- **File Concept**: `CONCEPT_[PREFIX]_[Name].md` (vd: `CONCEPT_PY_Pandas_Basics.md`).
- **File Entity**: `ENTITY_[TYPE]_[Name].md` (vd: `ENTITY_TOOL_Lightpanda.md`).
- **Ngôn ngữ**: Tiếng Việt (UTF-8 no BOM). Không dùng dấu cách, dùng `_`.

### 2. Cấu trúc Concept chuẩn (Golden Template)
Mọi trang Concept phải tuân thủ cấu trúc 4 tầng:
1.  **Metadata**: `file_id`, `category: "Wiki Page"`, `prefix: "WIKI"`, `agent_id`, `status: "verified|stub"`.
2.  **Core Principle**: Bản chất cốt lõi của khái niệm.
3.  **Ví dụ đối chiếu (Rule 17)**: 1 ví dụ thực tế (Original) + 1 ẩn dụ sư phạm (Pedagogical).
4.  **4F Reflection**: Facts, Feelings, Findings, Futures.

---

## ⚡ LỆNH VẬN HÀNH (Wiki 2.0)

| Lệnh | Agent | Làm gì |
|---|---|---|
| `/ingest [file]` | @scout | Nạp raw -> atomic atoms + sơ khởi liên kết |
| `/absorb` | @librarian | Hợp nhất atoms vào synthesis |
| `/query [query]` | @librarian | Truy vấn tri thức (Hybrid Search) |
| `/breakdown` | @scout | Phát hiện lỗ hổng tri thức |
| `/cleanup` | @auditor | Dọn dẹp & Audit chất lượng |
| `/status` | @pm | Báo cáo sức khỏe Wiki |
| `/rebuild` | @engineer | Đồng bộ Index & Backlinks |

---
*Full agent registry + folder map → `AGENTS.md`*
