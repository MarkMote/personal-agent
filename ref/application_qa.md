# Application Q&A — Reusable Answers

Answers developed for applications, reusable across companies. Adjust for context.

---

## Most Significant Projects

**Roostr (2024-present) — AI-Native Freight Forwarder**
- Contribution: 100% (sole production engineer)
- Stack: Python 3.10, FastAPI, MongoDB, Docker (backend); Next.js, TypeScript, Tailwind (frontend); OpenAI APIs
- Purpose: Multi-tenant freight operations platform. Core system was a long-running LLM pipeline that ingested carrier emails and attachments, extracted structured rate data via hybrid deterministic + LLM parsing, and persisted to a searchable pricing engine. Over 10k rate entries processed to date. Also built quoting automation and encoded forwarding SOPs as a finite-state policy graph for progressive automation.

**Pytheia (2021-2024) — Multi-Camera 3D Perception System**
- Contribution: ~30% of code; owned system architecture, product direction, and integration strategy. Two co-founders handled core ML/algorithmic components and systems implementation respectively.
- Stack: Python, PyTorch, OpenCV, NumPy/SciPy, Shapely (perception); Next.js, FastAPI, Apache Superset, LangChain (data platform)
- Purpose: Real-time spatial perception engine that fused arbitrary CCTV camera feeds into a unified 3D world model. Pipeline: YOLO detection → DeepSORT tracking → 2D→3D projection → Kalman filtering → multi-camera fusion via Hungarian algorithm. Deployed for smart city pilots, robotics demos, and retail analytics. Later pivoted to LLM-driven data acquisition and demand forecasting for enterprise manufacturing customers.

**Robotarium (2016-2021) — Multi-Robot Research Testbed**
- Contribution: one of six researchers on founding team
- Stack: Python, MATLAB
- Purpose: NSF/ONR-funded (~$2.5M) remotely accessible swarm robotics testbed. Built safety verification tooling that allowed external researchers to run experiments on physical robots without damaging hardware. System has supported 16,000+ experiments and remains active. Work directly informed my PhD thesis on safe autonomy.

---

## Most Significant Accomplishment

I built the production AI system at Roostr as the sole engineer.

Roostr is an AI-native freight forwarder. I built the entire stack: a multi-tenant platform that ingested carrier rate emails, extracted structured pricing data through a hybrid LLM + deterministic pipeline, and served it through a searchable rate engine. I also built the customer and operations dashboards.

The hard part was making LLMs reliable. Carrier emails are messy. I built a hybrid system: programmatic parsing for structured files, LLMs for semantic interpretation, typed schemas and validation as guardrails. I also built custom debugging tooling so failures could be diagnosed in minutes.

One customer attributed ~$1M in incremental monthly revenue to faster quoting. I built and maintained everything: backend, frontend, data layer, auth, infra.

**Additional accomplishments to mention:**
- Co-founded Pytheia, bootstrapped a real-time multi-camera perception system and later an LLM data platform to ~$300k ARR on $20k capital.
- Greatest research contribution: algorithm + implementation of provably safe real-time safety regulator for spacecraft attitude control under noise (https://youtu.be/JQBrW4yLVHk?si=b_FnKXGHPp9B9ziQ)

---

## Publications / How I Stay Current

I don't regularly read academic journals. I stay current through arXiv when researching specific topics, Twitter/X for ML and robotics discourse, and Hacker News for broader engineering trends. When I need depth on a topic, I go to primary sources (papers, documentation) rather than following publications passively.

---

## Areas of Expertise and Interest

**Strongest matches:**
- Algorithm analysis
- Model architecture and implementation

**Foundation:** PhD in convex optimization for control systems. Four years implementing and shipping production AI systems.

**New domains I'd learn:** Drug discovery, scientific data curation, etc. (adjust per company)

**Outside current expertise:** Specialized chip design

---

## Lifetime Code Estimates

- **Python:** ~30-40k lines lifetime
- **TypeScript/JavaScript:** ~10-15k lines
- **MATLAB:** ~5-10k lines (PhD era)
