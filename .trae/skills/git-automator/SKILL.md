---
name: git-automator
description: Automates the git commit and push process. Use this skill when the user wants to commit code to the repository, especially when they ask for "one-click commit", "auto commit" or "push to github". It handles checking status, generating commit messages based on changes, and pushing to remote.
---

# Git Automator

This skill helps you automate the git commit workflow.

## Workflow

When the user triggers this skill, you should:

1.  **Check Status**: Run `git status` to see if there are any changes.
    *   If no changes, inform the user and exit.
2.  **Get Diff**: Run `git diff` (and `git diff --cached` if needed) to understand the changes.
    *   If there are untracked files, use `git status` output to identify them.
3.  **Generate Commit Message**: Based on the changes, generate a concise and descriptive commit message.
    *   Format: `<type>: <subject>` (e.g., `feat: add new login feature`, `fix: resolve null pointer exception`).
    *   Keep it under 50 characters if possible.
    *   **Do NOT ask the user for the message**. The user expects YOU to generate it.
4.  **Execute Git Commands**:
    *   `git add .`
    *   `git commit -m "YOUR_GENERATED_MESSAGE"`
    *   `git push`
5.  **Report**: Inform the user of the success and the commit message used.

## Rules

*   **Autonomy**: You should execute these commands automatically without asking for confirmation for every step, unless there is a potential conflict or error.
*   **Safety**: If `git push` fails (e.g., due to conflict), stop and inform the user. Do not force push unless explicitly requested.
*   **Log Generation**: The user relies on YOU to write the commit message. Do not ask the user for it unless they explicitly want to provide one.
