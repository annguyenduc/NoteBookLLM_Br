# AGENTS.md - EduResearch Hub v2.0
> Runtime Source of Truth cho mọi Agent hoạt động trong dự án này.

---

## 1. Nguồn Sự Thật Khi Chạy (Runtime Source of Truth)
Nếu có mâu thuẫn khi chạy, ưu tiên theo thứ tự:
1. Chỉ dẫn của user trong phiên hiện tại (nếu không vi phạm an toàn).
2. `AGENTS.md` (File này).
3. `SOUL.md` (Triết lý và Ranh giới).
4. Các quy định được ghi trong thư mục `.agent/`.

## 2. Đường Dẫn Cốt Lõi (Edu Architecture v2.0)
Mọi tài nguyên và công việc đều được phân bổ vào 6 luồng sau. Tuyệt đối không tạo thêm thư mục gốc khác trừ khi được yêu cầu.

```
01_NghienCuu_Review/    ← Căn cứ nghiên cứu, chuẩn PRISMA
02_Khung_ChuyenMon/     ← Khung chương trình, chuẩn K-12, STEM
03_ThietKe_BaiDay/      ← Kế hoạch bài dạy, giáo án 3 mức độ
04_DanhGia_KiemTra/     ← Ma trận đề, Rubric đánh giá
05_Kho_NguyenLieu/      ← Kho chứa tài liệu thô, PDF, ảnh, media
06_LuuTru_Archive/      ← Kho lưu trữ dự án cũ, đồ án đã hoàn thành
.agent/                 ← "Não bộ" - Chứa scripts, kỹ năng, scratch và log
```
*Lưu ý: Mọi tài liệu nháp hoặc tạm thời phải được ghi vào `.agent/scratch/` hoặc thư mục vùng đệm được định cấu hình, không được ghi rải rác ngoài thư mục gốc.*

## 3. Vùng Đệm (Staging Buffer)
Mọi tài liệu thô mới tải về (từ web scrape, PDF) phải nằm ở **Vùng đệm** (do `.agent/config/workspace-routing.yaml` chỉ định, ví dụ `05_Kho_NguyenLieu/pdf_raw`).
- Không ghi trực tiếp vào các kho lưu trữ chính (`01` đến `04`) khi chưa qua xử lý/audit.
- Dùng kỹ năng `process-raw-resource` để đọc nhanh, `boc-tach-pdf` để OCR.

## 4. An Toàn Hành Động (Action Safety)
- **Read-only**: Các thao tác đọc, lập kế hoạch, phân tích trong chat không cần phê duyệt.
- **Write-mode**: Mọi thao tác GHI/XÓA/SỬA vào 6 luồng chính đều phải tuân theo `SOUL.md` (Human Governance Gate). Luôn hỏi ý kiến người dùng trước khi phá vỡ hiện trạng.
- **Cấm xóa**: Không được tự động xóa dữ liệu nguyên bản (PDF gốc, video gốc). Nếu cần dọn dẹp, di chuyển vào `06_LuuTru_Archive`.

## 5. Giao Thức Tạo File
- **R9 - TÌM TRƯỚC KHI TẠO**: Kiểm tra xem file tương đương đã có chưa, nếu có hãy sửa file đó (surgical diff).
- **R10 - KHÔNG HẬU TỐ LOẠN**: Tránh đặt tên kiểu `_v2`, `_final`. Thay vào đó, đặt tên rõ nghĩa hoặc lưu vào `.agent/scratch/` để kiểm thử.
- **R13 - DỌN DẸP**: Sau khi hoàn thành task, hãy dọn dẹp các file nháp tạo ra trong `.agent/scratch/`.

## 6. Kết Thúc Phiên Làm Việc (Session End)
Mỗi phiên có thay đổi lớn hoặc tạo future dependency, Agent BẮT BUỘC cập nhật tệp `CONTINUITY.md`:
```yaml
current_state: "[Đang ở đâu, đã làm xong gì]"
next_step_for_AN: "[Bước tiếp theo để User kiểm tra]"
blockers: "[Nêu rõ nếu có]"
```
Không để `CONTINUITY.md` quá dài, chỉ tóm tắt đúng trạng thái hiện tại.

## 7. Các Vai Trò Agent Chuyên Biệt
- `@pm`: Lập kế hoạch, quản lý tiến độ.
- `@scout`: Phân tích tài liệu thô từ Vùng đệm, tóm tắt kiến thức.
- `@engineer`: Lập trình, chạy script, tự động hóa tài liệu.
- `@designer`: Thiết kế luồng học tập, giáo án K-12.

