---
description: "Hợp đồng đặc tả 6 cổng kiểm soát (Stage Gates) nội bộ của quy trình Ingest Lifecycle chính thức."
visibility: "internal_stage"
parent_workflow: "ingest-lifecycle"
user_entrypoint: false
---

# Ingest Stage Contracts

Hồ sơ đặc tả chi tiết 6 cổng kiểm soát kỹ thuật nội bộ (Stage Gates) của quy trình nạp tri thức chính thức (Canonical Ingest Lifecycle). 6 cổng kiểm soát này bắt buộc phải tuân thủ để ngăn chặn ảo tưởng tri thức (hallucination), kiểm chứng dữ liệu, chống nạp trùng nguồn tri thức và cho phép khôi phục chính xác (resume) nếu quy trình bị gián đoạn.

---

## Stage 1: prepare-source

*   **Mô tả gốc:** Chuẩn bị source evidence file trước mọi ingest run.
*   **Runtime Boundary:** Xác định source trong chat là read-only; stage/copy file vào `00_Inbox/sources/[source_id]/` hoặc tạo run package trong `runs/` là side effect và cần AN GO.
*   **Hạn chế:** Không tạo Atom, không promote vào Wiki, và không bắt đầu ingest chính.

### 1. Mục tiêu
*   Xác định đúng `source_evidence_file`
*   Xác định `source_type`
*   Đưa nguồn vào đúng khu staging ban đầu
*   Chọn đúng mode `source-scoped staging` hay `run package`
*   Tránh việc nhiều file cạnh tranh vai trò evidence trong cùng một ingest run

### 2. Đầu vào
Source có thể là: PDF, DOCX, PPTX, Markdown, HTML export, audio file, video file, hoặc URL web.

### 3. Hành động chi tiết
1. Xác định source user muốn ingest là gì.
2. Chuẩn hóa source về một `source_evidence_file` duy nhất.
3. Nếu source là file ngoài:
   - Stage vào `00_Inbox/sources/[source_id]/` với source đơn giản.
   - Hoặc tạo run package dưới `runs/ingest_[source_id]_[YYYYMMDD]_[seq]/` với source phức tạp, AI-first, hoặc rerun cần resume.
4. Nếu source là URL:
   - Chưa ingest trực tiếp.
   - Chỉ ghi nhận URL làm evidence source ban đầu và chuyển sang workflow acquisition phù hợp nếu cần.
5. Xác định `source_type`.
6. Xác định `intake_mode`: `FRESH_STAGED_SOURCE` | `EXISTING_MANAGED_SOURCE_RERUN` | `LIVE_SOURCE_PENDING_ACQUISITION`.
7. Kiểm tra xem có nhiều source cùng cạnh tranh một ingest run hay không.

### 4. Quy tắc vận hành
*   Một ingest run chỉ có đúng một `source_evidence_file`.
*   Không được tự promote file vào `3-resources/`.
*   Không được tự tạo `primary_ingest_file`.
*   Không được để lifecycle control artifacts phẳng trực tiếp trong `00_Inbox/` nếu source đã có `source_id` hoặc run scope rõ ràng.
*   Không được tạo source folder con trong `3-resources/raw_*`.
*   Nếu source còn mơ hồ hoặc user chưa chọn rõ, workflow phải `BLOCKED`.

### 5. Hợp đồng đầu ra (Output Contract)
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

### 6. Tiêu chí hoàn thành (READY Criteria)
`READY` chỉ khi:
*   `source_evidence_file` đã rõ và chỉ có một file duy nhất cho ingest run này.
*   `source_type` đã rõ.
*   Source đã ở đúng nơi staging ban đầu hoặc đã được chỉ rõ là URL/source ngoài.
*   `staging_location` và `intake_mode` phản ánh đúng run hiện tại.

### 7. Điều kiện tắc nghẽn (BLOCKED Conditions)
*   User chưa xác định source nào là nguồn chính.
*   Có nhiều file cạnh tranh vai trò source evidence.
*   Source type chưa xác định được hoặc file chưa được stage đúng nơi.

### 8. Downstream Consumer
Output của stage này là input bắt buộc cho: **Stage 2: audit-promote-source**.

---

## Stage 2: audit-promote-source

