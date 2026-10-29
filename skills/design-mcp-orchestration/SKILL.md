---
name: design-mcp-orchestration
description: Runs UI design as a multi-agent build — a researcher and colour designer set direction, a scout per section picks real parts from library MCPs (shadcn/ui, Magic UI, Aceternity, Animate UI, Eased, Wensity, HeroUI, Mantine, 21st.dev), and a reviewer checks the rendered result — and blocks completion when a required capability is missing. Use when asked to make, redesign, theme or review a UI or frontend design, page or screen.
---
# Design MCP Orchestration

## Overview
UI work done from memory, by one agent treating the page as a single picture, looks generic. This skill splits the work: specialists research references and colour, a scout per component picks real library components through MCPs, the lead integrates, and a reviewer inspects the rendered result. Every step uses connected MCPs and says plainly when one could not run.

## When to Use
Every UI design, redesign, theme, palette, frontend visual implementation or visual review. This skill is the entry point: it calls `design-reference-research`, `color-system-design` and `frontend-ui-engineering` (load by name; they may be plugin-prefixed, e.g. `agent-skills:frontend-ui-engineering`) through the agents below. Only a one-property tweak to an existing component (a colour, a padding) may skip the fan-out, and it still gets the rendered review.

## Multi-agent workflow
A design is built as a team, not as one piece. Each component gets its own `component-scout` so the component-library MCPs decide what each part is made of, and a separate `design-reviewer` judges the assembled result. The main session is the lead; personas never call each other. Spawn with the Agent tool, `subagent_type` = the persona name, and **issue every call in a wave in one turn** so they run in parallel.

### 1. Lead: brief
Inspect the product, platform, base component library and tokens (`package.json`, `components.json`, theme files). Confirm which MCPs are connected. Write a short brief: screen goal, audience, stack, tokens, motion budget, what must not change.

Open the design gate in the target project root: create `.design-gate/active`, write a fresh `.design-gate/evidence.json` containing only `{"design_task": true}` (never reuse a previous task's evidence), and add `.design-gate/` to `.git/info/exclude` so it is never committed. While the marker exists, Claude Code's Stop hook refuses to finish until the evidence is complete.

### 2. Wave A — direction (parallel)
- **`design-researcher`** — runs `design-reference-research` through reference MCPs; returns references, design contract and the **component list**.
- **`color-designer`** — runs `color-system-design` through a colour MCP; returns token table, measured contrast and restyle notes. Spawn it on every design task; when colour isn't changing it audits the existing tokens for this screen.

### 3. Wave B — components (parallel)
Spawn one **`component-scout`** per item in the component list (cap 8 per wave; group trivial items). Give each its brief from the list, the stack, the tokens/restyle notes and its motion allowance. Each searches **every** connected component-library MCP that fits the stack ([catalog](references/component-libraries.md)), compares 2–4 real candidates and returns one pick with an exact install command. Scouts do not install.

### 4. Lead: integrate
Resolve conflicts across picks: one base system, the page's motion budget, consistent radii/type/density between libraries. Install the chosen components **in one sequential pass**, then compose the page with `frontend-ui-engineering`, restyling every installed component to the token table. Write down what came from which library.

### 5. Wave C — review
Spawn **`design-reviewer`** with the run/open instructions, contract, component list and token table. It renders the UI (Playwright MCP, Flutter MCP/Widgetbook), inspects real viewport sizes and states, and attributes each defect to a component. Fix Critical and Important defects; if a component is wrong rather than mis-styled, re-spawn its `component-scout` with the defect. Re-review. Stop after the review passes or after three rounds, and report what remains.

### 6. Report
Personas spawned, MCPs each one actually used or found unavailable, references, components installed per library, token changes, screenshots inspected, defects fixed and remaining limitations. Then close the gate: fill `.design-gate/evidence.json` with what actually happened — `reference_mcp`, `reference_urls`, `color_task`/`color_mcp`, `implementation_task`/`implementation_tool`, `agents_spawned` (persona names, one entry per scout), `component_mcps` (libraries the scouts queried), `rendered_review`, `issues_reviewed`, and `blocked: true` with the reason if any wave was blocked. Run `python3 <agent-skills>/scripts/design-gate.py .design-gate/evidence.json`; when it prints PASS, delete `.design-gate/active`. Never write evidence for steps that did not run.

**Harness without subagents:** run each persona's instructions yourself in the same order, one component at a time, and say that the fan-out ran sequentially.

## Failure policy
- Never silently skip required research, color validation or visual inspection.
- If a required MCP is missing, disconnected, rate-limited or unauthorized, stop the affected wave and give the exact blocker and setup action (for component libraries: `python3 scripts/setup-mcps.py --client claude --profile components --apply`). Do not claim completion or substitute invented research.
- An explicitly user-approved manual fallback can be used, but must be identified as such; never pretend an MCP ran.
- No MCP can be used until the client connects/authorizes it. This skill cannot install or force the host to execute tools.
- Do not send private project assets to third parties without authorization.

## Common Rationalizations
- "I can write this card/hero myself faster": a library component has states, accessibility and motion already worked out; search first, hand-roll only what no library covers.
- "More animation looks more premium": one or two animated set pieces per page; the rest should be calm.
- "The installed component looks fine in its default colours": it has to wear the product's tokens before it counts as done.
- "It's one page, one agent can design it": one agent designs the page as a single picture and hand-rolls the parts. Scouts per component are what put library-quality components in each slot.
- "Mixing HeroUI, Mantine and shadcn gives the best of each": it gives three design languages and three theming systems. One base per project.

## Red Flags
- A second base component system added to a project that already has one
- Aceternity/Magic UI pieces shipped in their demo colours and fonts
- React component libraries proposed for a Flutter or native app
- Claiming a component came from a library MCP when it was written by hand
- Animated components with no reduced-motion fallback
- Scouts installing packages in parallel, or the lead skipping Wave B and writing components directly
- A review based on reading code instead of rendered screenshots

## Verification
A UI task is complete only after Waves A–C ran (or ran sequentially and say so), each component was scouted against connected library MCPs, the integrated UI passed a rendered review, and the report lists what each agent used. If any mandatory phase is blocked, label the task BLOCKED, not DONE.

## Related
- `skills/design-reference-research/SKILL.md`
- `skills/color-system-design/SKILL.md`
- `skills/frontend-ui-engineering/SKILL.md`
- [Component library MCPs](references/component-libraries.md)
- Personas: `agents/design-researcher.md`, `agents/color-designer.md`, `agents/component-scout.md`, `agents/design-reviewer.md`
- `/design` command
- `docs/mcp-automation.md`
