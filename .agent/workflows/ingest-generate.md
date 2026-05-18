---
description: Tạo atom thật từ analysis đã duyệt sau khi ingest orchestration hoàn tất
---

# Workflow: ingest-generate

Workflow này nhận output từ `ingest` và thực hiện bước generate atom thật.

Runtime boundary: đây là workflow có side effect vì tạo/patch Atom. Chỉ chạy sau khi có AN GO rõ cho `ingest-generate`.

Workflow cha tham chiếu:

- `ingest-lifecycle`

Nó không thay thế:

- `ingest` orchestration
- `ingest-index-log`

---

## 1. Mục tiêu

- đọc `Analysis_[ID]_CHUNK_XX.md` đã duyệt
- tạo source/concept/entity atoms thật theo naming lock
- giữ traceability về `primary_ingest_file`
- xuất báo cáo generate rõ ràng cho bước closeout

---

## 2. Input Bắt buộc

```yaml
INGEST ORCHESTRATION REPORT:
  source_id: "[ID]"
  source_evidence_file: "[path]"
  primary_ingest_file: "[path]"
  naming_lock_file: "1-projects/sources/[source_id]/NAMING_LOCK_[ID].md"
  chunk_analysis_files:
    - "1-projects/sources/[source_id]/Analysis_[ID]_CHUNK_XX.md"
  status: "READY_FOR_GENERATE"
  gate_reasons:
    - "[reason]"
  projected_end_to_end_outcome:
    - "[what will be materialized if all gates pass]"
```

Ngoài ra phải có:

- `STRUCTURE_[ID].md`
- `MAP_[ID].md`
- `FIGURES_[ID].md` nếu source cần visual evidence
- template trong `.agent/skills/references/`

---

## 2.5. Language Policy For Markdown Outputs

Workflow này phải giữ metadata ở dạng canonical, nhưng phần nội dung markdown dành cho human review phải viết bằng tiếng Việt.

Giữ nguyên tiếng Anh hoặc canonical form cho:

- metadata keys
- status enums
- filenames
- `source_id`
- exact source title
- code
- technical terms khi cần giữ nguyên độ chính xác

Áp dụng cho:

- body của atom source/concept/entity được tạo mới hoặc patch
- `WRITE REPORT`
- `INGEST GENERATE REPORT` phần mô tả tự do

Khi cần nhắc thuật ngữ gốc, ưu tiên mẫu:

- `vòng phản hồi cân bằng (balancing feedback)`
- `dòng chảy (flow)`
- `tồn kho/tích lũy (stock)`

---

## 3. Quy tắc

- chỉ generate từ analysis đã duyệt
- canonical filename phải lấy từ `NAMING_LOCK_[ID].md`
- nếu term/entity chưa được naming lock chốt -> `BLOCKED`
- không tự set `SYNTHESIZED`
- không tự làm rebuild/log ở workflow này
- không coi "tiếp tục" là GO nếu chưa nêu rõ được phép tạo/patch Atom

---

## 4. Hành động

1. Đọc `INGEST ORCHESTRATION REPORT`
2. Đọc lại `primary_ingest_file` để giữ traceability với raw reading input
3. Đọc `NAMING_LOCK_[ID].md`
4. Với mỗi `Analysis_[ID]_CHUNK_XX.md` đã duyệt:
   - tạo hoặc patch source atom nếu cần
   - tạo hoặc patch concept atoms
   - tạo hoặc patch entity atoms
5. Mỗi atom phải:
   - bám template chuẩn
   - có wikilinks cần thiết
   - có evidence rõ ràng
   - bám canonical filename
6. Ghi `WRITE REPORT` cho từng file được tạo hoặc patch
7. `WRITE REPORT` phải mô tả bằng tiếng Việt; chỉ giữ enum và filename ở dạng canonical

---

## 5. Output Contract

```yaml
INGEST GENERATE REPORT:
  source_id: "[ID]"
  chunk_file: "[path]"
  atoms_created:
    - "[path]"
  atoms_patched:
    - "[path]"
  write_reports:
    - file: "[path]"
      operation: "create | patch"
      added: "[summary]"
      removed: "NONE | [summary]"
  status: "DONE | BLOCKED"
  fail_reason: "NONE | ..."
```

---

## 6. READY Criteria

`DONE` chỉ khi:

- orchestration report là `READY_FOR_GENERATE`
- chunk analysis đã duyệt
- mọi filename đều khớp naming lock
- không có atom nào được generate từ term/entity chưa khóa tên
- `FIGURES_[ID].md` không còn `PENDING_EXTRACTION`
- `FIGURES_[ID].md` không còn `ASSETS_PRESENT_BUT_UNREGISTERED`

---

## 7. BLOCKED Conditions

- thiếu orchestration report
- orchestration report chưa `READY_FOR_GENERATE`
- chunk analysis chưa duyệt
- `NAMING_LOCK_[ID].md` thiếu mapping cần thiết
- source evidence phụ thuộc visual nhưng thiếu `FIGURES_[ID].md`
- `FIGURES_[ID].md` còn `PENDING_EXTRACTION`
- `FIGURES_[ID].md` còn `ASSETS_PRESENT_BUT_UNREGISTERED`

---

## 8. Handoff

- khi generate xong -> chuyển sang `ingest-index-log`
- nếu generate bị block -> không được chạy closeout
