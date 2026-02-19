# GNC Prep — SpaceX + Archer

Two tracks: SpaceX (orbital mechanics, classical controls) and Archer (safe autonomy, eVTOL). Significant overlap in control theory fundamentals.

---

# TRACK A: SpaceX — GNC Engineer (Starlink)

**Next step:** Recruiter call Fri 2/20 2pm ET (non-technical). Technical phone screen comes after.
**Technical screen format:** 40-60 min, "very technical." PD control, orbit determination, frequency domain, resume deep-dive.
**Full process details:** `company-intel/03_ACTIVE/t1_spacex/full_context.md`

## A1. Orbital Mechanics (MUST KNOW)

### Six Classical Orbital Elements (Keplerian)
Be able to name all six, draw them, and explain what each controls:
1. **a** — semi-major axis (size of orbit, determines period)
2. **e** — eccentricity (shape: 0=circle, 0<e<1=ellipse, e=1=parabola)
3. **i** — inclination (tilt relative to equatorial plane)
4. **Ω** — RAAN / right ascension of ascending node (orientation of orbital plane)
5. **ω** — argument of periapsis (orientation of ellipse within plane)
6. **ν** — true anomaly (position along orbit)

### J2 Perturbation Effects
Earth isn't a sphere — it's oblate. The J2 term (largest perturbation) causes:
- **RAAN drift (Ω̇):** Nodal regression. Rate depends on a, e, i. Used for sun-synchronous orbits.
- **Argument of periapsis drift (ω̇):** Apsidal rotation.
- **No secular effect on a, e, i** — only periodic oscillations.
- Formula: Ω̇ = -3/2 * n * J2 * (R_E/p)^2 * cos(i), where p = a(1-e^2)
- **Why it matters for Starlink:** Must account for differential RAAN drift across the constellation. Satellites at different inclinations/altitudes drift apart.

### Hohmann Transfer
- Minimum-energy two-impulse transfer between circular orbits
- ΔV₁ at periapsis of transfer ellipse, ΔV₂ at apoapsis
- Transfer time = half the period of the transfer ellipse
- **For Starlink:** Not directly used (they use low-thrust), but the concept underlies orbit-raising strategy

### Relative Motion (CW/Hill Equations)
- "If an astronaut threw a baseball, what does the trajectory look like?" — The ball follows an elliptical relative orbit (CW equations).
- Key insight: in the LVLH frame, motion is coupled. Radial displacement causes along-track drift.
- This is relevant to formation flying and proximity operations (your AFRL docking work).

### Low-Thrust Trajectory Optimization
- Starlink uses Hall-effect thrusters (krypton propellant)
- Orbit-raising from deployment altitude (~300 km) to operational (~550 km) takes weeks
- Continuous thrust, not impulsive — requires different optimization (indirect/direct methods, shooting, collocation)
- **Your angle:** PhD was optimization for spacecraft controls. Low-thrust is a natural extension.

---

## A2. Controls (MUST KNOW)

### PD Control Design
Be able to design a PD controller for a simple system and explain each term.
```
u(t) = Kp * e(t) + Kd * ė(t)

- Kp: proportional gain — drives error to zero
- Kd: derivative gain — dampens oscillation, adds phase lead
- No Ki: PD is sufficient for many spacecraft applications (no steady-state load)
```

**Simple example:** 1D point mass, ẍ = u. Design PD controller to track reference x_ref.
- e = x_ref - x
- u = Kp * e + Kd * (ẋ_ref - ẋ)
- Closed-loop: ẍ + Kd*ẋ + Kp*x = Kd*ẋ_ref + Kp*x_ref
- Characteristic equation: s² + Kd*s + Kp = 0
- Choose Kp, Kd for desired natural frequency ωn and damping ratio ζ: Kp = ωn², Kd = 2ζωn

### Frequency Domain Analysis (REFRESH)
They asked about this in technical screens. Be conversational, not rusty.

**Bode Plots:**
- Magnitude plot (dB vs log freq) and phase plot (degrees vs log freq)
- Key features: DC gain, roll-off rate (-20dB/dec per pole), resonance peak
- Read off: bandwidth, gain margin, phase margin

