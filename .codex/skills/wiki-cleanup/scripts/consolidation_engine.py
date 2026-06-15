import os
import re

ROOT_DIR = os.getenv(
    "NOTEBOOKLLM_ROOT",
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
)
WIKI_DIR = os.path.join(ROOT_DIR, "3-resources", "wiki")
INSIGHT_REPORT = os.path.join(WIKI_DIR, "graph_insight_report.md")
PROPOSAL_REPORT = os.path.join(WIKI_DIR, "consolidation_proposals.md")
THRESHOLD_PROMOTION = 3

def run_consolidation():
    print(f"--- STARTING CONSOLIDATION ANALYSIS (Threshold: {THRESHOLD_PROMOTION} links) ---")
    
    if not os.path.exists(INSIGHT_REPORT):
        print("[ERROR] Graph Insight Report not found. Run dense_linker.py first.")
        return

    with open(INSIGHT_REPORT, "r", encoding="utf-8") as f:
        content = f.read()

    # Tìm các link và số lượng trích dẫn bằng Regex
    # Định dạng: - [[file_id]]: count links
    matches = re.findall(r"- \[\[(QUERY_.*?)\]\]:\s*(\d+)\s*links", content)
    
    proposals = []
    for file_id, count in matches:
        count = int(count)
        if count >= THRESHOLD_PROMOTION:
            proposals.append(f"- **{file_id}**: {count} trích dẫn -> Đề xuất thăng hạng lên **CONCEPT**.")

    if proposals:
        with open(PROPOSAL_REPORT, "w", encoding="utf-8") as f:
            f.write("# Đề xuất Thăng hạng Tri thức (Consolidation Proposals)\n\n")
            f.write("Dựa trên phân suất trích dẫn và liên kết, các trang Query sau đây đủ điều kiện để trở thành tri thức Semantic (Concept):\n\n")
            f.write("\n".join(proposals))
            f.write("\n\n---\n*@engineer: Vui lòng xem xét chuyển đổi các file này sang thư mục concepts/ và cập nhật Template.*")
        print(f"--- Consolidation Proposals created at: {PROPOSAL_REPORT} ---")
    else:
        print("--- NO PROPOSALS. Keep compounding knowledge. ---")

if __name__ == "__main__":
    run_consolidation()
