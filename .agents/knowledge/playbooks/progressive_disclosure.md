---
name: progressive-disclosure
description: Mechanics of on-demand capability injection for Agent Skills. Use this to optimize context window management and token quota.
version: 1.0.0
---
# Progressive Disclosure — Agent Skill Orchestration

## Core Pattern
Skills are not loaded entirely into the prompt at runtime. Instead, the agent traverses three phases: Discovery, Activation, and Execution. This secures capabilities on-demand, preventing context bloat and token quota exhaustion.

## The Three Phases
1. **Discovery**: When a conversation initiates, the agent performs a lightweight scan, seeing *only* the names and descriptions of the skills available in the YAML frontmatter of `SKILL.md` files.
2. **Activation**: When the reasoning model determines a skill is relevant (based on the description), it "cracks open" the skill, reading the full Markdown instructions and best practices.
3. **Execution**: The agent executes the instructions, which may include running local scripts or making external API calls.

## Quality Gate: YAML Precision
- **Trigger**: The `description` field in the YAML frontmatter.
- **Rule**: Avoid vague "do everything" descriptions. Descriptions must be mutually exclusive and task-specific.
- **Impact**: Precise descriptions prevent "Semantic Misrouting" where the wrong skill is activated, flooding the context with irrelevant data.

## Implementation Standard
- Keep `SKILL.md` files focused.
- Use decision trees within the Markdown body to guide the agent.
- Reference external scripts as "Black Boxes" to be executed, not parsed as text.
