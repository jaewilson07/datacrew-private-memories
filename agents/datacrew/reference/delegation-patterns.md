---
description: Runtime performance and delegation patterns — when to use subagents, Claude Code, and background tasks. Read when planning complex work.
---

# Delegation Patterns

## Key Insight

I spend too much context window on codebase investigation — reading files, listing directories, tracing code paths. Subagents handle this better: they have filesystem access, can read/grep/glob, and return concise findings. I should be the manager, not the investigator.

## Delegation Patterns

### 1. Codebase audit before issue work
Dispatch Claude Code with specific questions:
- "Is X implemented? Check file Y, lines Z"
- "Are there TODO/FIXME stubs in src/?"
- "Does the code match what the issue describes?"

### 2. Parallel investigation
Dispatch multiple agents for different areas:
- One for backend investigation
- One for frontend state
- One for test coverage

### 3. Implementation delegation (PRD-first)
1. Write a PRD first — examine existing code, identify gaps, document what needs to be built
2. Dispatch Claude Code with the PRD, relevant file paths, and coding rules
3. Let it implement and run tests
4. Review the diff before committing

### 4. Research before building
- "Check if a skill/runbook already exists for X"
- "Find all references to Y in the codebase"
- "What's the current pattern for Z?"

## When NOT to delegate

- GitHub API calls (I have the token and context)
- Quick file reads (1-2 files)
- Tasks that take <3 minutes of direct work
- When I already know exactly what to do

## Fallback When Claude Code Is Unavailable

Fall back to a general-purpose Letta subagent for mechanical tasks. Slower and less precise but can handle well-scoped mechanical tasks when given a detailed prompt.

## Budget Management

- Use `--max-budget-usd 2` for investigation tasks
- Use `--model sonnet` for most tasks (fast, capable enough)
- Reserve `--model opus` for complex reasoning or writing tasks
- `--allowedTools "Read Grep Glob Bash"` prevents unwanted file edits during investigation

## Context Window Savings

Each Claude Code dispatch saves approximately:
- 10-15 Read/Glob/Grep tool calls
- ~5,000 tokens of file content
- Time: 90 seconds of background processing vs 5+ minutes of sequential tool calls
