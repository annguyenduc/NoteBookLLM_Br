import os
import sqlite3
import logging
import sys
from fastmcp import FastMCP

# Redirect tất cả log sang stderr để tránh làm hỏng luồng stdout của MCP
logging.basicConfig(stream=sys.stderr, level=logging.WARNING)

ROOT_DIR = r"d:\NoteBookLLM_Br"
WIKI_DIR = os.path.join(ROOT_DIR, "3-resources", "wiki")
DB_PATH  = os.path.join(WIKI_DIR, "wiki_brain.db")

mcp = FastMCP("NoteBookLLM Wiki", log_level="WARNING")

@mcp.tool()
def search_atoms(query: str, limit: int = 5):
    """Tìm kiếm các Atoms trong Wiki bằng tìm kiếm ngữ nghĩa/toàn văn."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        results = cursor.execute("""
            SELECT a.file_id, a.title, a.status, a.confidence, s.content
            FROM atom_search s
            JOIN atoms a ON s.file_id = a.file_id
            WHERE s.content MATCH ?
            ORDER BY rank
            LIMIT ?
        """, (query, limit)).fetchall()
        conn.close()
        
        return [
            {
                "file_id": r[0],
                "title": r[1],
                "status": r[2],
                "confidence": r[3],
                "snippet": r[4][:200] + "..."
            } for r in results
        ]
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def get_atom_details(file_id: str):
    """Lấy nội dung chi tiết và các liên kết (Neighbors) của một Atom."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # 1. Content
        atom = cursor.execute("SELECT title, type, status, confidence FROM atoms WHERE file_id = ?", (file_id,)).fetchone()
        if not atom:
            conn.close()
            return f"Atom {file_id} not found."
            
        # 2. Incoming/Outgoing Edges
        edges = cursor.execute("""
            SELECT source_id, target_id, edge_type, confidence 
            FROM edges 
            WHERE source_id = ? OR target_id = ?
        """, (file_id, file_id)).fetchall()
        
        conn.close()
        
        return {
            "metadata": {
                "title": atom[0],
                "type": atom[1],
                "status": atom[2],
                "confidence": atom[3]
            },
            "neighbors": [
                {
                    "source": e[0],
                    "target": e[1],
                    "type": e[2],
                    "weight": e[3]
                } for e in edges
            ]
        }
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def expand_neighbors(atom_id: str):
    """Truy vấn các Atoms kết nối trực tiếp với atom_id kèm tiêu đề và nội dung."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        results = cursor.execute("""
            SELECT edges.target_id, edges.edge_type, atoms.title, atoms.content
            FROM edges
            JOIN atoms ON edges.target_id = atoms.file_id
            WHERE edges.source_id = ?
        """, (atom_id,)).fetchall()
        conn.close()
        return [
            {"target_id": r[0], "type": r[1], "title": r[2], "content": r[3]}
            for r in results
        ]
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def get_cluster(wing_name: str):
    """Lấy tất cả Atoms thuộc cùng một Wing hoặc Category (dựa trên đường dẫn hoặc metadata)."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        results = cursor.execute("""
            SELECT file_id, title, status, category
            FROM atoms
            WHERE path LIKE ? OR category = ?
        """, (f"%{wing_name}%", wing_name)).fetchall()
        conn.close()
        return [
            {"file_id": r[0], "title": r[1], "status": r[2], "category": r[3]}
            for r in results
        ]
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def get_revision_history(atom_id: str):
    """Truy xuất lịch sử các thao tác (ingest, rebuild, etc.) đã thực hiện trên Atom này."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        results = cursor.execute("""
            SELECT agent_id, action, timestamp, details
            FROM task_logs
            WHERE target_file LIKE ?
            ORDER BY timestamp DESC
        """, (f"%{atom_id}%",)).fetchall()
        conn.close()
        return [
            {"agent": r[0], "action": r[1], "timestamp": r[2], "details": r[3]}
            for r in results
        ]
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.resource("wiki://stats")
def get_wiki_stats():
    """Lấy thông tin thống kê sức khỏe của Wiki vault."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        count = cursor.execute("SELECT COUNT(*) FROM atoms").fetchone()[0]
        edges = cursor.execute("SELECT COUNT(*) FROM edges").fetchone()[0]
        verified = cursor.execute("SELECT COUNT(*) FROM atoms WHERE status = 'VERIFIED'").fetchone()[0]
        conn.close()
        
        return f"Wiki Vault: {count} atoms, {edges} edges. Verification rate: {(verified/count)*100:.1f}%"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()
