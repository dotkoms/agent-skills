---
name: design-mcp-orchestration
description: Mandatory tool-first workflow for any app/web UI design, redesign, palette, or visual quality review. Require applicable connected MCP research and rendered validation; block completion if required capabilities are unavailable.
---
# Design MCP Orchestration

## When to Use
Every UI design, redesign, theme, palette, frontend visual implementation or visual review. Invoke before design-reference-research, color-system-design and frontend-ui-engineering.

## Mandatory workflow
1. Inspect the existing product, component library, platform and design tokens.
2. Discover available MCP tools in the active client; don't assume a cataloged MCP is connected. For visual design, call at least one connected design-reference MCP (Screenrove, Inspo, VP0, One Page Love, A1 or equivalent). Capture actual source URLs and observations.
3. For color/theme work, call a connected color-science/palette MCP (Color Theory, Coolors, Palette Extractor or equivalent). Independently verify numeric contrast.
4. For implementation, use connected platform tooling when relevant (Flutter MCP for Flutter; shadcn registry for compatible React; Figma MCP when source Figma designs are provided and access is authorized).
5. Render the resulting UI and inspect it through connected Playwright MCP, Flutter MCP/Widgetbook or equivalent visual tooling. Run a visual quality review for hierarchy, typography, consistency, responsiveness, originality, states and accessibility. Revise defects and inspect again.
6. Report tools actually invoked, source references, screenshots inspected, issues fixed and remaining limitations.

## Failure policy
- Never silently skip required research, color validation or visual inspection.
- If a required MCP is missing, disconnected, rate-limited or unauthorized, stop the affected phase and give the exact blocker and setup action. Do not claim completion or substitute invented research.
- An explicitly user-approved manual fallback can be used, but must be identified as such; never pretend an MCP ran.
- No MCP can be used until the client connects/authorizes it. This skill cannot install or force the host to execute tools.
- Do not send private project assets to third parties without authorization.

## Verification
A UI task is complete only after actual reference research, applicable color analysis, rendered visual inspection, and a final report. If any mandatory phase is blocked, label the task BLOCKED, not DONE.

## Related
- `skills/design-reference-research/SKILL.md`
- `skills/color-system-design/SKILL.md`
- `skills/frontend-ui-engineering/SKILL.md`
- `docs/mcp-automation.md`
