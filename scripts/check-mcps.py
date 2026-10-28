#!/usr/bin/env python3
"""Display MCP registration status and optional catalog coverage."""
import json
import shutil
import subprocess
import sys
from pathlib import Path
data = json.loads((Path(__file__).resolve().parent.parent / "mcp/servers.json").read_text())
client = sys.argv[1] if len(sys.argv) > 1 else "claude"
if client not in ("claude", "codex"):
    sys.exit("Usage: python3 scripts/check-mcps.py [claude|codex]")
if not shutil.which(client):
    sys.exit(f"{client} CLI is not installed on PATH")
cmd = [client, "mcp", "list"]
print("$ " + " ".join(cmd), flush=True)
p = subprocess.run(cmd, check=False)
print("\nKnown automatic entries:", ", ".join(data["servers"]))
print("Optional MCPs requiring manual review:", len(data["manual"]))
print("Note: a listed configuration may still require auth or fail when invoked.")
sys.exit(p.returncode)
