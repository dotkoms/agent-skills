#!/usr/bin/env python3
"""Fail closed on missing design MCP evidence. No dependencies."""
import json,sys
from pathlib import Path
def validate(d):
    required=["design_task","reference_mcp","reference_urls","agents_spawned","rendered_review","issues_reviewed"]
    missing=[k for k in required if not d.get(k)]
    if d.get("color_task") and not d.get("color_mcp"): missing.append("color_mcp")
    if d.get("implementation_task") and not d.get("implementation_tool"): missing.append("implementation_tool")
    if d.get("implementation_task") and not d.get("component_mcps"): missing.append("component_mcps")
    if d.get("blocked"): missing.append("blocked")
    return missing
def main():
    if len(sys.argv)!=2: sys.exit("Usage: python3 scripts/design-gate.py path/to/design-evidence.json")
    try: d=json.loads(Path(sys.argv[1]).read_text())
    except (OSError,ValueError) as e: sys.exit(f"BLOCKED: evidence unreadable: {e}")
    missing=validate(d)
    if missing: sys.exit("BLOCKED: missing or incomplete: "+", ".join(missing))
    print("PASS: design evidence fields present (self-reported; not cryptographic proof of MCP calls)")
if __name__=="__main__": main()
