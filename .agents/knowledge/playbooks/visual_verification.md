---
name: visual-verification
description: Protocols for UI testing and walkthroughs using screenshots and recordings.
version: 1.0.0
---
# Visual Verification Protocols

## Core Principle
Documentation of UI changes must include visual proof to bridge the gap between "code committed" and "feature working".

## Screenshot Protocol
- **Trigger**: Upon completion of any UI component or page layout.
- **Action**: Use the `generate_image` or browser tools to capture the state.
- **Context**: Force the creation of a visual artifact by explicitly prompting: "Take a screenshot of the final DOM state."

## Recording Protocol
- **Trigger**: Complex user flows or animations.
- **Action**: Use the browser subagent to record the interaction sequence.
- **Embedding**: Embed the `.mp4` or `.png` artifacts directly into the `walkthrough.md` using absolute `file:///` URIs.

## Walkthrough Standard
- Every `walkthrough.md` involving UI changes MUST embed a screenshot or recording.
- Include a "Visual Delta" section explaining the changes from the previous state.
