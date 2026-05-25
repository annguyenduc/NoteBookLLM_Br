# Agent Runtime Tests

Thư mục này chứa test cho skill routing, workflow routing, và safety boundary của `NoteBookLLM_Br`.

Superpowers trong `workspaces/refs/superpowers` được dùng làm direct grader trong audit session. Test thật của vault nằm ở đây.

## Nhóm test

- `skill-triggering/`: kiểm tra agent có chọn đúng skill không.
- `workflow-routing/`: kiểm tra agent có chọn đúng workflow không.
- `expected/`: ma trận kỳ vọng, hành động cấm, vùng ghi cho phép.

## Nguyên tắc

Mỗi test phải nêu rõ:

- prompt đầu vào;
- skill mong đợi;
- workflow mong đợi nếu có;
- mode mong đợi;
- hành động cấm;
- vùng được ghi;
- điều kiện pass/fail.
