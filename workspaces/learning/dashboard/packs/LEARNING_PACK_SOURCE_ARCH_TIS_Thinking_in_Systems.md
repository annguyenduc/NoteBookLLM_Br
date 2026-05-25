---
title: "LEARNING_PACK_ARCH_TIS_Fast_Start"
type: "learning_pack"
source_id: "ARCH_TIS"
status: "LEARNING_DRAFT"
learning_pack_status: "EXPLORATORY"
owner: "@librarian"
created_at: "2026-05-20"
---

# Big Picture

**EXPLORATORY Learning Pack** vì các atom `ARCH_TIS` hiện đọc được đều đang `status: "DRAFT"`. Các claim dưới đây dùng atom có `source_ref` / `source_file`, nhưng chưa trình bày như synthesis đã chốt.

`Thinking in Systems` nên học theo một đường chính:

```text
System
-> Structure creates behavior
-> Stocks/Flows create state change
-> Feedback loops create dynamics
-> Delays create oscillation/overshoot
-> Boundaries decide what you can see
-> Traps reveal repeated failure patterns
-> Leverage points show where to intervene
-> Systems wisdom is the operating mindset
```

Mục tiêu 60-90 phút: không thuộc lòng toàn bộ concept, mà nắm được cách nhìn hệ thống để áp dụng vào một vấn đề thật.

# Key Concepts

1. **System**: một tập hợp phần tử kết nối với nhau để tạo ra mục đích hoặc hành vi chung.
2. **System Structure**: cấu trúc quan hệ, luồng, stock, feedback và rule là nguyên nhân sâu hơn của hành vi.
3. **Event / Behavior / Structure**: sự kiện là bề mặt; pattern hành vi và cấu trúc mới là tầng cần phân tích.
4. **Stock**: trạng thái tích lũy của hệ thống tại một thời điểm.
5. **Flow**: dòng vào / dòng ra làm stock tăng hoặc giảm theo thời gian.
6. **Feedback Loop**: vòng phản hồi khiến hành động hôm nay quay lại ảnh hưởng trạng thái tương lai.
7. **Balancing Feedback**: vòng phản hồi kéo hệ về mục tiêu hoặc trạng thái cân bằng.
8. **Reinforcing Feedback**: vòng phản hồi khuếch đại tăng trưởng hoặc suy giảm.
9. **Delay**: độ trễ giữa hành động và kết quả, thường gây dao động hoặc overcorrection.
10. **System Boundaries**: ranh giới quyết định cái gì được tính vào phân tích và cái gì bị bỏ ngoài.
11. **System Traps**: mẫu lỗi lặp lại do cấu trúc hệ thống, không chỉ do con người ra quyết định kém.
12. **Leverage Points**: điểm can thiệp có sức đổi hệ thống, từ tham số nông đến mục tiêu và mindset sâu.
13. **Resilience / Self-Organization / Hierarchy**: năng lực hệ thống hấp thụ biến động, tự tái cấu trúc, và tổ chức nhiều tầng.
14. **Systems Wisdom**: thái độ vận hành khi làm việc với hệ thống phức tạp: khiêm tốn, quan sát feedback, thử nhỏ, và học từ hành vi thật.

# Concept Map

```text
[[CONCEPT_ARCH_TIS_System]]
├─ [[CONCEPT_ARCH_TIS_System_Structure]]
│  ├─ [[CONCEPT_ARCH_TIS_Event_Behavior_Structure]]
│  ├─ [[CONCEPT_ARCH_TIS_System_Boundaries]]
│  └─ [[CONCEPT_ARCH_TIS_Hierarchy]]
├─ [[CONCEPT_ARCH_TIS_Stock]]
│  └─ [[CONCEPT_ARCH_TIS_Flow]]
├─ [[CONCEPT_ARCH_TIS_Feedback_Loop]]
│  ├─ [[CONCEPT_ARCH_TIS_Balancing_Feedback]]
│  ├─ [[CONCEPT_ARCH_TIS_Reinforcing_Feedback]]
│  ├─ [[CONCEPT_ARCH_TIS_Delay]]
│  └─ [[CONCEPT_ARCH_TIS_Oscillation]]
├─ [[CONCEPT_ARCH_TIS_System_Traps]]
│  ├─ [[CONCEPT_ARCH_TIS_Tragedy_of_Commons]]
│  └─ [[CONCEPT_ARCH_TIS_Escalation]]
└─ [[CONCEPT_ARCH_TIS_Leverage_Points]]
   ├─ [[CONCEPT_ARCH_TIS_Resilience]]
   ├─ [[CONCEPT_ARCH_TIS_Self_Organization]]
   └─ [[CONCEPT_ARCH_TIS_Systems_Wisdom]]
```

# Must-Know Atoms

Học theo thứ tự này trong 60-90 phút:

