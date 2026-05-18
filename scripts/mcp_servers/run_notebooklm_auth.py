import sys
import site
from pathlib import Path


def bootstrap_workspace_venv() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    site_packages = repo_root / ".venv" / "Lib" / "site-packages"
    if site_packages.exists():
        site.addsitedir(str(site_packages))


bootstrap_workspace_venv()

from notebooklm_mcp.auth_cli import main


if __name__ == "__main__":
    sys.exit(main())
