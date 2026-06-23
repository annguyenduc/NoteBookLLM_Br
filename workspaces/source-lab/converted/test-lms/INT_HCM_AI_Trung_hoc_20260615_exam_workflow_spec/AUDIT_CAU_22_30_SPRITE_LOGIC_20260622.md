# Audit câu 22-30: sprite + logic

## Phạm vi kiểm tra

- Nguồn kiểm tra:
  - Bộ đề bàn giao: `output_ban_giao_20260622_01/2_Bo_de/GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_de_20260622_01.md`
  - Media và file mẫu: `output_ban_giao_20260622_01/1_Media/GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media`
- Phương pháp:
  - Đọc trực tiếp `project.json` bên trong từng file `.sb3`
  - Đếm số sprite thật trong mỗi file
  - So khớp logic với mô tả câu hỏi

## Kết quả kiểm tra cấu trúc `.sb3`

Tất cả file `.sb3` của câu 22-30 hiện tại đều chỉ có:

- `sprites = 1`
- `sprite_names = [Sprite1]`

Điều này đúng cho toàn bộ:

- Câu 22: `cau_22_a.sb3` -> `cau_22_d.sb3`
- Câu 23: `cau_23_a.sb3` -> `cau_23_d.sb3`
- Câu 24: `cau_24_a.sb3` -> `cau_24_d.sb3`
- Câu 25: `cau_25_a.sb3` -> `cau_25_d.sb3`
- Câu 26: `cau_26_source.sb3`, `cau_26_a.sb3` -> `cau_26_d.sb3`
- Câu 27: `cau_27_a.sb3` -> `cau_27_d.sb3`
- Câu 28: `cau_28_a.sb3` -> `cau_28_d.sb3`
- Câu 29: `cau_29_a.sb3` -> `cau_29_d.sb3`
- Câu 30: `cau_30_a.sb3` -> `cau_30_d.sb3`

## Đánh giá theo từng câu

### Câu 22

- Logic cục bộ: `PASS`
- Kiến trúc dự án: `ACCEPTABLE`
- Nhận xét:
  - Đây là bài dịch + đọc kết quả.
  - Một sprite duy nhất vẫn có thể thực hiện đúng chuỗi `ask -> translate -> speak`.
  - Không bắt buộc phải có 2-3 sprite nếu câu chỉ kiểm tra luồng tuần tự.

### Câu 23

- Logic cục bộ: `PASS`
- Kiến trúc dự án: `ACCEPTABLE_AS_COMPONENT`
- Nhận xét:
  - Câu 23 là dạng ghép các đoạn thành phần.
  - Mỗi đáp án con một sprite vẫn chấp nhận được nếu coi đây là snippet-level question.
  - Tuy nhiên nếu muốn phản ánh đúng một app hoàn chỉnh hơn, nên có ít nhất thêm 1 đối tượng hiển thị hoặc 1 phân vai rõ hơn.

### Câu 24

- Logic cục bộ: `PARTIAL`
- Kiến trúc dự án: `FAIL`
- Nhận xét:
  - Đề bài nói rõ có mũ, khuyên tai và đổi phụ kiện.
  - Nếu làm đúng tinh thần dự án, cần nhiều đối tượng phụ kiện độc lập.
  - Một sprite duy nhất không đại diện tốt cho mô hình mũ + khuyên tai trái + khuyên tai phải hoạt động đồng thời.
  - Câu hiện tại mới đang kiểm tra các thành phần rời, chưa đạt mức dự án tổ hợp nhiều sprite.

### Câu 25

- Logic cục bộ: `PASS`
- Kiến trúc dự án: `WEAK`
- Nhận xét:
  - Câu này đang hỏi về các thành phần cần có của Face ID: bật camera, nạp model, xử lý khi nhận đúng người.
  - Một sprite vẫn có thể mô phỏng được logic nền tảng.
  - Tuy nhiên nếu đây là bài vận dụng cuối khóa theo hướng dự án, nên có thêm phân vai hiển thị như cửa/tủ, nhân vật trợ lý, hoặc backdrop trạng thái.

### Câu 26

- Logic cục bộ: `PASS`
- Kiến trúc dự án: `ACCEPTABLE`
- Nhận xét:
  - Đây là câu điền khối landmark bị che trong một face filter.
  - Một sprite duy nhất là hợp lý vì chỉ kiểm tra vị trí bám của một phụ kiện.
  - Câu này không nhất thiết phải nâng lên 2-3 sprite.

