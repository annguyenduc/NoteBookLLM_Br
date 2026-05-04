# RESEARCH: Tooling Logic Reference (Benchmarks)

Tài liệu này tổng hợp các logic tinh túy từ 4 repo Second Brain hàng đầu để áp dụng cho NoteBookLLM_Br.

---

## 1. Skill: `wiki-absorb` (Logic: Reconciler)
**Tham chiếu**: `eugeniughelbur/obsidian-second-brain`

### Logic chính (Reconciliation Logic):
- **Conflict Detection**: So sánh timestamp và "Recency Marker" trong frontmatter để xác định thông tin nào mới hơn.
- **Contradiction Sweeping**: Thay vì chỉ append (thêm vào cuối), agent sẽ đọc Master Synthesis hiện tại và Atom mới. Nếu Atom mới mâu thuẫn với Master, agent thực hiện "Rewrite" (viết lại) đoạn đó để phản ánh sự thật mới nhất.
- **Source Compounding**: Khi hợp nhất, không được xóa trích dẫn nguồn cũ. Phải gộp trích dẫn: `Nguồn: [Source A], [Source B]`.

---

## 2. Skill: `wiki-cleanup` & `wiki-status` (Logic: Link Density & Audit)
**Tham chiếu**: `agricidaniel/claude-obsidian` & `eugeniughelbur`

### Logic Audit (8 Categories):
1. **Orphans**: File không có link inbound.
2. **Dead Links**: Wikilinks trỏ đến file không tồn tại.
3. **Missing Sources**: Claims không có Source Tracing (Rule 14).
4. **Tag Inconsistency**: Tag không nằm trong `schema.md`.
5. **Double Example Gap**: Thiếu ví dụ đối chiếu (Rule 17).
6. **Structure Drift**: Frontmatter thiếu các trường bắt buộc (V3.0).
7. **Semantic Gaps**: Các Concepts liên quan nhưng không link với nhau.
8. **Stale Claims**: Thông tin đã quá hạn so với nguồn mới nhất.

### Chỉ số Link Density (LDI):
- `LDI = (Tổng số Wikilinks) / (Tổng số MD files)`.
- Mục tiêu: Dashboard hiển thị LDI > 3.0.

---

## 3. Skill: `wiki-rebuild` (Logic: Manifest & Index Sync)
**Tham chiếu**: `Ar9av/obsidian-wiki`

### Logic Sync:
- **Manifest Tracking**: Sử dụng `.manifest.json` để lưu hash của từng file. Chỉ sync/rebuild những file có thay đổi (Delta Rebuild) để tiết kiệm Token.
- **Automatic Backlink Injection**: Script quét toàn bộ vault và tự động append danh sách "Linked Mentions" vào cuối mỗi file (nếu Obsidian chưa hiển thị tốt).
- **Index hierarchy**: Tự động phân loại file vào `index.md` dựa trên `type` trong frontmatter (concept/entity/source/synthesis).

---

## 4. Skill: `wiki-breakdown` (Logic: Concrete Noun Test)
**Thiết kế riêng (Unique Design)**:

### Logic:
- Sử dụng NLP (hoặc Regex thuật ngữ) để trích xuất các danh từ riêng.
- Loại trừ các từ đã có trong `index.md`.
- Gợi ý danh sách "Missing Atoms" (Top 10 danh từ xuất hiện nhiều nhất nhưng chưa có trang Wiki).

---

## Kế hoạch hành động tiếp theo
1. **Giao cho @engineer**: Viết `scripts/sync_engine.py` cho `wiki-rebuild` (Dễ nhất, tạo nền tảng).
2. **Giao cho @engineer**: Viết `scripts/reconciler.py` cho `wiki-absorb` (Phức tạp nhất, cần test kỹ).
3. **@pm & @auditor**: Thực hiện Audit 8 Categories bằng `wiki-cleanup`.


# WIKI SKILL SYSTEM — BUILD PLAN v1.0

## Mục tiêu
Xây dựng bộ 7 wiki skill cho hệ thống Second Brain Wiki 2.0,
dựa trên Schema V3.0 và 7 Operational Commands đã định nghĩa
trong SYNTHESIS_MASTER_Second_Brain_Blueprint.

## Nguyên tắc bắt buộc
- Đọc SKILL.md tham khảo TRƯỚC khi viết bất kỳ skill nào
- Mỗi skill phải có: Purpose / Trigger / Instructions / Examples
- Skill tạo content phải đồng thời tạo connections (link density)
- Không viết logic vào SKILL.md nếu cần side effects trên
  filesystem — dùng scripts/ thay thế
- Backup .agent/skills/ vào 4-archive/ trước khi thay đổi

---

## BƯỚC 0 — Setup tham khảo (làm trước tất cả)

### Clone 2 repo chính
git clone https://github.com/eugeniughelbur/obsidian-second-brain
git clone https://github.com/Ar9av/obsidian-wiki

### Lấy 3 skill folder từ sickn33 (sparse checkout)
npx antigravity-awesome-skills \
  --path .agent/skills/references \
  --tags memory,research,obsidian

### Đọc 1 file methodology
https://github.com/obra/superpowers/blob/main/skills/writing-skills/SKILL.md

### Output bước này
- [ ] Folder .agent/skills/references/ có đủ tài liệu
- [ ] Agent đã đọc writing-skills pattern của Superpowers
- [ ] Backup .agent/skills/ hiện tại → 4-archive/

---

## BƯỚC 1 — wiki-ingest (Skill đầu tiên)