1. [[SOURCE_ARCH_TIS_Thinking_in_Systems]]
2. [[CONCEPT_ARCH_TIS_System]]
3. [[CONCEPT_ARCH_TIS_System_Structure]]
4. [[CONCEPT_ARCH_TIS_Event_Behavior_Structure]]
5. [[CONCEPT_ARCH_TIS_Stock]]
6. [[CONCEPT_ARCH_TIS_Flow]]
7. [[CONCEPT_ARCH_TIS_Feedback_Loop]]
8. [[CONCEPT_ARCH_TIS_Balancing_Feedback]]
9. [[CONCEPT_ARCH_TIS_Reinforcing_Feedback]]
10. [[CONCEPT_ARCH_TIS_Delay]]
11. [[CONCEPT_ARCH_TIS_System_Boundaries]]
12. [[CONCEPT_ARCH_TIS_System_Traps]]
13. [[CONCEPT_ARCH_TIS_Leverage_Points]]
14. [[CONCEPT_ARCH_TIS_Systems_Wisdom]]

Optional extension nếu còn thời gian:

- [[CONCEPT_ARCH_TIS_Oscillation]]
- [[CONCEPT_ARCH_TIS_Tragedy_of_Commons]]
- [[CONCEPT_ARCH_TIS_Escalation]]
- [[CONCEPT_ARCH_TIS_Resilience]]
- [[CONCEPT_ARCH_TIS_Self_Organization]]
- [[CONCEPT_ARCH_TIS_Hierarchy]]

# Comparison Table

| Pair | Phân biệt nhanh | Câu hỏi kiểm tra |
|---|---|---|
| Event vs Behavior vs Structure | Event là điều vừa xảy ra; behavior là pattern qua thời gian; structure là nguyên nhân tạo pattern. | Bạn đang sửa triệu chứng hay sửa cấu trúc? |
| Stock vs Flow | Stock là lượng tích lũy; flow là tốc độ vào / ra làm stock đổi. | Bạn đang đo trạng thái hay đo dòng thay đổi? |
| Balancing vs Reinforcing Feedback | Balancing ổn định / kéo về mục tiêu; reinforcing khuếch đại. | Feedback đang làm hệ tự ổn định hay tự tăng tốc? |
| Delay vs No Delay | Delay làm tác động đến muộn, dễ gây phản ứng quá tay. | Có khoảng trễ nào làm bạn hiểu sai kết quả không? |
| Boundary vs Whole System | Boundary quyết định scope phân tích; đổi boundary có thể đổi kết luận. | Ai / cái gì đang bị loại khỏi bản đồ hệ thống? |
| Trap vs Bad Decision | Trap là lỗi do cấu trúc lặp lại; bad decision là lỗi cục bộ. | Nếu thay người mà lỗi vẫn lặp lại, trap là gì? |
| Parameter vs Leverage Point sâu | Parameter thường dễ chỉnh nhưng ít đổi hệ; goal/mindset/rule sâu hơn. | Bạn đang chỉnh số hay đổi logic vận hành? |

# Failure Modes

1. **Chỉ nhìn event**: thấy một lỗi đơn lẻ rồi sửa nhanh, nhưng bỏ qua pattern và cấu trúc.
2. **Nhầm stock với flow**: dùng dữ liệu tốc độ để kết luận về trạng thái tích lũy, hoặc ngược lại.
3. **Bỏ qua delay**: can thiệp quá sớm / quá mạnh vì chưa thấy kết quả đến.
4. **Tìm thủ phạm thay vì tìm cấu trúc**: quy lỗi cho cá nhân trong khi incentive, boundary, rule hoặc feedback mới là nguyên nhân.
5. **Can thiệp ở điểm đòn bẩy nông**: chỉnh tham số nhưng không chạm rule, goal, information flow, hoặc mindset.
6. **Vẽ boundary quá hẹp**: tối ưu một phần khiến toàn hệ xấu hơn.
7. **Coi Learning Pack là synthesis cuối**: pack này chỉ là learning artifact để học và thực hành, không phải kết luận đã duyệt.

# Practice Task

Chọn một hệ thống thật trong vault hoặc công việc hiện tại, ví dụ:

- pipeline ingest của `NoteBookLLM_Br`
- quy trình học một nguồn dài như `Thinking in Systems`
- workflow tạo atom -> review -> synthesis
- một lớp học / chương trình đào tạo đang thiết kế

Làm trong 25-35 phút:

1. Ghi mục đích của hệ thống trong 1 câu.
2. Liệt kê 2-3 stock chính.
3. Liệt kê flow làm mỗi stock tăng / giảm.
4. Vẽ ít nhất một balancing loop và một reinforcing loop.
5. Chỉ ra một delay quan trọng.
6. Ghi boundary đang dùng và một boundary thay thế.
7. Chọn một system trap có thể đang xảy ra.
8. Đề xuất một leverage point sâu hơn chỉnh tham số.

Output mong muốn:

