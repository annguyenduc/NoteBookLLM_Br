---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v16_18
  title: CONV_atoms_v16_18
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) kỹ thuật về nền tảng mạng (cơ sở hạ tầng cho IoT và Robotics) được trích xuất từ nguồn dữ liệu v16:

- **Fact:** [CONV] Subnet Mask được sử dụng để xác định địa chỉ mạng bằng cách kết hợp với địa chỉ IP, giúp phân biệt các mạng con (subnet) nhằm tăng hiệu suất và bảo mật.
- **Source:** [vv16] - Section: Xác định địa chỉ mạng / Phân biệt các mạng con.
- **Tag:** [vv16]

- **Fact:** [CONV] CIDR (Classless Inter-Domain Routing) là phương pháp định tuyến linh hoạt thay thế cho các lớp mạng cố định (A, B, C), sử dụng ký hiệu "prefix length" (ví dụ: /24) để biểu thị số bit mạng.
- **Source:** [vv16] - Section: Đặc điểm của CIDR.
- **Tag:** [vv16]

- **Fact:** [CONV] Địa chỉ MAC (Media Access Control) là định danh duy nhất dài 48 bit (6 byte) được gắn cứng vào card mạng, dùng để xác định thiết bị trong mạng cục bộ (Layer 2).
- **Source:** [vv16] - Section: địa chỉ mac là gì?.
- **Tag:** [vv16]

- **Fact:** [CONV] Trong mỗi mạng IP, luôn có 2 địa chỉ ID máy chủ bị mất (không thể gán cho thiết bị): một cho địa chỉ mạng (network address) và một cho địa chỉ quảng bá (broadcast address).
- **Source:** [vv16] - Section: Question 5 (How many possible host IDs...).
- **Tag:** [vv16]

- **Fact:** [CONV] Autonomous Systems (AS) là một tập hợp các mạng và thiết bị được quản lý bởi một tổ chức hoặc ISP duy nhất, hoạt động theo các quy tắc định tuyến riêng.
- **Source:** [vv16] - Section: Autonomous Systems (AS).
- **Tag:** [vv16]

- **Fact:** [CONV] Giao thức ARP (Address Resolution Protocol) có mục đích thông báo địa chỉ MAC của thiết bị đích cho nút đang phát sóng để hoàn thiện khung dữ liệu phần cứng.
- **Source:** [vv16] - Section: Question 5 (What is the purpose of an ARP response?).
- **Tag:** [vv16]

- **Fact:** [CONV] Một địa chỉ IPv4 tiêu chuẩn có độ dài là 32 bit.
- **Source:** [vv16] - Section: Question 2 (How many bits long is an IP address?).
- **Tag:** [vv16]

- **Fact:** [CONV] Lớp Vận chuyển (Transport Layer) chịu trách nhiệm phân chia dữ liệu từ lớp Ứng dụng thành các đoạn nhỏ (segments/datagrams) và đảm bảo truyền thông tin cậy (TCP) hoặc tốc độ cao (UDP).
- **Source:** [vv16] - Section: Transport Layer.
- **Tag:** [vv16]

- **Fact:** [CONV] Các dải địa chỉ IP không định tuyến (non-routable) dùng cho mạng nội bộ bao gồm: 10.0.0.0/8, 172.16.0.0/12 và 192.168.0.0/16.
- **Source:** [vv16] - Section: Question 5 (Which of the following are non-routable IP addresses?).
- **Tag:** [vv16]

- **Fact:** [CONV] Bảng định tuyến (Routing Table) cơ bản thường chứa 4 cột thông tin chính: Mạng đích (Destination Network), Bước nhảy tiếp theo (Next Hop), Tổng số bước nhảy (Total Hops) và Giao diện (Interface).
- **Source:** [vv16] - Section: Question 3 (A typical routing table may contain...).
- **Tag:** [vv16]