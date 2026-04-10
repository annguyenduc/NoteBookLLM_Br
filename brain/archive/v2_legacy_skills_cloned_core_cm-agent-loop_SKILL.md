---
name: cm-agent-loop
description: "CORE — Thiết kế và triển khai các kiến trúc vòng lặp agent tự động. Từ pipeline tuần tự đơn giản đến vòng lặp PR liên tục với cổng CI/CD. Bao gồm mẫu De-Sloppify và điều phối bầy đàn Subagent song song."
version: 2.0.0
origin: Cherry-picked from ECC (affaan-m/everything-claude-code) + merged cm-core-swarm
tags: [core, automation, pipeline, agent-orchestration, swarm]
---

# cm-agent-loop — Autonomous Agent Loop & Swarm Orchestration

Patterns and architectures for running agents in loops — from simple sequential pipelines to continuous PR loops with CI gates — and for coordinating synchronized agent swarms in parallel workstreams.

## When to Activate

- Setting up multi-step automated execution workflows
- Choosing the right loop architecture for a given problem
- Adding a cleanup pass after agent execution output
- Building automated quality validation pipelines
- A task is too large for a single agent context window
- Multiple independent modules can be implemented in parallel
- Cross-verification by a separate reviewer agent is required

## Instructions

### Loop Pattern Spectrum (simplest to most complex)

