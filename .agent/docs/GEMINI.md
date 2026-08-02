# GEMINI.md — Governance Reference / Archive

> Reference mở rộng cho lịch sử rule, audit sâu, và workflow phức tạp.
> Không inject mặc định ở startup.
> File này không phải runtime source of truth.
> Khi có xung đột, thứ tự ưu tiên là:
> 1. User instruction trong phiên hiện tại, nếu không vi phạm runtime safety.
> 2. `AGENTS.md`
> 3. `.agent/rules/CORE.md`
> 4. `.agent/rules/[agent].md`
> 5. Workflow được gọi trực tiếp.
> 6. Skill instruction.
> 7. `GEMINI.md` như tài liệu tham chiếu/archive.

## META-RULE
Không dùng file này để phủ quyết mọi yêu cầu của User.
Chỉ từ chối khi yêu cầu vi phạm safety rule rõ ràng: raw immutable, secret exposure, destructive command, fake reporting, hoặc agent tự set SYNTHESIZED.

---

## 🛡️ BỘ QUY TẮC CỐT LÕI (Hard Stop Rules)

| Nhóm | Rule | Tên Luật | Hành vi BẮT BUỘC / CẤM |
|---|---|---|---|
| **I. Quản trị** | **R1** | Raw Immutable | Vùng `raw_*/` là vùng cấm tuyệt đối. NGHIÊM CẤM thực thi các lệnh xóa (`rm`), di chuyển (`mv`), hoặc đổi tên (`ren`/`rename`) đối với bất kỳ file nào trong `3-resources/`. |
| | **R2** | Proactive Integrity | CẤM báo cáo ảo. BẮT BUỘC ghi log trước khi thực hiện (Logging First). |
| | **R3** | Source Tracing & Map-First | Mọi trích dẫn phải có Link Nguồn (Source Node). BẮT BUỘC khởi tạo Bản đồ (Source Node) TRƯỚC KHI bóc tách chi tiết. |
| | **R4** | Structure & Encoding | BẮT BUỘC Python UTF-8 & Surgical Diff. CẤM dùng PowerShell ghi file tiếng Việt & CẤM file mới tại Root. |
| | **R5** | Prereq Gate | Lệnh sản xuất (Design/Task) phải rõ ràng trước khi chạy. |
| **II. Thực thi** | **R6** | Phased Execution | Tuyệt đối KHÔNG viết Skill khi chưa xong Phase 1. |
| | **R7** | Stress Testing | BẮT BUỘC Stress Test sau mỗi Skill/Script. |
| | **R8** | Human Supremacy | CHỈ User mới được set trạng thái `SYNTHESIZED` (3-Layer Enforced). |
| | **R9** | Surgical Min | Chỉ thay đổi code tối thiểu (Surgical Changes). |
| | **R10** | Strict URL Ingestion | CẤM sử dụng sub_browser hoặc trình duyệt mặc định để đọc tài liệu gốc (Wikipedia, bài báo, v.v.). BẮT BUỘC dùng .agent/skills/wiki-web-scrape (cho static text) hoặc .agent/skills/wiki-crawl-4ai (nếu cần screenshot) để lưu bản nháp vào 00_Inbox/ TRƯỚC KHI tạo Atom. |
| **III. Dữ liệu** | **R11** | Density Filter | KHÔNG tạo atom cho file < 200 bytes. |
| | **R12** | Example Adherence | BẮT BUỘC đối soát với `EXAMPLES.md` & `@/obsidian-markdown`. |
| | **R13** | Atom Lifecycle | Mọi atom mới mặc định `status = DRAFT`. |
| | **R14** | Log Rotation | Log phân mảnh theo ngày: `log_YYYY_MM_DD.md`. |
| | **R15** | Peer-layer Sync | BẮT BUỘC dùng `@obsidian-cli` để reload sau Metadata. |
| | **R16** | Checkpoint | Khai báo trạng thái (READY/BLOCKED) trước task. |
| | **R17** | Sync Direction | File vật lý là Source of Truth duy nhất. |
| | **R18** | Double Examples | BẮT BUỘC mỗi Atom phải có 2 ví dụ đối chiếu (Sách + Sư phạm). |
| | **R19** | Sandbox Protocol | BẮT BUỘC chạy code thử nghiệm trong Localsandbox (WASM). |
| | **R20** | YAML Validity | Metadata có dấu `:` phải để trong ngoặc kép "". |
| | **R21** | Self-Auditing Gate | BẮT BUỘC pass `audit_raw_ingest.py` khi vào `raw_ingest`. |
| | **R22** | Staging-Promote | BẮT BUỘC xử lý thô trong `00_Inbox`. CẤM ghi trực tiếp vào `3-resources`. |
| | **R-FLATTEN** | Flattened Storage | CẤM tạo thư mục con trong `raw_sources/`, `raw_ingest/`, và `raw_assets/`. Mọi tệp phải nằm ở root của các thư mục này. |
| | **R-VENV** | Venv Mandatory | BẮT BUỘC sử dụng `.venv\Scripts\python.exe` cho mọi thao tác Python để đảm bảo hỗ trợ GPU/CUDA và cô lập thư viện. |
| | **R23** | Promotion Gate | TUYỆT ĐỐI CẤM dùng `move_file` hoặc shell (`Move-Item`) để đưa file vào `raw_*`. CHỈ được dùng `promote.py` qua Circuit Breaker. |
| **IV. Local AI Audit** | **R24** | Local AI Audit — Trigger | @scout PHẢI gọi `gap_check.py` thủ công sau mỗi chunk, trước khi báo "User Approved". |
| | **R25** | Local AI Audit — Non-blocking | Nếu Ollama offline hoặc gemma3:4b lỗi → WARNING + tiếp tục. CẤM block pipeline chính. |
| | **R26** | Local AI Audit — Human Gate | `gap_candidates/` chỉ dành cho Human Review. @engineer không được tự ý dùng output này nếu chưa có Human approve. |
| | **R27** | Local AI Audit — Scope Isolation | CHỈ dùng Gap-Check cho `DRAFT` atoms. Tuyệt đối KHÔNG dùng cho `synthesis/` hoặc `verified` content. |
| **V. Recovery** | **R28** | Healer Scope | `@healer` được phép thao tác trong `00_Inbox/`, `failed_queue/` và `3-resources/wiki/` (chỉ để sửa lỗi link/R8 rollback). KHÔNG được promote thẳng vào `raw_*/`. Ghi log vào R14. |


