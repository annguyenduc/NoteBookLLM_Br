---
name: wiki-web-scrape
description: "Trích xuất Markdown từ URL (Wikipedia, trang web) qua Lightpanda vào 00_Inbox/. Cấm ghi thẳng vào raw/."
---

# Thu Thập Web (Web Scrape)

## Khi Nào Dùng
Khi cần lấy nội dung từ trang web tĩnh, công khai để đưa vào `00_Inbox/` cho review và ingest chính thức.

## Quy Tắc Bắt Buộc
- **RANH GIỚI STAGING**: KHÔNG BAO GIỜ ghi thẳng vào `3-resources/raw_*/` — đây là vùng bất biến (R1)
- **MỤC TIÊU DUY NHẤT**: Mọi output phải lưu vào `00_Inbox/`
- **KHÔNG có ảnh chụp màn hình**: Nếu cần visual evidence (R10), dừng lại và dùng `wiki-crawl-4ai`

## Quy Trình

1. Xác nhận URL tĩnh và công khai
2. Chạy lệnh staging:
   ```
   python .agent/skills/wiki-web-scrape/scripts/lightpanda_scrape.py --url "<url>" --output "00_Inbox/<tên-file>.md"
   ```
3. Kiểm tra chất lượng output trong inbox
4. Chuyển artifact đã xác nhận sang luồng `/ingest` chính thức qua `ingest-lifecycle`

## Lưu Ý Bàn Giao
- `wiki-web-scrape` kết thúc ở bước tạo staged inbox output + xác nhận thủ công
- Ingest chính thức phải tiếp tục qua `ingest-lifecycle`

## Lệnh Nhanh
```
python .agent/skills/wiki-web-scrape/scripts/lightpanda_scrape.py --url <URL> --output 00_Inbox/<tên>.md
```

## Lỗi Phổ Biến
| Lý do | Thực tế |
|---|---|
| "Ghi thẳng vào raw/ nhanh hơn" | Vi phạm R1/R4. Tốc độ không biện hộ cho việc phá vỡ toàn vẹn hệ thống |
| "Trang đơn giản, không sao" | Nếu có JS phức tạp, Lightpanda sẽ trả về text rỗng. Chuyển sang crawl-4ai |

## Chạy Test
```powershell
python .agent/skills/wiki-web-scrape/tests/test_scrape.py
```