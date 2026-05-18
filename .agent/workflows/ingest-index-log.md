---
description: Rebuild, append log, và closeout bookkeeping sau khi ingest-generate hoàn tất
---

# Workflow: ingest-index-log

Workflow này đóng ingest run sau khi atom đã được generate.

Runtime boundary: rebuild, append log và bookkeeping là side effect. Chỉ chạy khi GO ban đầu bao gồm closeout hoặc AN cấp GO riêng cho `ingest-index-log`.

Workflow cha tham chiếu:

- `ingest-lifecycle`

Nó không làm lại:

- orchestration
- atom generation

---

## 1. Mục tiêu

- rebuild filesystem -> DB/index
- append ingest log
- hoàn tất post-ingest bookkeeping

---

## 2. Input Bắt buộc

```yaml
INGEST GENERATE REPORT:
  source_id: "[ID]"
  chunk_file: "[path]"
  atoms_created:
    - "[path]"
  status: "DONE"
```

---

## 3. Hành động

1. Đọc `INGEST GENERATE REPORT`
2. Chạy rebuild phù hợp để đồng bộ filesystem và index
3. Ghi closeout log cho ingest run
4. Ghi lại số lượng artifact đã tạo hoặc patch
5. Chốt trạng thái bookkeeping

---

## 4. Log Scope

Closeout log nên phản ánh:

- `source_id`
- `source_evidence_file` nếu có trong handoff context
- `primary_ingest_file` nếu có trong handoff context
- danh sách atom được tạo hoặc patch
- số lượng concept/entity/source đã thay đổi

---

## 5. Output Contract

```yaml
INGEST CLOSEOUT REPORT:
  source_id: "[ID]"
  rebuild_status: "DONE | FAILED"
  log_status: "DONE | FAILED"
  bookkeeping_status: "DONE | FAILED"
  status: "DONE | BLOCKED"
  fail_reason: "NONE | ..."
```

---

## 6. READY Criteria

`DONE` chỉ khi:

- generate report là `DONE`
- rebuild hoàn tất
- log hoàn tất
- bookkeeping hoàn tất

---

## 7. BLOCKED Conditions

- thiếu generate report
- generate report chưa `DONE`
- rebuild thất bại
- append log thất bại

---

## 8. Guardrails

- không chạy nếu atom generation chưa xong
- không sửa ngược lại artifact orchestration để che lỗi generate
- nếu rebuild fail thì phải báo `FAILED`, không được coi ingest run là hoàn tất
