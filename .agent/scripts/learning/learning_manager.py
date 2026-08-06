#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
learning_manager.py — Core Engine quản lý học tập và Spaced Repetition cho NoteBookLLM_Br.
"""

from __future__ import annotations
import os
import sys
import sqlite3
import argparse
import re
import hashlib
from datetime import datetime, timedelta

# Fix encoding for Windows terminal
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

# Cấu hình đường dẫn
ROOT_DIR = os.getenv(
    "NOTEBOOKLLM_ROOT",
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
)
WIKI_DIR = os.getenv("WIKI_ROOT_PATH", os.path.join(ROOT_DIR, "3-resources", "wiki"))
DB_PATH  = os.getenv("WIKI_DB_PATH", os.path.join(WIKI_DIR, "wiki_brain.db"))
LEARNING_DIR = os.path.join(ROOT_DIR, "workspaces", "learning", "dashboard")

def get_db_connection() -> sqlite3.Connection:
    return sqlite3.connect(DB_PATH)

def init_db():
    """Khởi tạo và nâng cấp database schema an toàn."""
    print("Initializing Learning Schema in SQLite...")
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 1. Thêm các cột SM-2 và trạng thái học tập vào bảng atoms
    columns_to_add = {
        "learning_status": "TEXT DEFAULT 'TODO'",
        "next_review": "TEXT",
        "ease_factor": "REAL DEFAULT 2.5",
        "repetition_interval": "INTEGER DEFAULT 0",
        "repetition_count": "INTEGER DEFAULT 0"
    }
    
    # Lấy danh sách cột hiện tại
    cursor.execute("PRAGMA table_info(atoms)")
    existing_cols = {row[1] for row in cursor.fetchall()}
    
    for col_name, col_def in columns_to_add.items():
        if col_name not in existing_cols:
            print(f"  Adding column {col_name} to table atoms...")
            cursor.execute(f"ALTER TABLE atoms ADD COLUMN {col_name} {col_def}")
            
    # 2. Tạo bảng learning_history để lưu lịch sử ôn tập
    print("  Creating table learning_history if not exists...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS learning_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            atom_id TEXT NOT NULL,
            status_before TEXT NOT NULL,
            status_after TEXT NOT NULL,
            retention_score REAL DEFAULT 0.0,
            practice_count INTEGER DEFAULT 0,
            reviewed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            notes TEXT,
            FOREIGN KEY(atom_id) REFERENCES atoms(file_id)
        );
    """)
    
    conn.commit()
    conn.close()
    print("Learning Schema initialized successfully.")

def extract_source_prefix(source_id: str) -> str:
    """
    Trích xuất prefix viết hoa thông minh từ source_id.
    Ví dụ: SOURCE_ARCH_TIS_Thinking_in_Systems -> ARCH_TIS
    SOURCE_TIS_Stock -> TIS
    """
    parts = source_id.split("_")
    # Lấy các phần tử viết hoa hoàn toàn sau phần tử đầu tiên (SOURCE)
    upper_parts = []
    for p in parts[1:]:
        if p.isupper() and p != "SOURCE":
            upper_parts.append(p)
        else:
            break
    if upper_parts:
        return "_".join(upper_parts)
    return parts[-1] if len(parts) > 1 else source_id

def find_atom_file(atom_id: str) -> str | None:
    """Tìm đường dẫn tệp markdown vật lý của Atom."""
    scan_folders = ["concepts", "entities", "sources", "comparisons", "synthesis", "review_queue", "session_insights"]
    for folder in scan_folders:
        path = os.path.join(WIKI_DIR, folder, f"{atom_id}.md")
        if os.path.exists(path):
            return path
    return None

