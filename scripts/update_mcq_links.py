import os
import re

WIKI_DIR = r"d:\NoteBookLLM_Br\brain\wiki"
MASTER_FILES = [
    os.path.join(WIKI_DIR, "WIKI_IOT_Arduino_Hardware.md"),
    os.path.join(WIKI_DIR, "WIKI_IOT_Arduino_Logic.md"),
    r"d:\NoteBookLLM_Br\brain\distilled\KB_IOT_Arduino_Master.md"
]

def update_links(content):
    # Pattern: [[MCQ_IOT_DeX_QXX]] hoặc [[MCQ_IOT_DeX_QXX_vX]]
    # Chúng ta đã đổi tên thành MCQ_[Device]_DeX_QXX.md
    # Vì chúng ta không biết Device từ link thô, chúng ta sẽ quét thư mục để tìm tên thực tế
    
    def replacement(match):
        old_link = match.group(1)
        # Tìm file thực tế bắt đầu bằng MCQ_ và kết thúc bằng DeX_QXX
        # Ví dụ: MCQ_Arduino_De1_Q01
        match_parts = re.search(r"De(\d+)_Q(\d+)", old_link)
        if not match_parts:
            return f"[[{old_link}]]"
            
        de_num = match_parts.group(1)
        q_num = match_parts.group(2)
        
        # Tìm file trong thư mục wiki
        for f in os.listdir(WIKI_DIR):
            if f.endswith(f"De{de_num}_Q{q_num}.md") and f.startswith("MCQ_"):
                return f"[[{f[:-3]}]]"
        
        return f"[[{old_link}]]"

    return re.sub(r"\[\[(MCQ_IOT_(?:Arduino_|Yolobit_|Halocode_)?De\d+_Q\d+[^\]]*)\]\]", replacement, content)

def main():
    for path in MASTER_FILES:
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        new_content = update_links(content)
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated links in: {path}")

if __name__ == "__main__":
    main()
