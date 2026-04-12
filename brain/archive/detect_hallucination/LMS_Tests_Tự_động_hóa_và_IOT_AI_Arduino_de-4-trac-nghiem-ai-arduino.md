ĐỀ KIỂM TRA TRẮC NGHIỆM - AI Arduino
(Đề 4)
- 30 câu: 12 nhận biết (40%) - 18 thông hiểu (60%)
- Câu trắc nghiệm 1 đáp án: 1 điểm
- Câu trắc nghiệm nhiều đáp án: Số điểm = số đáp án đúng, đúng 1 câu được 1 điểm
- Điểm đạt: 70% điểm tối đa
- Thời lượng: 60ph

Các kiến thức cần đạt | Nhận biết
(12 câu) | Thông hiểu / Vận dụng
(18 câu)
Tổng quan sử dụng Arduino và giao diện phần mềm mBlock5 | 1,2 | 
Cấu tạo và cách sử dụng linh kiện điện tử
- LED đơn
- LED siêu sáng
- Còi Buzzer
- Đèn Laser diode 8cm 3-5V
- Động cơ rung 0834 3-5V
- Mạch thu phát âm thanh ISD1820
- Động cơ Servo
- Breadboard | 3
4
5


6
7
8 | 9

10,11,12
Lập trình điều khiển các linh kiện điện tử
- Event green flag, key pressed, vòng lặp
- Biến số, Repeat Until | 13 | 14,15,16,17
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
Điện áp đầu ra (output) của các cổng Arduino Uno có thể là bao nhiêu?
- A/ 5V
- B/ 4V
- C/ 7V
- D/ Tất cả đáp án đều sai
Câu 3 (Nhận biết)
Phát biểu nào sau đây là đúng khi nói về đèn LED đơn?
![Visual](media/de-4-trac-nghiem-ai-arduino/rId6.png)
- A/ Đèn LED đơn gồm hai cực âm, dương. Chân dài hơn là chân dương.
- B/ Đèn LED đơn gồm hai cực âm, dương. Chân ngắn hơn là cực dương.
- C/ Đèn LED đơn gồm hai cực âm, dương. Chân dài hơn là chân âm.
- D/ Tất cả các câu trên đều sai.
Câu 4 (Nhận biết)
Khối lệnh nào dưới đây dùng để điều khiển đèn led siêu sáng ?
- A/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId7.png)
- B/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId8.png)
- C/
- D/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId9.png)
![Visual](media/de-4-trac-nghiem-ai-arduino/rId10.png)
Câu 5 (Nhận biết)
Khẳng định nào sau đây là SAI?
- A/ Còi buzzer có cấu tạo gồm 2 chân; chân dài là chân âm; chân ngắn là chân dương.
- B/ Còi buzzer có điện áp hoạt động từ 3V đến 5V.
- C/ Còi buzzer là thiết bị output.
- D/ Còi buzzer là một thiết bị có thể phát ra âm thanh, có khả năng tiếp nhận các loại tín hiệu và chuyển chúng thành tín hiệu âm thanh.
Câu 6 (Nhận biết)
Để điều khiển động cơ rung qua mạch Arduino ta cần nối mạch điện như thế nào?
- A/ Dây đỏ của động cơ rung nối với cổng pin digital 2-13; dây đen nối với cổng GND.
- B/ Dây đỏ của động cơ rung nối với cổng GND; dây đen nối với cổng pin digital 2-13.
- C/ Dây đỏ của động cơ rung nối với cổng 3,3V hoặc 5V; dây đen nối với cổng GND.
- D/ Dây đỏ của động cơ rung nối với cổng GND; dây đen nối với cổng 3,3V hoặc 5V.
Câu 7 (Nhận biết)
Phát biểu nào sau đây là đúng khi nói về động cơ Servo?
- A/ Dây màu cam của động cơ Servo được gọi là dây tín hiệu, kết nối với chân Digital 2-13 của Arduino.
- B/ Dây màu đỏ của động cơ Servo được gọi là dây tín hiệu, kết nối với chân Digital 2-13 của Arduino.
- C/ Dây màu cam của động cơ Servo được gọi là dây tín hiệu, chỉ có thể kết nối với chân Digital có dấu (~): 3, 5, 6, 9, 10, 11 của Arduino.
- D/ Dây màu đỏ của động cơ Servo được gọi là dây nguồn, kết nối với chân 5V hoặc GND bất kỳ của Arduino.
Câu 8 (Nhận biết)
Nếu nối nguồn điện 5V vào điểm A thì điểm nào trong 4 điểm B,C,D,E cũng có điện?
![Visual](media/de-4-trac-nghiem-ai-arduino/rId11.png)
- A/ E
- B/ D
- C/ C
- D/ B
Câu 9 (Thông hiểu)
Phân biệt sự khác nhau giữa 2 chân PLAYE và PLAYL trong mạch ISD1820:
- A/ Khi điện áp ở mức cao, PLAYE/PLAYL đều phát nhạc. Tuy nhiên, PLAYE chỉ tắt sau khi phát hết bộ nhớ còn PLAYL tắt khi điện áp ở mức thấp hoặc hết bộ nhớ.
- B/ Khi điện áp ở mức cao, PLAYE phát nhạc còn PLAYL tắt.
- C/ Khi điện áp ở mức cao, PLAYE/PLAYL đều phát nhạc. Nếu điện áp ở mức thấp, âm thanh ngừng phát.
- D/ Khi điện áp ở mức cao, PLAYE/PLAYL đều phát nhạc. Tuy nhiên, PLAYlE chỉ tắt sau khi phát hết bộ nhớ còn PLAYE tắt khi điện áp ở mức thấp hoặc hết bộ nhớ.
Câu 10 (Thông hiểu)
Cho mạch điện Arduino gồm 5 đèn LED như hình sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId12.png)
Một học sinh đã lập trình một chương trình như hình sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId13.png)
Khi chạy chương trình trên, hỏi các đèn LED hoạt động như thế nào?
- A/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId14.gif)
- B/
- C/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId15.gif)
- D/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId16.gif)
![Visual](media/de-4-trac-nghiem-ai-arduino/rId17.gif)
Câu 11 (Thông hiểu)
Cho mạch điện Arduino gồm 4 đèn LED như hình sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId18.png)
Mạch điện gồm 1 breadboard; 4 đèn LED đỏ, vàng, xanh lá, xanh dương như hình trên.
Các cặp đèn LED nào sẽ hoạt động giống nhau khi được lập trình?
- A/ Đỏ - xanh lá, vàng - xanh dương
- B/ Đỏ - xanh dương, vàng - xanh lá
- C/ Đỏ - vàng, xanh lá - xanh dương 
- D/ Đỏ - xanh dương, vàng - xanh lá
Câu 12 (Thông hiểu)
Cho đoạn chương trình như sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId19.png)
Cách mắc mạch điện và kết nối với Arduino nào sau đây giúp điều khiển tắt, mở cả 4 đèn LED cùng lúc bằng hai phím a, b?
- A/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId20.png)
- B/
- C/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId21.png)
- D/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId22.png)
![Visual](media/de-4-trac-nghiem-ai-arduino/rId23.png)
Câu 13 (Nhận biết)
Hãy sắp xếp các hành động sau theo thứ tự phù hợp để sử dụng tạo một biến bất kỳ.
- A/ Đặt tên biến bất kì ở phần New variable name
- B/ Chọn nhóm lệnh Variable
- C/ Click vào OK để hoàn thành việc tạo biến
- D/ Nhấn chọn Make a Variable để tạo biến.
- A/ BDAC
- B/ ABCD
- C/ BCAD
- D/ DABC
Câu 14 (Thông hiểu)
Cho mạch Arduino gồm 4 đèn LED, 1 còi buzzer có hiệu ứng như sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId24.gif)
Hiệu ứng của các linh kiện bắt đầu khi nhấn lá cờ xanh, chương trình lặp lại mãi mãi.
Một học sinh lập trình chương trình của Arduino như sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId25.png)
Hỏi để ra được hiệu ứng các đèn LED và còi Buzzer như hình trên, chỗ trống theo thứ tự số 1, 2 ,3 ,4, 5, 6 nên điền là high hay low?
Số 1: high
Số 2: low
Số 3: low
Số 4: low
Số 5: high
Số 6: high
Câu 15 (Thông hiểu)
Cho mạch điện Arduino với 1 động cơ Servo với yêu cầu sau:
Lập trình hệ thống điều khiển động cơ Servo xoay phải (về góc 0 độ) hoặc xoay trái (về góc 180 độ) bằng phím A và B:
- Khi nhấn phím A, động cơ Servo sẽ xoay chậm rãi từ góc 180 về góc 0 độ.
- Khi nhấn phím B, động cơ Servo sẽ reset, xoay nhanh về lại góc 180 độ.
![Visual](media/de-4-trac-nghiem-ai-arduino/rId26.gif)
Một học sinh đã lập trình như sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId27.png)
Hãy điền vào phần code thiếu để thực hiện yêu cầu trên
- A/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId28.png)
- B/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId29.png)
- C/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId30.png)
- D/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId31.png)
Câu 16 (Thông hiểu)
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
![Visual](media/de-4-trac-nghiem-ai-arduino/rId32.png)
Hỏi đoạn chương trình còn thiếu ở chỗ trống là gì?
- A/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId33.png)
- B/
- C/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId34.png)
- D/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId35.png)
![Visual](media/de-4-trac-nghiem-ai-arduino/rId36.png)
Câu 17 (Thông hiểu)
Một bạn học sinh mắc mạch gồm Arduino, đèn LED và breadboard, quy ước các chân đèn LED được minh họa như hình. 
Với đoạn chương trình của học sinh đã thực hiện dưới đây, khi nhấn lá cờ xanh, những đèn LED nào sẽ phát sáng?
![Visual](media/de-4-trac-nghiem-ai-arduino/rId37.png)
![Visual](media/de-4-trac-nghiem-ai-arduino/rId38.png)
- A/ Chỉ có đèn đỏ sáng.
- B/ Chỉ có đèn xanh lá, xanh dương, xám, vàng sáng; Đèn đỏ không sáng.
- C/ Chỉ có đèn đỏ, xanh lá, xanh dương, xám, sáng; Đèn vàng không sáng.
- D/ Cả 5 đèn đều sáng.
Câu 18 (Thông hiểu)
Cho mạch điện Arduino như hình sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId39.png)
Lập trình chương trình điều khiển mạch trên với hai chức năng chính như sau:
1/ Khi nhấn nút thứ nhất, bật đèn và thu âm trong 10 giây, sau đó đèn tắt
2/ Khi nhấn nút thứ hai, có tiếng còi báo hiệu và phát lại âm thanh đã thu trước đó.
![Visual](media/de-4-trac-nghiem-ai-arduino/rId40.png)
Hãy cho biết đoạn chương trình nào thực hiện việc phát âm thanh đã được ghi âm?
- A/ C
- B/ B
- C/ A
- D/ Các câu trên đều sai.
Câu 19 (Thông hiểu)
Cho mạch Arduino với 1 mạch thu phát âm thanh như sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId41.png)
(Chân REC = D10, P-E = D11)
Lập trình 1 mạch thu phát âm thanh phát có các chức năng sử dụng bằng các nút như sau:
- Khi nhấn Space, mạch ISD1820 sẽ ghi âm giọng nói của người dùng trong 10 giây.
- Khi nhấn phím A, mạch sẽ phát âm thanh được ghi âm rồi tắt.
Đoạn chương trình nào dưới đây giúp mạch Arduino hoạt động đúng như yêu cầu?
- A/ B/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId42.png)
![Visual](media/de-4-trac-nghiem-ai-arduino/rId43.png)
- C/ D/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId44.png)
![Visual](media/de-4-trac-nghiem-ai-arduino/rId45.png)
Câu 20 (Thông hiểu)
Cho mạch Arduino gồm 1 đèn LED như hình sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId46.png)
Cho đoạn chương trình như sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId47.png)
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
Câu 22 (Thông hiểu)
Cho mạch điện Arduino với 1 đèn LED đỏ, 1 đèn led xanh, động cơ rung như hình sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId48.png)
Cho chương trình gồm 3 nhân vật nút nhấn “Button1/2/3”
![Visual](media/de-4-trac-nghiem-ai-arduino/rId49.png)
Hãy lập trình thiết bị Arduino và các nhân vật nút nhấn thỏa các yêu cầu sau:
- Khi nhấn vào nhân vật nút nhấn 1, đèn LED đỏ sẽ sáng, đèn LED xanh và động cơ rung sẽ tắt.
- Khi nhấn vào nhân vật nút nhấn 2, đèn LED xanh sẽ sáng, đèn LED đỏ và động cơ rung sẽ tắt.
- Khi nhấn vào nhân vật nút nhấn 3, động cơ rung sẽ hoạt động, đèn LED đỏ và đèn LED xanh sẽ tắt.
Biết rằng chương trình của Arduino được lập trình như sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId50.png)
Đáp án nào sau đây thể hiện câu lệnh của 3 nhân vật nút nhấn?
- A/          B/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId51.png)
![Visual](media/de-4-trac-nghiem-ai-arduino/rId52.png)
- C/               D/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId53.png)
![Visual](media/de-4-trac-nghiem-ai-arduino/rId54.png)
Câu 23 (Thông hiểu)
Cho mạch điện Arduino với 1 động cơ Servo như hình sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId55.png)
Hệ thống gồm 2 nhân vật nút nhấn “On”, “Off” có chương trình như sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId56.png)
Hãy lập trình hệ thống điều khiển động cơ Servo xoay trái (góc 0 độ) hoặc xoay phải (góc 180 độ) bằng hai nhân vật nút nhấn “On”, “Off” thỏa yêu cầu sau:
- Khi nhấn vào nút nhấn “Off”, động cơ Servo sẽ đứng yên ở vị trí giữa (góc 90 độ).
- Khi nhấn vào nút nhấn “On”, động cơ Servo sẽ tự động xoay trái (góc 0 độ), phải (góc 180 độ) liên tục đến khi nhấn “Off” thì sẽ dừng xoay.
Đáp án nào sau đây thể hiện câu lệnh của Arduino để thực hiện yêu cầu trên?
- A/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId57.png)
- B/
- C/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId58.png)
- D/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId59.png)
![Visual](media/de-4-trac-nghiem-ai-arduino/rId60.png)
Câu 24 (Thông hiểu)
Cho mạch điện Arduino với 1 đèn LED như hình sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId61.png)
Cho chương trình gồm 1 nhân vật đèn “Bulb” có 2 trang phục như hình sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId62.png)
Hãy lập trình thiết bị Arduino và nhân vật đèn thỏa các yêu cầu sau:
- Khi nhấn vào nhân vật, nếu nhân vật đang ở trang phục “off” sẽ đổi thành “on” và ngược lại.
- Khi nhân vật ở trang phục “off", đèn LED trên Arduino sẽ tắt; Khi nhân vật ở trang phục “on”,  đèn LED trên Arduino sẽ mở.
Biết rằng chương trình Arduino được lập trình như sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId63.png)
Chương trình của nhân vật đèn “Bulb” nào dưới đây thực hiện yêu cầu trên?
- A/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId64.png)
- B/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId65.png)
- C/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId66.png)
- D/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId67.png)
Câu 25 (Nhận biết)
Câu lệnh hình sau đây sẽ mang giá trị gì?
![Visual](media/de-4-trac-nghiem-ai-arduino/rId68.png)
- A/ True - False
- B/ Số
- C/ Chuỗi
- D/ Tất cả đều đúng
Câu 26 (Thông hiểu)
Cho mạch điện Arduino với 1 động cơ Servo như hình sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId55.png)
Hãy lập trình hệ thống điều khiển động cơ Servo xoay trái (góc 0 độ) hoặc xoay phải (góc 180 độ) bằng giọng nói với từ khóa “left”/”right”.
- Khi nhấn phím Space, chương trình sẽ hỏi “Servo turn left or right?”
- Khi đó hệ thống sẽ mở lên bảng nhận diện giọng nói và người dùng nói bằng tiếng Anh.
- Nếu trong lời nói chứa từ khóa “left” thì servo sẽ xoay trái (góc 0 độ); Nếu trong lời nói chứa từ khóa “right” thì servo sẽ xoay phải (góc 180 độ).
Biết rằng chương trình của Arduino được lập trình như sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId69.png)
Đáp án nào sau đây thể hiện câu lệnh của nhân vật để thực hiện yêu cầu trên?
- A/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId70.png)
- B/
- C/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId71.png)
- D/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId72.png)
![Visual](media/de-4-trac-nghiem-ai-arduino/rId73.png)
Câu 27 (Thông hiểu)
Cho mạch điện Arduino với 3 đèn LED như hình sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId74.png)
Cho chương trình gồm 1 nhân vật có chương trình như sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId75.png)
Biết rằng chương trình của thiết bị Arduino được lập trình như sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId76.png)
Hỏi khi người dùng nhấn phím Space, sau đó nói “Light number three!”, đèn LED nào trên mạch Arduino sẽ sáng?
- A/ Cả ba đèn LED đều sáng.
- B/ Đèn LED đỏ và xanh dương sáng, đèn LED xanh lá tắt.
- C/ Đèn LED xanh dương sáng, đèn LED đỏ, xanh lá tắt.
- D/ Đèn LED đỏ và xanh lá sáng, đèn LED xanh dương tắt.
Câu 28 (Nhận biết)
Khẳng định nào dưới đây là SAI về Teachable Machine?
- A/ Tiện ích mở rộng Teachable Machine nằm trong phần Extension của thiết bị Device.
- B/ Tiện ích mở rộng Teachable Machine nằm trong phần Extension của nhân vật Sprite.
- C/ Teachable machine không yêu cầu đăng nhập tài khoản mBlock và không cần sử dụng Wifi.
- D/ Teachable Machine là một tính năng cho phép người dùng dễ dàng tạo ra các mô hình máy học (Machine learning) và huấn luyện chúng thông qua dữ liệu mà bạn cung cấp, và sau đó sử dụng mô hình đó để phân loại và nhận diện các đối tượng thực tế.
Câu 29 (Thông hiểu)
Cho mạch điện Arduino với 1 đèn LED như hình sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId61.png)
Hãy lập trình một chương trình cửa nhận diện được một người có phải là chủ nhà hay không?
- Hãy dùng công cụ Teachable Machine và dùng hình ảnh thực tế để dạy máy tính phân biệt 2 trường hợp và đặt tên như sau: 
	1/ Chủ nhà (owner)
	2/ Người lạ (stranger)