---

## 🎭 HỆ THỐNG DANH TÍNH AGENT (PERSONAS)
Bản tóm tắt "Linh hồn" và Thẩm quyền của 7 đặc vụ trong NoteBookLLM_Br. (Chi tiết quy tắc xem tại `.agent/rules/`).

- **@pm (Product Manager)**: Visionary Architect (15+ yrs). Thiết kế hệ thống, lập kế hoạch. Không viết code. Phải có User Approve (R5).
- **@engineer (Full-Stack Engineer)**: 10x Senior Polyglot. Viết code DRY, Surgical Min (R9). Tuân thủ Sandbox (R19) và kiến trúc của PM.
- **@scout (Knowledge Scout)**: Elite Data Analyst. Bóc tách tri thức thô. Bị giới hạn nghiêm ngặt ở `00_Inbox/` (R22) và Strict URL (R10).
- **@librarian (Knowledge Librarian)**: Master Archivist. Quản lý Index, Taxonomy. Tuyệt đối không tự set `SYNTHESIZED` (R8).
- **@auditor (QA & Integrity Auditor)**: Relentless QA. Ám ảnh với độ tinh khiết của Metadata và Source Tracing (R3). Fail-hard nếu có lỗi.
- **@designer (Instructional Designer)**: World-class Educator. Ánh xạ tri thức sang Bloom/EDP. Yêu cầu Trainer Profile trước khi chạy.
- **@healer (System Healer & DevOps)**: Khôi phục hệ thống (DLQ), sửa lỗi đứt gãy. Bị giới hạn không gian hoạt động, không được vượt rào promote (R28).

---
## HARD STOP RULES - CẬP NHẬT THÁNG 5/2026

### 0. General Rules (Thêm)
- **DỪNG-STOP**: Nếu có thông báo vi phạm Rule. Dừng tiến trình lại và thông báo User không được làm gì tiếp.

### 00. Terminal Protocol (Reinforced)
- **File Operation**: Mọi thao tác ghi file (Write) BẮT BUỘC thông qua Python với `encoding="utf-8"` và sử dụng **Surgical Diff** (chỉ thay đổi tối thiểu).
- **PowerShell Prohibition**: Tuyệt đối không dùng `Out-File`, `Set-Content` hoặc chuyển hướng `>` từ terminal để ghi nội dung có tiếng Việt vào file.
- **Environment**: Luôn đảm bảo `$env:PYTHONIOENCODING = "utf-8"` (đã cấu hình trong Profile).

## WikiCouncil 2.0 - 7 Level Audit

### 1.WikiCouncil 2.0 - Nguyên tắc Tạo Nguồn (Source Node Protocol)
- **Bối cảnh**: Quy trình Wiki Council (R8) hiện chưa định rõ cách xử lý tài liệu từ web (Wikipedia, báo chí, URL).
- **Bổ sung**: Cấm tuyệt đối việc trích dẫn trực tiếp từ web vào Atom mà không qua giai đoạn trung gian (Inbox/Scrape).

### 2. Wiki Council 2.0 - Xử lý tài liệu từ Web (Web Scrape Protocol)
- **Cấm**: Sử dụng trình duyệt mặc định (browser.use_browser) hoặc các lệnh không qua hệ thống (sub_browser) để lấy nội dung web.
- **Bắt buộc**: Phải sử dụng các agent chuyên dụng (`.agent/skills/wiki-web-scrape` hoặc `wiki-crawl-4ai`) để đưa nội dung vào thư mục `00_Inbox/` trước.
- **Quyền phê duyệt**: Chỉ có `WikiCouncil` (hoặc `@human`) mới có quyền lấy nội dung từ Inbox ra Atom chính thức.

### 3. WikiCouncil 2.0 - Vòng đời của Atom (Atom Lifecycle)
- **Trạng thái mới (DRAFT)**: Mặc định mọi Atom tạo mới có trạng thái là `DRAFT`.
- **Vai trò của Agent**: Agent chỉ có quyền chuyển trạng thái lên `VERIFIED` sau khi hoàn thành quy trình kiểm định (Audit).
- **Quyền Synthesize**: Chỉ `WikiCouncil` (hoặc `@human`) mới có quyền phê duyệt cuối cùng (chuyển sang `SYNTHESIZED`).

