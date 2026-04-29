# 🗺️ WORKSPACE OVERVIEW — NoteBookLLM_Br
> **Dành cho**: AI Agent (đọc trước khi hành động) & User (kiểm tra toàn cảnh).
> **Cập nhật**: 2026-04-29 | Schema v4.1

---

## 1. Cấu trúc thư mục (Directory Map)

```
NoteBookLLM_Br/
│
├── 📥 00_Inbox/                  ← Files thô từ ngoài vào. Flat, prefix YYYYMMDD_.
│                                    @librarian xử lý hàng tuần qua /ingest-inbox.
│
├── 📁 1-projects/                ← Dự án đang active.
│   ├── 2026_Data_Analyst/        ← DỰ ÁN CHÍNH (80/20 Ingest)
│   │   └── Ingest_80_20.md       ← Checklist trích xuất concept
│   ├── 2026_AI_Knowledge_Mining/ ← Nghiên cứu AI
│   └── 2026_MimiClaw_Inbox/      ← Bot MimiClaw
│
├── 📁 2-areas/                   ← Vùng quản lý liên tục.
│   ├── Profiles/                 ← Trainer Profile (@profiler ghi)
│   └── Assessment/               ← Báo cáo đánh giá (@evaluator ghi)
│
├── 📁 3-resources/               ← KHO TRI THỨC TRUNG TÂM
│   ├── schema.md                 ← Quy ước tên file & liên kết
│   ├── purpose.md                ← Mục tiêu & câu hỏi nghiên cứu
│   ├── WIKI_AGENT_GUIDE.md       ← Hướng dẫn tạo Wiki Atom (BẮT BUỘC đọc trước)
│   │
│   ├── 📂 raw/                   ← IMMUTABLE — chỉ User được thêm vào
│   │   ├── sources/              ← 31 file PDF/MD nguồn (Data Analyst library)
│   │   └── assets/               ← Hình ảnh, templates, prompts
│   │
│   └── 📂 wiki/                  ← KHO WIKI SỐNG (Agent đọc/ghi)
│       ├── index.md              ← Bản đồ (auto-generated bởi script)
│       ├── log.md                ← Nhật ký mọi thay đổi (append-only)
│       ├── overview.md           ← Tóm tắt tổng quan (auto-updated)
│       ├── concepts/             ← 41 Atomic concept pages (THINK_*, STAT_*, ...)
│       ├── entities/             ← 3 Entity pages (ENTITY_SQL, Python, Data_Science)
│       ├── sources/              ← 3 Source summaries (SOURCE_THINK_*)
│       ├── synthesis/            ← 2 Master synthesis files (THINK_Analytical_Thinking...)
│       ├── comparisons/          ← 1 Comparison page (COMPARE_*)
│       └── queries/              ← Kết quả file-back từ research (empty → chờ)
│
├── 📁 4-archive/                 ← Lưu trữ vĩnh viễn. Wikilinks đã trung hòa.
│
├── 📁 scripts/                   ← Công cụ tự động hóa
│   ├── update_wiki_index.py      ← Tái tạo wiki/index.md
│   ├── brain_lint.py             ← Kiểm tra sức khỏe Wiki
│   └── maintenance/              ← Các script bảo trì khác
│
├── 📁 .agent/                    ← Cấu hình Swarm Agent
│   ├── WORKSPACE_OVERVIEW.md     ← File này ← User review & Agent startup
│   └── workflows/                ← Workflow files (/ingest, /file-back, /lint...)
│
├── AGENTS.md                     ← BỘ LUẬT SWARM (đọc TRƯỚC KHI làm gì)
├── task_plan.md                  ← Kế hoạch hiện tại (v5.3 — Data Analyst 80/20)
├── CONTINUITY.md                 ← Ghi nhớ liên phiên (lỗi đã gặp, context)
└── COMMAND_BOARD.md              ← Bảng điều khiển lệnh nhanh
```

---

## 2. Workflow Chính (Main Flows)

### 2.1 — `/ingest` : Nạp nguồn tài liệu mới (Two-Step CoT)

