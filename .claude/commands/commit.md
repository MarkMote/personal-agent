# /commit - Quick git commit

Simple commit for backup/audit. No fancy conventions.

## Steps

1. Run `git status` (no -uall flag) and `git diff --stat` to see what changed
2. Stage all changes with `git add -A`
3. Write a concise commit message (1 line, lowercase, no period)
   - Summarize what changed, not why
   - Examples: "update tracker and de-shaw folders", "add inbound policy rules", "fix typo in profile"
4. Commit with the message
5. Confirm success

## Rules

- Keep messages short and lowercase
- Don't ask for confirmation - just commit
- Don't push (local only)
- If nothing to commit, just say so