*   **Mô tả gốc:** Audit và promote source artifact để tạo ingest-reading artifact chính.
*   **Runtime Boundary:** Audit read-only có thể chạy trước GO; promote hoặc tạo artifact mới là side effect và cần AN GO theo `AGENTS.md`.
*   **Hạn chế:** Không bắt đầu Phase 0 của ingest chính.

### 1. Mục tiêu
*   Audit source đã được chuẩn bị.
*   Tạo hoặc xác nhận `primary_ingest_file`.
*   Đảm bảo artifact đọc chính đủ sạch để làm ingest-reading input.

### 2. Đầu vào bắt buộc
```yaml
SOURCE PREP REPORT:
  staging_status: "READY"
```

### 3. Hành động chi tiết
1. Đọc `SOURCE PREP REPORT`.
2. Xác nhận `source_evidence_file` có hợp lệ.
3. Chọn workflow audit/promote phù hợp theo `source_type`.
4. Tạo hoặc xác nhận đúng một `primary_ingest_file`.
5. Ghi rõ `artifact_type`.
6. Nếu audit fail hoặc artifact đọc không rõ ràng, dừng tại đây.

### 4. Quy tắc vận hành
*   `primary_ingest_file` là ingest-reading input chính.
*   Với PDF lớn: PDF là evidence, còn artifact text/structured output mới là thứ ingest sẽ đọc mặc định.
*   Không được để nhiều artifact text cạnh tranh vai trò `primary_ingest_file`.
*   Không được vào ingest chính nếu audit chưa `PASSED`.

### 5. Hợp đồng đầu ra (Output Contract)
```yaml
SOURCE AUDIT REPORT:
  source_evidence_file: "[path or URL]"
  promoted_artifact: "[path]"
  artifact_type: "raw_ingest_md | staged_md | transcript | web_md | structure_stub | other"
  audit_status: "PASSED | FAILED | BLOCKED"
  ready_for_input_lock: "YES | NO"
  fail_reason: "NONE | ..."
```

### 6. Tiêu chí hoàn thành (PASSED Criteria)
`PASSED` chỉ khi:
*   Source prep đã `READY`.
*   Có đúng một `promoted_artifact` và `artifact_type` đã rõ.
*   Artifact đã đủ điều kiện để trở thành `primary_ingest_file`.

### 7. Điều kiện tắc nghẽn (BLOCKED / FAILED Conditions)
*   Source prep chưa `READY`.
*   Không tạo/xác định được `promoted_artifact` hoặc có nhiều artifact cạnh tranh nhau.
*   Audit chưa pass hoặc artifact chưa đủ chất lượng để làm ingest-reading input.

### 8. Downstream Consumer
Output của stage này là input bắt buộc cho: **Stage 3: lock-ingest-input**.

---

## Stage 3: lock-ingest-input

*   **Mô tả gốc:** Khóa source_evidence_file, primary_ingest_file, và source_id trước khi vào ingest chính.
*   **Runtime Boundary:** Kiểm tra nhất quán là read-only; ghi `INGEST INPUT LOCK` ra file là side effect và cần AN GO.
*   **Hạn chế:** Không tạo `STRUCTURE`, `FIGURES`, `MAP`, `NAMING_LOCK`, hoặc Atom.

### 1. Mục tiêu
*   Khóa 3 trường đầu vào bất biến cho ingest run: `source_evidence_file`, `primary_ingest_file`, và `source_id`.
*   Chốt artifact control nào là active cho source/run hiện tại.

### 2. Đầu vào bắt buộc
```yaml
SOURCE PREP REPORT:
  staging_status: "READY"

SOURCE AUDIT REPORT:
  audit_status: "PASSED"
  ready_for_input_lock: "YES"
```

### 3. Hành động chi tiết
1. Đọc `SOURCE PREP REPORT` và `SOURCE AUDIT REPORT`.
2. Xác nhận `source_evidence_file` và `promoted_artifact` cùng chỉ về một source logic.
3. Gán: `source_evidence_file`, `primary_ingest_file = promoted_artifact` và `source_id`.
4. Kiểm tra không có ingest-reading file cạnh tranh.
5. Resolve artifact control path active cho run hiện tại: `00_Inbox/sources/[source_id]/` hoặc `runs/ingest_[source_id]_[YYYYMMDD]_[seq]/`.
6. Nếu mọi thứ nhất quán, khóa input cho ingest chính.

