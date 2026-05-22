# SPEC — NoteBookLLM_Br
## Personal Knowledge Acceleration System
> Version: 1.2 | Date: 2026-05-13 | Status: ACTIVE
> Author: AN | Schema: v7.0 (Knowledge OS + Kernel Bridge)

---

## PHẦN 1 — BỐI CẢNH & MỤC TIÊU

### 1.1 Vấn đề cần giải quyết

Học một kỹ năng hoặc lĩnh vực mới mất nhiều thời gian vì:
- Tài liệu dài (200-400 trang), đọc tuần tự tốn kém
- Kiến thức không có cấu trúc → khó tra cứu khi cần
- Học xong quên → phải đọc lại từ đầu
- Không biết mình đang thiếu kiến thức ở đâu

### 1.2 Mục tiêu hệ thống

Xây dựng "trí nhớ thứ hai" (Second Brain) giúp người dùng:
- Học nhanh hơn so với học bình thường
- Tra cứu kiến thức chính xác, có nguồn gốc rõ ràng
- Phát hiện gap kiến thức chủ động
- Scale được cho người khác khi cần

### 1.3 Triết lý cốt lõi

```
Vault phải giúp học nhanh hơn — không phải lưu nhiều hơn.
Connections giữa các Atom quan trọng hơn số lượng Atom.
Human gate là bắt buộc — AI chỉ đề xuất, người dùng quyết định.
```

### 1.4 Người dùng

- **Hiện tại:** Solo user (AN) — Instructional Designer, AI/STEAM K-12
- **Tương lai:** Scale ra cho người dùng khác khi hệ thống đủ ổn định

---

## PHẦN 2 — KIẾN TRÚC TỔNG THỂ

### 2.1 Mô hình tư duy

Hệ thống lấy cảm hứng từ hai nguồn:
- **Karpathy LLM Wiki** — hierarchical notes, semantic linking,
  distilled understanding, retrieval-first
- **PARA Method** — Projects / Areas / Resources / Archives

Kết quả là một **Cognitive Infrastructure**:
không phải coding workspace, không phải note-taking app,
mà là knowledge operating system.

### 2.2 Pipeline tổng thể (5 tầng)

```
[INPUT] Tài liệu thô (PDF, HTML, URL)
     ↓
[TẦNG 1] Cách ly & Chuyển đổi (00_Inbox)
   hd_converter.py → md_auditor.py → promote.py
   (Check: Audit Stamp + UTC Timestamp)
     ↓
[TẦNG 2] Lưu trữ & Đăng ký (3-resources)
   raw_sources/ + raw_ingest/ + raw_assets/
   ingest-lifecycle → wiki-ingest stage → Atoms (DRAFT)
     ↓
[TẦNG 2.5] Local AI Audit (Gap-Check)
   @scout + gemma3:4b → gap_candidates/
   DLQ: 00_Inbox/failed_queue/ (retry-able)
     ↓
[TẦNG 3] Hợp nhất & Xung đột
   wiki-absorb → review_queue/ hoặc wiki-council
     ↓
[TẦNG 4] Human Governance (R8 Enforcement) ★
  Human Review → VERIFIED → [synthesis_guard.py] → SYNTHESIZED
     ↓
[TẦNG 5] Bảo trì
   wiki-rebuild → wiki-cleanup → wiki-status
     ↓
[OUTPUT] Obsidian PARA Vault — tri thức có thể tra cứu
```

### 2.3 Vault Structure

```
NoteBookLLM_Br/
│
├── 00_Inbox/                  ← QUARANTINE ZONE
│   ├── Converted_Sources/     ← PDF → MD staging
│   ├── gap_candidates/        ← Local AI audit output
│   ├── failed_queue/          ← Dead-Letter Queue (DLQ)
│   └── _deprecated/
│
├── 1-projects/                ← Active work
├── 2-areas/                   ← Ongoing domains
│
├── 3-resources/               ← SOURCE OF TRUTH
│   ├── raw_sources/           ← Original files (IMMUTABLE)
│   ├── raw_ingest/            ← Audited markdown (FUEL)
│   ├── raw_assets/            ← Images/diagrams
│   └── wiki/
│       ├── concepts/          ← Atomic knowledge nodes
│       ├── entities/          ← Tools, people, orgs
│       ├── sources/           ← Source citation nodes
│       ├── comparisons/       ← Side-by-side analysis
│       ├── synthesis/         ← Verified synthesis (human-only)
│       ├── review_queue/      ← Pending human review
│       ├── decisions/         ← Wiki council verdicts
│       ├── queries/           ← Complex query results
│       └── session_insights/  ← Session audit logs
│
├── 4-archive/                 ← Permanent storage
├── .agent/skills/             ← Agent skill library
├── .kiro/                     ← Circuit breaker & error logs
│
├── AGENTS.md                  ← Runtime source of truth cho agent
├── GEMINI.md                  ← Governance reference/archive, không phải runtime source of truth
├── SOUL.md                    ← System soul, chỉ đọc khi task cần định hướng triết lý
├── USER.md                    ← User profile, chỉ đọc khi task cần cá nhân hóa
└── WORKSPACE_OVERVIEW.md      ← Architecture map, đọc theo startup profile
```

