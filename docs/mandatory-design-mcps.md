# Mandatory MCP Policy for Design Tasks

Use `skills/design-mcp-orchestration/SKILL.md` for every UI/UX design task.

The policy requires tool-first reference research, color MCP use for color-related tasks, relevant implementation tooling, and screenshot-based visual validation. Missing required connections block completion until installed, authorized or explicitly waived by the user. An installed skill alone cannot guarantee that a host agent invokes an MCP.

Setup: `python3 scripts/setup-mcps.py --client claude --profile core --apply` and `python3 scripts/check-mcps.py claude`. Color MCPs, Flutter, Figma and other optional integrations currently require separate verified installation. See `mcp/servers.json`.

Recommended prompt: "Use design-mcp-orchestration. Do not mark this design complete unless required connected MCPs were actually invoked and the rendered UI reviewed."

## Enabling the Claude Code Stop gate

The repository contains `hooks/design-stop-gate.py` and `scripts/design-gate.py`. To enable it, register the Stop hook in your Claude Code settings using the example in [design-gate-hook.json](design-gate-hook.json), replacing `\${CLAUDE_PLUGIN_ROOT}` with an absolute repository path if not running as a Claude plugin. This hook is **not installed into other projects by merely cloning the repo**.

The `design-mcp-orchestration` skill opens and closes the gate itself (creates the marker and a fresh evidence file at the brief, fills it and removes the marker after a PASS). To do it by hand for a design task in the active project:

```bash
mkdir -p .design-gate
touch .design-gate/active
cp /path/to/agent-skills/docs/design-gate-evidence.example.json .design-gate/evidence.json
python3 /path/to/agent-skills/scripts/design-gate.py .design-gate/evidence.json
```

Replace sample placeholders with truthful tool names, inspected URLs, and screenshot-review evidence. A passing result only checks **self-reported fields**, not the actual MCP tool-call logs. Do not treat it as cryptographic proof or an independent quality score. Remove the `active` marker only when the task ends or is explicitly cancelled; a missing marker disables the hook. The hook avoids recursive stop loops when Claude reports that a Stop hook is already active, so it blocks the first attempt to finish and lets a second, immediate attempt through. Evidence must also list `agents_spawned` and, for implementation tasks, `component_mcps`.

**Limitations:** `AGENTS.md` applies only where that file is loaded. Claude Code requires the hook to be registered and activated in the target workspace. Other agent hosts need their own equivalent hook. The policy cannot force unconnected MCP servers to work.