### 4. WikiCouncil 2.0 - Xử lý Tài liệu Cũ và Đã Tồn Tại (Legacy Data Handling)
- **Bối cảnh**: Trong hệ thống hiện tại, các file Atom cũ (VD: Concept_X.md) thường có trạng thái ngầm định là `VERIFIED` hoặc đã được tổng hợp.
- **Bổ sung**: Khi thực hiện các tác vụ Wiki Council (Scan, Audit, Verify), Agent PHẢI kiểm tra và cập nhật lại metadata của các file này nếu cần:
    1. Nếu Atom đó là **Nguồn tham khảo (Source Node)** cho các Atom khác: Đảm bảo `status` là `VERIFIED` và có metadata nguồn rõ ràng.
    2. Nếu Atom đó chứa **Tri thức chính (Core Knowledge)**: Cân nhắc chuyển sang trạng thái `SYNTHESIZED` nếu nó đã được kiểm duyệt kỹ lưỡng.
    3. **Cấm**: Để một Atom quan trọng ở trạng thái `DRAFT` quá lâu mà không có kế hoạch rõ ràng.

### 5. WikiCouncil 2.0 - Nguyên tắc Xử lý Xung đột Nguồn (Source Conflict Resolution Protocol)
- **Bối cảnh**: Khi ingest tài liệu có thông tin mâu thuẫn (ví dụ: hai file PDF về cùng một chủ đề nhưng có số liệu khác nhau), Agent gặp khó khăn trong việc quyết định nguồn nào đúng.
- **Bổ sung**:
    1. **Không được tự quyết**: Agent tuyệt đối không được tự ý chọn một bên là "đúng" và bác bỏ bên còn lại.
    2. **Đánh dấu mâu thuẫn**: Khi phát hiện Source Node mâu thuẫn, Agent PHẢI:
        - Tạo một Atom ghi lại mâu thuẫn đó (`CONTRADICTS`).
        - Kích hoạt `wiki-council` (hoặc `@human`) để thông báo về xung đột.
        - Yêu cầu hội đồng đưa ra phán quyết cuối cùng.
    3. **Mục tiêu**: Đảm bảo tính toàn vẹn và chính xác của tri thức, tránh lan truyền thông tin sai lệch.
### 6. WikiCouncil 2.0 - Tối ưu hóa Năng suất (Productivity Optimization)
- **Bối cảnh**: Quy trình WikiCouncil hiện tại đôi khi còn tốn nhiều tài nguyên và thời gian cho các tác vụ đơn giản.
- **Bổ sung**:
    1. **Phân loại Tác vụ**: Chia thành 3 loại chính: 
        - `SCAN`: Chỉ đọc và phân tích, không thay đổi dữ liệu.
        - `AUDIT`: Kiểm tra, đánh giá và sửa lỗi metadata.
        - `VERIFY`: Xác nhận và phê duyệt, có thể thay đổi trạng thái.
    2. **Tự động hóa**: Tận dụng tối đa các công cụ và agent có sẵn (`wiki-web-scrape`, `wiki-crawl-4ai`, `@obsidian-cli`) để giảm thiểu thao tác thủ công.
    3. **Quyền hạn hóa**: Ủy quyền cho Agent thực hiện các tác vụ `SCAN` và `AUDIT` một cách độc lập, chỉ cần `@human` hoặc `wiki-council` phê duyệt khi có thay đổi quan trọng hoặc xung đột.
### 7. WikiCouncil 2.0 - Bảo vệ Liên kết Hệ thống (System Link Integrity Protocol)
- **Bối cảnh**: Trong quá trình chỉnh sửa, Atom và Metadata có thể bị tách rời, dẫn đến "Broken Links" (liên kết gãy) hoặc metadata không đồng bộ.
- **Bổ sung**:
    1. **Liên kết Nội bộ (Internal Links)**: Khi sửa đổi tên file Atom hoặc Metadata, Agent PHẢI tìm kiếm toàn bộ các Atom khác đang liên kết đến file cũ và cập nhật lại đường dẫn cho chính xác.
    2. **Đồng bộ Metadata (Metadata Sync)**: Sau khi sửa đổi Metadata, Agent BẮT BUỘC phải kích hoạt `@obsidian-cli` để reload lại hệ thống, đảm bảo các thay đổi được áp dụng ngay lập tức.
    3. **Kiểm tra Chéo (Cross-check)**: Trước khi hoàn thành tác vụ, Agent phải thực hiện kiểm tra chéo để đảm bảo không có Broken Links mới phát sinh và Metadata được đồng bộ hoàn toàn.
### 8. WikiCouncil 2.0 - Chống Nội dung "Rác" và Tái Chế Kiến thức (Anti-Spam & Knowledge Reuse Protocol)
- **Bối cảnh**: Hệ thống có thể bị lạm dụng để tạo ra số lượng lớn Atom chất lượng thấp ("Spam") hoặc các Atom chỉ lặp lại thông tin đã có.
- **Bổ sung**:
    1. **Ngăn chặn Tạo Nội dung Rác (Anti-Spam)**:
        - **Luật R11 Mở rộng (Content Density)**: Ngoài việc kiểm tra dung lượng (< 200 bytes), Agent còn phải đánh giá **Mật độ tri thức (Knowledge Density)**. Không chấp nhận các Atom chỉ chứa định nghĩa hời hợt hoặc thông tin quá hiển nhiên mà không có phân tích sâu hoặc ví dụ minh họa.
        - **Knowledge Reuse Check**: Đối với các yêu cầu tạo nội dung mới, Agent phải kiểm tra xem thông tin đó đã tồn tại trong Wiki chưa. Nếu đã có, ưu tiên tạo **Atomic Links** hoặc **Refactor** (tái cấu trúc) chứ không tạo file mới.
    2. **Tái Chế Kiến thức (Knowledge Reuse)**: Khi một tài liệu mới có nội dung tương tự tài liệu đã có, Agent cần:
        - Tìm kiếm các Atom liên quan (`@query`).
        - Hợp nhất (Merge) thông tin hoặc tạo **Citations** (trích dẫn) đến Atom cũ thay vì tạo lại nội dung.
        - Đánh dấu Atom gốc là `VERIFIED` nếu nó chưa được đánh dấu.
