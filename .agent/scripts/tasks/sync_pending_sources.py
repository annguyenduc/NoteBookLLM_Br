# -*- coding: utf-8 -*-
"""
Script đồng bộ hóa danh sách nguồn trong thư mục 00_Inbox/sources-pending/
với file source_registry.md, tự động phát hiện trùng lặp bằng MD5 hash
và sinh source_id chuẩn hoá theo định dạng lowercase_snake_case.
"""

import os
import re
import hashlib
import sys

# Thiết lập encoding UTF-8 cho console output trên Windows
if sys.platform.startswith('win'):
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.detach())

PENDING_DIR = r"D:\NoteBookLLM_Br\00_Inbox\sources-pending"
REGISTRY_PATH = os.path.join(PENDING_DIR, "source_registry.md")

# Các file test mặc định bỏ qua
IGNORE_FILES = {"empty.pdf", "sample.pdf", "source_registry.md"}

# Map Category prefix sang tên đầy đủ của section trong Markdown
CATEGORY_MAP = {
    "ARCH": "Architecture",
    "AIMET": "AI/ML Engineering Tools",
    "DE": "Data Engineering",
    "DSML": "Data Science & Machine Learning",
    "FA": "Framework / Storytelling Analytics",
    "MATH": "Mathematics",
    "MISC": "Miscellaneous",
    "SQLDB": "SQL & Databases",
    "STAT": "Statistics",
    "SYS": "Systems & Operating Systems",
    "THINK": "Thinking & Problem-Solving",
    "VIZ": "Visualization & BI Tools"
}

def calculate_md5(filepath):
    """Tính MD5 hash của file theo từng chunk để tối ưu bộ nhớ"""
    hash_md5 = hashlib.md5()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest().upper()
    except Exception as e:
        print(f"[ERROR] Không thể tính hash cho file {filepath}: {e}")
        return None

def normalize_source_id(filename):
    """
    Sinh source_id theo convention lowercase_snake_case
    Ví dụ: ARCH_Thinking_in_Systems.pdf -> arch_thinking_in_systems
    """
    name_without_ext = os.path.splitext(filename)[0]
    # Thay thế các ký tự đặc biệt, khoảng trắng, gạch ngang thành gạch dưới
    clean_name = re.sub(r'[^a-zA-Z0-9_]', '_', name_without_ext)
    # Rút gọn nhiều gạch dưới liên tiếp
    clean_name = re.sub(r'_+', '_', clean_name)
    # Lowercase toàn bộ và loại bỏ gạch dưới ở đầu/cuối
    return clean_name.lower().strip('_')

