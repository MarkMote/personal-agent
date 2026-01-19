# 📂 PYTHEIA — FINAL CONSOLIDATED REPORT

**Status:** Jan 2026
**Role:** Co-Founder & CEO (Systems & Product Architecture)
**Company Lifetime:** Aug 2021 – Mar 2024 (~2.5 years)
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
* **Primary customer:** Lippert (Tier-1 RV supplier). Single-customer concentration — >95% of revenue.
* **Duration:** Nov 2023 → Mar 2024 (~5 months).
* **Contract end:** Product was well-received by end users, but contract was canceled at executive level due to internal procurement dynamics, independent of product performance.
* **Other revenue:** ~$1–2k MRR from pricing data customers; small CV contracts (restaurant pilot, fall detection).
* **Capital raised:** $20k (Pioneer, 2% equity). Otherwise bootstrapped.
* **Final outcome:** Company wound down after founder alignment drift, fatigue, and loss of momentum toward original vision.

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
* Vision: A real-time semantic world model — "an internet for robots." A shared reality that would make the world safer.

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

* Founder geographic separation (Matt → NJ, Ben/Mark → SF).
* Founder fatigue after multiple pivots — hearts no longer in it.
* Enterprise contract canceled at executive level.
* Alignment drift from original "internet for robots" mission.

**The Human Story:**

Ben, after a difficult breakup, concluded it was impossible to pursue both startup success and having a family. He chose stability. My reaction: "Yeah, of course. That makes total sense. No hard feelings — we had a great journey and now we move on to something else." There is no shame in quitting something that isn't working for you.

Matt and Ben now work together at a Series A startup in NYC. We're all still close — Ben was one of two people I brought to my wedding in Georgia (the country) in 2025.

**Transition to Roostr:**

Met Jacky at the Pioneer office while processing the wind-down. He had also just lost his CTO to stability-seeking. I spent a month evaluating two paths: Jacky's freight automation idea, or a friend's AI engineering tool (later YC-backed, ~$3M raised). Chose founder-fit over idea-fit. Started Roostr in April 2024.

---

## 4) Core Technical Systems

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
* "Advice is state-dependent. If they don't know you personally and can't see what side of the tradeoff you're too extreme on, it can be bad advice."
* "Don't take advice from anyone you wouldn't trade places with."

### Execution

* Iteration speed beats theoretical perfection.
* "Hire-fast-fire-fast applies to products too. Most experiments should be default-dead until proven otherwise."
* Customer trust compounds slowly but powerfully.

### Personal

* Must balance passion with economic reality.
* Founder alignment matters more than traction alone.
* "Risk is a proxy goal — it's not inherently good. There were paths where we could have taken less risk and succeeded more."

### Leadership Artifact: "State of the Business" Meeting

When stress peaked and relationships suffered, I created a bi-weekly ritual: Friday coffee, open discussion about where we were, what we liked, what we didn't, and honestly how we felt.

> "It's not always convenient to bring these things up. If you're working with people who are more agreeable, the risk is that things build up and turn to resentment. Having dedicated time where things get said was extremely cathartic."

Made it fun — Chick-fil-A afterwards. I believe this is why we're still such good friends today.

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

---

# APPENDIX — Technical Deep Dive (Argus)

*For robotics/autonomy interviews requiring additional depth.*

## Pipeline Architecture

```
Image Frame → Detection → Tracking → Transform → Estimation → Fusion
     ↓           ↓           ↓          ↓            ↓          ↓
   Camera     YOLO      DeepSORT    2D→3D       Kalman     Multi-cam
   stream    detects    assigns    project     filter      merge
             objects   persistent  to world   smooths    measurements
                          IDs      coords    position
```

## Component Details

**Detection Layer (YOLO)**
* YOLOv5 as primary detector
* Fine-tuning for domain-specific objects
* Object classes: PEDESTRIAN, BICYCLE, CAR, MOTORCYCLE, PICKUP_TRUCK, SEMI_TRUCK, VAN, BOX_TRUCK, BUS

**Tracking Layer (DeepSORT)**
* Re-identification using ResNet50 or OSNet
* Maintains persistent track IDs through occlusions
* Tunable parameters: max_dist, max_iou_distance, max_age, n_init, nn_budget

**Transformer Layer (2D → 3D Projection)**
* `Box3Inverter`: Projects 2D bounding boxes to 3D world coordinates
* Uses camera calibration (intrinsics + extrinsics)
* Inverse projection to ground plane (z=0)
* Handles lens distortion via `distortion_inverse_mapping`
* Modes: "center", "fix_l_w", "fix_w_theta"

**State Estimation Layer (Kalman Filter)**
* Double-integrator model: state = [x, y, vx, vy]
* Per-class filter parameters (pedestrians vs vehicles have different dynamics)
* Region of Interest filtering via Shapely polygons
* Track lifecycle management (init, update, prune)

**Multi-Camera Fusion Layer**
* Associates measurements from multiple cameras using IoU matching
* Hungarian algorithm (scipy.optimize.linear_sum_assignment)
* Fuses matched measurements into single estimate (position averaging, angle averaging)
* Handles track splits and merges across cameras

## Stack

* Python 3.10
* PyTorch (detection, re-ID networks)
* OpenCV (image processing)
* NumPy / SciPy (linear algebra, optimization)
* Shapely (geometric operations, IoU, ROI polygons)
* YAML config files per deployment



## Other

We could have raised, why did we bootstrap? 

> We deliberately chose to bootstrap. It forced discipline. We had to make customers happy immediately or we died. If we had needed capital to unlock growth, we would have raised. We didn’t at that stage