### 9. WikiCouncil 2.0 - Quy tắc Kiểm định Metadata (Metadata Verification Rules)
- **Bối cảnh**: Metadata là xương sống của hệ thống Wiki Council, nhưng Agent có xu hướng bỏ qua hoặc làm sai lệch thông tin này.
- **Bổ sung**:
    1. **Bắt buộc Metadata**: Mọi Atom mới tạo phải có đầy đủ các trường metadata bắt buộc theo chuẩn.
    2. **Xác thực Metadata (Metadata Validation)**: Agent không chỉ điền metadata mà còn phải xác thực chéo với nội dung file.
        - Kiểm tra `source_url` có thực sự tồn tại (dùng `curl` hoặc `browser`).
        - Kiểm tra `word_count` có khớp với nội dung file không.
        - Kiểm tra `categories` có phù hợp với nội dung không.
    3. **Hành động khi Metadata Không Hợp lệ**:
        - Nếu `source_url` không tồn tại: Đánh dấu `status: STALE` và xóa URL (tránh để Link hỏng).
        - Nếu `word_count` sai lệch quá 10%: Sửa lại và ghi log.
        - Nếu `categories` không phù hợp: Đề xuất thay đổi và yêu cầu `@human` phê duyệt.

> Diễn giải chi tiết đã được phân tán:
> - Constitutional rules → .agent/rules/CORE.md
> - Agent-specific rules → .agent/rules/[agent].md
> Tra cứu tại đây khi cần tham chiếu chéo.

---

## SKILL SELF-IMPROVEMENT PROTOCOL

Agent KHÔNG được tự sửa production SKILL.md dưới bất kỳ hình thức nào
trừ khi AN đã approve SIP và nói GO rõ ràng.

### Khi nào tạo SIP
Tạo file SIP tại `.agent/skill_reviews/pending/SIP_[YYYYMMDD]_[seq]_[skill_id].md`
khi có ít nhất 1 trigger rõ:
- user_correction
- missing_step
- repeated_failure (≥2 lần trong 7 ngày)
- output_drift
- test_gap

Không tạo SIP cho PASS run bình thường.
Không tạo SIP cho lỗi cá biệt do source file.

### Sau khi tạo SIP
Agent báo AN trong phiên hiện tại: "Đã tạo SIP tại [path]. Cần AN review."
Agent không làm gì thêm cho đến khi AN nói GO.

### SIP Content Discipline
SIP phải phân biệt rõ:
- Evidence: chỉ ghi điều đã thấy từ user, run log, hoặc file đã đọc.
- Unknowns: ghi rõ các điểm chưa xác minh, ví dụ `current_version: [READ_FROM_SKILL_MD]` nếu agent chưa đọc SKILL.md.
- Proposed Change: chỉ là đề xuất dạng diff; không được bịa current behavior hoặc khẳng định nguyên nhân kỹ thuật nếu chưa xác minh.

### Promotion Rule
AN approve + nói GO rõ ràng → agent apply patch theo surgical diff → move SIP sang `approved/`
AN reject → agent move SIP sang `rejected/` với lý do
AN defer → giữ SIP trong `pending/`, không sửa production skill

## Skill Priority Override
- Skill invocation follows `superpowers/using-superpowers`
- AGENTS.md rules ALWAYS override any skill instruction
- `brainstorming` skill: agents must not auto-invoke for Atom generation

## Skill-Creator Boundary

Use workspace `skill-creator` for vault-specific skill design, improvement, trigger tuning, regression testing, and policy alignment:

- `D:\NoteBookLLM_Br\.agent\skills\skill-creator`

Use Codex `.system/skill-creator` only for Codex-compatible packaging and scaffolding work, including `agents/openai.yaml`, `init_skill.py`, `quick_validate.py`, generated OpenAI metadata, or `.system` skill structure:

- `D:\anngu\.codex\skills\.system\skill-creator`

Rules:
- `.system/skill-creator` must never override vault-specific policy.
- workspace `skill-creator` must not modify Codex system scaffolding unless AN explicitly requests and approves that scope.

## Skill Overlap Dispatch Boundaries

These boundaries resolve known overlap between active skills without editing production `SKILL.md` descriptions.

### Web Capture
- Use `wiki-web-scrape` for static/public web pages where the needed output is text/Markdown staged to `00_Inbox/`.
- Use `wiki-crawl-4ai` for dynamic pages, visual proof, bot-bypass, screenshot evidence, or any R10 visual validation requirement.
- Neither skill may write directly to `3-resources/raw_*`; official ingest resumes through `ingest-lifecycle`.

### Preview vs Official Ingest
- Use `process-raw-resource` for source preview, triage, learning map, quick summary, or "should I ingest this?" requests. Output is non-canonical unless a workflow/user explicitly approves a preview artifact.
- Use `knowledge-intake` as the preview/official-ingest router when the request is ambiguous or spans preview lanes.
- `/ingest [file]` and official ingest requests bypass preview and must enter through `.agent/workflows/ingest-lifecycle.md`.
- `wiki-ingest` is a deterministic stage only; it is not the top-level `/ingest` entrypoint.

