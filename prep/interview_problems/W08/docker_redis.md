# Docker + Redis — Multi-Service Backend

Build a FastAPI app with Redis as a backing store, containerized with Docker Compose.

## The Problem

Build a URL shortener with two services:

1. **API (FastAPI)**
   - `POST /shorten` — accepts `{"url": "https://..."}`, returns `{"short_id": "abc123", "short_url": "http://localhost:8000/abc123"}`
   - `GET /{short_id}` — redirects to original URL (302)
   - `GET /stats/{short_id}` — returns `{"url": "...", "hits": 42}`
   - Store mappings and hit counts in Redis

2. **Redis** — backing store, no persistence needed for this exercise

## Files to Write

- `app.py` — FastAPI app, uses `redis.asyncio` client
- `Dockerfile` — multi-stage or simple, Python 3.11+, install deps, run with uvicorn
- `docker-compose.yml` — two services (app + redis), network, health checks
- `requirements.txt` — fastapi, uvicorn, redis

## Things to Know

- `docker build -t myapp .`
- `docker compose up --build`
- `docker compose down`
- Dockerfile: `FROM`, `WORKDIR`, `COPY`, `RUN`, `EXPOSE`, `CMD`
- docker-compose: `services`, `ports`, `depends_on`, `environment`, `healthcheck`
- Redis via `redis.asyncio`: `await r.set(key, val)`, `await r.get(key)`, `await r.incr(key)`
- Environment variables for config: `REDIS_URL=redis://redis:6379` (service name as hostname in compose network)
