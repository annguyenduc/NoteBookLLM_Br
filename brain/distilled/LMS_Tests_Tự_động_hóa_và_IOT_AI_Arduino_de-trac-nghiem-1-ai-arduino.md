Chế độ Live chỉ hoạt động trong quá trình mở mBlock5 và kết nối với board Arduino.ĐỀ KIỂM TRA TRẮC NGHIỆM - AI Arduino
(Đề 1)
- 30 câu: 12 nhận biết (40%) - 18 thông hiểu (60%)
- Câu trắc nghiệm 1 đáp án: 1 điểm
- Câu trắc nghiệm nhiều đáp án: Số điểm = số đáp án đúng, đúng 1 câu được 1 điểm
- Điểm đạt: 70% điểm tối đa
- Thời lượng: 60ph

Các kiến thức cần đạt | Nhận biết
(12 câu) | Thông hiểu / Vận dụng
(18 câu)
Tổng quan sử dụng Arduino và giao diện phần mềm mBlock5 | 1,2,3 | 
Cấu tạo và cách sử dụng linh kiện điện tử
- LED đơn
- LED siêu sáng
- Còi Buzzer
- Đèn Laser diode 8cm 3-5V
- Động cơ rung 0834 3-5V
- Mạch thu phát âm thanh ISD1820
- Động cơ Servo
- Breadboard | 4


5
6,7
8
9 | 10

11,12,13
Lập trình điều khiển các linh kiện điện tử
- Event green flag, key pressed, vòng lặp
- Biến số, Repeat Until |  | 14,15,16,17
18,19,20
Lập trình điều khiển các nhân vật truyền tín hiệu qua lại với linh kiện điện tử
- Sử dụng sự kiện khi nhấn nút bàn phím
- Broadcast-Receive message | 21 | 22,23,24
Lập trình nhận diện giọng nói bằng extension Cognitive Services | 25 | 26,27
Lập trình nhận diện hình ảnh bằng extension Teachable Machine | 28 | 29,30

