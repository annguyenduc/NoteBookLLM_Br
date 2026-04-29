---
ID: CONCEPT_VIZ_Eliminating_Clutter
Type: Concept
Topic: Data Visualization
Status: verified
Created: 2026-04-29
Tags: [Gestalt, Cognitive_Load, Design_Principles, Clutter]
---

# Loại bỏ Rác nhiễu (Eliminating Clutter)

> "Rác nhiễu là kẻ thù của sự rõ ràng." Mỗi yếu tố bạn thêm vào trang/màn hình đều chiếm **tải nhận thức** của khán giả. Nếu một yếu tố không đóng góp giá trị thông tin, nó cần bị loại bỏ.

## 1. Tải nhận thức (Cognitive Load)
Tải nhận thức là nỗ lực tinh thần cần thiết để xử lý thông tin mới.
- **Tải nhận thức ngoại lai (Extraneous Cognitive Load):** Việc xử lý các yếu tố chiếm dụng tài nguyên trí não nhưng không giúp khán giả hiểu thông tin. Đây là thứ chúng ta cần tránh.
- **Tỷ lệ Tín hiệu trên Nhiễu (Signal-to-Noise Ratio):** 
    - **Tín hiệu (Signal):** Thông tin quan trọng muốn truyền tải.
    - **Nhiễu (Noise):** Các yếu tố gây xao nhãng, không thêm giá trị.
    - *Mục tiêu:* Tối đa hóa tín hiệu, tối thiểu hóa nhiễu.

## 2. Các nguyên tắc Gestalt về Tri giác Thị giác
Giúp hiểu cách con người nhìn nhận trật tự để xác định các yếu tố thừa:

| Nguyên tắc | Mô tả | Ứng dụng |
|:---|:---|:---|
| **Tiệm cận (Proximity)** | Các vật ở gần nhau được coi là cùng nhóm. | Dùng khoảng cách thay vì đường kẻ để nhóm dữ liệu trong bảng. |
| **Tương đồng (Similarity)** | Các vật giống nhau về màu sắc, hình dạng, kích thước được coi là cùng nhóm. | Dùng màu sắc đồng nhất để chỉ dẫn mắt đọc theo hàng/cột. |
| **Bao quanh (Enclosure)** | Các vật nằm trong một vùng bao quanh được coi là cùng nhóm. | Dùng mảng màu nền nhẹ để phân biệt dữ liệu dự báo (forecast) với thực tế. |
| **Đóng kín (Closure)** | Con người có xu hướng nhìn các cấu trúc mở như một thực thể đóng hoàn chỉnh. | Loại bỏ khung viền biểu đồ và màu nền; mắt vẫn sẽ thấy biểu đồ là một khối. |
| **Liên tục (Continuity)** | Mắt người đi theo con đường mượt mà nhất. | Loại bỏ trục Y; mắt vẫn thấy các thanh biểu đồ thẳng hàng nhờ khoảng trắng nhất quán. |
| **Kết nối (Connection)** | Các vật được kết nối vật lý được coi là cùng nhóm mạnh hơn cả sự tương đồng. | Dùng đường kẻ nối các điểm trong biểu đồ đường (line graph). |

## 3. Trật tự Thị giác & Căn lề
- **Căn lề (Alignment):** 
    - Tránh căn giữa (center-aligned) vì nó tạo ra các đường lề nham nhở.
    - Ưu tiên căn lề trái (left-justified) để tạo ra "đường thẳng thị giác" sạch sẽ.
    - Căn lề các văn bản bổ trợ (tiêu đề, chú giải) ở góc trên bên trái để khán giả biết cách đọc trước khi tiếp cận dữ liệu.
- **Văn bản chéo (Diagonal elements):** Tuyệt đối tránh. Chữ nghiêng 45 độ làm tốc độ đọc chậm hơn 52%, nghiêng 90 độ chậm hơn 205%.

## 4. Khoảng trắng (White Space)
Khoảng trắng trong giao tiếp thị giác quan trọng như những khoảng nghỉ trong diễn thuyết.
- Đừng sợ khoảng trắng. Đừng cố lấp đầy không gian trống bằng dữ liệu không cần thiết.
- Sử dụng khoảng trắng một cách chiến lược để làm nổi bật các phần quan trọng nhất.

## 5. Sử dụng Tương phản Chiến lược
- Contrast là tín hiệu giúp khán giả biết nên tập trung vào đâu.
- **Quy luật Con diều hâu:** Dễ dàng phát hiện một con diều hâu giữa đàn bồ câu, nhưng nếu quá nhiều loại chim khác nhau, con diều hâu sẽ bị lu mờ.
- Nếu mọi thứ đều nổi bật, thì không có gì nổi bật cả.

## 6. Ví dụ Dọn dẹp (Decluttering) từng bước
1. **Loại bỏ viền biểu đồ (Chart border):** Không cần thiết (Gestalt Closure).
2. **Loại bỏ đường lưới (Gridlines):** Làm mờ hoặc loại bỏ để dữ liệu nổi bật hơn.
3. **Loại bỏ đánh dấu dữ liệu (Data markers):** Trong biểu đồ đường, chỉ dùng nếu cần nhấn mạnh điểm cụ thể.
4. **Dọn dẹp nhãn trục (Clean up axis labels):** Loại bỏ các số thập phân thừa, rút gọn đơn vị.
5. **Dán nhãn trực tiếp (Label data directly):** Thay vì dùng chú giải (legend) rời rạc (giảm tải nhận thức do mắt phải đảo qua lại).
6. **Nhất quán màu sắc (Leverage consistent color):** Dùng màu sắc để kết nối nhãn với dữ liệu.

## 7. Ví dụ đối chiếu (Rule 17: Double Examples)

### 7.1. Ví dụ từ sách (Original)
*Tình huống: Nguyên tắc Tiệm cận (Proximity) trong bảng số liệu tài chính.*
- **Cách giải quyết:** Khi trình bày một bảng báo cáo tài chính chằng chịt các đường viền sọc dọc ngang (gridlines). Tác giả khuyên nên xóa bỏ tất cả các đường viền dọc, chỉ để lại khoảng trắng đủ rộng giữa các cột. Theo nguyên tắc Proximity, mắt người vẫn sẽ tự động gộp các con số nằm sát nhau thành một nhóm cột mà không cần bất kỳ đường kẻ nào, giúp giảm tải nhận thức đáng kể.

### 7.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Dán nhãn trực tiếp (Label directly) lên biểu đồ theo dõi điểm số.*
- **Cách giải quyết:** Giáo viên vẽ biểu đồ Line chart với 3 đường biểu diễn kết quả học tập của 3 tổ. Thay vì để chú giải (Legend) "Tổ 1: Màu xanh, Tổ 2: Màu đỏ..." ở góc dưới biểu đồ buộc mắt giáo viên phải lia qua lia lại để đối chiếu màu, hãy dán trực tiếp chữ "Tổ 1", "Tổ 2" cùng màu ngay tại điểm kết thúc của mỗi đường dây. Việc này loại bỏ hoàn toàn một bước tra cứu thừa trong não.

---
Nguồn: [[SOURCE_VIZ_Storytelling_with_Data_P1]] (Xác nhận Rule 14 từ: [[\VIZ_Storytelling_with_Data_P1]])
