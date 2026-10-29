#!/usr/bin/env python3
"""Configure free-first, approved MCPs for Claude Code or Codex without shell interpolation."""
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "mcp" / "servers.json"

def read_catalog():
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        raise ValueError("Unsupported MCP catalog version")
    return data

def run(args, execute):
    print("$ " + " ".join(args))
    if not execute:
        return True
    p = subprocess.run(args, check=False)
    if p.returncode:
        print(f"  FAILED (exit {p.returncode})", file=sys.stderr)
        return False
    return True

def get_existing(client, execute):
    if not execute:
        return set()
    p = subprocess.run([client, "mcp", "list"], capture_output=True, text=True, check=False)
    if p.returncode:
        print("Could not inspect existing MCPs; refusing to overwrite. Check CLI login/setup.", file=sys.stderr)
        sys.exit(2)
    # Claude outputs lines 'name: ...'; Codex outputs a table with the name in the first column.
    out = p.stdout.splitlines()
    return {line.split(":", 1)[0].strip() for line in out if ":" in line} if client == "claude" else {line.split()[0] for line in out[1:] if line.strip()}

def main():
    parser = argparse.ArgumentParser(description="Install vetted MCPs from mcp/servers.json")
    parser.add_argument("--client", choices=["claude", "codex"], default="claude")
    parser.add_argument("--profile", default="core")
    parser.add_argument("--scope", choices=["user", "local", "project"], default="user", help="Claude only; Codex MCPs are user-scoped")
    parser.add_argument("--apply", action="store_true", help="Actually change client settings; otherwise dry-run")
    parser.add_argument("--force", action="store_true", help="Allow replacing existing named connections (not default)")
    parser.add_argument("--list", action="store_true", help="Print catalog without connecting")
    args = parser.parse_args()
    catalog = read_catalog()
    if args.list:
        for profile, names in catalog["profiles"].items():
            print(f"{profile}: {', '.join(names) or '(manual configuration required)'}")
        print("\nManual/optional servers:")
        for entry in catalog["manual"]:
            print(f"  {entry['name']}: {entry['url']}")
        return 0
    if args.profile not in catalog["profiles"]:
        parser.error(f"unknown profile: {args.profile}")
    client = args.client
    names = catalog["profiles"][args.profile]
    if client == "codex" and args.scope != "user":
        parser.error("Codex only supports --scope user here")
    if args.apply and not shutil.which(client):
        parser.error(f"{client} not found on PATH")
    if args.apply and any(catalog["servers"][name]["transport"] == "stdio" for name in names) and not shutil.which("npx"):
        parser.error("npx not found (required for stdio MCPs in this profile)")
    existing = get_existing(client, args.apply)
    failures = 0
    for name in names:
        config = catalog["servers"][name]
        if name in existing:
            if not args.force:
                print(f"SKIP {name}: already configured (use --force to replace)")
                continue
            print(f"Replacing existing {name}")
            if not run([client, "mcp", "remove", name], args.apply):
                failures += 1
                continue
        if client == "claude":
            prefix = ["claude", "mcp", "add", "--scope", args.scope]
            if config["transport"] == "http":
                cmd = prefix + ["--transport", "http", name, config["url"]]
            else:
                cmd = prefix + [name, "--", config["command"]] + config["args"]
        else:
            prefix = ["codex", "mcp", "add", name]
            cmd = prefix + (["--url", config["url"]] if config["transport"] == "http" else ["--", config["command"]] + config["args"])
        if not run(cmd, args.apply):
            failures += 1
    if not names:
        print("This profile contains manual-only integrations. See mcp/servers.json and docs/mcp-automation.md.")
    print(f"\n{'Applied' if args.apply else 'Dry-run complete (no changes)'}: {len(names)} selected, {failures} failed")
    if args.apply:
        print(f"Verify: {client} mcp list")
        print("Registration does not guarantee connectivity; some providers require login or rate-limit.")
    return 1 if failures else 0

if __name__ == "__main__":
    sys.exit(main())
