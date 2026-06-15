import os
import re
import sys
import yaml

ROOT_DIR = os.getenv(
    "NOTEBOOKLLM_ROOT",
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
)
WIKI_DIR = os.path.join(ROOT_DIR, "3-resources", "wiki")
CONCEPTS_DIR = os.path.join(WIKI_DIR, "concepts")

def get_all_concepts():
    """Lấy danh sách các concept và file_id tương ứng."""
    concepts = {}
    for root, dirs, files in os.walk(WIKI_DIR):
        for f in files:
            if f.endswith(".md") and (f.startswith("CONCEPT_") or f.startswith("ENTITY_")):
                core_name = f.replace("CONCEPT_META_", "").replace("CONCEPT_", "").replace("ENTITY_", "").replace(".md", "").replace("_", " ")
                concepts[core_name.lower()] = f.replace(".md", "")
    return concepts

def extract_yaml(content):
    """Trích xuất phần YAML frontmatter."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1)), match.group(0)
        except:
            return None, None
    return None, None

def process_wiki(concepts, apply_changes=False):
    print(f"--- STARTING {'APPLYING' if apply_changes else 'SCANNING'} (INTELLIGENT GRAPH) ---")
    report = []
    graph_insight = {} # file_id -> count_inbound
    
    EXCLUDE_FILES = ["index.md", "overview.md", "log.md", "review.md", "dense_linking_report.md"]
    
    for root, dirs, files in os.walk(WIKI_DIR):
        for file in files:
            if not file.endswith(".md") or file in EXCLUDE_FILES:
                continue
            
            file_path = os.path.join(root, file)
            file_id_current = file.replace(".md", "")
            
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            yaml_data, yaml_raw = extract_yaml(content)
            new_content = content
            found_in_file = []
            
            # 1. Tự động tạo link trong nội dung
            for concept_name, file_id in concepts.items():
                if file_id == file_id_current:
                    continue
                    
                pattern = rf"(?<!\[\[)\b({re.escape(concept_name)})\b(?!\]\])"
                
                if re.search(pattern, content, re.IGNORECASE):
                    found_in_file.append(concept_name)
                    graph_insight[file_id] = graph_insight.get(file_id, 0) + 1
                    if apply_changes:
                        new_content = re.sub(pattern, rf"[[{file_id}|\1]]", new_content, count=1, flags=re.IGNORECASE)
            
            # 2. Kiểm tra quan hệ trong YAML (Typed Graph)
            if yaml_data and "relationships" not in yaml_data and apply_changes:
                # Gợi ý thêm trường relationships nếu chưa có
                if found_in_file:
                    rel_block = "relationships:\n"
                    for c_name in found_in_file[:2]: # Chỉ gợi ý 2 cái đầu
                        rel_block += f"  - type: \"relates_to\"\n    target: \"[[{concepts[c_name]}]]\"\n"
                    new_content = new_content.replace(yaml_raw, yaml_raw + rel_block)

            if found_in_file:
                report.append(f"- **{file}**: {', '.join(found_in_file)}")
                if apply_changes:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
    
    return report, graph_insight

if __name__ == "__main__":
    apply_mode = "--apply" in sys.argv
    concepts = get_all_concepts()
    print(f"Found {len(concepts)} nodes in graph.")
    
    report, insights = process_wiki(concepts, apply_changes=apply_mode)
    
    # Tạo báo cáo Graph Insight
    insight_path = os.path.join(WIKI_DIR, "graph_insight_report.md")
    with open(insight_path, "w", encoding="utf-8") as f:
        f.write("# Báo cáo Phân tích Đồ thị Tri thức (Graph Insight)\n\n")
        f.write("## 🔝 Top các Concept quan trọng (Inbound Links)\n")
        sorted_insights = sorted(insights.items(), key=lambda x: x[1], reverse=True)
        for fid, count in sorted_insights[:10]:
            f.write(f"- [[{fid}]]: {count} links\n")
        
        f.write("\n## 📋 Chi tiết liên kết mới\n")
        f.write("\n".join(report))
        
    print(f"--- Graph Insight created at: {insight_path} ---")
