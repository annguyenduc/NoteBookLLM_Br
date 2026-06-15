# CONTINUITY.md

current_state: "Hoàn thành nâng cấp Câu 25 (lỗi nhấp nháy sticker tai mèo), sửa và đồng bộ Câu 26 (đa luồng bám đuổi cầu mũi và phát âm thanh nhắm mắt), Câu 27 (phân loại khẩu trang trên Teachable Machine), bỏ viền đỏ Câu 28, crop sát ảnh Câu 17 (nose bridge), phục hồi Câu 22 (lý do dùng forever bám đuổi sống mũi) và đồng bộ Câu 23, 24. Biên dịch thành công HTML và validator báo PASS 100%."
next_step_for_AN: "Kiểm tra hiển thị của đề thi v2 định dạng HTML tại workspaces/source-lab/converted/test-lms/INT_HCM_AI_Trung_hoc/GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2.html trong worktree D:\\_agent_worktrees\\20260615_exam_workflow_spec\\."
blockers: []
verification:
  - "node render_cau_17_crop.js: OK"
  - "node render_cau_25.js: OK"
  - "python update_sb3_q25.py: OK"
  - "node render_cau_26.js: OK"
  - "python update_sb3_q26.py: OK"
  - "node render_cau_28_clean.js: OK"
  - "python scripts/maintenance/generate_exam_html.py: OK"
  - "python scripts/maintenance/exam_workflow_validator.py: PASS (100% code files valid)"

