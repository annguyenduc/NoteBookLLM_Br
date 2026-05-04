import os
import re

LOG_PATH = r'd:\NoteBookLLM_Br\3-resources\wiki\log.md'

MISSING_ENTRY = """## [2026-05-04 09:12] TEST | @scout | Pressure Test: wiki-crawl-4ai & wiki-web-scrape
- File: 00_Inbox/WEBSITE_TEST_LIGHTPANDA.md
- File: 00_Inbox/WEBSITE_TEST_CRAWL4AI.md
- Lý do: Kiểm tra tính ổn định của hệ thống cào dữ liệu web. Cả hai đều hoạt động tốt."""

SURGICAL_ENTRY = """## [2026-05-05 06:42] UPDATE | @auditor | Surgical content population cho 102 atoms
- File: 3-resources/wiki/wiki_brain.db
- Lý do: Đồng bộ nội dung từ file vật lý vào DB cho các atom bị thiếu content (NULL/Empty) mà không làm thay đổi cấu trúc liên kết hay trạng thái."""

def final_fix():
    with open(LOG_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add missing 09:12 entry at the beginning if not present
    if "2026-05-04 09:12" not in content:
        content = MISSING_ENTRY + "\n\n" + content

    # 2. Add 06:42 entry at the end if not present
    if "2026-05-05 06:42" not in content:
        content = content.strip() + "\n\n" + SURGICAL_ENTRY + "\n"
    
    # 3. Final cleanup of any potential duplicates or weird starts
    entries = re.split(r'\n(?=## )', content)
    unique = []
    seen = set()
    for e in entries:
        e = e.strip()
        if not e: continue
        h = re.sub(r'[^a-zA-Z0-9]', '', e.split('\n')[0]).lower()
        if h not in seen:
            unique.append(e)
            seen.add(h)
    
    def get_date(e):
        m = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}', e)
        return m.group(0) if m else "0000-00-00 00:00"
    
    unique.sort(key=get_date)
    
    with open(LOG_PATH, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(unique) + '\n')
    
    print("Final log fix successful.")

if __name__ == "__main__":
    final_fix()
    # Cleanup backups
    if os.path.exists(LOG_PATH + '.bak'):
        os.remove(LOG_PATH + '.bak')