- Bootstrapping forces discipline.
- Revenue is the only real validation.
- Fundraising is a tool, not an achievement.
- You raise when it unlocks growth you cannot otherwise achieve.
- Building something customers pay for without external capital is strictly harder and more informative.


### Bootstrapping vs Fundraising

> We deliberately chose to bootstrap. It forced discipline. We had to make customers happy immediately or we died. If we had needed capital to unlock growth, we would have raised. We didn’t at that stage.

- Bootstrapping forces real constraints. You cannot hide behind runway, headcount, or roadmap theater.
    
- Revenue is the only durable validation. Everything else is proxy signal.
    
- Fundraising is a tool, not an accomplishment. What matters is what you build with the capital, not the act of raising it.
    
- You should raise when capital unlocks growth you cannot achieve through execution alone. Otherwise it introduces distraction and false positives.
    
- Building something customers pay for without external capital is strictly harder and more informative than convincing investors to fund an idea.

**Where we over-indexed:**

- We treated being anti-VC as a principle instead of a situational choice.
    
- In hindsight, we should have focused less on the ideology of bootstrapping and more on what unlocked the highest expected value in each phase.
    
- Some of the ideas likely would have benefited from earlier capital to accelerate market entry, partnerships, or sales motion.
    

**Updated belief:**

- Bootstrapping is a powerful tool for early discipline and signal clarity.
    
- Fundraising is a powerful tool when capital unlocks nonlinear growth.
    
- The mistake is not raising or not raising. The mistake is treating either as identity rather than strategy.
    


---

### Strong Opinions, Held Lightly

- High-performing engineers and founders need strong opinions. Taste, judgment, and internal models are what separate builders from implementers.
    
- Opinions should come from direct exposure to real systems, not theory or pattern matching.
    
- Being opinionated does not mean being rigid. It means having a coherent model and updating it when reality disagrees.
    
- The best technical conversations are about tradeoffs, not rules.
    

---

### Design Philosophy: Control Over Abstraction

- Abstraction is a liability when you don’t understand the failure modes.
    
- Frameworks optimize for speed of initial development, not long-term operability or debuggability.
    
- Owning the full execution path gives you leverage when things break under real-world conditions.
    
- It’s often better to build a small, explicit system you fully understand than adopt a large opaque framework.
    

---

### Reliability: MTTR Beats Theoretical Correctness

- In production systems, mean time to repair matters more than theoretical perfection.
    
- It’s usually impossible to anticipate all edge cases up front. What matters is how quickly you can detect, diagnose, and fix failures.
    
- Systems should be designed to surface errors clearly and allow fast iteration, not hide them behind layers of abstraction.
    
- This mindset mirrors SpaceX’s approach: ship early, learn from real failures, and close the loop quickly.
    

---

### Automation Reality

- Most automation failures are orchestration failures, not model failures.
    
- The hard problems are state management, invariants, exception handling, and recovery paths.
    
- LLMs are stochastic components and must be wrapped in deterministic control logic if you want reliable behavior.
    
- Human-in-the-loop is not a temporary crutch; it is often a permanent safety boundary in complex systems.
    

---

### Full-Stack Ownership

- Owning the entire operational loop creates clarity and speed. Fragmented ownership creates slow feedback and hidden coupling.
    
- Many SaaS products optimize surface polish while ignoring the real operational bottlenecks.
    
- The highest leverage comes from controlling the system that actually produces outcomes, not just the interface.
    

---

### Product vs Technology

- “Cool technology” and “valuable product” are only weakly correlated.
    
- Real value comes from solving painful operational problems, not from novelty.
    
- If users love the output but ignore the UI, the UI is the wrong product.
    
- Killing good technology in favor of better leverage is part of disciplined product thinking.
    

---

### On Pivoting

- Pivoting is not failure; it’s a form of market learning.
    
- The mistake is not pivoting. The mistake is staying attached to an idea after the evidence has moved on.
    
- The goal is not to be consistent. The goal is to converge toward something real.
    

---

### On Advice

- Advice is state-dependent. If someone doesn’t understand your exact constraints and incentives, their advice may be actively harmful.
    
- Don’t take advice from people you wouldn’t trade places with.
    
- The best advice is either highly specific or embarrassingly simple. Everything else is noise.
    
- Experience compresses ambiguity faster than reasoning alone.
    

---

### On Teams and Leadership

- Strong teams are built on trust, psychological safety, and honest communication, not just talent.
    
- Tension is inevitable in startups. The failure mode is letting it accumulate silently.
    
- Explicit rituals for airing concerns prevent resentment and preserve long-term relationships.
    
- Long-term trust compounds faster than short-term performance wins.
    

---

### On Risk

- Risk is a proxy goal, not a real goal.
    
- Taking risk only matters if it meaningfully increases expected value or learning.
    
- There are paths where lower risk produces better outcomes and stronger long-term positioning.
    
- Scrappiness builds resilience, but resilience alone does not guarantee success.
    

---

### On Market Timing

- Some ideas are correct but early. Timing matters more than correctness.
    
- Technical feasibility does not imply market readiness.
    
- The hardest part is not building the system; it’s aligning with adoption velocity, budgets, and trust cycles.
    

---

### On Enterprise Reality

- Enterprise sales are slow because trust is slow.
    
- The fastest way to build trust is to deliver small concrete wins, not big promises.
    
- Product quality matters less than perceived reliability and organizational fit early on.
    
- Internal politics can kill technically successful deployments.
    

---

### On Building Systems That Survive Reality

- Real systems are messy, adversarial, and full of edge cases.
    
- If a system only works in clean demos, it’s not a system yet.
    
- Robustness comes from explicit state, clear invariants, and fast feedback loops.
    
- Software should be designed for the world as it is, not the world as we wish it were.