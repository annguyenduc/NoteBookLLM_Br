---
description: Chuẩn bị source evidence file trước mọi ingest run
---

# Workflow: prepare-source

Workflow này chuẩn hóa bước tiếp nhận nguồn mới trước khi audit hoặc ingest.

Runtime boundary: xác định source trong chat là read-only; stage/copy file vào `00_Inbox/sources/[source_id]/` hoặc tạo run package trong `runs/` là side effect và cần AN GO.

`prepare-source` không tạo Atom, không promote vào Wiki, và không bắt đầu ingest chính.

---

## 1. Mục tiêu

- Xác định đúng `source_evidence_file`
- Xác định `source_type`
- Đưa nguồn vào đúng khu staging ban đầu
- Chọn đúng mode `source-scoped staging` hay `run package`
- Tránh việc nhiều file cạnh tranh vai trò evidence trong cùng một ingest run

---

## 2. Đầu vào

Source có thể là:
- PDF
- DOCX
- PPTX
- Markdown
- HTML export
- audio file
- video file
- URL web

---

## 3. Hành động

1. Xác định source user muốn ingest là gì.
2. Chuẩn hóa source về một `source_evidence_file` duy nhất.
3. Nếu source là file ngoài:
   - stage vào `00_Inbox/sources/[source_id]/` với source đơn giản
   - hoặc tạo run package dưới `runs/ingest_[source_id]_[YYYYMMDD]_[seq]/` với source phức tạp, AI-first, hoặc rerun cần resume
4. Nếu source là URL:
   - chưa ingest trực tiếp
   - chỉ ghi nhận URL làm evidence source ban đầu và chuyển sang workflow acquisition phù hợp nếu cần
5. Xác định `source_type`.
6. Xác định `intake_mode`:
   - `FRESH_STAGED_SOURCE`
   - `EXISTING_MANAGED_SOURCE_RERUN`
   - `LIVE_SOURCE_PENDING_ACQUISITION`
7. Kiểm tra xem có nhiều source cùng cạnh tranh một ingest run hay không.

---

## 4. Quy tắc

- Một ingest run chỉ có đúng một `source_evidence_file`.
- `prepare-source` không được tự promote file vào `3-resources/`.
- `prepare-source` không được tự tạo `primary_ingest_file`.
- `prepare-source` không được để lifecycle control artifacts phẳng trực tiếp trong `00_Inbox/` nếu source đã có `source_id` hoặc run scope rõ ràng.
- `prepare-source` không được tạo source folder con trong `3-resources/raw_*`.
- Nếu source còn mơ hồ hoặc user chưa chọn rõ, workflow phải `BLOCKED`.

---

## 5. Output Contract

```yaml
SOURCE PREP REPORT:
  source_evidence_file: "[path or URL]"
  source_type: "pdf | docx | pptx | markdown | html | web | video | audio | unknown"
  staging_location: "00_Inbox/sources/[source_id] | runs/ingest_[source_id]_[YYYYMMDD]_[seq] | external URL | existing managed path"
  intake_mode: "FRESH_STAGED_SOURCE | EXISTING_MANAGED_SOURCE_RERUN | LIVE_SOURCE_PENDING_ACQUISITION"
  single_source_confirmed: "YES | NO"
  staging_status: "READY | BLOCKED"
  fail_reason: "NONE | ..."
```

---

## 6. READY Criteria

`READY` chỉ khi:
- `source_evidence_file` đã rõ
- `source_type` đã rõ
- chỉ có một source evidence file cho ingest run này
- source đã ở đúng nơi staging ban đầu hoặc đã được chỉ rõ là URL/source ngoài
- `staging_location` và `intake_mode` phản ánh đúng run hiện tại

---

## 7. BLOCKED Conditions

- user chưa xác định source nào là nguồn chính
- có nhiều file cạnh tranh vai trò source evidence
- source type chưa xác định được
- file chưa được stage đúng nơi

---

## 8. Downstream Consumer

Output của workflow này là input bắt buộc cho:
- `audit-promote-source.md`