Câu 1 (Nhận biết)
Ta có thể thực hiện cách nào sau đây để kết nối Arduino với máy tính?
- A/ Kết nối bằng dây cáp kết nối. Cổng dùng để kết nối với máy tính là cổng USB - A type. Cổng dùng để kết nối với Arduino là cổng USB - B type.
- B/ Kết nối bằng dây cáp kết nối. Cổng dùng để kết nối với máy tính là cổng USB - B type. Cổng dùng để kết nối với Arduino là cổng USB - C type.
- C/ Kết nối bằng Bluetooth.
- D/ Kết nối bằng dây điện jumper male-male.
Câu 2 (Nhận biết)
Phát biểu nào sau đây là đúng khi nói về chế độ Live và chế độ Upload khi lập trình Arduino trên mBlock5?
- A/ Chế độ Live chỉ hoạt động trong quá trình mở mBlock5 và kết nối với board Arduino.
- B/ Sau khi tải chương trình từ máy tính sang Arduino bằng chế độ Upload, nếu ta ngắt kết nối giữa hai thiết bị, chương trình được tải lên sẽ bị xóa khỏi bộ nhớ của Arduino.
- C/ Sau khi tải chương trình từ máy tính sang Arduino bằng chế độ Upload, nếu ta xóa câu lệnh ở khu vực lập trình, chương trình hoạt động của Arduino sẽ bị thay đổi ngay lập tức.
- D/ Với chế độ Live, ta có thể thấy trực tiếp chương trình đang chạy đến khối lệnh nào khi chọn “Setting - Update firmware - OK”.
Câu 3 (Nhận biết)
Khối lệnh nào sau đây không thể sử dụng được trong việc lập trình Arduino bằng chế độ Live?
- A/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId7.png)
- B/
- C/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId8.png)
- D/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId9.png)
![Visual](media/de-trac-nghiem-1-ai-arduino/rId10.png)
Câu 4 (Nhận biết)
Ta có thể phân biệt được chân dương, chân âm của đèn LED siêu sáng bằng cách nào?
- A/ Phần chân âm của đèn LED siêu sáng được đánh dấu bằng một lỗ nhỏ, chân dương không có.
- B/ Phần chân âm của đèn LED siêu sáng dài hơn chân dương.
- C/ Phần chân dương của đèn LED siêu sáng có màu sáng hơn chân âm.
- D/ Phần chân dương của đèn LED siêu sáng được đánh dấu bằng một lỗ nhỏ, chân âm không có.
Câu 5 (Nhận biết)
Khối lệnh nào sau đây được sử dụng để điều khiển việc hoạt động/tắt của động cơ rung 0834 3-5V?
- A/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId11.png)
- B/
- C/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId12.png)
- D/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId13.png)
![Visual](media/de-trac-nghiem-1-ai-arduino/rId14.png)
Câu 6 (Nhận biết)
Phát biểu nào sau đây là đúng nói về các chân kết nối của mạch thu phát âm thanh ISD1820?
- A/ Chân REC của mạch được gắn với cổng Digital 2-13 của Arduino.
- B/ Chân VCC của mạch được gắn với cổng GND của Arduino.
- C/ Chân GND của mạch được gắn với cổng 5V của Arduino.
- D/ Chân PLAYE, PLAYL của mạch chỉ có thể được gắn ở một số chân Digital không có dấu ngã (~): 2, 4, 7, 8, 12, 13.
Câu 7 (Nhận biết)
Phát biểu nào sau đây là đúng khi nói về chức năng PLAYE và PLAYL của mạch thu phát âm thanh ISD1820?
- A/ Cả 3 đáp án còn lại đều đúng.
- B/ Khi nhấn và giữ nút nhấn, điện áp ở chân kết nối đang ở mức cao. Khi không nhấn nút, điện áp ở chân kết nối ở mức thấp. 
- C/ Chức năng PLAYE sẽ phát đoạn âm thanh được ghi lại. Âm thanh phát ra đến khi ngắt nguồn hoặc thả nút nhấn thì tắt ngay lập tức.
- D/ Chức năng PLAYE sẽ phát đoạn âm thanh được ghi lại. Âm thanh phát ra đầy đủ và tự tắt khi kết thúc. Ngay cả khi ngắt điện áp trong lúc phát, đoạn âm thanh vẫn sẽ tiếp tục chạy đến khi kết thúc.
Câu 8 (Nhận biết)
Phát biểu nào sau đây là đúng khi nói về động cơ Servo?
- A/ Dây màu cam của động cơ Servo được gọi là dây tín hiệu, kết nối với chân Digital 2-13 của Arduino.
- B/ Dây màu đỏ của động cơ Servo được gọi là dây tín hiệu, kết nối với chân Digital 2-13 của Arduino.
- C/ Dây màu cam của động cơ Servo được gọi là dây tín hiệu, chỉ có thể kết nối với chân Digital có dấu (~): 3, 5, 6, 9, 10, 11 của Arduino.
- D/ Dây màu đỏ của động cơ Servo được gọi là dây nguồn, kết nối với chân 5V hoặc GND bất kỳ của Arduino.
Câu 9 (Nhận biết)
Phát biểu nào sau đây là đúng khi nói về cách kết nối các lỗ trên Breadboard?
![Visual](media/de-trac-nghiem-1-ai-arduino/rId15.png)
- A/ Các lỗ ở khu vực B hoặc C được kết nối theo hàng dọc, mỗi cột 5 lỗ được kết nối với nhau.
- B/ Các lỗ ở khu vực A hoặc D được kết nối theo hàng dọc, mỗi cột 2 lỗ được kết nối với nhau.
- C/ Các lỗ ở khu vực B hoặc C được kết nối theo hàng ngang, mỗi hàng 30 lỗ được kết nối với nhau.
- D/ Tất cả các lỗ ở khu vực B hoặc C được kết nối với nhau theo hàng ngang và hàng dọc, tất cả các lỗ trong khu B hoặc C đều có chức năng giống nhau.
Câu 10 (Thông hiểu)
Để kết nối mạch thu phát âm thanh ISD1820 với Arduino, cách kết nối nào sau đây là đúng?
- A/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId16.png)
- B/
- C/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId17.png)
- D/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId18.png)
![Visual](media/de-trac-nghiem-1-ai-arduino/rId19.png)
Câu 11 (Thông hiểu)
Cho đoạn chương trình như sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId20.png)
Cách mắc mạch điện và kết nối với Arduino nào sau đây giúp điều khiển tắt, mở cả 4 đèn LED cùng lúc bằng hai phím a, b?
- A/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId21.png)
- B/
- C/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId22.png)
- D/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId23.png)
![Visual](media/de-trac-nghiem-1-ai-arduino/rId24.png)
Câu 12 (Thông hiểu)
Một mạch Arduino gồm 2 đèn LED đỏ và xanh, 1 động cơ servo, 1 mạch thu phát âm thanh ISD1820. Cho sơ đồ mạch điện như sau, hỏi thiết bị nào sẽ KHÔNG hoạt động khi thực hiện lập trình?
![Visual](media/de-trac-nghiem-1-ai-arduino/rId25.png)
- A/ 2 đèn LED xanh, đỏ
- B/ Động cơ Servo
- C/ Mạch thu phát âm thanh ISD1820
- D/ Động cơ Servo và mạch thu phát âm thanh ISD1820
(CŨ) Câu 13 (Thông hiểu)
Cho mạch Arduino gồm các linh kiện điện tử như sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId26.png)
Phát biểu nào sau đây là đúng khi nói về các linh kiện điện tử của mạch điện trên?
(Nhiều đáp án)
- A/ Khi sử dụng chức năng ghi âm của mạch ISD1820, đèn LED xanh lá sẽ sáng.
- B/ Còi Buzzer không thể hoạt động được.
- C/ Chân REC của mạch ISD1820 được nối với chân Digital 10 của Arduino.
- D/ Khi sử dụng chức năng ghi âm của mạch ISD1820, đèn LED đỏ sẽ sáng.
E/ Khi đèn LED xanh lá sáng, còi Buzzer sẽ kêu.
F/ Khi sử dụng chức năng PLAYE của mạch ISD1820, đèn LED xanh dương sẽ sáng.
(*Mới) Câu 13 (Thông hiểu)
Cho mạch Arduino gồm các linh kiện điện tử như sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId27.png)
Hãy ghép chân của các linh kiện điện tử đã kết nối trên Arduino?
(Dạng ghép nối)
Đáp án

