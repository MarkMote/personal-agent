# SpaceX HM Interview Prep — Cole Morgan
**Date:** Thu Mar 5, 4:00-4:45pm ET
**Format:** 45 min phone. Accomplishment deep-dive + technical. No AI.
**Call:** +17703662040
**Interviewer:** Cole Morgan, Sr. GNC Engineer, Starlink. At SpaceX ~5.5 yrs.

---

## Know Your Interviewer

Cole did his MS at UW's Autonomous Controls Lab under **Prof. Behcet Acikmeseq**, one of the top names in convex optimization for spacecraft trajectory planning. This is directly adjacent to your optimization work. His research interests: spacecraft GNC, optimal trajectory generation, swarm control.

**What this means:** Cole will understand and appreciate your math. He's not a generalist interviewer. You can go deep on optimization, convex relaxations, trajectory generation, and he'll follow. This is a huge advantage for you. Don't dumb it down.

**Mutual connection:** Prince Kuevor (Lincoln Lab). Don't bring up unless it flows naturally.

---

## Interview Structure (Expected)

Based on recruiter notes and Glassdoor reports:

**Part 1: Accomplishment Deep-Dive (~20-25 min)**
SpaceX uses an Elon-style approach: pick 1-2 projects from your resume and drill deep. The logic is that only someone who actually solved a problem can explain the solution in detail. Expect:
- "Tell me about your hardest technical problem"
- "Walk me through exactly how you solved it"
- "Why did you choose that approach over X?"
- "What would you do differently?"

**Part 2: Technical Questions (~15-20 min)**
First-principles GNC questions. Not trivia. Expect derivations and reasoning, not memorized answers. Given Cole's background, likely skewing toward controls and orbital mechanics rather than pure coding.

---

## Your 4 Projects (Ranked for This Interview)

Have these ready to go deep on. Cole will likely pick 1-2 based on your intro.

