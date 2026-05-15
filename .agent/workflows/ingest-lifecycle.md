---
description: Workflow cha duy nhất cho toàn bộ ingest lifecycle, điều phối 6 workflow con bằng artifact gates và resume rules
---

# Workflow: ingest-lifecycle

Đây là workflow cha cho toàn bộ vòng đời ingest.

User chỉ nên nghĩ theo một entrypoint này.

Các workflow con vẫn tồn tại để:

- giữ boundary rõ
- giảm drift
- cho phép resume chính xác theo artifact

---

## 1. Mục tiêu

- cung cấp một entrypoint duy nhất cho ingest chính thức
- luôn đi theo full lifecycle chuẩn
- không cho phép bỏ stage bắt buộc
- cho phép resume từ stage hợp lệ tiếp theo nếu artifact trước đó đã tồn tại và pass gate

---

## 2. Full Chain

```md
prepare-source
-> audit-promote-source
-> lock-ingest-input
-> ingest
-> ingest-generate
-> ingest-index-log
```

Đây là lifecycle chuẩn cho một source ingest chính thức.

---

## 3. Nguyên tắc vận hành

### Full-chain required

- một source mới phải thuộc full lifecycle này
- không được coi run là hợp lệ nếu thiếu bất kỳ stage bắt buộc nào

### Checkpoint-stop allowed

Workflow cha được phép dừng ở gate hợp lệ:

- `BLOCKED` vì thiếu artifact
- `BLOCKED` vì fail gate
- `WAITING_FOR_REVIEW` vì analysis chưa được duyệt

Việc dừng ở gate hợp lệ không được coi là cắt workflow.

### Mid-chain start forbidden for fresh runs

- một ingest run mới không được bắt đầu từ giữa chuỗi
- entrypoint chuẩn luôn là `ingest-lifecycle`

### Mid-chain resume allowed by artifact

Nếu artifact của các stage trước đã tồn tại và hợp lệ, workflow cha được phép resume từ stage kế tiếp.

Resume chỉ được dựa trên artifact contract, không dựa trên đoán trạng thái.

---

## 4. Stage Contracts

### Stage 1: prepare-source

Expected artifact:

```yaml
SOURCE PREP REPORT:
  source_evidence_file: "[path]"
  source_type: "pdf | docx | pptx | markdown | html | web | video | audio | unknown"
  staging_status: "READY | BLOCKED"
```

### Stage 2: audit-promote-source

Expected artifact:

```yaml
SOURCE AUDIT REPORT:
  source_evidence_file: "[path]"
  promoted_artifact: "[path]"
  artifact_type: "raw_ingest_md | staged_md | transcript | web_md | structure_stub | other"
  audit_status: "PASSED | FAILED | BLOCKED"
  ready_for_input_lock: "YES | NO"
```

### Stage 3: lock-ingest-input

Expected artifact:

```yaml
INGEST INPUT LOCK:
  source_evidence_file: "[path]"
  primary_ingest_file: "[path]"
  source_id: "[ID]"
  status: "READY | BLOCKED"
```

### Stage 4: ingest

Expected artifact:

```yaml
INGEST ORCHESTRATION REPORT:
  source_id: "[ID]"
  primary_ingest_file: "[path]"
  chunk_analysis_files:
    - "[path]"
  status: "READY_FOR_GENERATE | BLOCKED"
```

### Stage 5: ingest-generate

Expected artifact:

```yaml
INGEST GENERATE REPORT:
  source_id: "[ID]"
  chunk_file: "[path]"
  status: "DONE | BLOCKED"
```

### Stage 6: ingest-index-log

Expected artifact:

```yaml
INGEST CLOSEOUT REPORT:
  source_id: "[ID]"
  status: "DONE | BLOCKED"
```

---

## 5. Parent Precheck

Trước khi chạy, workflow cha phải xác định lifecycle đang ở đâu.

