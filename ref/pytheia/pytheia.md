# 📂 PYTHEIA — FINAL CONSOLIDATED REPORT

**Status:** Jan 2026
**Role:** Co-Founder / CEO → Systems & Product Architect
**Company Lifetime:** Aug 2021 – ~Mar 2024 (~2.5 years)
**Outcome:** Bootstrapped to ~$300k ARR peak on $20k external capital

---

## 0) How to Read This Document

This document serves two purposes:

1. **Ground Truth Repository**
   Factual record of what was built, sold, learned, and why the company ended.

2. **Narrative Library**
   Strategic projections of the same facts for interviews, recruiting, and positioning.

No claims here require embellishment to be impressive.

---

# PART 1 — GROUND TRUTH (Reference Layer)

---

## 1) Executive Snapshot

**What Pytheia Built**

Across five market probes, Pytheia built two deep technical systems:

### System A — Real-Time Multi-Camera 3D Perception ("Argus")

A production-grade spatial perception engine capable of:

* Fusing arbitrary CCTV camera feeds into a unified 3D world model.
* Tracking people and vehicles in real-world coordinates.
* Providing live spatial analytics and natural-language querying.
* Operating without specialized hardware.

This system was deployed in smart-city pilots, robotics demos, and a live restaurant design partnership.

---

### System B — Agentic Data Acquisition & Forecasting Platform

A production agent platform capable of:

* Autonomously scraping heterogeneous websites using LLM agents.
* Structuring messy public data into clean datasets.
* Running geographic pricing models and demand forecasts.
* Delivering dashboards and interactive analytics to enterprise users.

This system reached meaningful enterprise revenue with Tier-1 manufacturing customers.

---

**Commercial Outcome**

* **Peak enterprise revenue:** ~$25k MRR (~$300k ARR equivalent).
* **Primary customer:** Lippert (>95% of revenue).
* **Duration:** Nov 2023 → ~Mar 2024 (~5 months).
* **Other revenue:** ~$1–2k MRR from pricing data customers; negligible.
* **Capital raised:** $20k (Pioneer, 2% equity). Otherwise bootstrapped.
* **Final outcome:** Company wound down after founder alignment drift and loss of momentum toward original vision.

---

## 2) Founding Team

Three co-founders from the same Georgia Tech robotics lab.

### Mark Mote — Founder / Product & Systems Architect

* PhD Robotics, MS Aerospace Engineering (Georgia Tech).
* Thesis: Optimization for spacecraft controls.
* ~800+ citations at founding.
* Research / internships: Stanford, MIT Lincoln Lab (2×), NASA JPL, AFRL, KAUST, ISAE-ENSMA.
* Founding member of the Robotarium.
* Role:

  * Owned **system architecture, product direction, integration strategy, and external interface**.
  * Deep technical ownership of modeling, system tradeoffs, and product design.
  * Contributed directly to frontend and selected backend components.
  * Led customer discovery, pitching, and product framing.

### Matthew Abate — Math / ML

* PhD Robotics, MS Computer Engineering, MS Electrical Engineering.
* Focus: Applied mathematics, computational methods.
* Owned modeling and algorithmic components.

### Ben Mains — Systems / Software

* MS ECE.
* Background: Distributed systems, scheduling.
* Industry: Yamaha (autonomous marine perception), General Atomics, Inria, Raytheon.
* Owned large portions of systems implementation.

**Team Dynamic**

* Long-standing personal trust and compatibility.
* Equal equity split (20/20/20) intentionally chosen for cohesion.
* Still close personally post-company.

---

## 3) Company Timeline & Market Probes

---

### Phase A — Shared Perception for Autonomous Vehicles

**Aug 2021 – Summer 2022**

**Thesis**

* Traffic cameras + V2X can provide shared perception for autonomous vehicles.
* One camera can serve many vehicles more efficiently than onboard sensors.
* Vision: A real-time semantic world model for vehicles.

**Technical Work**

* Ingested traffic camera feeds (Georgia 511).
* API access to ~3,500 PTZ cameras.
* Pilot with Peachtree Corners smart city testbed.
* Cloud partnerships (OVHcloud).
* Latency testing via AWS Wavelength.

**Discovery**

* ~30 OEM and Tier-1 interviews (Ford, Waymo, Mercedes, Aptiv, Porsche).
* Clear interest but slow cycles.

**Why It Stalled**

* Latency limits of existing infrastructure.
* Government coordination friction.
* 3–5 year OEM sales cycles.
* Trust barriers for external perception.

---

---

### Phase B — Robotics Perception Software

**Summer 2022 – Early 2023**

**Pivot Rationale**

* Same technology, faster robotics sales cycles.

**Product**

* Offboard camera perception system for robots.
* Frame-rate and resolution agnostic.
* Spatial analytics beyond onboard sensor limits.

**Competitors**

* Optitrack/Vicon (marker-based).
* Mobileye (onboard sensors).
* Tangram Vision, SLAMCore (onboard perception).

**Why It Stalled**

* Market still early.
* Robotics teams often build internally.
* Sales velocity insufficient.

---

---

### Phase C — Brick-and-Mortar Spatial AI

**Early 2023 – Summer 2023**

**Pivot Rationale**

* Apply spatial perception to retail and restaurant operations.

**Product**

* Multi-camera 3D spatial tracking.
* Live floor visualization.
* SMS natural-language interface.
* Worked with existing CCTV.

**Customer Discovery**

* Design partnership with fast-casual restaurant group.
* LOI signed.
* Live pilot.
* No meaningful recurring revenue.

**Accelerator**