**Stability Margins:**
- **Gain margin:** how much you can increase gain before instability. Read from Bode where phase = -180°.
- **Phase margin:** how much additional phase lag before instability. Read from Bode where magnitude = 0dB.
- Rule of thumb: gain margin > 6dB, phase margin > 30-45° for robust design.

**Transfer Functions:**
- G(s) = Y(s)/U(s) — input-output relationship in Laplace domain
- Poles = roots of denominator → stability (must be in LHP)
- Zeros = roots of numerator → affect transient response

### Attitude Control Modes
Relevant for Starlink satellites:
- **Three-axis stabilized:** momentum wheels (reaction wheels), magnetic torquers, thrusters
- **Momentum management:** reaction wheels saturate → must desaturate using magnetic torquers or thrusters
- **Attitude determination:** star tracker (primary, each Starlink sat has one), gyroscope, magnetometer

---

## A3. State Estimation / Navigation

### Orbit Determination
- GPS/GNSS: primary for LEO. Starlink sats have GNSS receivers.
- Ground-based tracking: radar, optical
- Filtering: batch least squares, sequential (Kalman filter)
- **Your JPL work:** communication-aware swarm navigation — relevant

### Attitude Determination
- Star tracker: measures star positions → computes quaternion
- Gyroscope: measures angular rate → propagates attitude between star tracker updates
- TRIAD / QUEST algorithms for attitude from vector observations
- Kalman filter to fuse: gyro propagation + star tracker updates

---

## A4. SpaceX-Specific Knowledge

### Starlink Facts
- 6,000+ satellites in orbit, targeting 12,000+
- ~550 km operational altitude, 53° inclination (and other shells)
- 300,000 collision avoidance maneuvers in 2025
- Hall-effect thrusters, krypton propellant
- Each satellite has: star tracker, GNSS receiver, reaction wheels, krypton thrusters
- "Algorithms, not operators" — autonomous operation at scale
- Beam allocation: electrically steered beams (phased array), rapid handoff between satellites

### Culture
- Elon's 5-step design process: (1) make requirements less dumb, (2) delete the part/process, (3) simplify/optimize, (4) accelerate cycle time, (5) automate
- Deep problem understanding before implementation
- Results must be "airtight" with solid analytical backing
- More important to be motivated and able to learn quickly than to check every box

---

# TRACK B: Archer — Staff Autonomy Engineer

**Interview:** Thu Feb 26, onsite San Jose. Case study (1hr) + 5 individual interviews (30 min each).
**Full prep:** `company-intel/03_ACTIVE/t1_archer-aviation/on_site/review_topics.md` (comprehensive)
**Case study notes:** `on_site/case_study.md`

The review_topics.md file is the primary study guide for Archer. This doc summarizes the key areas; go to that file for depth.

## B1. Your Thesis — Say This Out Loud (PRACTICE)

> "My thesis was on runtime assurance — how you let a potentially unsafe controller run while guaranteeing that a backup system intervenes before anything bad happens. The core contribution was making this scalable to nonlinear systems using control barrier functions and mixed-integer optimization."

Practice saying this until it's natural. Dennis and Peter will ask follow-ups.

## B2. Control Barrier Functions (centerpiece)

**What:** h(x) defines safe set {x : h(x) ≥ 0}. If h_dot(x,u) ≥ -α(h(x)), you stay safe.

**How it becomes a controller:** QP at each timestep:
```
min  ||u - u_nom||²
s.t. Lf(h) + Lg(h)·u ≥ -α(h(x))
```
QP is small and fast → runs in real time.

**Why it's better:** Minimally invasive. Safety filter only overrides when necessary. Nominal controller gets maximum freedom.

**Be able to draw this on a whiteboard.**

## B3. Runtime Assurance Architecture

```
Untrusted/aggressive controller → Safety Filter (CBF-QP) → Actuators
```
- Filter is transparent when safe, intervenes only near boundary
- Decouples performance from safety → can iterate on performance controller without re-certifying safety
- **Directly relevant to Archer's FAA path:** certify the safety filter, not the entire autonomy stack

