---
title: "Implementation P1.1 - MimiClaw GitHub Capture"
date: 2026-04-28
owner: "@pm"
status: draft
related_plan: "1-projects/2026_MimiClaw_Inbox/PLAN_Inbox_Workflow.md"
target_repo: "D:/01_Workspaces/mimiclaw"
target_output: "00_Inbox/"
---

# P1.1 - Báo cáo Khai thác sâu tri thức

### 📊 Thống kê hiệu suất Khai thác (Mining Stats)
| Chỉ số | Giá trị | Ghi chú |
| :--- | :--- | :--- |
| **Số tệp nguồn đã quét** | 5 tệp | `METAS_AGENTS.md`, `CLAUDE.md`, `task_plan.md`, `3-resources/PROCESS_TEMPLATE.md`, `1-projects/2026_MimiClaw_Inbox/PLAN_Inbox_Workflow.md` |
| **Tổng số câu hỏi** | 1 mục tiêu triển khai | P1.1 chỉ tập trung vào capture note từ Telegram sang GitHub Inbox |
| **Nguyên tử tri thức (Atoms)** | 0 | Đây là implementation plan, chưa thực hiện extraction tri thức |
| **Tỷ lệ tri thức/câu hỏi** | **1 : 1** | 1 bài toán triển khai -> 1 kế hoạch thực thi tối thiểu |

### Master Files sẽ được bồi đắp tri thức từ nguồn này
- Chưa có ở P1.1
- `3-resources/distilled/`: none

---

## 📂 Tóm tắt Điều hành
- Repo trung tâm: `NoteBookLLM_Br`
- Thiết bị capture: `MimiClaw` tại `D:\01_Workspaces\mimiclaw`
- Mục tiêu Definition of Done:
  - Gửi Telegram message bắt đầu bằng `note:`
  - ESP32 gọi GitHub API thành công
  - Tạo file markdown mới trong `00_Inbox/`
  - Bot phản hồi xác nhận ngắn trên Telegram
- P1.1 chỉ làm `Capture`, chưa làm `Query` và chưa đưa `/file-back` xuống device

## 📂 Scope In
- Thêm GitHub credentials vào cấu hình MimiClaw
- Viết GitHub gateway tối thiểu để tạo file trong repo
- Parse trigger `note:` từ Telegram
- Tạo file theo template cố định cho `00_Inbox/`
- Gửi xác nhận thành công/thất bại về Telegram

## 📂 Scope Out
- Chưa đọc Wiki từ GitHub
- Chưa sync `3-resources/wiki/`
- Chưa parse `HEARTBEAT.md`
- Chưa đưa `/file-back` vào ESP32
- Chưa xử lý nhiều loại message như ảnh, voice, document

## 📂 Quyết định Kiến trúc
- GitHub là `Source of Truth` cho tri thức dài hạn
- `00_Inbox/` là landing zone duy nhất của P1.1
- Capture path phải đi thẳng, không qua LLM
- Trigger `note:` được xử lý theo deterministic flow để giảm token, giảm sai số, tăng độ tin cậy

## 📂 Luồng Dữ liệu Mục tiêu
1. User gửi Telegram message:
   - `note: học sinh hay nhầm pull-up resistor với pull-down`
2. Telegram channel nhận text
3. Firmware phát hiện prefix `note:`
4. Bỏ qua agent loop/LLM cho nhánh này
5. Gọi GitHub API `PUT /repos/{owner}/{repo}/contents/00_Inbox/{filename}`
6. Ghi file markdown với frontmatter chuẩn
7. Nếu thành công:
   - trả Telegram: `Da luu note vao 00_Inbox`
8. Nếu thất bại:
   - trả Telegram: `Luu note that bai: <ly do ngan>`

## 📂 Contract file đầu ra
### Filename
- Mẫu: `YYYYMMDD_note_<slug>.md`
- Ví dụ: `20260428_note_pullup_vs_pulldown.md`

### Nội dung file
```md
---
date: 2026-04-28
source: telegram
type: note
status: unprocessed
---

hoc sinh hay nham pull-up resistor voi pull-down
```

### Quy ước slug
- Lowercase
- ASCII-safe
- Space -> `_`
- Cắt về độ dài vừa phải, ví dụ 40-60 ký tự
- Nếu không tạo được slug tốt thì fallback:
  - `YYYYMMDD_note_capture_<unix_ts>.md`

## 📂 Bản đồ thay đổi file ở repo MimiClaw
### A. Secrets & config
- `D:\01_Workspaces\mimiclaw\main\mimi_secrets.h.example`
  - thêm:
    - `MIMI_SECRET_GITHUB_TOKEN`
    - `MIMI_SECRET_GITHUB_REPO`
    - `MIMI_SECRET_GITHUB_BRANCH`
- `D:\01_Workspaces\mimiclaw\main\mimi_config.h`
  - thêm constants cho GitHub API host/path, buffer limits, timeout