### 1. JPL — Multi-Spacecraft Swarm Optimization (BEST FIT)
**Why lead with this:** Swarm of spacecraft. Trajectory optimization. Communication constraints. This is the closest thing to Starlink GNC on your resume.
- Optimized trajectories and communication for a swarm of satellites around an asteroid
- Published in AIAA JGCD (the journal Cole's community reads)
- Multi-agent coordination with resource constraints
- **Be ready to explain:** The optimization formulation. What made it hard (coupling between trajectories and comms). How you handled the combinatorial structure. What the solver looked like.

### 2. AFRL — Safe Spacecraft Docking
**Why:** Direct spacecraft GNC application. Safety-critical control with real constraints.
- Built a mechanism that enforced safety by guaranteeing the spacecraft was always on a safe trajectory to a parking orbit
- Runtime assurance / control barrier functions
- **Be ready to explain:** The safety constraint formulation. How you guaranteed feasibility. How this would work operationally (the "always have a safe escape" concept maps to collision avoidance).

### 3. Robotarium — Swarm Safety at Scale
**Why:** Demonstrates "algorithms, not operators" thinking (SpaceX's design philosophy).
- Open-access lab with 100 robots, anyone in the world can run code
- You built the safety layer that prevented untrusted code from damaging robots
- Barrier certificates enforced at runtime
- **Be ready to explain:** How the safety filter works. How it handles multiple agents simultaneously. The real-time computational challenge. The fact that it ran 16,000+ experiments.

### 4. Stanford — Collision-Inclusive Trajectory Optimization
**Why:** Novel, technically impressive, good conversation piece.
- Modeled collisions as constraints rather than failures
- Expanded the feasible set for motion planning
- **Be ready to explain:** Why this is useful (debris-rich environments, constrained spaces). The mathematical formulation. How you handle the discontinuity at impact.

---

## Technical Questions to Expect

### Orbital Mechanics
- **Classical orbital elements:** Know all 6, what each describes, when each is undefined
- **J2 perturbation:** What it does to RAAN and argument of perigee. Why it matters for Starlink (constellation maintenance, sun-sync implications)
- **Hohmann transfer:** Derivation, when it's optimal, why Starlink doesn't use Hohmann (low-thrust spiral orbit raising instead)
- **Relative motion:** CW/HCW equations. "An astronaut throws a baseball in orbit, what happens?" Relative ellipse.
- **Starlink orbit lowering:** 4,400 sats from 550km to 480km. Why? (Solar minimum, slower atmospheric drag, faster ballistic decay needed for safety)

### Controls
- **PD/PID control:** Design a controller for a simple system. Tuning tradeoffs.
- **Bode plots:** Gain/phase margins. Stability analysis in frequency domain.
- **State estimation:** Kalman filter basics. What measurements does a satellite have? (Star tracker, GPS, IMU, magnetometer)
- **Attitude control:** Three-axis stabilization. Momentum management. Why magnetic torquers? (No propellant cost, desaturation of reaction wheels)

### Optimization (Cole's background — likely to probe here)
- **Convex vs. non-convex:** When can you convexify a trajectory problem? Lossless convexification (Acikmeseq's work).
- **Low-thrust trajectory optimization:** Why it's harder than impulsive. Continuous thrust arcs, many-revolution transfers.
- **Your JGCD paper:** Know it cold. He may have read it.

---

## Questions to Ask Cole (Pick 2-3)

Pick based on conversation flow. These show genuine technical curiosity, not generic interest.

1. **"The orbit lowering campaign is moving 4,400 sats this year. What's been the hardest GNC challenge in that?"** (Shows you're tracking current events, asks about a real problem)

2. **"How does the collision avoidance pipeline handle uncertainty propagation at the fleet scale? Is it satellite-side or ground-side decision-making?"** (Shows depth, maps to your safety work)

3. **"What does the development cycle look like from algorithm to running on live satellites?"** (Practical, shows builder mindset)

4. **"What's the GNC team's biggest open problem right now?"** (Shows you want to contribute, not just join)

5. **"V3 is a very different vehicle. How much of the GNC stack transfers vs. needs to be rebuilt?"** (Shows you understand the transition challenge)

---

## Talking Points to Weave In

These aren't things you say directly. Work them in naturally when relevant.

- **"Algorithms, not operators"** is SpaceX's GNC philosophy. Your Robotarium work is literally this: safety guarantees through algorithms, not human supervision. Draw the parallel if it comes up.
- **Scale:** You've thought about multi-agent systems (JPL swarm, Robotarium 100 robots). Starlink is the extreme version. Show you understand what scale changes about the problem.
- **Safety-critical thinking:** Your PhD was about guaranteeing safety for autonomous systems. Starlink collision avoidance is the same problem at planetary scale. This is your unique angle vs. other GNC candidates.
- **Builder, not just theorist:** You founded companies, shipped products, wrote production code. You can implement, not just derive.

---

## Landmines to Avoid

- **C++ depth:** If asked about C++ experience, be honest. "My research was in MATLAB and Python. I'd need to ramp on C++, but the algorithms and math are what I bring." Don't fake it.
- **Don't over-talk startups.** Cole cares about GNC. Roostr and Pytheia are context for "why are you not in aerospace right now," not the main event. Keep startup discussion to 2-3 sentences max unless asked to go deeper.
- **Don't mention other offers or processes.** Not relevant here.
- **Don't ask about comp, remote, hours, or WLB.** Wrong time, wrong person.
- **Don't bring up DOGE or politics.**

---

## 60-Second Opening

If Cole asks "walk me through your background":

"I did my PhD in robotics at Georgia Tech, focused on safety-critical control for spacecraft. My research at JPL was on trajectory optimization for multi-spacecraft swarms, published in JGCD. At AFRL I worked on safe autonomous docking, and at Stanford on collision-inclusive trajectory planning. I was part of the founding team for the Robotarium, an open-access swarm robotics lab that's run over 16,000 autonomous experiments.

After grad school I co-founded two companies as the technical lead. Built real-time perception systems at the first one, and an AI-powered logistics platform at the second. Great experience, but spacecraft GNC has always been what I'm most passionate about. Starlink is the hardest and most interesting version of that problem."

~45 seconds. Hits: publications, GNC depth, safety, swarms, builder credibility, passion. Leaves room for Cole to pick a thread.

---

## Quick Reference Card (Print This)

| If Cole asks about... | Lead with... |
|---|---|
| Hardest problem | JPL swarm optimization |
| Safety / reliability | AFRL docking + Robotarium barrier certs |
| Multi-agent systems | JPL swarm + Robotarium |
| Optimization | PhD thesis, JGCD paper, Stanford collision work |
| Why startups | Short: "Adventure, learning velocity, but ready to get back to spacecraft" |
| Why SpaceX | "SpaceX is the reason I became an aerospace engineer" |
| Why Starlink specifically | "Swarm of 10K autonomous spacecraft with collision avoidance. It ties together everything I worked on in my PhD" |
| C++ | "Research was Python/MATLAB. Math and algorithms are what I bring. C++ is a tool I'd ramp on." |
| Biggest weakness | C++ honestly. Or: "I've been away from aerospace industry for 4 years. Domain knowledge is there, toolchain would need updating." |
