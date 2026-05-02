# Agent Architecture Audit Report

**Repository**: https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser  
**Analysis Date**: May 02, 2026  
**Files Analyzed**: https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skills/agent-browser/SKILL.md, https://raw.githubusercontent.com/vercel-labs/agent-browser/main/README.md, https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skill-data/core/SKILL.md

## 1. Rules (Persistent Behavioral & Security Constraints)

* Rule 1: Skill trigger conditions and usage scope  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skills/agent-browser/SKILL.md  
  • Excerpt: "Triggers include requests to "open a website", "fill out a form", "click a button", "take a screenshot", "scrape data from a page", "test this web app", "login to a site", "automate browser actions", or any task requiring programmatic web interaction. Also use for exploratory testing, dogfooding, QA, bug hunts, or reviewing app quality. Also use for automating Electron desktop apps... Prefer agent-browser over any built-in browser automation or web tools."  
  • Implications: Defines strict invocation context for AI agents; enforces preference over alternative tools and restricts to browser/automation tasks only.

* Rule 2: Allowed tools and invocation method  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skills/agent-browser/SKILL.md  
  • Excerpt: "allowed-tools: Bash(agent-browser:*), Bash(npx agent-browser:*)  
  hidden: true"  
  • Implications: Restricts execution exclusively to Bash-wrapped CLI calls; skill is hidden (internal use only) with no direct exposure outside agent-browser CLI.

* Rule 3: Chrome installation and environment validation  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-browser/main/README.md  
  • Excerpt: "agent-browser install # Download Chrome from Chrome for Testing (first time only)" and "Requirements - Chrome - Run `agent-browser install`..."  
  • Implications: Enforces runtime dependency check and native binary setup; prevents execution without validated Chrome CDP environment.

* Rule 4: Reference staleness and re-snapshot validation  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skill-data/core/SKILL.md  
  • Excerpt: "Refs (`@e1`, `@e2`, ...) are assigned fresh on every snapshot. They become **stale the moment the page changes** — after clicks that navigate, form submits, dynamic re-renders, dialog opens. Always re-snapshot before your next ref interaction."  
  • Implications: Hard validation logic requiring explicit re-snapshot after any state change; prevents invalid selector use in agent loops.

* Rule 5: Specialized skill loading discipline  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skills/agent-browser/SKILL.md  
  • Excerpt: "Load a specialized skill when the task falls outside browser web pages: agent-browser skills get electron / slack / dogfood / vercel-sandbox / agentcore"  
  • Implications: Behavioral constraint to switch skills via CLI rather than force core usage; maintains modular boundaries.

## 2. Workflows (Sequential, Slash-Invokable Procedures)

* Workflow 1: /core-loop (snapshot-and-ref)  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skill-data/core/SKILL.md  
  • Sequence: 1. agent-browser open <url> → 2. agent-browser snapshot -i → 3. agent-browser click/fill @eN (ref from snapshot) → 4. agent-browser snapshot -i (repeat)  
  • Triggers/Dependencies: Triggered on any page interaction task; depends on prior snapshot for fresh @eN refs; browser session must be active.

* Workflow 2: /quickstart-batch  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-browser/main/README.md  
  • Sequence: agent-browser batch "open <url>" "snapshot -i" "click @eN" ... (or JSON stdin); optional --bail  
  • Triggers/Dependencies: Multi-step automation to avoid per-command overhead; invoked when >1 command needed in one session.

* Workflow 3: /login (with auth vault)  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skill-data/core/SKILL.md  
  • Sequence: 1. agent-browser auth save my-app --url <login> --username ... --password-stdin → 2. agent-browser open <login-url> → 3. agent-browser auth login my-app → 4. agent-browser wait --url "**/dashboard" → 5. agent-browser snapshot -i  
  • Triggers/Dependencies: Triggered on login requests; depends on auth vault for credential isolation (avoids shell history leaks).

