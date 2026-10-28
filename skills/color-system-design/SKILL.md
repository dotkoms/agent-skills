---
name: color-system-design
description: Develop accessible, harmonious, brand-consistent color palettes and semantic UI color tokens using free color-science MCPs. Use for color theory, palette generation, dark/light themes, screenshot color extraction, design tokens, contrast audits, or chart/heatmap color systems.
---

# Color System Design

## Overview
Build a usable interface color system, not just five appealing swatches. Color-science tools and MCPs are optional; follow deterministic contrast checks and preserve existing product identity. See [resource catalog](references/color-tools.md).

## When to Use
- Selecting or refining brand colors or UI themes
- Turning a screenshot/reference into an original palette
- Making dark and light modes or semantic design tokens
- Auditing readability, buttons, charts, heatmaps, alerts, or states
- Choosing accessible financial/trading gain-loss and chart colors

## Process
1. **Read current tokens.** Inspect theme files, brand assets, screenshot references, background elevation, existing chart colors, accessibility constraints and platform.
2. **Identify color roles.** Separate brand/accent, neutral surface scales, text, borders, focus, overlays, interaction states, semantic feedback, and categorical/quantitative data series.
3. **Research/generate options.** When available, use Color Theory MCP for harmony/perceptual comparisons; Coolors MCP for theme generation; Palette Extractor MCP for screenshot seeds. Validate tool output; never fabricate MCP results. Generate 2–3 distinct directions and state their tradeoffs.
4. **Build tonal scales.** Prefer perceptually uniform OKLCH interpolation with bounded chroma/hue; check conversion to sRGB and avoid clipped/out-of-gamut values. Keep neutral surfaces neutral where appropriate.
5. **Validate pairs.** Calculate WCAG 2.2 contrast against actual rendered backgrounds, including buttons and badges. Aim for at least 4.5:1 normal text, 3:1 large text and non-text UI boundaries where required; check hover/disabled/focus states. Color alone must not convey meaning. Document any exceptions and applicable criteria.
6. **Define semantics.** Output tokens for background/surface/elevation, on-surface/text tiers, primary/accent/on-primary, positive/negative/warning/information, focus, border, interactive hover/pressed/disabled, and chart categorical/diverging scales.
7. **Implement in the project's existing stack** (Flutter ThemeData/ColorScheme, CSS custom properties, or design-token JSON). Do not replace current branding without a request.
8. **Verify in context.** Screenshot both themes at real device sizes; test contrast, color-vision deficiencies, and use of red/green in financial charts with redundant signs/labels/patterns. Iterate.

## Deliverables
- Existing palette audit and restrictions
- 2–3 palette options with rationale
- Selected semantic tokens as hex/OKLCH plus dark/light variants where relevant
- Contrast table (foreground, background, calculated ratio, expected criterion, pass/fail)
- Components/screenshots demonstrating hierarchy and states
- Notes on gamut, color vision, and any departures from prior tokens

## Common Rationalizations
- "Complementary colors are automatically readable": incorrect; harmony does not prove contrast.
- "A palette generator produces a complete design system": incorrect; roles and component states matter.
- "Red and green are enough to show gain/loss": incorrect; use numbers, signs and labels.
- "Screenshot colors can simply be copied": incorrect; check licensing, preserve brand identity and derive new roles.

## Red Flags
- Claiming WCAG compliance without calculating contrast
- Mixing arbitrary hex values directly into components
- Saturated accent colors on every surface
- Building palettes without testing dark mode, elevation or data visualization
- Assuming external MCPs are installed solely because they are cataloged

## Verification
- Every contrast claim includes the numeric pair and ratio.
- Roles and component states are resolved for each requested theme.
- Exports match the app's platform/token architecture.
- Palette evaluated in actual layouts, not swatches alone.
