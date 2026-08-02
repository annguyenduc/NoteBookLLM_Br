import argparse
import json
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


WORKSPACE_SKILLS = Path(r"D:\NoteBookLLM_Br\.agent\skills")
ANTIGRAVITY_SKILLS = Path(r"D:\anngu\.gemini\antigravity\skills")
CODEX_SKILLS = Path(r"D:\anngu\.codex\skills")

IGNORED_NAMES = {
    ".git",
    ".system",
    "__pycache__",
}


@dataclass
class SkillEntry:
    name: str
    path: Path
    source: str


def configure_stdout() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Union-sync workspace skills and Antigravity global skills so Codex "
            "can resolve both from stable roots."
        )
    )
    parser.add_argument(
        "--workspace-skills",
        type=Path,
        default=WORKSPACE_SKILLS,
        help="Workspace skill root. Default: %(default)s",
    )
    parser.add_argument(
        "--antigravity-skills",
        type=Path,
        default=ANTIGRAVITY_SKILLS,
        help="Antigravity global skill root. Default: %(default)s",
    )
    parser.add_argument(
        "--codex-skills",
        type=Path,
        default=CODEX_SKILLS,
        help="Codex global skill root. Default: %(default)s",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Create missing junctions. Default is report-only.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON instead of human-readable text.",
    )
    return parser.parse_args()


def is_skill_dir(path: Path) -> bool:
    if not path.is_dir():
        return False
    if path.name in IGNORED_NAMES:
        return False
    return (path / "SKILL.md").is_file()


def collect_skills(root: Path, source_name: str) -> dict[str, SkillEntry]:
    skills: dict[str, SkillEntry] = {}
    if not root.exists():
        return skills

    for child in sorted(root.iterdir(), key=lambda item: item.name.lower()):
        if is_skill_dir(child):
            skills[child.name] = SkillEntry(name=child.name, path=child, source=source_name)
    return skills


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def is_directory_junction(path: Path) -> bool:
    try:
        return bool(path.exists() and path.is_dir() and path.is_junction())
    except AttributeError:
        return False


def existing_target(path: Path) -> str | None:
    try:
        if path.is_symlink() or is_directory_junction(path):
            target = os.readlink(path)
            return str(Path(target))
    except OSError:
        return None
    return None


def dir_is_empty(path: Path) -> bool:
    try:
        next(path.iterdir())
    except StopIteration:
        return True
    return False


