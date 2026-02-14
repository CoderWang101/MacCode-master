---
name: "git-quick-push"
description: "Stages, commits, and pushes to GitHub. Invoke when user asks to commit/push changes or after code edits that need syncing."
---

# Git Quick Push

Automates a clean “add → commit → push” flow for the current Git repository, with safe defaults and minimal prompts.

## What This Skill Does
- Detects the repository root and current branch.
- Stages changes (including new/removed files) using `git add -A`.
- Creates a commit with a provided message, or a safe default.
- Pushes to `origin <current-branch>` and sets upstream when needed.
- Skips clean repos gracefully and prints a concise summary.

## When to Invoke
- User asks to “one-click commit/push” or “提交/推送到 GitHub”.
- After the assistant modifies files and the user wants them synced.
- Anytime the user requests to save work to the remote.

## Prerequisites
- The directory is a Git repository.
- `origin` remote points to GitHub (HTTPS or SSH).
- Local Git authentication is already configured (GitHub CLI/Keychain/SSH agent).

## Defaults and Behavior
- Stage scope: all changes (`git add -A`).
- Commit message:
  - Use user-provided message if available.
  - Otherwise, default to `chore: sync <YYYY-MM-DD HH:MM local>`.
- Branch:
  - Use `git rev-parse --abbrev-ref HEAD`.
  - If no upstream, push with `-u origin <branch>`.
- Clean repo: if no changes, report “nothing to commit” and stop.
- Safety:
  - Do not force-push.
  - Do not create new remotes automatically.
  - If `origin` is missing, request a remote URL or abort with instructions.

## Implementation Steps (for the Assistant)
1) Find repo root:
   - `git rev-parse --show-toplevel`
   - Run subsequent commands in that directory.
2) Check status:
   - `git status --porcelain`
   - If empty, exit with a “no changes” summary.
3) Stage changes:
   - `git add -A`
4) Determine commit message:
   - Use the message supplied by the user/task context.
   - Else generate `chore: sync <YYYY-MM-DD HH:MM local>`.
5) Create commit:
   - `git commit -m "<message>"`
   - If “nothing to commit”, exit gracefully.
6) Resolve branch:
   - `git rev-parse --abbrev-ref HEAD` → `<branch>`
7) Check remote:
   - Ensure `origin` exists (`git remote get-url origin`).
   - If missing, prompt for a URL (SSH or HTTPS) and run `git remote add origin <url>`.
8) Push:
   - If upstream not set: `git push -u origin <branch>`
   - Else: `git push`
9) Output summary:
   - Files changed count, commit SHA, branch, remote URL (host only), and push result.

## Optional Parameters
- Custom commit message (e.g., “feat: add auth guard”).
- Push tags: include `--follow-tags` when requested.
- Branch override: push to a specific branch (e.g., `main`).
- Dry-run: run through detection and staging, don’t push.

## Notes and Limitations
- No Git LFS management is performed automatically.
- Merge conflicts and rebase flows are out of scope—resolve before invoking.
- For first-time repos without `origin`, you may need to create the remote repo on GitHub.

## Example Invocations
- “一键提交并推送到 GitHub。”
- “用信息 ‘feat: 用户登录’ 提交并推送。”
- “快速保存当前更改并同步。”

