import os
import json

def generate_link_map_from_audit(audit_file="brain/depth_audit.json"):
    if not os.path.exists(audit_file):
        print(f"Error: Audit file {audit_file} not found.")
        return
        
    with open(audit_file, "r", encoding="utf-8") as f:
        violations = json.load(f)
        
    print(f"Generating link mapping from {len(violations)} violations...")
    mapping = {}
    
    for v in violations:
        path = v['path'] # e.g. "brain\\archive\\v2_legacy\\X\\Y\\file.md"
        parts = path.split(os.sep)
        
        # We only care about things deeper than 3 in brain/archive or brain/distilled
        if len(parts) <= 3:
            continue
            
        # Level 3 bucket
        # e.g. brain/archive/v2_legacy/X/Y/file.md -> prefix=X_Y, filename=file.md
        sub_parts = parts[3:]
        # Get filename and parents
        filename = sub_parts[-1]
        parent_parts = sub_parts[:-1]
        
        prefix = "_".join(parent_parts)
        if prefix:
            new_name = f"{prefix}_{filename}".replace(" ", "_")
        else:
            new_name = filename.replace(" ", "_")
            
        # Target path for link replacement
        # e.g. [[X/Y/file.md]] or [[X/Y/file]] or [doc](X/Y/file.md)
        # The link in Obsidian/Markdown is usually relative to the "bucket" root if it's broad,
        # or relative to the CURRENT FILE.
        
        # 1. Full relative path from bucket (Level 3)
        old_rel_path = "/".join(sub_parts)
        mapping[old_rel_path] = new_name
        
        # 2. Base name (wikilink style)
        old_base = os.path.splitext(old_rel_path)[0]
        new_base = os.path.splitext(new_name)[0]
        mapping[old_base] = new_base
        
        # 3. Just the file name if linked directly
        if filename not in mapping:
            mapping[filename] = new_name
        f_base = os.path.splitext(filename)[0]
        if f_base not in mapping:
            mapping[f_base] = new_base

    output_file = "brain/link_map.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(mapping, f, indent=2, ensure_ascii=False)
    
    print(f"Mapping complete. Saved {len(mapping)} entries to {output_file}")

if __name__ == "__main__":
    generate_link_map_from_audit()
