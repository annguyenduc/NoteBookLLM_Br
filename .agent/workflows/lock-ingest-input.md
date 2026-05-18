---
description: Khóa source_evidence_file, primary_ingest_file, và source_id trước khi vào ingest chính
---

# Workflow: lock-ingest-input

Workflow này là cổng vào cuối cùng trước khi chạy `ingest.md`.

Runtime boundary: kiểm tra nhất quán là read-only; ghi `INGEST INPUT LOCK` ra file là side effect và cần AN GO.

Nó không tạo `STRUCTURE`, `FIGURES`, `MAP`, `NAMING_LOCK`, hoặc Atom.

---

## 1. Mục tiêu

- Khóa 3 trường đầu vào bất biến cho ingest run:
  - `source_evidence_file`
  - `primary_ingest_file`
  - `source_id`
- Chốt artifact control nào là active cho source/run hiện tại

---

## 2. Input Bắt buộc

```yaml
SOURCE PREP REPORT:
  ...
  staging_status: "READY"

SOURCE AUDIT REPORT:
  ...
  audit_status: "PASSED"
  ready_for_input_lock: "YES"
```

---

## 3. Hành động

1. Đọc `SOURCE PREP REPORT`.
2. Đọc `SOURCE AUDIT REPORT`.
3. Xác nhận `source_evidence_file` và `promoted_artifact` cùng chỉ về một source logic.
4. Gán:
   - `source_evidence_file`
   - `primary_ingest_file = promoted_artifact`
   - `source_id`
5. Kiểm tra không có ingest-reading file cạnh tranh.
6. Resolve artifact control path active cho run hiện tại:
   - `00_Inbox/sources/[source_id]/`
   - hoặc `runs/ingest_[source_id]_[YYYYMMDD]_[seq]/`
7. Nếu mọi thứ nhất quán, khóa input cho ingest chính.

---

## 4. Quy tắc

- Một ingest run chỉ có đúng một `source_evidence_file`.
- Một ingest run chỉ có đúng một `primary_ingest_file`.
- `source_id` phải là anchor định danh duy nhất cho mọi artifact downstream.
- `source_id` không được tự suy ra lại từ display title, title slug, hay raw filename stem nếu naming lock đã tồn tại.
- Lifecycle control artifact filenames phải dùng `source_id` đã khóa, không dùng title slug thay thế.
- `INGEST INPUT LOCK` không được đặt trong `1-projects/`.
- Lifecycle control artifacts không satisfy official ingest gates chỉ vì nằm đúng thư mục; run hiện tại phải resolve chúng là active artifacts cho source/run đó.
- Nếu ba trường này chưa khóa được, `ingest.md` phải `BLOCKED`.

---

## 5. Output Contract

```yaml
INGEST INPUT LOCK:
  source_evidence_file: "[path]"
  primary_ingest_file: "[path]"
  source_id: "[ID]"
  active_control_path: "00_Inbox/sources/[source_id] | runs/ingest_[source_id]_[YYYYMMDD]_[seq]"
  status: "READY | BLOCKED"
  fail_reason: "NONE | ..."
```

---

## 6. READY Criteria

`READY` chỉ khi:
- `SOURCE PREP REPORT` đã `READY`
- `SOURCE AUDIT REPORT` đã `PASSED`
- có đúng một `source_evidence_file`
- có đúng một `primary_ingest_file`
- `source_id` đã chốt
- `active_control_path` đã chốt

---

## 7. BLOCKED Conditions

- thiếu `SOURCE PREP REPORT`
- thiếu `SOURCE AUDIT REPORT`
- `audit_status` chưa `PASSED`
- `source_id` chưa chốt
- có nhiều candidate cho `primary_ingest_file`
- `source_evidence_file` và `promoted_artifact` không còn trỏ về cùng một source logic

---

## 8. Downstream Consumer

Output của workflow này là prerequisite bắt buộc cho:
- `ingest.md`
