---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v06_7
  title: CONV_atoms_v06_7
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu về máy in 3D (một phần của hệ sinh thái Robotics và chế tạo phần cứng IoT):

- **Fact:** [CONV] [Trong phần mềm Cura, chế độ hiển thị "Line Type" phân biệt các thành phần in bằng màu sắc: Vỏ (vàng/cam), Infill (đỏ), Support (xanh lá), Brim/Raft (xanh dương).]
- **Source:** [Phần "Cách kiểm tra" và "Kết luận" đầu file]
- **Tag:** [vv06]

- **Fact:** [CONV] [Máy in Elegoo Neptune 4 sử dụng mã G-code để điều khiển: G28 (Home toàn bộ trục), G90 (Tọa độ tuyệt đối), M82 (Đùn nhựa tuyệt đối).]
- **Source:** [Phần "1. Xuất file G-code" và "Start G-code"]
- **Tag:** [vv06]

- **Fact:** [CONV] [Lệnh M420 S1 trong G-code được sử dụng để kích hoạt lưới cân bằng bàn in (mesh) đã lưu trong EEPROM sau khi thực hiện Auto Bed Leveling.]
- **Source:** [Phần "Ghi chú nhanh" sau End G-code]
- **Tag:** [vv06]

- **Fact:** [CONV] [Hệ thống nạp nhựa của Neptune 4 bao gồm: Giá đỡ cuộn (spool holder), cảm biến filament (filament sensor), ống dẫn PTFE và bộ đùn (extruder).]
- **Source:** [Phần "3. Luồn nhựa vào máy" và "ASCII sơ đồ đường đi"]
- **Tag:** [vv06]

- **Fact:** [CONV] [Bàn in Textured PEI Plate (mặt nhám) hỗ trợ đa dạng vật liệu như PLA, TPU, ABS, PETG và Carbon-Fiber, giúp sản phẩm dễ gỡ hơn sau khi nguội.]
- **Source:** [Phần "2. Tấm Textured PEI Plate (ảnh 2)"]
- **Tag:** [vv06]

- **Fact:** [CONV] [Để chống cong vênh (warping) cho sản phẩm Robotics, cần thiết lập Initial Fan Speed = 0% trong 3-5 lớp đầu tiên để nhựa bám chắc vào bàn in.]
- **Source:** [Phần "Initial Fan Speed = 0% và chỉ bật quạt sau layer thứ 3–5"]
- **Tag:** [vv06]

- **Fact:** [CONV] [Máy in Neptune 4 Pro có thể nâng cấp khả năng kết nối không dây (IoT) thông qua Elegoo Nebula Pad hoặc sử dụng Raspberry Pi chạy OctoPrint/Klipper.]
- **Source:** [Phần "2. Có thể in không dây được không?"]
- **Tag:** [vv06]

- **Fact:** [CONV] [Z-offset là thông số quan trọng điều chỉnh khoảng cách giữa đầu phun và bàn in; nếu quá cao sẽ gây bong tróc sản phẩm ngay từ lớp đầu tiên.]
- **Source:** [Phần "2. Cách khắc phục" lỗi bong tróc]
- **Tag:** [vv06]