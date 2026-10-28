# Free-first UI/UX Design Resource Catalog

Access models change. "Free browsing" is not the same as a free MCP, source export, commercial license, or unlimited API. Re-check pricing, quotas, endpoints and usage terms before installing. Entries below are leads and references, not claims that every provider is currently unlimited.

## MCP and agent-facing sources

| Resource | Link | Primary use | Free caveat |
|---|---|---|---|
| Inspo MCP | https://inspomcp.dev/ | Real website references, visual styles and palettes | Check current hosted/self-hosted terms |
| Screenrove | https://screenrove.com/agents | Product screen discovery, flow/style comparison | Verify MCP endpoint and rate limits |
| One Page Love MCP | https://onepagelove.com/mcp | Landing-page and one-page-site references | Beta/rate limits may apply |
| VP0 MCP | https://vp0.com/mcp | Mobile/iOS references and structured screen data | Generated code may be Expo/React Native, not Flutter |
| A1 Gallery MCP | https://www.a1.gallery/mcp | Web inspiration by visual characteristics | Limited free request quota |
| shadcn/ui MCP | https://ui.shadcn.com/docs/mcp | React component registry discovery | Open source components; not a mobile UI inspiration database |
| Figma MCP | https://developers.figma.com/docs/figma-mcp-server/ | Read frames/components/context | Plan and access limits; not unlimited free |
| Playwright MCP | https://github.com/microsoft/playwright-mcp | Browser interaction, layout verification | Open source; websites may impose access restrictions |
| Dart/Flutter MCP | https://docs.flutter.dev/ai/get-started | Flutter project analysis, tools and testing | Requires suitable Flutter/Dart SDK and agent support |

## Free-to-browse galleries and libraries

| Resource | Link | Best use | Note |
|---|---|---|---|
| Kombai Gallery | https://kombai.com/gallery/web/ | Web/mobile pattern examples | Browse access does not imply API access |
| Banani References | https://www.banani.co/references/apps | Mobile app patterns and journeys | Check current usage policy |
| VP0 Library | https://vp0.com/ | iOS screen examples | See MCP listing for platform caveat |
| Figma Community | https://www.figma.com/community | Community UI kits and editable assets | Each file has its own license |
| Lapa Ninja | https://www.lapa.ninja/ | Landing page references | Reference-only unless licensed |
| Behance | https://www.behance.net/ | Design case studies and art direction | Do not reuse imagery without permission |
| One Page Love | https://onepagelove.com/ | Landing page examples | Separate browsing vs MCP access |

## Free agent skills and component QA
- UI/UX Pro Max — https://github.com/nextlevelbuilder/ui-ux-pro-max-skill — optional third-party design knowledge skill; review before installing; do not vendor it without checking its license.
- Widgetbook — https://www.widgetbook.io/ — open-source Flutter component catalog / visual QA; hosted services may have paid tiers.
- Existing local `frontend-ui-engineering` and `browser-testing-with-devtools` skills should be used to implement and verify.

## Source selection
- **Flutter mobile / social trading:** VP0, Banani, Kombai; verify with Flutter MCP + Widgetbook.
- **SaaS / fintech dashboards:** Screenrove, Inspo, Figma Community; verify with Playwright.
- **Marketing / launch pages:** One Page Love, A1 Gallery, Lapa Ninja, Inspo.
- **React production component discovery:** shadcn/ui MCP; adhere to existing tokens.
- **Deep style inspiration:** Behance and Figma Community, with licensing checks.

## Minimum source metadata
For each reference preserve: URL, title/product, platform, screen purpose, design patterns observed, capture/access date, and any relevant usage restrictions. If access is unavailable, mark as **not inspected**, not as a completed research finding.
