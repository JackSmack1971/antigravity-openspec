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
```ts
// WRONG — Sequential (2-10x slower, blocks render)
const user = await getUser(id);
const posts = await getPosts(id);

// CORRECT — Parallel (minimal latency)
const [user, posts] = await Promise.all([getUser(id), getPosts(id)]);
```

### BUNDLE: No Barrel File Imports
```ts
// WRONG — imports entire barrel (bundle bloat)
import { Button, Input } from './components/index';
// CORRECT — direct source import
import { Button } from './components/Button';
import { Input } from './components/Input';
```

## HIGH Priority Rules
- React Server Components (RSC): use for all non-interactive UI (reduces client JS bundle).
- Avoid unnecessary re-renders: useMemo/useCallback ONLY with stable, meaningful deps.
- Data fetching: server-side in RSC or server actions. Avoid useEffect for initial data.
- State: colocate as close to consumer as possible. No prop drilling > 2 levels.

## MEDIUM Priority Rules
- useEffect for derived state → WRONG. Compute during render instead.
- Large components → split at 100+ lines into smaller focused components.

## Verification
Before any ship: pnpm build → must exit 0 with zero warnings.

## Quality Gates
- [ ] No sequential awaits for independent operations (Promise.all used)
- [ ] No barrel imports in critical render paths
- [ ] pnpm build exits 0, zero warnings