```mermaid
flowchart TD
    A[👤 User thêm file vào\n3-resources/raw/sources/] --> B

    subgraph STEP1 ["Step 1 — Analysis (@scout)"]
        B[Đọc file raw] --> C[Tạo Analysis file\n1-projects/2026_Data_Analyst/\nAnalysis_PREFIX.md]
        C --> C1[📋 Key entities & concepts]
        C --> C2[🔗 Connections với Wiki hiện có]
        C --> C3[⚡ Contradictions & Tensions]
        C --> C4[🔍 Deep Research Queries]
        C --> C5[📐 Wiki Structure Recommendations]
    end

    C5 --> D{👤 User duyệt\nbản phân tích?}
    D -- "Approve" --> E

    subgraph STEP2 ["Step 2 — Generation (@engineer)"]
        E[Tạo SOURCE_ page\nwiki/sources/] --> F[Tạo/Cập nhật\nConcepts & Entities]
        F --> G[Direct Compounding\nvào wiki/synthesis/]
        G --> H[📋 Review Items\ncho Human Judgment]
    end

    H --> I[@librarian\nchạy update_wiki_index.py]
    I --> J[@pm ghi log\nvào wiki/log.md]
    J --> K[✅ Ingest hoàn tất\ngit commit + push]
```

### 2.2 — `/file-back` : Lưu kết quả research thành Wiki page

```mermaid
flowchart LR
    A[💬 Chat session\ncó Insight giá trị] --> B[@pm quyết định\nfile-back?]
    B -- Yes --> C[Tạo page mới\nwiki/queries/ hoặc\nwiki/concepts/]
    C --> D[Cập nhật\nwiki/index.md]
    D --> E[Append wiki/log.md]
    E --> F[✅ git commit]
```

### 2.3 — `/lint` : Kiểm tra sức khỏe Wiki

```mermaid
flowchart LR
    A[@librarian chạy\nbrain_lint.py] --> B{Kết quả?}
    B -- "Broken Links" --> C[@healer sửa links]
    B -- "Orphan Pages" --> D[Thêm wikilinks]
    B -- "Stale Claims" --> E[@auditor review\n& update nguồn]
    B -- "CLEAN ✅" --> F[Ghi log & done]
```

---

## 3. Phân quyền Agent (Quick Reference)

| Agent | Đọc | GHI (được phép) |
|:---|:---|:---|
| `@pm` | Tất cả | `wiki/log.md`, `1-projects/`, `CONTINUITY.md` |
| `@scout` | `raw/`, `1-projects/` | `1-projects/*/Analysis_*.md` (draft) |
| `@engineer` | `1-projects/`, `wiki/synthesis/` | `1-projects/*/output`, `wiki/concepts/`, `wiki/entities/`, `wiki/sources/` |
| `@librarian` | Tất cả | `wiki/synthesis/` (sau verify), `wiki/log.md`, `wiki/index.md` |
| `@auditor` | Tất cả (read-only) | `wiki/log.md` (append only) |
| `@devops` | Tất cả | `scripts/`, `tools/` |
| `@healer` | Tất cả | `wiki/` (sửa links), `scripts/` |
| **KHÔNG AI ĐƯỢC** | — | `raw/sources/` (IMMUTABLE) |

---

## 4. Trạng thái Ingest (Data Analyst 80/20)

| Nhóm | Chủ đề | Raw Files | Source Summary | Concepts | Trạng thái |
|:---|:---|:---:|:---:|:---:|:---|
| **Nhóm 1** | THINK (Tư duy) | 3 | ✅ 3 | ✅ 10 | **DONE** |
| **Nhóm 3** | SQL | 4 | ❌ 0 | ❌ 0 | 🔴 Chưa bắt đầu |
| **Nhóm 4** | Python/Pandas | 2 | ❌ 0 | ❌ 0 | 🔴 Chưa bắt đầu |
| **Nhóm 5** | Visualization | 7 | ❌ 0 | ❌ 0 | 🔴 Chưa bắt đầu |

**Ưu tiên tiếp theo**: Nhóm 3 — SQL (`TOOL_SQL_Getting_Started.md`)

---

## 5. Các lệnh thường dùng

```powershell
# Kiểm tra sức khỏe Wiki
python scripts/brain_lint.py

# Tái tạo index.md
python scripts/update_wiki_index.py

# Git checkpoint
git add -A && git commit -m "..." && git push
```

---
*File này được cập nhật mỗi khi có thay đổi lớn về cấu trúc hoặc khi bắt đầu phiên làm việc mới.*
