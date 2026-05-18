import sys
import site
import os
from pathlib import Path


def bootstrap_workspace_venv() -> None:
    """Load the repo venv's site-packages even when using an external runtime.

    This keeps NotebookLM MCP working if the original Windows venv launcher
    becomes unusable, while still reusing the package set already installed in
    the project venv.
    """
    repo_root = Path(__file__).resolve().parents[2]
    site_packages = repo_root / ".venv" / "Lib" / "site-packages"
    if site_packages.exists():
        site.addsitedir(str(site_packages))


def configure_fastmcp_runtime() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    fastmcp_home = repo_root / "scratch" / "fastmcp"
    os.environ.setdefault("FASTMCP_CHECK_FOR_UPDATES", "off")
    os.environ.setdefault("FASTMCP_HOME", str(fastmcp_home))

# Simple delegation approach
class SimpleFilteredStdout:
    def __init__(self, original):
        self.original = original
        # Copy encoding if available, otherwise default to utf-8
        self.encoding = getattr(original, 'encoding', 'utf-8')
        
    def write(self, s):
        # Filter out banner lines
        if any(c in s for c in ['╭', '│', '╰', '─']):
            return len(s)
        if "FastMCP server" in s:
            return len(s)
        return self.original.write(s)
        
    def flush(self):
        if hasattr(self.original, 'flush'):
            self.original.flush()
        
    def __getattr__(self, name):
        return getattr(self.original, name)

# Patch stdout BEFORE importing notebooklm_mcp.server
# because FastMCP initializes at module level
bootstrap_workspace_venv()
configure_fastmcp_runtime()
original_stdout = sys.stdout
sys.stdout = SimpleFilteredStdout(original_stdout)

from notebooklm_mcp.server import main

if __name__ == "__main__":
    sys.exit(main())