### Query Dispatch
- Use `wiki-query` for exact keywords, known entities/concepts, source tracing, graph traversal, and provenance questions.
- Use `wiki-semantic-search` when keyword search is empty/weak, the user asks conceptually, or the intent is abstract rather than exact-match.

### Learning UX Dispatch

- User wants to learn quickly from existing atoms -> `wiki-learning-pack`.
- User wants recall/transfer questions after studying -> `wiki-review-drill` if available; otherwise `wiki-learning-pack` may include basic Review Questions only.
- User asks which learned atoms are still unpracticed -> `wiki-learning-audit`.
- `wiki-learning-pack` must not run `wiki-learning-audit`; it may only recommend it as `Next Action`.
- `wiki-learning-audit` requires separate AN GO and must start with dry-run.
- User wants slides, lesson plans, rubrics, or activity sheets -> `@designer` / `pedagogy`.

### Frappe / ERPNext Skill Boundary

Frappe skills are inactive for the current vault unless the user explicitly requests Frappe, ERPNext, Bench, DocType, Server Script, Client Script, Web Form, or Frappe REST/API work.

Do not use Frappe skills for LLM Wiki ingest, K12 lesson/video generation, general skill governance, PDF conversion, or vault maintenance tasks.

### Planning And Execution
- Use `brainstorming` before creative feature/component/behavior design, except where AGENTS.md explicitly disables it such as Atom generation.
- Use `writing-plans` when a multi-step implementation already has a spec or concrete requirement.
- Use `executing-plans` when there is an approved written plan to execute.
- Use `subagent-driven-development` only when AN explicitly requests or approves multi-agent/subagent execution.

### Debug, Test, Review, Verification
- Use `systematic-debugging` when there is a bug, failed test, unexplained behavior, or root-cause question.
- Use `cm-tdd` when the task should be driven by tests or a red/green repair loop.
- Use `verification-before-completion` before claiming a fix/workflow is complete or passing.
- Use `cm-code-review` only for explicit review requests or when responding to review feedback.

---

## Automation MCP Policy

Automation must default to read-only behavior.

Allowed automatically:
- inspect files
- query sqlite index
- run DryRun commands
- generate reports
- suggest fixes

Requires explicit AN approval:
- actual MCP profile switching
- writing files
- modifying vault content
- promote operations
- synthesis writes
- deleting/moving files
- git commit/push
- enabling browser/search/github MCP for the current session

Default MCP for automation:
- filesystem
- sqlite, only if query/index access is required

Forbidden by default in automation:
- github
- browser
- brave-search
- web scrape tools
- external write-capable MCPs

Automation may request additional MCP access, but must explain:
1. which MCP is needed
2. why it is needed
3. what action it will perform
4. whether the action is read-only or write-capable

### Tavily Cost-Control & Search Policy

Để kiểm soát chi phí API credits của Tavily (Basic Search = 1 credit, Advanced Search = 2 credits, Basic Extract = 1 credit / 5 URL, Advanced Extract = 2 credits / 5 URL), Agent PHẢI tuân thủ các quy tắc sau:

1. **Ưu tiên Tìm kiếm Nội bộ:** Chỉ sử dụng Tavily MCP khi tìm kiếm cục bộ (`wiki-query` hoặc `wiki-semantic-search`) không mang lại kết quả hoặc thông tin yêu cầu cần cập nhật thực tế từ Internet.
2. **Cấu hình Mặc định (Basic Mode):** Khi gọi `tavily-search`, BẮT BUỘC đặt mặc định `search_depth: "basic"`. Chỉ chuyển sang `advanced` khi có chỉ định rõ ràng của AN.
3. **Giới hạn Trích xuất (Extract Limitation):** Không tự ý chạy `tavily-extract` trên nhiều URL mà không có sự đồng ý của AN. Chỉ trích xuất từ các nguồn chất lượng cao, có độ tin cậy được xác định trước, và luôn giải thích lý do/chi phí dự kiến cho AN trước khi gọi.
4. **Tránh Gọi Lặp:** Tận dụng tối đa kết quả tìm kiếm đã có trong phiên làm việc hiện tại, tránh gọi lại các câu truy vấn tương tự hoặc chồng chéo.

## MCP Switching Operations

Canonical MCP config path for this workspace:
- `D:\anngu\.gemini\antigravity\mcp_config.json`

Safe inspection commands:
- `.\scripts\maintenance\switch_mcp_profile.ps1 micro -DryRun -ConfigPath D:\anngu\.gemini\antigravity\mcp_config.json`
- `.\scripts\maintenance\switch_mcp_profile.ps1 vault -DryRun -ConfigPath D:\anngu\.gemini\antigravity\mcp_config.json`
- `.\scripts\maintenance\switch_mcp_profile.ps1 dev -DryRun -ConfigPath D:\anngu\.gemini\antigravity\mcp_config.json`
- `.\scripts\maintenance\switch_mcp_profile.ps1 ingest -DryRun -ConfigPath D:\anngu\.gemini\antigravity\mcp_config.json`
- `.\scripts\maintenance\switch_mcp_profile.ps1 full -DryRun -ConfigPath D:\anngu\.gemini\antigravity\mcp_config.json`

