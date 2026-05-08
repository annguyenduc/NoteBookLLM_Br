---
file_id: SYNTHESIS_MASTER_Second_Brain_Blueprint
title: "SYNTHESIS: Master Second Brain Blueprint (V3.0 - Unified)"
type: synthesis
status: VERIFIED
tags:
ai-first: true
confidence: high
last_reconciled: 2026-05-02
created: 2026-05-02
last_updated: 2026-05-08
---

# Master Second Brain Blueprint (Đại bản thiết kế Bộ não thứ hai)

## ## For future Claude
Tài liệu này là **"Hiến pháp"** tối cao của hệ thống Wiki. Nó hợp nhất mọi phương pháp luận từ Karpathy, Nashsu và Wiki-Gen thành một quy trình vận hành duy nhất. Mọi Agent khi thực hiện tác vụ Wiki PHẢI tuân thủ các chuẩn Metadata, cấu trúc Body và hệ thống 7 Skill được định nghĩa tại đây. Ưu tiên hàng đầu: AI-First, Rewrite Principle, và Source Tracing tuyệt đối.

## ## Key Claims / Summary
1.  **AI-First Vault**: Hệ thống được tối ưu để Agent đọc hiểu trong <10 giây.
2.  **Rewrite Engine**: Tri thức không được "nối thêm" (Append) mà phải được "tái sinh" (Rewrite) để giữ mạch truyện (Narrative Coherence).
3.  **Flat Architecture (Rule 7)**: Giữ cấu trúc thư mục phẳng ở cấp 3 để tối ưu tốc độ truy vấn của AI.
4.  **7 Skills & 5 Extensions**: Hệ thống tự vận hành thông qua các Skill đóng gói và khả năng tự hòa giải (Reconciliation).

## ## Detailed Analysis

### 1. Kiến trúc Hệ thống (The Architecture)
Hệ thống vận hành theo mô hình **Swarm Intelligence** chia thành 5 Module chức năng:

- **Module Ingest**: Cửa ngõ chuyển đổi `raw/` -> `Atoms`. Sử dụng Prefix-based Flattening để quản lý hàng trăm file nguồn.
- **Module Absorption**: Vòng lặp hấp thụ tri thức. Đây là nơi thực hiện các cú "Rewrite" để tích hợp thông tin mới vào các node cũ.
- **Module Intelligence**: Tầng suy luận, trả lời câu hỏi và phát hiện lỗ hổng logic (`/wiki query`).
- **Module Mining**: Khai thác thực thể mới bằng "Concrete Noun Test" (`/wiki breakdown`).
- **Module Maintenance**: Tự động sửa link, chuẩn hóa Tone Wikipedia và Audit chất lượng (`/wiki cleanup`, `/wiki rebuild`).

### 2. Tiêu chuẩn High-Fidelity Schema (Metadata & Body)
Để biến Markdown thành "Database Objects", mọi file Wiki phải tuân thủ:

**A. Metadata (Frontmatter) V3**: 
Bắt buộc có: `file_id`, `type`, `ai-first: true`, `source`, `relationships` (Typed Links), và `last_reconciled`.

**B. Cấu trúc Body (The standard flow)**:
1. `## For future Claude` (Preamble)
2. `## Key Claims / Summary`
3. `## Detailed Analysis` (Sử dụng Recency Markers)
4. `## Relationships` (Visual list)
5. `## Source Tracing` (R3 compliance)
6. `## History / Revisions`

### 3. Hệ thống 7 Lệnh vận hành (Operational Protocol)
1.  **`/wiki ingest`**: Nạp liệu & Phân loại.
2.  **`/wiki absorb`**: Hấp thụ & Rewrite.
3.  **`/wiki query`**: Truy vấn Đồ thị & Tổng hợp.
4.  **`/wiki cleanup`**: Audit chất lượng (Steve Jobs Test).
5.  **`/wiki breakdown`**: Khai thác lỗ hổng tri thức.
6.  **`/wiki status`**: Đo lường sức khỏe & Mật độ liên kết.
7.  **`/wiki rebuild`**: Đồng bộ hóa Index & Backlinks.

### 4. Tiện ích mở rộng V3 (The Intelligence Layer)
- **Automatic Reconciliation**: Tự động giải quyết mâu thuẫn tri thức.
- **Unsolicited Synthesis**: AI tự tạo trang tổng hợp khi thấy các Pattern lặp lại.
- **Write-back**: Chat tự động cập nhật ngược lại Wiki.
- **Reversibility**: Mọi thay đổi ghi vào `daily_diff.md`, cho phép khôi phục trong 24h.

## ## Active Roadmap & Gaps (Từ Audit 2026-05-01)
Dựa trên kết quả kiểm toán, hệ thống cần tập trung vào:
- [x] **Agentic Expansion**: Tích hợp lộ trình [[SOURCE_AIMET_AGENTIC_ROADMAP_2026]] vào hệ thống (May 2026).
- [ ] **Entity Genesis**: Khởi tạo `ENTITY_TOOL_` cho các công cụ lõi (Gemini, Claude, Obsidian).
- [ ] **Comparison Layer**: Xây dựng `COMPARE_` để hòa trộn sâu sắc giữa Karpathy và Nashsu.
- [ ] **Assessment Integration**: Concept về việc biến Wiki thành đề thi/kiểm tra tự động.
- [ ] **Rule 7 Compliance**: Hoàn tất việc chuẩn hóa Prefix cho toàn bộ `raw/sources/`.

## ## Relationships
- `governs` -> [[index]]
- `supersedes` -> [[SYNTHESIS_ULTIMATE_Second_Brain_Spec]]
- `supersedes` -> [[SYNTHESIS_Second_Brain_Standard_Spec]]
- `supersedes` -> [[SYNTHESIS_Wiki_Intelligence_Architecture]]
- `relates_to` -> [[CONCEPT_META_Atomic_Methodology]]

## ## Source Tracing
- **Nguồn**: [[SOURCE_META_WIKI_GEN_CLONE]] — Lệnh & Taxonomy.
- **Nguồn**: SOURCE_META_KARPATHY_LLM_WIKI — AI-First & Extensions.
- **Nguồn**: SOURCE_META_NASHUS_LLMWIKI — High Fidelity Graph.
- **Nguồn**: [[SOURCE_META_LLM_WIKI_V2]] — Consolidation Tiers.

## ## History / Revisions
- **2026-05-03**: [@engineer] Ingest Roadmap Agentic AI 2026. Tích hợp 11 atoms mới về Python Standards, Context Budgeting và Multi-Agent.
- **2026-05-02**: [@pm] Đại hợp nhất 4 file Synthesis thành Master Blueprint. Khai tử các phiên bản V1, V2 để tránh trùng lặp.


## 4F Reflection
- **Facts**: Hệ thống build được đầy đủ về kỹ thuật nhưng 289 atoms cũ không có content thật. Agent hallucinate nếu không có human check.
- **Feelings**: Hứng thú ban đầu → thực tế phức tạp hơn. Cần kiểm soát nhiều hơn tưởng.
- **Findings**: Human Gate không phải optional — là thứ duy nhất ngăn vault đầy rác. Hiểu lý do agents sai quan trọng hơn biết agents làm gì. **[2026-05-07]**: Agent suggest fix không phải lúc nào cũng đúng. `human_review_flag = 0` cho Inbox là đúng vì confidence threshold đã handle việc routing. Không fix thứ không broken.
- **Futures**: Tuần tới: ingest có chọn lọc thay vì bulk. Mỗi atom phải qua mắt mình trước khi VERIFIED.
