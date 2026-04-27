---
file_id: "WIKI_DESIGN_WORDPRESS"
title: "Thiết kế Website với WordPress"
category: "Wiki Page"
prefix: "WIKI"
tags: ["WordPress", "CMS", "Web_Design", "Domain", "SEO"]
source: "[[DESIGN_Wordpress_de_trac_nghiem_1_-_Wordpress.md]]"
status: "verified"
created: "2026-04-26"
last_updated: "2026-04-26"
---

# 🌐 Thiết kế Website với WordPress

## 📌 Định nghĩa cốt lõi
WordPress là một phần mềm mã nguồn mở (CMS - Content Management System) giúp người dùng tạo website, blog hoặc ứng dụng một cách dễ dàng mà không cần biết sâu về lập trình.

## 🏗️ Cấu trúc và Nền tảng
*   **WordPress.com vs WordPress.org**:
    *   **WordPress.com**: Dịch vụ lưu trữ web tích hợp, có bản miễn phí (dùng tên miền `...wordpress.com`).
    *   **WordPress.org**: Nền tảng tự cài đặt, linh hoạt hơn nhưng yêu cầu người dùng tự quản lý hosting.
*   **Tên miền (Domain)**: Địa chỉ của website. Chuyển đổi từ tên miền sang IP do máy chủ **DNS** đảm trách.
    *   `.com`: Website thương mại.
    *   `.edu`: Tổ chức giáo dục.
    *   `.gov`: Tổ chức chính phủ.
    *   `.org`: Tổ chức phi lợi nhuận.
    *   `.net`: Nhà cung cấp dịch vụ mạng.
*   **Sitemap**: Bản đồ trang web giúp công cụ tìm kiếm và người dùng hiểu được cấu trúc phân cấp của website.

## 📝 Quản lý nội dung (Post vs Page)
| Đặc điểm | Post (Bài viết) | Page (Trang) |
| :--- | :--- | :--- |
| **Tính chất** | Động, liệt kê theo thời gian đảo ngược | Tĩnh, nội dung ít thay đổi |
| **Phân loại** | Sử dụng `Categories` và `Tags` | Không dùng Cat/Tag, dùng cấu trúc `Mẹ-Con` |
| **Ví dụ** | Tin tức, bài hướng dẫn, review | Giới thiệu, Liên hệ, Trang chủ |

*   **Featured Image**: Ảnh đại diện chính cho bài viết/trang.
*   **Excerpt**: Đoạn tóm tắt ngắn hiển thị ở trang danh sách.
*   **Schedule**: Hẹn giờ xuất bản bài viết tự động.

## 🎨 Giao diện và Điều hướng
*   **Theme**: Bộ giao diện quy định font chữ, màu sắc, bố cục.
    *   Đường dẫn: `Appearance -> Themes`.
    *   Lưu ý: Khi đổi Theme, trang chủ cũ thường được lưu thành bản nháp (Draft).
*   **Menu**: Thanh điều hướng chính (thường ở Header).
    *   Đường dẫn: `Appearance -> Customize -> Menus`.
    *   Có thể chèn: Page, Post, Category, Custom Link.

## 🛠️ Trình soạn thảo Block (Gutenberg)
*   **Paragraph**: Block văn bản cơ bản. Có tính năng `Drop cap`.
*   **Highlight**: Đổi màu cho một đoạn chữ nhỏ trong block văn bản.
*   **Media blocks**:
    *   `Gallery`: Bộ sưu tập ảnh.
    *   `Slide show`: Ảnh trình chiếu.
    *   `Tilted Gallery`: Thư viện ảnh nghiêng.
*   **Interactions**: `Post Comments Form` giúp người dùng để lại bình luận.

## 🔗 Liên kết tư duy
*   [[WIKI_DESIGN_Media_Master]] - Tổng quan về truyền thông số.
*   [[WIKI_DESIGN_General_Master]] - Nguyên lý thiết kế đồ họa.

## 📖 Nguồn trích dẫn
*   [[[brain/raw/DESIGN_Wordpress_de_trac_nghiem_1_-_Wordpress.md]]](file:///d:/NoteBookLLM_Br/brain/raw/[[brain/raw/DESIGN_Wordpress_de_trac_nghiem_1_-_Wordpress.md]])
