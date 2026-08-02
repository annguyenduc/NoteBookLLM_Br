---
description: Default lightweight workflow for learning quickly and deciding whether a source deserves official ingest
---

# Workflow: learning-first

`learning-first` là workflow mặc định của vault.

Mục tiêu không phải đọc hết tài liệu hoặc ingest mọi thứ. Mục tiêu là giúp AN học nhanh hơn và tra cứu nhanh hơn.

```text
Capture -> Learn Note -> Promote if valuable
```

---

## 1. Khi dùng

Dùng workflow này khi AN nói:

- đọc nhanh tài liệu này
- tài liệu này có đáng học không
- tạo bản đồ học (learning map)
- thiết lập sơ đồ tri thức phi tuyến tính / bản đồ học ngữ nghĩa (Semantic Learning Map Mode)
- tóm tắt để tra cứu nhanh
- dùng NotebookLM để hỏi tài liệu dài
- tôi cần giải quyết vấn đề này, tìm phần liên quan trong sách

Không dùng workflow này khi AN gọi rõ:

```text
/ingest [file]
```

hoặc yêu cầu official ingest vào vault canonical.

---

## 2. Ba bước tối giản

### Bước 1: Capture

Nhận nguồn và xác định mục tiêu học.

Allowed inputs:

- file trong `00_Inbox/`
- file trong `workspaces/*/`
- tài liệu đã có trong NotebookLM
- URL hoặc ghi chú thủ công, nếu user cung cấp

Output trong bước này mặc định là chat, không ghi file nếu chưa được yêu cầu.

Mọi output learning-first phải bắt đầu bằng routing trace:

```yaml
ROUTING_DECISION:
  cwd_context: "vault_root | workspace_child"
  selected_workspace: "[provided by .agent/config/workspace-routing.yaml]"
  mode: "learning-first"
  reason: "[why this is learning-first instead of official ingest]"
  loaded_overlay: "[provided by workspace routing registry | NONE]"
  action_type: "read-only/chat-only | write-preview-artifact"
  write_artifact: "NO | YES"
  canonical_write: "NO"
  ingest_lifecycle: "NO"
  forbidden_actions_checked:
    - "no 3-resources write"
    - "no Atom generation"
    - "no VERIFIED/SYNTHESIZED"
    - "no ingest-lifecycle"
```

### Bước 2: Learn Note & Semantic Learning Map

Tạo câu trả lời ngắn, learning note, hoặc sơ đồ tri thức phi tuyến tính.

#### A. Chế độ Ghi chú học nhanh (Learning Note Mode)
Đầu ra mặc định là câu trả lời ngắn gọn trong chat hoặc tệp ghi chú tóm tắt.

Output contract:
```yaml
ROUTING_DECISION:
  cwd_context: "vault_root | workspace_child"
  selected_workspace: "[provided by workspace routing registry]"
  mode: "learning-first"
  action_type: "read-only/chat-only | write-preview-artifact"
  write_artifact: "NO | YES"
  canonical_write: "NO"
  ingest_lifecycle: "NO"
LEARNING NOTE:
  learning_status: "PREVIEW_ONLY"
  canonical_status: "NON_CANONICAL"
  source_id: "NONE"
  trust: "UNVERIFIED"
  recommendation: "SKIP | KEEP_SUMMARY | PROMOTE"
```

Template nội dung:
```md
# Learning Map - [Title]

## Vấn đề đang giải quyết
## Câu trả lời ngắn
## Cấu trúc tài liệu
## Câu hỏi chính
## Phần đáng đọc trước
## Khái niệm cần nhớ
## Phần có thể bỏ qua
## Có đáng đưa vào wiki không?
SKIP | KEEP_SUMMARY | PROMOTE
```

#### B. Chế độ Bản đồ ngữ nghĩa phi tuyến (Semantic Learning Map Mode)
Được kích hoạt khi người dùng yêu cầu lập sơ đồ tri thức, kết nối chéo giữa các Atoms để đọc phi tuyến tính.

*   **Đầu ra:** Bản đồ đồ thị Mermaid Render mô tả mối quan hệ ngữ nghĩa giữa các nhóm Atoms và danh sách liên kết Obsidian dạng `[[CONCEPT_*]]` để điều hướng nhanh.
*   **Vị trí lưu trữ bắt buộc (Non-canonical Preview):**
    👉 **`1-projects/learning_maps/PATH_ARCH_TIS_[NAME].md`**
*   **Ranh giới cấm ghi tuyệt đối (Guardrails):**
    - Cấm ghi trực tiếp sơ đồ tri thức này vào thư mục tri thức chính thức `3-resources/` hoặc `3-resources/wiki/synthesis/`.
    - Đối với việc tạo tệp sơ đồ ngữ nghĩa tổng vĩ mô chính thức (`SYNTHESIS_ARCH_TIS_Semantic_Graph.md` tại `3-resources/wiki/synthesis/`), đây là tác vụ **synthesis write** rủi ro cao, bắt buộc phải tách thành một task độc lập ở tương lai, được bảo vệ bằng `synthesis_guard.py` và cần có exact-path GO riêng từ AN.

#### C. Quy tắc lưu trữ chung cho Workflow:
Persisted learning notes / semantic paths khi được phép ghi file, ưu tiên:
```text
1-projects/learning_maps/
```
Không ghi bất kỳ tệp tin nào của workflow này vào:
```text
3-resources/
3-resources/wiki/
3-resources/raw_sources/
3-resources/raw_ingest/
3-resources/raw_assets/
```

### Bước 3: Promote if valuable

Chỉ khi recommendation là `PROMOTE` và AN đồng ý, handoff sang:

```text
.agent/workflows/ingest-lifecycle.md
```

Không tự tạo `source_id`, Atom, audit stamp, `VERIFIED`, hoặc `SYNTHESIZED` trong workflow này.

---

## 3. Tài liệu dài

Với tài liệu 500-1000 trang, không đọc tuần tự từ đầu đến cuối.

Thứ tự đúng:

```text
NotebookLM query
-> structure map
-> problem/question selection
-> targeted reading
-> learning note
```

NotebookLM output là reconnaissance (trinh sát), không phải source of truth.

Agent phải ghi rõ khi dùng thông tin chưa verify:

```yaml
recon_status: "UNVERIFIED"
source_truth: "NO"
```

---

## 4. MCP tối thiểu

Default MCP set cho learning-first:

```text
filesystem
notebooklm-mcp-server
sqlite
tavily
```

Nếu Tavily chưa được bật trong `codex mcp list` hoặc `antigravity mcp list`, báo thiếu MCP và tiếp tục bằng nguồn hiện có nếu task không bắt buộc Tavily.

---

## 5. Handoff sang ingest

Khi cần official ingest, output phải ngắn:

```yaml
LEARNING FIRST HANDOFF:
  source_input: "[path]"
  reason_to_promote:
    - "[why this deserves canonical ingest]"
  suggested_next_workflow: "ingest-lifecycle"
  canonical_write_done: "NO"
```