### 4. Quy tắc vận hành
*   Một ingest run chỉ có đúng một `source_evidence_file` và một `primary_ingest_file`.
*   `source_id` phải là anchor định danh duy nhất cho mọi artifact downstream.
*   `source_id` không được tự suy ra lại từ display title, title slug, hay raw filename stem nếu naming lock đã tồn tại.
*   Lifecycle control artifact filenames phải dùng `source_id` đã khóa, không dùng title slug thay thế.
*   `INGEST INPUT LOCK` không được đặt trong `1-projects/`.
*   Lifecycle control artifacts không satisfy official ingest gates chỉ vì nằm đúng thư mục; run hiện tại phải resolve chúng là active artifacts cho source/run đó.
*   Nếu ba trường này chưa khóa được, stage tiếp theo phải `BLOCKED`.

### 5. Hợp đồng đầu ra (Output Contract)
```yaml
INGEST INPUT LOCK:
  source_evidence_file: "[path]"
  primary_ingest_file: "[path]"
  source_id: "[ID]"
  active_control_path: "00_Inbox/sources/[source_id] | runs/ingest_[source_id]_[YYYYMMDD]_[seq]"
  status: "READY | BLOCKED"
  fail_reason: "NONE | ..."
```

### 6. Tiêu chí hoàn thành (READY Criteria)
`READY` chỉ khi:
*   `SOURCE PREP REPORT` đã `READY` và `SOURCE AUDIT REPORT` đã `PASSED`.
*   Có đúng một `source_evidence_file` và một `primary_ingest_file`.
*   `source_id` và `active_control_path` đã chốt.

### 7. Điều kiện tắc nghẽn (BLOCKED Conditions)
*   Thiếu `SOURCE PREP REPORT` hoặc `SOURCE AUDIT REPORT`.
*   `audit_status` chưa `PASSED` hoặc `source_id` chưa chốt.
*   Có nhiều candidate cho `primary_ingest_file` hoặc hai file evidence/artifact không trỏ về cùng một source logic.

### 8. Downstream Consumer
Output của stage này là prerequisite bắt buộc cho: **Stage 4: ingest**.

---

## Stage 4: ingest

*   **Mô tả gốc:** Orchestration-only stage cho source-first ingest sau khi upstream artifacts đã được khóa.
*   **Runtime Boundary:** `@scout` được phân tích và đề xuất analysis/candidates. Nếu cần ghi/cập nhật artifact phân tích, phải có AN GO theo `AGENTS.md`. Tạo atom thật thuộc `ingest-generate` và do `@engineer` thực hiện sau GO.

### 1. Mục tiêu
*   Kiểm tra output artifact của các stage trước đã đủ hay chưa.
*   Nếu đủ thì vào `Phase 0+` để lập kế hoạch cấu trúc và phân tích.
*   Nếu thiếu thì `BLOCKED` và chỉ ra workflow nào còn thiếu.
*   Điều phối các artifact phân tích cấp ingest: `STRUCTURE_[ID].md`, `FIGURES_[ID].md`, `NAMING_LOCK_[ID].md`, `MAP_[ID].md`, `Analysis_[ID]_MASTER_STRATEGY.md`, và `Analysis_[ID]_CHUNK_XX.md`.

### 2. Đầu vào bắt buộc
```yaml
SOURCE PREP REPORT:
  staging_status: "READY"

SOURCE AUDIT REPORT:
  audit_status: "PASSED"
  ready_for_input_lock: "YES"

INGEST INPUT LOCK:
  status: "READY"
```

### 3. Hành động chi tiết
1. Thực hiện Precheck: Đảm bảo cả 3 upstream reports đều có giá trị `YES`.
2. **Phase 0 (Structure, Figures, Naming Lock, Map):** Tạo hoặc cập nhật các tệp tin cấu trúc và định danh trong `1-projects/sources/[source_id]/`.
3. **Phase 0.5 (Master Strategy):** Đọc `primary_ingest_file` để lập lộ trình chia chunk phân tích.
4. **Phase 1 (Anchor Planning):** Lập kế hoạch anchor set (Source Node, Foundation Entities) và ghi nhận vào `NAMING_LOCK_[ID].md`.
5. **Phase 2 (Chunk Analysis):** Tạo `Analysis_[ID]_CHUNK_XX.md` phân tích tri thức tinh túy của từng chunk và chuyển sang chờ AN duyệt.

