# Mark L. Mote

**New York, NY** | [markmote@gmail.com](mailto:markmote@gmail.com) | [linkedin.com/in/mote](https://www.linkedin.com/in/mote) | [markmote.com](https://markmote.com)

## One-Line

Founder-engineer with a Robotics PhD who builds production systems at the boundary of autonomy, perception, and agentic software. Strong bias for shipping, rapid iteration, and operating real systems.

---

# Highlights

- **Roostr (2024–2026):** Built and operated an AI-native freight ops stack as **sole production engineer**, spanning **rate ingestion, quoting, and shipment workflow automation**. Customer-attributed **~$1M incremental monthly revenue** impact via faster quoting; processed **10,000+ rates** across **28 carrier partners**.

- **Pytheia (2021–2024):** Co-founded and led a deep-tech startup through multiple pivots, reaching **~$300k ARR peak** on **$20k Pioneer investment** (bootstrapped otherwise). Built two production systems:
  - **Argus:** Real-time multi-camera **3D perception** (detection, tracking, calibration, fusion)
  - **Agentic Data Platform:** LLM-agent web data sourcing + forecasting dashboards for enterprise supply-chain use cases

- **Research:** 1,449 citations, h-index 13, i10-index 17. Work across safe autonomy, runtime assurance, multi-robot systems, and trajectory optimization. Internships at **NASA JPL**, **AFRL**, **MIT Lincoln Lab**, and collaboration at **Stanford** and **KAUST**.

---

# About

I build systems that live in the real world: they ingest messy inputs, run continuously, fail in surprising ways, recover fast, and improve over time. My thesis was on runtime assurance—the art of moving fast without breaking things. That tension between speed and safety has defined my career.

**I'm comfortable spanning:**
- Product design and customer discovery
- Full-stack engineering (frontend, backend, infra)
- Autonomy-style thinking (state, uncertainty, safety, monitoring, MTTR)
- Computer vision and state estimation (detection, tracking, calibration, fusion)
- Optimization and control (convex/MIP, CBFs, trajectory optimization)

**What I'm looking for:** A place to go deep on hard technical problems with a strong team. Work that pulls rather than pushes.

---

# Experience

## Roostr — Co-Founder & CTO (Sole Production Engineer)
**New York, NY | April 2024 – Present**

AI-native freight-forwarding operations stack designed to collapse quote turnaround time by turning unstructured carrier emails and documents into a structured, searchable rate engine and quoting workflow.

### The Problem

Freight forwarders quote shipments by searching through inboxes and spreadsheets manually. Quote turnaround takes hours. Carriers send rate updates via email in dozens of different formats—PDFs, Excel files, HTML tables, plain text. No structure, no standards.

### System Overview (Production)

```
Rate Ingestion:   Email → Nylas → Hybrid Extraction (LLM + Code) → Normalization (SSOT) → MongoDB → Searchable UI
Quoting:          RFQ parsing → Rate matching → Quote generation → Outbound email
Ops Automation:   Policy-graph shipment state machine (pre-booking automated; other nodes tracked manually initially)
```

### Impact

- One fully integrated customer attributed **~$1M incremental revenue in a month** to improved quote speed
  - Freight is pass-through; estimated profit impact **~5–10%** of top-line
  - This is customer-reported, not a rigorously instrumented causal model
- **10,000+ rates** processed across **28 carrier partners** (rates per email ranged from 1 to 1,000+)

### How I Engineered It (The Real Differentiator)

**Built for MTTR (Mean Time To Repair) and continuous improvement rather than theoretical perfection.**

Designed a **rapid reaction loop**: when extraction failed, I could reproduce, fix, and redeploy quickly, then add the failing case into a regression set.

**Testing Methodology ("Golden Set" + Zero-Tolerance Drift):**
- Maintained a "Golden Set" of ~20 representative and adversarial emails/docs
- In SaaS mode (3 customers): ran regressions on major updates, monitored customer accounts directly. It only broke 1–2 times, and I detected before customers did.
- As an operator (our own forwarder): could relax testing if needed and prioritize building better systems. Still kept the "zero tolerance long-term error" approach—any failure became a regression case.

**Failure Modes I Handled:**

| Problem | Cause | Fix |
|---------|-------|-----|
| Runaway loops | Agent replying to its own emails | Explicit blacklists/filters and guardrails |
| Data drift | Inconsistent port naming ("Shanghai" vs "CN SHG" vs "CNSHG") | SSOT normalization layer with 3,340 canonical port codes |
| Parsing edge cases | Chinese characters in XLS breaking pipelines | Hardened parsing, targeted modules |

**Unit Economics (AI + Infra):**
- Designed hybrid approach: **programmatic parsing for large XLS/CSV**, LLMs only for semantic tasks
- Tiered model usage: smaller models for intent classification/routing; larger models for complex extraction
- Cost per complex rate email: **< $0.01–$0.10**
- At typical volumes: **< $100/month per customer** in LLM spend

**Why No LangChain:**

Deliberate choice. Needed deterministic control over state transitions, visibility into context/prompting, and debuggable pipelines. Built a minimal internal abstraction:
- **Planner** → decides action
- **Tool** → executes
- **Intent** → database updates, emails

This kept LLM reasoning decoupled from deterministic execution.

### Architecture Details

**Rate Extraction Pipeline:**
1. Email arrives via Nylas webhook
2. Quick filter rejects obvious non-rate emails (cheap model)
3. Planner decides: extract / respond / skip / escalate
4. If extract: process attachments (PDF, CSV, XLS, HTML)
   - Large files parsed programmatically
   - LLM handles column mapping and semantic interpretation
5. Schema validation and field standardization
6. SSOT normalization (ports, incoterms, carriers)
7. Persist to MongoDB with tenant isolation
8. Surface in review UI for human approval

**Quote Agent:**
- Planner-driven agentic loop (max 7 iterations)
- 6 specialized tools: RFQ parser, RFQ updater, rate matcher, email generator, human handoff, no-action
- Terminates on terminal tool call or iteration limit

**Tech Stack:**
- Backend: Python 3.10, FastAPI, Docker, DigitalOcean
- Frontend: Next.js, TypeScript, Tailwind, Vercel
- Database: MongoDB Atlas (multi-tenant, `tenant_id` scoped)
- Email: Nylas API
- LLM: Claude (Anthropic) — 3.7 Sonnet (default), 3.5 Sonnet (extraction), 3.5 Haiku (validation)
- Auth: Wristband OAuth + RBAC

**Scale:**
- ~65,000 lines of code across backend and frontend
- 318 commits in ~6 weeks of initial development
- 10 tenants supported, 28 carrier partners, 293 whitelisted senders

---

## Pytheia Corporation — Co-Founder & CEO
**Atlanta, GA → SF (brief) | August 2021 – March 2024**

Deep-tech startup that explored multiple markets while preserving a core technical edge: spatial perception and later agentic data sourcing + forecasting.

**Funding:** $20k (Pioneer, 2% equity). Bootstrapped otherwise.
**Peak revenue:** ~**$300k ARR** equivalent during pricing/demand phase.
**Concentration:** >95% of revenue came from one enterprise customer (Lippert). This was a strength (enterprise value) and also a fragility.

### Phase Timeline

| Phase | Period | Focus | Key Learning |
|-------|--------|-------|--------------|
| A | Aug 2021 – Summer 2022 | Shared perception for AVs | OEM cycles 3-5 years; latency limits of traffic camera infrastructure |
| B | Summer 2022 – Early 2023 | Robotics perception software | Market still early; robotics teams build internally |
| C | Early 2023 – Summer 2023 | Brick-and-mortar spatial AI | Hardware heterogeneity; deployment variability |
| D | Jul 2023 – Oct 2023 | Pricing optimization for franchises | Pricing itself not sticky enough |
| E | Oct 2023 – Mar 2024 | Demand forecasting for manufacturers | Achieved PMF; founder alignment drift |

### Phase A — Shared Perception for Autonomous Vehicles
**Aug 2021 – Summer 2022**

**Thesis:** Traffic cameras + V2X can provide shared perception for autonomous vehicles. One camera can serve many vehicles more efficiently than onboard sensors. A shared reality that would make the world safer—essentially a real-time semantic search engine for the physical world.

**Technical Work:**
- Built PoC using Georgia 511 camera streams
- Obtained API access to ~3,500 PTZ cameras
- Pilot with Curiosity Lab at Peachtree Corners (smart city AV testbed, ~1.5 mile stretch with continuous camera coverage)
- Cloud partnerships (OVHcloud), latency testing via AWS Wavelength

**Discovery:**
- ~30 customer interviews with OEMs, Tier-1 suppliers, DOTs
- Talked to Ford, Waymo, Mercedes, Aptiv, Panasonic, Porsche
- Clear interest but slow cycles

**Why It Stalled:**
- Latency too high with existing traffic camera infrastructure
- Government coordination friction
- 3–5 year OEM sales cycles
- Trust barriers for external perception

### Phase B — Robotics Perception Software
**Summer 2022 – Early 2023**

**Pivot Rationale:** Same core technology, faster robotics sales cycles.

**Product:** Off-board camera perception system for robots. Frame-rate and resolution agnostic. Spatial analytics beyond onboard sensor limits.

**Competitors:**
- Optitrack/Vicon (marker-based, lab only)
- Mobileye (onboard automotive)
- Tangram Vision, SLAMCore (onboard perception)

**Why It Stalled:** Market still early; robotics teams often build internally; sales velocity insufficient.

### Phase C — Brick-and-Mortar Spatial AI
**Early 2023 – Summer 2023**

**Pivot Rationale:** Apply spatial perception to retail and restaurant operations.

**Product:**
- Multi-camera 3D spatial tracking
- Live floor visualization
- SMS natural-language interface
- Works with existing CCTV

**Traction:**
- Design partnership with fast-casual restaurant group
- LOI signed, live pilot
- $20k investment from Pioneer (2% equity)

**Why It Stalled:** Deployment variability across locations; hardware heterogeneity; sales complexity.

### Phase D — Pricing Optimization for Franchises
**July 2023 – October 2023**

**Pivot Rationale:** LLM agents unlocked web data extraction at scale.

**Product:**
- Agentic web scrapers: LLM agents collect franchise prices given a brand's URL
- Geographic pricing optimization models
- Auto-generated monthly reports

**Revenue:** ~$1.5k total, ~$900 MRR

**Why It Pivoted:** Pricing itself not sticky; larger opportunity identified in demand forecasting.

### Phase E — Demand Forecasting for Manufacturers
**October 2023 – March 2024**

**Product:** Forecast downstream demand and inventory for Tier-1 suppliers using scraped market data.

**Two-Agent Architecture:**
1. **Data sourcing agent:** Writes web scraper executables, maintains infrastructure around the data produced
2. **Customer-facing agent:** Code-interpreter style assistant with domain-specific primitives and dataset access

**Stack:** Next.js, TypeScript, Tailwind, FastAPI, Apache Superset, GPT-3.5 family, LangChain, ChromaDB, custom AutoGen-like framework

**Traction:**
- Enterprise customer: Lippert (Tier-1 RV parts supplier)
- Peak: **$25k MRR** (Nov 2023) primarily from Lippert
- Validated with Yamaha

**Why It Ended:**
- Founder geographic separation (Matt → NJ, Ben/Mark → SF)
- Fatigue after multiple pivots—hearts no longer in it
- Enterprise contract canceled at executive level despite users valuing the product
- Co-founder life priorities shifted (family/stability)

**The Human Story:** Ben concluded it was impossible to pursue both startup success and having a family. He chose stability. My reaction: "Yeah, of course. That makes total sense. No hard feelings—we had a great journey and now we move on to something else." There is no shame in quitting something that isn't working for you.

We're all still close—Ben was one of two people I brought to my wedding in Georgia (the country) in 2025.

**Transition to Roostr:** Met Jacky at the Pioneer office while processing the wind-down. He had also just lost his CTO to stability-seeking. I spent a month evaluating two paths and chose founder-fit over idea-fit. Started Roostr in April 2024.

---

## Systems Built at Pytheia

### Argus — Real-Time Multi-Camera 3D Perception

Production-grade spatial perception engine. The hardest problems weren't ML accuracy—they were calibration, latency, data association, and operational reliability.

**Pipeline:**
```
Camera → Detection (YOLO) → Tracking (DeepSORT) → 2D→3D Projection → State Estimation (Kalman) → Multi-Camera Fusion
```

**What It Did:**
- Fused arbitrary CCTV camera feeds into unified 3D world model
- Tracked people and vehicles in real-world coordinates (position, velocity)
- Spatial analytics: walking speeds, line speeds, occupancy—metrics impossible in 2D pixel space
- Works with any camera, no specialized hardware required

**Core Components:**

| Layer | Technology | Details |
|-------|------------|---------|
| Detection | YOLOv5 | Fine-tuning for domain-specific objects |
| Tracking | DeepSORT | Re-ID via ResNet50/OSNet, persistent track IDs through occlusions |
| Projection | Box3Inverter | Camera intrinsics/extrinsics, inverse projection to ground plane (z=0), distortion handling |
| State Estimation | Kalman Filter | Double-integrator model [x, y, vx, vy], per-class dynamics |
| Fusion | Hungarian Algorithm | IoU matching across cameras, split/merge handling |
| ROI Filtering | Shapely | Polygon-based region of interest |

**Object Classes:** PEDESTRIAN, BICYCLE, CAR, MOTORCYCLE, PICKUP_TRUCK, SEMI_TRUCK, VAN, BOX_TRUCK, BUS

**Calibration:** Standard intrinsics/extrinsics workflow; manual/semi-manual per site; persistent configs stored.

**Stack:** Python 3.10, PyTorch, OpenCV, NumPy/SciPy, Shapely, YAML configs

**Differentiators:**
- Operates in **spatial frame** (real-world coordinates) vs image frame (pixels)
- Enables metrics that 2D-only systems can't compute
- No specialized hardware—works with existing CCTV
- Generalizable across environments

**Evidence:**
- Demo video: [youtube.com/watch?v=Wdzhru0Y5f0](https://youtube.com/watch?v=Wdzhru0Y5f0)
- Channel: [youtube.com/@PytheiaAI](https://youtube.com/@PytheiaAI)

### Agentic Data Platform

**What It Did:**
- LLM-agent web scraping across arbitrary sites
- Dataset normalization
- Forecast modeling
- Enterprise dashboards with chat interface

**Stack:** Next.js + TypeScript + Tailwind, FastAPI, Apache Superset, GPT-3.5, LangChain, ChromaDB, custom agent framework

---

## Georgia Institute of Technology — Graduate Research Assistant
**Atlanta, GA | January 2016 – July 2021**

### Robotarium Project (NSF Award No. 1544332)

**Founding team member** of the Robotarium—the world's first remotely accessible multi-robot research testbed. Built safety and verification tooling enabling researchers worldwide to run experiments on physical robots without being on-site.

**My Contributions:**
- Designed and implemented runtime assurance algorithms for safe multi-agent coordination
- Built control barrier function frameworks ensuring collision avoidance under real-time constraints
- Developed scalable safety verification methods for nonlinear systems
- Created tooling that enabled the platform to serve 1,000+ researchers globally

**Impact:**
- Flagship paper: 501 citations
- IEEE Control Systems Magazine paper: 314 citations
- Work directly enabled the platform's transition from research prototype to globally-accessible facility

---

## NASA Jet Propulsion Laboratory (NASA-JPL) — Intern
**Pasadena, CA | May 2019 – August 2019**

**Maritime and Multi-Agent Autonomy Group (347N)**

Designed communication and control algorithms for distributed asteroid exploration using satellite swarms.

**Work:**
- Developed coordination protocols for multi-agent spacecraft systems
- Built simulation framework for swarm behavior validation
- Contributed to mission concept development

**Publication:** Journal of Guidance, Control, and Dynamics (AIAA JGCD)

**Outcome:** Return offer for full-time position

---

## Air Force Research Laboratory (AFRL) — Intern
**Dayton, OH | May 2020 – August 2020**

**Autonomy Capabilities Team 3 (ACT3)**

Developed provably safe spacecraft docking using control barrier functions and shielded reinforcement learning.

**Work:**
- Combined learned policies with formal safety guarantees
- Built framework where RL explores freely while safety constraints are mathematically enforced
- Demonstrated on spacecraft proximity operations scenarios

**Publication:** 2021 IEEE Aerospace Conference

**Outcome:** Return offer for full-time position

---

## MIT Lincoln Laboratory — Research Intern
**Boston, MA | Summers 2017, 2018**

**BMDS Integration Group**

Applied formal verification techniques to neural network image classifiers.

**Work:**
- Developed methods to verify properties of deep neural networks
- Focus on robustness and correctness guarantees for safety-critical systems
- Research became restricted for security reasons—can discuss topic but not details

---

## Stanford University — Visiting Researcher
**Stanford, CA | June 2018 – July 2018**

**Autonomous Systems Laboratory (ASL)**

Built and tested collision-inclusive trajectory optimization on 3-DOF spacecraft testbed.

**Work:**
- Developed trajectory optimization algorithms that explicitly model contact/collision
- Tested on Stanford's spacecraft simulator platform
- Demonstrated "bouncing" trajectories that use collision for efficiency

**Publication:** Journal of Guidance, Control, and Dynamics (AIAA JGCD)

**Demo:** [youtube.com/watch?v=4kOOn6TPuDI](https://youtube.com/watch?v=4kOOn6TPuDI)

---

## King Abdullah University of Science and Technology (KAUST) — Visiting Student
**Thuwal, Saudi Arabia | January 2020 – May 2020**

**Computer, Electrical and Mathematical Sciences & Engineering Division**

Collaborative research on safe autonomy and control theory.

---

## ISAE-ENSMA — Research Intern
**Poitiers, France | May 2015 – July 2015**

**LIAS Laboratory**

Developed and compared quadcopter flight controllers. Contributed to auto-coding design automation research.

---

# Education

## Georgia Institute of Technology

| Degree | Honors | Date |
|--------|--------|------|
| Ph.D. in Robotics | Highest Honors | August 2021 |
| M.S. in Aerospace Engineering | Highest Honors | May 2018 |
| B.S. in Aerospace Engineering | Highest Honors | December 2015 |

**PhD Thesis:** Runtime assurance for safety-critical systems / Optimization for spacecraft controls

**Advisor:** Magnus Egerstedt

---

# Publications & Citations

**Google Scholar Stats:**
- Citations: 1,449 total (1,132 since 2021)
- h-index: 13
- i10-index: 17

## Selected Papers

### Foundational Work

1. **"The Robotarium: A remotely accessible swarm robotics research testbed"**
   IEEE ICRA 2017 | **501 citations**
   > Established the architecture and safety guarantees for the world's first remotely-accessible multi-robot platform.

2. **"The Robotarium: Globally impactful opportunities, challenges, and lessons learned..."**
   IEEE Control Systems Magazine 2020 | **314 citations**
   > Retrospective on scaling the platform to serve researchers worldwide.

3. **"Runtime assurance for safety-critical systems: An introduction to safety filtering"**
   IEEE Control Systems Magazine 2023 | **101 citations**
   > Tutorial on safety filtering methods for autonomous systems.

### Core Technical Contributions

4. **"An online approach to active set invariance"**
   IEEE CDC 2018 | **104 citations**

5. **"A scalable safety critical control framework for nonlinear systems"**
   Automatica 2020 | **91 citations**

### Spacecraft & Multi-Agent Systems

6. **"Natural motion for satellite proximity operations"** *(NASA JPL collaboration)*
   AIAA Journal of Guidance, Control, and Dynamics

7. **"Safe spacecraft docking using control barrier functions"** *(AFRL collaboration)*
   IEEE Aerospace Conference 2021

8. **"Collision-inclusive trajectory optimization"** *(Stanford collaboration)*
   AIAA Journal of Guidance, Control, and Dynamics

---

# Research Areas

### Safe Autonomy & Runtime Assurance

How do you let learning systems explore while guaranteeing they don't violate safety constraints? My thesis work developed control barrier function frameworks that provide formal safety guarantees for nonlinear systems. This isn't just theory—I've deployed these methods on multi-robot platforms and spacecraft simulations.

### Multi-Agent Coordination

How do you get swarms of robots to work together? The Robotarium project tackled this at scale, enabling researchers worldwide to run multi-robot experiments remotely. The core challenge: ensuring safety when you can't control what algorithms users upload.

### Perception for Robotics

Traditional CV gives you pixels. Robots need positions, velocities, and predictions in the real world. At Pytheia, I built systems that fused multiple camera feeds into unified 3D spatial representations—working in "spatial frame" rather than "image frame."

### Spacecraft GNC

My PhD focused on optimization for spacecraft controls. The work at JPL (asteroid swarm coordination), AFRL (safe docking), and Stanford (collision-inclusive trajectory optimization) all applied control theory to space systems.

---

# Skills

## Core Competencies

Production autonomous systems | Full-stack product engineering | LLM/agent systems | Computer vision/perception | Sensor fusion & state estimation | Optimization & control | Simulation

## Stack

| Category | Technologies |
|----------|-------------|
| Backend | Python, FastAPI, Docker, MongoDB |
| Frontend | TypeScript, React, Next.js, Tailwind |
| ML/AI | PyTorch, OpenCV, Claude (Anthropic), GPT family |
| Research | MATLAB, C++, Julia, ROS |
| Data | NumPy, SciPy, Pandas, Snowflake |

## Methods

Mixed-integer convex optimization | Trajectory optimization | Control barrier functions | Kalman filtering (EKF, UKF) | Multi-object tracking | Camera calibration | Multi-sensor fusion

## Infrastructure

Production cloud deployments (Vercel, DigitalOcean, AWS) | Observability & incident response | Fault-tolerant pipelines | CI/CD (GitHub Actions) | Monitoring/alerting

---

# Engineering Philosophy

## Build for MTTR ("SpaceX Strategy")

I optimize for iteration velocity and recovery time rather than trying to pre-solve every edge case. In practice:
1. Ship a working system fast
2. Instrument it so failures are visible
3. Fix failures immediately
4. Add every failure to regression coverage
5. Over time you spend effort only on real problems

This is not universally correct, but it was correct for early-stage startups operating under uncertainty.

## Control Over Abstraction

Abstraction is a liability when you don't understand the failure modes. Frameworks optimize for speed of initial development, not long-term operability. Owning the full execution path gives you leverage when things break under real-world conditions. It's often better to build a small, explicit system you fully understand than adopt a large opaque framework.

## Strong Opinions, Held Lightly

High-performing engineers need strong opinions—taste, judgment, internal models. But opinions should come from direct exposure to real systems, not theory. Being opinionated doesn't mean being rigid. It means having a coherent model and updating when reality disagrees.

## Automation Reality

Most automation failures are orchestration failures, not model failures. The hard problems are state management, invariants, exception handling, and recovery paths. LLMs are stochastic components that must be wrapped in deterministic control logic. Human-in-the-loop is often a permanent safety boundary, not a temporary crutch.

---

# Leadership

## "State of the Business" Meeting

At Pytheia, I realized things were getting tense—the stress was too high, our relationships were suffering. We were friends before this and would work better as friends. I created a "state of the business" meeting every 2–3 weeks.

On Friday we'd drink coffee, sit inside, have a very open discussion about where we were, what we were happy with, what we didn't like. And very honestly how we felt.

> "It's not always convenient to bring these things up. If you're working with people who are more agreeable, the risk is that things build up and turn to resentment. Having dedicated time where things get said was extremely cathartic."

Made it fun—got Chick-fil-A right afterwards. I believe this is the reason we are still such good friends today.

---

# FAQ / Interview-Ready

## Why did you bootstrap instead of raising?

We deliberately chose to bootstrap early. It forced discipline. We had to make customers happy immediately or we died. If capital would have unlocked growth we couldn't otherwise achieve, we would have raised. At that stage, it didn't.

**What I learned:** We probably over-indexed on being anti-VC at times. Fundraising is a tool, not a credential. The right move depends on the scenario.

## Why are you leaving Roostr?

Roostr is still operating, the product works, we're getting inbound, and I'm on great terms with my cofounder. We're at a point where the constraint is mostly sales and operations scaling. I'm personally more excited about building hard systems than running a logistics operation day-to-day, so this is a natural transition point.

*(If asked)* Roostr is low six-figure run-rate; if I stayed we'd likely need to raise sooner. Leaving keeps incentives clean and gives my cofounder more runway.

## What's your biggest weakness?

A natural tendency I have to stay cognizant of is over-optimizing for immediate execution and delivery. I enjoy shipping and solving concrete problems, so if I'm not careful I can underinvest in longer-term exploratory work or skill compounding.

I first became aware of this at JPL. I focused heavily on delivering simulation improvements that created fast impact and led to a return offer, but I deferred some higher-risk theoretical exploration that I later wished I had pursued. That experience made the pattern clear to me.

Since then I've learned to actively manage that tendency. I deliberately protect time for deeper exploration and learning, and I periodically step back to ask whether I'm optimizing for the right horizon, not just the fastest local win.

## What's the core thing you're best at?

Building production systems that run continuously, ingest unstructured real-world inputs, degrade gracefully, and get better over time. I'm unusually fast at diagnosing failures and turning them into product improvements.

---

# The Bigger Picture

## Driving Philosophy

There will be three great changes in my lifetime: life extension, a human Mars mission, and artificial intelligence. If we're lucky, four—we discover alien life. This has been the compass for a decade.

Aerospace was the path that resonated—leaving Earth, making humans fly, answering the big questions. I worked toward JPL from undergrad and got the offer. But I took a different path: entrepreneurship.

> "There were people with this knowledge of how to just do things, and I would never forgive myself if I didn't figure that out too. If I didn't try to do something great, at least once, what kind of life would that be."

## The JPL Decision

All hosts offered full-time roles at graduation. The Stanford professor (now NVIDIA AV director) was building a team. JPL offer in hand. The principal rocket landing engineer at SpaceX reached out personally for a tour. Chose the startup path instead.

## What I Bring Now

I bring something most pure aerospace people don't: the ability to commercialize deep tech. PhD rigor plus startup operator plus technical leadership is rare. I've taken AI systems from research to production, twice.

## What Energizes Me

- Spacecraft and robotics—the deepest pull, since undergrad
- Hard technical problems that matter (safe autonomy, vision, controls)
- Building businesses, not just products—the "meta-engineering"
- AI/ML as tooling for the above, not as an end in itself
- Leading teams, working on things that move the needle

---

# Links & Evidence

| Resource | URL |
|----------|-----|
| LinkedIn | [linkedin.com/in/mote](https://www.linkedin.com/in/mote) |
| Website | [markmote.com](https://markmote.com) |
| Pytheia demos | [youtube.com/@PytheiaAI](https://youtube.com/@PytheiaAI) |
| Argus demo | [youtube.com/watch?v=Wdzhru0Y5f0](https://youtube.com/watch?v=Wdzhru0Y5f0) |
| Stanford testbed | [youtube.com/watch?v=4kOOn6TPuDI](https://youtube.com/watch?v=4kOOn6TPuDI) |
| PhD spacecraft demo | [youtube.com/watch?v=JQBrW4yLVHk](https://youtube.com/watch?v=JQBrW4yLVHk) |
| Pytheia site (historical) | [pytheia.com](https://www.pytheia.com/) |

---

# Portfolio (Recommended for Web)

## Roostr

- **Screenshots:** Rate search UI, quote builder, workflow state view
- **Diagram:** Email → extraction pipeline → structured rates
- **Story:** Reliability loop (monitoring + regression + fast fixes)

## Pytheia / Argus

- **Embedded demo clip:** 3D tracking visualization
- **Pipeline diagram:** Detection → Tracking → Projection → Fusion
- **Key insight:** Spatial frame vs image frame—why it matters

## Research

- **Top 3–5 papers** with "why it mattered" bullets
- **Google Scholar link** prominently displayed

---

*Last updated: January 2026*