### B. Gateway
- `D:\01_Workspaces\mimiclaw\main\gateway\github_api.h`
- `D:\01_Workspaces\mimiclaw\main\gateway\github_api.c`
- Chức năng tối thiểu:
  - `github_api_init()`
  - `github_create_inbox_note(date, body, out_path, out_err)`

### C. Telegram capture path
- `D:\01_Workspaces\mimiclaw\main\channels\telegram\telegram_bot.c`
- Hoặc tách tại layer trung gian phù hợp nếu repo đang route inbound qua message bus
- Bổ sung detect prefix:
  - `note:`
  - có thể mở rộng thêm `ghi chú:` sau này, nhưng không nằm trong P1.1

### D. Tool layer
- Chưa cần generic `tool_github.c` trong P1.1 nếu capture path đi thẳng
- Nếu team muốn giữ kiến trúc tool-first, chỉ tạo 1 tool hẹp:
  - `capture_note`

### E. Docs
- `D:\01_Workspaces\mimiclaw\README.md`
  - thêm hướng dẫn cấu hình GitHub token
- `D:\01_Workspaces\mimiclaw\docs\ERROR_DICTIONARY_K12.md`
  - thêm lỗi thường gặp sau khi test

## 📂 File flow đề xuất trong firmware
- Inbound:
  - `telegram_bot.c` lấy text
  - nếu không phải `note:` -> flow cũ
  - nếu là `note:` -> `capture_note_handler(...)`
- Capture handler:
  - sanitize body
  - generate filename
  - render markdown
  - gọi `github_create_inbox_note`
- Outbound:
  - queue response xác nhận về Telegram

## 📂 Acceptance Criteria
- AC1: Tin nhắn `note:` tạo được file mới trong `00_Inbox/`
- AC2: File đúng frontmatter và không thiếu body
- AC3: Tên file tuân theo `YYYYMMDD_note_<slug>.md`
- AC4: Bot phản hồi lại trên Telegram trong cùng phiên
- AC5: Khi GitHub API lỗi, bot trả lỗi ngắn gọn thay vì im lặng
- AC6: Không làm hỏng luồng chat bình thường không có prefix `note:`

## 📂 Test Plan
### Test 1 - Happy path
- Input:
  - `note: học sinh hay nhầm pull-up resistor với pull-down`
- Expected:
  - tạo đúng 1 file trong `00_Inbox/`
  - Telegram trả xác nhận thành công

### Test 2 - Empty note
- Input:
  - `note:`
- Expected:
  - không gọi GitHub API
  - trả lỗi: `Noi dung note rong`

### Test 3 - Unicode/Vietnamese
- Input:
  - `note: Đèn LED hay bị học sinh cắm ngược cực`
- Expected:
  - file body giữ được nội dung
  - filename vẫn an toàn nhờ slug/fallback

### Test 4 - Network fail
- Tắt WiFi hoặc dùng token sai
- Expected:
  - bot báo lỗi ngắn
  - không crash

### Test 5 - Non-note chat
- Input:
  - `Hôm nay học gì?`
- Expected:
  - flow Telegram/LLM cũ vẫn hoạt động

## 📂 Rủi ro kỹ thuật
- GitHub API cần base64 content và SHA logic nếu update file
  - P1.1 chỉ tạo file mới để tránh complexity update
- ESP32 giới hạn RAM cho JSON payload
  - giữ payload nhỏ, không upload note dài ở P1.1
- Unicode/slug tiếng Việt
  - body giữ nguyên, filename dùng slug ASCII hoặc fallback timestamp
- Token lộ trong source
  - ưu tiên cho phép set runtime sau này; trước mắt hỗ trợ build-time secret

## 📂 Rollback Plan
- Nếu GitHub capture gây lỗi cho luồng Telegram:
  - disable detect `note:` bằng compile flag hoặc guard config
  - giữ nguyên channel polling và outbound messaging
- Nếu GitHub API chưa ổn:
  - tạm fallback sang lưu local queue trên SPIFFS, nhưng fallback này không thuộc P1.1

## 📂 Handoff cho @engineer
- Triển khai theo thứ tự:
  1. secrets/config
  2. github gateway tối thiểu
  3. note-prefix capture path
  4. Telegram confirmation
  5. test happy path + failure path
- Không mở rộng sang query/file-back trong cùng nhánh đầu tiên

## 📂 Kết luận
- P1.1 thành công khi MimiClaw trở thành thiết bị capture đáng tin cậy cho `00_Inbox/`
- Đây là milestone mở khóa toàn bộ workflow:
  - `Telegram -> 00_Inbox -> /ingest-inbox -> Query -> /file-back`

---
*Báo cáo được khởi tạo theo chuẩn Swarm 4.0 Supreme. Mọi thay đổi phải cập nhật lại bảng thống kê.*