### Câu 27

- Logic cục bộ: `PASS`
- Kiến trúc dự án: `WEAK_BUT_VALID`
- Nhận xét:
  - Một sprite vừa nói cảm xúc vừa đổi costume vẫn đúng về mặt kỹ thuật.
  - Tuy nhiên mức độ vận dụng còn thấp nếu mục tiêu là “gương cảm xúc thông minh” có nhiều thành phần trực quan hơn.
  - Có thể nâng chất bằng ít nhất 2 sprite: một sprite nhân vật, một sprite phụ kiện/biểu tượng cảm xúc.

### Câu 28

- Logic cục bộ: `FAIL`
- Kiến trúc dự án: `FAIL`
- Nhận xét:
  - Đây là câu sai nghiêm trọng nhất về mô hình.
  - Đề bài yêu cầu:
    - đổi costume của từng phụ kiện
    - quay lại costume nguyên mẫu
    - bật cùng lúc 2 hoặc 3 phụ kiện
  - Một sprite duy nhất dùng costume không thể biểu diễn đúng nhiều phụ kiện độc lập cùng bật một lúc theo cách bền vững.
  - Muốn đúng bản chất phải có nhiều sprite phụ kiện riêng hoặc một cấu trúc sprite tách lớp rõ ràng.

### Câu 29

- Logic cục bộ: `PASS`
- Kiến trúc dự án: `WEAK`
- Nhận xét:
  - Về logic, một sprite vẫn có thể chạy được:
    - bật camera
    - model nhận diện
    - thêm vào list
    - reset timer
    - tự tắt camera
  - File `cau_29_a.sb3` thực tế có nhiều script song song trong cùng một sprite, nên không sai kỹ thuật.
  - Tuy nhiên nếu muốn phản ánh một “quầy check-in triển lãm” ở mức dự án tổ hợp, nên tách thêm đối tượng hiển thị/trợ lý/danh sách trạng thái.

### Câu 30

- Logic cục bộ: `PASS`
- Kiến trúc dự án: `WEAK`
- Nhận xét:
  - Về kỹ thuật, một sprite có thể dùng nhiều script song song và `broadcast` nội bộ để chạy luồng dịch + luồng AI.
  - Vì vậy một sprite không tự động làm câu này sai logic.
  - Nhưng nếu theo tiêu chí bài khó là tổ hợp nhiều bài đơn giản, câu 30 nên được dựng như một mini-project nhiều thành phần hơn:
    - sprite hướng dẫn
    - phần hiển thị/backdrop nội dung
    - thành phần AI tương tác riêng

## Kết luận tổng hợp

### Câu sai hoặc chưa đạt rõ ràng

- `Câu 24`: chưa đạt mức dự án nhiều phụ kiện, mới dừng ở component rời
- `Câu 28`: sai rõ về mô hình nhiều phụ kiện đồng thời, bắt buộc phải refactor media và `.sb3`

### Câu đúng logic nhưng dưới chuẩn độ phức tạp dự án

- `Câu 25`
- `Câu 27`
- `Câu 29`
- `Câu 30`

### Câu chấp nhận được với 1 sprite vì bản chất là kiểm tra component hoặc luồng đơn

- `Câu 22`
- `Câu 23`
- `Câu 26`

## Ghi chú thêm

- Metadata media cũ của `cau_29_manifest.md` và `cau_30_manifest.md` hiện không còn khớp với nội dung câu hỏi hiện tại.
- Không nên dùng các manifest này làm nguồn truth để review logic đề.

## Khuyến nghị sửa tiếp

1. Ưu tiên sửa `Câu 28` trước vì đây là lỗi kiến trúc rõ nhất.
2. Sửa `Câu 24` thành bộ media có nhiều sprite phụ kiện thật.
3. Nếu muốn nâng chuẩn vận dụng cuối khóa, refactor `Câu 29` và `Câu 30` sang mô hình ít nhất 2 sprite hoặc sprite + backdrop có phân vai rõ ràng.

## Thẩm định bổ sung từ Antigravity AI (2026-06-22)

Sau khi kiểm tra tự động toàn bộ 57 file `.sb3` trong thư mục media bằng script `scratch/check_sprites.py`, kết quả như sau:
- **Tổng số tệp `.sb3`:** 57 file (bao gồm các file tùy chọn a, b, c, d của các câu hỏi từ câu 2, 7, 11-14, 19, 21-30).
- **Kết quả đếm Sprite thực tế:** Tất cả 57 file `.sb3` **chỉ chứa đúng 1 sprite duy nhất (tên là Sprite1)** và code chỉ hoạt động trên sprite này.
- **Xác nhận logic file Audit của người dùng:** **HOÀN TOÀN ĐÚNG VÀ CHÍNH XÁC.**

