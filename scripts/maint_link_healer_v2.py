import os
import re

def link_healer_v2(root_path):
    print(f"Starting Intelligent Link Healing for: {root_path}")
    
    target_dirs = [
        os.path.join(root_path, "brain", "distilled"),
        os.path.join(root_path, "brain", "archive")
    ]
    
    # 1. Map all existing files in the project for fast lookup
    all_files = {}
    for t_dir in target_dirs:
        if not os.path.exists(t_dir): continue
        for root, dirs, filenames in os.walk(t_dir):
            for f in filenames:
                if f.endswith(".md"):
                    all_files[f] = os.path.join(root, f)
                    all_files[os.path.splitext(f)[0]] = os.path.join(root, f)

    wiki_pattern = re.compile(r"\[\[(.*?)\]\]")
    md_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    
    updated_files = 0
    
    for t_dir in target_dirs:
      if not os.path.exists(t_dir): continue
      for root, dirs, filenames in os.walk(t_dir):
        for f in filenames:
            if not f.endswith(".md"): continue
            
            file_path = os.path.join(root, f)
            # Try to guess prefix from filename (e.g., skills_cloned_core_...)
            # Prefix is everything before the last underscore if it matches a known pattern
            # But simpler: just try to match the link by prefixing it with parts of the current filename
            f_base = os.path.splitext(f)[0]
            f_parts = f_base.split("_")
            
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                
                old_content = content
                
                def heal_match(link_text):
                    link_clean = link_text.replace("./", "").lstrip("/")
                    # If link exists as is, don't touch
                    if link_clean in all_files:
                        return link_text
                    
                    # Try to heal by adding prefixes from current file context
                    # e.g. current file: A_B_C_file1.md, link: [[file2]]
                    # Try: A_B_C_file2, A_B_file2, A_file2
                    for i in range(len(f_parts)-1, 0, -1):
                        prefix = "_".join(f_parts[:i])
                        candidate = f"{prefix}_{link_clean}"
                        if candidate in all_files:
                            return candidate
                        # Also try with extension
                        if f"{candidate}.md" in all_files:
                            return candidate
                    return link_text

                # Heal Wiki Links
                def wiki_sub(match):
                    link_full = match.group(1)
                    if "|" in link_full:
                        link, alias = link_full.split("|", 1)
                        healed = heal_match(link)
                        return f"[[{healed}|{alias}]]"
                    else:
                        healed = heal_match(link_full)
                        return f"[[{healed}]]"
                
                content = wiki_pattern.sub(wiki_sub, content)
                
                # Heal Markdown Links
                def md_sub(match):
                    text, path = match.group(1), match.group(2)
                    if path.startswith("http"): return match.group(0)
                    healed = heal_match(path)
                    return f"[{text}]({healed})"

                content = md_pattern.sub(md_sub, content)
                
                if content != old_content:
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.write(content)
                    updated_files += 1
            except Exception:
                continue

    print(f"Healing complete. Updated {updated_files} files.")

if __name__ == "__main__":
    link_healer_v2(os.getcwd())