---

## PHẦN 3 — HARDWARE & RUNTIME

### 3.1 Hardware

```
Machine:  Acer Nitro 5
CPU:      Intel i7-11400h (6 cores)
RAM:      32GB
GPU:      GTX 1650, 4GB VRAM
Storage:  100GB SSD available
OS:       Windows 11
```

### 3.2 Constraints

- **VRAM:** Chỉ chạy 1 local model tại một thời điểm
- **Context:** gemma3:4b comfortable ở 4K-8K tokens thực tế
- **Encoding:** UTF-8 no BOM bắt buộc toàn hệ thống
- **Runtime:** Python 3.11 (Core) / 3.12 (Sandbox)

### 3.3 Local Model Stack

| Model | Vai trò | VRAM | Status |
|---|---|---|---|
| gemma3:4b | Gap-check chính | ~2.5GB | ✅ Primary |
| phi3:mini | Structured reasoning | ~2.2GB | ✅ Available |
| qwen3:4b | Synthesis, tiếng Việt | ~2.5GB | ⚠️ RAM leak |
| llama3.2:3b | General fallback | ~2.0GB | ✅ Available |
| qwen2.5:3b | Multilingual | ~1.9GB | ✅ Available |

**Rule:** `OLLAMA_MAX_LOADED_MODELS=1`

### 3.4 Search Layer

**qmd** (github.com/tobi/qmd) — CLI search engine chạy local:
- BM25 full-text + Vector semantic + LLM re-ranking
- Models riêng (~2GB): embeddinggemma-300M + qwen3-reranker
- Chạy độc lập, không conflict VRAM với Ollama
- Dùng cho `wiki-semantic-search` skill

---

## PHẦN 4 — AGENT SYSTEM

### 4.1 Agent Roster

| Agent | Trigger | Vai trò |
|---|---|---|
| @pm | Kế hoạch, phân task | Quản lý pipeline |
| @scout | Nghiên cứu, phân tích raw | Tạo Scout Analysis |
| @engineer | Viết code, tạo atoms | Thực thi task |
| @librarian | Quản lý wiki, synthesis | Cập nhật index |
| @auditor | Kiểm định nguồn, lint | Reverse tracing |
| @designer | Thiết kế learning sequence | Cần Trainer Profile |
| @healer | Sửa lỗi link, rollback | Khắc phục vi phạm |

### 4.2 IDE Stack

| Vai trò | Tool | Lý do |
|---|---|---|
| IDE chính | Antigravity Pro | Gemini quota, Skills system |
| Local inference | Ollama REST API | Direct call, 0 cost |
| Complex tasks | Kiro + Claude Sonnet | Có chủ đích, tốn credit |
| Vault UI | Obsidian | Graph view, wikilinks |
| Semantic search | qmd CLI / MCP | Standalone, no conflict |

### 4.3 Startup Protocol

Runtime startup được định nghĩa trong `AGENTS.md`.

```yaml
1. Chọn startup profile: MICRO | NORMAL | FULL
2. Đọc đúng các file theo profile
3. Chọn đúng active role
4. Khai báo CHECKPOINT cho task phức tạp
5. Với side effect: cần AN GO trước khi thực thi
6. Sau side effect: ghi log vào 3-resources/wiki/logs/log_YYYY_MM_DD.md
```

Không inject mặc định: `GEMINI.md`, `SOUL.md`, `USER.md`, `SKILLS_INDEX.md`, skill dài, log lịch sử.

---

## PHẦN 5 — PIPELINE CHI TIẾT

### 5.1 Ingest Flow (Standard)

