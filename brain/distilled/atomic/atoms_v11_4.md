Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v11 về lập trình HaloCode trên nền tảng mBlock:

- **Fact:** HaloCode tích hợp một vòng LED gồm 12 bóng, được đánh số thứ tự từ 0 đến 11.
- **Source:** [vv11] - Section: Giải thích code Python & Bước 2: Viết Code Cyclone Game.
- **Tag:** [vv11]

- **Fact:** Trong môi trường mBlock Python cho HaloCode, việc gọi hàm đệ quy hoặc lồng ghép các hàm chứa vòng lặp (ví dụ: hàm reset gọi lại hàm chứa vòng lặp chính) có thể gây tràn bộ nhớ hoặc vượt quá giới hạn hệ thống, dẫn đến việc chương trình tự dừng sau khoảng 5 lần thực hiện.
- **Source:** [vv11] - Section: Nguyên nhân lỗi & Những điểm đã sửa.
- **Tag:** [vv11]

- **Fact:** Thư viện `halo` trong mBlock Python cung cấp các phương thức điều khiển LED bao gồm: `halo.led.show_single(index, r, g, b)` để bật một LED cụ thể, `halo.led.off_all()` để tắt toàn bộ LED, và `halo.led.show_all(r, g, b)` để bật tất cả LED cùng một màu.
- **Source:** [vv11] - Section: Bước 2: Viết Code Cyclone Game & Mã sửa lỗi hoàn chỉnh.
- **Tag:** [vv11]

- **Fact:** Trạng thái của cảm biến chạm trên HaloCode được kiểm tra thông qua lệnh `halo.touchpad0.is_touched()`, trả về giá trị logic tương ứng với việc người dùng có đang chạm vào cảm biến hay không.
- **Source:** [vv11] - Section: Bước 2: Viết Code Cyclone Game.
- **Tag:** [vv11]

- **Fact:** Một số phiên bản hoặc chế độ lập trình trên mBlock không hỗ trợ các từ khóa Boolean tiêu chuẩn (`True`/`False`), yêu cầu lập trình viên sử dụng giá trị số nguyên (`1`/`0`) để thay thế trong các cấu trúc điều kiện và vòng lặp.
- **Source:** [vv11] - Section: Trong lập trình halocode trên mblock không có block True/False.
- **Tag:** [vv11]

- **Fact:** Cấu trúc vòng lặp `while True:` đặt trong sự kiện `@event.start` (on_start) là giải pháp tối ưu để duy trì chương trình chạy vô hạn trên HaloCode mà không gặp lỗi giới hạn tầng lặp của hệ thống.
- **Source:** [vv11] - Section: Cách sửa lỗi (Mã sửa lỗi hoàn chỉnh).
- **Tag:** [vv11]

- **Fact:** Lệnh kiểm tra tư cách thành viên trong danh sách (`if x in [...]`) có thể không tương thích với một số trình biên dịch Python rút gọn trên mBlock, cần được thay thế bằng các phép so sánh logic rời rạc kết hợp với toán tử `or`.
- **Source:** [vv11] - Section: Dòng lệnh này trong block không có.
- **Tag:** [vv11]

- **Fact:** Độ khó của trò chơi dạng Cyclone trên vòng LED có thể được điều chỉnh bằng cách thay đổi tốc độ xoay (thông qua `time.sleep()`) hoặc giảm số lượng LED mục tiêu sáng cùng lúc.
- **Source:** [vv11] - Section: NÂNG ĐỘ KHÓ LÊN MỘT CHÚT.
- **Tag:** [vv11]