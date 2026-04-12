Chào bạn, việc tạm dừng và tắt máy để đảm bảo an toàn là một quyết định đúng đắn. Dưới đây là các sự kiện kỹ thuật và hướng dẫn để bạn tiếp tục in trên **Elegoo Neptune 4**.

### 1. Trích xuất sự kiện kỹ thuật (Facts)

- **Fact:** Máy in Elegoo Neptune 4 có tính năng "Power Loss Recovery" (Khôi phục sau khi mất điện), cho phép tiếp tục in từ lớp bị gián đoạn.
- **Source:** Quy trình vận hành máy in 3D Klipper.
- **Tag:** [Unverified_Source]

- **Fact:** Nhiệt độ bàn in (Bed Temperature) trong profile Neptune 4 thường được thiết lập từ 60°C đến 65°C để duy trì độ bám dính của PLA.
- **Source:** Dữ liệu RAW v06 - Section: [values] & [overrides].
- **Tag:** [vv06]

- **Fact:** Khi tắt nguồn hoàn toàn, bàn nhiệt sẽ nguội đi, khiến nhựa PLA co lại và có nguy cơ bong khỏi bề mặt bàn in (đặc biệt là mặt PEI).
- **Source:** Nguyên lý vật liệu in 3D.
- **Tag:** [Unverified_Source]

---

### 2. Hướng dẫn cách tiếp tục in trên Neptune 4

Để tiếp tục in sau khi bạn quay trở lại, hãy làm theo các bước sau:

**Bước 1: Trước khi tắt máy (Quan trọng)**
- Nếu có thể, hãy nhấn nút **Pause** trên màn hình cảm ứng của máy in. Việc này giúp đầu phun (Nozzle) di chuyển ra khỏi vị trí đang in (Parking), tránh việc nhiệt độ dư làm chảy một lỗ trên bề mặt sản phẩm tại điểm dừng.
- Sau khi máy đã Pause và đầu phun đã tách ra, bạn có thể tắt công tắc nguồn.

**Bước 2: Khi quay trở lại in**
1. Bật công tắc nguồn của máy in.
2. Đợi màn hình khởi động xong. Một thông báo sẽ hiện lên: **"Power loss detected. Continue printing?"** (Phát hiện mất điện. Tiếp tục in?).
3. Chọn **Confirm** hoặc **Yes**.
4. Máy sẽ bắt đầu hâm nóng lại đầu phun và bàn in về nhiệt độ thiết lập (ví dụ: 200°C/60°C như trong profile [vv06]).
5. Sau khi đạt nhiệt độ, máy sẽ tự động di chuyển về vị trí cũ và tiếp tục in.

---

### ⚠️ Lưu ý rủi ro (Cực kỳ quan trọng)

1. **Nguy cơ bong sản phẩm:** Đây là rủi ro lớn nhất. Khi bàn in nguội xuống nhiệt độ phòng, nhựa PLA sẽ mất độ bám dính với tấm PEI. Nếu sản phẩm bị bong hoặc xê dịch dù chỉ 1mm trong lúc máy tắt, khi in lại, đầu phun sẽ đâm vào sản phẩm hoặc in "trên không", gây hỏng bản in.
   - *Mẹo:* Nếu bạn thấy sản phẩm đã bị bong nhẹ ở mép, không nên in tiếp vì sẽ hỏng máy.

2. **Vết lằn trên sản phẩm:** Tại vị trí dừng và in lại thường sẽ xuất hiện một đường kẻ ngang (seam) do sự chênh lệch nhiệt độ giữa hai lần in.

3. **Lỗi kẹt nhựa (Heat Creep):** Khi tắt nguồn đột ngột, quạt tản nhiệt đầu phun cũng dừng lại. Nhiệt độ dư từ cục sưởi có thể lan ngược lên trên làm chảy nhựa ở đoạn ống dẫn, gây kẹt nhựa khi khởi động lại.

**Lời khuyên:** Nếu sản phẩm Tiger của bạn đã in được hơn 70% và bạn phải đi lâu (qua đêm), hãy cân nhắc rủi ro bong bàn in. Nếu chỉ đi ngắn hạn, tính năng Resume của Neptune 4 hoạt động khá tin cậy.

Bạn có cần mình hướng dẫn cách xử lý nếu máy không tự hiện thông báo Resume không?