## B4. Robotarium Story

- Built safety layer for remote multi-agent robotics lab at Georgia Tech
- CBF based on inter-robot distances → collision avoidance
- 16,000+ experiments, still running
- **Your own critique:** "Easy mode — robots could just stop (ẋ=u). Real challenge is systems that can't stop, like aircraft." → Bridge to Archer.

## B5. How This Applies to Archer

- FAA's core question: "How do you guarantee the vehicle doesn't do something unsafe?"
- Your answer: runtime assurance. Certify the safety filter separately.
- Applications: detect-and-avoid, geofencing, safe landing corridors, envelope protection
- **Be honest about gaps:** eVTOL dynamics are more complex than ground robots. CBF design for 6-DOF aircraft with aerodynamic coupling is nontrivial. Saying this shows maturity.

## B6. General eVTOL Knowledge

- **Flight phases:** takeoff (hover) → transition → cruise → transition → landing
- **Transition is hardest:** mixed aero/rotor authority, rapidly changing dynamics
- **Midnight:** 6 tilt rotors, 6 lift rotors, V-tail, 4 passengers, ~60 mi range, ~150 mph cruise
- **FAA path:** Part 135 air carrier cert + type certificate
- **DO-178C:** software certification standard for airborne systems
- **ACAS-X:** next-gen collision avoidance (dynamic programming / MDPs)
- **Competitors:** Joby (further on FAA cert), Wisk (fully autonomous), Lilium (ducted fans), Beta (charging infra)

## B7. Audience Quick Reference

| Interviewer | Background | What they'll probe |
|---|---|---|
| Mason U'ren | Simulation (AirSim, Carla) | Sim infrastructure, testing |
| Peter Anderson | RL research | RL + safety, your AFRL work |
| Dheepak Khatri | VIO/SLAM | Sensor fusion, perception |
| Suresh Kannan | Behavioral/hiring manager | Judgment, culture, timeline |
| Dennis Ding | Formal methods, TuSimple | Formal verification, temporal logic, CBF relationship |

---

# SHARED: Control Theory Fundamentals

These overlap between SpaceX and Archer. Review once, use for both.

## Lyapunov Stability
- V(x) > 0 and V̇(x) < 0 → asymptotically stable
- CBFs are the safety analog: h(x) ≥ 0 and ḣ(x,u) ≥ -α(h) → safe
- This parallel helps explain CBFs to people who know Lyapunov but not CBFs

## State Space / Transfer Functions
- State space: ẋ = Ax + Bu, y = Cx + Du
- Transfer function: G(s) = C(sI-A)⁻¹B + D
- Poles = eigenvalues of A = roots of det(sI-A)
- Stability: all eigenvalues in LHP (continuous) or inside unit circle (discrete)

## Key Equations to Have Ready
- PD controller: u = Kp*e + Kd*ė, characteristic eq s² + 2ζωn*s + ωn² = 0
- CBF constraint: Lf(h) + Lg(h)u ≥ -α(h)
- Hohmann ΔV: ΔV₁ = √(μ/r₁)(√(2r₂/(r₁+r₂)) - 1)
- J2 RAAN drift: Ω̇ = -3/2 n J2 (R_E/p)² cos(i)
- Vis-viva: v² = μ(2/r - 1/a)

---

## Study Schedule

| Day | SpaceX | Archer |
|-----|--------|--------|
| Thu 2/19 | Review orbital elements + J2 | — |
| Fri 2/20 | (SpaceX recruiter call 2pm — non-technical) | — |
| Sat 2/21 | — | **Full day Archer prep** (case study, review_topics.md) |
| Sun 2/22 | Frequency domain refresh (Bode, margins) | Practice thesis pitch out loud |
| Mon 2/23 | PD control design + state estimation | CBF QP formulation, whiteboard practice |
| Tue 2/24 | (Scale AI morning) | Final Archer touches, interviewer prep |
| Wed 2/25 | — | Light review on flight to SJC |
| Thu 2/26 | — | **Archer onsite** |
