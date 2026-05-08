# 🎓 build-peda — Pedagogical Swarm System for STEM Education

> Hệ thống Swarm Agent tự động hoá quy trình thiết kế và sản xuất nội dung đào tạo STEM/AI cho giáo viên K-12, vận hành trên nền tảng LLM free-tier thông qua 9Router Gateway.

---

## 🎯 Mục tiêu dự án

1. **LLM Wiki Sư phạm** — Xây dựng kho tri thức sống (`3-resources/`) về đào tạo và giáo dục STEAM, tích lũy theo thời gian qua cơ chế Stream Ingest.
2. **Swarm Agent đúng vai** — Mỗi agent (@profiler, @designer, @engineer, @creative, @evaluator, @auditor) được giao đúng model AI phù hợp năng lực, có fallback tự động khi gặp lỗi.
3. **Sản xuất nội dung đào tạo** — Pipeline tự động tạo giáo án, slide, assignment cho một khoá học hoàn chỉnh, với cơ chế chunking để không vượt token limit của free tier.

---

## 🏗️ Kiến trúc hệ thống

```
build-peda/
├── 📥 00_Inbox/       # Khu vực chờ Markdown
├── 📁 1-projects/     # Các dự án thực thi
├── 📁 2-areas/        # Lĩnh vực trách nhiệm
├── 📁 3-resources/    # HẠ TẦNG TRI THỨC (Source of Truth)
│   ├── 📂 raw_sources/ # PDF/Video gốc (IMMUTABLE)
│   ├── 📂 raw_ingest/  # Markdown sạch (IMMUTABLE)
│   └── 📂 wiki/        # Kho tri thức Atomic
├── 📁 4-archive/      # Lưu trữ vĩnh viễn
├── 📁 .agent/         # Kỹ năng & Quy trình (Skills & Workflows)
├── AGENTS.md          # Registry Swarm Agent
├── SOUL.md            # Tính cách Agent
└── USER.md            # Hồ sơ User
```

---

## 🤖 Biệt đội Agent (Swarm Registry v4.0 Supreme)
Dự án vận hành theo mô hình Swarm với hệ thống Phân loại thông minh (Taxonomy). 

👉 **Xem chi tiết tại: [[AGENTS.md]]**

| Agent | Vai trò | Trọng tâm v2.8 |
| :--- | :--- | :--- |
| **@pm** | Planner | Lập kế hoạch & Điều phối Swarm. |
| **@scout** | Researcher | Nghiên cứu tri thức & Audit nguồn. |
| **@engineer** | Executioner | Viết mã nguồn & Thực thi TDD. |
| **@librarian** | Reviewer | Rà soát chất lượng & Quản lý Wiki. |
| **@auditor** | Integrity | Kiểm định tính xác thực (R10). |
| **@designer** | ID Expert | Thiết kế learning sequence (5E/UDL). |

---

## 🔄 Pipeline Sư phạm (R11 — Bắt buộc)

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

Script: `.agent/skills/pedagogy/scripts/chunked_engineer.py`

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
python .agent/skills/wiki-cleanup/scripts/lint_engine.py

# Cập nhật đồ thị tri thức (Rebuild Index)
python .agent/skills/wiki-rebuild/scripts/update_wiki_index.py

# Xem Dashboard trạng thái
python .agent/skills/wiki-status/scripts/dashboard.py
```

---

## 📋 Quy tắc vận hành

- **Anti-Hallucination**: Mọi claim phải có nguồn từ `3-resources/raw_sources/`.
- **Log-First Ingest**: Mọi thay đổi tri thức ghi vào `3-resources/wiki/log.md` (append only).
- **Absolute Flatness**: Thư mục tối đa 2 cấp từ root. Dùng underscore prefix thay vì thư mục con.
- **Source Integrity**: Chỉ trích dẫn từ file gốc hiện tồn tại trong `3-resources/raw_sources/`.

---

## 📊 Trạng thái dự án

- [x] Swarm Agent Registry v4.0 Supreme
- [x] LLM Client với fallback chain thông minh (404/429/502)
- [x] Pedagogical Pipeline (R11)
- [x] Anti-Hallucination Protocol
- [ ] Chunked Engineer Script
- [ ] Ping Free Tier Script
- [ ] Execution Manifest Integration
- [ ] Brain content — Module M2.1 (ML for Kids)

---

*Framework: Antigravity v4.0 | Gateway: 9Router | Preset: Free Tier Supreme*