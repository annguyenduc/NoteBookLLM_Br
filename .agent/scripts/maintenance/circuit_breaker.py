"""Canonical entrypoint for the Wiki ingest circuit breaker.

The implementation currently lives in `.kiro/circuit_breaker.py` for backward
compatibility with existing docs and skill references. Use this wrapper for new
calls so the maintenance entrypoint is discoverable with the rest of the tools.
"""

from __future__ import annotations

import runpy
from pathlib import Path


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    legacy_entrypoint = repo_root / ".kiro" / "circuit_breaker.py"
    runpy.run_path(str(legacy_entrypoint), run_name="__main__")


if __name__ == "__main__":
    main()