### Tham khảo chính
- Ar9av/obsidian-wiki: cấu trúc raw/ → wiki/
- NicholasSpisak/second-brain: README (pattern đơn giản)

### Logic
Raw file → Analysis → Atoms
Tự động gán Prefix (AIMET_, DSML_...) và rename file raw

### Deliverable
- [ ] .agent/skills/wiki-ingest/SKILL.md
- [ ] .agent/skills/wiki-ingest/scripts/ingest.py

---

## BƯỚC 2 — wiki-absorb

### Tham khảo chính
- eugeniughelbur SKILL.md: Phase 2 Reconcile + Phase 3 Synthesize
- sickn33 agent-memory-systems: conflict resolution pattern

### Logic
New Atom + Existing Synthesis → Rewritten Master
Auto-resolve mâu thuẫn rõ ràng
Flag ambiguous → wiki/decisions/

### Deliverable
- [ ] .agent/skills/wiki-absorb/SKILL.md
- [ ] .agent/skills/wiki-absorb/scripts/reconciler.py

---

## BƯỚC 3 — wiki-query

### Tham khảo chính
- sickn33 agent-memory-systems: semantic memory framework
- sickn33 context-manager: tránh context overflow

### Logic
Graph Traversal + Semantic Reranking
Output có trích dẫn nguồn tuyệt đối (Rule 14)
Dùng subagent để search, không pollute context window chính

### Deliverable
- [ ] .agent/skills/wiki-query/SKILL.md
(SKILL.md thuần, không cần script)

---

## BƯỚC 4 — wiki-breakdown

### Tham khảo chính
- sickn33 deep-research: autonomous gap detection loop
- sickn33 bdistill-knowledge-extraction: extract proper nouns

### Logic
Concrete Noun Test: phát hiện danh từ riêng chưa có trang Wiki
Query → tìm missing angles → surface gap → tạo stub page

### Deliverable
- [ ] .agent/skills/wiki-breakdown/SKILL.md
- [ ] .agent/skills/wiki-breakdown/scripts/noun_miner.py

---

## BƯỚC 5 — wiki-cleanup

### Tham khảo chính
- agricidaniel/claude-obsidian: lint 8 categories
- eugeniughelbur: duplicate detection ("vault rot" rule)

### Logic
Sửa broken links, chuẩn hóa tone, Steve Jobs Test
Scan 8 categories, gán severity, suggest fix

### Deliverable
- [ ] .agent/skills/wiki-cleanup/SKILL.md
- [ ] .agent/skills/wiki-cleanup/scripts/lint_engine.py

---

## BƯỚC 6 — wiki-status + wiki-rebuild

### Tham khảo chính
- eugeniughelbur: Phase 4 Heal + Phase 5 Log
- sickn33 obsidian-bases: dashboard render trong Obsidian

### Logic wiki-status
Thống kê: link density, tỷ lệ verified vs draft
Output: bảng dashboard sức khỏe + log.md entry
Format: X reconciled / Y synthesized / Z orphans linked

### Logic wiki-rebuild
Sync index.md + _backlinks.json
Chạy như 2 subagent song song (context isolation)
Triggered bởi: nightly agent HOẶC lệnh trực tiếp

### Deliverable
- [ ] .agent/skills/wiki-status/SKILL.md
- [ ] .agent/skills/wiki-rebuild/SKILL.md
- [ ] .agent/skills/wiki-rebuild/scripts/rebuild.py

---

## BƯỚC 7 — AGENTS.md + Test toàn bộ

### Tham khảo chính
- obra/superpowers: using-superpowers (1% rule)
- obra/superpowers: subagent-driven-development

### Logic AGENTS.md
Nếu có 1% khả năng wiki skill apply → PHẢI invoke
Thứ tự ưu tiên: ingest → absorb → query → breakdown →
cleanup → status → rebuild

### Test chain
Chạy chuỗi: Ingest → Absorb → Status
Verify log.md có entry đúng format
Verify index.md và _backlinks.json đồng bộ

### Deliverable
- [ ] .agent/AGENTS.md (cập nhật)
- [ ] Test log tại 4-archive/test-YYYY-MM-DD.md

---

## Cấu trúc thư mục kết quả

.agent/
├── AGENTS.md
├── skills/
│   ├── wiki-ingest/
│   │   ├── SKILL.md
│   │   └── scripts/ingest.py
│   ├── wiki-absorb/
│   │   ├── SKILL.md
│   │   └── scripts/reconciler.py
│   ├── wiki-query/
│   │   └── SKILL.md
│   ├── wiki-breakdown/
│   │   ├── SKILL.md
│   │   └── scripts/noun_miner.py
│   ├── wiki-cleanup/
│   │   ├── SKILL.md
│   │   └── scripts/lint_engine.py
│   ├── wiki-status/
│   │   └── SKILL.md
│   ├── wiki-rebuild/
│   │   ├── SKILL.md
│   │   └── scripts/rebuild.py
│   └── references/        ← tài liệu tham khảo, KHÔNG load thường trực
└── 4-archive/

---

## Quy tắc thực thi cho Agent

1. Làm tuần tự theo Bước 0 → 7, không nhảy bước
2. Sau mỗi SKILL.md: chạy 1 pressure test trước khi sang skill tiếp
3. Không xóa file cũ — move vào 4-archive/ trước
4. Mỗi script phải có --dry-run flag trước khi chạy production
5. Ghi log tiến độ vào 4-archive/build-log.md sau mỗi bước