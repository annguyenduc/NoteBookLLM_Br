---
description: Tạo atom thật từ analysis đã duyệt sau khi ingest orchestration hoàn tất
---

# Workflow: ingest-generate

Workflow này nhận output từ `ingest` và thực hiện bước generate atom thật.

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
  naming_lock_file: "1-projects/NAMING_LOCK_[ID].md"
  chunk_analysis_files:
    - "1-projects/Analysis_[ID]_CHUNK_XX.md"
  status: "READY_FOR_GENERATE"
```

Ngoài ra phải có:

- `STRUCTURE_[ID].md`
- `MAP_[ID].md`
- `FIGURES_[ID].md` nếu source cần visual evidence
- template trong `.agent/skills/references/`

---

## 3. Quy tắc

- chỉ generate từ analysis đã duyệt
- canonical filename phải lấy từ `NAMING_LOCK_[ID].md`
- nếu term/entity chưa được naming lock chốt -> `BLOCKED`
- không tự set `SYNTHESIZED`
- không tự làm rebuild/log ở workflow này

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

---

## 7. BLOCKED Conditions

- thiếu orchestration report
- orchestration report chưa `READY_FOR_GENERATE`
- chunk analysis chưa duyệt
- `NAMING_LOCK_[ID].md` thiếu mapping cần thiết
- source evidence phụ thuộc visual nhưng thiếu `FIGURES_[ID].md`

---

## 8. Handoff

- khi generate xong -> chuyển sang `ingest-index-log`
- nếu generate bị block -> không được chạy closeout
