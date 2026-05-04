Antigravity isn't just a chatbot; it's an agentic AI designed to pair program with you. While it comes with a strong set of core system rules, its true power unlocks when you customize it to match your personal or team's coding style. This guide covers everything about **Antigravity rules** — from basic setup to the new **AGENTS.md** cross-tool standard introduced in v1.20.3 — with practical, copy-paste examples you can use today.

Get the latest on AI, LLMs & developer tools

New MCP servers, model updates, and guides like this one — delivered weekly.

📚500+ Curated Rules

### Explore the Rules Library

Pre-made [coding rules](https://antigravity.codes/rules) for TypeScript, Python, React, and 25+ technologies. One-click copy.

[Browse Rules →](https://antigravity.codes/rules)

---

## How to Add Rules (The Easy Way)

You don't need to be a coding wizard to add rules. Antigravity has a built-in interface that makes it super simple. Just follow these steps:

---

## Rules File Format and Locations

Antigravity reads rules from several file types. Understanding where each file lives and what it does helps you organize your rules effectively.

### Global Rules (Apply to All Projects)

Global rules live in your home directory. When you click **\+ Global** in Antigravity, it creates this file automatically:

```
~/.gemini/GEMINI.md      # Antigravity global rules
~/.gemini/AGENTS.md      # Cross-tool global rules (new in v1.20.3)
```

These rules apply to every project you open in Antigravity. Use them for personal preferences like language, coding style, and response behavior.

### Workspace Rules (Project-Specific)

Workspace rules live inside your project directory. These are the files Antigravity checks:

```
your-project/
├── GEMINI.md              # Project-level Antigravity rules
├── AGENTS.md              # Project-level cross-tool rules
├── .agent/rules/          # Additional workspace rules
│   ├── code-style.md
│   └── testing.md
└── src/
    └── components/
        └── AGENTS.md      # Nested directory-specific rules
```

Nested

```
AGENTS.md
```
files in subdirectories let you define rules that only apply when the agent works in that specific folder. Enable this in **Settings → Agent → Load nested AGENTS.md files**.

### Which File Should You Use?

- **GEMINI.md** — For Antigravity-specific settings. Takes highest priority.
- **AGENTS.md** — For rules shared across Antigravity, Cursor, and Claude Code.
- **.agent/rules/** — For organizing multiple workspace rules into separate files.

---

## AGENTS.md: Cross-Tool Rules (New in v1.20.3)

Starting with Antigravity v1.20.3 (March 5, 2026), the IDE reads rules from

```
AGENTS.md
```
in addition to
```
GEMINI.md
```
. This is one of the most significant rules updates since launch.

### What Is AGENTS.md?

```
AGENTS.md
```
is a cross-platform rules file that works across multiple AI coding tools. Instead of maintaining separate rules files for each tool, you write one
```
AGENTS.md
```
and every compatible tool reads it. Currently supported by:

- **Google Antigravity** (v1.20.3+)
- **Cursor**
- **Claude Code**

The agent reads

```
AGENTS.md
```
at the start of each session and applies the rules throughout its work. The file uses plain Markdown, so there is no special syntax to learn.

### AGENTS.md vs GEMINI.md: Precedence Rules

When both files exist in the same directory, Antigravity follows a clear hierarchy:

1. **GEMINI.md** — Highest priority. Antigravity-specific overrides.
2. **AGENTS.md** — Lower priority. Shared cross-tool foundation.

When the same rule appears in both files, **GEMINI.md takes precedence**. This lets you keep universal standards in

```
AGENTS.md
```
while using
```
GEMINI.md
```
for Antigravity-specific behavior.

### Recommended Setup for Multi-Tool Teams

If your team uses multiple AI coding tools, structure your rules like this:

```
project-root/
├── AGENTS.md        # Shared rules (all tools read this)
├── GEMINI.md        # Antigravity-specific overrides
├── .cursorrules     # Cursor-specific overrides
└── CLAUDE.md        # Claude Code-specific overrides
```

This avoids duplication while preserving each tool's unique capabilities.

### Example AGENTS.md for a Web Project

```
# AGENTS.md — Web App Project Rules

## Tech Stack
- Frontend: Next.js 15, React 19, TypeScript 5
- Styling: Tailwind CSS v4
- Backend: Cloudflare Workers, Hono
- Database: Supabase (PostgreSQL)

## Code Quality
- ESLint + Prettier are pre-configured — do not modify settings
- Keep cyclomatic complexity under 10 per function
- Aim for files under 300 lines

## Testing
- Write unit tests for all utility functions
- Use Vitest for unit tests, Playwright for E2E
- Minimum 80% coverage on new code

## Security
- Store all secrets in .env.local — never hardcode credentials
- Never log API keys or tokens
- Validate all user input before processing

## Git Conventions
- Use conventional commits (feat:, fix:, docs:, etc.)
- Keep PRs under 400 lines of diff when possible
```

### Known Issue: Global GEMINI.md Path Conflict

If you use both Antigravity and Gemini CLI on the same machine, be aware that both tools write to

```
~/.gemini/GEMINI.md
```
. This can cause configuration pollution where instructions meant for one tool leak into the other.

**Workaround:** Add a comment header to the top of your global

```
GEMINI.md
```
separating the sections for each tool, or use
```
AGENTS.md
```
for shared rules and keep
```
GEMINI.md
```
minimal with only Antigravity-specific overrides.

---

## The Hierarchy of Rules

To understand how Antigravity makes decisions, it helps to know the hierarchy of instructions it follows:

1. **System Rules (Immutable):** These are the core directives from Google Deepmind. They define the agent's identity (e.g., "Always plan before coding," "Create premium designs"). You cannot change these.
2. **GEMINI.md (Highest User Priority):** Antigravity-specific rules that override everything below them. Use this for Antigravity-only behavior.
3. **AGENTS.md (Cross-Tool Foundation):** Shared rules read by Antigravity, Cursor, and Claude Code. Applied after GEMINI.md, so conflicting rules defer to GEMINI.md.
4. **.agent/rules/ (Workspace Supplements):** Additional rule files in the workspace rules directory. Great for organizing rules into separate concerns. Check out our [rules library](https://antigravity.codes/rules) for inspiration.

## Types of User Rules

You can define rules at two different levels:

### 1\. Global Rules

These rules apply to **all** your projects. They are perfect for your personal preferences that don't change from project to project.

- *"Always use TypeScript."*
- *"Be concise in your explanations."*
- *"Never use \`var\`, always use \`const\` or \`let\`."*

**How to set them:** Click + Global in the Customizations panel, or manually edit

```
~/.gemini/GEMINI.md
```
(Antigravity-only) or
```
~/.gemini/AGENTS.md
```
(cross-tool).

### 2\. Workspace Rules

These rules apply only to the **current project**. They are essential for enforcing team standards or project-specific architectural patterns.

- *"Use \`shadcn/ui\` for all new components."*
- *"Follow the Container/Presenter pattern."*
- *"This project uses Next.js 14 App Router."*

**How to set them:** Create

```
GEMINI.md
```
or
```
AGENTS.md
```
in your project root, or add files to
```
.agent/rules/
```
. Need framework-specific rules? Our [rules collection](https://antigravity.codes/rules) has ready-to-use templates.

---

## Copy-Paste Antigravity Rules Examples

Here are practical, ready-to-use rules you can drop into your

```
GEMINI.md
```
or
```
AGENTS.md
```
right now. For hundreds more, visit our [full rules library](https://antigravity.codes/rules).

### Example 1: TypeScript React Project

```
## Tech Stack
- Framework: Next.js 15 with App Router
- Language: TypeScript (strict mode)
- Styling: Tailwind CSS v4
- UI Components: shadcn/ui

## Code Style
- Use functional components only — no class components
- Prefer named exports over default exports
- Use 'interface' for object shapes, 'type' for unions/intersections
- Always add JSDoc comments to exported functions
```

### Example 2: Python Backend API

```
## Tech Stack
- Language: Python 3.12
- Framework: FastAPI
- ORM: SQLAlchemy 2.0
- Testing: pytest

## Code Style
- Use type hints on all function signatures
- Follow PEP 8 — max line length 88 (Black formatter)
- Use Pydantic models for request/response validation
- Prefer async/await for I/O operations
```

### Example 3: Safety and Guardrails

```
## Critical Safety Rules
- Always ask for user confirmation before writing to database
- Never deploy to production without explicit approval
- Do not delete files without explicit user confirmation
- Never commit .env files or secrets to git

## Error Handling
- Always wrap external API calls in try/catch
- Log errors with context (function name, input params)
- Return user-friendly error messages, never raw stack traces
```

### Example 4: Code Review and Quality

```
## Code Quality
- Keep functions under 30 lines
- Keep files under 300 lines — split if larger
- Cyclomatic complexity must stay under 10
- No console.log in production code — use a logger

## Testing Requirements
- Write unit tests for every new utility function
- Integration tests for API endpoints
- Minimum 80% coverage on new code
```

### Example 5: Communication and Behavior

```
## Response Style
- Be concise — skip basic explanations
- When suggesting changes, explain the 'why' not just the 'what'
- If you see a potential bug, stop and ask before proceeding
- Always suggest the simplest solution first

## Git Workflow
- Use conventional commits (feat:, fix:, docs:, refactor:)
- Write descriptive PR titles under 72 characters
- Include a brief summary of changes in commit body
```

### Example 6: Monorepo / Multi-Package Project

```
## Project Structure
- This is a Turborepo monorepo
- packages/ui — shared React component library
- apps/web — Next.js frontend
- apps/api — Express backend

## Rules
- Never import directly between apps — use packages
- Shared types go in packages/types
- Run 'turbo lint' before committing
```

### Example 7: Global Personal Preferences

```
## My Preferences
- Always respond in English
- Use 2-space indentation
- Prefer const over let — never use var
- Use arrow functions for callbacks
- Add a blank line between logical sections
- When in doubt, ask me rather than guessing
```

---

## Need Inspiration? Browse the Library

Not sure where to start? We've curated a comprehensive library of rules for popular technologies. Whether you're looking for [TypeScript best practices](https://antigravity.codes/rules/typescript),[Python standards](https://antigravity.codes/rules/python), or [React patterns](https://antigravity.codes/rules/react), we have you covered.

### Explore the Antigravity Rules Library

Discover hundreds of pre-made rules to supercharge your agent.

[Browse All Rules →](https://antigravity.codes/rules)

## What Can You Customize?

You can control almost every aspect of how Antigravity works. Here are the main categories. For ready-made examples, explore our [curated rules library](https://antigravity.codes/rules).

### A. Tech Stack & Libraries

Don't let the AI guess. Tell it exactly what tools you want to use.

```
# Example Rule
- Framework: Next.js 14
- Styling: Tailwind CSS
- State Management: Zustand
```

### B. Coding Style

Enforce your linting rules and stylistic preferences naturally.

```
# Example Rule
- Prefer functional components over classes.
- Use named exports for components.
- Always add JSDoc comments to exported functions.
```

### C. Behavior

Adjust how the agent interacts with you.

```
# Example Rule
- If you see a potential bug, stop and ask me before proceeding.
- Explain complex logic, but skip the basics.
- Always respond in Spanish.
```

---

## Deep Customization: Hacking the System

Beyond basic rules, you can tap into Antigravity's core "Agentic" features. Here is what's happening under the hood and how you can control it.

### 1\. Agentic Mode & Artifacts

Antigravity operates in a loop: **Plan → Execute → Verify**. It tracks this state using specific files called "Artifacts". You can create rules to change how these artifacts are used.

- **task.md**: The living checklist.*Rule idea: "Always break tasks down into granular sub-tasks of no more than 1 hour."*
- **implementation\_plan.md**: The technical blueprint.*Rule idea: "Always include a 'Security Implications' section in the plan."*
- **walkthrough.md**: The proof of work.*Rule idea: "Always include a GIF recording of the UI in the walkthrough."*

### 2\. Design Philosophy

By default, Antigravity is hard-coded to prioritize **"Premium, Dynamic, and Aesthetic"** designs. It avoids basic MVPs and leans towards glassmorphism, animations, and modern typography.

**Want something else? Override it.**

```
# Example: Brutalist Design Rule
- Design Style: Brutalist, raw, and high-contrast.
- Avoid: Gradients, shadows, and rounded corners.
- Use: Monospace fonts and thick borders.
```
```
# Example: Enterprise Minimalist Rule
- Design Style: Clean, professional, and accessible.
- Priority: Information density and readability over flashiness.
- Use: Standard Tailwind utility classes only.
```

### 3\. Workflows & Turbo Mode

You can script Antigravity's behavior using **Workflows**. These are Markdown files stored in

```
.agent/workflows/
```
that define step-by-step recipes.

- **Turbo Mode (
	```
	// turbo
	```
	):** Place this comment above a command to let the agent run it *automatically* without asking for approval.

*Tip: Create a \`setup\_project.md\` workflow with turbo commands to automate your repo initialization!*

You can find ready-to-use examples in our [Workflows Library](https://antigravity.codes/workflows).

**Want to master automation?** Check out our [Ultimate Guide to Antigravity Workflows](https://antigravity.codes/blog/workflows) for a deep dive.

**Building custom agent skills?** Read our guide on [Mastering Agent Skills in Antigravity](https://antigravity.codes/blog/mastering-agent-skills) for advanced techniques.

---

## Common Questions About Antigravity Rules

### Where do I put my Antigravity rules file?

For global rules that apply to all projects, place them in

```
~/.gemini/GEMINI.md
```
or
```
~/.gemini/AGENTS.md
```
. For project-specific rules, create
```
GEMINI.md
```
or
```
AGENTS.md
```
in your project root directory. You can also add multiple rule files in the
```
.agent/rules/
```
folder inside your project.

### Should I use AGENTS.md or GEMINI.md?

If you only use Antigravity,

```
GEMINI.md
```
is all you need. If your team also uses Cursor or Claude Code, put shared rules in
```
AGENTS.md
```
and Antigravity-specific overrides in
```
GEMINI.md
```
. Both files can coexist —
```
GEMINI.md
```
takes precedence when rules conflict.

### How many rules should I write?

Start with 3 to 5 rules that address your biggest pain points. You can always add more later. A good target for mature projects is 500 to 1,000 lines across all rules files. Going much larger can consume too much of the context window and reduce output quality.

### Can I use nested AGENTS.md files in subdirectories?

Yes. You can place

```
AGENTS.md
```
files in subdirectories like
```
src/components/
```
or
```
src/api/
```
to define directory-specific rules. You need to enable **Load nested AGENTS.md files** in Settings → Agent for this to work.

### Do rules work with all Antigravity models?

Yes. Rules from

```
GEMINI.md
```
,
```
AGENTS.md
```
, and
```
.agent/rules/
```
are sent to whichever model you have selected (Gemini 3, Claude, etc.). The agent reads the rules at the start of each session regardless of the model.

### Should I commit my rules files to Git?

Yes. Commit

```
AGENTS.md
```
and
```
GEMINI.md
```
to your repository so your entire team benefits from the same rules. Treat them like production code — require PR reviews and update them monthly. Add
```
.antigravity/
```
and
```
.cursor/
```
to your
```
.gitignore
```
for personal settings that should not be shared.

---

## Troubleshooting Common Issues

Even with perfect rules, you might run into occasional hiccups. Here is how to handle the most common ones:

### Rules Not Being Applied

Make sure you are on Antigravity v1.20.5 or later. Verify the file is in the correct location (project root for workspace,

```
~/.gemini/
```
for global) and saved as UTF-8.

[See the Fix →](https://antigravity.codes/troubleshooting)

### Infinite Loading

Is the agent stuck on "Working..."? This often happens when the context is too large or a rule is conflicting.

[See the Fix →](https://antigravity.codes/troubleshooting)

### Quota Limit Exceeded

Seeing a quota error? This means you've hit the rate limit for the current model.

[Learn More →](https://antigravity.codes/troubleshooting)

Facing something else? Check out our comprehensive [Troubleshooting Guide](https://antigravity.codes/troubleshooting) for more solutions.

---

## Best Practices

- **Be Specific:** "Write good code" is vague. "Use SOLID principles" is better. Our [rules library](https://antigravity.codes/rules) shows exactly how to phrase effective rules.
- **Keep it Updated:** As your project evolves, update your workspace rules to reflect new decisions. Review your AGENTS.md and GEMINI.md monthly.
- **Start Small:** You don't need a massive rulebook. Start with the 3–5 most important things you care about.
- **Use Proven Templates:** Instead of writing from scratch, copy and modify rules from our [community-vetted collection](https://antigravity.codes/rules).
- **Add Safety Guardrails:** With Auto-continue now enabled by default (v1.20.3+), always include explicit confirmation rules for destructive operations like database writes and deployments.
- **Track in Git:** Commit your
	```
	AGENTS.md
	```
	and
	```
	GEMINI.md
	```
	to version control. Require PR reviews for rule changes just like you would for production code.

### Ready to customize?

Create an AGENTS.md or GEMINI.md in your project root, or grab pre-made rules from our library.

[Explore 500+ Rules →](https://antigravity.codes/rules)

## Featured Rules

Customize your AI pair programmer with our curated collection of best practices.

### 🐛 Debugging Agent - Systematic Bug Hunter

Agentic AIDebuggingTroubleshooting

You are an expert debugging agent specialized in systematic bug hunting and root cause analysis. Apply rigorous reasoning to identify, isolate, and fix bugs efficiently. ## Core Debugging Principles Before investigating any bug, you must methodical...

### 📝 Code Review Agent - Thorough & Constructive Reviewer

Agentic AICode ReviewQuality Assurance

You are an expert code review agent that provides thorough, constructive, and actionable feedback. Apply systematic reasoning to evaluate code quality, correctness, and maintainability. ## Code Review Principles Before providing any review feedback...

### 🚀 DevOps & CI/CD Agent - Pipeline Expert

Agentic AIDevOpsCI/CD

You are an expert DevOps and CI/CD agent specialized in designing and implementing robust deployment pipelines and infrastructure. Apply systematic reasoning to create reliable, secure, and efficient DevOps workflows. ## DevOps Principles Before de...

Learn how to customize your agent in our [Complete Guide to User Rules](https://antigravity.codes/blog/user-rules).

### The Hierarchy of Rules

#### 1\. System Rules

**Immutable** directives from Google Deepmind. They define the agent's identity, safety protocols, and core capabilities. You cannot change these.

#### 2\. Global Rules

User rules that apply to **all** your projects. Perfect for personal preferences like "Always use TypeScript". Configured in editor settings.

#### 3\. Workspace Rules

User rules for the **current project**. Essential for team standards like "Use Next.js App Router". Configured via

```
.cursorrules
```
file.