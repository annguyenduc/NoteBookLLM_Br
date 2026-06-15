# CONTINUITY.md

current_state: "Đã khắc phục lỗi lộ đáp án Câu 14 (xóa bỏ text tiếng Việt chứa đáp án trong hình ảnh), sửa lỗi logic bám sống mũi/đầu mũi ở Câu 17 (đổi các tùy chọn đáp án sang hình ảnh khối lệnh Scratch trực quan), và thêm hình ảnh thiết lập camera cho Câu 19. Đồng thời viết thêm công cụ generate_exam_html.py để kết xuất tự động sang HTML và cập nhật cả tệp .md và .html của bộ đề thi v2."
next_step_for_AN: "Kiểm tra và đọc hiển thị của đề thi v2 định dạng HTML tại workspaces/source-lab/converted/test-lms/INT_HCM_AI_Trung_hoc/GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2.html."
blockers: []
verification:
  - "python scripts/maintenance/test_exam_workflow_validator.py: OK"
  - "python scripts/maintenance/exam_workflow_validator.py: PASS"
  - "GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2.html successfully generated and synced"