```yaml
LIFECYCLE PRECHECK:
  source_prep_report: "YES | NO"
  source_audit_report: "YES | NO"
  ingest_input_lock: "YES | NO"
  ingest_orchestration_report: "YES | NO"
  ingest_generate_report: "YES | NO"
  ingest_closeout_report: "YES | NO"
  next_stage: "prepare-source | audit-promote-source | lock-ingest-input | ingest | ingest-generate | ingest-index-log | DONE | BLOCKED"
  status: "READY | BLOCKED"
```

---

## 6. Resume Resolution

Workflow cha xác định `next_stage` theo quy tắc:

1. nếu chưa có `SOURCE PREP REPORT` -> `prepare-source`
2. nếu có `SOURCE PREP REPORT` nhưng chưa có `SOURCE AUDIT REPORT` -> `audit-promote-source`
3. nếu có `SOURCE AUDIT REPORT` nhưng chưa có `INGEST INPUT LOCK` -> `lock-ingest-input`
4. nếu có `INGEST INPUT LOCK` nhưng chưa có `INGEST ORCHESTRATION REPORT` -> `ingest`
5. nếu có `INGEST ORCHESTRATION REPORT` nhưng chưa có `INGEST GENERATE REPORT` -> `ingest-generate`
6. nếu có `INGEST GENERATE REPORT` nhưng chưa có `INGEST CLOSEOUT REPORT` -> `ingest-index-log`
7. nếu có `INGEST CLOSEOUT REPORT` với `status: DONE` -> `DONE`

Nếu artifact có nhưng ở trạng thái fail/block:

- không được tự nhảy qua stage sau
- phải giữ `BLOCKED`
- phải nêu rõ stage đang giữ lỗi

---

## 7. Execution Modes

Workflow cha chỉ có hai mode:

### Guided

- dừng ở từng gate quan trọng
- phù hợp khi source lớn hoặc state mơ hồ

### Fast-path

- được phép chạy liên tiếp nhiều stage cho đến gate tiếp theo
- vẫn phải đi đủ chain
- không được bỏ stage

`Fast-path` chỉ là cách chạy, không thay đổi process graph.

---

## 8. Gate Rules

- không được chạy `audit-promote-source` khi `prepare-source` chưa `READY`
- không được chạy `lock-ingest-input` khi `audit-promote-source` chưa `PASSED`
- không được chạy `ingest` khi thiếu bất kỳ upstream artifact nào
- không được chạy `ingest-generate` khi `INGEST ORCHESTRATION REPORT` chưa `READY_FOR_GENERATE`
- không được chạy `ingest-index-log` khi `INGEST GENERATE REPORT` chưa `DONE`

---

## 9. Output Contract

Workflow cha phải kết thúc bằng:

```yaml
INGEST LIFECYCLE REPORT:
  source_id: "[ID] | UNKNOWN"
  current_stage: "[stage]"
  next_stage: "[stage | DONE | BLOCKED]"
  mode: "guided | fast-path"
  lifecycle_status: "DONE | BLOCKED | WAITING_FOR_REVIEW | IN_PROGRESS"
  final_artifact: "[path | NONE]"
  fail_reason: "NONE | ..."
```

---

## 10. Pressure Test Scope

Pressure test nên nhắm vào workflow cha này, không chỉ từng workflow con.

### Contract Tests

- phát hiện thiếu artifact đúng stage
- không cho skip stage
- resume đúng stage kế tiếp

### Path Tests

- happy path: full chain thành công
- blocked path: fail tại từng gate chính
- resume path: dừng giữa chừng rồi tiếp tục đúng artifact

### Scale Tests

- PDF nhỏ
- PDF trung bình
- PDF lớn

Mục tiêu của pressure test là kiểm tra orchestration stability, không chỉ test parser riêng lẻ.

---

## 11. Guardrails

- không dùng đoán trạng thái thay cho artifact contract
- không cho fresh run bắt đầu từ stage giữa chừng
- không coi checkpoint-stop là workflow completion
- không để workflow cha nuốt mất boundary của workflow con

---

## 12. References

- `.agent/workflows/prepare-source.md`
- `.agent/workflows/audit-promote-source.md`
- `.agent/workflows/lock-ingest-input.md`
- `.agent/workflows/ingest.md`
- `.agent/workflows/ingest-generate.md`
- `.agent/workflows/ingest-index-log.md`

