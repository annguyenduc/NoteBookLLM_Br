# 🎓 build-peda — Pedagogical Swarm System for STEM Education

> Hệ thống Swarm Agent tự động hoá quy trình thiết kế và sản xuất nội dung đào tạo STEM/AI cho giáo viên K-12, vận hành trên nền tảng LLM free-tier thông qua 9Router Gateway.

---

## 🎯 Mục tiêu dự án

1. **LLM Wiki Sư phạm** — Xây dựng kho tri thức sống (`brain/`) về đào tạo và giáo dục STEAM, tích lũy theo thời gian qua cơ chế Stream Ingest.
2. **Swarm Agent đúng vai** — Mỗi agent (@profiler, @designer, @engineer, @creative, @evaluator, @auditor) được giao đúng model AI phù hợp năng lực, có fallback tự động khi gặp lỗi.
3. **Sản xuất nội dung đào tạo** — Pipeline tự động tạo giáo án, slide, assignment cho một khoá học hoàn chỉnh, với cơ chế chunking để không vượt token limit của free tier.

---

## 🏗️ Kiến trúc hệ thống

```
build-peda/
├── brain/            # Wiki Knowledge Base (Raw, Wiki, Distilled, Process)
├── scripts/          # Các script automation (maintenance, pipelines, setup)
├── libs/             # Thư viện core và wrapper API
├── tools/            # Các công cụ bổ trợ hệ thống
├── assets/           # Tài nguyên tĩnh, hình ảnh, templates
├── storage/          # Dữ liệu tạm, logs thực thi (execution_manifest)
├── archive/          # Lưu trữ các tệp cũ hoặc atoms lỗi
├── AGENTS.md         # Registry Swarm Agent v4.0 Supreme
├── CLAUDE.md         # Operational Memory (LOM) & Session Context
├── COMMAND_BOARD.md  # Bảng điều khiển tác vụ hàng ngày
├── CONTINUITY.md     # Duy trì mạch tri thức giữa các phiên
└── AUDITOR_Protocol.md # Quy trình chống hallucination
```

---

## 🤖 Biệt đội Agent (Swarm Registry v4.0 Supreme)
Dự án vận hành theo mô hình Swarm với hệ thống Phân loại thông minh (Taxonomy). 

👉 **Xem chi tiết tại: [[AGENTS.md]]**

| Agent | Vai trò | Trọng tâm v4.0 |
| :--- | :--- | :--- |
| **@pm** | Planner | Lập kế hoạch & Điều phối Swarm. |
| **@scout** | Researcher | Nghiên cứu tri thức & Audit nguồn. |
| **@engineer** | Executioner | Viết mã nguồn & Thực thi TDD. |
| **@librarian** | Reviewer | Rà soát chất lượng & Quản lý Wiki. |
| **@auditor** | Integrity | Kiểm định tính xác thực (Rule 10). |
| **@designer** | ID Expert | Thiết kế learning sequence (5E/UDL). |

---

## 🔄 Pipeline Sư phạm (Rule 11 — Bắt buộc)

```
@profiler → @designer → @engineer → @evaluator
    ↑                                     ↓
    └──────────── @auditor (kiểm định) ───┘
```

Mọi tác vụ tạo nội dung đào tạo **bắt buộc** đi theo thứ tự này. Không bỏ qua bước nào.

---

## 📦 Output Chunking — Tạo slide & assignment không vượt token limit

Để tránh 429 rate limit khi tạo nội dung dài, `@engineer` sử dụng chiến lược chunked output:

| Loại nội dung | Chunk size | Số lần gọi API |
| :--- | :--- | :--- |
| Giáo án 90 phút | 1 call (~3k tokens) | 1 |
| Slide deck 20 trang | 5 slides/call | 4 calls |
| Assignment đầy đủ | Đề + Rubric + Key tách riêng | 3 calls |
| Khoá học hoàn chỉnh | Theo module | N calls |

Script: `scripts/chunked_engineer.py`

---

## 🚀 Khởi động nhanh

### 1. Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### 2. Cấu hình môi trường
```bash
# Copy và điền API key
cp .env.example .env
# NINEROUTER_API_KEY=your_key
# SMART_ROUTER_URL=http://localhost:20128/v1/chat/completions
# PEDAGOGICAL_MODEL_PRESET=free
```

### 3. Kiểm tra gateway
```bash
python scripts/verify_9router.py
python scripts/ping_free_tier.py  # Test tất cả model free
```

### 4. Chạy pipeline đầu tiên
```bash
python scripts/run_pipeline.py --module M2.1 --trainer-level entry
```

---

## 🛠️ Lệnh thường dùng

```bash
# Kiểm định sức khỏe Wiki
python scripts/brain_lint.py

# Cập nhật đồ thị tri thức
python scripts/graphify_bootstrap.py

# Xem execution manifest (verify swarm đã chạy đúng)
cat storage/execution_manifest.jsonl

# Tạo slide theo chunk
python scripts/chunked_engineer.py --output slide --module M2.1 --chunk-size 5
```

---

## 📋 Quy tắc vận hành

- **Anti-Hallucination**: Mọi claim phải có nguồn từ `brain/raw/` hoặc `brain/distilled/`. Xem `AUDITOR_Protocol.md`.
- **Log-First Ingest**: Mọi thay đổi tri thức ghi vào `brain/log.md` (append only).
- **Absolute Flatness**: Thư mục tối đa 2 cấp từ root. Dùng underscore prefix thay vì thư mục con.
- **Source Integrity**: Chỉ trích dẫn từ file gốc hiện tồn tại trong `brain/raw/`.

---

## 📊 Trạng thái dự án

- [x] Swarm Agent Registry v4.0 Supreme
- [x] LLM Client với fallback chain thông minh (404/429/502)
- [x] Pedagogical Pipeline (Rule 11)
- [x] Anti-Hallucination Protocol
- [ ] Chunked Engineer Script
- [ ] Ping Free Tier Script
- [ ] Execution Manifest Integration
- [ ] Brain content — Module M2.1 (ML for Kids)

---

*Framework: Antigravity v4.0 | Gateway: 9Router | Preset: Free Tier Supreme*