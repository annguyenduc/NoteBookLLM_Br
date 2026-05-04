import os
import re

def verify_index(index_path, base_dir):
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract file paths from markdown table rows: | Tag | File Path | Tên File |
    # Example: | **[IOT_001]** | `Tổng hợp đề kiểm tra LMS\...` | ... |
    pattern = r'\| \*\*\[.*?\]\*\* \| `(.*?)` \|'
    matches = re.findall(pattern, content)
    
    total = len(matches)
    missing = []
    
    print(f"Checking {total} files from {index_path}...")
    
    for relative_path in matches:
        # Normalize path for Windows
        full_path = os.path.join(base_dir, relative_path.replace('\\', os.sep))
        if not os.path.exists(full_path):
            missing.append(relative_path)
            
    if not missing:
        print("SUCCESS: All files in the index exist on disk.")
    else:
        print(f"FAILED: {len(missing)} files are missing.")
        for m in missing[:10]:
            print(f"  - Missing: {m}")
        if len(missing) > 10:
            print(f"  ... and {len(missing)-10} more.")

if __name__ == "__main__":
    verify_index(
        r"d:\NoteBookLLM_Br\brain\raw\MASTER_SOURCE_INDEX.md",
        r"d:\NoteBookLLM_Br\brain\raw"
    )
