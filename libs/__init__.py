"""Compatibility shim for scripts that still import ``libs.*``.

The real code-plane library now lives in ``workspaces/dev-lab/libs``.  Keep
this package tiny so root remains an operational entrypoint during migration.
"""

from pathlib import Path

_DEV_LAB_LIBS = Path(__file__).resolve().parents[1] / "workspaces" / "dev-lab" / "libs"

if _DEV_LAB_LIBS.is_dir():
    __path__.append(str(_DEV_LAB_LIBS))
