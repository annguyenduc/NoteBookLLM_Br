# CONTINUITY.md

current_state: "Đã hoàn thành dọn dẹp toàn bộ file rác/tạm thời từ root sang workspaces/dev-lab/sandbox/ và workspaces/dev-lab/tests/. Đồng thời khắc phục triệt để sự cố nạp khối lệnh Scratch bị rỗng (Blocks count = 0) cho BT2 bằng cách tăng thời gian chờ đồng bộ trong generate_bt2.js (chờ 3.5s sau setEditingTarget và 3s sau domToWorkspace). Số lượng blocks của Rabbit đạt 66 blocks. Ghi hình lại video demo bt2_demo.webm chạy thực tế Stage Full Screen dài 48s hoàn tất. Copy đầy đủ 20 file code đáp án và 1 video demo sang converted/."
next_step_for_AN: "Kiểm tra video demo 'bt2_demo.webm' trong thư mục converted/ và đề thi HTML 'Bai_kiem_tra_thuc_hanh_AI_THCS.html' đã được cập nhật."
blockers: []
verification:
  - "Test import shim libs: SUCCESS (.venv/Scripts/python -c 'from libs.core.logger import get_logger' thành công)"
  - "Dọn dẹp root: SUCCESS"
  - "node generate_bt2.js: SUCCESS (Rabbit target blocks: 66)"
  - "node record_bt2_video.js: SUCCESS (bt2_demo.webm generated and saved to converted/)"
  - "python scripts/maintenance/exam_workflow_validator.py: PASS (10 exercises, 20 code files, 1 video)"
  - "python scripts/maintenance/generate_exam_html.py: HTML compiled successfully"
