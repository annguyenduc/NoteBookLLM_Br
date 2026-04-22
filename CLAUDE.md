# Antigravity CLAUDE.md (LOM v4.0 Supreme)

> **Goal**: Vận hành Hệ sinh thái Tri thức NotebookLM chuyên sâu cho giáo dục STEAM & AI. Hướng tới hệ thống Swarm Agent tự phục hồi (Self-healing) và tự học (Recursive Learning).

## 🗺️ SESSION_CONTEXT (Điền trước mỗi phiên làm việc)
    Ai điền: Người dùng điền trước khi gọi agent đầu tiên trong phiên.
    Khi nào cập nhật: @pm append cập nhật vào brain/log.md sau mỗi bước hoàn thành.
    Quy tắc: Agent đọc block này ĐẦU TIÊN trước khi đọc bất cứ thứ gì khác. 
```yaml
session:
  date: "YYYY-MM-DD"
  active_task: "[VD: Tạo đề kiểm tra Module M2.1]"
  active_pipeline: "exam | design | scout | audit | split-kb"
  current_step: "[VD: Bước 2/4 — @engineer viết đề]"
  last_output: "[VD: brain/distilled/EXAM_Context_M2.md — đã tạo xong]"
  next_expected: "[VD: brain/distilled/EXAM_M2_Draft.md]"
  blocking_issues: "none | [mô tả vấn đề cụ thể]"
  active_agent: "@[tên agent đang chạy]"
  notes: "[ghi chú thêm nếu cần — để trống nếu không có]"
```
Ví dụ điền thực tế:

```yaml
session:
  date: "2026-04-12"
  active_task: "Split ELN_Test_KB_IOT.md thành atomic notes"
  active_pipeline: "split-kb"
  current_step: "Bước 1/4 — @scout liệt kê tags"
  last_output: "none"
  next_expected: "brain/distilled/TAG_LIST_IOT.md"
  blocking_issues: "none"
  active_agent: "@scout"
  notes: "Nguồn: brain/raw/ELN_Test_KB_IOT.md"
``` 
## 🗂️ Cấu trúc tri thức (Wiki Taxonomy)
Các Knowledge Items (KIs) chính nằm tại `brain/distilled/`:
- [[Pedagogical_Master_DNA]] — "Gen" sư phạm và Tri thức nền.
- [[Education_AI_Handbook]] — Cẩm nang dạy & học AI K12.
- [[Engineering_Robotics_Master]] — Kỹ thuật Robot & Hệ thống.
- [[DevOps_IT_Automation_Wiki]] — Lưu trữ script và vận hành IT.

## 🛠️ Quy trình làm việc (ECC Standard)
1. **Manus First**: Luôn đọc `task_plan.md` (nếu có) và `AGENTS.md` trước khi làm việc.
2. **Absolute Flatness**: Tuyệt đối không để thư mục sâu quá 2 cấp từ Root. Sử dụng underscore prefix thay vì thư mục con (e.g. `distilled/ELN_Test_AI_file.md`).
3. **Double Link**: Mọi tệp markdown mới phải có liên kết chéo `[[Wikilink]]`.
4. **Log-First Ingest**: Mọi thay đổi lớn phải được ghi vào `brain/log.md`, phải dùng append không được overwrite, phải viết đúng định dạng được ghi trong log.
5. **Anti-Hallucination**: Tuân thủ nghiêm ngặt [[AUDITOR_Protocol.md]].
6. **Exam Handoff (Rule 9)**: Mọi tác vụ ra đề kiểm tra BẮT BUỘC @scout tạo `brain/distilled/EXAM_Context_[module].md` trước. @engineer chỉ được bắt đầu sau khi file này tồn tại. Xem chi tiết tại [[AGENTS.md]].

## 🤖 Biệt đội Agent (Swarm Registry v4.0 Supreme)
Xem chi tiết tại [[AGENTS.md]]. Các vai trò chính:
- **Planner (@pm)**: Lập kế hoạch theo ECC, Audit ID và điều phối Swarm.
- **Executioner (@engineer)**: Viết mã nguồn, thực thi TDD và sửa lỗi hệ thống (@healer profile).
- **Researcher (@scout)**: Nghiên cứu tri thức, Audit CLT và tạo EXAM Context.
- **Orchestrator (@devops)**: Quản lý MCP, Terminal, Git và hạ tầng Smart Proxy.
- **Reviewer (@librarian)**: Rà soát chất lượng tri thức, quản lý Wiki và linting.
- **Integrity (@auditor)**: Đối soát nguồn theo AUDITOR_Protocol và ngăn chặn ảo giác.
- **Instructional Designer (@designer)**: Thiết kế learning sequence, scaffolding, lesson plan theo 5E/UDL/Backward Design.
- **Learning Evaluator (@evaluator)**: Phân tích kết quả đào tạo theo Kirkpatrick, xác định knowledge gap, đề xuất remediation.
- **Learner Profiler (@profiler)**: Xây dựng Trainer Profile (entry/intermediate/advanced), feed context cho @designer và @engineer.
- **Creative Specialist (@creative)**: Tạo case study, roleplay scenario, lesson plan mẫu (High-engagement content).
- **Maintenance Specialist (@healer)**: Hàn gắn tri thức, sửa lỗi liên kết và phục hồi tính toàn vẹn hệ thống.

## 🚀 Build & Test Commands
- `python scripts/brain_lint.py` — Kiểm định sức khỏe Wiki.
- `python scripts/setup/graphify_bootstrap.py` — Cập nhật đồ thị tri thức (V-Ingest).
- `/heal` — Sửa lỗi hệ thống tự động.
- `/heartbeat` — Đồng bộ hóa tri thức raw -> distilled.

---
*Thuộc dự án: NoteBookLLM_Br | Framework: Antigravity v4.0 | Engine: LLM Wiki Supreme*