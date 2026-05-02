# Agent Architecture Audit Report

**Repository**: https://github.com/obra/superpowers/tree/main/skills/systematic-debugging  
**Analysis Date**: May 02, 2026  
**Files Analyzed**: https://raw.githubusercontent.com/obra/superpowers/main/skills/systematic-debugging/SKILL.md, https://raw.githubusercontent.com/obra/superpowers/main/README.md, https://raw.githubusercontent.com/obra/superpowers/main/skills/systematic-debugging/root-cause-tracing.md, https://raw.githubusercontent.com/obra/superpowers/main/skills/systematic-debugging/defense-in-depth.md, https://raw.githubusercontent.com/obra/superpowers/main/skills/systematic-debugging/condition-based-waiting.md, https://raw.githubusercontent.com/obra/superpowers/main/skills/systematic-debugging/CREATION-LOG.md, https://raw.githubusercontent.com/obra/superpowers/main/skills/systematic-debugging/find-polluter.sh

## 1. Rules (Persistent Behavioral & Security Constraints)

* Rule 1: Iron Law of Systematic Debugging  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/systematic-debugging/SKILL.md  
  • Excerpt: "NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST" + "ALWAYS find root cause before any fixes"  
  • Implications: Enforces absolute prohibition on symptom fixes, quick patches, or rationalizations under time pressure; any violation (e.g., proposing solutions without tracing) triggers mandatory return to Phase 1.

* Rule 2: Sequential Phase Completion  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/systematic-debugging/SKILL.md  
  • Excerpt: "Must complete each of 4 phases sequentially before next" + red flags like "Quick fix for now", "I know what the problem is", "Just one more change"  
  • Implications: Blocks skipping tests, guessing, multiple simultaneous changes, or skipping evidence gathering; 3+ failed fixes requires architecture re-evaluation.

* Rule 3: Multi-Layer Validation (Defense-in-Depth)  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/systematic-debugging/defense-in-depth.md  
  • Excerpt: "Validate at EVERY layer (Entry, Business Logic, Environment Guards, Debug)"  
  • Implications: Makes certain classes of bugs impossible by requiring 4-layer checks; constrains all implementation to include instrumentation and guards.

* Rule 4: Anti-Rationalization & Bulletproofing  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/systematic-debugging/CREATION-LOG.md  
  • Excerpt: "bulletproofed skill extracted from CLAUDE.md framework... defenses against rationalizations/time pressure"  
  • Implications: Persistent constraint against ad-hoc debugging; skill self-enforces via subagent testing and creation process.

## 2. Workflows (Sequential, Slash-Invokable Procedures)

* Workflow 1: /systematic-debugging (4-Phase Debugging Procedure)  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/systematic-debugging/SKILL.md  
  • Sequence: 1. Root Cause Investigation (reproduce exactly, check recent changes, gather evidence/logs/instrumentation, trace data flow/call stack). 2. Pattern Analysis (find working examples, compare diffs). 3. Hypothesis and Testing (scientific method with single hypothesis + minimal test). 4. Implementation (create failing test first, apply single fix at root, verify; if 3+ fails → question architecture).  
  • Triggers/Dependencies: Invoked on any bug/test failure; depends on superpowers:test-driven-development skill; red flags auto-return to Phase 1.

* Workflow 2: Backward Root-Cause Tracing  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/systematic-debugging/root-cause-tracing.md  
  • Sequence: Start from symptom → trace backward through call chain/stack → add instrumentation/logs → identify original trigger; integrate with find-polluter.sh for isolation.  
  • Triggers/Dependencies: Phase 1 of main workflow; requires stack traces and logging.

* Workflow 3: Defense-in-Depth Validation  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/systematic-debugging/defense-in-depth.md  
  • Sequence: After tracing → add 4-layer validation (Entry → Business Logic → Env Guards → Debug Instrumentation).  
  • Triggers/Dependencies: Post-Phase 4 of main workflow.

* Workflow 4: Condition-Based Waiting (Flakiness Elimination)  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/systematic-debugging/condition-based-waiting.md  
  • Sequence: Replace arbitrary sleeps/timeouts with waitFor(condition) polling loop until predicate met.  
  • Triggers/Dependencies: Test reliability phase; includes TypeScript example implementation.

## 3. Skills (Modular Capabilities & Tools)

* Skill 1: systematic-debugging  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/systematic-debugging/SKILL.md  
  • Description: Core agentic skill enforcing 4-phase root-cause-first debugging for all bugs/test failures in coding agents.  
  • Inputs/Outputs: Input=bug/symptom; Output=verified root fix + tests; references TDD skill.  
  • Implementation excerpt: "Four Phases workflow - 1. Root Cause Investigation... 4. Implementation"

* Skill 2: root-cause-tracing  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/systematic-debugging/root-cause-tracing.md  
  • Description: Backward call-chain tracing with stack instrumentation to locate original trigger.  
  • Inputs/Outputs: Input=symptom location; Output=source trigger + evidence.  
  • Implementation excerpt: "Backward tracing workflow from symptom to source trigger, with examples, stack trace instrumentation"

* Skill 3: defense-in-depth  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/systematic-debugging/defense-in-depth.md  
  • Description: 4-layer validation to prevent bugs at entry, logic, env, and debug layers.  
  • Inputs/Outputs: Input=traced root cause; Output=hardened code with guards.  
  • Implementation excerpt: "4-layer validation rule (Entry, Business Logic, Env Guards, Debug)"

* Skill 4: condition-based-waiting  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/systematic-debugging/condition-based-waiting.md  
  • Description: Polling-based waitFor(condition) to replace flaky sleeps in tests.  
  • Inputs/Outputs: Input=condition predicate; Output=reliable test wait.  
  • Implementation excerpt: "Condition-based waiting instead of arbitrary sleeps for tests" + example .ts code.

* Skill 5: find-polluter (Bisection Tool)  
  • Source file: https://raw.githubusercontent.com/obra/superpowers/main/skills/systematic-debugging/find-polluter.sh  
  • Description: Script for isolating test pollution (unwanted state/files) via bisection.  
  • Inputs/Outputs: Inputs=test pattern + pollution path; Output=culprit test identified.  
  • Implementation excerpt: "Usage: ./find-polluter.sh <pollution_path> <test_pattern>"

## 4. Interconnections & Architecture Summary

* How Rules constrain Workflows/Skills: Iron Law + red flags + sequential rules gate every phase of /systematic-debugging workflow and all sub-skills (root-cause-tracing, defense-in-depth); anti-rationalization rules (from CREATION-LOG.md) prevent any skill bypass under pressure; defense-in-depth rule injects validation into Implementation phase.

* How Workflows invoke Skills: Main 4-phase workflow directly invokes root-cause-tracing (Phase 1), defense-in-depth (Phase 4), condition-based-waiting (test phase), find-polluter (isolation), and superpowers:test-driven-development; each sub-workflow returns control to parent.

* Overall agent design insights: This is a composable, bulletproofed skill module within the superpowers framework for coding agents. Designed for automatic invocation on bugs; enforces mechanistic, scientific debugging over ad-hoc LLM guessing; integrates via slash-invokable patterns and subagent testing for self-verification. Zero tolerance for symptom-only fixes makes the agent reliable and auditable.
