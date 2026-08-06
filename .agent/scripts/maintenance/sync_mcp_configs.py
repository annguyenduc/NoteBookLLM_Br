#!/usr/bin/env python3
"""Generate Codex TOML + Antigravity JSON from one MCP registry."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Expected mapping YAML at {path}")
    return data


def get_profiles(registry: dict[str, Any], profiles_file: Path | None) -> dict[str, Any]:
    if profiles_file:
        data = load_yaml(profiles_file)
        profiles = data.get("profiles")
    else:
        profiles = registry.get("profiles")
    if not isinstance(profiles, dict):
        raise ValueError("Missing 'profiles' mapping.")
    return profiles


def resolve_profile_servers(
    registry: dict[str, Any],
    profiles: dict[str, Any],
    profile_name: str,
) -> dict[str, dict[str, Any]]:
    servers = registry.get("servers")
    if not isinstance(servers, dict):
        raise ValueError("Missing 'servers' mapping in registry.")

    profile = profiles.get(profile_name)
    if not isinstance(profile, dict):
        available = ", ".join(sorted(profiles.keys()))
        raise ValueError(f"Unknown profile '{profile_name}'. Available: {available}")

    enabled = profile.get("enabled")
    if not isinstance(enabled, list) or not all(isinstance(x, str) for x in enabled):
        raise ValueError(f"Profile '{profile_name}' requires 'enabled: [server,...]'.")

    selected: dict[str, dict[str, Any]] = {}
    missing: list[str] = []
    for name in enabled:
        entry = servers.get(name)
        if not isinstance(entry, dict):
            missing.append(name)
            continue
        selected[name] = entry

    if missing:
        raise ValueError(f"Profile '{profile_name}' references missing servers: {', '.join(missing)}")
    return selected


def antigravity_server_entry(name: str, entry: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    if "url" in entry:
        out["serverUrl"] = str(entry["url"])
    else:
        out["command"] = str(entry["command"])
        out["args"] = [str(x) for x in entry.get("args", [])]
        if "env" in entry:
            env = entry["env"]
            if not isinstance(env, dict):
                raise ValueError(f"Server '{name}' has non-mapping env.")
            out["env"] = {str(k): str(v) for k, v in env.items()}
    return out


def toml_quote(value: str) -> str:
    return json.dumps(value)


def build_mcp_toml_blocks(selected: dict[str, dict[str, Any]]) -> str:
    lines: list[str] = []
    for name, entry in selected.items():
        lines.append(f"[mcp_servers.{name}]")
        if "url" in entry:
            lines.append(f'url = {toml_quote(str(entry["url"]))}')
        else:
            lines.append(f'command = {toml_quote(str(entry["command"]))}')
            args = entry.get("args", [])
            if not isinstance(args, list):
                raise ValueError(f"Server '{name}' has non-list args.")
            args_str = ", ".join(toml_quote(str(x)) for x in args)
            lines.append(f"args = [{args_str}]")

            enabled = entry.get("enabled")
            if isinstance(enabled, bool):
                lines.append(f"enabled = {'true' if enabled else 'false'}")

            env = entry.get("env")
            if env is not None:
                if not isinstance(env, dict):
                    raise ValueError(f"Server '{name}' has non-mapping env.")
                lines.append("")
                lines.append(f"[mcp_servers.{name}.env]")
                for k, v in env.items():
                    lines.append(f"{k} = {toml_quote(str(v))}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


MCP_SECTION_RE = re.compile(r"^\[mcp_servers\.[^\]]+\]\s*$")
ANY_SECTION_RE = re.compile(r"^\[[^\]]+\]\s*$")


def remove_existing_mcp_sections(toml_text: str) -> str:
    lines = toml_text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        if MCP_SECTION_RE.match(line.strip()):
            i += 1
            while i < n:
                nxt = lines[i]
                stripped = nxt.strip()
                if ANY_SECTION_RE.match(stripped):
                    if MCP_SECTION_RE.match(stripped):
                        i += 1
                        continue
                    break
                i += 1
            continue
        out.append(line)
        i += 1
    return "".join(out).rstrip() + "\n\n"


def build_codex_toml(existing_toml: str, selected: dict[str, dict[str, Any]]) -> str:
    base = remove_existing_mcp_sections(existing_toml)
    blocks = build_mcp_toml_blocks(selected)
    return base + blocks


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync MCP registry into Codex TOML + Antigravity JSON.")
    parser.add_argument("--registry", required=True, help="Path to mcp.registry.yaml")
    parser.add_argument("--profile", required=True, help="Profile name to materialize")
    parser.add_argument("--profiles", help="Optional path to mcp.profiles.yaml")
    parser.add_argument("--codex-out", required=True, help="Target path for Codex config.toml")
    parser.add_argument("--antigravity-out", required=True, help="Target path for Antigravity mcp_config.json")
    parser.add_argument("--apply", action="store_true", help="Write files. Default is dry-run.")
    args = parser.parse_args()

    registry_path = Path(args.registry).resolve()
    profiles_path = Path(args.profiles).resolve() if args.profiles else None
    codex_out_path = Path(args.codex_out).resolve()
    antigravity_out_path = Path(args.antigravity_out).resolve()

    registry = load_yaml(registry_path)
    profiles = get_profiles(registry, profiles_path)
    selected = resolve_profile_servers(registry, profiles, args.profile)

    antigravity_data = {
        "mcpServers": {
            name: antigravity_server_entry(name, entry)
            for name, entry in selected.items()
        }
    }
    antigravity_json = json.dumps(antigravity_data, ensure_ascii=False, indent=2) + "\n"

    if codex_out_path.exists():
        existing_toml = codex_out_path.read_text(encoding="utf-8")
    else:
        existing_toml = ""
    codex_toml = build_codex_toml(existing_toml, selected)

    print(f"registry: {registry_path}")
    if profiles_path:
        print(f"profiles: {profiles_path}")
    print(f"profile: {args.profile}")
    print(f"servers: {', '.join(selected.keys())}")
    print(f"codex_out: {codex_out_path}")
    print(f"antigravity_out: {antigravity_out_path}")

    if not args.apply:
        print("mode: dry-run (no file writes)")
        return 0

    write_text(codex_out_path, codex_toml)
    write_text(antigravity_out_path, antigravity_json)
    print("mode: apply (files updated)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