def create_junction(link_path: Path, target_path: Path) -> None:
    ensure_dir(link_path.parent)
    cmd = [
        "cmd",
        "/c",
        "mklink",
        "/J",
        str(link_path),
        str(target_path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if result.returncode != 0:
        stderr = result.stderr.strip()
        stdout = result.stdout.strip()
        detail = stderr or stdout or f"mklink exited with {result.returncode}"
        raise RuntimeError(detail)


def plan_workspace_union(
    workspace_root: Path,
    antigravity_root: Path,
) -> list[dict[str, str]]:
    workspace_skills = collect_skills(workspace_root, "workspace")
    antigravity_skills = collect_skills(antigravity_root, "antigravity")
    actions: list[dict[str, str]] = []

    for name, entry in antigravity_skills.items():
        dest = workspace_root / name
        if name in workspace_skills:
            continue
        actions.append(
            {
                "scope": "workspace",
                "skill": name,
                "action": "link_missing_global_into_workspace",
                "source": str(entry.path),
                "destination": str(dest),
            }
        )

    return actions


def plan_codex_union(
    codex_root: Path,
    workspace_root: Path,
    antigravity_root: Path,
) -> list[dict[str, str]]:
    codex_skills = collect_skills(codex_root, "codex")
    workspace_skills = collect_skills(workspace_root, "workspace")
    antigravity_skills = collect_skills(antigravity_root, "antigravity")
    actions: list[dict[str, str]] = []

    for name, entry in workspace_skills.items():
        dest = codex_root / name
        if name in codex_skills:
            continue
        actions.append(
            {
                "scope": "codex",
                "skill": name,
                "action": "link_missing_workspace_into_codex",
                "source": str(entry.path),
                "destination": str(dest),
            }
        )

    for name, entry in antigravity_skills.items():
        dest = codex_root / name
        if name in codex_skills:
            continue
        if any(item["skill"] == name for item in actions):
            continue
        actions.append(
            {
                "scope": "codex",
                "skill": name,
                "action": "link_missing_antigravity_into_codex",
                "source": str(entry.path),
                "destination": str(dest),
            }
        )

    return actions


def collect_conflicts(
    workspace_root: Path,
    antigravity_root: Path,
    codex_root: Path,
) -> list[dict[str, str]]:
    workspace_skills = collect_skills(workspace_root, "workspace")
    antigravity_skills = collect_skills(antigravity_root, "antigravity")
    codex_skills = collect_skills(codex_root, "codex")
    conflicts: list[dict[str, str]] = []

    for name in sorted(set(workspace_skills) & set(antigravity_skills)):
        ws_path = workspace_skills[name].path
        ag_path = antigravity_skills[name].path
        if ws_path.resolve() == ag_path.resolve():
            continue
        conflicts.append(
            {
                "scope": "collision",
                "skill": name,
                "workspace": str(ws_path),
                "antigravity": str(ag_path),
            }
        )

    for name in sorted(set(workspace_skills) & set(codex_skills)):
        ws_path = workspace_skills[name].path
        cx_path = codex_skills[name].path
        if ws_path.resolve() == cx_path.resolve():
            continue
        target = existing_target(cx_path) or str(cx_path)
        conflicts.append(
            {
                "scope": "collision",
                "skill": name,
                "workspace": str(ws_path),
                "codex": target,
            }
        )

    return conflicts


def apply_actions(actions: list[dict[str, str]]) -> list[dict[str, str]]:
    applied: list[dict[str, str]] = []
    for action in actions:
        dest = Path(action["destination"])
        src = Path(action["source"])
        if dest.exists():
            if dest.is_dir() and not is_skill_dir(dest) and dir_is_empty(dest):
                dest.rmdir()
                create_junction(dest, src)
                action_copy = dict(action)
                action_copy["result"] = "replaced_empty_dir"
                applied.append(action_copy)
                continue

            action_copy = dict(action)
            action_copy["result"] = "skipped_exists"
            applied.append(action_copy)
            continue
        create_junction(dest, src)
        action_copy = dict(action)
        action_copy["result"] = "linked"
        applied.append(action_copy)
    return applied


def build_report(args: argparse.Namespace) -> dict[str, object]:
    workspace_root = args.workspace_skills
    antigravity_root = args.antigravity_skills
    codex_root = args.codex_skills

    workspace_actions = plan_workspace_union(workspace_root, antigravity_root)
    codex_actions = plan_codex_union(codex_root, workspace_root, antigravity_root)
    conflicts = collect_conflicts(workspace_root, antigravity_root, codex_root)

    report: dict[str, object] = {
        "mode": "apply" if args.apply else "report",
        "workspace_skills": str(workspace_root),
        "antigravity_skills": str(antigravity_root),
        "codex_skills": str(codex_root),
        "workspace_actions": workspace_actions,
        "codex_actions": codex_actions,
        "conflicts": conflicts,
    }

    if args.apply:
        report["workspace_results"] = apply_actions(workspace_actions)
        report["codex_results"] = apply_actions(codex_actions)

    return report


def render_text(report: dict[str, object]) -> str:
    lines: list[str] = []
    lines.append(f"Mode: {report['mode']}")
    lines.append(f"Workspace root: {report['workspace_skills']}")
    lines.append(f"Antigravity root: {report['antigravity_skills']}")
    lines.append(f"Codex root: {report['codex_skills']}")
    lines.append("")

    workspace_actions = report["workspace_actions"]
    codex_actions = report["codex_actions"]
    conflicts = report["conflicts"]

    lines.append(f"Workspace additions planned: {len(workspace_actions)}")
    for item in workspace_actions:
        lines.append(f"  - {item['skill']} <= {item['source']}")

    lines.append(f"Codex additions planned: {len(codex_actions)}")
    for item in codex_actions:
        lines.append(f"  - {item['skill']} <= {item['source']}")

    lines.append(f"Conflicts detected: {len(conflicts)}")
    for item in conflicts:
        lines.append(f"  - {item['skill']}")

    if report["mode"] == "apply":
        lines.append("")
        lines.append("Apply results:")
        for key in ("workspace_results", "codex_results"):
            for item in report.get(key, []):
                lines.append(f"  - {item['skill']}: {item['result']}")

    return "\n".join(lines)


def main() -> int:
    configure_stdout()
    args = parse_args()
    report = build_report(args)

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(render_text(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
