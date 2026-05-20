# Worktree Agent Rule

This rule applies to autonomous agent runs, especially `/goal` runs.

## Purpose

Agents must be allowed to work independently, but only inside a safe and disposable workspace.

The expected model is:

```text
main vault = stable source of truth
agent worktree = disposable execution space
```

## Hard Boundary

The agent must not modify the main vault directly.

The agent must only edit files inside the current Git worktree.

The agent must not write, move, delete, or generate files outside the current repository root.

## Required Preflight

Before making any file changes, the agent must run:

```bash
git status
git branch --show-current
git rev-parse --show-toplevel
```

The agent must inspect the result before continuing.

## Stop Conditions

The agent must stop immediately if the current branch is:

```text
main
master
```

The agent must stop immediately if the current branch does not start with:

```text
agent/
```

The agent must stop immediately if the current working directory is the main vault path.

For this vault, the main vault path is:

```text
D:\NoteBookLLM_Br
```

Approved worktree paths should be under:

```text
D:\_agent_worktrees\
```

If any stop condition is met, the agent must report:

```text
WRONG_BRANCH_OR_WORKTREE
```

and must not continue.

## Allowed Actions

Inside the approved worktree, the agent may:

- edit files related to the assigned task
- create temporary reports inside the repo
- run validation commands
- inspect diffs
- propose merge recommendations

## Forbidden Actions

The agent must not:

- modify `main` directly
- auto-merge into `main`
- delete source files unless explicitly requested
- change global Git config
- write outside the current repo root
- run destructive commands without explicit approval
- modify unrelated skills, workflows, or rules

## Completion Report

At the end of the task, the agent must report:

```yaml
TASK_REPORT:
  branch: ""
  worktree_path: ""
  changed_files: []
  commands_run: []
  validation:
    status: "PASS | FAIL | NOT_RUN"
    notes: ""
  rollback:
    command: ""
  merge_recommendation: "MERGE | DO_NOT_MERGE | REVIEW_REQUIRED"
```

## Rollback Command Format

The rollback command should follow this pattern:

```bash
cd /d D:\NoteBookLLM_Br
git worktree remove D:\_agent_worktrees\<worktree-name> --force
git branch -D agent/<branch-name>
```

## Merge Rule

The agent may recommend merge, but must not perform merge unless the user explicitly asks.

Merge into `main` must happen one branch at a time.

After each merge, validation must be run from the main vault.