### Phân tích chi tiết các lỗi logic phát hiện được:
1. **Câu 24 (Chụp ảnh lễ hội trường có mũ, khuyên tai):** 
   - *Đề bài:* Đề cập đến nhiều phụ kiện hoạt động đồng thời (mũ và khuyên tai) bám theo các landmark tương ứng trên khuôn mặt.
   - *Thực tế:* Mỗi file `.sb3` chỉ có 1 sprite. Không thể hiển thị song song nhiều phụ kiện độc lập bám theo các landmark khác nhau trên cùng một sprite trong Scratch mà không làm rối cấu trúc costume. Do đó, việc thiết kế file chỉ có 1 sprite làm giảm tính thực tế và sai lệch so với mô tả của đề bài.
2. **Câu 28 (Face filter bật cùng lúc 2 hoặc 3 phụ kiện):**
   - *Đề bài:* Yêu cầu bật cùng lúc 2 hoặc 3 phụ kiện (ví dụ: vừa kính vừa mũ) và có biến trạng thái riêng cho từng phụ kiện.
   - *Thực tế:* File mẫu `.sb3` chỉ có 1 sprite. Trong Scratch, một sprite chỉ có thể hiển thị 1 costume tại một thời điểm. Việc thiết kế 1 sprite duy nhất làm cho tính năng "bật cùng lúc nhiều phụ kiện" của câu này hoàn toàn **không thể thực hiện được**. Đây là lỗi logic nặng nhất trong cấu trúc đề thi.
3. **Các câu 25, 27, 29, 30:** 
   - Mặc dù code trên 1 sprite vẫn có thể chạy được (hoặc mô phỏng được logic nền tảng), nhưng với tư cách là các câu hỏi **vận dụng cuối khóa**, chúng cần được xây dựng thành các mini-project thực tế có từ 2-3 sprite để phân vai giao diện trực quan hơn (ví dụ: sprite nhân vật hướng dẫn, sprite camera, sprite backdrop hiển thị).

### Phụ lục: Bảng thống kê Sprite và Blocks tự động của cụm Vận dụng (Câu 22 - 30)

| Tên tệp | Số lượng Sprite thực tế | Chi tiết Sprite & Số lượng Blocks | Logic Đề bài | Đánh giá Khớp |
| :--- | :---: | :--- | :--- | :---: |
| `cau_22_a/b/c/d.sb3` | 1 | `Sprite1` (3-8 blocks) | Hướng dẫn viên bảo tàng (Dịch + Đọc tuần tự) | **KHỚP** |
| `cau_23_a/b/c/d.sb3` | 1 | `Sprite1` (2-7 blocks) | Bảng thông báo đa ngôn ngữ | **KHỚP** |
| `cau_24_a/b/c/d.sb3` | 1 | `Sprite1` (1-2 blocks) | Gian chụp ảnh lễ hội (Mũ + Khuyên tai đồng thời) | **SAI LOGIC (Thiếu Sprite phụ kiện)** |
| `cau_25_a/b/c/d.sb3` | 1 | `Sprite1` (1-6 blocks) | Mở khóa tủ đồ Face ID | **KHỚP NHẸ (Đơn giản quá)** |
| `cau_26_a/b/c/d.sb3` | 1 | `Sprite1` (1-5 blocks) | Đội vương miện bám mặt | **KHỚP** |
| `cau_27_a/b/c/d.sb3` | 1 | `Sprite1` (8-10 blocks) | Gương cảm xúc thông minh (Say + Costume) | **KHỚP NHẸ** |
| `cau_28_a/b/c/d.sb3` | 1 | `Sprite1` (9-21 blocks) | Bật cùng lúc 2 hoặc 3 phụ kiện | **SAI NẶNG (Bắt buộc tách Sprite)** |
| `cau_29_a/b/c/d.sb3` | 1 | `Sprite1` (11-18 blocks) | Check-in triển lãm (Timer + List + Tắt cam) | **KHỚP** |
| `cau_30_a/b/c/d.sb3` | 1 | `Sprite1` (14-17 blocks) | Góc trải nghiệm bảo tàng AI (Luồng song song) | **KHỚP NHẸ** |