def update_markdown_frontmatter(file_path: str, status: str, next_review: str = None) -> bool:
    """Surgical Diff cập nhật YAML Frontmatter của file markdown."""
    try:
        with open(file_path, "r", encoding="utf-8-sig") as f:
            content = f.read()
        
        # Tìm khối frontmatter
        fm_match = re.search(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL | re.MULTILINE)
        if not fm_match:
            print(f"  [Error] No valid frontmatter found in {file_path}")
            return False
        
        fm_content = fm_match.group(1)
        
        # Cập nhật learning_status
        if "learning_status:" in fm_content:
            fm_content = re.sub(r"^learning_status:\s*.*$", f"learning_status: \"{status}\"", fm_content, flags=re.MULTILINE)
        else:
            fm_content += f"\nlearning_status: \"{status}\""
            
        # Cập nhật next_review_date
        if next_review:
            if "next_review_date:" in fm_content:
                fm_content = re.sub(r"^next_review_date:\s*.*$", f"next_review_date: \"{next_review}\"", fm_content, flags=re.MULTILINE)
            else:
                fm_content += f"\nnext_review_date: \"{next_review}\""
                
        # Cập nhật last_reviewed
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if "last_reviewed:" in fm_content:
            fm_content = re.sub(r"^last_reviewed:\s*.*$", f"last_reviewed: \"{now_str}\"", fm_content, flags=re.MULTILINE)
        else:
            fm_content += f"\nlast_reviewed: \"{now_str}\""
            
        # Chuẩn hóa khoảng trống thừa và ghép lại
        new_fm = f"---\n{fm_content.strip()}\n---\n"
        new_content = content[:fm_match.start()] + new_fm + content[fm_match.end():]
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    except Exception as e:
        print(f"  [Error] Failed to update markdown {file_path}: {e}")
        return False

def calculate_sm2(q: int, ease_factor: float, repetition_interval: int, repetition_count: int) -> tuple[float, int, int]:
    """
    Thuật toán SuperMemo SM-2 cho Spaced Repetition.
    q: chất lượng ôn tập (0-5)
    ease_factor: độ dễ (mặc định 2.5)
    repetition_interval: khoảng thời gian ôn tập hiện tại (số ngày)
    repetition_count: số lần ôn tập thành công liên tiếp
    Trợ giúp q:
    0: Hoàn toàn quên
    1: Quên nhưng nhận ra khi thấy đáp án
    2: Nhớ mang máng, mất nhiều công recall
    3: Nhớ nhưng tốn sức recall
    4: Nhớ tốt sau một chút suy nghĩ
    5: Nhớ hoàn hảo lập tức
    """
    if q >= 3:
        if repetition_count == 0:
            repetition_interval = 1
        elif repetition_count == 1:
            repetition_interval = 6
        else:
            repetition_interval = round(repetition_interval * ease_factor)
        repetition_count += 1
    else:
        repetition_count = 0
        repetition_interval = 1
        
    ease_factor = ease_factor + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
    ease_factor = max(1.3, ease_factor)
    
    return ease_factor, repetition_interval, repetition_count

def extract_existing_goal(source_id: str) -> str:
    """Trích xuất mục tiêu học tập hiện tại từ file Lộ trình để bảo toàn khi tái sinh."""
    path_file = os.path.join(LEARNING_DIR, "paths", f"LEARNING_PATH_{source_id}.md")
    if os.path.exists(path_file):
        try:
            with open(path_file, "r", encoding="utf-8") as f:
                content = f.read()
                # Tìm dòng mục tiêu học tập của AN: *mục tiêu*
                match = re.search(r"\*\*Mục tiêu học tập của AN\*\*:\s*\*([^*]+)\*", content)
                if match:
                    return match.group(1).strip()
        except Exception:
            pass
    return "Thiet ke kien truc he thong phan mem"  # Mặc định mục tiêu của AN