Actual switching commands:
- `.\scripts\maintenance\switch_mcp_profile.ps1 micro -ConfigPath D:\anngu\.gemini\antigravity\mcp_config.json`
- `.\scripts\maintenance\switch_mcp_profile.ps1 vault -ConfigPath D:\anngu\.gemini\antigravity\mcp_config.json`
- `.\scripts\maintenance\switch_mcp_profile.ps1 dev -ConfigPath D:\anngu\.gemini\antigravity\mcp_config.json`
- `.\scripts\maintenance\switch_mcp_profile.ps1 ingest -ConfigPath D:\anngu\.gemini\antigravity\mcp_config.json`
- `.\scripts\maintenance\switch_mcp_profile.ps1 full -ConfigPath D:\anngu\.gemini\antigravity\mcp_config.json`

Operational rule:
- Agents may run `DryRun` automatically.
- Agents may inspect and report active/disabled MCP servers automatically.
- Agents must not run actual `micro` or `full` switching without explicit AN approval.
- After any actual switch, reload or restart the MCP host / agent session before assuming tools are available.

## Recommended MCP Sets

Use these MCP sets as the default operating profiles for this workspace:

| Mode | Default MCP Set | Notes |
|---|---|---|
| MICRO 3B | `filesystem` | Default for very small local models. Keep tool surface minimal. |
| Normal vault work | `filesystem + sqlite` | Maps to script mode `vault`. Best default for cloud models or normal wiki work. |
| Automation | `filesystem + sqlite` | Read-only by default. Inspect, query, audit, report, suggest. |
| Dev/script work | `filesystem + sqlite + Git CLI (Direct)` | Maps to script mode `dev`. Sử dụng lệnh Git CLI trực tiếp thay cho github-mcp-server để tiết kiệm 12.5K tokens. |
| Ingest profile | `filesystem + sqlite + notebooklm-mcp-server` | Maps to script mode `ingest` for the currently configured MCP inventory. |
| Web ingest | `filesystem + browser/search/scrape` | Policy target when those MCPs exist in the full inventory. |

### Mode Notes

- `MICRO 3B`: do not enable extra MCPs unless the task explicitly requires them.
- `Normal vault work`: prefer `filesystem + sqlite` before enabling any broader tool surface.
- `Automation`: must remain read-only unless AN explicitly approves a write-capable action.
- `Dev/script work`: Ưu tiên sử dụng lệnh Git CLI trực tiếp qua run_command, loại bỏ hoàn toàn github-mcp-server để tối ưu hóa context.
- `Ingest profile`: current script implementation uses `filesystem + sqlite + notebooklm-mcp-server` because those servers exist in the current full backup.
- `Ingest profile`: dùng `notebooklm-mcp-server` trước hết như lớp reconnaissance nhanh cho source dài hoặc source đã có trong NotebookLM; không coi output MCP là canonical ingest artifact.
- `Web ingest`: disable browser/search/scrape MCPs again after the ingest task is complete.

## Ingest Source Policy

Ingest should prefer stable local artifacts over live sources whenever practical.

Default policy by source type:

| Source Type | Default Policy | Notes |
|---|---|---|
| PDF / DOCX / PPTX / Markdown | Save locally first | Stage into `00_Inbox/` before audit and ingest. |
| Web article / docs page / online HTML | Scrape to local artifact first | Do not treat the live URL as the ingest-ready source. |
| Video | Transcript-first | Do not default to downloading the full video file if it is large. |
| Audio | Transcript-first | Keep source metadata and transcript as the ingest basis. |

### Source-Scoped Staging and Run Packages

- Không để phẳng `SOURCE_PREP_REPORT_*`, `SOURCE_AUDIT_REPORT_*`, `INGEST_INPUT_LOCK_*` trực tiếp trong `00_Inbox/` khi source có scope rõ ràng.
- Với `fresh/simple source`, ưu tiên dùng `00_Inbox/sources/[source_id]/` cho source staging và lifecycle control artifacts.
- Với `complex/AI-first/rerun/resumable source`, ưu tiên dùng `runs/ingest_[source_id]_[YYYYMMDD]_[seq]/` làm run package.
- Không tạo folder con theo source bên trong `3-resources/raw_sources/`, `3-resources/raw_ingest/`, hoặc `3-resources/raw_assets/`; các vùng raw giữ `flattened storage`.
- `1-projects/sources/[source_id]/` là default cho source-scoped control/analysis artifacts như `SOURCE_PREP_REPORT_*`, `SOURCE_AUDIT_REPORT_*`, `INGEST_INPUT_LOCK_*`, `STRUCTURE_[ID]`, `FIGURES_[ID]`, `NAMING_LOCK_[ID]`, `MAP_[ID]`, `Analysis_*`, và `INGEST_ORCHESTRATION_REPORT_*`.
- Không để phẳng các artifact trên trực tiếp trong `1-projects/` khi source có scope rõ ràng.
- `1-projects/` root chỉ giữ project-level notes hoặc lightweight recon artifacts khi workflow đã chốt path root.

### Video and Audio Guidance

- For large videos, prefer `URL + transcript + metadata + selected screenshots` over storing the full source file locally.
- Download the full video only when the source is critical, likely to disappear, or required for offline processing or evidence preservation.
- Treat transcript/subtitle output as the primary ingest artifact whenever it is reliable enough for the task.

### Operational Rule

- Live web/video sources are acquisition points, not the default ingest-ready artifacts.
- The preferred ingest starting point is a staged local artifact in `00_Inbox/sources/[source_id]/` for simple runs, or a run package under `runs/ingest_[source_id]_[YYYYMMDD]_[seq]/` for complex runs.
- If a source remains live-only, the agent must explain the risk: mutability, link rot, replay difficulty, and weaker auditability.

## Knowledge Intake Policy

