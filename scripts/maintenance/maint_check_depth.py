import os
import json

def check_folder_depth(root_path, max_depth=3):
    violations = []
    root_path = os.path.abspath(root_path)
    
    for root, dirs, files in os.walk(root_path):
        rel_path = os.path.relpath(root, root_path)
        if rel_path == ".":
            depth = 0
        else:
            depth = len(rel_path.split(os.sep))
            
        if depth > max_depth:
            # Skip managed environment folders
            parts = rel_path.split(os.sep)
            if any(part.startswith('.') or part in ['node_modules', 'venv', '.venv', 'storage', 'graphify-out'] for part in parts):
                continue
            violations.append({"path": rel_path, "depth": depth})
            
    return violations

if __name__ == "__main__":
    current_dir = os.getcwd()
    deep_folders = check_folder_depth(current_dir)
    
    output_file = "brain/depth_audit.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(deep_folders, f, indent=2, ensure_ascii=False)
    
    print(f"Audit complete. Found {len(deep_folders)} violations. Results saved to {output_file}")