Chân dương (+) LED đỏ | D5
Chân dương (+) LED xanh lá | D10
Chân dương (+) LED xanh dương | D6
Chân dương (+) còi Buzzer | D12
Chân PL mạch thu phát âm thanh | D5
Chân PE mạch thu phát âm thanh | D6
Chân REC mạch thu phát âm thanh | D10

Câu 14 (Thông hiểu)
Một bạn học sinh mắc mạch gồm Arduino, đèn Led và breadboard, quy ước các chân đèn Led được minh họa như hình. Hỏi khi bạn thực hiện chương trình sau thì có những đèn nào phát sáng?
![Visual](media/de-trac-nghiem-1-ai-arduino/rId28.png)
Đây là đoạn chương trình của học sinh đã thực hiện. Hỏi khi nhấn lá cờ xanh, những đèn LED nào sẽ phát sáng?
![Visual](media/de-trac-nghiem-1-ai-arduino/rId29.png)
![Visual](media/de-trac-nghiem-1-ai-arduino/rId30.png)
- A/ Chỉ có đèn xanh dương sáng.
- B/ Chỉ có đèn xanh lá, xanh dương, xám, vàng sáng; Đèn đỏ không sáng.
- C/ Chỉ có đèn đỏ, xanh lá, xanh dương, xám, sáng; Đèn vàng không sáng.
- D/ Cả 5 đèn đều sáng.
Câu 15 (Thông hiểu)
Cho một hệ thống có yêu cầu như sau:
- Mạch Arduino gồm 3 đèn LED.
- Khi nhấn lá cờ, 3 đèn LED sáng-tắt luân phiên, lặp lại mãi mãi như hình sau:
Một học sinh lập trình chương trình của Arduino như sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId31.gif)
![Visual](media/de-trac-nghiem-1-ai-arduino/rId32.png)
Hỏi giá trị của biến số X, Y lần lượt là bao nhiêu để ra được hiệu ứng 3 đèn luân phiên đúng thứ tự như hình trên?
- A/ X = 10, Y = 11
- B/ X = 11, Y = 10
- C/ X = 12, Y = 11
- D/ Tất cả đáp án đều sai.
Câu 16 (Thông hiểu)
Cho mạch Arduino gồm 4 đèn LED, 1 còi buzzer có hiệu ứng như sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId33.gif)
Hiệu ứng của các linh kiện bắt đầu khi nhấn lá cờ xanh, chương trình lặp lại mãi mãi.
Một học sinh lập trình chương trình của Arduino như sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId34.png)
Hỏi để ra được hiệu ứng các đèn LED và còi Buzzer như hình trên, chỗ trống theo thứ tự số 1, 2 ,3 ,4, 5, 6 nên điền là high hay low?
Số 1: high
Số 2: low
Số 3: low
Số 4: low
Số 5: high
Số 6: high
- A/ 1:high, 2:low, 3:low, 4:low, 5:high, 6:high
- B/ 1:low, 2:low, 3:low, 4:high, 5:high, 6:high
- C/ 1:low, 2:high, 3:high, 4:high, 5:low, 6:low
- D/ 1:high, 2:high, 3:low, 4:low, 5:low, 6:high
Câu 17 (Thông hiểu)
Cho một hệ thống có yêu cầu như sau:
- Mạch Arduino gồm 2 đèn LED đỏ và xanh, 1 động cơ servo, 1 mạch thu phát âm thanh ISD1820.
- Khi nhấn lá cờ, cả 2 đèn LED đều tắt và servo xoay ở góc 90 độ.
- Khi nhấn nút mũi tên trái, đèn LED đỏ sáng, LED xanh tắt, động cơ servo gạt tay sang trái (giả sử servo gạt sang trái ở góc 0 độ) và mạch ISD1820 sẽ bắt đầu quá trình ghi âm trong 10 giây.
- Sau 10 giây ghi âm, các thiết bị sẽ tự động quay về trạng thái ban đầu giống như khi nhấn lá cờ xanh.
- Khi nhấn nút mũi tên phải, đèn LED xanh sáng, LED đỏ tắt, động cơ servo gạt tay sang phải (giả sử servo gạt sang trái ở góc 180 độ) và mạch ISD1820 sẽ phát ra âm thanh được ghi.
- Sau khi phát âm thanh được ghi, các thiết bị sẽ tự động quay về trạng thái ban đầu giống như khi nhấn lá cờ xanh.
Cho bảng kết nối các linh kiện điện tử với chân Digital trên Arduino như sau:

Linh kiện điện tử | Chân kết nối của linh kiện | Chân Digital trên Arduino
LED đỏ | Chân dương | Digital 13
LED xanh | Chân dương | Digital 12
Động cơ Servo | Dây tín hiệu (Cam) | Digital 11
Mạch thu phát âm thanh ISD1820 | Chân PLAYL | Digital 6
Mạch thu phát âm thanh ISD1820 | Chân PLAYE | Digital 5
Mạch thu phát âm thanh ISD1820 | Chân REC | Digital 4

Một học sinh lập trình chương trình của Arduino như sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId35.png)
Hỏi đoạn chương trình còn thiếu ở chỗ trống là gì?
- A/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId36.png)
- B/
- C/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId37.png)
- D/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId38.png)
![Visual](media/de-trac-nghiem-1-ai-arduino/rId39.png)
Câu 18 (Thông hiểu)
Hãy lựa chọn chương trình phù hợp để điều khiển mạch Arduino và 4 đèn LED sáng luân phiên, lặp lại mãi mãi khi nhấn lá cờ.
![Visual](media/de-trac-nghiem-1-ai-arduino/rId40.gif)
- A/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId41.png)
- B/
- C/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId42.png)
- D/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId43.png)
![Visual](media/de-trac-nghiem-1-ai-arduino/rId44.png)
Câu 19 (Thông hiểu)
Cho mạch điện Arduino gồm 5 đèn LED như hình sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId45.png)
Một học sinh đã lập trình một chương trình như hình sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId46.png)
Khi chạy chương trình trên, hỏi các đèn LED hoạt động như thế nào?
- A/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId47.gif)
- B/
- C/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId48.gif)
- D/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId49.gif)
![Visual](media/de-trac-nghiem-1-ai-arduino/rId50.gif)
Câu 20 (Thông hiểu)
Cho mạch Arduino gồm 1 đèn LED như hình sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId51.png)
Cho đoạn chương trình như sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId52.png)
Hỏi khi nhấn phím a, sau đó 10 giây thì nhấn phím b, đèn LED sẽ hoạt động như thế nào?
- A/ Khi nhấn phím a, đèn LED chớp tắt liên tục mỗi 0,5 giây. Khi nhấn phím b, đèn LED tắt trong thời gian ngắn, sau đó tiếp tục chớp tắt liên tục.
- B/ Khi nhấn phím a, đèn LED chớp tắt liên tục mỗi 0,5 giây. Khi nhấn phím b, đèn LED tắt hẳn.
- C/ Khi nhấn phím a, đèn LED tắt. Khi nhấn phím b, đèn LED sáng lên.
- D/ Khi nhấn phím a, đèn LED sáng. Khi nhấn phím b, đèn LED tắt đi.
Câu 21 (Nhận biết)
Phát biểu nào sau đây là đúng khi nói về khối lệnh “Broadcast” và “When I receive message”?
- A/ Việc truyền và nhận tin nhắn khi lập trình Arduino chỉ có thể sử dụng khi dùng chế độ LIVE.
- B/ Việc truyền và nhận tin nhắn chỉ có thể sử dụng khi lập trình các nhân vật.
- C/ Arduino chỉ có thể nhận tin nhắn từ nhân vật, chứ không thể gửi tin nhắn đến nhân vật.
- D/ Mỗi nhân vật, thiết bị chỉ có thể truyền, nhận 1 tin nhắn khi lập trình.
Câu 22 (Thông hiểu)...
Cho mạch điện Arduino với đèn LED, động cơ rung, đèn laser như hình sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId53.png)
Cho chương trình gồm 3 nhân vật nút nhấn “Button1/2/3”
![Visual](media/de-trac-nghiem-1-ai-arduino/rId54.png)
Hãy lập trình thiết bị Arduino và các nhân vật nút nhấn thỏa các yêu cầu sau:
- Khi nhấn vào nhân vật nút nhấn 1, đèn LED sẽ sáng, đèn Laser và động cơ rung sẽ tắt.
- Khi nhấn vào nhân vật nút nhấn 2, đèn Laser sẽ chiếu sáng, đèn LED và động cơ rung sẽ tắt.
- Khi nhấn vào nhân vật nút nhấn 3, động cơ rung sẽ hoạt động, đèn LED và đèn Laser sẽ tắt.
Biết rằng chương trình của Arduino được lập trình như sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId55.png)
Đáp án nào sau đây thể hiện câu lệnh của 3 nhân vật nút nhấn?
- A/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId56.png)
- B/
- C/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId57.png)
- D/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId58.png)
![Visual](media/de-trac-nghiem-1-ai-arduino/rId59.png)
Câu 23 (Thông hiểu)
Cho mạch điện Arduino với 1 đèn LED như hình sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId51.png)
Cho chương trình gồm 1 nhân vật đèn “Bulb” có 2 trang phục như hình sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId60.png)
Hãy lập trình thiết bị Arduino và nhân vật đèn thỏa các yêu cầu sau:
- Khi nhấn vào nhân vật, nếu nhân vật đang ở trang phục “off” sẽ đổi thành “on” và ngược lại.
- Khi nhân vật ở trang phục “off", đèn LED trên Arduino sẽ tắt; Khi nhân vật ở trang phục “on”,  đèn LED trên Arduino sẽ mở.
Biết rằng chương trình của nhân vật đèn “Bulb” được lập trình như sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId61.png)
Đáp án nào sau đây thể hiện câu lệnh của Arduino để thực hiện yêu cầu trên?
- A/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId62.png)
- B/
- C/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId63.png)
- D/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId64.png)
![Visual](media/de-trac-nghiem-1-ai-arduino/rId65.png)
Câu 24 (Thông hiểu)
Cho mạch điện Arduino với 1 động cơ Servo như hình sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId66.png)
Hệ thống gồm 2 nhân vật nút nhấn “On”, “Off” có chương trình như sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId67.png)
Hãy lập trình hệ thống điều khiển động cơ Servo xoay trái (góc 0 độ) hoặc xoay phải (góc 180 độ) bằng hai nhân vật nút nhấn “On”, “Off” thỏa yêu cầu sau:
- Khi nhấn vào nút nhấn “Off”, động cơ Servo sẽ đứng yên ở vị trí giữa (góc 90 độ).
- Khi nhấn vào nút nhấn “On”, động cơ Servo sẽ tự động xoay trái (góc 0 độ), phải (góc 180 độ) liên tục đến khi nhấn “Off” thì sẽ dừng xoay.
Đáp án nào sau đây thể hiện câu lệnh của Arduino để thực hiện yêu cầu trên?
- A/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId68.png)
- B/
- C/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId69.png)
- D/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId70.png)
![Visual](media/de-trac-nghiem-1-ai-arduino/rId71.png)
Câu 25 (Nhận biết)
Phát biểu nào sau đây là đúng khi nói về extension “Cognitive Services”?
- A/ Các câu lệnh "Recognize" dùng để hiện lên khung nhận diện (Camera thu hình ảnh và Voice Record để thu âm thanh), có giới hạn số lần sử dụng trong một ngày.
- B/ Để sử dụng nhóm lệnh trên, ta lần lượt thực hiện các thao tác sau: Chọn phần lập trình thiết bị (Devices) > Thêm thiết bị Arduino > Chọn mục Extension > Tìm và chọn nhóm lệnh “Cognitive Services”.
- C/ Các câu lệnh “Recognize” luôn đi kèm với các câu lệnh khác cho ra kết quả nhận diện. Khối lệnh đó luôn cho ra kết quả là một chuỗi ký tự.
- D/ Vì các câu lệnh thực thi “Recognize” luôn mở bảng nhận diện giống nhau nên ta chỉ cần sử dụng 1 câu lệnh cho mọi trường hợp nhận diện, chỉ cần đổi các câu lệnh result cho phù hợp.
Câu 26 (Thông hiểu)
Cho mạch điện Arduino với 1 động cơ Servo như hình sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId66.png)
Hãy lập trình hệ thống điều khiển động cơ Servo xoay trái (góc 0 độ) hoặc xoay phải (góc 180 độ) bằng giọng nói với từ khóa “left”/”right”.
- Khi nhấn phím Space, chương trình sẽ hỏi “Servo turn left or right?”
- Khi đó hệ thống sẽ mở lên bảng nhận diện giọng nói và người dùng nói bằng tiếng Anh.
- Nếu trong lời nói chứa từ khóa “left” thì servo sẽ xoay trái (góc 0 độ); Nếu trong lời nói chứa từ khóa “right” thì servo sẽ xoay phải (góc 180 độ).
Biết rằng chương trình của Arduino được lập trình như sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId72.png)
Đáp án nào sau đây thể hiện câu lệnh của nhân vật để thực hiện yêu cầu trên?
- A/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId73.png)
- B/
- C/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId74.png)
- D/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId75.png)
![Visual](media/de-trac-nghiem-1-ai-arduino/rId76.png)
Câu 27 (Thông hiểu)
Cho mạch điện Arduino với 3 đèn LED như hình sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId77.png)
Cho chương trình gồm 1 nhân vật có chương trình như sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId78.png)
Biết rằng chương trình của thiết bị Arduino được lập trình như sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId79.png)
Hỏi khi người dùng nhấn phím Space, sau đó nói “Light number two!”, đèn LED nào trên mạch Arduino sẽ sáng?
- A/ Đèn LED đỏ và xanh lá sáng, đèn LED xanh dương tắt.
- B/ Đèn LED đỏ và xanh dương sáng, đèn LED xanh lá tắt.
- C/ Đèn LED xanh dương sáng, đèn LED đỏ, xanh lá tắt.
- D/ Cả ba đèn LED đều sáng.
Câu 28 (Nhận biết)
Hãy sắp xếp các hành động sau theo thứ tự phù hợp để sử dụng Teachable Machine dạy máy tính về (hình ảnh) một sự vật bất kỳ.
- A/ Chọn “Use the model” để sử dụng mẫu các sự vật và quay lại màn hình lập trình.
- B/ Chọn “Build ở new model” và nhập số lượng sự vật dạy cho máy tính.
- C/ Cung cấp hình ảnh từ nhiều góc độ khác nhau về các nhóm sự vật được dạy.
- D/ Ở phần lập trình nhân vật, chọn extension và thêm tiện ích mở rộng “Teachable Machine”.
E/ Trong nhóm lệnh Teachable Machine, chọn “Training model”.
F/ Ở từng nhóm sự vật, đặt tên và nhấn “Learn” để bắt đầu dạy cho máy tính.
- A/ D-E-B-C-F-A
- B/ E-D-B-C-F-A
- C/ D-A-C-F-B-E
- D/ D-A-B-C-F-E
Câu 29 (Thông hiểu)
Cho mạch điện Arduino với 1 đèn LED như hình sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId51.png)
Hãy lập trình một chương trình có thể nhận diện được một người có đang đeo khẩu trang hay không:
- Hãy dùng công cụ Teachable Machine và dùng hình ảnh thực tế để dạy máy tính phân biệt 3 trường hợp và đặt tên như sau: 
	1/ Người đang đeo khẩu trang (mask)
	2/ Người không đeo khẩu trang (nomask)
	3/ Các trường hợp khác (empty)