```md
## System Chosen
## Purpose
## Stocks
## Flows
## Feedback Loops
## Delays
## Boundary Choice
## Likely Trap
## Leverage Point
## What I Would Test Next
```

# Review Questions

1. Nếu chỉ được nhớ một câu về system, bạn sẽ nói gì?
2. Vì sao structure quan trọng hơn event khi muốn sửa lỗi lặp lại?
3. Stock khác flow ở đâu? Cho một ví dụ trong vault.
4. Một reinforcing loop có thể tạo tăng trưởng tốt và suy giảm xấu như thế nào?
5. Balancing feedback có phải lúc nào cũng tốt không?
6. Delay gây oscillation bằng cách nào?
7. Khi đổi boundary, kết luận phân tích có thể đổi ra sao?
8. Dấu hiệu nào cho thấy vấn đề là system trap chứ không phải lỗi cá nhân?
9. Vì sao leverage point sâu thường khó dùng hơn leverage point nông?
10. Bạn sẽ áp dụng systems wisdom vào một quyết định tuần này như thế nào?

# Related Projects

- `ARCH_TIS`: học nhanh `Thinking in Systems` từ atom đã có.
- Wiki ingest lifecycle: dùng event / behavior / structure để phân biệt lỗi local với blocker toàn pipeline.
- Skill governance: dùng boundary để tách `wiki-learning-pack` khỏi `wiki-learning-audit`, `pedagogy`, ingest, và synthesis.
- Learning UX layer: dùng pack này làm bước trước `wiki-review-drill` và `wiki-learning-audit`.

# Source Trace

Pack này trace về các atom/source sau:

- `3-resources/wiki/sources/SOURCE_ARCH_TIS_Thinking_in_Systems.md`
- `3-resources/wiki/concepts/CONCEPT_ARCH_TIS_System.md`
- `3-resources/wiki/concepts/CONCEPT_ARCH_TIS_System_Structure.md`
- `3-resources/wiki/concepts/CONCEPT_ARCH_TIS_Event_Behavior_Structure.md`
- `3-resources/wiki/concepts/CONCEPT_ARCH_TIS_System_Boundaries.md`
- `3-resources/wiki/concepts/CONCEPT_ARCH_TIS_Stock.md`
- `3-resources/wiki/concepts/CONCEPT_ARCH_TIS_Flow.md`
- `3-resources/wiki/concepts/CONCEPT_ARCH_TIS_Feedback_Loop.md`
- `3-resources/wiki/concepts/CONCEPT_ARCH_TIS_Balancing_Feedback.md`
- `3-resources/wiki/concepts/CONCEPT_ARCH_TIS_Reinforcing_Feedback.md`
- `3-resources/wiki/concepts/CONCEPT_ARCH_TIS_Delay.md`
- `3-resources/wiki/concepts/CONCEPT_ARCH_TIS_Oscillation.md`
- `3-resources/wiki/concepts/CONCEPT_ARCH_TIS_System_Traps.md`
- `3-resources/wiki/concepts/CONCEPT_ARCH_TIS_Tragedy_of_Commons.md`
- `3-resources/wiki/concepts/CONCEPT_ARCH_TIS_Escalation.md`
- `3-resources/wiki/concepts/CONCEPT_ARCH_TIS_Leverage_Points.md`
- `3-resources/wiki/concepts/CONCEPT_ARCH_TIS_Resilience.md`
- `3-resources/wiki/concepts/CONCEPT_ARCH_TIS_Self_Organization.md`
- `3-resources/wiki/concepts/CONCEPT_ARCH_TIS_Hierarchy.md`
- `3-resources/wiki/concepts/CONCEPT_ARCH_TIS_Systems_Wisdom.md`

# Missing Context

- Các atom `ARCH_TIS` đọc được trong bước chat-only test đang là `DRAFT`, nên artifact này giữ `learning_pack_status: "EXPLORATORY"` và `status: "LEARNING_DRAFT"`.
- Source atom ghi “37 atoms”, nhưng filesystem query ở bước test thấy 33 file `ARCH_TIS`. Cần reconcile con số này trước khi coi pack là trạng thái ổn định dài hạn.
- Chưa chạy `wiki-breakdown`, nên chưa xác nhận khái niệm nào còn thiếu để học nhanh.
- Chưa chạy `wiki-learning-audit`, đúng boundary: pack này chỉ recommend audit, không tự chạy.

# Next Action

1. Dùng pack này để học `ARCH_TIS` trong một phiên 60-90 phút.
2. Sau khi học, tạo `wiki-review-drill` nếu cần câu hỏi recall / transfer chuyên biệt.
3. Nếu muốn kiểm tra atom nào “đã đọc nhưng chưa thực hành”, chạy GO riêng:

```text
AN GO - run wiki-learning-audit dry-run for ARCH_TIS
```

4. Nếu muốn biến pack thành giáo án, slide, activity sheet, hoặc rubric, handoff sang `@designer` / `pedagogy`.