# 📕 Operational Memory (LOM) — CLAUDE.md

> **Status**: ACTIVE | **Session ID**: 99db579e | **Focus**: IOT Arduino Deep Distillation

## 📏 Wiki Content Standards (Bắt buộc)
Mọi file Wiki liên quan đến phần cứng (Hardware) **BẮT BUỘC** phải có cấu trúc:
1.  **Quy tắc vật lý:** Cách nhận dạng, cực tính (+/-), số chân.
2.  **Quy tắc đấu nối:** Ánh xạ chân cắm cụ thể (Ví dụ: GND ➔ GND, Signal ➔ D2).
3.  **Lưu ý an toàn:** Điện áp, điện trở bảo vệ, chia sẻ GND chung.
*Tuyệt đối không chấp nhận các file Wiki chỉ có mô tả chung chung.*

## 🗓️ Session Context (2026-04-24)
- **Task Hiện tại**: Chuẩn hóa Wiki IOT Arduino (Pure IOT).
- **Tiến độ**: 
    - [x] Tách bạch Hardware vs Logic.
    - [x] Bổ sung 100% linh kiện từ 120 câu hỏi.
    - [x] Thiết lập tiêu chuẩn "Quy tắc vật lý & Đấu nối".
- **Hành động tiếp theo**: Đồng bộ hóa Logic Lập trình.

## 🧭 Wiki Taxonomy (Trạng thái)
- [[WIKI_IOT_Arduino_Hardware]] — **[ĐÃ HOÀN TẤT]** (100% linh kiện).
- [[WIKI_IOT_Arduino_Logic]] — **[ĐANG XỬ LÝ]** (Cần nâng cấp theo chuẩn mới).
- [[WIKI_Arduino_System]] — **[ĐÃ HOÀN TẤT]**.

## 🛠️ Supreme Toolkit (Lệnh nhanh)
- `/distill` — Chưng cất tri thức từ MCQ sang Wiki.
- `/consolidate` — Tổng hợp các Wiki nhỏ thành Master KB.
- `/maintenance-gateway` — Bảo trì SmartProxyHub (Port 4000).
- `/file-back` — Lưu kết quả phân tích có giá trị thành Wiki page mới (Auto File-Back).
- `/lint` — Kiểm tra sức khỏe Wiki: trang mồ côi, liên kết gãy, mâu thuẫn.

---

## 🏛️ Nền tảng Kiến trúc (Architectural Foundation)

> **Đọc bắt buộc**: `llm-wiki.md` tại Root là tài liệu gốc định hình toàn bộ triết lý của hệ thống này.
> Mọi Agent PHẢI hiểu và tuân thủ 3 tầng và 3 phép vận hành được mô tả trong đó.

### Ba tầng (Three Layers)
| Tầng | Thư mục | Quy tắc cốt lõi |
| :--- | :--- | :--- |
| **Raw Sources** | `3-resources/raw/` | Bất biến. LLM chỉ đọc, tuyệt đối không ghi (Rule 12). |
| **The Wiki** | `3-resources/wiki/` | LLM sở hữu và bảo trì. Mọi tri thức đều có nguồn gốc truy vết được. |
| **The Schema** | `AGENTS.md`, `CLAUDE.md`, `AUDITOR_Protocol.md` | Quy định cách LLM vận hành wiki. |

### Ba phép vận hành (Three Operations)
| Phép vận hành | Lệnh | Mô tả |
| :--- | :--- | :--- |
| **Ingest** | `/distill`, `/consolidate` | Đọc raw → Khai thác → Ghi wiki → Update index → Append log. |
| **Query + File-Back** | `/file-back` | Trả lời từ Wiki. Kết quả tốt được nộp ngược thành Wiki page mới. |
| **Lint** | `/lint` | Định kỳ kiểm tra sức khỏe: mâu thuẫn, orphan pages, stale claims. |

### 🔍 Future Tools (Bookmark — chưa implement)
| Tool | Repo | Khi nào dùng |
| :--- | :--- | :--- |
| **qmd** | https://github.com/tobi/qmd | Khi Concept pages > 200, cần semantic search nội dung. BM25 + Vector + MCP server. |
