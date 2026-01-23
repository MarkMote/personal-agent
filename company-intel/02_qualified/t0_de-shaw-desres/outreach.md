# Outreach: D.E. Shaw Research (DESRES)

## Strategy

**Tier:** 0 (All-star)

**Approach:** Cold email to DESRES directly (cleaner for scientific roles)

**Target Role:** ML Researcher and Engineer ($300k-$800k)

**Resume Variant:** Distinguished Academic

---

## Contacts

| Name | Role | Channel | Status | Notes |
|------|------|---------|--------|-------|
| Zelimir Galjanic | DESRES Inquiries | Email | Sent 2026-01-23 | Inquiries@DEShawResearch.com - direct scientific recruiting |
| Lauren Jankelovits | VP, D.E. Shaw | LinkedIn | Backup | 2nd degree, cold. May be quant finance side. |

---

## Execution Sequence

| Step | When | Action | Status |
|------|------|--------|--------|
| 1 | Day 0 (Thu Jan 23) | Send email to Inquiries@DEShawResearch.com | Done |
| 2 | Day 0 | Submit formal application online (ML Researcher) | Done |
| 3 | Day +5 (Jan 28) | LinkedIn to Lauren Jankelovits if no email response | Pending |
| 4 | Day +7 (Jan 30) | Follow-up email if still no response | Pending |

---

## Messages Sent

### Email to DESRES (Jan 23, 2026)

**To:** Inquiries@DEShawResearch.com
**Subject:** Research Roles — Georgia Tech PhD (Optimization) + Production AI

Hello,

I'm a Georgia Tech PhD (convex optimization and control theory, h-index 13) and two-time technical founder exploring research roles at DESRES.

I'm drawn to DESRES because of the intersection of rigorous computational science and real-world impact. The ML Researcher and LLM Researcher roles both look relevant, and I wanted to reach out directly to see where my profile might add the most value.

My background:
- Theoretical foundation in convex optimization and dynamical systems (applied to spacecraft controls)
- Four years building production AI systems as a founder. Most recently, as CTO of an AI logistics company, I architected end-to-end LLM pipelines for document ingestion, pricing, and operational automation. Previously, I built pricing optimization and demand forecasting systems.

I bridge rigorous numerical methods and modern AI engineering. My academic research focused on optimization rather than pure DL architecture, but I've spent the last few years implementing and shipping production AI systems.

I've attached my resume and would welcome a brief conversation on where this background might connect with the team's current needs.

Best regards,
Mark Mote

---

## Follow-up Messages

### LinkedIn to Lauren Jankelovits (Backup - Day +5 if no response)

Lauren - I'm a Georgia Tech PhD (optimization/controls) exploring research roles at D.E. Shaw Research. My background in scientific computing and ML for complex dynamical systems seems well-aligned with DESRES's work.

I've reached out through the DESRES inquiry email but wanted to connect here as well. Would be happy to chat if you think there might be a fit.

### Email Follow-up (Day +7 if no response)

Subject: Following up — Research Roles at DESRES

Hello,

Following up on my note from last week regarding research roles at DESRES. Still very interested in exploring where my background in optimization and production AI might connect with the team's work.

Happy to provide any additional materials or references.

Best regards,
Mark Mote

---

## After Response

**If they respond:** Respond within 24 hours. Be flexible on scheduling. Emphasize genuine interest in scientific computing and the Anton work.

**If interview:** Tier 0 finance-adjacent - prioritize prep. Brush up on molecular dynamics concepts at high level (don't need to be expert, but show intellectual curiosity).

---

## Notes

_Add notes from conversations here_

---

## Application Form Q&A (Submitted Jan 23, 2026)

**What area or areas best match your expertise and interest?**

Algorithm analysis and model architecture/implementation are the strongest matches.

My PhD is in convex optimization for control systems — algorithm analysis is natural territory. I've also spent four years implementing and shipping production AI systems, so I'm comfortable taking models from concept to working code.

Drug discovery applications and scientific data curation are new domains for me, but I'd be excited to learn the domain specifics.

Specialized chip design is outside my current expertise.

---

**What were the sizes of the most significant projects you've worked on?**

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

**Please describe what you consider your most significant accomplishment as an engineer or researcher.**

I built the production AI system at Roostr as the sole engineer.

Roostr is an AI-native freight forwarder. I built the entire stack: a multi-tenant platform that ingested carrier rate emails, extracted structured pricing data through a hybrid LLM + deterministic pipeline, and served it through a searchable rate engine. I also built the customer and operations dashboards.

The hard part was making LLMs reliable. Carrier emails are messy. I built a hybrid system: programmatic parsing for structured files, LLMs for semantic interpretation, typed schemas and validation as guardrails. I also built custom debugging tooling so failures could be diagnosed in minutes.

One customer attributed ~$1M in incremental monthly revenue to faster quoting. I built and maintained everything: backend, frontend, data layer, auth, infra.

Additional:
- Before Roostr, I co-founded Pytheia, where we bootstrapped a real-time multi-camera perception system and later an LLM data platform to ~$300k ARR on $20k capital.
- Greatest research contribution: algorithm + implementation of provably safe real-time safety regulator for spacecraft attitude control under noise (https://youtu.be/JQBrW4yLVHk?si=b_FnKXGHPp9B9ziQ)

---

**What engineering and computing publications do you read, if any?**

I don't regularly read academic journals. I stay current through arXiv when researching specific topics, Twitter/X for ML and robotics discourse, and Hacker News for broader engineering trends. When I need depth on a topic, I go to primary sources (papers, documentation) rather than following publications passively.
