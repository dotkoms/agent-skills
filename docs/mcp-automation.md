# MCP Bootstrap — Claude Code + Codex

This repository **does not automatically execute external packages or grant permissions** when you install skills. Use this optional, reviewed bootstrap to configure compatible MCP clients.

## Quick start

Clone this repository, then run the script **from its root or any directory**:

```bash
python3 scripts/setup-mcps.py --list
python3 scripts/setup-mcps.py --client claude --profile core  # dry run
python3 scripts/setup-mcps.py --client claude --profile core --apply
python3 scripts/check-mcps.py claude
```

Codex:

```bash
python3 scripts/setup-mcps.py --client codex --profile core --apply
python3 scripts/check-mcps.py codex
```

Or on macOS/Linux: `bash scripts/setup-mcps.sh --client claude --profile core --apply`.

### Profiles
- `core`: Screenrove + One Page Love + Playwright; appropriate for design research and testing.
- `research`: Screenrove + One Page Love.
- `testing`: Playwright only.
- `colors`: currently manual only; vetted server launchers are not confirmed.
- `all`: all **verified launcher entries**, not every cataloged candidate.

## Scopes, repeatability and safety
- Default is **user** scope for Claude Code: shared by Claude projects using that account. Select `--scope local` for one Claude project or `--scope project` for Claude project-level shared settings; follow Claude Code documentation regarding project trust and committing configuration.
- Codex CLI stores MCP registration in its own user configuration.
- Re-running `--apply` skips existing entries; `--force` explicitly removes/replaces names, so review before using.
- `--apply` invokes the installed client command; plain mode prints commands without executing them.
- No secrets are embedded. OAuth/API-key providers still require manual authorization.
- External MCPs have access to data permitted by the host client. Only authorize trusted providers. Review remote URLs, package dependencies and server tool permissions.
- The catalog in `mcp/servers.json` is the single source of truth for bootstrap profiles.
- CLI list success proves **registration**, not that an MCP responds correctly. Test a real search/interaction after setup. CLI behavior may change with versions.

## Manual candidates
See `mcp/servers.json` for Inspo, VP0, A1 Gallery, Figma, Flutter, shadcn/ui and color-related MCP links. These are deliberately not bulk-installed without verifying each transport, package, authentication requirement and free usage terms. Copy a provider's official setup instructions into your client and add a smoke test before moving it into an automatic profile.

## Adding a new reviewed server
1. Audit publisher, package/source, transport, URL, cost and auth requirements.
2. Add `http` or `stdio` entry in `mcp/servers.json`; avoid inline secrets.
3. Put the server name in the relevant profile(s).
4. Test dry-run, apply, repeated apply and a real MCP tool call on supported clients.
5. Update the skill's resources file with any rate limits or requirements.
