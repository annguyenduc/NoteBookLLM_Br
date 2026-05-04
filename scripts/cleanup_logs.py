import os
import re

LOG_PATH = r'd:\NoteBookLLM_Br\3-resources\wiki\log.md'
TEMP_PATH = r'd:\NoteBookLLM_Br\3-resources\wiki\log_temp.md'

def clean_log():
    # 1. Read the backup created earlier or the current log.md
    log_file = LOG_PATH + '.bak' if os.path.exists(LOG_PATH + '.bak') else LOG_PATH
    try:
        with open(log_file, 'rb') as f:
            data = f.read()
        
        # Find first header
        start_idx = data.find(b'## ')
        if start_idx != -1:
            valid_log = data[start_idx:].decode('utf-8', errors='ignore')
        else:
            valid_log = ""
    except Exception as e:
        print(f"Error reading log: {e}")
        valid_log = ""

    # 2. Read and clean log_temp.md
    try:
        temp = ""
        # We might have deleted it, but let's assume we can recover from our logic
        if os.path.exists(TEMP_PATH):
            with open(TEMP_PATH, 'r', encoding='utf-8', errors='ignore') as f:
                temp = f.read()
            
            # Aggressive cleaning for corrupted spacing
            temp = re.sub(r'(?<=[A-Za-z0-9#]) (?=[A-Za-z0-9#])', '', temp)
            temp = temp.replace('# #', '##')
            temp = re.sub(r' +', ' ', temp)
    except Exception as e:
        print(f"Error reading log_temp.md: {e}")

    # 3. Combine and Deduplicate
    all_text = temp + '\n' + valid_log
    
    # Split by ## headers
    entries = re.split(r'\n(?=## )', all_text)
    
    unique_entries = []
    seen_headers = set()
    
    for entry in entries:
        entry = entry.strip()
        if not entry: continue
        
        # Normalize header for comparison
        header = entry.split('\n')[0].strip()
        # Remove brackets, spaces, and make lowercase for comparison
        header_norm = re.sub(r'[^a-zA-Z0-9]', '', header).lower()
        
        if header_norm not in seen_headers:
            unique_entries.append(entry)
            seen_headers.add(header_norm)

    # 4. Sort by Date
    def extract_date(e):
        match = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}', e)
        return match.group(0) if match else "0000-00-00 00:00"

    unique_entries.sort(key=extract_date)

    # 5. Write Result
    try:
        with open(LOG_PATH, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(unique_entries) + '\n')
        print("Log cleanup and merge successful (Aggressive Mode).")
    except Exception as e:
        print(f"Error writing output: {e}")

if __name__ == "__main__":
    clean_log()
