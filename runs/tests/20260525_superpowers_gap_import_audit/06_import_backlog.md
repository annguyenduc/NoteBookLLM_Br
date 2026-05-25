# Superpowers Import Backlog (Restructured)

Báo cáo này thiết lập lộ trình chuẩn hóa và nhập khẩu kỹ năng từ Superpowers sang vault `NoteBookLLM_Br` theo mô hình **5 Giai đoạn (5 Phases) có kiểm soát**, lấy triết lý **Kiểm thử đi trước, Tích hợp theo sau (Test-First, Merge-Later)** làm kim chỉ nam vận hành tối thượng để bảo toàn sự ổn định của Antigravity.

---

## Giai đoạn 1 — Test-First Infrastructure (Móng kiểm thử an toàn)
Thiết lập toàn bộ hạ tầng test hồi quy local tại `.agent/tests/` nhằm tạo lớp lưới bảo hiểm (safety net) ngăn Agent bị loạn định tuyến trước khi thay đổi bất kỳ skill nào.

| ID | Action (Hành động) | Source (Nguồn) | Target (Đích) | Decision (Quyết định) | Risk (Rủi ro) | Requires GO |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SPEC-SPG-020** | Adapt Superpowers `skill-triggering` tests for vault routing | `superpowers/tests/skill-triggering` | `.agent/tests/skill-triggering` | adapt_as_test | **Low** (Hoàn toàn local và cực kỳ an toàn) | **Yes** |
| **SPEC-SPG-021** | Adapt Superpowers `explicit-skill-requests` tests | `superpowers/tests/explicit-skill-requests` | `.agent/tests/explicit-skill-requests` | adapt_as_test | **Low** (Tạo chốt chặn chống bypass rules) | **Yes** |

*Chú thích: Hai hoạt động này sẽ được gộp chung dưới một Spec kiểm thử duy nhất: **`SPEC-SPG-020: Adapt Superpowers skill-triggering and explicit-skill-requests tests`**.*

---

## Giai đoạn 2 — Core Phase 0 Adoption (Kích hoạt cổng chào)
Port kỹ năng cổng chào và kỹ năng Phase 0 để chuẩn hóa đầu phiên làm việc.

| ID | Action (Hành động) | Source (Nguồn) | Target (Đích) | Decision (Quyết định) | Risk (Rủi ro) | Requires GO |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SPG-000** | Port & Normalize `using-superpowers` as bootstrap standard | `superpowers/skills/using-superpowers` | `.agent/skills/using-superpowers` | port/normalize | **High** (Dễ ảnh hưởng cách Agent chọn skill) | **Yes** |
| **SPG-000b** | Integrate Antigravity tools and announcement checklist into `using-superpowers` | `.agent/skills/using-superpowers` | `.agent/skills/using-superpowers` | merge/adapt | **Medium** (Tích hợp checklist thông báo) | **Yes** |
| **SPG-001** | Adopt Superpowers `brainstorming` as Phase 0 core skill | `superpowers/skills/brainstorming` | `.agent/skills/brainstorming` | port/normalize | **Medium** (Lấy làm chuẩn chính cho Phase 0) | **Yes** |
| **SPG-001b** | Extract planning & risk logic of `cm-planning` as brainstorming adaptation | `.agent/skills/cm-planning` | `.agent/skills/brainstorming` | merge_into_superpowers | **Medium** (Chuyển cm-planning thành nguồn adaptation) | **Yes** |

---

## Giai đoạn 3 — Verification, TDD & Systematic Debugging (Kiểm thử & Khắc phục lỗi)
Chuẩn hóa bộ kỹ năng thực thi, kiểm thử đệ quy và chẩn đoán lỗi hệ thống ở giữa và cuối task.

| ID | Action (Hành động) | Source (Nguồn) | Target (Đích) | Decision (Quyết định) | Risk (Rủi ro) | Requires GO |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SPG-002** | Adopt Superpowers `test-driven-development` as testing standard | `superpowers/skills/test-driven-development` | `.agent/skills/test-driven-development` | port/normalize | **Medium** (Dễ làm Agent lặp/bỏ kiểm chứng) | **Yes** |
| **SPG-002b** | Move useful `cm-tdd` self-healing logic into `test-driven-development` | `.agent/skills/cm-tdd` | `.agent/skills/test-driven-development` | merge_into_superpowers | **Medium** (Tích hợp logic tự phục hồi đệ quy) | **Yes** |
| **SPG-003** | Adopt Superpowers `systematic-debugging` as main debugging skill | `superpowers/skills/systematic-debugging` | `.agent/skills/systematic-debugging` | port/normalize | **Low** (Không có rủi ro lớn) | **Yes** |
| **SPG-003b** | Extract vault-specific RCA checklist from `cm-debugging` into `systematic-debugging` | `.agent/skills/cm-debugging` | `.agent/skills/systematic-debugging` | merge_into_superpowers | **Low** (Gom các checklist chẩn đoán đặc thù) | **Yes** |

---

## Giai đoạn 4 — Parallel Subagents & Review Mechanics (Điều phối & Rà soát)
Chuẩn hóa quy trình điều phối tác nhân song song phức tạp và rà soát chất lượng code.

| ID | Action (Hành động) | Source (Nguồn) | Target (Đích) | Decision (Quyết định) | Risk (Rủi ro) | Requires GO |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SPG-004** | Adopt Superpowers code review pair (requesting & receiving review) | `requesting-code-review`, `receiving-code-review` | `.agent/skills/requesting-code-review`, `receiving-code-review` | port/normalize | **Medium** (Phải loại bỏ hoàn toàn GitHub PR) | **Yes** |
| **SPG-004b** | Extract review guidelines from `cm-code-review` | `.agent/skills/cm-code-review` | `.agent/skills/requesting-code-review` | merge/adapt | **Low** (Tích hợp checklist review) | **Yes** |
| **SPG-010** | Port `dispatching-parallel-agents` as controlled multi-agent dispatcher | `superpowers/skills/dispatching-parallel-agents` | `.agent/skills/dispatching-parallel-agents` | port | **High** (Dễ gây phình context và tốn token) | **Yes** |

*Chú thích: Kỹ năng `dispatching-parallel-agents` chỉ được kích hoạt sau khi các test case về kiểm soát ngân sách token (token budget) thông qua `cm-context-budget` đã chạy thử nghiệm thành công.*

---

## Giai đoạn 5 — Deprecate & Archive (Lưu trữ và Dọn dẹp)
Lưu trữ và đóng băng các kỹ năng cũ của vault sau khi các test case kiểm chứng hành vi tương đương vượt qua 100%.

| ID | Action (Hành động) | Target (Đích) | Decision (Quyết định) | Condition to Execute (Điều kiện kích hoạt) | Requires GO |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **SPG-DEP-01** | Archive `cm-planning` | `4-archive/skills/cm-planning` | archive_deprecated | Khi `brainstorming` chuẩn đã pass test T003/T004 | **Yes** |
| **SPG-DEP-02** | Archive `cm-tdd` | `4-archive/skills/cm-tdd` | archive_deprecated | Khi `test-driven-development` đã pass test TDD | **Yes** |
| **SPG-DEP-03** | Archive `cm-debugging` | `4-archive/skills/cm-debugging` | archive_deprecated | Khi `systematic-debugging` đã pass test debugging | **Yes** |
| **SPG-DEP-04** | Archive `cm-code-review` | `4-archive/skills/cm-code-review` | archive_deprecated | Khi bộ đôi review mới đã pass test | **Yes** |

