# PLAN — MimiClaw Inbox Workflow

## 1. Objective
- Thiết lập workflow để MimiClaw ghi note vào `00_Inbox/` và Antigravity xử lý bằng lệnh `/ingest-inbox`.
- Nối rõ giai đoạn `Query + File-Back` để các kết quả phân tích tốt không dừng ở chat mà được nộp ngược thành Wiki page mới qua `/file-back`.
- Giữ nguyên triết lý flat structure, append-only log, raw immutable, và archive sau xử lý.
- Tránh xung đột với `task_plan.md` hiện tại đang ở trạng thái `Test Bank Only`.
- Implementation plan chi tiết cho nhánh `Telegram -> GitHub -> 00_Inbox` nằm tại `IMPLEMENTATION_P1_1_MimiClaw_GitHub_Capture.md`.

## 2. Current Constraints
- `task_plan.md` đang ghi rõ: không tạo thêm `wiki/` hoặc `distilled/` nếu chưa có yêu cầu mới.
- User hiện đã đưa ra yêu cầu mới cho `00_Inbox/` và `/ingest-inbox`, nên cần coi đây là một workflow mở rộng có chủ đích.
- `00_Inbox/` là root bucket hợp lệ theo Rule 7 và phù hợp cho intake kiểu MimiClaw.

## 3. Proposed Target Workflow
1. MimiClaw tạo file mới trong `00_Inbox/` theo frontmatter chuẩn:
   - `date`
   - `source`
   - `type`
   - `status: unprocessed`
2. Người vận hành chạy:
   - `git pull`
   - mở Antigravity
   - `/ingest-inbox`
3. `@librarian` đọc toàn bộ file `status: unprocessed` trong `00_Inbox/`.
4. Với mỗi file, agent thực hiện phân loại theo decision tree:
   - `wiki`: khi note là tri thức nguyên tử, có thể chuẩn hóa thành một concept page.
   - `project`: khi note gắn với đầu việc hoặc deliverable cụ thể trong `1-projects/`.
   - `area`: khi note là quy tắc vận hành, rubric, SOP hoặc tri thức duy trì dài hạn trong `2-areas/`.
   - `ignore`: khi note quá mơ hồ, trùng lặp, hoặc không đủ giá trị để nạp hệ thống.
5. Trước khi ghi bất kỳ wiki page nào:
   - bắt buộc đọc `3-resources/WIKI_AGENT_GUIDE.md`
   - cập nhật `3-resources/WIKI_INDEX.md`
   - append `3-resources/log.md`
6. Sau khi xử lý xong từng inbox note:
   - đổi trạng thái logic thành `processed`
   - di chuyển file gốc sang `4-archive/` với prefix ngày xử lý `YYYYMMDD_`
   - nếu file có wikilinks thì neutralize trước khi archive
7. Sau giai đoạn ingest, người vận hành có thể dùng tri thức đã vào Wiki để hỏi đáp, tổng hợp hoặc phân tích tiếp trong Antigravity.
8. Nếu câu trả lời tạo ra insight tốt, checklist rõ, synthesis có giá trị tái sử dụng hoặc mini knowledge page sạch:
   - chạy `/file-back`
   - `@librarian` hoặc agent phù hợp chuẩn hóa kết quả thành Wiki page mới
   - page mới phải tuân thủ `WIKI_AGENT_GUIDE.md`, có ít nhất 2 `[[Wikilinks]]`, được cập nhật vào `WIKI_INDEX.md` và append log
9. Kết thúc phiên:
   - `git push`

## 4. Command Spec for `/ingest-inbox`
- Primary agent: `@librarian`
- Purpose: đọc toàn bộ `00_Inbox/`, phân loại từng file, propose action trước khi execute
- Input contract:
  - chỉ đọc file markdown flat trong `00_Inbox/`
  - ưu tiên file có `status: unprocessed`
- Output contract:
  - danh sách file đã xử lý
  - action đã chọn cho từng file: `wiki | project | area | ignore`
  - file đích đã tạo nếu có
  - file archive tương ứng
  - log entry tương ứng

## 4A. Command Spec for `/file-back`
- Primary agent: `@librarian`
- Purpose: lấy kết quả phân tích tốt từ phiên query hiện tại và nộp ngược thành Wiki page mới
- Input contract:
  - đầu vào phải là kết quả đã được người vận hành đánh giá là có giá trị tái sử dụng
  - không dùng `/file-back` cho note thô, nhắc nhớ rời rạc hoặc câu trả lời quá ngắn
- Output contract:
  - 1 Wiki page mới hoặc 1 update có giá trị cho Wiki page hiện có
  - cập nhật `3-resources/WIKI_INDEX.md`
  - append `3-resources/log.md`
