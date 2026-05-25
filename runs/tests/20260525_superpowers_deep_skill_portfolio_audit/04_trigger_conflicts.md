# Trigger Conflicts: Phân Tích Xung Đột Điều Kiện Kích Hoạt

Báo cáo này xác định các mẫu prompt (prompt patterns) dễ gây xung đột hoặc nhầm lẫn giữa các kỹ năng của vault, đề xuất tuyến định hướng chính xác (correct route), phân tích rủi ro và đưa ra giải pháp khắc phục.

| Prompt Pattern (Mẫu Prompt) | Skills That May Trigger (Các skill dễ bị kích hoạt) | Correct Route (Tuyến định hướng chính xác) | Risk (Rủi ro khi kích hoạt sai) | Fix (Giải pháp khắc phục) |
| :--- | :--- | :--- | :--- | :--- |
| **"Tóm tắt PDF này để tôi học nhanh"** | `wiki-learning-pack`, `wiki-hd-convert`, `process-raw-resource`, `wiki-ingest` | `wiki-learning-pack` hoặc `process-raw-resource` (ở chế độ chat-only). Không được kích hoạt canonical ingest. | **High.** Agent có thể tự ý di chuyển PDF vào `raw_sources/` và tạo các Atom tri thức chính thức (canonical atom) làm bẩn vault của người dùng. | Cấu hình định tuyến cứng trong `workspace-routing.yaml` định hướng các câu hỏi tóm tắt/học nhanh đi thẳng vào workspace `learning` và workflow `learning-first`. |
| **"Sửa script convert PDF để chạy ổn định hơn"** | `writing-plans`, `executing-plans`, `cm-planning`, `cm-tdd`, `verification-before-completion` | `cm-planning` (Phase 0) trước để làm rõ lỗi, sau đó chuyển giao sang `writing-plans`. | **Medium.** Agent bắt tay vào sửa code ngay bằng `executing-plans` mà không lập plan, dẫn đến sửa lỗi mò mẫm, dễ phá vỡ cấu trúc code hiện có. | Áp dụng rule an toàn bắt buộc: Mọi prompt chứa từ khóa *"sửa script"*, *"sửa code"*, *"fix bug"* đều phải kích hoạt `cm-planning` trước để làm rõ RCA và tạo spec nháp. |
| **"Tôi muốn đưa tài liệu này vào vault chính"** | `wiki-ingest`, `process-raw-resource`, `wiki-md-auditor`, `wiki-absorb` | `wiki-ingest` và kích hoạt workflow `ingest-lifecycle` qua gate chuẩn bị. | **High.** Agent bỏ qua các chốt chặn chuẩn hóa Markdown (`wiki-md-auditor`) hay khóa nguồn (`lock-ingest-input`), ghi trực tiếp dữ liệu thô vào `3-resources/`. | Bypass hoàn toàn preview lane. Kích hoạt trực tiếp Ingest Lifecycle workflow và yêu cầu người dùng xác nhận phê duyệt (AN GO) trước khi ghi. |
| **"Tìm định nghĩa của thuật ngữ X"** | `wiki-query`, `wiki-semantic-search`, `wiki-breakdown` | `wiki-query` chạy trước ( keyword / graph traversal). | **Medium.** Agent kích hoạt đồng thời cả hai skill tìm kiếm, nạp một lượng lớn Atom có ngữ nghĩa gần giống vào context, gây lãng phí token. | Phân luồng ưu tiên rõ ràng trong rule tìm kiếm: `wiki-query` luôn được chạy trước; nếu kết quả rỗng mới được gọi `wiki-semantic-search`. |
| **"Tạo sơ đồ giáo án hoặc slide cho bài học X"** | `pedagogy`, `wiki-to-deliverable`, `wiki-learning-pack` | `pedagogy` (chuyên trách sư phạm). | **Medium.** Agent sinh ra một bài báo cáo deliverable phẳng thông thường thay vì một slide hoặc giáo án có cấu trúc phân rã sư phạm (lesson plan, slide,spaced repetition). | Định nghĩa rõ boundary trong prompt-master: prompt chứa *"giáo án"*, *"slide"*, *"spaced repetition"* chỉ kích hoạt `pedagogy` với Trainer Profile được load. |

---

## Phân tích Chi tiết Xung đột & Giải pháp Khắc phục

### 1. Xung đột giữa Học nhanh (Learning Mode) và Nạp tri thức chính thức (Canonical Ingest)
- **Hành vi nhầm lẫn:** Khi người dùng nói *"Tóm tắt để học nhanh"*, Agent dễ bị nhầm lẫn giữa việc chỉ tạo bản tóm tắt tạm thời để đọc (Preview) với việc nạp tài liệu đó vào hệ thống tri thức (Ingest). Việc này xảy ra do trigger của các skill `process-raw-resource` và `wiki-ingest` có từ khóa trùng lặp như *"PDF"*, *"tài liệu"*, *"tóm tắt"*.
- **Rủi ro vận hành:** Tạo ra hàng loạt Atom nháp không mong muốn hoặc tự tiện ghi dữ liệu vào `3-resources/wiki/`, vi phạm ranh giới đóng băng đường dẫn cốt lõi.
- **Giải pháp:** Cập nhật file rules của `workspace-routing.yaml` để xác định rõ: Bất kỳ yêu cầu học nhanh nào bắt buộc phải chạy ở chế độ `learning-first` với ranh giới `no-write` đối với vùng canonical.

### 2. Xung đột giữa Lập kế hoạch Phase 0 (`cm-planning`) và Viết Kế hoạch Phase 1 (`writing-plans`)
- **Hành vi nhầm lẫn:** Agent dễ bỏ qua Phase 0 (làm rõ ý định, đánh giá rủi ro, RCA lỗi) mà nhảy thẳng vào Phase 1 (`writing-plans`) để viết file `implementation_plan.md` khi người dùng cung cấp một yêu cầu code có vẻ rõ ràng nhưng thực chất còn nhiều rủi ro.
- **Rủi ro vận hành:** Bản kế hoạch triển khai bị over-engineered, thiếu các phương án rollback, hoặc bỏ sót các trường hợp biên quan trọng.
- **Giải pháp:** Tích hợp logic chốt chặn (gate-check) trong bootstrap: Không cho phép Agent sử dụng `writing-plans` hay `executing-plans` nếu chưa chứng minh được đã hoàn tất bước phân tích rủi ro và RCA lỗi của `cm-planning`.
