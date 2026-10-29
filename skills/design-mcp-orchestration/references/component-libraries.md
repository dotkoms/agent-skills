# Component Library MCPs

Use these when a UI/frontend design is being **built**, not only researched. Each one lets the agent search a real component library and install its source, instead of inventing components from scratch. Every entry below was checked against the provider's own docs and npm on 2026-10-29; re-check before relying on pricing or tiers.

All of these are **React + Tailwind** (Mantine uses its own styling). None of them apply to Flutter, SwiftUI or native mobile.

## Catalog

| Library | Best for | How the agent reaches it | Cost |
|---|---|---|---|
| [shadcn/ui](https://ui.shadcn.com/docs/mcp) | Dashboards, forms, navigation, app UI; the base the animated libraries sit on | Official shadcn MCP (`npx shadcn@latest mcp`) | Free |
| [Magic UI](https://magicui.design) | Animated text, backgrounds, cards, effects | Dedicated MCP (`@magicuidesign/mcp`) and `@magicui` registry | Free components |
| [Aceternity UI](https://ui.aceternity.com) | Premium-looking animations, 3D effects | shadcn MCP via `@aceternity` registry | Free components |
| [Animate UI](https://animate-ui.com/docs/mcp) | Animated buttons, menus, dialogs, icons | shadcn MCP via `@animate-ui` registry | Free |
| [Eased](https://github.com/easedui/ui) | Smooth motion and interactive elements; respects `prefers-reduced-motion` | Dedicated MCP (HTTP, `https://eased.dev/api/mcp`) and `@eased` registry | Free, MIT (60 components) |
| [Wensity UI](https://ui.wensity.com/docs/mcp) | Animated components and page sections (hero, pricing, FAQ, nav, footer) | Dedicated MCP (`@wensity/mcp`); shows an install plan and waits for approval | Free components; Pro tier needs a token |
| [HeroUI](https://heroui.com/en/docs/react/getting-started/mcp-server) | Complete application interfaces | Dedicated MCP (`@heroui/react-mcp`); HeroUI React v3 only | Open source |
| [Mantine](https://mantine.dev/guides/llms/) | Data-heavy dashboards and forms | Official MCP (`@mantine/mcp-server`), versioned with Mantine | Free |
| [21st.dev](https://21st.dev/mcp) | Community components, animations, templates | Dedicated HTTP MCP; **needs an API key** | Limited free tier; AI generation needs paid AI access |

## Choosing

1. **Follow the stack that's already there.** Read `package.json` and `components.json` first. If the project is on Mantine, use Mantine; if it's on HeroUI, use HeroUI; if it has `components.json`, it's shadcn. Don't introduce a second base system.
2. **One base, then motion on top.** The base is shadcn/ui, HeroUI or Mantine. Magic UI, Aceternity, Animate UI, Eased and Wensity are shadcn/Tailwind-flavoured layers for motion and showpiece sections; add them to shadcn projects, not to Mantine or HeroUI projects.
3. **Pick by job:**
   - App screens, settings, tables, forms: shadcn/ui, or Mantine for data-heavy work, or HeroUI for a full app kit.
   - Landing/marketing sections: Wensity blocks, Magic UI, Aceternity.
   - Micro-interactions on existing controls: Animate UI, Eased.
   - Nothing fits: search 21st.dev community components (key required).
4. **Restyle to the product's tokens.** Installed components land as source in the repo. Map their colours, radii, type and spacing onto the project's existing tokens; a pasted Aceternity hero in default colours is a defect.
5. **Motion has a budget.** One or two animated set pieces per page. Check `prefers-reduced-motion` handling on anything that moves.

## Setup

Automatic (keyless servers only), from the repo root:

```bash
python3 scripts/setup-mcps.py --client claude --profile components           # dry run
python3 scripts/setup-mcps.py --client claude --profile components --apply
```

That registers `shadcn`, `magicui`, `eased`, `wensity`, `heroui` and `mantine`. Equivalent manual commands:

```bash
claude mcp add --scope user shadcn -- npx -y shadcn@latest mcp
claude mcp add --scope user magicui -- npx -y @magicuidesign/mcp@latest
claude mcp add --scope user --transport http eased https://eased.dev/api/mcp
claude mcp add --scope user wensity -- npx -y @wensity/mcp@latest
claude mcp add --scope user heroui -- npx -y @heroui/react-mcp@latest
claude mcp add --scope user mantine -- npx -y @mantine/mcp-server
```

21st.dev needs a key from https://21st.dev/mcp, so it is not automated. Its official installer is `npx @21st-dev/cli@latest init --client claude`; the manual config is an HTTP server at `https://21st.dev/api/mcp` with header `x-api-key`. Keep the key in the client config, never in this repo.

### shadcn registries for the animated libraries

Aceternity and Animate UI have no MCP of their own; the shadcn MCP reaches them through registries declared in the **target project's** `components.json`:

```json
{
  "registries": {
    "@magicui": "https://magicui.design/r/{name}.json",
    "@aceternity": "https://ui.aceternity.com/registry/{name}.json",
    "@animate-ui": "https://animate-ui.com/r/{name}.json",
    "@eased": "https://eased.dev/r/{name}.json"
  }
}
```

Then `npx shadcn@latest add @aceternity/3d-marquee` (or ask the agent to search the registry through the shadcn MCP). Add only the registries the project will use. Eased needs React 19 and Tailwind v4.

## Smoke test

After setup, restart the client and run one narrow search per server (e.g. "animated pricing section", "data table with filters"). A server that is listed but returns nothing counts as **not connected** for the design gate.
