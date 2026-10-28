# Free-first Color Tools and MCPs

Availability, package names, quotas and licenses may change. Review upstream documentation and code before installing. This repository does not automatically install MCP servers.

| Resource | URL | Specialization |
|---|---|---|
| Color Theory MCP | https://github.com/JoshuaRamirez/color-theory-mcp | Color harmony, OKLCH/Lab, WCAG, color-blindness simulation, perceptual comparison, gradients and tokens |
| Coolors MCP | https://github.com/x51xxx/coolors-mcp | App-wide palettes, tonal scales, semantic roles and Material 3 theme exploration; independent project, not necessarily official Coolors service |
| Color Palette Extractor MCP | https://github.com/aka-kika/color-palette-extractor-mcp | Extract candidate colors from UI screenshots and derive variants |
| Colors & Fonts MCP | https://www.colorsandfonts.com/mcp/ | Palette and typography discovery / export; confirm hosted free-tier restrictions |
| RNV Color MCP | https://github.com/RNVizion/rnv-color-mcp | Save/retrieve named palette selections across sessions |

## Complementary free reference websites (not necessarily MCPs)
- https://coolors.co/ — manual palette inspiration; verify commercial and API limits
- https://color.adobe.com/ — color wheel, harmonies and palette reference
- https://www.realtimecolors.com/ — test palette and typography in sample layouts
- https://webaim.org/resources/contrastchecker/ — independent numeric WCAG contrast cross-check
- https://oklch.com/ — OKLCH exploration and gamut visualization

## Recommended routing
- **Brand direction:** Color Theory MCP → 2–3 harmonious options → independent contrast test
- **App theme:** Coolors MCP → semantic tokens → cross-check text/background pairs
- **Screenshot reference:** Palette Extractor MCP → filter reference colors → derive distinct project palette
- **Financial heatmaps/charts:** perceptual scales, neutral zero, accessible diverging hue pairs, visible +/- indicators
- **Token memory:** RNV Color MCP or, preferably, version-controlled platform tokens in the app

## Installation guidance
Read each linked project's README for its current command and server configuration. Do not infer a registry package or remotely execute unreviewed packages. In Claude Code, confirm MCP connectivity with `claude mcp list`, then run a test tool call. Different clients use different configuration formats.

## Color validation rules
- WCAG AA normal text: >= 4.5:1; large text >= 3:1.
- Non-text visual components/focus indicators where applicable: >= 3:1 against adjacent colors.
- Check actual composited color for transparency, disabled states, chart labels and hover/focus.
- Distinguish perceptual harmony from measured accessibility.
- Preserve documented tokens, access dates, and sources.
