# Full Context: SpaceX - GNC Engineer (Starlink)

_Unstructured reference document for all company research, notes, and context._

---

## Interview Process Research (2026-02-18)

Sources: Glassdoor, interviewing.io, Jointaro, spacecrew.com, Built In, snubber.ai, SpaceX Reddit AMA, various job postings.

### Interview Process Overview

**Timeline:** ~4-8 weeks end-to-end. GNC-specific candidates report ~11 days average on Glassdoor (small sample of 4 reports). Likely longer in practice.

**Stages (typical for engineering roles):**

1. **Recruiter Screen (~15-30 min)**
   - Non-technical / lightly technical
   - Background, motivation, "why SpaceX?"
   - Verify basic qualifications (citizenship, relocation willingness, degree)
   - Do NOT discuss salary expectations or other companies' processes
   - Eric Harvey is the technical recruiter — his call will likely follow this format

2. **Hiring Manager / Technical Phone Screen (~40-60 min)**
   - Hybrid technical + experience discussion
   - One GNC candidate (Jan 2025, Seattle): 40 min, described as "very technical"
   - Topics covered: PD control, orbit determination, frequency domain analysis
   - Resume project deep-dive
   - May include a system design question related to the team's work

3. **Asynchronous Coding/Technical Assessment**
   - Take-home, usually on Codility platform
   - ~3-4 hours of work, 2 weeks to complete
   - Medium-difficulty algorithmic problems (LeetCode-equivalent)
   - Choose your language (C++, Python, etc.)
   - Evaluated on: test coverage, runtime complexity, code style
   - For GNC roles specifically: may include domain-specific problem sets (orbital mechanics, controls) rather than pure SWE algorithms — unclear

4. **Onsite / Virtual Loop (~5 hours)**
   - Strongly recommended to attend in person
   - Components:
     - **Facility tour** (~25 min, if onsite)
     - **Project presentation** (1 hour): Suggest 5 project ideas ahead of time, they pick one. Present to the entire team with source code. Heavy Q&A.
     - **Coding round 1** (1 hour): CodeSignal platform, hybrid algorithmic + design, often SpaceX-related scenarios
     - **Lunch** (~45 min): Informal, with recruiter
     - **Coding round 2** (1 hour): CodeSignal, two interviewers
     - **System design** (1 hour): Ambiguous problem, tests ability to ask clarifying questions
     - **Behavioral** (1 hour): Amazon Leadership Principles style. With hiring manager.
   - Managers have discretion; failing one round may allow a retake

### GNC-Specific Technical Questions (Reported)

**Orbital Mechanics:**
- "Name the six orbital elements" (classical Keplerian elements)
- "What is the effect of Earth's oblateness on the orbital elements?" (J2 perturbations)
- "If the Earth changed into a disc while maintaining its mass, how would that affect a satellite's orbit?"
- "If an astronaut orbiting the Earth threw a baseball, what does the trajectory look like to the astronaut?" (relative motion / CW equations)
- Hohmann Transfer concept and derivation

**Controls:**
- PD control theory and design
- Frequency domain analysis (Bode plots, stability margins)
- Develop a controller in MATLAB for a simple vehicle point-mass model that follows a straight line and executes a U-turn, then present findings
- Inverted pendulum / rocket dynamics controller design

**State Estimation / Navigation:**
- Orbit determination methods
- Attitude determination
- GNSS and radio navigation

**General Engineering:**
- First-principles derivations (not memorization)
- Thermodynamics, structural analysis, fluid mechanics basics may come up

### Recruiter Screen Specific Prep

**Expect these questions:**
- Walk me through your background
- Why SpaceX? (Mission alignment is critical — know the mission, projects, and culture)
- Why this role specifically?
- What interests you about Starlink?
- Visa/citizenship status
- Relocation willingness (Redmond, WA for Starlink GNC)
- Timeline / availability

**Tips:**
- Keep it concise — call is only 15-30 min
- Show genuine passion for the mission (making life multiplanetary)
- Don't volunteer salary expectations
- Don't discuss other companies' process status
- Know Elon's 5-step design process (referenced as important cultural knowledge)

---

## Starlink GNC Team Details

### Location
- **Redmond, WA** (NOT LA — this is the Starlink satellite development facility)
- SpaceX consolidated Seattle-area operations to Redmond Ridge Corporate Center (three-building facility)
- Started with 60 engineers in 2015, has grown significantly

### What They Work On

The Starlink GNC team develops autopilot algorithms for **thousands of satellites** and **2+ million user terminals**. Key areas:

