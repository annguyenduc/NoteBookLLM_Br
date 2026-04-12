Dưới đây là phần **giải thích ví dụ** về tương tác cơ bản với GitHub và phần **trích xuất sự kiện** theo quy tắc LOM v4.1.

---

### ✅ Giải thích ví dụ: Basic interaction with GitHub

**1. Sao chép kho lưu trữ (Clone Repository):**
```bash
git clone https://github.com/redquinoa/health-checks.git
```
👉 Lệnh này tải toàn bộ mã nguồn, các nhánh và lịch sử chỉnh sửa từ địa chỉ URL trên GitHub về máy tính cá nhân của bạn.

**2. Xác thực người dùng:**
```text
Username for 'https://github.com': redquinoa
Password for 'https://redquinoa@github.com': 
```
👉 Khi sử dụng giao thức HTTPS, Git yêu cầu bạn nhập tên đăng nhập và mật khẩu (hoặc Personal Access Token) để xác minh quyền truy cập.

**3. Quá trình tải dữ liệu (Output):**
*   `Enumerating objects`: Git đếm tổng số tệp tin và lịch sử trong kho.
*   `Counting objects`: Kiểm tra các đối tượng cần tải.
*   `Compressing objects`: Nén dữ liệu để truyền tải nhanh hơn.
*   `Unpacking objects`: Giải nén dữ liệu vào thư mục cục bộ trên máy bạn.

**4. Truy cập vào dự án:**
```bash
cd health-checks/
ls -l
```
👉 Sau khi clone xong, bạn dùng `cd` để di chuyển vào thư mục dự án vừa tạo và `ls -l` để liệt kê danh sách các file đã tải về.

---

### 📋 Trích xuất sự kiện (LOM v4.1)

- **Fact:** Lệnh `git clone [URL]` được sử dụng để tạo một bản sao cục bộ của một kho lưu trữ từ xa (remote repository) từ GitHub về máy tính.
- **Source:** (v10 - Section: Basic interaction with GitHub)
- **Tag:** [vv10]

- **Fact:** Khi thực hiện clone qua giao thức HTTPS, Git yêu cầu xác thực danh tính thông qua Username và Password của tài khoản GitHub.
- **Source:** (v10 - Section: Basic interaction with GitHub)
- **Tag:** [vv10]

- **Fact:** Quá trình `git clone` bao gồm các giai đoạn: liệt kê đối tượng (enumerating), nén (compressing) và giải nén (unpacking) dữ liệu từ server về máy cục bộ.
- **Source:** (v10 - Section: Basic interaction with GitHub)
- **Tag:** [vv10]

- **Fact:** Sau khi clone thành công, một thư mục mới có tên trùng với tên kho lưu trữ (ví dụ: `health-checks`) sẽ được tạo ra trong thư mục hiện hành.
- **Source:** (v10 - Section: Basic interaction with GitHub)
- **Tag:** [vv10]