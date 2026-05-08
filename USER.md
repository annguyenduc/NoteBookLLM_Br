# USER.md
> Machine-readable execution constraints — tiêm vào mọi LLM call

---

## identity

```yaml
name: AN
role: Instructional Designer / AI-ML Curriculum Developer
organization: XXXX Education
focus: Teacher training programs — AI/ML và STEAM education (K-12)
platform: Antigravity IDE + Obsidian (NoteBookLLM_Br vault)
```

---

## expertise

```yaml
primary_domains:
  - AI pedagogy (K-12, teacher-facing)
  - Instructional design (Bloom's Taxonomy, Backward Design, EDP)
  - STEAM curriculum development
  - Agent-based workflows (Antigravity, Claude Code)

secondary_domains:
  - LLM tooling (Claude, Antigravity, Codex)
  - Knowledge management systems (Obsidian, SQLite)

frameworks_in_use:
  - Bloom's Taxonomy
  - Engineering Design Process (EDP)
  - UNESCO AI Competency Framework
  - ISTE Standards
  - CRISP-DM
  - Backward Design (UbD)
```

---

## wiki_usage

```yaml
primary_goal: Lưu trữ và tra cứu kiến thức cá nhân
secondary_goal: Học thêm kiến thức mới — wiki là công cụ học tập tích lũy, không chỉ lưu trữ
vault_structure: PARA (Projects/Areas/Resources/Archive)
daily_workflow:
  - Ingest tài liệu nghiên cứu AI mới
  - Query vault khi thiết kế curriculum
  - Review queue hàng tuần (Human Gate)
  - Promote insights từ chat session lên Atoms

learning_stance:
  mode: active         # đang chủ động mở rộng kiến thức, không chỉ consolidate
  domains_expanding:
    - AI engineering (từ pedagogy sang technical depth)
    - Agent-based systems và multi-agent workflows
    - Knowledge management systems
    - Vibe coding và solo developer workflows
  principle: >
    Wiki phải phản ánh quá trình học — Atoms mới từ học tập được đánh dấu learning_source để phân biệt với kiến thức đã được kiểm chứng qua thực hành
---

## output_constraints

```yaml
format: Đa dạng tùy context
rules:
  - Nếu output là concept/definition → atomic, có thể link được
  - Nếu output là so sánh → bảng biểu
  - Nếu output là quy trình → sơ đồ hoặc numbered steps 
  - Nếu output là code/script → sẵn sàng chạy, có --dry-run flag
  - Nếu output là tài liệu đào tạo → phân biệt rõ teacher-facing vs student-facing

language: Tiếng Việt cho ghi chú cá nhân, tiếng Anh cho technical terms
length: Súc tích — nếu có thể nói trong 3 dòng thì không dùng 10 dòng
confidence_display: Luôn hiển thị source khi trả lời từ vault (R3)
```

---

## solution_space_limits

```yaml
# Agent chỉ được sinh output trong giới hạn này
scope_filter:
  - Ưu tiên context K-12 và teacher training trước khi mở rộng
  - Không generate curriculum content mà không có pedagogical framework dẫn đường
  - Không suggest tool mới nếu Antigravity + Obsidian đã đủ làm việc đó

avoid:
  - Generic AI chatbot responses không có grounding trong vault
  - Overconfident claims về AI/ML concepts chưa có trong vault
  - Tự động tạo Synthesis mà không có human rewrite

tool_overrides:
  - DO NOT use: "sub_browser" for reading content from URLs.
  - MUST use: "wiki-web-scrape" (Lightpanda) or "wiki-crawl-4ai" for any URL processing.
  - Reason: Web content must be staged as Markdown in 00_Inbox/ for auditing before atom creation.
```

---

## current_projects

```yaml
active:
  - NoteBookLLM_Br: Build Second Brain V3.1 và vận hành nó như công cụ học tập chính - tích lũy kiến thức có cấu trúc, giảm thời gian research lặp lại, tăng tốc độ nắm bắt lĩnh vực mới

context_for_agent:
  - Mục tiêu tối thượng: vault phải giúp học nhanh hơn, không phải lưu nhiều hơn
  - Khi query liên quan đến wiki system → tham chiếu kiến trúc V3.1
  - Khi query là kiến thức mới đang học → label Atom với learning_source=true, confidence tự động giảm 0.1 so với nguồn đã kiểm chứng, ưu tiên đưa vào review queue để bản thân verify qua thực hành
  - Ưu tiên connections giữa các Atom hơn là tạo Atom mới — learning xảy ra tại điểm giao nhau giữa kiến thức cũ và mới
  - Khi hỏi về workflow hoặc agents → luôn trả lời theo "Vibe Coding" style, sử dụng Antigravity như "AI pair programmer" và vault như "shared brain", không dùng ngôn ngữ corporate hoặc academic quá khô khan
```

---

## review_preferences

```yaml
weekly_review:
  day: Cuối tuần
  max_items: 10 atoms/lần
  rewrite_required: true      # SYNTHESIZED chỉ sau khi tự viết lại
  defer_allowed: true         # PENDING giữ nguyên nếu chưa sẵn sàng

conflict_resolution:
  auto_resolve_threshold: 0.85
  ambiguous_action: invoke wiki-council → flag decisions/
  human_decision_required: true khi council không resolve được
```
