---
name: react-best-practices
description: Use when writing, reviewing, or refactoring any React or Next.js code. Triggers: new React component, data fetching logic, Next.js page/layout/route, bundle optimization task, SSR/SSG patterns, state management, testing React components. Auto-activated for .tsx/.jsx/.ts files in components/ or app/.
version: 1.0.0
user-invokable: true
globs: ["**/*.tsx","**/*.jsx","pages/**","app/**","components/**"]
allowed-tools: Read, Write, Bash
---
# react-best-practices — CRITICAL + HIGH Priority Rules

## CRITICAL Rules (apply FIRST — these cause production outages)

### ASYNC: Promise.all for Independent Operations
- **Requirement**: Use `Promise.all()` for independent async operations. NEVER sequential awaits.
```ts
// CORRECT — Parallel
const [user, posts] = await Promise.all([getUser(id), getPosts(id)]);
```

### BUNDLE: No Barrel File Imports
- **Requirement**: NEVER re-export from `index.ts`. Import directly from the source file.
- **Verification**: Run `grep -r "export * from" src/`.

### SERVER/CLIENT BOUNDARY
- **Requirement**: Provider wrappers MUST be in separate "use client" files. NEVER inline in `layout.tsx`.

### HYDRATION SAFETY
- **Requirement**: Third-party providers must not wrap the root layout directly. Create a `ClientProvider.tsx` wrapper instead.
- **KI Reference**: Check `.agents/knowledge/` for React 19 hydration pitfall KI.

### DATA FETCHING
- **Requirement**: NEVER use `useEffect` for initial data fetching. Use React Query, SWR, or Server Components instead.

### OPTIMIZATION
- **Images**: Always use `next/image` with explicit `width` and `height`.
- **Fonts**: Always use `next/font`. NEVER use `@import` in CSS.

## HIGH Priority Rules
- **TypeScript**: Strict mode ALWAYS enabled.
- **Keys in Lists**: Always use stable IDs, NEVER array indices.
- **Error Boundaries**: Required for all async subtrees.
- **Suspense**: Required for all async server components.
- **RSC**: Use React Server Components for all non-interactive UI.
- **State**: Colocate as close to consumer as possible. No prop drilling > 2 levels.

## Workflow
1. **Activation**: Load this skill (Layer 2) on ANY React/Next.js file change.
2. **Self-Audit**: After implementation, verify code against the CRITICAL rules list above.
3. **Verification**: Pre-commit, run `grep -r "export * from" src/` to confirm no barrel imports.

## Verification
Before any ship: pnpm build → must exit 0 with zero warnings.

## Quality Gates
- [ ] No sequential awaits for independent operations (Promise.all used)
- [ ] No barrel imports in critical render paths
- [ ] pnpm build exits 0, zero warnings
- [ ] Code adheres to L0 Foundational Rules (SIMPLICITY FIRST, SURGICAL EDITS)