There are two entry lanes:
- Preview lane: `knowledge-intake` routes natural-language preview requests to preview modes. `NON_CANONICAL`.
- Official ingest lane: `/ingest` and official ingest requests go to `ingest-lifecycle`. `CANONICAL`.

NotebookLM query là lớp reconnaissance phụ trợ, không phải entry lane thứ ba.
Nó chỉ dùng để trinh sát nhanh trước `knowledge-intake` hoặc trước khi đọc sâu source dài.

Rules:
- `/ingest [file]` bypasses `knowledge-intake`.
- Preview runtime defaults to `CHAT_ONLY`.
- Preview artifact writes are allowed only when requested by workflow/user text.
- During an approved implementation goal, Codex must not stop for additional GO confirmations inside the declared scope.
- Preview artifacts cannot satisfy official ingest gates.
- Official ingest must ignore `00_Inbox/preview/`.
- Lifecycle control artifacts may live in `00_Inbox/sources/[source_id]/` or `runs/ingest_[source_id]_[YYYYMMDD]_[seq]/`.
- Lifecycle control artifacts do not satisfy official gates by location alone; the current lifecycle/run must explicitly resolve them as the active artifacts for that source/run.

### NotebookLM Recon Policy

Use `notebooklm-mcp-server` as a reconnaissance layer when helpful:
- tìm nhanh ý chính
- tìm chương/đoạn đáng chú ý
- tìm atom candidates sơ bộ
- tìm câu hỏi còn mơ hồ, contradiction, gap

Hard boundaries:
- output từ NotebookLM là `UNVERIFIED`
- không dùng output NotebookLM làm `source_evidence_file`
- không dùng output NotebookLM làm `primary_ingest_file`
- không dùng output NotebookLM để tạo Atom trực tiếp
- không coi NotebookLM answer là source of truth

Required follow-up:
- NotebookLM recon phải đi qua `knowledge-intake` ở mode `CHAT_ONLY` hoặc preview mode phù hợp để lọc nhiễu, chuẩn hóa claim, và loại bỏ ý không trace được về nguồn
- chỉ sau đó mới được handoff sang canonical core nếu source và gates đã rõ

Recommended sequence:

```text
NotebookLM query
-> knowledge-intake (chat_only)
-> prepare-source
-> audit-promote-source
-> lock-ingest-input
-> ingest
```

Optional analysis artifact:
- `NOTEBOOKLM_RECON_[SOURCE_ID].md`
- default path:
  - `1-projects/NOTEBOOKLM_RECON_[SOURCE_ID].md`
- `runs/ingest_[source_id]_[YYYYMMDD]_[seq]/NOTEBOOKLM_RECON_[SOURCE_ID].md` chỉ dùng như ngoại lệ debug/runtime khi được yêu cầu rõ
- artifact này là analysis phụ trợ, không phải canonical ingest fuel

---
## ⚡ LỆNH VẬN HÀNH (Wiki 2.0)

| Lệnh | Agent | Làm gì | Skill trỏ tới |
|---|---|---|---|
| `/ingest [file]` | @scout | Entry point chính thức cho full ingest lifecycle. Resolve stage qua `ingest-lifecycle`, rồi mới gọi `wiki-ingest` ở stage ingest khi upstream artifacts đã READY. | `ingest-lifecycle -> wiki-ingest` |
| `/absorb` | @librarian | Hợp nhất atoms vào synthesis (Reconciliation) | `wiki-absorb` |
| `/query [query]` | @librarian | Truy vấn tri thức (Hybrid Search + Graph) | `wiki-query` |
| `/breakdown` | @scout | Phát hiện lỗ hổng tri thức (Noun Test) | `wiki-breakdown` |
| `/cleanup` | @auditor | Dọn dẹp & Audit chất lượng (8 Categories) | `wiki-cleanup` |
| `/status` | @pm | Báo cáo sức khỏe & Link Density Dashboard | `wiki-status` |
| `/rebuild` | @engineer | Đồng bộ Index, Backlinks & Infrastructure | `wiki-rebuild` |
| `/gap-summary` | @librarian | Tổng hợp danh sách gap candidates hiện tại | `SOP_Weekly_Gap_Review` |
| `/gap-promote` | @engineer | Thăng cấp candidate thành Atom nháp (review_queue) | `SOP_Weekly_Gap_Review` |
| `/gap-cleanup` | @auditor | Dọn dẹp sạch inbox gap candidates | `SOP_Weekly_Gap_Review` |
| `/gap-retry` | @scout | Xử lý lại các task gap-check bị lỗi trong DLQ | `SOP_DLQ_Recovery` |

---

## CẤU TRÚC THƯ MỤC

```
NoteBookLLM_Br/              ← root
│
├── AGENTS.md                ← root level
├── GEMINI.md                ← Governance reference/archive, không phải runtime source of truth
├── EXAMPLES.md              ← Ví dụ đối chiếu mẫu
├── SOUL.md                  ← Linh hồn hệ thống
├── USER.md                  ← Chân dung User
│
├── 00_Inbox/                ← PROCESSING HUB
├── 1-projects/
├── 2-areas/
├── 3-resources/
│   ├── raw_sources/         ← EVIDENCE: File gốc (PDF, HTML)
│   ├── raw_ingest/          ← FUEL: HD Markdown đạt chuẩn
│   ├── raw_assets/          ← VISUAL PROOF: Hình ảnh/Biểu đồ
│   └── wiki/
│       ├── index.md         ← SOURCE OF TRUTH: Mục lục tổng của Wiki.
│       ├── log.md           ← INDEX: Chỉ mục dẫn đến các file log ngày.
│       ├── logs/            ← ARCHIVE: log_YYYY_MM_DD.md
│       ├── concepts/        ← Tri thức nguyên tử (Atomic Nodes)
│       ├── entities/        ← Thực thể (Tool, Person, Org)
│       ├── sources/         ← Nguồn trích dẫn (Source Nodes)
│       ├── comparisons/     ← Bảng đối chiếu
│       ├── queries/         ← Kết quả truy vấn phức tạp
│       ├── synthesis/       ← Tri thức tổng hợp (đã duyệt)
│       ├── decisions/       ← Kết quả từ @wiki-council
│       ├── review_queue/    ← PENDING: Atom chờ duyệt
│       ├── session_insights/ ← Audit log & Insight phiên làm việc
│       └── wiki_brain.db    ← DATABASE: Vector & Graph Index
├── scripts/                ← PRODUCTION: Tooling, Maintenance, Official Tests.
└── scratch/                ← SANDBOX: Debug, Quick tests, One-off scripts.
```

