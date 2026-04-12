---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v04_3
  title: CONV_atoms_v04_3
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu **Volume v04** về IoT, Robotics và lập trình điều khiển:

- **Fact:** [CONV] Hệ thống chấm điểm dự án IoT/Robotics bao gồm 5 tiêu chí chính: Kỹ thuật & Lập trình (35đ), Thiết kế 3D & Thẩm mỹ (25đ), Thuyết trình (25đ), Tính khả thi & bám kit (10đ), và Tuân thủ định dạng (5đ).
- **Source:** [vv04 - Phần: Phiếu chấm nhanh (1 trang)]
- **Tag:** [vv04]

- **Fact:** [CONV] Một dự án IoT đạt yêu cầu về tính khả thi và bám sát bộ kit phải sử dụng tối thiểu ≥3 cảm biến và ≥2 cơ cấu chấp hành (như relay, bơm, servo, quạt).
- **Source:** [vv04 - Phần: 4) Tính khả thi & bám kit – 10đ]
- **Tag:** [vv04]

- **Fact:** [CONV] Logic điều khiển tưới cây tự động mẫu: Kích hoạt bơm khi độ ẩm đất < 35% và ánh sáng > 200 lux; giới hạn thời gian bơm tối đa 20 giây và khóa bơm (lockout) trong 2 phút sau mỗi lần tưới.
- **Source:** [vv04 - Phần: Gợi ý nhanh cho thí sinh (không cần phần cứng)]
- **Tag:** [vv04]

- **Fact:** [CONV] Cơ chế Hysteresis (độ trễ) được sử dụng để chống nhiễu và tránh bật/tắt thiết bị liên tục; ví dụ: bật quạt khi T > 30°C nhưng chỉ tắt khi T < 28°C (sai số ±2°C).
- **Source:** [vv04 - Phần: Gợi ý nhanh cho thí sinh & Mẫu demo]
- **Tag:** [vv04]

- **Fact:** [CONV] Sơ đồ khối IoT tiêu chuẩn phải thể hiện rõ luồng dữ liệu từ Nguồn (5V/USB-C) → Bộ điều khiển (Yolo:Bit/Yolo UNO) → Cảm biến (Input) → Cơ cấu chấp hành (Output) → Giao diện người dùng (LCD/LED).
- **Source:** [vv04 - Phần: 1) Sơ đồ khối IoT (mô tả chữ)]
- **Tag:** [vv04]

- **Fact:** [CONV] Các tính năng an toàn (Fail-safe) bắt buộc trong lập trình điều khiển bao gồm: Timeout (giới hạn thời gian chạy), Lockout (thời gian nghỉ giữa các chu kỳ), xử lý khi mất tín hiệu cảm biến và chế độ điều khiển thủ công (Manual override).
- **Source:** [vv04 - Phần: 3. Fail-safe & An toàn]
- **Tag:** [vv04]

- **Fact:** [CONV] Kế hoạch kiểm thử (Test plan) cho hệ thống IoT cần tối thiểu 5 ca kiểm thử (test cases) có thông số đầu vào định lượng, kết quả đầu ra mong đợi và tiêu chí đạt/không đạt.
- **Source:** [vv04 - Phần: 4. Kế hoạch kiểm thử]
- **Tag:** [vv04]

- **Fact:** [CONV] Trong thiết kế 3D cho IoT, các yếu tố kỹ thuật cần lưu ý bao gồm: độ kín nước của file STL (watertight), dung sai lắp ghép (0.3-0.4mm), độ dày tường (1.2-1.6mm) và hạn chế góc nghiêng (overhang) > 60 độ để giảm support khi in.
- **Source:** [vv04 - Phần: 3) Mô hình 3D “skibidi – Viet Nguyễn” & Gợi ý nâng điểm]
- **Tag:** [vv04]

- **Fact:** [CONV] Cảm biến siêu âm hoặc hồng ngoại (IR) được sử dụng trong hệ thống tưới để phát hiện người trong khoảng cách < 30cm nhằm tạm dừng hoạt động bơm để đảm bảo an toàn và thẩm mỹ.
- **Source:** [vv04 - Phần: Mẫu demo (tham khảo) – Chủ đề “Tưới chậu cây tiết kiệm”]
- **Tag:** [vv04]

- **Fact:** [CONV] Việc không sử dụng pin-map hoặc không viết mã nguồn (code) cụ thể vẫn có thể hoàn thành barem điểm "Bạn Lập trình" nếu tập trung vào sơ đồ khối, lưu đồ thuật toán (flowchart) và kế hoạch kiểm thử.
- **Source:** [vv04 - Phần: Barem chi tiết – Bạn Lập trình (35đ)]
- **Tag:** [vv04]