def update_status(atom_id: str, status: str, notes: str = None):
    """Cập nhật trạng thái học tập của Atom."""
    status = status.upper()
    if status not in ['TODO', 'IN_PROGRESS', 'LEARNED', 'MASTERED']:
        print(f"Error: Invalid learning status '{status}'. Must be one of TODO, IN_PROGRESS, LEARNED, MASTERED.")
        return
        
    file_path = find_atom_file(atom_id)
    if not file_path:
        print(f"Error: Atom file for '{atom_id}' not found in Vault.")
        return
        
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Lấy thông tin hiện tại trong DB
    cursor.execute("SELECT learning_status, ease_factor, repetition_interval, repetition_count FROM atoms WHERE file_id = ?", (atom_id,))
    res = cursor.fetchone()
    
    if not res:
        print(f"Warning: Atom '{atom_id}' not found in sqlite database. Running DB rebuild first is recommended.")
        # Chèn tạm thời nếu thiếu
        cursor.execute("INSERT OR IGNORE INTO atoms (file_id, title, type, status) VALUES (?, ?, 'Concept', 'DRAFT')", (atom_id, atom_id.replace("_", " ")))
        current_status = 'TODO'
        ef, rep_int, rep_count = 2.5, 0, 0
    else:
        current_status = res[0] if res[0] else 'TODO'
        ef = res[1] if res[1] is not None else 2.5
        rep_int = res[2] if res[2] is not None else 0
        rep_count = res[3] if res[3] is not None else 0
        
    # Xác định chất lượng ôn tập (quality q) cho SM-2
    # TODO = 0, IN_PROGRESS = 2, LEARNED = 4, MASTERED = 5
    q_map = {'TODO': 0, 'IN_PROGRESS': 2, 'LEARNED': 4, 'MASTERED': 5}
    q = q_map.get(status, 0)
    
    # Tính toán khoảng ôn tập kế tiếp
    new_ef, new_rep_int, new_rep_count = calculate_sm2(q, ef, rep_int, rep_count)
    next_review_date = (datetime.now() + timedelta(days=new_rep_int)).strftime("%Y-%m-%d")
    
    # Cập nhật SQLite
    cursor.execute("""
        UPDATE atoms 
        SET learning_status = ?, next_review = ?, ease_factor = ?, repetition_interval = ?, repetition_count = ?
        WHERE file_id = ?
    """, (status, next_review_date, new_ef, new_rep_int, new_rep_count, atom_id))
    
    # Ghi log lịch sử học tập
    cursor.execute("""
        INSERT INTO learning_history (atom_id, status_before, status_after, retention_score, notes)
        VALUES (?, ?, ?, ?, ?)
    """, (atom_id, current_status, status, q / 5.0, notes if notes else ""))
    
    conn.commit()
    conn.close()
    
    # Đồng bộ ra Markdown Frontmatter
    sync_ok = update_markdown_frontmatter(file_path, status, next_review_date)
    
    print(f"Successfully updated {atom_id}: {current_status} -> {status}")
    print(f"  SM-2 metrics: Ease Factor: {new_ef:.2f} | Interval: {new_rep_int} days | Next Review: {next_review_date}")
    if sync_ok:
        print(f"  YAML Frontmatter in markdown file synchronized.")
        
    # Tự động render HTML Reader ngầm nếu có file Learning Pack tương ứng
    # Quy tắc: Quét xem source_id của Atom này là gì bằng cách tìm prefix trong file_id
    # Ví dụ: CONCEPT_TIS_Stock -> prefix là TIS -> Nguồn là ARCH_TIS
    prefix_match = re.search(r"^[A-Z]+_([A-Z0-9]+)_", atom_id)
    if prefix_match:
        source_prefix = prefix_match.group(1)
        # Tìm kiếm source_id tương ứng
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT file_id FROM atoms WHERE type = 'Source' AND file_id LIKE ?", (f"%{source_prefix}%",))
        source_res = cursor.fetchone()
        conn.close()
        
        if source_res:
            source_id = source_res[0]
            pack_path = os.path.join(LEARNING_DIR, "packs", f"LEARNING_PACK_{source_id}.md")
            if os.path.exists(pack_path):
                html_output_dir = os.path.join(LEARNING_DIR, "packs", "html")
                os.makedirs(html_output_dir, exist_ok=True)
                html_path = os.path.join(html_output_dir, f"LEARNING_PACK_{source_id}.html")
                print(f"  [Auto-Render] Generating background HTML Reader for {source_id}...")
                render_script = os.path.join(ROOT_DIR, "scripts", "learning", "render_learning_pack.py")
                if os.path.exists(render_script):
                    import subprocess
                    subprocess.run([
                        sys.executable, render_script,
                        "--input", pack_path,
                        "--output", html_path
                    ], capture_output=True)
                    print(f"  [Auto-Render] HTML Reader generated: file:///{html_path.replace(os.sep, '/')}")
            
            # Tự động đồng bộ hóa Lộ trình học tập cá nhân hóa & Dashboard
            goal = extract_existing_goal(source_id)
            print(f"  [Auto-Sync] Re-generating personalized path and dashboard to keep in sync...")
            generate_path(source_id, goal)

