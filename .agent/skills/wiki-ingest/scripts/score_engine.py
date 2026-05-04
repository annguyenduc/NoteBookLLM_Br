import math
import sqlite3
from datetime import datetime

# Configuration constants
SOURCE_TIER = {
    "personal_note": 1.0,
    "verified_atom": 0.95,
    "peer_reviewed": 0.90,
    "official_doc": 0.85,
    "textbook": 0.80,
    "blog_expert": 0.65,
    "video_transcript": 0.60,
    "llm_generated": 0.50,
    "web_scrape": 0.35,
    "unknown": 0.20
}

HALF_LIFE = {
    "AI_ML": 180,
    "pedagogy": 730,
    "tool_tutorial": 90,
    "concept": 1825,
    "default": 365
}

def compute_confidence(atom_data, conn):
    """
    Compute confidence score based on 4-axis logic.
    atom_data: dict containing keys like 'source_type', 'content', 'created_at', 'domain', 'file_id'
    conn: sqlite3 connection
    """
    # 1. Source Score (35%)
    source_type = atom_data.get("source_type", "unknown")
    source_score = SOURCE_TIER.get(source_type, SOURCE_TIER["unknown"])
    
    # 2. Semantic Score (30%)
    # Mocking semantic analysis: 
    # - Corroboration: +0.1 per supporting edge
    # - Contradiction: -0.4 per contradicting edge
    # - Specificity: +0.1 if content length > 500 chars
    semantic_score = 0.5 # Baseline
    file_id = atom_data.get("file_id")
    if file_id:
        cursor = conn.cursor()
        # Count contradictions
        cursor.execute("SELECT COUNT(*) FROM edges WHERE target_id = ? AND edge_type = 'CONTRADICTS'", (file_id,))
        contradictions = cursor.fetchone()[0]
        semantic_score -= (contradictions * 0.4)
        
        # Count corroborations (e.g. REFERENCES or SUPPORTS)
        cursor.execute("SELECT COUNT(*) FROM edges WHERE target_id = ? AND edge_type IN ('REFERENCES', 'SUPPORTS')", (file_id,))
        corroborations = cursor.fetchone()[0]
        semantic_score += (corroborations * 0.1)
        
    content = atom_data.get("content", "")
    if len(content) > 500:
        semantic_score += 0.1
    
    semantic_score = max(0.0, min(1.0, semantic_score))

    # 3. Freshness Score (20%)
    # exponential decay: score = 0.5 ^ (age / half_life)
    created_at_str = atom_data.get("created_at")
    if created_at_str:
        try:
            created_at = datetime.fromisoformat(created_at_str.replace('Z', '+00:00'))
        except ValueError:
            created_at = datetime.now()
    else:
        created_at = datetime.now()
        
    age_days = (datetime.now() - created_at).days
    domain = atom_data.get("domain", "default")
    half_life = HALF_LIFE.get(domain, HALF_LIFE["default"])
    freshness_score = math.pow(0.5, age_days / half_life)

    # 4. Graph Score (15%)
    # incoming edges * cross-domain factor
    graph_score = 0.2 # Baseline
    if file_id:
        cursor.execute("SELECT COUNT(*) FROM edges WHERE target_id = ?", (file_id,))
        incoming_count = cursor.fetchone()[0]
        graph_score += (incoming_count * 0.05)
        
    graph_score = max(0.0, min(1.0, graph_score))

    # Weighted Average
    confidence = (
        0.35 * source_score +
        0.30 * semantic_score +
        0.20 * freshness_score +
        0.15 * graph_score
    )
    
    return round(max(0.0, min(1.0, confidence)), 4)

if __name__ == "__main__":
    # Internal simple test
    class MockConn:
        def cursor(self): return self
        def execute(self, q, p=None): return self
        def fetchone(self): return [0]
    
    test_atom = {
        "source_type": "personal_note",
        "created_at": datetime.now().isoformat(),
        "domain": "AI_ML",
        "content": "Deep learning is a subset of machine learning."
    }
    print(f"Test Score (Personal Note, Fresh): {compute_confidence(test_atom, MockConn())}")
