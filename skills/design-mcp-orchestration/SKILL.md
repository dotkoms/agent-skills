---
name: design-mcp-orchestration
description: Enforces a tool-first workflow for app/web UI design — connected reference MCPs for research, component-library MCPs (shadcn/ui, Magic UI, Aceternity, Animate UI, Eased, Wensity, HeroUI, Mantine, 21st.dev) for building, colour MCPs for palettes, and rendered validation — and blocks completion when a required capability is missing. Use when asked to make, redesign, theme or review any UI or frontend design, page, screen or component.
---
# Design MCP Orchestration

## Overview
UI work done from memory looks generic. This skill makes the agent research real references, build from real component libraries and look at the rendered result, using connected MCPs at each step, and say plainly when a step could not run.

## When to Use
Every UI design, redesign, theme, palette, frontend visual implementation or visual review. Invoke before design-reference-research, color-system-design and frontend-ui-engineering.

## Mandatory workflow
1. Inspect the existing product, component library, platform and design tokens (`package.json`, `components.json`, theme files).
2. Discover available MCP tools in the active client; don't assume a cataloged MCP is connected. For visual design, call at least one connected design-reference MCP (Screenrove, Inspo, VP0, One Page Love, A1 or equivalent). Capture actual source URLs and observations.
3. For color/theme work, call a connected color-science/palette MCP (Color Theory, Coolors, Palette Extractor or equivalent). Independently verify numeric contrast.
4. For implementation, build from connected component-library MCPs instead of hand-rolling components. For React/web, pick from the [component library catalog](references/component-libraries.md): the project's existing base (shadcn/ui, HeroUI or Mantine), plus Magic UI, Aceternity, Animate UI, Eased or Wensity for motion and showpiece sections, and 21st.dev when nothing else fits. Search the library, install its source, then restyle it to the product's tokens. For Flutter use the Dart/Flutter MCP; use Figma MCP when source Figma designs are provided and access is authorized.
5. Render the resulting UI and inspect it through connected Playwright MCP, Flutter MCP/Widgetbook or equivalent visual tooling. Run a visual quality review for hierarchy, typography, consistency, responsiveness, originality, states, motion (including `prefers-reduced-motion`) and accessibility. Revise defects and inspect again.
6. Report tools actually invoked, source references, components installed and from which library, screenshots inspected, issues fixed and remaining limitations.

## Failure policy
- Never silently skip required research, color validation or visual inspection.
- If a required MCP is missing, disconnected, rate-limited or unauthorized, stop the affected phase and give the exact blocker and setup action (for component libraries: `python3 scripts/setup-mcps.py --client claude --profile components --apply`). Do not claim completion or substitute invented research.
- An explicitly user-approved manual fallback can be used, but must be identified as such; never pretend an MCP ran.
- No MCP can be used until the client connects/authorizes it. This skill cannot install or force the host to execute tools.
- Do not send private project assets to third parties without authorization.

## Common Rationalizations
- "I can write this card/hero myself faster": a library component has states, accessibility and motion already worked out; search first, hand-roll only what no library covers.
- "More animation looks more premium": one or two animated set pieces per page; the rest should be calm.
- "The installed component looks fine in its default colours": it has to wear the product's tokens before it counts as done.
- "Mixing HeroUI, Mantine and shadcn gives the best of each": it gives three design languages and three theming systems. One base per project.

## Red Flags
- A second base component system added to a project that already has one
- Aceternity/Magic UI pieces shipped in their demo colours and fonts
- React component libraries proposed for a Flutter or native app
- Claiming a component came from a library MCP when it was written by hand
- Animated components with no reduced-motion fallback

## Verification
A UI task is complete only after actual reference research, applicable color analysis, implementation from a connected component source where one fits, rendered visual inspection, and a final report. If any mandatory phase is blocked, label the task BLOCKED, not DONE.

## Related
- `skills/design-reference-research/SKILL.md`
- `skills/color-system-design/SKILL.md`
- `skills/frontend-ui-engineering/SKILL.md`
- [Component library MCPs](references/component-libraries.md)
- `docs/mcp-automation.md`