def draw_mermaid_progress_bar(percent: float) -> str:
    """Tạo thanh tiến trình Mermaid Pie/Bar."""
    filled = int(percent / 10)
    empty = 10 - filled
    bar = "█" * filled + "░" * empty
    return f"`{bar}` {percent:.1f}%"

def generate_dashboard():
    """Quét toàn bộ tiến độ và sinh file LEARNING_DASHBOARD.md."""
    print("Generating Learning Dashboard...")
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 1. Tìm tất cả các Source Atoms để tính tiến độ theo từng nguồn
    cursor.execute("SELECT file_id, title FROM atoms WHERE type = 'Source' AND status != 'DEPRECATED'")
    sources = cursor.fetchall()
    
    dashboard_lines = []
    dashboard_lines.append("# 📊 HỆ THỐNG GIÁM SÁT TIẾN ĐỘ HỌC TẬP — LEARNING DASHBOARD")
    dashboard_lines.append(f"> [!NOTE]\n> Cập nhật tự động vào: **{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}**.\n> File này chứa bảng theo dõi tiến độ thời gian thực (Mermaid + DataviewJS) và hàng đợi ôn tập thông minh (SM-2 Spaced Repetition).")
    dashboard_lines.append("")
    
    dashboard_lines.append("## 📈 Tiến độ học tập theo Nguồn tri thức")
    dashboard_lines.append("| Nguồn học tập | Tiến trình (%) | Lộ trình | Giao diện đọc Interactive HTML |")
    dashboard_lines.append("| :--- | :--- | :--- | :--- |")
    
    source_progress_data = {}
    
    for src_id, src_title in sources:
        # Lấy tất cả các Concept Atoms liên kết với Source này
        # Dựa trên quan hệ trong bảng edges hoặc lọc theo tiền tố (convention)
        # Sử dụng edges để đảm bảo tính chuẩn xác của đồ thị
        cursor.execute("""
            SELECT a.file_id, a.learning_status 
            FROM atoms a
            JOIN edges e ON a.file_id = e.source_id
            WHERE e.target_id = ? AND a.type = 'Concept' AND a.status != 'DEPRECATED'
        """, (src_id,))
        concepts = cursor.fetchall()
        
        # Fallback: nếu edges rỗng, thử lọc theo tiền tố source (ví dụ CONCEPT_TIS_*)
        if not concepts:
            # Tìm prefix từ src_id, ví dụ SOURCE_ARCH_TIS -> prefix ARCH_TIS
            prefix = extract_source_prefix(src_id)
            cursor.execute("""
                SELECT file_id, learning_status 
                FROM atoms 
                WHERE type = 'Concept' AND file_id LIKE ? AND status != 'DEPRECATED'
            """, (f"%_{prefix}_%",))
            concepts = cursor.fetchall()
            
        if not concepts:
            continue
            
        total_concepts = len(concepts)
        todo_c = sum(1 for c in concepts if c[1] == 'TODO' or c[1] is None)
        ip_c = sum(1 for c in concepts if c[1] == 'IN_PROGRESS')
        learned_c = sum(1 for c in concepts if c[1] == 'LEARNED')
        mastered_c = sum(1 for c in concepts if c[1] == 'MASTERED')
        
        # Trọng số: TODO = 0%, IN_PROGRESS = 25%, LEARNED = 75%, MASTERED = 100%
        total_score = (todo_c * 0.0) + (ip_c * 0.25) + (learned_c * 0.75) + (mastered_c * 1.0)
        progress_pct = (total_score / total_concepts) * 100.0 if total_concepts > 0 else 0.0
        
        source_progress_data[src_id] = progress_pct
        
        # Tạo liên kết cục bộ (sử dụng đường dẫn tương đối để Obsidian mở trực tiếp trong app, không nhảy ra IDE)
        path_link = f"[📝 Mở Lộ trình](paths/LEARNING_PATH_{src_id}.md)"
        html_link = f"[🌐 Mở HTML Reader](file:///{os.path.join(LEARNING_DIR, 'packs', 'html', f'LEARNING_PACK_{src_id}.html').replace(os.sep, '/')})"
        
        # Nếu chưa tồn tại file, ẩn link
        if not os.path.exists(os.path.join(LEARNING_DIR, "paths", f"LEARNING_PATH_{src_id}.md")):
            path_link = "*Chưa tạo lộ trình*"
        if not os.path.exists(os.path.join(LEARNING_DIR, "packs", "html", f"LEARNING_PACK_{src_id}.html")):
            html_link = "*Chưa tạo HTML*"
            
        progress_bar = draw_mermaid_progress_bar(progress_pct)
        dashboard_lines.append(f"| **{src_title}** ({src_id}) | {progress_bar} | {path_link} | {html_link} |")
        
    dashboard_lines.append("")
    
    # 2. Sinh biểu đồ Mermaid Pie chart tổng thể
    if source_progress_data:
        dashboard_lines.append("### 📊 Biểu đồ so sánh Tiến độ các nguồn")
        dashboard_lines.append("```mermaid")
        dashboard_lines.append("pie title Tiến độ học tập các nguồn tri thức")
        for src_id, pct in source_progress_data.items():
            # Rút gọn tên
            name = src_id.replace("SOURCE_", "")
            dashboard_lines.append(f'    "{name} (đã học)" : {pct:.1f}')
            dashboard_lines.append(f'    "{name} (còn lại)" : {100.0 - pct:.1f}')
        dashboard_lines.append("```")
        dashboard_lines.append("")

    # 3. Spaced Repetition Queue (SM-2)
    dashboard_lines.append("## 🔄 Hàng đợi Ôn tập Hôm nay (Spaced Repetition Queue)")
    dashboard_lines.append("Áp dụng thuật toán **SuperMemo SM-2** để tối ưu hóa trí nhớ dài hạn:")
    dashboard_lines.append("")
    dashboard_lines.append("| Concept Atom | Trạng thái học | Ngày ôn tập kế tiếp | Ease Factor | Khoảng cách (ngày) | Lộ trình nguồn |")
    dashboard_lines.append("| :--- | :---: | :---: | :---: | :---: | :--- |")
    
    today_str = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("""
        SELECT file_id, learning_status, next_review, ease_factor, repetition_interval 
        FROM atoms 
        WHERE type = 'Concept' AND learning_status IN ('IN_PROGRESS', 'LEARNED') AND status != 'DEPRECATED'
        ORDER BY next_review ASC
        LIMIT 10
    """)
    due_atoms = cursor.fetchall()
    
    if due_atoms:
        for fid, status, next_rev, ef, interval in due_atoms:
            # Tìm xem atom này thuộc nguồn nào
            prefix_match = re.search(r"^[A-Z]+_([A-Z0-9]+)_", fid)
            src_link = "Liên kết tự do"
            if prefix_match:
                source_prefix = prefix_match.group(1)
                cursor.execute("SELECT file_id, title FROM atoms WHERE type = 'Source' AND file_id LIKE ?", (f"%{source_prefix}%",))
                s_res = cursor.fetchone()
                if s_res:
                    src_link = f"[{s_res[1]}](paths/LEARNING_PATH_{s_res[0]}.md)"
            
            is_due = "⚠️ **Hôm nay!**" if next_rev <= today_str else f"`{next_rev}`"
            dashboard_lines.append(f"| [[{fid}]] | `{status}` | {is_due} | `{ef:.2f}` | `{interval}` | {src_link} |")
    else:
        dashboard_lines.append("| *Tuyệt vời!* | *Không có concept nào* | *cần ôn tập hôm nay* | *—* | *—* | *—* |")
        
    dashboard_lines.append("")
    
    # 4. Tích hợp DataviewJS và Heatmap Tracker cho Obsidian
    dashboard_lines.append("## 🔌 Obsidian DataviewJS Integration (Thời gian thực)")
    dashboard_lines.append("> [!TIP]\n> Nếu AN đã cài Community Plugin **Dataview** và **Heatmap Tracker**, Obsidian sẽ tự động vẽ biểu đồ nhiệt tiến trình commit học tập cực đẹp giống hệt GitHub:")
    dashboard_lines.append("")
    
    dashboard_lines.append("```dataviewjs")
    dashboard_lines.append("""const calendarData = {
    year: new Date().getFullYear(),
    colors: {
        blue: ["#eff6ff", "#dbeafe", "#bfdbfe", "#60a5fa", "#1d4ed8"],
    },
    entries: []
}

// Quét toàn bộ Concept Atoms có ghi nhận thực hành MASTERED hoặc LEARNED
for (let page of dv.pages('"3-resources/wiki"')) {
    if (page.learning_status && page.last_reviewed) {
        let intensity = 2;
        if (page.learning_status === "MASTERED") intensity = 4;
        else if (page.learning_status === "LEARNED") intensity = 3;
        
        calendarData.entries.push({
            date: page.last_reviewed.split(" ")[0],
            intensity: intensity,
            content: page.learning_status + ": " + page.file.name
        });
    }
}

if (typeof renderHeatmapCalendar !== "undefined") {
    renderHeatmapCalendar(this.container, calendarData);
} else {
    dv.paragraph("⚠️ *Lưu ý: Để hiển thị biểu đồ nhiệt (Heatmap) dạng ô vuông màu sắc giống GitHub, bạn hãy cài đặt plugin **Heatmap Calendar** trong Obsidian settings.*");
    
    // Fallback: Vẽ một bảng danh sách commit học tập đơn giản nhưng đẹp mắt
    if (calendarData.entries.length > 0) {
        dv.header(3, "📅 Nhật ký thực hành gần đây");
        dv.table(
            ["Ngày học", "Trạng thái", "Tên Concept Atom"], 
            calendarData.entries.map(e => [e.date, e.content.split(": ")[0], e.content.split(": ")[1]])
        );
    } else {
        dv.paragraph("*Chưa có lịch sử học tập nào được ghi nhận dưới dạng LEARNED hoặc MASTERED.*");
    }
}
```""")
    
    conn.close()
    
    # Ghi file dashboard
    os.makedirs(LEARNING_DIR, exist_ok=True)
    dashboard_path = os.path.join(LEARNING_DIR, "LEARNING_DASHBOARD.md")
    with open(dashboard_path, "w", encoding="utf-8") as f:
        f.write("\n".join(dashboard_lines))
        
    print(f"Learning Dashboard generated successfully at: {dashboard_path}")

