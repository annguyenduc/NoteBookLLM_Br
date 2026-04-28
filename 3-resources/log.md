# PROJECT LOG

## [2026-04-22 09:15] <migration> | @pm | Hoàn tất Module mBot và AI Arduino
- Lý do: Di trú tri thức từ Docx sang Markdown Atomic.

## [2026-04-22 10:10] <migration> | @pm | Hoàn tất Module Robotics Rover (13 nodes)
- File tạo: brain/wiki/QUESTION_IOT_Rover_*
- Lý do: Di trú tri thức từ 5 bộ đề Rover. (Đang thực hiện sửa lỗi hiển thị).

## [2026-04-22 10:30] <heal> | @pm | Tổng kiểm tra và sửa lỗi Unicode toàn hệ thống
- File tạo/sửa: brain/WIKI_INDEX.md, CONTINUITY.md, brain/log.md
- Lý do: Phát hiện lỗi Mojibake (corrupted characters) do xung đột encoding. Đang thực hiện quy trình Re-Ingest.

## [2026-04-22 10:46] <incident> | @pm | VI PHẠM RULE 12 - RAW IS IMMUTABLE
- Chi tiết: Agent tự ý đổi tên file trong thư mục raw/ bằng GUID.
- Khắc phục: Triệu hồi @healer thực hiện phục hồi tên file theo chuẩn Snake_Case dựa trên nội dung title.
- Bài học: Tuyệt đối không dùng lệnh sửa đổi (Rename/Write) trong thư mục raw.

## [2026-04-22 13:00] Update | @pm | Hoàn thành Module KHMT
- File tạo/sửa: d:\NoteBookLLM_Br\brain\raw\KHMT_*, d:\NoteBookLLM_Br\brain\atoms\QUESTION_KHMT_*
- Lý do: Chuyển đổi thành công 11 bộ KHMT sang chuẩn Wiki 2.0 phẳng, cập nhật và hình ảnh trong lựa chọn.

## [2026-04-22 13:30] Update | @pm | Hoàn thành Module Robot
- File tạo/sửa: d:\NoteBookLLM_Br\brain\raw\Robot_*, d:\NoteBookLLM_Br\brain\atoms\QUESTION_Robot_*
- Lý do: Chuyển đổi thành công 24 bộ Robotics sang chuẩn Wiki 2.0 phẳng.

## [2026-04-22 13:50] Update | @pm | Hoàn thành Module IOT
- File tạo/sửa: d:\NoteBookLLM_Br\brain\raw\IOT_*, d:\NoteBookLLM_Br\brain\atoms\QUESTION_IOT_*
- Lý do: Chuyển đổi thành công 22 bộ IOT sang chuẩn Wiki 2.0 phẳng.

