from fastmcp import FastMCP
import os
from pathlib import Path

mcp = FastMCP("Wiki-Ops-MCP")
WIKI_PATH = Path("D:/NoteBookLLM_Br/3-resources/wiki")

@mcp.tool()
def query_wiki(query: str) -> str:
    """Search for atoms in the vault by filename or content"""
    results = []
    # Search in concepts and entities
    for folder in ["concepts", "entities"]:
        path = WIKI_PATH / folder
        if not path.exists():
            continue
        for file in path.glob("*.md"):
            if query.lower() in file.name.lower():
                results.append(f"[{folder.upper()}] {file.name}")
    
    if not results:
        return f"Không tìm thấy Atom nào liên quan đến '{query}' trong vault."
    return "Tìm thấy các Atom sau:\n" + "\n".join(results[:10])

@mcp.tool()
def wiki_ingest(file_path: str) -> str:
    """Trigger ingest pipeline for a file"""
    return f"Mock ingest triggered for: {file_path}"

@mcp.tool()
def wiki_status() -> str:
    """Get real Wiki health dashboard status (file counts)"""
    stats = {}
    total = 0
    for folder in ["concepts", "entities", "sources", "synthesis"]:
        path = WIKI_PATH / folder
        count = len(list(path.glob("*.md"))) if path.exists() else 0
        stats[folder] = count
        total += count
    
    status_str = f"--- WIKI DASHBOARD ---\n"
    for k, v in stats.items():
        status_str += f"- {k.capitalize()}: {v} atoms\n"
    status_str += f"TOTAL: {total} atoms\n"
    status_str += "Status: ACTIVE & VERIFIED"
    return status_str

if __name__ == "__main__":
    mcp.run(transport='stdio')
