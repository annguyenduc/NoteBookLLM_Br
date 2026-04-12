Chào bạn, nếu đồng hồ hiện **0.00** khi đo dòng (Ampe), có nghĩa là **không có dòng điện chạy qua đồng hồ**. 

Dưới đây là các nguyên nhân và cách xử lý nhanh nhất để bạn thấy được con số:

### 1. Kiểm tra lại cách đấu nối (Quan trọng nhất)
Để đo dòng, bạn **bắt buộc** phải cắt đứt mạch điện và chèn đồng hồ vào giữa. 
- **Sai:** Chạm 2 que đo vào 2 cực của pin (đây là đo điện áp).
- **Đúng:** 
    1. Dây **Dương (+)** từ bo sạc nối vào **Que Đỏ**.
    2. **Que Đen** nối vào cực **Dương (+)** của pin.
    3. Cực **Âm (-)** của pin vẫn nối với cực **Âm (-)** của bo sạc.

### 2. Thang đo quá lớn so với dòng điện thực tế
Bạn đang để thang **20A**, trong khi pin của bạn đang ở trạng thái "hồi phục" (1.46V) nên dòng sạc có thể cực kỳ nhỏ (ví dụ 0.005A). Thang 20A sẽ không hiển thị được số lẻ nhỏ này và hiện **0.00**.

**👉 Cách xử lý:**
- Chuyển dây đỏ sang lỗ **mA**.
- Xoay núm đồng hồ về thang **200mA** (vùng A—).
- **Lưu ý:** Chỉ làm việc này khi bạn chắc chắn dòng sạc nhỏ (dưới 0.2A). Với pin đang 1.46V thì thường dòng rất nhỏ, nên cách này sẽ giúp bạn thấy số.

### 3. Cầu chì của đồng hồ bị đứt (Rất hay gặp)
Bên trong đồng hồ số có cầu chì bảo vệ cho các cổng đo dòng (mA hoặc 20A). Nếu trước đó bạn lỡ đo nhầm, cầu chì sẽ đứt và mạch bị hở, dẫn đến hiện **0.00**.

**👉 Cách kiểm tra cầu chì:**
- Chuyển đồng hồ về thang đo thông mạch (có tiếng "bíp").
- Dùng một đồng hồ khác (nếu có) hoặc dùng chính thang đo điện trở để đo thông mạch giữa các lỗ cắm trên đồng hồ. (Tuy nhiên cách này hơi khó nếu bạn chỉ có 1 đồng hồ).
- **Cách thử nhanh:** Cắm lại dây đo điện áp (V), nếu đo điện áp vẫn lên mà đo dòng không lên dù đã đấu nối tiếp đúng, thì 90% là **cầu chì đo dòng đã đứt**.

### 4. Pin hoặc Bo sạc đã ngắt
Vì pin của bạn đang ở mức 1.46V (quá thấp), bo sạc có thể đã tự ngắt để bảo vệ hoặc pin đã hỏng hoàn toàn không nhận dòng nữa.

---

### 🛠 Lời khuyên bước tiếp theo:
1. **Thử lại thang mA:** Chuyển dây đỏ sang lỗ **mA**, xoay núm về **200m** (trong vùng A—). Nếu hiện số (ví dụ 5.0 hoặc 10.0) thì tức là đang có dòng sạc nhỏ.
2. **Kiểm tra tiếp xúc:** Đảm bảo các đầu dây kẹp chắc chắn, không bị lỏng.

**Fact:** Khi pin Lithium 18650 rơi xuống dưới 2.5V, mạch sạc thông minh sẽ chỉ cấp dòng "mồi" (Trickle Charge) rất nhỏ để cứu pin.
**Source:** [Unverified_Source]
**Tag:** [vv10]

Bạn thử chuyển sang thang **mA** xem có hiện số không nhé? Nếu vẫn 0.00 thì khả năng cao là cầu chì đồng hồ đã đứt hoặc bo sạc đã ngừng cấp dòng.