* Pioneer (Spring 2023): $20k investment for 2%.

**Why It Stalled**

* Deployment variability across locations.
* Hardware heterogeneity.
* Sales complexity.

---

---

### Phase D — Pricing Optimization for Franchises

**Jul 2023 – Oct 2023**

**Pivot Rationale**

* LLM agents unlocked web data extraction at scale.

**Product**

* Agentic web scrapers.
* Geographic pricing optimization models.
* Auto-generated monthly reports.

**Revenue**

* ~$1.5k total, ~$900 MRR.

**Why It Pivoted**

* Pricing itself not sticky.
* Larger opportunity identified in demand forecasting.

---

---

### Phase E — Demand Forecasting for Manufacturers

**Oct 2023 – Mar 2024**

**Product**

* Two-agent architecture:

  * Data sourcing agent (writes scrapers, maintains infra).
  * Customer agent (analytics + interpretation).
* Scrapes dealership inventory nationwide.
* Forecasts supply/demand trends.
* Interactive dashboard + chat interface.

**Stack**

* Next.js, TypeScript, Tailwind.
* FastAPI backend.
* Apache Superset.
* GPT-3.5 family, LangChain, ChromaDB.
* Custom AutoGen-like framework.

**Traction**

* Enterprise customer: Lippert (Tier-1 RV supplier).
* ~$25k MRR peak (>95% of revenue).
* Yamaha validated similar demand internally.

**Why It Ended**

* Founder geographic separation.
* Founder fatigue after multiple pivots.
* Enterprise contract ended at executive level.
* Alignment drift from original mission.

---

## 4) Core Technical Systems

---

### System A — Argus: Multi-Camera 3D Perception

**Pipeline**

```
Camera → YOLO Detection → DeepSORT Tracking → 2D→3D Projection
       → Kalman Filtering → Multi-Camera Fusion
```

**Capabilities**

* Real-time 3D object tracking.
* Multi-camera fusion via Hungarian matching.
* Spatial analytics (speed, flow, occupancy).
* Works with any CCTV camera.

**Calibration**

* Standard camera calibration (intrinsics/extrinsics).
* Manual / semi-manual per site.
* Persistent configs stored.

**Stack**

* Python, PyTorch, OpenCV, NumPy, SciPy, Shapely.

**Differentiation**

* Operates in spatial frame vs image frame.
* No specialized hardware.
* Generalizable across environments.

---

---

### System B — Agentic Data Platform

**Capabilities**

* LLM-driven web scraping across arbitrary sites.
* Dataset normalization.
* Forecast modeling.
* Enterprise dashboards.

**Agent Architecture**

* Autonomous scraper agent.
* Domain-specific analytics agent.

**Stack**

* Next.js + FastAPI.
* Superset.
* GPT-3.5, LangChain.
* Custom agent framework.

---

## 5) What Was Objectively Impressive

* Built a **real-time multi-camera spatial perception system** from scratch.
* Bootstrapped to **~$300k ARR on $20k capital**.
* Shipped production agent systems before most tooling matured.
* Successfully sold enterprise software without sales staff or capital.
* Maintained full-stack ownership across perception, ML, infra, frontend.

---

## 6) Lessons Learned

### Strategic

* Market timing matters more than technical correctness.
* Robotics adoption cycles are long and trust-bound.
* Bootstrapping enforces discipline but limits upside speed.
* Advice must be filtered heavily.

### Execution

* Iteration speed beats theoretical perfection.
* Small experiments should be default-dead unless validated.
* Customer trust compounds slowly but powerfully.

### Personal

* Must balance passion with economic reality.
* Founder alignment matters more than traction alone.
* Long-term domain alignment is critical.

---

# PART 2 — NARRATIVE PROJECTIONS (Interview Layer)

---

## Narrative A — Robotics / Autonomy

> “I built a real-time multi-camera 3D perception engine that fused arbitrary CCTV feeds into a unified spatial world model. It handled detection, tracking, projection, filtering, and multi-camera association in production environments. The hardest problems weren’t ML accuracy, but calibration, latency, data association, and operational reliability.”

Keywords: perception, sensor fusion, Kalman filters, systems engineering, robotics realism.

---

## Narrative B — Staff / Principal Engineer

> “I’ve architected multiple production systems end-to-end under extreme resource constraints: real-time perception pipelines and autonomous agent platforms. I optimize for iteration velocity, operational correctness, and economic reality rather than demos.”

Keywords: systems ownership, iteration speed, reliability, architecture, tradeoffs.

---

## Narrative C — Founder / Product Engineer

> “We bootstrapped to ~$300k ARR on $20k capital by running disciplined market probes against a consistent technical core. Every pivot preserved real technical leverage and tested willingness-to-pay.”

Keywords: capital efficiency, product discipline, pivots, execution.

---

# PART 3 — RESUME BULLET PRIMITIVES

* Built a **real-time multi-camera 3D perception system** fusing heterogeneous CCTV feeds into unified spatial world models.
* Implemented end-to-end perception pipeline: detection (YOLO), tracking (DeepSORT), projection, Kalman filtering, and multi-camera fusion.
* Designed calibration workflows using standard intrinsics/extrinsics for field deployment.
* Architected an **agentic data acquisition platform** using LLM agents to autonomously scrape and structure web data at scale.
* Built production dashboards and forecasting pipelines for enterprise manufacturing customers.
* Bootstrapped company to **~$300k ARR peak on $20k total capital**.
* Led architecture, product design, integration strategy, and customer discovery as founding engineer.
* Shipped complex systems under extreme resource constraints with full-stack ownership.