def parse_registry(registry_path):
    """
    Parse source_registry.md để trích xuất:
    - Danh sách nguồn đã đăng ký (source_id -> {filename, status, category})
    - Danh sách file bị loại (filename -> reason)
    - Toàn bộ nội dung thô để tái cấu trúc
    """
    registered_sources = {}
    excluded_files = {}
    
    if not os.path.exists(registry_path):
        return registered_sources, excluded_files

    with open(registry_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse registered sources
    # Bảng format: | `source_id` | Tên File | Status |
    # Hoặc: | source_id | Tên File | Status |
    pattern_source = r'\|\s*`?([a-z0-9_]+)`?\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|'
    # Tìm tất cả dòng khớp bảng
    lines = content.split('\n')
    current_category = "MISC"
    
    for line in lines:
        if line.startswith('## '):
            # Cập nhật category hiện tại khi duyệt qua các section
            for prefix in CATEGORY_MAP.keys():
                if f"## {prefix} " in line:
                    current_category = prefix
                    break
        
        match = re.match(r'\|\s*`?([a-z0-9_~]+)`?\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|', line)
        if match:
            source_id = match.group(1).strip('`~ ')
            filename = match.group(2).strip('` ')
            status = match.group(3).strip('` ')
            
            # Bỏ qua dòng header của bảng
            if source_id.lower() == "source_id" or source_id.startswith("---"):
                continue
                
            registered_sources[source_id] = {
                "filename": filename,
                "status": status,
                "category": current_category
            }

    # Parse excluded files
    # Bảng format: | Tên File | Lý do |
    in_excluded_section = False
    for line in lines:
        if "## Files Bị Loại" in line:
            in_excluded_section = True
            continue
        if in_excluded_section and line.startswith('---'):
            in_excluded_section = False
            
        if in_excluded_section:
            match = re.match(r'\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|', line)
            if match:
                filename = match.group(1).strip('` ')
                reason = match.group(2).strip('` ')
                if filename.lower() == "tên file" or filename.startswith("---"):
                    continue
                excluded_files[filename] = reason

    return registered_sources, excluded_files

def write_registry(registry_path, registered_sources, excluded_files):
    """Ghi lại file source_registry.md theo cấu trúc chuẩn hoá"""
    
    # 1. Tính toán tóm tắt số lượng theo category
    cat_counts = {prefix: 0 for prefix in CATEGORY_MAP.keys()}
    for source in registered_sources.values():
        cat = source["category"]
        if cat in cat_counts:
            cat_counts[cat] += 1
            
    total_active = sum(cat_counts.values())

    lines = []
    lines.append("# Source Registry — 00_Inbox/sources-pending")
    lines.append("")
    lines.append("> Đăng ký source_id chuẩn hoá cho toàn bộ file canonical trong sources-pending.")
    lines.append("> Convention: `lowercase_snake_case` (từ tên file, bỏ extension, lowercase toàn bộ)")
    lines.append("> Canonical master: `3-resources/raw_sources/MASTER_SOURCE_INDEX.md`")
    lines.append(">")
    lines.append("> **Ví dụ chuẩn (Golden Case):**")
    lines.append("> `ARCH_Thinking_in_Systems.pdf` → `source_id: arch_thinking_in_systems`")
    lines.append(">")
    lines.append("> **Status mặc định:** PENDING (chưa ingest)")
    lines.append("> **Generated:** 2026-05-26 | **Convention v2:** lowercase_snake_case")
    lines.append("> **Hash check:** 2026-05-26 — Duplicate confirmed bằng MD5")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Tóm tắt theo Category")
    lines.append("")
    lines.append("| Category | Prefix | Số lượng |")
    lines.append("| :--- | :--- | :---: |")
    
    for prefix, name in CATEGORY_MAP.items():
        lines.append(f"| {name} | {prefix} | {cat_counts[prefix]} |")
    
    lines.append(f"| **TỔNG** | | **{total_active}** |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Ghi Chú")
    lines.append("")
    lines.append("- **`arch_thinking_in_systems`** đã được đăng ký và ingest (xem `MASTER_SOURCE_INDEX.md`)")
    lines.append("- Files không có prefix = bản tên cũ duplicate → **bỏ qua, không cấp source_id**")
    lines.append("- `empty.pdf`, `sample.pdf` → **bỏ qua** (file test)")
    lines.append("")
    lines.append("### ✅ Kết Quả Hash Check (MD5 — 2026-05-26)")
    lines.append("")
    lines.append("| File A | File B | MD5 | Kết quả |")
    lines.append("| :--- | :--- | :--- | :--- |")
    lines.append("| `FA_Storytelling_with_Data_Visualization_v1_.pdf` | `VIZ_FA_Storytelling_with_Data_Visualization_v1_.pdf` | `2DE18A03` = `2DE18A03` | ✅ **CÙNG 1 FILE** — giữ `fa_storytelling_with_data_viz`, loại VIZ_FA |")
    lines.append("| `STAT_OReily_Practical_Statistics_for_Data_Scientists.pdf` | `STAT_Practical_Statistics_for_Data_Scientists.pdf` | `9259B485` ≠ `1CDB0825` | ❌ **2 FILE KHÁC** — cấp 2 source_id riêng |")
    lines.append("")
    lines.append("---")

    # Ghi nhận các Category
    for prefix, name in CATEGORY_MAP.items():
        lines.append("")
        lines.append(f"## {prefix} — {name}")
        lines.append("")
        lines.append("| source_id | Tên File | Status |")
        lines.append("| :--- | :--- | :--- |")
        
        # Lọc các nguồn thuộc category này
        cat_sources = {k: v for k, v in registered_sources.items() if v["category"] == prefix}
        # Sắp xếp theo source_id tăng dần cho gọn đẹp
        for source_id in sorted(cat_sources.keys()):
            filename = cat_sources[source_id]["filename"]
            status = cat_sources[source_id]["status"]
            # Format gạch ngang cho các file đã ingest
            if "ingest" in status.lower() or "đã" in status.lower():
                lines.append(f"| ~~`{source_id}`~~ | ~~{filename}~~ | ✅ {status} |")
            else:
                lines.append(f"| `{source_id}` | {filename} | {status} |")
        lines.append("")
        lines.append("---")

    # Ghi nhận mục Bị Loại
    lines.append("")
    lines.append("## Files Bị Loại (Không Cấp source_id)")
    lines.append("")
    lines.append("| Tên File | Lý do |")
    lines.append("| :--- | :--- |")
    for filename in sorted(excluded_files.keys()):
        reason = excluded_files[filename]
        lines.append(f"| `{filename}` | {reason} |")
    lines.append("")

    with open(registry_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[SUCCESS] Đã cập nhật thành công {registry_path}")

def sync():
    print("==================================================")
    print("BẮT ĐẦU ĐỒNG BỘ HÓA NGUỒN (sync_pending_sources.py)")
    print("==================================================")
    
    if not os.path.exists(PENDING_DIR):
        print(f"[ERROR] Thư mục {PENDING_DIR} không tồn tại!")
        return

    # 1. Quét các file PDF thực tế trong thư mục
    actual_files = [f for f in os.listdir(PENDING_DIR) if f.endswith(".pdf") and f not in IGNORE_FILES]
    print(f"[INFO] Tìm thấy {len(actual_files)} file PDF thực tế trong sources-pending.")

    # 2. Parse Registry hiện tại
    registered_sources, excluded_files = parse_registry(REGISTRY_PATH)
    print(f"[INFO] Registry hiện tại có {len(registered_sources)} nguồn đã đăng ký, {len(excluded_files)} file bị loại.")

    # 3. Tính toán hash MD5 của các file PDF thực tế để so sánh trùng lặp
    file_hashes = {}
    print("[INFO] Đang tính toán mã MD5 cho các file PDF thực tế...")
    for filename in actual_files:
        filepath = os.path.join(PENDING_DIR, filename)
        md5 = calculate_md5(filepath)
        if md5:
            file_hashes[filename] = md5

    # Phân nhóm các file PDF thực tế thành file chuẩn (có prefix) và file không chuẩn (không prefix)
    prefixed_files = []
    unprefixed_files = []
    for filename in actual_files:
        # Check xem file có prefix thuộc CATEGORY_MAP không
        has_prefix = False
        for prefix in CATEGORY_MAP.keys():
            if filename.startswith(prefix + "_"):
                has_prefix = True
                break
        
        # Trường hợp ngoại lệ được đăng ký chính thức: [Description]-Building-Simple-NotebookLM.pdf hay Operating-Systems-Principles .pdf
        # Các file này đã được chuẩn hoá trong registry và có source_id tương ứng
        if has_prefix or filename in {"[Description]-Building-Simple-NotebookLM.pdf", "Operating-Systems-Principles .pdf", "Data Analytics - Data Science, Data Analysis and Predictive Analytics for Business - Daniel Covington.pdf"}:
            prefixed_files.append(filename)
        else:
            unprefixed_files.append(filename)

    print(f"[INFO] Phân loại: {len(prefixed_files)} file chuẩn, {len(unprefixed_files)} file không chuẩn (cũ).")

    # 4. Tìm kiếm các trùng lặp (Duplicate Detection)
    # Lập bản đồ hash -> file chuẩn đại diện
    hash_to_prefixed_file = {}
    for filename in prefixed_files:
        h = file_hashes.get(filename)
        if h:
            # Nếu chưa có file nào sở hữu hash này, hoặc file hiện tại ngắn/đẹp hơn
            if h not in hash_to_prefixed_file:
                hash_to_prefixed_file[h] = filename

    # 5. Cập nhật Registry logic:
    new_registrations = 0
    new_exclusions = 0
    missing_files = []
    
    # a. Đánh dấu các source_id bị thiếu (đăng ký nhưng file không tồn tại)
    active_filenames = set(actual_files)
    for source_id, info in list(registered_sources.items()):
        if info["filename"] not in active_filenames:
            print(f"[WARNING] File của source_id '{source_id}' không tồn tại: {info['filename']}")
            # Nếu đã ingest thì giữ nguyên, ngược lại đánh dấu MISSING
            if "ingest" not in info["status"].lower() and "đã" not in info["status"].lower():
                registered_sources[source_id]["status"] = "MISSING"
                missing_files.append(info["filename"])

    # b. Duyệt các file chuẩn để đảm bảo đã đăng ký hoặc đăng ký mới
    registered_filenames = {info["filename"]: source_id for source_id, info in registered_sources.items()}
    
    for filename in prefixed_files:
        if filename in registered_filenames:
            # File đã được đăng ký, kiểm tra xem có thay đổi gì không
            source_id = registered_filenames[filename]
            if registered_sources[source_id]["status"] == "MISSING":
                registered_sources[source_id]["status"] = "PENDING"
                print(f"[INFO] Khôi phục file missing: {filename} -> PENDING")
        else:
            # File chuẩn CHƯA được đăng ký -> Cần đăng ký mới
            # Xác định Category
            category = "MISC"
            for prefix in CATEGORY_MAP.keys():
                if filename.startswith(prefix + "_"):
                    category = prefix
                    break
            
            # Xử lý trường hợp ngoại lệ
            if filename == "Data Analytics - Data Science, Data Analysis and Predictive Analytics for Business - Daniel Covington.pdf":
                category = "DSML"
            elif filename == "Operating-Systems-Principles .pdf":
                category = "SYS"
            
            source_id = normalize_source_id(filename)
            
            # Check trùng hash với file chuẩn đã có
            my_hash = file_hashes.get(filename)
            is_duplicate = False
            for dup_filename, dup_hash in file_hashes.items():
                if dup_filename != filename and dup_hash == my_hash and dup_filename in registered_filenames:
                    dup_source_id = registered_filenames[dup_filename]
                    reason = f"DUPLICATE — MD5 = {dup_filename} -> dùng `{dup_source_id}`"
                    excluded_files[filename] = reason
                    new_exclusions += 1
                    is_duplicate = True
                    print(f"[DUPLICATE] Phát hiện file chuẩn trùng hash: {filename} trùng {dup_filename}")
                    break
            
            if not is_duplicate:
                registered_sources[source_id] = {
                    "filename": filename,
                    "status": "PENDING",
                    "category": category
                }
                registered_filenames[filename] = source_id
                new_registrations += 1
                print(f"[REGISTER] Đăng ký nguồn mới: {source_id} -> {filename} (Category: {category})")

    # c. Duyệt các file không chuẩn (cũ) để loại bỏ
    for filename in unprefixed_files:
        if filename in excluded_files:
            continue  # Đã có trong danh sách loại
            
        my_hash = file_hashes.get(filename)
        # So sánh hash với các file chuẩn đại diện
        found_match = False
        if my_hash in hash_to_prefixed_file:
            matched_prefixed = hash_to_prefixed_file[my_hash]
            matched_source_id = registered_filenames.get(matched_prefixed, "unknown")
            reason = f"Tên cũ → đã có `{matched_source_id}`"
            excluded_files[filename] = reason
            new_exclusions += 1
            print(f"[EXCLUDE] Loại file tên cũ (trùng hash): {filename} -> trùng {matched_prefixed}")
            found_match = True
        
        if not found_match:
            # Không trùng hash nhưng là file không chuẩn (không có prefix)
            reason = "Tên cũ (chưa đổi tên / thiếu prefix) -> Bỏ qua, yêu cầu đổi tên"
            excluded_files[filename] = reason
            new_exclusions += 1
            print(f"[EXCLUDE] Loại file thiếu prefix chuẩn: {filename}")

    # 6. Ghi lại Registry và in báo cáo
    write_registry(REGISTRY_PATH, registered_sources, excluded_files)
    
    print("\n==================================================")
    print("BÁO CÁO KẾT QUẢ ĐỒNG BỘ")
    print("==================================================")
    print(f"- Số lượng đăng ký mới: {new_registrations}")
    print(f"- Số lượng file bị loại thêm mới: {new_exclusions}")
    print(f"- Số lượng file missing: {len(missing_files)}")
    print(f"- Tổng số nguồn đang đăng ký hoạt động: {len(registered_sources)}")
    print(f"- Tổng số file bị loại trong registry: {len(excluded_files)}")
    print("==================================================")

if __name__ == "__main__":
    sync()
