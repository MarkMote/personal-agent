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

---

## Deep Research (2026-03-04) — HM Interview Prep

### Cole Morgan — Hiring Manager Profile

**Current:** Sr. GNC Engineer, SpaceX (since July 2020, ~5.5 years)
**Education:** University of Washington, MS Aerospace Engineering (2018-2020), BS Aerospace Engineering (2014-2018)
**Lab:** UW Autonomous Controls Laboratory (ACL), PI: Prof. Behcet Acikmeseq (known for powered descent guidance / convex optimization — same community as Mark's work)
**Previous experience:**
- UW RAM Accelerator and Rotating Detonation Engine Labs (research assistant, 2016-2018)
- SDI Engineering Inc.
- Co-led GNC subsystem of UW's AA CubeSat team
**Research interests:** Spacecraft GNC, optimal trajectory generation, swarm control, aircraft stability and control
**Publications:** Co-authored paper with SpaceX Starlink GNC team accepted in Space Weather journal. Involved with IEEE Control Systems Magazine tutorial on convex algorithms for fast trajectory generation.
**Location:** Seattle/Redmond, WA area
**Mutual connection:** Prince Kuevor (Mark knows from Lincoln Lab, also at SpaceX)

**Key observations for the interview:**
- Cole's advisor (Acikmeseq) is famous for powered descent guidance and lossless convexification. This is the same optimal control / convex optimization community Mark publishes in. Strong technical overlap.
- Cole's research interests (swarm control, optimal trajectory generation) directly overlap with Mark's JPL work on multi-spacecraft swarm communication/control.
- He joined SpaceX right out of his MS in 2020, so he has grown up professionally on the Starlink GNC problem.
- Since he co-led the CubeSat GNC subsystem, he likely values hands-on spacecraft experience.

### Expanded Job Posting Details (Multiple Active Postings)

SpaceX currently has multiple open GNC roles on the Starlink team in Redmond, indicating significant team growth:

#### 1. GNC Engineer (Starlink) — General
**Responsibilities:**
- Develop highly reliable and performant GNC algorithms, simulations, tools, services, and dashboards using C++ or Python
- Participate in architecture, design, and code reviews
- Perform bulk data analysis on constellation performance metrics
- Write technical documentation for programs and algorithms
- Support on-call operations rotating satellite commanding duties
- Spans sub-teams: constellation design, fleet management, collision avoidance, attitude control, orbit control, state estimation

**Basic Qualifications:**
- Bachelor's in CS, aerospace, physics, or engineering
- Software development experience in C++ or Python

**Preferred:**
- Master's or PhD in engineering/physics
- Spacecraft control experience, orbital mechanics expertise, state estimation knowledge
- "Capability of identifying and solving complex problems with little to no supervision or direction"

#### 2. GNC Engineer, Starlink Controls
**Responsibilities:**
- Design, analysis, implementation of satellite attitude control and momentum management systems
- Develop electromechanical control systems for solar arrays, antenna gimbals, and optical systems
- Create high-fidelity simulations using C++, Python, and MATLAB
- Write and validate production software for spacecraft control algorithms
- Support hardware development and fleet performance monitoring

**Basic Qualifications:**
- Bachelor's in aerospace, physics or engineering
- C++ software development experience
- Expertise in closed-loop control system design and analysis

**Preferred:**
- Rigid body dynamics and orbital mechanics
- Spacecraft flight software development and testing
- State-space and frequency-domain control analysis
- Flexible body dynamics and finite element analysis
- "Fast paced, autonomously driven, and demanding start-up atmosphere"

#### 3. GNC Engineer, Starlink Collision Avoidance
**Responsibilities:**
- Full-stack ownership of automated collision avoidance pipeline
- Satellite-side algorithms + ground-side supporting services + monitoring infrastructure
- Design and implement autonomous on-satellite collision avoidance algorithms using C++
- Design and implement orbit determination systems, including state/uncertainty propagation
- Run Monte Carlo analysis to characterize performance of new features
- Bulk data analysis of telemetry from thousands of satellites
- Write integrated test cases for satellite and ground software
- Monitor on-orbit system performance, troubleshoot
- Coordinate with third-party data providers and constellation operators
- On-call rotation for manual satellite commanding

**Preferred:**
- Strong analytical backgrounds
- Ability to analyze and interpret production data or simulations

#### 4. GNC Engineer, Navigation and Orbit Determination (Starlink)
**Focus:** Atmospheric density uncertainties in predicting satellite states in LEO. Starlink flight data provides opportunities to advance atmospheric modeling.

**Responsibilities:**
- Develop advanced models for real-time atmosphere state estimation
- Improve orbit predictions
- Work closely with collision-avoidance team on space safety

**Basic Qualifications:**
- Master's degree in aerospace, mechanical, or electrical engineering, or physics
- Software development in C++ or Python
- 2+ years professional experience with navigation or orbit determination (internship/research counts)

**Preferred:**
- PhD in aerospace with applications in orbit determination, navigation, or orbit propagation
- Strong understanding of orbital mechanics, perturbations, numerical propagation techniques
- Implemented, tested, tuned, and operated Kalman filters in real-world applications
- Experience with empirical and physics-based atmospheric density models

### Starlink Constellation Technical Details (Updated March 2026)

#### Current Scale
- **~9,400+ active satellites** in orbit (as of early 2026)
- **10M+ subscribers** (adding 20K/day)
- **155+ countries** served
- 65% of all active satellites in orbit are Starlink

#### Orbital Architecture
**Gen1 Constellation (largely complete):**
- Shell 1: 1,584 sats at 550 km, 53.0 deg inclination (72 planes x 22 sats) — being lowered to 480 km in 2026
- Shell 2: 1,584 sats at 540 km, 53.2 deg
- Shell 3: 720 sats at 570 km, 70 deg
- Shell 4: 348 sats at 560 km, 97.6 deg (SSO)
- Shell 5: 172 sats at 560 km, 97.6 deg

**Gen2 Constellation (approved):**
- Up to 29,988 additional satellites approved
- ~10,000 in 525-535 km altitude shells
- ~20,000 in 340-360 km shells
- ~500 in 604-614 km shells

#### Satellite Generations
**V1.0:** 260 kg, Hall-effect thrusters (krypton), star tracker navigation. Legacy fleet, being deorbited.
**V1.5:** Improved V1, also being phased out.
**V2 Mini (current workhorse):** ~800 kg, ~60 Gbps each, 4x V1 capacity. Up to 28 per Falcon 9 launch.
- Argon-fueled Hall thrusters (replacing krypton): 170 mN thrust, 2500 s Isp, 50% efficiency, 4.2 kW power, 2.1 kg mass
- 2.4x thrust and 1.5x Isp over V1 thrusters
- Argon is ~100x cheaper than krypton, ~1000x cheaper than xenon
**V3 (coming 2026):** ~2,000 kg, 1,000 Gbps downlink (10x+ over V2 Mini), ~4 Tbps combined RF+laser backhaul.
- Requires Starship for launch (~350 km operational altitude)
- Sub-20ms latency target
- Each Starship launch adds 60 Tbps network capacity (20x current Falcon 9 launches)
- First launches expected H1 2026

#### Collision Avoidance System (Updated Stats)
- **300,000 collision avoidance maneuvers in 2025** (~40 per satellite per year)
- 144,404 maneuvers Dec 2024 - May 2025 alone (200% increase over prior 6 months)
- Growth is exponential: 25,299 in H1 2023 → 50,000 in H2 2024 → 144,404 in H1 2025
- **Collision probability threshold: 3 in 10 million** (tightened from 1-in-100,000, which was already 100x stricter than industry standard 1-in-10,000)
- Maneuvering ~300x more often than industry norm
- Starlink states updated every ~30 minutes
- Fully autonomous: satellites fire thrusters when risk exceeds threshold, no human-in-the-loop
- Screening results available in minutes (vs. hours for industry standard)

#### Stargaze SSA System (Launched Jan 30, 2026)
- Space Situational Awareness system leveraging ~30,000 star trackers across Starlink fleet
- Detects ~30 million object transits daily (orders of magnitude better than ground-based systems)
- Can assess conjunctions in minutes vs. hours
- Real-world demo: detected third-party satellite unexpected maneuver with only 5 hours notice; Starlink reacted within 1 hour
- Free to all satellite operators who submit their own ephemeris data
- Collaboration with NASA Ames on experimental maneuver coordination APIs
- Currently in closed beta with 12+ satellite operators
- Contact: space-safety-onboarding@spacex.com

#### Orbit Lowering Campaign (Jan 2026)
- Lowering all ~4,400 satellites from ~550 km to ~480 km throughout 2026
- Announced Jan 1 by Michael Nicolls (VP Starlink Engineering)
- Rationale: solar minimum approaching → lower atmospheric density at 550 km → slower natural decay
- At 480 km: >80% reduction in ballistic decay time (4+ years reduced to months)
- Fewer debris objects and planned constellations below 500 km
- Coordinated with US Space Command and other operators
- Partly motivated by Dec 2025 anomaly (Starlink-35956 propulsion failure at 418 km, caused debris)

### Compensation Deep Dive

#### Posted Ranges (Base Salary)
- GNC Engineer Level I: $120,000 - $145,000/year
- GNC Engineer Level II: $140,000 - $170,000/year

#### Glassdoor Data (GNC Engineer at SpaceX)
- Estimated total pay: $139K - $227K/year
- Average base: $132K/year
- Average additional pay: $45K/year (stock, bonus, etc.)
- Compensation & benefits rating: 4.8/5 (40% higher than industry average for GNC Engineers)

#### Levels.fyi Data (Aerospace Engineer at SpaceX)
- Median total compensation: $167K/year
- L2 median total: $204,500/year
- Highest reported: $275,875/year
- Data last updated: Feb 6, 2026

#### Equity Structure
- RSUs or ISOs (depending on hire date and role)
- Vesting schedules: 3-year (1yr cliff + 2yr annual) or 5-year (1yr cliff + 4yr semi-annual)
- Employee Stock Purchase Plan (ESPP) at a discount
- Potential discretionary bonuses
- **IPO context:** SpaceX actively preparing for potential 2026 IPO. Valuation ~$800B (late 2025 tender), potential $1.5T at IPO. Equity could become very valuable.

#### Benefits
- 401(k), comprehensive medical/vision/dental
- 3 weeks PTO, 10+ paid holidays
- Short & long-term disability, life insurance
- Paid parental leave

#### Comparison to Other Offers
- Archer offer: $293K TC ($230K base). SpaceX base is $120-170K.
- Gap is significant on cash. SpaceX upside is entirely in equity/IPO.

### Culture / Work Environment (Redmond)

**From reviews:**
- Indeed Redmond rating: 67% would recommend (vs. 61% company-wide)
- Work-life balance: 2.4/5
- Culture & values: 3.4/5
- D&I: 3.6/5
- "Coolest engineering challenges on Earth with some of the smartest people you'll ever meet" — GNC engineer in Redmond
- "Long hours, 50-60 hours a week standard, stressful environment"
- "Well-compensated between base salary and stock options"
- "Lots of opportunities to take on real-world problems and own solutions"
- 5 days/week in office (confirmed by Eric Harvey on recruiter screen)
- Common to get dinner in the office (per Eric)
- 38% of company-wide employees have been there <1 year (high turnover)
- GNC team specifically has 10+ year veterans who are deeply methodical

### HM Interview Format (What to Expect March 5)

**Format:** 45-min phone call with Cole Morgan (Sr. GNC Engineer)
**Structure:** Hybrid accomplishment deep-dive + technical

**What to expect based on research:**
1. **Accomplishment deep-dive (~20-25 min):**
   - Cole has seen your resume and selected something he wants to explore
   - Expect deep drilling: "Tell me about your hardest problem and how you solved it" (Elon-style: anyone can describe the problem, only someone who solved it can explain the solution convincingly)
   - Resume project deep-dive: be ready to go deep on JPL swarm work, AFRL docking, Robotarium, or PhD optimization work
   - He'll want specifics and impact, not hand-waving

2. **Technical questions (~15-20 min):**
   - Reported GNC topics from Glassdoor: PD control, orbit determination, frequency domain analysis
   - First-principles derivations, not memorization
   - Possible system design question related to Starlink GNC work
   - Given Cole's background (Acikmeseq lab, trajectory optimization), expect comfort with optimization and convex methods

3. **Your questions (~5 min):**
   - Keep to 2-3 sharp questions

**Key insight from Eric's call:** The role is "fairly general" — they do a lot of things: simulations, momentum management, actuators and actuator interfaces. Eric specifically asked why Mark wants something as "general" as GNC. Be ready for this again from Cole.

**What Cole likely cares about (based on his background):**
- Can you actually do GNC? (Not just talk about it)
- Do you understand dynamics and controls at a deep level?
- Can you write production code? (C++ and Python)
- Are you motivated enough for the culture?
- Do you get the scale problem? (Thousands of sats, not one mission)