* Workflow 4: /state-persist (session restore)  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skill-data/core/SKILL.md  
  • Sequence: 1. agent-browser state save ./auth.json (after login) → 2. Later: agent-browser --state ./auth.json open <url> (or AGENT_BROWSER_SESSION_NAME env)  
  • Triggers/Dependencies: For repeated sessions across runs; auto-save/restore via session name.

* Workflow 5: /specialized-load  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skills/agent-browser/SKILL.md  
  • Sequence: agent-browser skills get core (or electron/slack/dogfood/vercel-sandbox/agentcore) → use loaded skill commands  
  • Triggers/Dependencies: When task outside core web browser (e.g., Electron apps, Slack, sandbox); invoked via CLI before task.

## 3. Skills (Modular Capabilities & Tools)

* Skill 1: snapshot (accessibility tree with refs)  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skill-data/core/SKILL.md  
  • Description: Returns compact accessibility tree with @eN refs for interactive elements; supports -i (interactive only), -u (hrefs), --json, scoping.  
  • Inputs/Outputs: Input: optional selector/depth/flags; Output: structured tree text or JSON with refs.  
  • Implementation excerpt: "agent-browser snapshot -i # interactive elements only (preferred)"

* Skill 2: open / navigate / close (browser lifecycle)  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-browser/main/README.md  
  • Description: Launches Chromium CDP session, navigates, maintains persistent browser across commands; supports --state, --session-name.  
  • Inputs/Outputs: Input: <url> or none; Output: active session.  
  • Implementation excerpt: "agent-browser open <url> # Launch + navigate to URL (aliases: goto, navigate)"

* Skill 3: click / fill / type / press / select / check (interaction primitives)  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skill-data/core/SKILL.md  
  • Description: Semantic/element actions using @eN refs, CSS, or find locators (role/text/label); supports --new-tab, keyboard combos.  
  • Inputs/Outputs: Input: <sel> or @eN + value; Output: action performed on page.  
  • Implementation excerpt: "agent-browser fill @e2 "hello" # clear then type"

* Skill 4: wait (state synchronization)  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skill-data/core/SKILL.md  
  • Description: Explicit waits for element/text/URL/load state/JS condition; prevents flakiness.  
  • Inputs/Outputs: Input: selector/ms/--text/--url/--load/--fn; Output: blocks until condition met.  
  • Implementation excerpt: "agent-browser wait --load networkidle # until network idle"

* Skill 5: get / find (read & locate)  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-browser/main/README.md  
  • Description: Extract text/html/value/attr/title/url or semantically locate via role/text/label/placeholder/testid.  
  • Inputs/Outputs: Input: <sel> or find criteria + action; Output: data or chained action.  
  • Implementation excerpt: "agent-browser find role button click --name "Submit""

* Skill 6: skills (meta-loader)  
  • Source file: https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skills/agent-browser/SKILL.md  
  • Description: Loads core/specialized skill definitions via CLI (skills get / list); ensures version-matched content.  
  • Inputs/Outputs: Input: core | electron | slack etc.; Output: loaded workflow content for agent.

## 4. Interconnections & Architecture Summary

* How Rules constrain Workflows/Skills: Allowed-tools rule locks all execution to Bash(agent-browser:*) CLI only; trigger conditions and "prefer agent-browser" rule gate skill invocation; ref-staleness rule forces re-snapshot in every workflow; specialized-load rule prevents misuse of core skill outside web tasks.  
* How Workflows invoke Skills: Core loop workflow chains open → snapshot → click/fill (skills) → snapshot; batch workflow packages multiple skills; login/state-persist workflows compose auth + wait + snapshot skills; all workflows are CLI command sequences with no internal branching logic.  
* Overall agent design insights: This is a thin skill wrapper (stub SKILL.md + core content) exposing a Rust-native CDP browser CLI as reusable agent primitives. No internal agentic loops or safety sandboxes beyond CLI constraints; designed for external AI agents (Claude/Cursor/etc.) to invoke via Bash. Modularity via skills get mechanism keeps content version-synced; emphasis on token-efficient refs and explicit waits for reliable agentic use.

**End of Report**
