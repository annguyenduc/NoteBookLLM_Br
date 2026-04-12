---
file_id: CONV_Atoms_atoms_v16_17
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms atoms v16 17

# Tài liệu Học Tập: Mạng Máy Tính và Công Nghệ Truyền Thông - LOM v4.4 Supreme

## Tổng Quan Khóa Học

**Tên Khóa Học:** Mạng Máy Tính và Công Nghệ Truyền Thông  
**Mã Học Phần:** NET-TECH-101  
**Thời Lượng:** 45 giờ học  
**Trình Độ:** Trung cấp  
**Ngôn Ngữ:** Tiếng Việt [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Mục Tiêu Học Tập

Sau khi hoàn thành khóa học này, học viên sẽ có khả năng:

- Hiểu và áp dụng các nguyên lý cơ bản của biểu thức chính quy (Regex)
- Phân tích cấu trúc và chức năng của các loại mạng (WAN, LAN, không dây)
- Xác định các công nghệ truyền thông Internet phổ biến
- Giải thích các giao thức mạng và dịch vụ hỗ trợ

---

## Bài 1: Biểu Thức Chính Quy (Regular Expressions)

### 1.1 Giới Thiệu

Biểu thức chính quy (Regex) là công cụ mạnh mẽ để tìm kiếm và xử lý văn bản dựa trên các mẫu ký tự cụ thể.

### 1.2 Các Ký Tự Đặc Biệt

| Ký Tự | Ý Nghĩa |
|-------|---------|
| `.` | Đại diện cho bất kỳ ký tự đơn nào [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) |
| `^` | Neo đầu dòng (khớp với điểm bắt đầu của một dòng) [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) |
| `$` | Neo cuối dòng (khớp với điểm kết thúc của một dòng) [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) |

### 1.3 Công Cụ Hỗ Trợ

- **grep**: Công cụ dòng lệnh dùng để tìm kiếm văn bản bằng biểu thức chính quy [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Bài 2: Mạng Diện Rộng (WAN)

### 2.1 Khái Niệm WAN

**WAN (Wide Area Network)** là mạng diện rộng kết nối các mạng cục bộ (LAN) ở khoảng cách địa lý xa nhau [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### 2.2 Cấu Trúc WAN

- **Local Loop**: Khu vực giữa điểm phân giới (demarcation point) và mạng lõi của ISP [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
- **VPN điểm-đến-điểm**: Còn gọi là site-to-site VPN [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Bài 3: Mạng Không Dây (Wireless Networking)

### 3.1 Tiêu Chuẩn 802.11

- **Header 802.11**: Chứa 4 trường địa chỉ [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### 3.2 Dải Tần Số

| Dải Tần | Tên Gọi |
|---------|---------|
| 2.4GHz | Dải tần phổ biến đầu tiên |
| 5GHz | Dải tần mới với ít nhiễu hơn [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) |

### 3.3 Bảo Mật Không Dây

- **WPA3**: Giao thức bảo mật mới thay thế WPA2 [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Bài 4: Công Nghệ Internet

### 4.1 Các Loại Kết Nối

| Loại Kết Nối | Tốc Độ | Môi Trường |
|--------------|--------|------------|
| T1 | 1.544 Mb/s | Cáp đồng xoắn đôi [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) |
| ADSL | Asymmetric | Đường dây điện thoại [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) |
| FTTP | Fiber | Cáp quang đến tận nơi [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) |

### 4.2 FTTP (Fiber to the Premises)

FTTP là công nghệ kéo cáp quang trực tiếp đến cơ sở của người dùng [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Bài 5: Dịch Vụ Mạng

### 5.1 DNS (Domain Name System)

- **Cổng 53**: Dùng cho các gói tin DNS qua UDP [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
- **Round Robin**: Kỹ thuật cân bằng tải DNS [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### 5.2 NAT (Network Address Translation)

- **Masquerading**: Kỹ thuật ẩn địa chỉ IP nguồn [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Bài 6: Công Nghệ Sợi Quang

### 6.1 ONT (Optical Network Terminal)

ONT là điểm phân giới trong công nghệ truyền dẫn bằng cáp quang [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Bài 7: Địa Chỉ IP

### 7.1 Cấu Trúc Địa Chỉ IP

- **Octet**: Mỗi octet gồm 8 bit, giá trị từ 0-255 [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
- **Lớp B**: Hai octet đầu cho Network ID, hai octet sau cho Host ID [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Bài 8: Mạng Quay Số (Dial-up Networking)

### 8.1 Tỷ Lệ Baud

**Baud Rate**: Đơn vị đo số lượng bit gửi qua đường dây điện thoại mỗi giây [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Bảng Tóm Tắt Thuật Ngữ

| Thuật Ngữ | Định Nghĩa |
|-----------|------------|
| Regex | Biểu thức chính quy |
| WAN | Mạng diện rộng |
| VPN | Mạng riêng ảo |
| WPA3 | Giao thức bảo mật không dây mới |
| FTTP | Cáp quang đến tận nơi |
| DNS | Hệ thống phân giải tên miền |
| NAT | Chuyển đổi địa chỉ mạng |
| ONT | Thiết bị đầu cuối mạng quang |
| Baud Rate | Tốc độ truyền tín hiệu |

---

## Tài Liệu Tham Khảo

- [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
- Tài liệu kỹ thuật mạng hiện hành
- Tiêu chuẩn IEEE 802.11
- RFC 1035 (DNS)

---

## Ghi Chú Bản Quyền

Tài liệu này được tạo ra theo tiêu chuẩn LOM v4.4 Supreme, sử dụng nội dung từ nguồn dữ liệu Volume v16 (vv16). Mọi quyền thuộc về đơn vị phát triển nội dung gốc. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)