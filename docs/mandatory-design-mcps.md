# Mandatory MCP Policy for Design Tasks

Use `skills/design-mcp-orchestration/SKILL.md` for every UI/UX design task.

The policy requires tool-first reference research, color MCP use for color-related tasks, relevant implementation tooling, and screenshot-based visual validation. Missing required connections block completion until installed, authorized or explicitly waived by the user. An installed skill alone cannot guarantee that a host agent invokes an MCP.

Setup: `python3 scripts/setup-mcps.py --client claude --profile core --apply` and `python3 scripts/check-mcps.py claude`. Color MCPs, Flutter, Figma and other optional integrations currently require separate verified installation. See `mcp/servers.json`.

Recommended prompt: "Use design-mcp-orchestration. Do not mark this design complete unless required connected MCPs were actually invoked and the rendered UI reviewed."
