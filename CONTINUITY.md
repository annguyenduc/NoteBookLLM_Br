# CONTINUITY.md

current_state: "Hoàn thành tối ưu token cho skill prompt-master (Hướng A). Tách 298 dòng tool-specific routing ra file references/tool-routing.md riêng. SKILL.md giảm từ 31KB (~7,800 tokens) xuống còn 10.8KB (~2,773 tokens), tiết kiệm ~65% khi nạp startup. Ba file references/ (tool-routing, templates, patterns) đều chỉ nạp JIT theo nhu cầu. Cấu trúc 3-tier JIT hoàn chỉnh."
next_step_for_AN: "Nếu muốn tiếp tục tối ưu hóa, có thể áp dụng cùng pattern Hướng A cho các skill khác còn nặng (cm-dockit, wiki-ingest). Hoặc đóng phiên — hệ thống đã ổn định."
blockers: []
verification:
  - "SKILL.md hiện 207 dòng, 10.8 KB — đã kiểm tra bằng PowerShell"
  - "references/tool-routing.md tồn tại, 19.9 KB, 25+ tool sections"
  - "Cấu trúc 8 sections trong SKILL.md: Intent Extraction → Tool Routing (pointer) → Credential Safety → Input Sanitization → Diagnostic Checklist → Memory Block → Safe Techniques → Agentic Output Warning"

learnings:
  - scope: "prompt-master"
    lesson: "SKILL.md nặng do nhúng trực tiếp routing hướng dẫn cho 25+ tool vào body. Pattern đúng: giữ pointer ngắn trong SKILL.md, tách nội dung tool-specific ra references/ để nạp JIT."
    technique: "PowerShell array slicing ($lines[0..72] + $lines[366..end]) để xóa chính xác khoảng dòng khi replace_file_content không thể match uniquely."



