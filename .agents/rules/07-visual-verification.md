---
name: 07-visual-verification
description: Mandatory visual proof requirements for browser UI tasks and background actuation.
globs: ["src/components/**/*", "*.html", "*.css", "**/*.jsx", "**/*.tsx"]
alwaysApply: false
---
# Frontend Walkthrough & Visual Verification Standards

## 1. Mandatory Visual Proof
- For any task modifying the UI, you MUST actuate the Browser Subagent to verify the changes upon completion.
- You must take a screenshot artifact of the final rendered DOM state.

## 2. Walkthrough Generation
- NEVER complete a frontend task without generating a final Walkthrough artifact.
- The Walkthrough MUST embed the generated screenshot and/or browser recording.
- Include a "Visual State Summary" in the Walkthrough describing the exact visual changes for optimal Knowledge Item (KI) extraction.

## 3. Failure State Auditing
- If the browser encounters an Allowlist prompt, MFA login, CAPTCHA, or network timeout, immediately capture a screenshot artifact, halt execution, and request human review.
