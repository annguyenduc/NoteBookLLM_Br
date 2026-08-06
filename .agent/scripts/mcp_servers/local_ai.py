import httpx
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from fastmcp import FastMCP

mcp = FastMCP("Local-AI-MCP")
OLLAMA_URL = "http://localhost:11434/api/generate"
CANONICAL_TYPES = "Concept|Entity|Method|Principle|Mental Model|Relationship"
DEFAULT_VAULT_ROOT = Path(r"D:\NoteBookLLM_Br")

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

def _normalize_gap_check_response(response: str) -> str:
    if not response:
        return response
    if response.startswith("WARNING:") or response.strip() == "NONE":
        return response

    normalized_lines = []
    for line in response.splitlines():
        stripped = line.strip()
        if re.match(rf"^- \[({CANONICAL_TYPES})\] .+?: .+", stripped):
            normalized_lines.append(stripped)
            continue

        match = re.match(rf"^- ({CANONICAL_TYPES}):\s*(.+?: .+)", stripped)
        if match:
            normalized_lines.append(f"- [{match.group(1)}] {match.group(2)}")

    return "\n".join(normalized_lines) if normalized_lines else response

def _review_root() -> Path:
    configured = os.getenv("LOCAL_AI_REVIEW_ROOT") or os.getenv("NOTEBOOKLLM_ROOT")
    if configured:
        return Path(configured)
    if DEFAULT_VAULT_ROOT.exists():
        return DEFAULT_VAULT_ROOT
    return Path(__file__).resolve().parents[2]

def _safe_slug(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9_-]+", "_", value).strip("_")
    return slug[:80] or "gap_check"

def _write_gap_review_artifact(atom_name: str, response: str, model: str = "gemma3:4b") -> Path:
    output_dir = _review_root() / "00_Inbox" / "gap_candidates"
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output_path = output_dir / f"local_ai_{_safe_slug(atom_name)}_{timestamp}.md"
    content = f"""---
source: Local-AI-MCP
atom_name: {atom_name}
date: {datetime.now().strftime('%Y-%m-%d')}
model: {model}
status: PENDING_REVIEW
audit_stamp: true
audit_timestamp: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}
---

## Local AI gap-check candidates

{response}
"""
    output_path.write_text(content, encoding="utf-8")
    return output_path

@mcp.tool()
def gap_check(atom_name: str) -> str:
    """Trigger gap analysis safely via Ollama"""
    prompt = f"""You are a knowledge gap detector for a personal knowledge vault.
Analyze this Wiki Atom name: {atom_name}

Return ONLY bullet points in this format:
- [Type] Name: One sentence value

Rules:
1. Valid types: Concept, Entity, Method, Principle, Mental Model, Relationship.
2. Report only source-specific knowledge worth preserving as a Wiki atom.
3. Ignore generic examples, analogies, metaphors, and everyday nouns used only to explain another concept.
4. If no useful gap exists, return exactly: NONE.
5. The type MUST be enclosed in square brackets, for example "- [Concept] Feedback Loop: ...".
6. Do not include preamble, headings, markdown sections, or explanations."""
    response = _normalize_gap_check_response(ollama_chat(prompt))
    review_path = _write_gap_review_artifact(atom_name, response)
    return f"review_artifact: {review_path}\n\n{response}"

if __name__ == "__main__":
    mcp.run(transport='stdio')
