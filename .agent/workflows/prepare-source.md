---
description: Chuẩn bị source evidence file trước mọi ingest run
---

# Workflow: prepare-source

Workflow này chuẩn hóa bước tiếp nhận nguồn mới trước khi audit hoặc ingest.

`prepare-source` không tạo Atom, không promote vào Wiki, và không bắt đầu ingest chính.

---

## 1. Mục tiêu

- Xác định đúng `source_evidence_file`
- Xác định `source_type`
- Đưa nguồn vào đúng khu staging ban đầu
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
   - stage vào `00_Inbox/`
4. Nếu source là URL:
   - chưa ingest trực tiếp
   - chỉ ghi nhận URL làm evidence source ban đầu và chuyển sang workflow acquisition phù hợp nếu cần
5. Xác định `source_type`.
6. Kiểm tra xem có nhiều source cùng cạnh tranh một ingest run hay không.

---

## 4. Quy tắc

- Một ingest run chỉ có đúng một `source_evidence_file`.
- `prepare-source` không được tự promote file vào `3-resources/`.
- `prepare-source` không được tự tạo `primary_ingest_file`.
- Nếu source còn mơ hồ hoặc user chưa chọn rõ, workflow phải `BLOCKED`.

---

## 5. Output Contract

```yaml
SOURCE PREP REPORT:
  source_evidence_file: "[path or URL]"
  source_type: "pdf | docx | pptx | markdown | html | web | video | audio | unknown"
  staging_location: "00_Inbox | external URL | existing managed path"
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
