# .agents/artifacts/ — Ephemeral Runtime Artifacts

This directory stores runtime-generated artifacts that are NEVER committed to git.

Contents (generated at runtime):
- review_<timestamp>.json — ce-correctness-reviewer JSON output
- review_summary.md — /review workflow walkthrough
- backend_status.json — parallel build status (backend agent)
- frontend_status.json — parallel build status (frontend agent)
- browser-state.json — agent-browser auth persistence
- actions.md — walkthrough artifact for PR description
- uat_recording.webp — browser QA recording
- final_render.png — visual verification screenshot
- compound-learning-summary.md — /ce-compound output

All files are cleared after each /ship execution.
