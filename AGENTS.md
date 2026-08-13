# Workspace Execution Policy

## Branch and worktree isolation

- Creating, switching, or inspecting a branch or worktree is a Git-only operation. It must not create or activate a virtual environment, install packages, start test discovery, or run pytest, coverage, or evaluation commands.
- Keep generated environments and test artifacts outside version control. Never add a branch-startup hook or task that performs those actions implicitly.

## Explicit validation only

- Tests are opt-in: run them only when the user requests validation or after an in-scope code change, using the smallest relevant selector first.
- Do not run a broad `pytest` command, create a virtual environment, or install dependencies merely because a workspace opens or changes branches. An explicit user instruction to do so takes precedence.