### 4. Quy tắc vận hành
*   Mọi thao tác tạo/sửa đổi artifact trong các phase chỉ được thực thi sau khi AN đã cấp GO rõ ràng.
*   Chấp hành nghiêm ngặt **Quy định ngôn ngữ:** Mọi văn bản tiếng Việt cho phần nội dung chính, được giữ tiếng Anh cho metadata, status enums và technical terms khi cần giữ độ chính xác.
*   Không được tự ý làm các bước upstream (prep, audit) hoặc tự ý generate atom thật vào `wiki/`.

### 5. Hợp đồng đầu ra (Output Contract)
```yaml
INGEST ORCHESTRATION REPORT:
  source_id: "[ID]"
  source_evidence_file: "[path]"
  primary_ingest_file: "[path]"
  structure_file: "1-projects/sources/[source_id]/STRUCTURE_[ID].md | NONE"
  figures_file: "1-projects/sources/[source_id]/FIGURES_[ID].md | NONE"
  naming_lock_file: "1-projects/sources/[source_id]/NAMING_LOCK_[ID].md | NONE"
  map_file: "1-projects/sources/[source_id]/MAP_[ID].md | NONE"
  master_strategy_file: "1-projects/sources/[source_id]/Analysis_[ID]_MASTER_STRATEGY.md | NONE"
  chunk_analysis_files:
    - "1-projects/sources/[source_id]/Analysis_[ID]_CHUNK_XX.md"
  next_workflow: "ingest-generate | WAITING_FOR_REVIEW | BLOCKED"
  status: "BLOCKED | WAITING_FOR_REVIEW | READY_FOR_GENERATE"
  gate_reasons:
    - "[reason]"
  projected_end_to_end_outcome:
    - "[what will be materialized if all gates pass]"
```

### 6. Tiêu chí hoàn thành (READY_FOR_GENERATE vs WAITING_FOR_REVIEW)
*   **READY_FOR_GENERATE:** Khi toàn bộ các tệp cấu trúc, định danh (`STRUCTURE`, `NAMING_LOCK`, `MAP`, `FIGURES`) đã sẵn sàng (không còn pending), và mọi chunk analysis trong batch đã được AN duyệt.
*   **WAITING_FOR_REVIEW:** Khi các file cấu trúc cơ bản đã đủ, đã có ít nhất một chunk analysis và còn ít nhất một batch analysis chưa được AN duyệt (chưa có blocker cứng).

### 7. Điều kiện tắc nghẽn (BLOCKED Conditions)
*   Thiếu bất kỳ artifact upstream nào hoặc `audit_status` chưa `PASSED`.
*   Không xác định được `source_id` hay `primary_ingest_file`.
*   `FIGURES_[ID].md` còn `PENDING_EXTRACTION` hoặc `ASSETS_PRESENT_BUT_UNREGISTERED`.

### 8. Downstream Consumer
Output của stage này là input bắt buộc cho: **Stage 5: ingest-generate**.

---

## Stage 5: ingest-generate

*   **Mô tả gốc:** Tạo atom thật từ analysis đã duyệt sau khi ingest orchestration hoàn tất.
*   **Runtime Boundary:** Đây là workflow có side effect vì tạo/patch Atom. Chỉ chạy sau khi có AN GO rõ cho `ingest-generate` và do `@engineer` thực hiện.

### 1. Mục tiêu
*   Đọc `Analysis_[ID]_CHUNK_XX.md` đã duyệt.
*   Tạo source/concept/entity atoms thật theo naming lock.
*   Giữ traceability về `primary_ingest_file`.
*   Xuất báo cáo generate rõ ràng cho bước closeout.

### 2. Đầu vào bắt buộc
```yaml
INGEST ORCHESTRATION REPORT:
  source_id: "[ID]"
  primary_ingest_file: "[path]"
  naming_lock_file: "1-projects/sources/[source_id]/NAMING_LOCK_[ID].md"
  chunk_analysis_files:
    - "1-projects/sources/[source_id]/Analysis_[ID]_CHUNK_XX.md"
  status: "READY_FOR_GENERATE"
```

