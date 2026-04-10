# 🔥 Burn Token — PDF Batch Translator

Hệ thống dịch PDF hàng loạt tự động bằng AI miễn phí (Qwen qua OpenRouter).

**Pipeline:** `PDF → Trích xuất text → Chia chunk → Qwen dịch → Làm sạch JSON → Kiểm chứng → Xuất PDF tiếng Việt`

---

## 📋 Yêu cầu

- Python 3.10 trở lên
- Tài khoản [OpenRouter](https://openrouter.ai) (miễn phí, không cần thẻ tín dụng)
- Kết nối Internet

---

## 🚀 Cài đặt (Chạy 1 lần)

### Bước 1 — Tải thư viện Python

Mở **PowerShell** trong thư mục `d:\Burn_Token\`:

```powershell
pip install -r requirements.txt
```

### Bước 2 — Cấu hình API Key

1. Vào [https://openrouter.ai/keys](https://openrouter.ai/keys) → tạo API key miễn phí
2. Copy file `.env.example` thành `.env`:

```powershell
copy .env.example .env
```

3. Mở file `.env` bằng Notepad và điền API key vào:

```
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxx
```

### Bước 3 — Tải font tiếng Việt + kiểm tra cấu hình

```powershell
python main.py --setup
```

Lệnh này sẽ:
- Tải font **DejaVu Sans** (hỗ trợ tiếng Việt đầy đủ)
- Kiểm tra API key
- Tạo các thư mục cần thiết

---

## 📖 Cách sử dụng

### Dịch tất cả PDF trong thư mục `./input/`

```powershell
# 1. Thả file PDF vào thư mục input/
# 2. Chạy lệnh:
python main.py
```

PDF đã dịch sẽ xuất hiện trong `./output/` với tên `[tên_gốc]_vi.pdf`

### Các lệnh khác

```powershell
# Dịch một file cụ thể
python main.py --input ./input/document.pdf

# Dịch một thư mục con
python main.py --input ./input/batchA/

# Tắt validation (nhanh hơn ~2x, tiết kiệm quota hơn)
# Dùng khi bạn cần dịch nhanh, không cần kiểm chứng
python main.py --no-validate

# Test thử với file PDF mẫu tự tạo
python main.py --test

# Kiểm tra lại cấu hình
python main.py --setup
```

---

## 🏗️ Kiến trúc Pipeline

```
┌─────────────┐     ┌─────────────┐     ┌─────────────────────────────────────┐
│  PDF Input  │────▶│  Step 1     │────▶│  Dict[page_num, text]               │
│             │     │  Extract    │     │                                     │
└─────────────┘     └─────────────┘     └─────────────────────────────────────┘
                                                          │
                                        ┌─────────────────▼─────────────────┐
                                        │  Step 2: Chunk                    │
                                        │  Chia ≤ 600 token/chunk           │
                                        │  Giữ nguyên ranh giới câu         │
                                        └─────────────────┬─────────────────┘
                                                          │
                                        ┌─────────────────▼─────────────────┐
                                        │  Step 3: Worker (Qwen 72B)        │
                                        │  Dịch từng chunk → JSON           │
                                        │  Cache MD5 nếu input trùng        │
                                        └─────────────────┬─────────────────┘
                                                          │
                                        ┌─────────────────▼─────────────────┐
                                        │  Step 4: JSON Sanitizer            │
                                        │  Trích xuất JSON, tự sửa lỗi      │
                                        │  Gắn cờ retry nếu không sửa được  │
                                        └─────────────────┬─────────────────┘
                                                          │
                                        ┌─────────────────▼─────────────────┐
                                        │  Step 5: Validator (Fallback)     │
                                        │  DeepSeek R1 → Llama 3.3 → Qwen   │
                                        │  Tự đổi model khi hết 429 quota   │
                                        └─────────────────┬─────────────────┘
                                                          │
                                        ┌─────────────────▼─────────────────┐
                                        │  Step 6: Merge & Export            │
                                        │  Retry chunk lỗi (max 3 lần)      │
                                        │  Xuất PDF tiếng Việt               │
                                        └─────────────────┬─────────────────┘
                                                          │
                                        ┌─────────────────▼─────────────────┐
                                        │       output/[tên]_vi.pdf          │
                                        └───────────────────────────────────┘
```

---

## ⚙️ Cấu hình nâng cao (`config.yaml`)

| Tham số | Mặc định | Ý nghĩa |
|---------|----------|---------|
| `pipeline.chunk_size` | 600 | Token tối đa mỗi chunk. Giảm xuống 400 nếu model thường trả lỗi |
| `pipeline.max_retries` | 3 | Số lần retry tối đa cho mỗi chunk lỗi |
| `pipeline.base_delay` | 3.0 | Giây chờ giữa các request (tăng nếu hay bị 429) |
| `validation.enabled` | true | `false` để tắt validation, tiết kiệm gần 50% quota |
| `validation.confidence_threshold` | 0.75 | Chỉ validate chunk có confidence < ngưỡng |
| `cache.enabled` | true | Tắt nếu muốn dịch lại tất cả từ đầu |

### Thêm/đổi validator model

Trong `config.yaml`, mục `models.validators` là danh sách **fallback chain** — khi model đầu tiên hết 200 req/ngày, tự động thử model tiếp theo:

```yaml
models:
  validators:
    - "openrouter/deepseek/deepseek-r1:free"       # Thử đầu tiên
    - "openrouter/meta-llama/llama-3.3-70b-instruct:free"  # Fallback 1
    - "openrouter/qwen/qwen3.6-plus-preview:free"   # Fallback 2
```

---

## ⚠️ Giới hạn Free Tier OpenRouter

| Giới hạn | Giá trị | Giải pháp |
|----------|---------|-----------|
| Request/phút | ~20 | Pipeline tự delay, không cần lo |
| Request/ngày | ~200/model | Dùng fallback chain nhiều model |
| PDF scan (ảnh) | Không hỗ trợ | Cần OCR riêng (ngoài scope) |
| Phù hợp dùng cho | Nghiên cứu, cá nhân | Không dùng production |

> **Mẹo tiết kiệm quota:** Dùng `--no-validate` khi dịch lần đầu. Chỉ validate khi cần kiểm tra chất lượng.

---

## 📁 Cấu trúc thư mục

```
d:\Burn_Token\
├── .env                    ← API key (KHÔNG chia sẻ!)
├── config.yaml             ← Cấu hình pipeline
├── main.py                 ← Chạy từ đây
├── setup_fonts.py          ← Tải font lần đầu
├── requirements.txt        ← Thư viện cần cài
│
├── core/                   ← Tiện ích dùng chung
│   ├── llm_client.py       ← Gọi AI + fallback
│   ├── schemas.py          ← Định nghĩa JSON schema
│   ├── logger.py           ← Log màu sắc + file
│   └── rate_limiter.py     ← Tránh bị block 429
│
├── pipeline/               ← 6 bước xử lý
│   ├── step1_extract.py    ← PDF → Text
│   ├── step2_chunk.py      ← Text → Chunks
│   ├── step3_worker.py     ← Qwen dịch
│   ├── step4_sanitize.py   ← Sửa JSON lỗi
│   ├── step5_validate.py   ← Kiểm chứng chất lượng
│   └── step6_merge.py      ← Gộp → PDF
│
├── input/                  ← 📥 Thả PDF vào đây
├── output/                 ← 📤 PDF đã dịch ra đây
├── fonts/                  ← Font tiếng Việt (tự động tải)
└── logs/                   ← Log + cache kết quả dịch
```

---

## 🐛 Xử lý lỗi thường gặp

**Lỗi: `OPENROUTER_API_KEY` không hợp lệ**
→ Kiểm tra file `.env`, đảm bảo key bắt đầu bằng `sk-or-v1-`

**Lỗi: Font không tìm thấy**
→ Chạy `python setup_fonts.py` hoặc `python main.py --setup`

**Lỗi: 429 Rate Limit quá nhiều**
→ Tăng `pipeline.base_delay` trong `config.yaml` lên 5 hoặc 10

**PDF không có text (trang ảnh scan)**
→ Phần mềm này chỉ đọc được text từ PDF có layer text. Cần OCR riêng cho ảnh scan.

**Output PDF không hiển thị đúng tiếng Việt**
→ Đảm bảo đã chạy `python setup_fonts.py` và thư mục `fonts/` tồn tại

---

## 📊 Ví dụ output terminal

```
╭─────────────────────────────────────────────────╮
│ 🔥 BURN TOKEN — PDF Batch Translator            │
│ Worker: Qwen 2.5 72B | Validator: DeepSeek R1   │
╰─────────────────────────────────────────────────╯

✓ Tìm thấy 3 file PDF cần dịch

──────────────── document1.pdf ─────────────────
[Step 1] Đọc: document1.pdf
  ✓ Đọc xong: 12/12 trang | 45,230 ký tự
[Step 2] Chia chunk (max 600 token/chunk)...
  ✓ Tổng: 38 chunks | 22,800 tokens ước tính
[Step 3] Dịch 38 chunks (English → Vietnamese)...
  ✓ Worker hoàn thành: 38/38 thành công | 5 cache hits
...

📊 Kết quả Pipeline
┌──────────────┬────────┬────────────┬──────────┬───────┬──────────┬──────────────────┐
│ File         │ Chunks │ Thành công │ Lỗi/Skip │ Tỉ lệ │ Thời gian│ Output           │
├──────────────┼────────┼────────────┼──────────┼───────┼──────────┼──────────────────┤
│ document1... │     38 │         38 │        0 │ 100%  │     142s │ document1_vi.pdf │
│ document2... │     52 │         51 │        1 │ 98.1% │     189s │ document2_vi.pdf │
└──────────────┴────────┴────────────┴──────────┴───────┴──────────┴──────────────────┘

Tổng kết: 2 files | Tỉ lệ thành công trung bình: 99.0%
```