```
Bước 1 — HD Convert
  python hd_converter.py "00_Inbox/[FILE].pdf" --chunk-size 15
  Engine: Docling (PDF có bảng/hình) hoặc pymupdf4llm (text-only)
  Output: 00_Inbox/Converted_Sources/[SOURCE]/

Bước 2 — Audit
  python md_auditor.py "00_Inbox/Converted_Sources/[SOURCE]/" --fix
  Đóng dấu Audit Stamp (audit_stamp: true + UTC timestamp) (R21)

Bước 3 — Promote (Gate 1)
  python .kiro/circuit_breaker.py promote ...
  Chỉ dùng promote.py — KHÔNG dùng Move-Item hoặc move_file (R23: Promotion Gate)
  PDF → raw_sources/
  MD  → raw_ingest/
  IMG → raw_assets/

Bước 4 — Register (Kernel Bridge Gate)
  Official `/ingest` must resolve through `ingest-lifecycle`
  Direct `ingest.py` invocation is stage-level only after upstream artifacts are READY
  BẮT BUỘC: audit_stamp=true. Đăng ký vào wiki_brain.db, tạo Atom type=source, status=DRAFT

Bước 5 — Scout Analysis (loop mỗi chunk 800-1000 dòng)
  @scout đọc chunk → Gemini extract atoms
  @engineer tạo file .md → 3-resources/wiki/review_queue/
  gap_check.py → gemma3:4b → 00_Inbox/gap_candidates/
  (Failure → 00_Inbox/failed_queue/ + retry_command)
  User xem qua Obsidian

Bước 6 — Human Gate
  Review atoms + gap_candidates cùng lúc
  Merge → approve → promote lên concepts/ hoặc entities/

Bước 7 — Absorb & Sync
  wiki-absorb → reconcile với vault
  wiki-rebuild → sync filesystem → DB
  obsidian reload (R15)
```

### 5.2 Large Document Strategy (200-400 trang)

```
Pass 1 — Global scan (Gemini Flash)
  Đọc toàn bộ → tạo bản đồ cấu trúc (~1-2 trang)
  Inject vào system prompt của mọi chunk sau
  Mục đích: giữ global context, tránh mất cross-chapter connections

Pass 2 — Chunk detail (loop)
  Chunk size: 800-1000 dòng / ~3,000-4,000 tokens
  Overlap: 200 tokens
  Gemini Pro: extract atoms (primary)
  gemma3:4b: gap-check (secondary, non-blocking)

Pass 3 — Cross-chunk synthesis
  phi3:mini: tìm connections bị miss giữa chunks
```

### 5.3 Atom Lifecycle

```
DRAFT       ← Agent tạo sơ khởi (mặc định)
    ↓
VERIFIED    ← Pass audit + source tracing
    ↓
SYNTHESIZED ← CHỈ Human được set (R8 Enforcement: Blocked for Agents)
```

---

## PHẦN 6 — LOCAL AI AUDIT LAYER (Gap-Check)

### 6.1 Mục đích

Gemini ingest mỗi chunk thường extract 10-15 atoms.
Gap-check dùng local model làm "second opinion" để giảm miss rate.

### 6.2 Vai trò theo giai đoạn

| Giai đoạn | atoms input | Vai trò thực tế |
|---|---|---|
| Lần ingest đầu | [] hoặc ít | Parallel extraction độc lập |
| Ingest tiếp theo | Có atoms trước | Gap-check thực sự |

### 6.3 gap_check.py Spec

**Vị trí:** `.agent/skills/wiki-ingest/scripts/gap_check.py`

**Interface:**
```bash
python gap_check.py \
  --chunk <file_path>          # Path đến chunk file
  --chunk-text <text>          # Hoặc text trực tiếp
  --atoms <json_array>         # ["atom1", "atom2"]
  --source <name>              # Tên source
  --chunk-num <n>              # Số thứ tự chunk
  --skip-gap-check             # Bypass hoàn toàn
```

**Config:**
```python
GAP_MODEL   = "gemma3:4b"      # env: GAP_CHECK_MODEL
TIMEOUT_SEC = 60
options = {
    "temperature": 0.2,
    "num_predict": 1024,
    "num_ctx": 4096,           # ← Pending fix
}
chunk_preview = chunk_text[:6000]  # ~1500 tokens
```

**Output format:**
```
00_Inbox/gap_candidates/<source>_gap_<n>.md
---
source: <source>
chunk: <n>
date: YYYY-MM-DD
model: gemma3:4b
status: PENDING_REVIEW
---
## Candidates bị bỏ sót
- [Concept] Name: Description
- [Mental Model] Name: Description

**DLQ (failed_queue):**
Nếu Ollama lỗi hoặc crash, script lưu trạng thái vào `.failed` file.
Retry command: `python gap_check.py --retry-failed <path>`
```

**Error handling (non-blocking):**
- Ollama offline → WARNING, exit 0
- Timeout → WARNING, exit 0
- JSON invalid → WARNING, dùng []
- File not found → WARNING, exit 0