- Quality gate:
  - phải có tiêu đề rõ
  - phải có ít nhất 2 `[[Wikilinks]]`
  - phải là nội dung đã được làm sạch từ chat output, không dump nguyên transcript

## 5. Decision Rules
### 5.1 Route to `3-resources/wiki/`
- Áp dụng khi note diễn đạt một insight rõ, có thể tái sử dụng.
- File wiki mới phải có tối thiểu 2 `[[Wikilinks]]`.
- Nếu note chưa đủ ngữ cảnh để tạo wiki page tốt, không ép nạp vào wiki.

### 5.2 Route to `1-projects/`
- Áp dụng khi note là ý tưởng đang phục vụ một project cụ thể.
- Nên đặt vào project folder phù hợp dưới dạng note hoặc plan file.

### 5.3 Route to `2-areas/`
- Áp dụng khi note là policy, checklist, hướng dẫn vận hành, rubric, profile, assessment guideline.

### 5.4 Route to `ignore`
- Áp dụng khi note:
  - quá ngắn và thiếu ngữ cảnh
  - trùng hoàn toàn với tri thức đã có
  - không đáng để lưu vào hệ tri thức
- Vẫn archive file gốc để giữ trace.

## 6. Required Changes Before Implementation
1. Cập nhật `AGENTS.md`
   - thêm hoặc hoàn thiện mô tả `/ingest-inbox`
   - làm rõ agent owner là `@librarian`
   - thêm tiêu chí phân loại inbox
2. Cập nhật `task_plan.md`
   - ghi rõ đây là ngoại lệ có chủ đích so với pivot `Test Bank Only`
   - nêu rằng inbox workflow là intake channel, không mặc định khôi phục toàn bộ wiki pipeline cũ
3. Tạo script hỗ trợ
   - ví dụ: `scripts/pipelines/ingest_inbox.ps1` hoặc `scripts/pipelines/ingest_inbox.py`
   - nhiệm vụ: scan frontmatter, validate schema, move archive, append log
4. Tạo quy ước naming cho output
   - wiki file: theo Rule 7 prefix hai cấp nếu nội dung thuộc taxonomy đã biết
   - archive file: `YYYYMMDD_[original_name].md`
5. Bổ sung handoff giữa `/ingest-inbox` và `/file-back`
   - xác định khi nào một note sau ingest chỉ dừng ở archive
   - khi nào tri thức phát sinh từ query mới đủ chuẩn để file-back vào wiki

## 7. Risks and Mitigations
- Risk: workflow mới mâu thuẫn với pivot hiện tại.
  - Mitigation: cập nhật `task_plan.md` trước khi triển khai code.
- Risk: note quá ngắn làm wiki chất lượng thấp.
  - Mitigation: mặc định `ignore` hoặc route sang project scratchpad thay vì ép thành wiki.
- Risk: archive làm mất trace trạng thái xử lý.
  - Mitigation: log mỗi file và giữ nguyên frontmatter gốc trong bản archive.
- Risk: tạo quá nhiều wiki rác.
  - Mitigation: thêm bước `propose action` trước `execute`.
- Risk: `/file-back` bị dùng để nộp ngược cả câu trả lời chưa tinh lọc.
  - Mitigation: thêm quality gate bắt buộc trước khi file-back, chỉ nộp nội dung đã được synthesize.

## 8. Execution Plan
1. `@pm` cập nhật plan và thống nhất rule mới với user.
2. `@devops` tạo script ingest inbox.
3. `@librarian` kiểm thử bằng 2-3 file mẫu trong `00_Inbox/`.
4. `@pm` và `@librarian` kiểm thử tiếp vòng `Query + /file-back` với 1 case tốt sau ingest.
5. `@healer` xử lý edge cases về naming, encoding, archive, broken links.
6. `@pm` chốt SOP vận hành hằng ngày:
   - `git pull`
   - `/ingest-inbox`
   - query/review ngắn trên Wiki mới cập nhật
   - `/file-back` nếu có synthesis tốt
   - `git push`

## 9. Recommendation
- Nên triển khai workflow này như một intake lane nhỏ, không mở lại toàn bộ knowledge-compounding pipeline cũ.
- Nên coi `/file-back` là vòng nén tri thức sau query, không phải bước mặc định cho mọi inbox note.
- Với note kiểu Telegram ngắn, mặc định route ưu tiên nên là:
  - `wiki` nếu insight rõ và tái sử dụng được
  - `ignore` nếu chỉ là nhắc nhớ cá nhân quá ngắn
  - `project` nếu đang phục vụ một module đang chạy
- Với output sau query, chỉ dùng `/file-back` khi nội dung đã vượt mức “trả lời trong chat” và xứng đáng trở thành tri thức lâu dài trong Wiki.