| Pattern | Complexity | Best For |
|---------|-----------|----------|
| [Sequential Pipeline](#1-sequential-pipeline) | Low | Daily dev steps, scripted workflows |
| [Continuous PR Loop](#2-continuous-pr-loop) | Medium | Multi-day projects with CI gates |
| [Agent Swarm](#3-agent-swarm-orchestration) | High | Parallel workstreams, large refactors |
| [De-Sloppify Pattern](#4-de-sloppify-pattern) | Add-on | Quality cleanup after any implement step |

---

### 1. Sequential Pipeline

**The simplest loop.** Break work into a sequence of independent steps, each a focused call with a clear objective.

**Design principles:**
1. **Each step is isolated** — Fresh context per call, no context bleed between steps
2. **Order matters** — Steps execute sequentially; each inherits filesystem state from the previous
3. **Exit codes propagate** — Failure at any step stops the pipeline
4. **Avoid negative instructions** — Instead of "don't do X", add a separate cleanup step (see De-Sloppify)

**Typical structure:**
```
Step 1: Implement (let the agent be thorough)
Step 2: De-Sloppify (dedicated cleanup step)
Step 3: Verify (run full test/lint/build suite)
Step 4: Commit / Publish
```

**Model routing by task type:**
```
Research / Analysis     → Strongest model (deep reasoning)
Implement / Write code  → Fast, capable model
Review / Security audit → Strongest model (thorough)
```

**Pass context via file, not prompt length:**
```
# Write priorities/context to a temp file
# Agent reads that file instead of receiving a long prompt
# Keeps context clean and reusable across steps
```

---

### 2. Continuous PR Loop

**Production-grade pipeline** that runs the agent in a loop, creates PRs, waits for CI, and can merge automatically.

**Core loop:**
```
1. Create new branch (e.g., auto/iteration-N)
2. Run agent with execution prompt
3. (Optional) Separate reviewer pass
4. Commit changes
5. Push + create PR
6. Wait for CI checks
7. CI fail? → Auto-fix pass with failure context
8. Merge PR
9. Return to main branch → repeat
```

**Stop conditions:**
- Max iteration count
- Max token cost budget
- Max elapsed time
- Agent self-signals "complete"

**Maintain cross-iteration context via shared notes file:**
```markdown
## Progress
- [x] Completed X (iteration 1)
- [x] Fixed edge case Y (iteration 2)
- [ ] Remaining: need to handle Z

## Next Steps
- Focus on rate-limiting module next
```
The agent reads this file at iteration start and updates it at end.

---

### 3. Agent Swarm Orchestration

**PRO mode.** Govern a synchronized and secure agent swarm for parallel workstreams. Inspired by Claude CLI's `AgentTool` and `TeamCreateTool`.

#### Phase 0: Swarm Architecting

Before launching any Subagent:
1. **Task Partitioning:** Break the large request into independent modules (e.g., Frontend, Backend, API Docs).
2. **Identity Setup:** Assign Personas (`FrontendExpert`, `SecurityAuditor`) and attach `cm-identity-guard` to each Agent.
3. **Communication Protocol:** Define how Agents report progress (via `task.md` or `CONTINUITY.md`).

#### Swarm Lifecycle

| Phase | Action | Goal |
|-------|--------|------|
| **🚀 DEPLOY** | Launch Subagent swarm via AgentManager. | Run workstreams in parallel to increase throughput. |
| **🛰️ MONITOR** | Track Heartbeat and Task status. | Detect and resolve blockers immediately. |
| **🧪 VERIFY** | A separate Subagent reviews another Agent's artifact. | Ensure objectivity and quality (Cross-verification). |
| **📥 MERGE** | Merge all code into the main branch. | Resolve conflicts and complete the workflow. |

#### Security & Permissions

- **Scoped Access:** Each Subagent only has access to directories relevant to its task.
- **Approval Gate:** All critical `Write` or `Execute` commands by a Subagent must be approved by the Host Agent or reported to the User.
- **Credential Protection:** Never allow Subagents to read files containing system secrets.

#### Rules of Discipline

- **No Over-orchestration:** Avoid creating too many Subagents for simple tasks (L0-L1 complexity).
- **Artifact Ownership:** Each artifact (file/doc) must have one Agent as primary owner.
- **Context Preservation:** Always update `CONTINUITY.md` after a Subagent ends its work session.

---

### 4. De-Sloppify Pattern

**An add-on for any loop.** Add a dedicated cleanup step after each implement step.

**The problem:**
When asking an agent to implement with TDD, it may produce:
- Tests that verify language/framework behavior rather than business logic
- Overly defensive error handling for impossible states
- Temporary debug output (console.log, commented code, etc.)

**Why NOT use negative instructions?**
Adding "don't create unnecessary tests" to the implement prompt has side effects:
- Agent becomes hesitant about ALL tests
- Legitimate edge case tests get skipped
- Quality degrades unpredictably

**Solution: Separate step**
```
# Step 1: Implement (let it be thorough)
[Agent implements the feature with full TDD]

# Step 2: De-Sloppify (separate context, focused cleanup)
Review all changes. Remove:
- Tests that verify language/framework behavior rather than business logic
- Redundant type checks the type system already enforces
- Overly defensive error handling for impossible states
- Debug output (console.log, print statements, etc.)
- Commented-out code

Keep ALL business logic tests. Run the test suite after cleanup.
```

**Core principle:**
> Two specialized agents (Implement + Cleanup) outperform one agent constrained by negative instructions.

---

## Pattern Selection Matrix

```
Is the task a single focused change?
├─ Yes → Sequential Pipeline + De-Sloppify
└─ No → Can it be parallelized across modules?
         ├─ Yes → Agent Swarm Orchestration
         └─ No → Is there a written spec/RFC?
                  ├─ Yes → Continuous PR Loop
                  └─ No → Sequential Pipeline + De-Sloppify
```

## Anti-Patterns

1. **Infinite loops without exit conditions** — Always have a limit (iterations, cost, time, or completion signal)
2. **No context bridge between iterations** — Each call starts fresh; use a shared notes file to persist progress
3. **Blind retry after failure** — Do not retry immediately. Capture the error context and feed it to the next attempt
4. **Negative instructions instead of cleanup steps** — Do not say "don't do X". Add a separate step to remove X afterward
5. **Subagents overwriting each other** — Each artifact must have one primary owner; always cross-verify before merge
6. **Nested Subagents deeper than 2 levels** — Creates exponential complexity and infinite loop risk

## Quality Gate

- [ ] Correct loop pattern selected for the task complexity
- [ ] All loops have explicit stop conditions
- [ ] De-Sloppify step present after every major implement step
- [ ] Context persisted across iterations (via shared file or equivalent mechanism)
- [ ] Swarm tasks: each Subagent has scoped access and a clear artifact owner
- [ ] Cross-verification (VERIFY phase) present for any swarm deployment

## Example Triggers

- "I need to automate a daily review-and-commit pipeline"
- "Design a pipeline: implement → test → cleanup → commit"
- "How do I prevent the agent from generating unnecessary boilerplate after implementing?"
- "I want the agent to keep running until the task is fully complete"
- "Set up a swarm to develop module X in parallel."
- "Coordinate Sub-agents to perform a large-scale refactor."
- "Decompose this implementation plan into independent parallel workstreams."
