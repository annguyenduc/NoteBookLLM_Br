---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v06_7
  title: atoms_v06_7
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu về vận hành máy in 3D (một phần quan trọng trong chế tạo Robotics và thiết bị IoT):

- **Fact:** Trong phần mềm Cura (chế độ Preview - Line Type), các thành phần in được phân biệt bằng màu sắc: Vỏ ngoài (vàng/cam), Infill (đỏ), Support (xanh lá), và Brim/Raft (xanh dương).
- **Source:** [vv06 - Section: Cura Preview Color Scheme]
- **Tag:** [vv06]

- **Fact:** Máy in Elegoo Neptune 4 sử dụng file định dạng `.gcode` để thực hiện lệnh in, thường được lưu vào thẻ nhớ microSD hoặc truyền qua cổng USB.
- **Source:** [vv06 - Section: 1. Xuất file G-code]
- **Tag:** [vv06]

- **Fact:** Thông số nhiệt độ tiêu chuẩn khi in nhựa PLA trên máy Neptune 4 là 200°C cho đầu phun (nozzle) và 60°C cho bàn in (bed).
- **Source:** [vv06 - Section: 3. Quá trình in]
- **Tag:** [vv06]

- **Fact:** Khi nạp nhựa (filament) 1.75mm vào máy in, đầu sợi nhựa cần được cắt vát khoảng 45° để dễ dàng luồn qua cảm biến filament và ống dẫn PTFE.
- **Source:** [vv06 - Section: 1. Chuẩn bị & 3. Luồn nhựa vào máy]
- **Tag:** [vv06]

- **Fact:** Lệnh G-code `G28` dùng để đưa toàn bộ các trục máy in về vị trí gốc (home), trong khi `M420 S1` dùng để kích hoạt lưới cân bàn (mesh) đã lưu từ quá trình Auto Bed Leveling.
- **Source:** [vv06 - Section: Start G-code]
- **Tag:** [vv06]

- **Fact:** Để tránh làm hỏng bề mặt bàn in PEI, người dùng nên đợi nhiệt độ bàn giảm xuống dưới 35–40°C trước khi gỡ sản phẩm hoặc sử dụng tính năng đàn hồi của tấm thép lò xo để làm bong nhựa.
- **Source:** [vv06 - Section: 1. Chờ nguội mới gỡ & 2. Uốn bàn in]
- **Tag:** [vv06]

- **Fact:** Tấm bàn in "Textured PEI Plate" (mặt nhám) được thiết kế đa dụng cho các loại nhựa PLA, TPU, ABS, PETG và Carbon-Fiber, giúp sản phẩm dễ gỡ hơn sau khi nguội.
- **Source:** [vv06 - Section: 2. Tấm Textured PEI Plate]
- **Tag:** [vv06]

- **Fact:** Hiện tượng cong vênh (warping) ở các chi tiết nhỏ hoặc dài thường do Z-offset quá cao, nhiệt bàn thấp hoặc quạt làm mát thổi mạnh quá sớm.
- **Source:** [vv06 - Section: 1. Nguyên nhân phần đuôi dễ bị lỗi]
- **Tag:** [vv06]

- **Fact:** Để tăng độ bám dính lớp đầu tiên, thông số "Initial Fan Speed" nên được thiết lập ở mức 0% và chỉ bắt đầu bật quạt làm mát từ lớp thứ 3 đến thứ 5 (tương đương độ cao khoảng 0.6mm).
- **Source:** [vv06 - Section: 2. Giải pháp khắc phục mạnh hơn & 2. Chỉnh thông số Cooling]
- **Tag:** [vv06]

- **Fact:** Máy Neptune 4 Pro nguyên bản không tích hợp Wi-Fi; việc điều khiển không dây yêu cầu các giải pháp bổ sung như Elegoo Nebula Pad hoặc sử dụng Raspberry Pi chạy Klipper (Mainsail/Fluidd).
- **Source:** [vv06 - Section: 2. Có thể in không dây được không?]
- **Tag:** [vv06]

- **Fact:** Cồn Isopropyl (IPA 70–99%) là dung dịch tiêu chuẩn để vệ sinh định kỳ bề mặt bàn in PEI nhằm loại bỏ dầu mỡ và bụi nhựa, đảm bảo độ bám dính.
- **Source:** [vv06 - Section: 1. Vệ sinh định kỳ]
- **Tag:** [vv06]