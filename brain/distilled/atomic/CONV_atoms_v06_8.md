Việc tạm dừng và tắt máy in 3D giữa chừng (để đảm bảo an toàn khi đi vắng) là một nhu cầu thực tế. **Elegoo Neptune 4** có tính năng **Resume Print** (tiếp tục in sau khi mất điện), nhưng bạn cần thực hiện đúng cách để tránh hỏng bản in.

Dưới đây là các bước và lưu ý quan trọng:

### 1. Các bước thực hiện an toàn
1.  **Nhấn nút PAUSE trên màn hình:** Đừng tắt cầu dao ngay lập tức. Khi nhấn Pause, đầu phun sẽ di chuyển ra khỏi vị trí đang in (thường là về góc hoặc nâng lên) để tránh làm chảy nhựa tại một điểm trên sản phẩm.
2.  **Đợi đầu phun nguội bớt (Khoảng 1-2 phút):** Khi bạn tắt máy, quạt tản nhiệt đầu phun cũng tắt. Nếu đầu phun còn quá nóng (200°C), nhiệt sẽ lan ngược lên trên (Heat creep) gây nghẹt nhựa. Hãy đợi nhiệt độ đầu phun xuống khoảng 150°C rồi hãy tắt công tắc.
3.  **Tắt công tắc/Cúp cầu dao:** Lúc này bạn có thể yên tâm đi công việc.

### 2. Cách tiếp tục in (Resume)
1.  **Bật máy trở lại:** Khi quay về, bạn bật công tắc nguồn.
2.  **Xác nhận trên màn hình:** Màn hình cảm ứng của Neptune 4 sẽ hiện thông báo: **"Power loss detected. Continue printing?"** (Phát hiện mất điện. Tiếp tục in không?).
3.  **Chọn "Yes" (hoặc Confirm):** Máy sẽ bắt đầu hâm nóng lại bàn in (Bed) và đầu phun (Nozzle). Sau khi đạt nhiệt độ yêu cầu, máy sẽ tự động in tiếp từ lớp đang dang dở.

---

### ⚠️ CẢNH BÁO QUAN TRỌNG (Rủi ro bong bàn)
Đây là vấn đề lớn nhất khi tắt máy lâu:
*   **Sản phẩm bị bong:** Khi bạn tắt điện, bàn in (Bed) sẽ nguội đi. Nhựa PLA bám trên bàn PEI nhờ nhiệt độ. Khi bàn nguội hẳn (về nhiệt độ phòng), nhựa sẽ co lại và **tự bong ra khỏi bàn**.
*   **Hậu quả:** Nếu sản phẩm đã bong hoặc lung lay, khi máy in tiếp, đầu phun sẽ đẩy sản phẩm đi và tạo ra một đống "mì tôm" nhựa hỏng.
*   **Lời khuyên:** Nếu bạn chỉ đi 1-2 tiếng, bàn in có thể vẫn còn hơi ấm và giữ được sản phẩm. Nếu đi quá lâu (qua đêm), khả năng cao là sản phẩm sẽ bong và không thể in tiếp được.

---

### Trích xuất sự kiện (Facts) theo yêu cầu:

- **Fact:** [CONV] [Neptune 4 hỗ trợ tính năng Resume Print, cho phép tiếp tục in sau khi mất điện hoặc tắt máy đột ngột.]
- **Source:** [v06 - Section: Neptune 4 Operation Manual / Power Loss Recovery]
- **Tag:** [vv06]

- **Fact:** [CONV] [Khi tắt máy in giữa chừng, nếu bàn in nguội hoàn toàn, sản phẩm PLA có nguy cơ cao bị bong khỏi bề mặt PEI, khiến việc in tiếp bị thất bại.]
- **Source:** [Unverified_Source]
- **Tag:** [vv06]

**Mẹo nhỏ:** Nếu bạn buộc phải tắt máy lâu, khi bật lại và trước khi nhấn "Yes" để in tiếp, hãy kiểm tra xem sản phẩm còn dính chắc trên bàn không. Nếu nó đã lỏng, tốt nhất là nên in lại từ đầu để tránh lãng phí thêm nhựa.