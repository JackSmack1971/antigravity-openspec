---
name: react-skill-invocation
description: Contextually triggered code execution for React/Next.js tasks.
---
# React Best Practices — Agent Skill Invocation Trigger

## Purpose
An implicit, contextually triggered workflow. It automatically activates the React Best Practices skill when specific domain tasks are detected.

## Trigger & Execution Sequence
1. **Detection:** The agent detects a React or Next.js task based on the user prompt or the presence of specific files (e.g., `package.json` with React dependencies, `.tsx`/`.jsx` files).
2. **Load Payload:** The agent dynamically loads the compiled `AGENTS.md` payload for the React Best Practices skill.
3. **Apply Rules:** The agent filters and applies the relevant rules based on category and impact (e.g., performance, accessibility, security).
4. **Output:** The agent outputs or implements highly optimized, rule-compliant React/Next.js code.
