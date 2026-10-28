# Agentic Design Skill Library

Entry point: [Design Reference Research](../skills/design-reference-research/SKILL.md).

This module adds free-first UI/UX research to the existing software engineering skills in this repository. It does **not** install external MCP servers, mirror image libraries or vendor third-party source code.

## Files
- [Skill: research workflow](../skills/design-reference-research/SKILL.md)
- [Catalog: MCPs, libraries, galleries and free-tier caveats](../skills/design-reference-research/references/resources.md)
- [MCP setup and security](../skills/design-reference-research/references/mcp-setup.md)
- [Existing frontend implementation skill](../skills/frontend-ui-engineering/SKILL.md)

## How to invoke
In Claude Code, Codex or another skills-aware agent, ask:

> Use the design-reference-research skill to research 3–6 real references for [screen], compare options against this repo's design system, write a design contract, implement with frontend-ui-engineering, and verify the resulting UI in a browser or Flutter preview.

For best results include: platform, current repo/component paths, target screen, screenshots, primary task, and explicit stylistic invariants.

## Example: Flutter trading application

> Research mobile trading leaderboards, markets, trader profiles, and heatmap layouts. Preserve our Flutter app's existing typography, colors, navigation and component language. Explain three options, pick one based on information density and usability, implement with reusable widgets and validate states at common phone sizes.

## Routing matrix

| Goal | Research | Implementation / verification |
|---|---|---|
| Flutter app | VP0, Banani, Kombai | Dart/Flutter MCP, Widgetbook |
| React dashboard | Screenrove, Inspo, Figma Community | frontend-ui-engineering, shadcn/ui, Playwright |
| Landing page | One Page Love, A1, Lapa Ninja | frontend-ui-engineering, Playwright |

## Quality bar
Document source URLs; extract patterns rather than copy; keep existing design tokens; check mobile responsiveness/accessibility and non-happy-path states; mark unavailable tools and uninspected sources explicitly.
