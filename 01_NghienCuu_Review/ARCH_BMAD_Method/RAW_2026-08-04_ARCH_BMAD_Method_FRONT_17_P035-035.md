# HD SOURCE: ARCH_BMAD_Method_FRONT_17_P035-035
Source PDF: ARCH_BMAD_Method.pdf
Extracted Images: 0
Structure Mode: chapter>section>page
Chunk Unit ID: FRONT_17
Part Title: NONE
Chapter Title: NONE
Section Title: 2.4 cách các concepts liên kết nhau
Chunk Range: Pages 35 to 35
Manifest File: RAW_2026-08-04_ARCH_BMAD_Method_MANIFEST.md
---

```
Bước 1: Agent tải các tài liệu phân tích nếu có (product-brief, market-research) ↓ Bước 2: Agent phỏng vấn bạn vềngười dùng và pain points ↓ Bước 3: Checkpoint Preview  -  bạn review và xác nhận personas ↓ Bước 4: Agent phỏng vấn về requirements ↓ Bước 5: Agent offer Advanced Elicitation (tùy chọn) ↓ Bước 6: Checkpoint Preview  -  bạn review requirements ↓ Bước 7: Agent phỏng vấn về success metrics ↓ Bước 8: Agent tổng hợp và tạo PRD.md hoàn chỉnh ↓ Bước 9: bmad-help tự động chạy để đề xuất bước tiếp theo
```

Điều đặc biệt của workflow là bạn không phải nhớ hay theo dõi quy trình  -  workflow dẫn bạn qua từng bước, hiện checkpoint tại các điểm quyết định quan trọng, và tự động tạo tài liệu đầu ra.

## Khái niệm 4: Task

Task làmột đơn vịcông việc nhỏ , cóthể tái sử dụng, thường được điều phối bên trong workflow.

Người dùng thường không tương tác trực tiếp với task  chúng là "bánh răng bên trong" của workflow. Ví dụ : khi chạy bmad-create-architecture , workflow cóthể gọi nhiều tasks bên trong nhưtask-analyze-prd , task-generate-adrs , task-create-directorystructure .

Bạn biết đến task gián tiếp khi thấy agent đang làm từng bước cụthể trong quátrình chạy workflow.

## 2.4 cách các concepts liên kết nhau

Hãy nhìn vào một ví dụ để thấy bốn khái niệm hoạt động cùng nhau:

```
Bạn gõ: bmad-create-prd ↓ [Skill] bmad-create-prd Gọi và khởi chạy ↓ [Workflow] create-prd.yaml Điều phối chuỗi tasks Kích hoạt và sử dụng ↓ [Agent] PM Agent (Amelia) Thực thi từng bước Gọi khi cần ↓
```

```
[Tasks] analyze-context, interview-personas, elicit-requirements, generate-prd...
```