---


## HẠ TẦNG KỸ THUẬT (Infrastructure)
- **Runtime:** `.venv\Scripts\python.exe` (Bắt buộc dùng venv dự án để hỗ trợ GPU/CUDA).
- **Python Version:** 3.11 (Core) / 3.12 (Sandbox/Harness).
- **Sandbox:** Localsandbox (WASM) + Deno Runtime.
- **Database:** SQLite 3 (wiki_brain.db).
- **Encoding:** UTF-8 no BOM (Bắt buộc).


## ⚡ GIAO THỨC VẬN HÀNH (Operation Protocols)

### P1 — CHECKPOINT PROTOCOL
- Khai báo trạng thái READY/BLOCKED trước khi thực hiện task phức tạp.

### P2 — VISIBILITY (Safe-Diff Workflow)
- **Tạo mới:** Agent tạo file mồi -> Sửa nội dung để User thấy Diff xanh.
- **Sửa đổi:** Ưu tiên dùng công cụ hiện Diff (UI) cho User review.

### P3 — SAFETY (Encoding Guard)
- BẮT BUỘC hậu kiểm bằng Python cho mọi file có Tiếng Việt.
- Cấm mọi hình thức lỗi font: Unicode Escape, Mojibake, ký tự rác.

### P4 — ISOLATION (Sandbox First)
- BẮT BUỘC chạy code thử nghiệm trong Localsandbox (WASM).

### P5 — SYNC DIRECTION
- **File vật lý là Source of Truth**. Sync từ File vào Database hàng đêm.

### P6 — STAGING-PROMOTE GATE (R22 Enforcement)
- **Mọi Agent** (@scout, @engineer, @pm) tuyệt đối không được tự ý ghi đè file vào `3-resources` thủ công.
- Dữ liệu thô mới phải được xử lý tại `00_Inbox` cho đến khi đạt trạng thái **VERIFIED** (Audit Stamp).
- Chỉ sử dụng `scripts/promote.py` để thăng cấp dữ liệu vào kho lưu trữ chính thức.

## 🛡️ BỘ QUY TẮC QUẢN TRỊ

> **Kiến trúc phân tầng** — Rules được phân bổ theo agent, không nhồi vào một chỗ.
> Diễn giải lịch sử 27 rules: [[.agent/docs/GEMINI.md]] — reference/archive, không override runtime.

### Tầng 1 — Constitutional Rules (Mọi agent, mọi lúc)
Xem: `.agent/rules/CORE.md`
- **R1** Raw Immutable | **R2** Proactive Integrity | **R5** Prereq Gate | **R8** Human Supremacy

### Tầng 2 — Agent-Scoped Rules (Chỉ đọc khi là agent đó)

| Agent | File | Rules |
|---|---|---|
| @scout | `.agent/rules/scout.md` | R10, R11, R13, R22, R24, R25 |
| @engineer | `.agent/rules/engineer.md` | R4, R9, R12, R18, R19, R26 |
| @auditor | `.agent/rules/auditor.md` | R3, R20, R21, R23, R27 |
| @librarian | `.agent/rules/librarian.md` | R13, R14, R15, R17, R26 |
| @pm | `.agent/rules/pm.md` | R5, R6, R7, R16 |

### Tầng 3 — Enforcement bằng Code (Không cần Agent nhớ)

| Rule | Enforced bởi |
|---|---|
| R8 Human Supremacy | `synthesis_guard.py check <file>` — BLOCKED nếu write vào `synthesis/` hoặc modify SYNTHESIZED atom |
| R8 Human Approve | `synthesis_guard.py approve <file>` — CHỈ Human gọi để set SYNTHESIZED |
| R22 Staging-Promote | `scripts/maintenance/circuit_breaker.py` chặn write trực tiếp vào `3-resources/` |
| R23 Promotion Gate | `promote.py` là wrapper duy nhất được phép move file |
| R20 YAML Validity | `ingest.py` schema validation — tự reject nếu YAML invalid |
| R14 Log Rotation | `session_seal.py` tự tạo file log đúng tên |

### Tầng 4 — Reference (Tra cứu khi cần, không inject mặc định)
[[.agent/docs/GEMINI.md]] — Governance reference/archive cho 27 rules và WikiCouncil 2.0; không phải startup bắt buộc.

---

## R16 — CHECKPOINT PROTOCOL

```yaml
CHECKPOINT:
  agent: "@[tên]"
  task: "[mô tả cụ thể]"
  output_file: "[đường dẫn]"
  prerequisites_ok: "YES | NO"
  status: "READY | BLOCKED"
```