### 6.4 Governance Rules (R24-R27)

**R24 — Trigger Manual:**
@scout PHẢI gọi gap_check.py thủ công sau mỗi chunk,
trước khi báo "User Approved".

**R25 — Non-blocking:**
Nếu Ollama offline hoặc gemma3:4b lỗi → WARNING + tiếp tục.
CẤM block pipeline chính.

**R26 — Human-in-the-Loop:**
gap_candidates/ chỉ dành cho Human Review.
@engineer không dùng output này nếu chưa có Human approve.

**R27 — Scope Isolation:**
CHỈ dùng cho DRAFT atoms.
KHÔNG dùng cho synthesis/ hoặc verified content.

### 6.5 Weekly Review SOP

```
/gap-summary    → @librarian tổng hợp danh sách candidates
/gap-promote    → @engineer thăng cấp candidate → review_queue/
/gap-cleanup    → @auditor dọn dẹp inbox
/gap-retry      → @scout xử lý lại DLQ (failed_queue)
```

---

## PHẦN 7 — HIẾN PHÁP (R1-R27 Summary)

### Nhóm I — Quản trị

| Rule | Tên | Nguyên tắc |
|---|---|---|
| R1 | Raw Immutable | raw_*/ là vùng cấm — chỉ scripts chính thức được ghi |
| R2 | Proactive Integrity | Log trước khi làm — cấm báo cáo ảo |
| R3 | Source Tracing | Mọi tri thức phải có nguồn vật lý |
| R4 | Structure & Encoding | Python UTF-8, surgical diff, cấm tạo file ở root |
| R5 | Prereq Gate | Plan → User duyệt → Execute |

### Nhóm II — Thực thi

| Rule | Tên | Nguyên tắc |
|---|---|---|
| R6 | Phased Execution | Xong Phase 1 mới viết Skill |
| R7 | Stress Testing | Test với dữ liệu thực trước khi deploy |
| R8 | Human Supremacy | Chỉ Human set SYNTHESIZED (Enforced via synthesis_guard.py TTY Gate) |
| R9 | Surgical Min | Chỉ thay đổi tối thiểu |
| R10 | Strict URL Ingestion | CẤM sub_browser — BẮT BUỘC wiki-web-scrape/crawl-4ai → 00_Inbox trước |

### Nhóm III — Dữ liệu

| Rule | Tên | Nguyên tắc |
|---|---|---|
| R11 | Density Filter | Bỏ file < 200 bytes; đánh giá Knowledge Density |
| R12 | Example Adherence | Đối soát EXAMPLES.md trước khi code |
| R13 | Atom Lifecycle | Mọi atom mới = DRAFT |
| R14 | Log Rotation | Log theo ngày: log_YYYY_MM_DD.md |
| R15 | Peer-layer Sync | obsidian reload sau mỗi metadata change |
| R16 | Checkpoint | Khai báo READY/BLOCKED trước task |
| R17 | Sync Direction | File vật lý = Source of Truth |
| R18 | Double Examples | Mỗi Atom có 2 ví dụ (Original + Pedagogical) |
| R19 | Sandbox Protocol | Code mới chạy WASM trước |
| R20 | YAML Validity | Dấu : trong metadata phải có ngoặc kép |
| R21 | Self-Auditing Gate | Pass audit_raw_ingest.py trước khi vào raw_ingest/ |
| R22 | Staging-Promote | 00_Inbox → promote.py → 3-resources |
| R23 | Promotion Gate | CẤM move_file/Move-Item — CHỈ dùng promote.py |

### Nhóm IV — Local AI Audit

| Rule | Tên | Nguyên tắc |
|---|---|---|
| R24 | Local AI Audit — Trigger | @scout gọi gap_check.py sau mỗi chunk, trước khi báo Approved |
| R25 | Local AI Audit — Non-blocking | Ollama offline không block pipeline |
| R26 | Local AI Audit — Human Gate | gap_candidates chỉ là gợi ý, không tự promote |
| R27 | Local AI Audit — Scope Isolation | Gap-check chỉ cho DRAFT atoms |

---

## PHẦN 8 — SKILL REGISTRY