- Khi nhấn lá cờ xanh, chương trình sẽ mở bảng nhận diện khuôn mặt.
- Nếu nhận diện được người đang đeo khẩu trang, đèn LED sẽ sáng. Ngược lại nếu nhận diện người đang không đeo khẩu trang, đèn LED sẽ tắt.
- Chương trình lặp lại mãi mãi.
Đáp án nào sau đây thể hiện câu lệnh của Arduino và phần nhân vật để thực hiện yêu cầu trên?
- A/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId80.png)
- B/
- C/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId81.png)
- D/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId82.png)
![Visual](media/de-trac-nghiem-1-ai-arduino/rId83.png)
Câu 30 (Thông hiểu)
Cho mạch điện Arduino với 3 đèn LED như hình sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId77.png)
Hãy lập trình một chương trình có thể nhận diện 3 màu sắc đỏ, xanh dương, xanh lá. Từ đó khi người dùng sử dụng giấy màu đặt trước camera nhận diện, đèn LED trên mạch điện sẽ sáng màu tương ứng:
- Hãy dùng công cụ Teachable Machine và dùng hình ảnh thực tế để dạy máy tính phân biệt 3 trường hợp và đặt tên như sau: 
	1/ Giấy A4 màu đỏ (red)
	2/ Giấy A4 màu xanh lá (green)
	3/ Giấy A4 màu xanh dương (blue)
	4/ Trường hợp khác (empty)
- Khi nhấn lá cờ xanh, chương trình sẽ mở bảng nhận diện.
- Nếu camera nhận diện được giấy màu đỏ/xanh lá/xanh dương, thì đèn LED đỏ/xanh lá/xanh dương trên mạch Arduino sẽ sáng.
- Khi 1 đèn LED sáng, 2 đèn còn lại sẽ tắt.
- Chương trình lặp lại mãi mãi.
Biết rằng chương trình của thiết bị Arduino được lập trình như sau:
![Visual](media/de-trac-nghiem-1-ai-arduino/rId84.png)
Đáp án nào sau đây thể hiện câu lệnh của phần nhân vật để thực hiện yêu cầu trên?
- A/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId85.png)
- B/
- C/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId86.png)
- D/
![Visual](media/de-trac-nghiem-1-ai-arduino/rId87.png)
![Visual](media/de-trac-nghiem-1-ai-arduino/rId88.png)