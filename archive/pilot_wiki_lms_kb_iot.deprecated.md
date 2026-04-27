# WORKFLOW: Pilot — Tạo Wiki Pages từ LMS_KB_IOT.md
# Lưu tại: .agent/workflows/pilot_wiki_lms_kb_iot.md
# Dùng trong Antigravity: paste prompt từng bước vào chat

---

## MỤC TIÊU
Tạo ~10 Wiki Pages mẫu từ file `brain/raw/LMS_KB_IOT.md`
vào `brain/wiki/` theo đúng template `WIKI_TEMPLATE.md`.

## ĐIỀU KIỆN TIÊN QUYẾT
- [ ] `brain/raw/LMS_KB_IOT.md` tồn tại
- [ ] `brain/wiki/WIKI_TEMPLATE.md` tồn tại
- [ ] `brain/log.md` tồn tại

---

## ═══════════════════════════════════════════
## BƯỚC 1 — Paste prompt này vào Antigravity
## ═══════════════════════════════════════════

```
@scout

CHECKPOINT bắt buộc — trả lời trước khi làm bất cứ điều gì:

```yaml
CHECKPOINT:
  agent: "@scout"
  task: "Đọc LMS_KB_IOT.md, liệt kê tất cả tags duy nhất"
  step: "1 / 4"
  output_file: "Danh sách tags — in ra màn hình, KHÔNG tạo file"
  stop_condition: "Sau khi in xong danh sách tags → DỪNG, chờ confirm"
  prerequisites:
    - file: "brain/raw/LMS_KB_IOT.md"
      exists: "?"
    - file: "brain/wiki/WIKI_TEMPLATE.md"  
      exists: "?"
  status: "READY | BLOCKED"
```

Sau khi confirm CHECKPOINT:
1. Đọc file `brain/raw/LMS_KB_IOT.md`
2. Tìm TẤT CẢ tags duy nhất — tags nằm sau `::` ở cuối mỗi fact, ví dụ `[Arduino Power]`, `[Servo Motor]`
3. In ra danh sách dạng:
   - [Tag 1] — X facts
   - [Tag 2] — Y facts
   - ...
4. DỪNG. Chờ tôi chọn tags nào làm trước.
```

---

## ═══════════════════════════════════════════
## BƯỚC 2 — Sau khi @scout trả về danh sách tags
## Chọn 5 tags rõ nhất, paste prompt này
## ═══════════════════════════════════════════

```
@scout

CHECKPOINT:

```yaml
CHECKPOINT:
  agent: "@scout"
  task: "Tạo Wiki Pages cho 5 tags đã chọn"
  step: "2 / 4"
  output_file: "brain/wiki/ATOMS_[TAG].md × 5 files"
  stop_condition: "Tạo đủ 5 files → DỪNG, báo cáo danh sách files đã tạo"
  prerequisites:
    - file: "brain/wiki/WIKI_TEMPLATE.md"
      exists: "YES"
  status: "READY"
```

Tạo atomic note cho các tags sau: [DÁN DANH SÁCH 5 TAGS VÀO ĐÂY]

Với MỖI tag:
1. Đọc template tại `brain/wiki/WIKI_TEMPLATE.md`
2. Tạo file `brain/wiki/ATOMS_[tên_tag_snake_case].md`
3. Điền đúng theo template — KHÔNG thêm nội dung ngoài template
4. Phần "Liên kết tư duy": tìm ít nhất 2 tags khác trong cùng file có thể link
5. Phần "Nguồn": ghi chính xác `brain/raw/LMS_KB_IOT.md — tag [TÊN TAG]`

SAU KHI TẠO XONG 5 FILES → DỪNG HOÀN TOÀN.
In ra:
- Danh sách 5 files đã tạo
- Với mỗi file: `wikilinks` đã inject là gì
```

---

## ═══════════════════════════════════════════
## BƯỚC 3 — Verify thủ công (BẠN TỰ LÀM)
## ═══════════════════════════════════════════

Mở từng file trong `brain/wiki/`, kiểm tra checklist:

```
Với mỗi file ATOMS_*.md:
[ ] Chỉ có 1 khái niệm duy nhất?
[ ] Có ít nhất 2 `wikilinks`?
[ ] Phần Futures không trống?
[ ] Nguồn trace được về brain/raw/LMS_KB_IOT.md?
[ ] Không có nội dung hallucinate (facts không có trong file gốc)?
```

Nếu tất cả pass → chạy Bước 4.
Nếu có file fail → ghi lại lỗi cụ thể, báo @healer sửa trước khi tiếp tục.

---

## ═══════════════════════════════════════════
## BƯỚC 4 — Ghi log và update status
## ═══════════════════════════════════════════

```
@devops

Append vào `brain/log.md`:

## [YYYY-MM-DD HH:MM] ingest | @scout | Pilot atoms từ LMS_KB_IOT.md
- Files tạo: [danh sách 5 files]
- Wikilinks inject: [tổng số links]
- Verify: PASS / FAIL
- Notes: [ghi chú nếu có]
```

---

## SAU KHI PILOT PASS

Nếu 5 atoms đầu tiên đúng format, bước tiếp theo:
→ Chạy batch toàn bộ tags còn lại trong LMS_KB_IOT.md
→ Sau đó mới chuyển sang MASTER_CONV_ATOMS.md

KHÔNG batch sang file mới khi pilot chưa pass.