| Skill | Script | Path | Input | Output |
|---|---|---|---|---|
| wiki-hd-convert | hd_converter.py | .agent/skills/wiki-hd-convert/scripts/ | PDF | 00_Inbox/Converted_Sources/ |
| wiki-md-auditor | md_auditor.py | scripts/maintenance/ | MD | Audit Stamp |
| Promotion | promote.py | scripts/maintenance/ | Inbox | raw_*/ |
| circuit-breaker | circuit_breaker.py | .kiro/ | Process | error_log.md |
| synthesis-guard | synthesis_guard.py | scripts/maintenance/ | Atom write request | Guard Verdict + auto-revert |
| wiki-ingest | ingest.py | .agent/skills/wiki-ingest/scripts/ | prepared ingest artifact / raw_ingest stage input | Atoms DRAFT |
| gap-check | gap_check.py | .agent/skills/wiki-ingest/scripts/ | Chunk + Atoms | gap_candidates/ |
| wiki-absorb | absorb.py | .agent/skills/wiki-absorb/ | Atoms | review_queue/ |
| wiki-council | council.py | .agent/skills/wiki-council/ | Conflict | decisions/ |
| wiki-rebuild | rebuild.py | scripts/ | Vault | wiki_brain.db |
| wiki-cleanup | cleanup.py | scripts/ | Vault | Fixed links |
| wiki-status | status.py | scripts/ | DB | Dashboard |
| vram-guard | vram_guard.py | scripts/maintenance/ | Atomic Lock | Resource isolation |
| wiki-query | query.py | .agent/skills/wiki-query/ | Query | Results |
| wiki-semantic-search | qmd CLI | Standalone (PATH) | Query | Semantic results |

---

## PHẦN 9 — KNOWN ISSUES & ROADMAP

### 9.1 Known Issues

| Issue | Severity | Status |
|---|---|---|
| num_ctx chưa set trong gap_check.py | ✅ Fixed | Đã set num_ctx: 4096 |
| synthesis_guard.py Layer 0 fix | ✅ Fixed 2026-05-12 | Extended scan toàn wiki/ + auto-revert unauthorized SYNTHESIZED |
| Docling non-deterministic (VRAM contention) | 🔴 High | Workaround: đóng Ollama trước |
| qwen3:4b RAM leak trên GTX 1650 | 🟡 Medium | Replaced by gemma3:4b |
| nomic-embed-text redundant (qmd đã handle) | 🟢 Low | Optional cleanup |
| Visual atom pipeline chưa có | 🟡 Medium | Phase 6 |

### 9.2 Docling Fix (Pending)

```python
# Trong hd_converter.py — detect PDF type trước khi fallback
def has_tables(pdf_path) -> bool:
    doc = pymupdf.open(pdf_path)
    for page in doc:
        if page.find_tables().tables:
            return True
    return False

# Logic:
# has_tables=True + docling fail → ESCALATE (không fallback pymupdf)
# has_tables=False → pymupdf4llm fallback OK
```

### 9.3 Roadmap

```
Phase 1-4   ✅ Core pipeline (done)
Phase 5     ✅ Local AI Audit Layer (done)
Phase 6     📋 Visual Atom Pipeline
               (tables, diagrams từ docling output)
Phase 7     📋 Cross-chunk synthesis automation
Phase 8     📋 Multi-user scaling
```

---

## PHẦN 10 — CÁCH ĐỌC SPEC NÀY

Nếu bạn đang build hệ thống mới tương tự, SPEC này cho thấy
cấu trúc cần có:

```
Phần 1 — Tại sao hệ thống tồn tại (Problem + Goal)
Phần 2 — Hệ thống trông như thế nào (Architecture)
Phần 3 — Chạy trên gì (Hardware + Runtime)
Phần 4 — Ai làm gì (Agents + IDE)
Phần 5 — Làm như thế nào (Pipeline chi tiết)
Phần 6 — Feature nổi bật nhất (Deep dive)
Phần 7 — Luật không được phá vỡ (Constitution)
Phần 8 — Công cụ hiện có (Skill Registry)
Phần 9 — Biết mình đang ở đâu (Issues + Roadmap)
Phần 10 — Hướng dẫn đọc (Meta)
```

**Nguyên tắc viết SPEC:**
- Phần 1 viết trước — nếu không rõ vấn đề thì đừng viết phần còn lại
- Phần 7 (Constitution) là phần quan trọng nhất cho long-term stability
- SPEC là living document — cập nhật mỗi khi có thay đổi kiến trúc
- SPEC không phải tutorial — không giải thích "how to use",
  chỉ ghi "what it is và why"

---
*SPEC này reflect trạng thái hệ thống tại 2026-05-12.
Duy trì bởi: AN + Antigravity @pm agent.*
*Cập nhật khi: thay đổi architecture, thêm rule mới, thay đổi hardware.*
*v1.1 — Rule numbering reconciled: R1-R27 canonical (2026-05-12).*
