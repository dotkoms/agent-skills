#!/usr/bin/env python3
"""Claude Code Stop hook. Only checks tasks explicitly tagged with design evidence."""
import json,os,subprocess,sys
from pathlib import Path
try: payload=json.load(sys.stdin)
except Exception: sys.exit(0)
# Activated by creating .design-gate/active in the target workspace.
root=Path(os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd())
marker=root/".design-gate"/"active"
if not marker.exists(): sys.exit(0)
evidence=root/".design-gate"/"evidence.json"
script=Path(__file__).resolve().parents[1]/"scripts"/"design-gate.py"
p=subprocess.run([sys.executable,str(script),str(evidence)],capture_output=True,text=True)
if p.returncode:
    if payload.get("stop_hook_active"): sys.exit(0)  # prevent infinite stop-hook loops
    print(json.dumps({"decision":"block","reason":"Design MCP gate: "+(p.stderr.strip() or p.stdout.strip())+". Complete MCP research and rendered review, then update .design-gate/evidence.json."}))