def generate_path(source_id: str, goal: str):
    """Tự động phân tích quan hệ edges để xếp lộ trình học tuần tự cá hiện hóa."""
    print(f"Generating personalized path for {source_id} with goal: '{goal}'...")
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Kiểm tra xem source có tồn tại không
    cursor.execute("SELECT title FROM atoms WHERE file_id = ? AND type = 'Source'", (source_id,))
    src_res = cursor.fetchone()
    if not src_res:
        print(f"Error: Source ID '{source_id}' not found in database.")
        conn.close()
        return
        
    src_title = src_res[0]
    
    # Lấy toàn bộ các Concept Atoms liên kết với Source này
    cursor.execute("""
        SELECT a.file_id, a.title, a.learning_status 
        FROM atoms a
        JOIN edges e ON a.file_id = e.source_id
        WHERE e.target_id = ? AND a.type = 'Concept' AND a.status != 'DEPRECATED'
    """, (source_id,))
    concepts = cursor.fetchall()
    
    if not concepts:
        # Fallback convention lọc theo prefix
        prefix = extract_source_prefix(source_id)
        cursor.execute("""
            SELECT file_id, title, learning_status 
            FROM atoms 
            WHERE type = 'Concept' AND file_id LIKE ? AND status != 'DEPRECATED'
        """, (f"%_{prefix}_%",))
        concepts = cursor.fetchall()
        
    if not concepts:
        print(f"Warning: No concepts found linked to {source_id}. Cannot generate path.")
        conn.close()
        return
        
    # Phân tích quan hệ phụ thuộc (edges) giữa các concepts này
    concept_ids = {c[0] for c in concepts}
    concept_map = {c[0]: c for c in concepts}
    
    dependencies: dict[str, list[str]] = {cid: [] for cid in concept_ids}
    
    # Truy vấn bảng edges tìm quan hệ MENTIONS/DEPENDS giữa các concepts này
    for cid in concept_ids:
        cursor.execute("""
            SELECT target_id FROM edges 
            WHERE source_id = ? AND target_id IN (
                SELECT file_id FROM atoms WHERE type = 'Concept'
            )
        """, (cid,))
        edges = cursor.fetchall()
        for edge in edges:
            target = edge[0]
            if target in concept_ids and target != cid:
                dependencies[cid].append(target)
                
    conn.close()
    
    # Sắp xếp Topological Sort rút gọn (sắp xếp tiên quyết)
    ordered_concepts = []
    visited = set()
    temp_visited = set()
    
    def visit(node):
        if node in temp_visited:
            # Phát hiện chu trình (cycle), bỏ qua để tránh loop vô hạn
            return
        if node not in visited:
            temp_visited.add(node)
            for dep in dependencies.get(node, []):
                visit(dep)
            temp_visited.remove(node)
            visited.add(node)
            ordered_concepts.append(node)
            
    for cid in concept_ids:
        if cid not in visited:
            visit(cid)
            
    # Xây dựng nội dung lộ trình cá nhân hóa tuần tự
    src_abs_path = os.path.join(WIKI_DIR, 'sources', f'{source_id}.md')
    src_rel_path = os.path.relpath(src_abs_path, start=os.path.join(LEARNING_DIR, 'paths')).replace(os.sep, '/')
    
    path_lines = []
    path_lines.append(f"# 🗺️ LỘ TRÌNH HỌC TẬP CÁ NHÂN HÓA: {src_title.upper()}")
    path_lines.append(f"> [!IMPORTANT]\n> **Mục tiêu học tập của AN**: *{goal}*\n> **Nguồn**: [{src_title}]({src_rel_path})\n> **HTML Reader**: [🌐 Click để mở giao diện đọc HTML siêu đẹp trên trình duyệt](file:///{os.path.join(LEARNING_DIR, 'packs', 'html', f'LEARNING_PACK_{source_id}.html').replace(os.sep, '/')})")
    path_lines.append("")
    
    path_lines.append("## 📈 Bản đồ lộ trình học tập tuần tự (Prerequisite Progression)")
    path_lines.append("Dưới đây là thứ tự học được sắp xếp khoa học từ cơ bản đến nâng cao dựa trên mối tương quan tri thức:")
    path_lines.append("")
    path_lines.append("```mermaid")
    path_lines.append("graph TD")
    
    # Vẽ sơ đồ Mermaid dependencies
    for cid in ordered_concepts:
        clean_name = cid.replace("CONCEPT_", "").replace(source_id.replace("SOURCE_", "") + "_", "")
        path_lines.append(f'    {clean_name}["{concept_map[cid][1]}"]')
        for dep in dependencies.get(cid, []):
            clean_dep = dep.replace("CONCEPT_", "").replace(source_id.replace("SOURCE_", "") + "_", "")
            path_lines.append(f"    {clean_dep} --> {clean_name}")
            
    path_lines.append("```")
    path_lines.append("")
    
    path_lines.append("## 👣 Từng bước làm chủ kiến thức (Checklist)")
    path_lines.append("AN hãy tích chọn hoàn thành lần lượt để cập nhật tiến độ tự động:")
    path_lines.append("")
    
    for index, cid in enumerate(ordered_concepts, 1):
        status = concept_map[cid][2] if concept_map[cid][2] else 'TODO'
        status_icons = {
            'TODO': '⚪ TODO',
            'IN_PROGRESS': '🟡 ĐANG HỌC LÝ THUYẾT (25%)',
            'LEARNED': '🟢 ĐÃ HIỂU LÝ THUYẾT (75%)',
            'MASTERED': '🔥 ĐÃ THỰC HÀNH MASTER (100%)'
        }
        icon = status_icons.get(status, '⚪ TODO')
        
        path_lines.append(f"### Bước {index}: {concept_map[cid][1]}")
        atom_abs_path = find_atom_file(cid)
        if atom_abs_path:
            path_lines.append(f"- **Mã tri thức**: [[{cid}]]")
        else:
            path_lines.append(f"- **Mã tri thức**: `{cid}` (File not found)")
        path_lines.append(f"- **Trạng thái hiện tại**: `{icon}`")
        
        # Gợi ý dựa trên mục tiêu người dùng
        path_lines.append(f"- **Định hướng ứng dụng cho mục tiêu**: *Hãy liên hệ lý thuyết {concept_map[cid][1]} trực tiếp tới '{goal}' khi làm bài tập thực hành.*")
        path_lines.append("")
        
    path_lines.append("## 🚀 Hướng dẫn thực thi lệnh cập nhật tiến độ")
    path_lines.append("Khi AN hoàn thành bất kỳ bước nào, hãy gõ câu lệnh sau trực tiếp với Antigravity hoặc chạy ngầm để cập nhật:")
    path_lines.append("```powershell")
    path_lines.append(f"# Ví dụ cập nhật lên trạng thái ĐÃ HIỂU lý thuyết:")
    path_lines.append(f"python scripts/learning/learning_manager.py update {ordered_concepts[0]} LEARNED --notes \"Đã hiểu bài\"")
    path_lines.append("")
    path_lines.append(f"# Ví dụ cập nhật lên trạng thái THỰC HÀNH THÀNH THẠO:")
    path_lines.append(f"python scripts/learning/learning_manager.py update {ordered_concepts[0]} MASTERED --notes \"Đã áp dụng thực hành\"")
    path_lines.append("```")
    
    paths_dir = os.path.join(LEARNING_DIR, "paths")
    os.makedirs(paths_dir, exist_ok=True)
    path_file_path = os.path.join(paths_dir, f"LEARNING_PATH_{source_id}.md")
    
    with open(path_file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(path_lines))
        
    print(f"Personalized path generated successfully at: {path_file_path}")
    
    # Đồng bộ cập nhật Dashboard sau khi sinh lộ trình mới
    generate_dashboard()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Learning Manager Core Engine")
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")
    
    # Subcommand init
    subparsers.add_parser("init", help="Initialize Learning database schema and update table tables.")
    
    # Subcommand update
    parser_update = subparsers.add_parser("update", help="Update learning status of a single Atom.")
    parser_update.add_argument("atom_id", help="The unique file ID of the Atom (e.g. CONCEPT_TIS_Stock).")
    parser_update.add_argument("status", choices=['TODO', 'IN_PROGRESS', 'LEARNED', 'MASTERED'], help="The new status to apply.")
    parser_update.add_argument("--notes", default=None, help="Optional learning notes/practice verification proof.")
    
    # Subcommand status
    subparsers.add_parser("status", help="Generate learning status and LEARNING_DASHBOARD.md.")
    
    # Subcommand generate-path
    parser_path = subparsers.add_parser("generate-path", help="Generate a customized sequence learning path for a source.")
    parser_path.add_argument("source_id", help="The unique Source ID (e.g. SOURCE_ARCH_TIS).")
    parser_path.add_argument("--goal", required=True, help="Your customized learning objective/goal.")
    
    args = parser.parse_args()
    
    if args.command == "init":
        init_db()
    elif args.command == "update":
        update_status(args.atom_id, args.status, args.notes)
    elif args.command == "status":
        generate_dashboard()
    elif args.command == "generate-path":
        generate_path(args.source_id, args.goal)
    else:
        parser.print_help()