Hỏi với chương trình của nhân vật và Arduino được thực hiện như dưới đây thì thiết bị hoạt động như thế nào?

Nhân vật | Arduino
 | 

- A/ Khi nhấn lá cờ xanh, chương trình sẽ mở bảng nhận diện khuôn mặt. Nếu nhận diện được chủ nhà, đèn LED sẽ sáng. Ngược lại nếu nhận diện người lạ, đèn LED sẽ tắt. Chương trình lặp lại mãi mãi.
- B/ Khi nhấn lá cờ xanh, chương trình sẽ mở bảng nhận diện khuôn mặt. Nếu nhận diện được người lạ, đèn LED sẽ tắt. Ngược lại nếu nhận diện chủ nhà, đèn LED sẽ sáng. Chương trình lặp lại mãi mãi.
- C/ Khi nhấn lá cờ xanh, chương trình sẽ mở bảng nhận diện khuôn mặt. Nếu nhận diện được người lạ, đèn LED sẽ nhấp nháy liên tục. Ngược lại nếu nhận diện chủ nhà, đèn LED sẽ tắt. Chương trình lặp lại mãi mãi.
- D/ Khi nhấn lá cờ xanh, chương trình sẽ mở bảng nhận diện khuôn mặt. Nếu nhận diện được người lạ, đèn LED sẽ tắt. Ngược lại nếu nhận diện chủ nhà, đèn LED sẽ nhấp nháy liên tục. Chương trình lặp lại mãi mãi.
Câu 30 (Thông hiểu)
Cho mạch điện Arduino với 3 đèn LED như hình sau:
![Visual](media/de-4-trac-nghiem-ai-arduino/rId74.png)
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
![Visual](media/de-4-trac-nghiem-ai-arduino/rId79.png)
Đáp án nào sau đây thể hiện câu lệnh của phần nhân vật để thực hiện yêu cầu trên?
- A/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId80.png)
- B/
- C/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId81.png)
- D/
![Visual](media/de-4-trac-nghiem-ai-arduino/rId82.png)
![Visual](media/de-4-trac-nghiem-ai-arduino/rId83.png)