## [2026-04-22 13:55] Update | @pm | Hoàn thành toàn bộ 4 Module (KHMT, Robot, IOT, DESIGN)
- File tạo/sửa: brain/raw/*, brain/wiki/QUESTION_*
- Lý do: Chuyển đổi thành công 85 bộ LMS sang chuẩn Wiki 2.0 phẳng. Tổng cộng 3932 Atoms.

## [2026-04-23 05:56] ACCESS | @pm | Truy xuất thông tin NotebookLM: Xây dựng Wiki Cá nhân bằng LLM
- File sửa: [brain/log.md]
- Lý do: Người dùng yêu cầu lấy thông tin notebook phục vụ lập kế hoạch Wiki.

## [2026-04-23 06:01] CREATE | @pm | Tạo brain/index.md và brain/wip.md (Gap fix từ NotebookLM)
- File tạo: brain/index.md
- File tạo: brain/wip.md
- Lý do: Gap Analysis với notebook 'Xây dựng Wiki Cá nhân bằng LLM' - 2 file này là bắt buộc theo mô hình Karpathy LLM Wiki.

## [2026-04-23 06:10] VERIFY | @librarian | Audit và verify ATOMS_* files
- File sửa: brain/wiki/ATOMS_Arduino_Power.md -> status: verified
- File sửa: brain/wiki/ATOMS_Breadboard.md -> status: verified
- File sửa: brain/wiki/ATOMS_Servo_Motor.md -> status: verified
- File sửa: brain/wiki/ATOMS_Prompt_Engineering_Hoc_Tap.md -> status: verified
- File sửa: brain/wiki/ATOMS_Prompt_Engineering_K10_Anh/Toan/Van.md -> status: verified
- File tạo: brain/distilled/KB_IOT_Hardware_Arduino_Concepts.md
- File tạo: brain/distilled/KB_AI_Prompt_Engineering_K10.md
- Lý do: Gap fix + populate distilled/ theo mô hình Karpathy LLM Wiki.

## [2026-04-23 06:12] AUDIT | @auditor | Fix nguồn deprecated LMS_KB_IOT_NORMALIZED.md
- File sửa: ATOMS_Arduino_Power.md, ATOMS_Breadboard.md, ATOMS_Servo_Motor.md, ATOMS_Buzzer.md, ATOMS_Teachable_Machine.md
- Lý do: LMS_KB_IOT_NORMALIZED.md không còn tồn tại trong brain/raw/. Truy vết lại về file raw gốc xác thực.

## [2026-04-23 06:47] CLEAN-UP | @pm | Tái cấu trúc thư mục và Cập nhật Hiến pháp
- File tạo/sửa: AGENTS.md, CLAUDE.md, dọn dẹp root/brain
- Lý do: Loại bỏ rác, tuân thủ Rule 7 Absolute Flatness. Bỏ các file HTML và lessons theo yêu cầu User. Pending Giai đoạn 2 (Merge).
- Lưu ý: Đã áp dụng quy tắc ép chuẩn UTF-8 cho toàn bộ hệ thống ghi log.

## [2026-04-23 07:00] CLEAN-UP | @pm | Tổng vệ sinh và cấu trúc lại thư mục scripts/
- File tạo/sửa: d:\NoteBookLLM_Br\scripts/ (archive, maintenance, pipelines, setup, tests)
- Lý do: Giảm tải số lượng file tại root scripts (từ 58 xuống còn ~10 file cốt lõi). Phân loại rõ ràng Verbs/Pipelines/Tests.

## [2026-04-23 11:15] maintenance | @pm | Dọn dẹp distilled và tạo Wiki KHMT K10/Scratch Jr
- File tạo/sửa: brain/distilled/ (xóa), brain/wiki/WIKI_Python_K10_System.md, brain/wiki/WIKI_Scratch_Jr_System.md
- Lý do: Loại bỏ rác Yolo:Bit và xây dựng hệ thống Wiki KHMT theo chuẩn v4.0.

## [2026-04-23 14:18] INGEST | @pm | Chưng cất tri thức Arduino Fundamentals chuẩn Karpathy
- File tạo/sửa: d:\NoteBookLLM_Br\brain\wiki\WIKI_IOT_Arduino_Fundamentals.md
- Lý do: Gom 10+ câu hỏi trắc nghiệm IOT De 1 thành 1 file Wiki lý thuyết sạch sẽ để nạp NotebookLM.

## [2026-04-23 15:32] INGEST | @pm | Chưng cất tri thức Arduino Advanced chuẩn Karpathy
- File tạo/sửa: d:\NoteBookLLM_Br\brain\wiki\WIKI_IOT_Arduino_Advanced.md
- Lý do: Gom trắc nghiệm về LCD, DHT11, Siêu âm thành file Wiki lý thuyết chuyên sâu.

## [2026-04-23 16:15] DISTILL | @pm | Đóng gói Module IOT Arduino Master
- File tạo: d:\NoteBookLLM_Br\brain\distilled\KB_IOT_Arduino_Master.md
- Lý do: Hoàn tất quy trình Ingest -> Query -> Distill cho mảng Arduino.

## [2026-04-24 09:12] COMPLETED | @pm | Tổng kết Session Chuẩn hóa Logic IOT Arduino
- File tạo/sửa: [d:\NoteBookLLM_Br\brain\wiki\WIKI_IOT_Arduino_Logic.md], [d:\NoteBookLLM_Br\brain\wiki\WIKI_IOT_Arduino_Hardware.md]
- Lý do: Hoàn tất refactor tri thức Arduino từ 120 câu hỏi LMS và bổ sung logic đa nhiệm nâng cao cho mBlock 5.

## [2026-04-25 09:45] REPORT | @pm | Báo cáo tình trạng session hiện tại cho người dùng
- File tạo/sửa: brain/log.md
- Lý do: Cung cấp cái nhìn tổng quan về tiến độ dự án và các bước tiếp theo.

## [2026-04-25 09:55] COMPLETED | @pm | Mở rộng tri thức Arduino Advanced v2.0
- File tạo/sửa: brain/wiki/WIKI_IOT_Arduino_Advanced.md, brain/WIKI_INDEX.md
- Lý do: Tổng hợp chi tiết kỹ thuật từ 120 câu hỏi LMS (LCD, Joystick, L298, DHT11) và cập nhật mục lục toàn hệ thống.

## [2026-04-25 10:45] COMPLETED | @pm | Dứt điểm Module Arduino & Tinh gọn Robotics
- File tạo/sửa: brain/distilled/KB_IOT_Arduino_Master.md, AGENTS.md, task_plan.md
- File dọn dẹp: brain/wiki/ (Gộp linh kiện lẻ vào Hardware.md), archive/GBot/ (Di chuyển toàn bộ file GBot)
- Lý do: Hoàn tất 100% module Arduino và loại bỏ GBot theo yêu cầu của User. Pivot sang xBot/Rover.

## [2026-04-25 11:00] VERIFIED | @auditor | Audit toàn diện IOT (Arduino) và Robotics (xBot/Rover)
- File tạo/sửa: brain/log.md
- Lý do: Thực hiện Reverse Knowledge Tracing theo yêu cầu của user. Xác nhận 100% Source Integrity cho cả hai module.

## [2026-04-25 11:02] COMPLETED | @librarian | Chưng cất tri thức Robotics
- File tạo/sửa: brain/distilled/KB_ROBOT_Master.md
- Lý do: Bổ sung tệp Distilled cuối cùng cho module Robotics theo phát hiện của user. Khóa sổ quy trình học thuật.

## [2026-04-25 11:15] COMPLETED | @devops & @librarian | Merge Workspace: Gemini_Study_Hub
- File tạo/sửa: 13 files raw đã copy và chuẩn hóa tên; 4 files Wiki (Toán, Văn, Anh, AI Evaluation) đã tạo; update WIKI_INDEX.md
- Lý do: Hoàn thành Giai đoạn 3 (Merge Workspace) để hợp nhất tri thức Prompt Engineering K10 vào hệ thống chính.

## [2026-04-25 13:32] COMPLETED | @pm | Cập nhật CLAUDE.md - Architectural Foundation
- File tạo/sửa: CLAUDE.md
- Lý do: Thêm nền tảng kiến trúc Karpathy (3 tầng + 3 phép vận hành) và đăng ký lệnh /file-back, /lint vào Toolkit.

## [2026-04-25 13:35] COMPLETED | @pm | Tạo workflow /file-back (Karpathy Query Compounding)
- File tạo/sửa: .agent/workflows/file-back.md (tạo mới), AGENTS.md (thêm 1 dòng đăng ký lệnh)
- Lý do: Implement Gap 1 - File-Back để kết quả phân tích không biến mất vào chat history.

## [2026-04-25 14:06] COMPLETED | @pm | Tạo workflow /ingest và /lint (Gap 3 + Gap 4)
- File tạo/sửa: .agent/workflows/ingest.md (tạo mới), .agent/workflows/lint.md (tạo mới)
- Lý do: Chuẩn hóa quy trình Ingest và Lint theo Karpathy LLM Wiki pattern.

## [2026-04-25 14:31] distill | @engineer | KB_IOT_Arduino_Master.md
- File tạo/sửa: brain/distilled/KB_IOT_Arduino_Master.md (update source_pages + distilled_by)
- Lý do: Chạy /distill workflow v4.3 trên domain IOT Arduino. Nội dung đã tốt, chỉ cập nhật metadata.

## [2026-04-25 14:35] COMPLETED | @pm | Lưu trữ (Archive) các workflow lỗi thời
- File di chuyển: .agent/workflows/consolidate.md -> archive/, .agent/workflows/pilot_wiki_lms_kb_iot.md -> archive/
- Lý do: Các workflow này đã bị thay thế bởi hệ thống /ingest và /distill chuẩn Karpathy, hoặc gọi các script không còn tồn tại.

## [2026-04-26 12:53] CREATE | @engineer | WIKI_ROBOT_Hardware_Master.md
- File tạo: brain/wiki/WIKI_ROBOT_Hardware_Master.md
- Lý do: Giải quyết Concept Gap quan trọng nhất cho mảng Robotics. Tổng hợp tri thức phần cứng xBot và Rover từ 5+ bộ đề raw.

## [2026-04-26 13:03] CREATE | @engineer | WIKI_ROBOT_Logic_Master.md
- File tạo: brain/wiki/WIKI_ROBOT_Logic_Master.md
- Lý do: Hoàn thiện Trụ cột Tư duy Lập trình cho mảng Robotics. Hệ thống hóa thuật toán dò line, né vật cản và cấu trúc đa nhiệm giả lập.

## [2026-04-26 13:35] COMPLETED | @pm | Dứt điểm Module Robotics (Expansion)
- File tạo: brain/wiki/WIKI_ROBOT_Rover_Expansion.md
- Lý do: Hoàn tất Giai đoạn 2 của Lộ trình v4.2. Hệ thống hóa tri thức về Servo, Tay gắp, AI và IOT Dashboard cho Robot OhStem.

## [2026-04-27 14:32] FINISH | @pm | Kết thúc dự án LMS & Chuẩn bị PARA
- File tạo/sửa: [walkthrough.md, CONTINUITY.md, implementation_plan.md]
- Lý do: Hoàn tất giai đoạn Mining LMS và ổn định đồ thị tri thức. Chốt kế hoạch PARA.

## [2026-04-27 15:38] SCOUT | @scout | Hoàn thành nghiên cứu G2 Robotics
- File tạo/sửa: 1-projects/2026_Robotics/EXAM_Context_Robotics_G2.md
- Lý do: Trích xuất terminology và phạm vi kiến thức cho Rover và xBot.

## [2026-04-27 15:39] ENGINEER | @engineer | Hoàn thành 3 Wiki Atoms cho G2 Robotics
- File tạo/sửa: 3-resources/wiki/ROBOT_Rover_Basic.md, 3-resources/wiki/ROBOT_xBot_Basic.md, 3-resources/wiki/AI_IOT_Rover_Control.md
- Lý do: Xây dựng kho tri thức chuẩn cho Rover và xBot dựa trên EXAM_Context.

## [2026-04-27 16:25] STANDARDIZE | @engineer | Chuẩn hóa prefix 1619 file test-bank
- File tạo/sửa: 3-resources/test-bank/*, WIKI_INDEX.md
- Lý do: Đồng bộ hệ thống theo Rule 7 (Absolute Flatness), gộp các prefix cũ về chuẩn LEVEL1_LEVEL2_TYPE.

## [2026-04-27 16:35] RECOVERY | @engineer | Hoàn tất Hyper-Standardization cho Test-Bank và Assets
- File tạo/sửa: 635 files trong 3-resources/test-bank/, 9000+ assets
- Lý do: Sửa lỗi encoding tên file ảnh, chuẩn hóa taxonomy Rule 7 và hàn gắn 388 links gãy.

## [2026-04-27 22:30] PIVOT | @pm | Chuyển hướng dự án sang Test Bank Only
- File tạo/sửa: 1-projects/ (archived), 3-resources/wiki/ (archived), 3-resources/distilled/ (archived), task_plan.md, WIKI_INDEX.md
- Lý do: Theo yêu cầu User, xóa bỏ các dự án và kiến thức Atom, tập trung 100% vào trích xuất test-bank.

## [2026-04-27 22:55] FINISHED | @pm | Hoàn tất dự án trích xuất LMS Test Bank
- File tạo/sửa: 1,538 Atoms trong 3-resources/test-bank/
- Lý do: Hoàn thành 100% trích xuất từ 84 đề Docx và tối ưu hóa 13,000+ ảnh trùng lặp. Hệ thống đã sẵn sàng đóng session.

## [2026-04-27 23:20] PLAN | @pm | Lập kế hoạch workflow ingest inbox cho MimiClaw
- File tạo/sửa: 1-projects/2026_MimiClaw_Inbox/PLAN_Inbox_Workflow.md, 3-resources/log.md
- Lý do: Chuẩn hóa luồng nhận note từ 00_Inbox sang wiki/project/area/archive theo yêu cầu mới của user.

## [2026-04-27 23:22] CORRECTION | @pm | Khôi phục phần log gần nhất sau lỗi ghi đè ngoài ý muốn
- File tạo/sửa: 3-resources/log.md
- Lý do: Phục hồi các entry cuối cùng đã được đọc trong phiên làm việc để đưa log trở lại trạng thái append-oriented.
## [2026-04-27 23:35] PLAN | @pm | Bổ sung Query + File-Back vào kế hoạch MimiClaw Inbox
- File tạo/sửa: 1-projects/2026_MimiClaw_Inbox/PLAN_Inbox_Workflow.md
- Lý do: Hoàn thiện workflow sau ingest để kết quả query tốt có thể được nộp ngược thành Wiki page qua /file-back.
## [2026-04-28 00:10] PLAN | @pm | Tạo implementation plan P1.1 cho MimiClaw GitHub Capture
- File tạo/sửa: 1-projects/2026_MimiClaw_Inbox/IMPLEMENTATION_P1_1_MimiClaw_GitHub_Capture.md, 1-projects/2026_MimiClaw_Inbox/PLAN_Inbox_Workflow.md
- Lý do: Chốt scope triển khai tối thiểu cho nhánh Telegram -> GitHub -> 00_Inbox trước khi giao cho @engineer.

## [2026-04-28 15:10] ingest | @pm | coursera-AI-essential-Bias, drift, and knowledge cutoff.md
- Atomic Files: ACAD_AI_Data_Bias.md, ACAD_AI_Knowledge_Cutoff.md, ACAD_AI_Model_Drift.md, ACAD_AI_Human_In_The_Loop.md
- Master Compounded: ACAD_AI_Responsible_AI.md
- Số concept: 4

## [2026-04-28 15:42] ingest | @pm | coursera-AI-essential-Stay up to date with AI.md
- Atomic Files: ACAD_AI_Information_Toolkit.md, ACAD_AI_Learning_Habits.md
- Master Compounded: ACAD_AI_Responsible_AI.md
- Số concept: 2

## [2026-04-28 15:49] file-back | @pm | ACAD_AI_Cutoff_vs_Drift.md