**Sub-teams within Starlink GNC:**
1. **Fleet Management & Orbit Transfer Automation** — Autonomous orbit raising for newly deployed satellites using low-thrust (Hall-effect) propulsion
2. **Collision Avoidance** — Autonomous maneuver planning; 300,000 avoidance maneuvers in 2025 alone. 1-in-a-million collision probability threshold (100x stricter than industry standard). Positions update every 30 minutes.
3. **Constellation-Level Analysis** — Network-level performance optimization, stationkeeping, orbit maintenance (maneuvers every 1-2 days per satellite)
4. **Navigation & State Estimation** — Attitude determination, orbit determination, GNSS, radio navigation
5. **Navigation & Orbit Determination** — Dedicated OD sub-team
6. **Device Navigation & Beam Pointing** — User terminal tracking, beam-steering logic, satellite handoff (each sat visible for only ~minutes at 7+ km/s)
7. **Controls** — Three-axis stabilized spacecraft control (momentum, magnetic, propulsive)
8. **GNC Simulations** — Vehicle dynamics simulator, Monte Carlo sims, HITL testing, visualization

### Key Technical Challenges
- **Scale:** Managing thousands of autonomous satellites simultaneously (not "one mission at a time" like traditional GNC)
- **Autonomy:** "Algorithms, not operators" — designed from ground up for autonomous operation, unlike legacy satellite systems
- **Collision avoidance at scale:** Onboard AI for real-time collision decisions without human intervention
- **Beam allocation:** Allocating beams from satellites to service areas on Earth, accounting for bandwidth demands, radio interference, field-of-view constraints
- **Handover:** Seamless satellite-to-satellite handoff as satellites traverse overhead
  - User-to-satellite: electrically steered beams (instantaneous switching)
  - Satellite-to-gateway: mechanically steered antennas (movement time required)
- **Low-thrust trajectory optimization:** Hall-effect thrusters (krypton propellant) for orbit raising and stationkeeping
- **Telemetry:** Handling out-of-order and delayed data at constellation scale
- **Orbit lowering initiative (2026):** SpaceX lowering thousands of satellites to reduce deorbit time if failure occurs

### Tech Stack
- **Languages:** C++ and Python (production code, not prototypes)
- **Simulation:** In-house vehicle dynamics simulator, Monte Carlo (dispersed), HITL
- **Models:** Multi-body physics, environmental perturbations, power/propulsion/control hardware
- **Data infrastructure:** .NET 5, Kafka, HBase, HDFS, Docker, Kubernetes (for telemetry)
- **Navigation hardware:** Startracker on each satellite
- **Propulsion:** Hall-effect thrusters (krypton)
- **Testing:** Mock ground stations with fixed antennas, software overrides for continuous contact simulation

### Job Requirements (from postings)

**Required:**
- Bachelor's in CS, aerospace, physics, or engineering
- Software development experience in C++ or Python
- U.S. citizen or permanent resident (ITAR)

**Preferred (strong signals of what they value):**
- Master's or PhD in engineering/physics
- Real-world deployed software experience
- Strong orbital mechanics (including low-thrust trajectory optimization, stationkeeping)
- State estimation (attitude determination, orbit determination, GNSS, radio nav)
- Cradle-to-grave development of 3-axis stabilized spacecraft (momentum, magnetic, propulsive control)
- Simulation verification & validation experience
- Numerical probability of collision methods
- Can identify and solve complex problems independently

### Compensation
- Level I: $120,000-$145,000/year
- Level II: $140,000-$170,000/year
- Plus: stock options, 401(k), comprehensive health, 3 weeks vacation, paid parental leave

### Culture Notes (from GNC intern account)
- Team is highly experienced (10+ year veterans at cutting edge of GNC)
- Emphasis on deep problem understanding before implementation (days, not hours)
- Methodical failure analysis, not surface-level patching
- Results must be "airtight" with solid analytical backing
- Clear documentation and narrative presentation of findings
- "More important to be motivated and able to learn quickly than to check every box"
- On-call rotation for satellite operations

---

## Mark's Fit Assessment

### Strong matches:
- PhD in spacecraft controls/optimization — directly relevant
- Published in AIAA JGCD — their community
- JPL research (swarm satellites) — autonomous multi-agent spacecraft
- AFRL docking research — proximity operations / relative nav
- Stanford free-flyer work — spacecraft GNC hands-on
- Control theory + optimization core expertise
- Python production experience from startups
- Computer vision / state estimation background

### Potential gaps to address:
- C++ proficiency level (production C++ specifically)
- Low-thrust trajectory optimization (Hall-effect specific)
- Constellation-scale operations (Mark's experience is more mission-level)
- Keplerian orbital elements drill (make sure these are sharp)
- J2 perturbation effects (be ready to derive, not just state)
- Frequency domain analysis (Bode plots, gain/phase margins) — refresh
- GNSS/radio navigation specifics

### Recruiter call narrative:
- Lead with PhD GNC pedigree (GT, JGCD publications, JPL/AFRL/Stanford)
- Connect to Starlink: "I've spent my career on spacecraft autonomy and controls — Starlink is doing this at unprecedented scale, which is exactly the kind of problem I want to work on"
- Startup experience shows shipping ability (not just research)
- Be ready for: "Why are you leaving your current role?" (have the standard answer ready from Q&A)
