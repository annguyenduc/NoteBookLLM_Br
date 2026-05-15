---
description: Audit và promote source artifact để tạo ingest-reading artifact chính
---

# Workflow: audit-promote-source

Workflow này nhận `SOURCE PREP REPORT` và tạo artifact đọc chính cho ingest.

`audit-promote-source` không bắt đầu Phase 0 của ingest chính.

---

## 1. Mục tiêu

- Audit source đã được chuẩn bị
- Tạo hoặc xác nhận `primary_ingest_file`
- Đảm bảo artifact đọc chính đủ sạch để làm ingest-reading input

---

## 2. Input Bắt buộc

```yaml
SOURCE PREP REPORT:
  ...
  staging_status: "READY"
```

---

## 3. Hành động

1. Đọc `SOURCE PREP REPORT`.
2. Xác nhận `source_evidence_file` có hợp lệ.
3. Chọn workflow audit/promote phù hợp theo `source_type`.
4. Tạo hoặc xác nhận đúng một `primary_ingest_file`.
5. Ghi rõ `artifact_type`.
6. Nếu audit fail hoặc artifact đọc không rõ ràng, dừng tại đây.

---

## 4. Quy tắc

- `primary_ingest_file` là ingest-reading input chính.
- Với PDF lớn:
  - PDF là evidence
  - artifact text/structured output mới là thứ ingest sẽ đọc mặc định
- Không được để nhiều artifact text cạnh tranh vai trò `primary_ingest_file`.
- Không được vào ingest chính nếu audit chưa `PASSED`.

---

## 5. Output Contract

```yaml
SOURCE AUDIT REPORT:
  source_evidence_file: "[path or URL]"
  promoted_artifact: "[path]"
  artifact_type: "raw_ingest_md | staged_md | transcript | web_md | structure_stub | other"
  audit_status: "PASSED | FAILED | BLOCKED"
  ready_for_input_lock: "YES | NO"
  fail_reason: "NONE | ..."
```

---

## 6. PASSED Criteria

`PASSED` chỉ khi:
- source prep đã `READY`
- có đúng một `promoted_artifact`
- `artifact_type` đã rõ
- artifact đã đủ điều kiện để trở thành `primary_ingest_file`

---

## 7. BLOCKED / FAILED Conditions

- source prep chưa `READY`
- không tạo/xác định được `promoted_artifact`
- có nhiều artifact cạnh tranh nhau
- audit chưa pass
- artifact chưa đủ chất lượng để làm ingest-reading input

---

## 8. Downstream Consumer

Output của workflow này là input bắt buộc cho:
- `lock-ingest-input.md`
