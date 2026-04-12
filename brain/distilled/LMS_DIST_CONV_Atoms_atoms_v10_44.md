---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v10_44
  title: 📚 Tóm tắt bài học: **Creating Bash scripts**
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, mình đã nhận được nội dung bài mới: **Review: Creating Bash scripts**. Theo đúng quy trình bạn đã thiết lập, mình sẽ tóm tắt mục đích, hướng dẫn chuẩn bị môi trường và trích xuất các sự kiện kỹ thuật (Facts) theo chuẩn @scout.

---

# 📚 Tóm tắt bài học: **Creating Bash scripts**

### 🎯 Mục đích của bài này:
- Hướng dẫn cách tạo một file script Bash hoàn chỉnh (tập lệnh tự động).
- Cách sử dụng **Shebang** (`#!/bin/bash`) để hệ thống biết cần dùng trình thông dịch nào.
- Cách kết hợp nhiều lệnh hệ thống (`date`, `uptime`, `free`, `who`) vào một file duy nhất để thu thập thông tin hệ thống nhanh chóng.
- Giới thiệu cách viết lệnh trên nhiều dòng hoặc gộp trên một dòng bằng dấu chấm phẩy (`;`).

---

# 🛠 Hướng dẫn tạo file thực hành: `gather-information.sh`

Để thực hành giống hệt video, bạn hãy tạo file script này trên máy của mình:

### Bước 1: Tạo file
```bash
nano gather-information.sh
```

### Bước 2: Dán nội dung sau vào (Phiên bản đầy đủ):
```bash
#!/bin/bash

echo "Starting at: $(date)"; echo

echo "UPTIME"; uptime; echo

echo "FREE"; free; echo

echo "WHO"; who; echo

echo "Finishing at: $(date)"
```

### Bước 3: Cấp quyền thực thi và chạy
```bash
chmod +x gather-information.sh
./gather-information.sh
```

---

# 🔍 Trích xuất sự kiện kỹ thuật (Facts) - @scout LOM v4.1

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu bạn cung cấp:

- **Fact:** Một script Bash tiêu chuẩn bắt đầu bằng dòng khai báo trình thông dịch `#!/bin/bash` (Shebang).
- **Source:** (v10 - Section: Creating Bash scripts - Line 1)
- **Tag:** [vv10]

- **Fact:** Cú pháp `$(date)` được sử dụng để thực thi lệnh `date` và chèn kết quả trực tiếp vào trong một chuỗi văn bản (Command Substitution).
- **Source:** (v10 - Section: Creating Bash scripts - Line 2)
- **Tag:** [vv10]

- **Fact:** Dấu chấm phẩy (`;`) cho phép đặt nhiều lệnh Linux trên cùng một dòng để thực thi tuần tự.
- **Source:** (v10 - Section: Creating Bash scripts - Line 11-14)
- **Tag:** [vv10]

- **Fact:** Lệnh `uptime` cung cấp thông tin về thời gian hệ thống đã hoạt động, số lượng người dùng và chỉ số tải trung bình (load average).
- **Source:** (v10 - Section: Creating Bash scripts - Code output)
- **Tag:** [vv10]

- **Fact:** Lệnh `who` liệt kê danh sách các người dùng hiện đang đăng nhập vào hệ thống cùng với thông tin terminal của họ.
- **Source:** (v10 - Section: Creating Bash scripts - Code output)
- **Tag:** [vv10]

- **Fact:** Bash script là công cụ nền tảng để quản lý và thu thập dữ liệu từ các hệ thống nhúng chạy Linux (như Raspberry Pi trong IoT hoặc các robot chạy ROS).
- **Source:** [Kiến thức bổ trợ cho ngữ cảnh IoT/Robotics]
- **Tag:** [Unverified_Source]

---

**🚀 Bạn đã sẵn sàng chưa?**
Nếu bạn đã chạy thử script `gather-information.sh` và thấy kết quả hiện ra thông tin RAM (`free`) và thời gian (`date`), chúng ta có thể tiếp tục sang phần tiếp theo của Bash Scripting! 

Bạn muốn mình giải thích thêm về **biến (variables)** trong Bash hay chuyển sang phần **vòng lặp (loops)**? Hãy gửi nội dung tiếp theo nhé! 🎯