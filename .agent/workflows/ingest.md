---
description: Orchestration-only workflow cho source-first ingest sau khi upstream artifacts đã được khóa
---

# Workflow: /ingest

Workflow này chỉ điều phối ingest chính sau khi đầu vào đã sẵn sàng.

Workflow cha tham chiếu:

- `ingest-lifecycle`

Nó không được tự làm lại các bước upstream:

- `prepare-source`
- `audit-promote-source`
- `lock-ingest-input`

Nó cũng không được ôm phần downstream:

- `ingest-generate`
- `ingest-index-log`

---

## 1. Mục tiêu

- kiểm tra output artifact của các workflow trước đã đủ hay chưa
- nếu đủ thì vào `Phase 0+`
- nếu thiếu thì `BLOCKED` và chỉ ra workflow nào còn thiếu
- điều phối các artifact phân tích cấp ingest:
  - `STRUCTURE_[ID].md`
  - `FIGURES_[ID].md`
  - `NAMING_LOCK_[ID].md`
  - `MAP_[ID].md`
  - `Analysis_[ID]_MASTER_STRATEGY.md`
  - `Analysis_[ID]_CHUNK_XX.md`

---

## 2. Workflow Chain

```md
prepare-source
-> audit-promote-source
-> lock-ingest-input
-> ingest
-> ingest-generate
-> ingest-index-log
```

Nếu user muốn chạy full lifecycle như một entrypoint duy nhất, dùng `ingest-lifecycle`.

---

## 3. Input Bắt buộc

Workflow này chỉ được `READY` khi đã có đủ 3 artifact:

```yaml
SOURCE PREP REPORT:
  source_evidence_file: "[path]"
  source_type: "pdf | docx | pptx | markdown | html | web | video | audio | unknown"
  staging_status: "READY"

SOURCE AUDIT REPORT:
  source_evidence_file: "[path]"
  promoted_artifact: "[path]"
  artifact_type: "raw_ingest_md | staged_md | transcript | web_md | structure_stub | other"
  audit_status: "PASSED"
  ready_for_input_lock: "YES"

INGEST INPUT LOCK:
  source_evidence_file: "[path]"
  primary_ingest_file: "[path]"
  source_id: "[ID]"
  status: "READY"
```

---

## 4. Precheck

Trước khi vào `Phase 0`, bắt buộc phải có precheck:

```yaml
PRECHECK:
  source_prep_report: "YES | NO"
  source_audit_report: "YES | NO"
  ingest_input_lock: "YES | NO"
  status: "READY | BLOCKED"
```

### Rule

- nếu bất kỳ dòng nào là `NO` -> `BLOCKED`
- nếu `SOURCE PREP REPORT` thiếu -> yêu cầu chạy `prepare-source`
- nếu `SOURCE AUDIT REPORT` thiếu -> yêu cầu chạy `audit-promote-source`
- nếu `INGEST INPUT LOCK` thiếu -> yêu cầu chạy `lock-ingest-input`
- nếu cả 3 đều `YES` -> mới được vào `Phase 0+`

---

## 5. Quy tắc đầu vào bất biến

- một ingest run chỉ có đúng một `source_evidence_file`
- một ingest run chỉ có đúng một `primary_ingest_file`
- `source_id` là anchor định danh duy nhất cho toàn bộ artifact downstream
- với PDF lớn:
  - PDF là evidence
  - `primary_ingest_file` mới là ingest-reading file mặc định
- không được để agent dùng nhiều file text cạnh tranh vai trò `primary_ingest_file`

---

## 6. Scope Boundary

Workflow này:

- được phép kiểm tra artifact đầu vào
- được phép điều phối phase phân tích và scaffold artifact phân tích
- được phép dừng ở trạng thái chờ user duyệt analysis

Workflow này không làm:

- stage file ngoài vào `00_Inbox/`
- audit hoặc promote lại source
- khóa lại `primary_ingest_file`
- tạo atom thật vào `wiki/`
- rebuild, append log, hay closeout bookkeeping

---

## 7. Phase Flow

### Phase 0: Structure, Figures, Naming Lock, Map

Áp dụng cho ingest orchestration sau khi precheck đạt `READY`.

1. Tạo hoặc cập nhật `STRUCTURE_[ID].md`
   - chứa metadata nguồn
   - table of contents
   - hierarchy `Part -> Chapter -> Section -> page_range`
2. Tạo hoặc cập nhật `FIGURES_[ID].md` khi visual evidence là quan trọng
   - mỗi item gắn với `chapter -> section -> page`
