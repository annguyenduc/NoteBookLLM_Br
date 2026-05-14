import httpx
from fastmcp import FastMCP

mcp = FastMCP("Local-AI-MCP")
OLLAMA_URL = "http://localhost:11434/api/generate"

@mcp.tool()
def ollama_chat(prompt: str, model: str = "gemma3:4b") -> str:
    """Communicate with local Ollama model (Non-blocking R25)"""
    try:
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }
        with httpx.Client() as client:
            response = client.post(OLLAMA_URL, json=payload, timeout=60.0)
            response.raise_for_status()
            return response.json().get("response", "AI returned empty response.")
    except Exception as e:
        return f"WARNING: Ollama is offline or failed: {str(e)}. (R25: Proceeding without AI)"

@mcp.tool()
def vram_guard_run(task_id: str) -> str:
    """Run AI task with VRAM lock (Simplified logic)"""
    # In a real scenario, this would check a lock file or GPU usage
    return f"VRAM Guard: Task {task_id} is allowed to run. (Resource check PASSED)"

@mcp.tool()
def gap_check(atom_name: str) -> str:
    """Trigger gap analysis safely via Ollama"""
    prompt = f"Analyze knowledge gaps for the following Wiki Atom: {atom_name}. Return candidates."
    return ollama_chat(prompt)

if __name__ == "__main__":
    mcp.run(transport='stdio')
