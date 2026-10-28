---
name: design-reference-research
description: Research real mobile and web UI references through free inspiration databases and available MCPs, extract reusable patterns, and prepare a design contract before implementing screens. Use for redesigns, screen inspiration, navigation, dashboards, onboarding, fintech, Flutter, SaaS, or landing pages.
---

# Design Reference Research

## Overview
Use real reference screens to inform design decisions without cloning another product. This skill is for discovery and analysis; hand implementation to `frontend-ui-engineering` and platform-specific tools. Read [resource catalog](references/resources.md) and [MCP setup](references/mcp-setup.md) when needed; do not load the full list automatically.

## When to Use
- A user asks for a visual direction, screen redesign, app/web references, or a Mobbin alternative.
- A design agent needs examples for navigation, leaderboards, heatmaps, dashboards, onboarding, forms, or landing pages.
- Existing generated UI feels generic or does not match product identity.

## Process
1. **Audit the product first.** Inspect current repository, screen captures, tokens, components, typography, routes, and available states. Capture invariants and constraints. Do not assume React components are suitable for Flutter.
2. **Pick targeted sources.** Choose 1–2 MCPs or catalogs based on platform: VP0/Banani/Kombai for mobile; Screenrove/Inspo for product UI; One Page Love/A1/Lapa Ninja for web; Figma Community for kits. Consult the resources file for access notes.
3. **Retrieve 3–6 references.** Prefer actual search tools when connected. If an MCP is not installed or unavailable, use permitted browsing; do not claim a reference was inspected when it wasn't. Record URL, screen type, date accessed, pattern, and limitations. Never hallucinate screenshots or tool results.
4. **Extract patterns, not assets.** Evaluate hierarchy, information density, grouping, navigation, responsive behavior, accessibility, interaction, empty/loading/error states, and design-token implications. Identify which ideas fit the current product and which conflict.
5. **Compare 2–3 directions.** Explain each direction's tradeoffs, prioritize the best fit, and state rejected clichés.
6. **Write a design contract** using the template below and seek approval if required by the task; otherwise implement a reversible iteration.
7. **Build and verify** with `frontend-ui-engineering`; for Flutter use Dart/Flutter tooling and Widgetbook if available; for web use Playwright MCP when available. Inspect screenshots and iterate.

## Design contract output
- Screen goal and primary action
- User context and core content priority
- Product constraints and existing design tokens
- 3 reference URLs with extracted patterns
- Selected layout/navigation and 2 rejected alternatives
- States: loading, empty, error, offline, selected, active
- Accessibility: contrast, tap targets, keyboard/focus, semantics
- Responsive dimensions and platform behavior
- Acceptance checks and screenshot review

## Common Rationalizations
- "An inspiration screenshot is a component specification": false; derive behavior and platform semantics.
- "The newest design is best": false; prioritize task fit.
- "Free website browsing equals free unrestricted MCP/API access": false; verify quotas and licensing.
- "We can reproduce the competitor screen exactly": false; borrow patterns, not protected assets or branding.

## Red Flags
- Invented references or unverified MCP installation commands
- Replacing the product's visual language with generic templates
- Shipping a mockup without checking overflow, states or actual device dimensions
- Importing React/Expo UI code directly into Flutter
- Ignoring commercial-use licensing or rate limits

## Verification
- Every referenced screen has a working source URL or is explicitly marked unverified.
- Design contract names product-specific tokens and states.
- Final work is visually checked and compared against the design contract.
- Installation and tool access were tested rather than assumed.

## Related
- `skills/frontend-ui-engineering/SKILL.md` — production UI implementation
- `skills/browser-testing-with-devtools/SKILL.md` — browser QA