3. Tạo hoặc cập nhật `NAMING_LOCK_[ID].md`
   - chốt `source_id`
   - chốt canonical filename patterns
   - không dùng `PREFIX` song song
4. Tạo hoặc cập nhật `MAP_[ID].md`
   - tổng hợp từ `STRUCTURE_[ID].md`
   - tổng hợp từ `FIGURES_[ID].md` khi có
   - không coi một chunk lẻ là global map

### Phase 0.5: Master Strategy

1. Đọc `primary_ingest_file` theo `INGEST INPUT LOCK`
2. Xác định knowledge pillars
3. Tạo `Analysis_[ID]_MASTER_STRATEGY.md`
4. Chốt roadmap chia chunk theo ưu tiên:
   1. chapter boundary first
   2. section boundary second
   3. page window last

### Phase 1: Anchor Planning

1. Xác định source node canonical filename
2. Xác định foundation entities cần có
3. Gắn chúng vào `NAMING_LOCK_[ID].md` hoặc `MAP_[ID].md`
4. Chỉ lập kế hoạch anchor set ở đây
5. Việc tạo atom thật thuộc `ingest-generate`

### Phase 2: Chunk Analysis

1. Tạo `Analysis_[ID]_CHUNK_XX.md`
2. Mỗi chunk phải bám theo:
   - `STRUCTURE_[ID].md`
   - `FIGURES_[ID].md` nếu có
   - `MAP_[ID].md`
   - `NAMING_LOCK_[ID].md`
   - `primary_ingest_file`
3. Chunk analysis phải nêu:
   - key takeaways
   - atoms proposed
   - contradictions and tensions
   - connections with existing wiki
   - deep research queries nếu có
4. Kết thúc phase này ở trạng thái chờ user duyệt analysis

---

## 8. Output Contract

Kết thúc workflow này phải có:

```yaml
INGEST ORCHESTRATION REPORT:
  source_id: "[ID]"
  source_evidence_file: "[path]"
  primary_ingest_file: "[path]"
  structure_file: "1-projects/STRUCTURE_[ID].md | NONE"
  figures_file: "1-projects/FIGURES_[ID].md | NONE"
  naming_lock_file: "1-projects/NAMING_LOCK_[ID].md | NONE"
  map_file: "1-projects/MAP_[ID].md | NONE"
  master_strategy_file: "1-projects/Analysis_[ID]_MASTER_STRATEGY.md | NONE"
  chunk_analysis_files:
    - "1-projects/Analysis_[ID]_CHUNK_XX.md"
  next_workflow: "ingest-generate | BLOCKED"
  status: "READY_FOR_GENERATE | BLOCKED"
```

---

## 9. READY Criteria

`READY_FOR_GENERATE` chỉ khi:

- precheck là `READY`
- `source_id` đã khóa
- `primary_ingest_file` đã khóa
- `STRUCTURE_[ID].md` đã sẵn sàng
- `FIGURES_[ID].md` đã sẵn sàng hoặc được đánh dấu `N/A`
- `NAMING_LOCK_[ID].md` đã sẵn sàng
- `MAP_[ID].md` đã sẵn sàng
- có ít nhất một `Analysis_[ID]_CHUNK_XX.md`
- analysis tương ứng đã chờ duyệt hoặc đã được duyệt cho generate

---

## 10. BLOCKED Conditions

- thiếu bất kỳ artifact upstream nào
- `audit_status` chưa `PASSED`
- `INGEST INPUT LOCK` chưa `READY`
- không xác định được `source_id`
- không xác định được `primary_ingest_file`
- `NAMING_LOCK_[ID].md` chưa chốt canonical filenames
- agent đang cố vào chunk analysis theo page-first trước chapter/section-first

---

## 11. Handoff

Khi orchestration đã hoàn tất:

- nếu analysis đã sẵn sàng cho tạo atom thật -> chuyển sang `ingest-generate`
- nếu analysis chưa được duyệt -> dừng và chờ user
- `ingest-index-log` chỉ chạy sau khi `ingest-generate` hoàn tất

---

## 12. Guardrails

- không treat PDF ad hoc reads như official ingest-ready extraction
- không tạo thêm atom thật trước khi `primary_ingest_file` được khóa
- không reintroduce `PREFIX` như naming anchor song song
- không để `page-first` thay thế `chapter/section-first`
- không để `ingest` tự hấp thụ lại trách nhiệm của upstream workflows
