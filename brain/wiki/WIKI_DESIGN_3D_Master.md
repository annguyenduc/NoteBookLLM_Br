---
file_id: "WIKI_DESIGN_3D_MASTER"
title: "Thiết kế 3D và Công nghệ In 3D"
category: "Wiki Page"
prefix: "WIKI"
tags: ["3D_Design", "Tinkercad", "Maker_Empire", "3D_Printing", "Cura"]
source: "[[DESIGN_3D_Tinkercad_de_trac_nghiem_1_-_3d_m1.md]], [[DESIGN_Maker_Empire_de_trac_nghiem_1_-_maker_empire.md]]"
status: "verified"
created: "2026-04-26"
last_updated: "2026-04-26"
---

# 🧊 Thiết kế 3D và Công nghệ In 3D

## 📌 Định nghĩa cốt lõi
Thiết kế 3D là quá trình tạo ra các mô hình kỹ thuật số trong không gian ba chiều (X, Y, Z). Các mô hình này sau đó có thể được "cắt lớp" (Slicing) và in ra thành vật thể vật lý bằng máy in 3D.

## 🔍 Công cụ thiết kế chính

### 1. Tinkercad (Phổ thông)
*   **Thao tác cơ bản**: Ctrl+D (Duplicate), Ctrl+G (Group), Align, Mirror.
*   **Kỹ thuật nâng cao**: Sử dụng khối "Hole" để khoét rỗng, Duplicate & Repeat để tạo các cấu trúc lặp lại (ví dụ: vạch đồng hồ, mạch ADN).
*   **Quản lý**: Đăng nhập qua Class Code và Nickname.

### 2. Maker Empire (Thiết kế 3D cho trẻ em)
*   **Giao diện**: World (chứa Basic Training), Gallery, Challenge, Create (tạo mới).
*   **Thao tác Camera**:
    *   **Xoay**: Chuột trái/phải + di chuyển hoặc `Shift` + di chuyển.
    *   **Phóng to/Thu nhỏ**: Lăn bánh xe chuột hoặc nhấp đôi chuột trái (vào đối tượng để phóng to, ra ngoài để thu nhỏ).
    *   **Di chuyển tầm nhìn (Pan)**: Nhấn giữ bánh xe chuột + di chuyển hoặc `Ctrl` + di chuyển.
*   **Công cụ biến đổi**:
    *   **Resize**: Thay đổi kích thước (có chế độ tự do và giữ tỉ lệ qua biểu tượng móc xích).
    *   **Move & Rotate**: Di chuyển và xoay theo các trục.
    *   **Magnet**: Dán đối tượng lên bề mặt khác hoặc đưa vật về mặt sàn.
*   **Kỹ thuật nâng cao**:
    *   **Group**: Nhóm đối tượng (nhấn giữ `Ctrl` để chọn nhiều vật).
    *   **Mirror**: Tạo bản sao đối xứng.
    *   **Lưu dự án**: Chọn `Finish`.

## 🖨️ Quy trình In 3D (Workflow)
1.  **Thiết kế**: Tạo file trên Tinkercad, xuất ra định dạng `.STL` hoặc `.OBJ`.
2.  **Lập trình in (Slicing)**: Sử dụng phần mềm **Ultimaker Cura**.
    *   **Infill**: Độ đặc của vật thể (giảm infill để in nhanh hơn).
    *   **Layer Height**: Bề dày lớp in (tăng độ dày để in nhanh hơn nhưng bề mặt sẽ thô).
    *   **Build Plate Adhesion**:
        *   **Skirt**: Vẽ đường bao quanh, không chạm vật thể. Đây là chế độ **nhanh nhất** và tốn ít nhựa nhất.
        *   **Brim**: Vẽ lớp bao quanh chạm sát vật thể để tăng diện tích tiếp xúc.
        *   **Raft**: Xây dựng một cái "bè" bên dưới vật thể. Tốn nhựa nhất nhưng chắc chắn nhất.
3.  **In G-code**: Xuất file ra định dạng `.GCODE`, nạp vào máy in và thực hiện in.

## 💡 Các thông số kỹ thuật & Phím tắt
*   **Hệ tọa độ**: X, Y, Z.
*   **Kích thước & Biến đổi**:
    *   **Shift + Kéo**: Thay đổi kích thước giữ nguyên tỉ lệ.
    *   **Alt + Kéo**: Thay đổi kích thước từ tâm của vật thể.
    *   **Align (Căn chỉnh)**: Sử dụng các nút đen để căn chỉnh đối tượng theo các cạnh hoặc tâm.
*   **Phím tắt & Độ cao**:
    *   `W`: Workplane (Mặt phẳng làm việc).
    *   `R`: Ruler (Thước đo).
    *   `D`: Đưa vật thể về mặt phẳng thiết kế (Workplane).
    *   `Ctrl + D`: Duplicate and Repeat (Nhân bản và lặp lại thao tác trước đó).
    *   `Ctrl + Mũi tên lên/xuống`: Nâng hoặc hạ độ cao vật thể.

## ⚙️ Cơ chế chuyển động & Dung sai (Engineering)
*   **Dung sai (Tolerance)**: Để các bộ phận có thể lắp ghép hoặc xoay được sau khi in, cần có khoảng hở giữa trục và lỗ.
    *   *Ví dụ*: Trục 3mm thì lỗ tròn nên là 5mm (khoảng cách 2mm) để đảm bảo không bị dính sau khi in.
*   **Khớp nối (Joints)**:
    *   **Trục - Lỗ**: Cơ chế cơ bản nhất cho móc khóa hoặc bánh xe.
    *   **Khớp nối phẳng (Print-in-place)**: Thiết kế rãnh rỗng (Hole) xen kẽ để các bộ phận tách rời nhưng vẫn liên kết bằng trục nhỏ bên trong.
*   **Quy trình Group khớp nối**: 1. Tạo rãnh -> 2. Tạo lỗ cho trục -> 3. Group khối chính với các khớp nối.


## 🔗 Liên kết tư duy
*   [[WIKI_DESIGN_General_Master]] - Tổng quan thiết kế.
*   [[WIKI_3D_Tinkercad_System]] - Chi tiết kiến trúc và môi trường Tinkercad.
*   [[WIKI_ROBOT_Hardware_Master]] - Thiết kế khung vỏ cho Robot.

## 4F — Phản tư sư phạm
*   **Facts**: In 3D mất nhiều thời gian, nên cần tối ưu hóa các thông số Slicing trong Cura.
*   **Feelings**: Học sinh cảm thấy tuyệt vời khi cầm trên tay sản phẩm mình tự thiết kế.
*   **Findings**: Kỹ thuật "Duplicate and Repeat" là chìa khóa để tạo ra các cấu trúc phức tạp một cách nhanh chóng.
*   **Futures**: Ứng dụng in 3D trong việc tạo ra các bộ phận thay thế hoặc mô hình học cụ.

## 📖 Nguồn trích dẫn
*   [[[brain/raw/DESIGN_3D_Tinkercad_de_trac_nghiem_1_-_3d_m1.md]]](file:///d:/NoteBookLLM_Br/brain/raw/[[brain/raw/DESIGN_3D_Tinkercad_de_trac_nghiem_1_-_3d_m1.md]])
*   [[[brain/raw/DESIGN_Maker_Empire_de_trac_nghiem_1_-_maker_empire.md]]](file:///d:/NoteBookLLM_Br/brain/raw/[[brain/raw/DESIGN_Maker_Empire_de_trac_nghiem_1_-_maker_empire.md]])
