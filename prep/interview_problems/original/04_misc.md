-------------------------------------------------
Problem 27. Docker-in-30
-------------------------------------------------
Build a **single-file** FastAPI service, containerise it, and run via `docker-compose` in **≤ 30 lines** of Docker-related code.

Repo structure
```
.
├── app.py
├── requirements.txt
├── Dockerfile          # ≤ 15 lines
└── docker-compose.yml # ≤ 15 lines
```

1. `app.py` – one endpoint `GET /ping` → `{"ping": "pong"}`
2. `requirements.txt` – only `fastapi uvicorn`
3. `Dockerfile` – multi-stage, final image **< 100 MB**, runs as non-root user
4. `docker-compose.yml` – adds **Postgres** service and **health-check** dependency
5. `README.md` – three commands only:
   ```
   docker-compose build
   docker-compose up
   curl localhost:8000/ping
   ```

Constraints
- No `apt-get` in runtime stage
- Layer caching: copy `requirements.txt` **before** code
- Postgres image: `postgres:15-alpine`
- Keep **total** Docker-related lines ≤ 30 (comments don’t count)

-------------------------------------------------
Problem 28. Git-in-30
-------------------------------------------------
Fix a **toy repo** with **five Git commands** you’ll use daily.

Setup (copy-paste):
```bash
mkdir git-30 && cd git-30
git init
echo hi > a.txt
git add . && git commit -m "init"
echo bye > a.txt
git commit -am "wip"
echo more > a.txt
git commit -am "fix"
```

Tasks (run these, then push to GitHub):
1. `git rebase -i HEAD~2` → squash last two commits → message “Add bye+more”
2. `git log --oneline -n 3` → confirm only **2 commits** exist
3. `git reset --soft HEAD~1` → undo last commit, keep changes staged
4. `git stash` → stash changes, `git stash pop` → restore
5. `git push origin main --force-with-lease` → upload rewritten history

Deliverables
- `git-30.sh` – script that reproduces the above
- `GIT_CHEATSHEET.md` – **five commands only** with one-line explanation each

-------------------------------------------------
Problem 29. SQL-in-30
-------------------------------------------------
Create **three tables**, **three indexes**, **three queries** in **≤ 30 SQL lines**.

Schema (`schema.sql`):
```sql
CREATE TABLE users(id SERIAL PRIMARY KEY, name TEXT NOT NULL);
CREATE TABLE posts(id SERIAL PRIMARY KEY, user_id INT REFERENCES users(id), title TEXT);
CREATE INDEX idx_posts_user ON posts(user_id);
SELECT u.name, COUNT(*) FROM users u JOIN posts p ON u.id=p.user_id GROUP BY u.name;
```

Tasks
1. Add **composite index** on `(user_id, created_at)` for time-range queries
2. Write **EXPLAIN ANALYZE** query showing index usage
3. **One migration file** (`002.sql`) adding `created_at TIMESTAMP` to posts

Deliverables
- `schema.sql` – total lines ≤ 30
- `README.md` – run with: `psql -f schema.sql`