### 3. Hành động chi tiết
1. Đọc `INGEST ORCHESTRATION REPORT` và `primary_ingest_file`.
2. Đọc `NAMING_LOCK_[ID].md`.
3. Với mỗi `Analysis_[ID]_CHUNK_XX.md` đã duyệt, tạo hoặc patch: Source Atom, Concept Atoms, hoặc Entity Atoms.
4. Đảm bảo mỗi atom bám template chuẩn, có đầy đủ wikilinks, evidence và đúng tên tệp canonical.
5. Ghi `WRITE REPORT` cho từng tệp tin thay đổi.

### 4. Quy tắc vận hành
*   Chỉ generate từ analysis đã duyệt và canonical filename phải lấy từ `NAMING_LOCK_[ID].md`.
*   Nếu term/entity chưa được naming lock chốt -> `BLOCKED`.
*   Tuyệt đối cấm Agent tự ý set trạng thái `SYNTHESIZED` (chỉ dành cho AN).
*   Không tự ý thực hiện rebuild filesystem hay index tại stage này.

### 5. Hợp đồng đầu ra (Output Contract)
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

### 6. Tiêu chí hoàn thành (DONE Criteria)
`DONE` chỉ khi:
*   Orchestration report là `READY_FOR_GENERATE` và chunk analysis đã duyệt.
*   Mọi filename đều khớp naming lock và không có atom nào được tạo từ khái niệm chưa khóa tên.
*   `FIGURES_[ID].md` không còn trạng thái pending extraction hay unregistered.

### 7. Điều kiện tắc nghẽn (BLOCKED Conditions)
*   Thiếu orchestration report hoặc status chưa `READY_FOR_GENERATE`.
*   Chunk analysis chưa được duyệt hoặc `NAMING_LOCK_[ID].md` thiếu mapping.
*   `FIGURES_[ID].md` còn `PENDING_EXTRACTION` hoặc `ASSETS_PRESENT_BUT_UNREGISTERED`.

### 8. Downstream Consumer
Output của stage này là input bắt buộc cho: **Stage 6: ingest-index-log**.

---

## Stage 6: ingest-index-log

*   **Mô tả gốc:** Rebuild, append log, và closeout bookkeeping sau khi ingest-generate hoàn tất.
*   **Runtime Boundary:** Rebuild, append log và bookkeeping là side effect. Chỉ chạy khi GO ban đầu bao gồm closeout hoặc AN cấp GO riêng cho `ingest-index-log`.

### 1. Mục tiêu
*   Rebuild filesystem -> DB/index.
*   Append ingest log.
*   Hoàn tất post-ingest bookkeeping.

### 2. Đầu vào bắt buộc
```yaml
INGEST GENERATE REPORT:
  source_id: "[ID]"
  status: "DONE"
```

### 3. Hành động chi tiết
1. Đọc `INGEST GENERATE REPORT`.
2. Chạy rebuild phù hợp để đồng bộ filesystem và index database.
3. Ghi closeout log cho ingest run, thống kê các tệp đã tạo hoặc patch.
4. Chốt trạng thái bookkeeping của run hiện tại.

### 4. Quy tắc vận hành & Log Scope
*   Log closeout phải ghi nhận rõ: `source_id`, evidence file, list atoms thay đổi và số lượng thay đổi.
*   Không chạy stage này nếu atom generation chưa xong.
*   Không sửa ngược lại artifact orchestration để che giấu lỗi generate.
*   Nếu rebuild filesystem/index fail, bắt buộc phải báo trạng thái `FAILED` để giữ an toàn dữ liệu.

### 5. Hợp đồng đầu ra (Output Contract)
```yaml
INGEST CLOSEOUT REPORT:
  source_id: "[ID]"
  rebuild_status: "DONE | FAILED"
  log_status: "DONE | FAILED"
  bookkeeping_status: "DONE | FAILED"
  status: "DONE | BLOCKED"
  fail_reason: "NONE | ..."
```

### 6. Tiêu chí hoàn thành (DONE Criteria)
`DONE` chỉ khi:
*   Generate report là `DONE`.
*   Rebuild, log và bookkeeping đều hoàn tất thành công.

### 7. Điều kiện tắc nghẽn (BLOCKED Conditions)
*   Thiếu generate report hoặc status chưa `DONE`.
*   Rebuild thất bại hoặc append log thất bại.
