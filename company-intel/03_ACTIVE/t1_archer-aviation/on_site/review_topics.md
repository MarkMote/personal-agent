# Archer Case Study — Prep Review Topics

Prioritized by: (likely to come up) × (impact if you blank) × (achievable in limited time).

You haven't worked on this daily in 4+ years. The audience knows that. The goal isn't to re-derive everything — it's to be conversational and not get tripped up on the fundamentals of your own work.

---

## TIER 1: Must review (high impact, quick refresh)

### 1. Your own thesis in one paragraph
Can you explain your dissertation contribution in 2-3 sentences without slides? Practice saying it out loud.
- "My thesis was on runtime assurance — how you let a potentially unsafe controller run while guaranteeing that a backup system intervenes before anything bad happens. The core contribution was making this scalable to nonlinear systems using control barrier functions and mixed-integer optimization"
- Dennis and Peter will ask follow-ups. The 2-3 sentence version anchors everything.


### 2. Control Barrier Functions (CBFs) — what they are, how they work
This is the centerpiece. You need to explain it clearly and handle follow-ups.
- What's a CBF? A function h(x) that defines a safe set {x : h(x) ≥ 0}. If you can keep h(x) from decreasing too fast (h_dot(x,u) ≥ -α(h(x))), you stay safe.
- How does it become a controller? You solve a QP at each timestep: minimize deviation from desired control input, subject to the CBF constraint. The QP is small and fast — runs in real time.
- Why is this better than just staying far from obstacles? It's minimally invasive — the safety filter only overrides when necessary, so the nominal controller gets maximum freedom.
- **Review:** The QP formulation. Be able to write it on a whiteboard: min ||u - u_nom||^2 s.t. Lf(h) + Lg(h)u ≥ -α(h(x)).

### 3. Runtime Assurance (RTA) — the architecture
This is the "Move Fast and Not Break Things" framing.
- The pattern: untrusted/aggressive controller → safety filter → actuators.
- The filter is transparent when the system is safe, intervenes only when approaching the boundary.
- Why this architecture? Decouples performance from safety. You can iterate on the performance controller without re-certifying safety. This is directly relevant to Archer's FAA path.
- **Dennis connection:** His postdoc was on formal methods with temporal logic guarantees. Your CBF approach is complementary — his is specification-level ("always eventually reach goal"), yours is state-level ("never enter unsafe set"). Be ready to discuss the relationship.

### 4. Robotarium — the practical story
You built the safety layer that let remote users run untrusted code on real robots without breaking them. This is the most concrete, practical demonstration of your work.
- What was the safety guarantee? Collision avoidance between robots.
- What was the CBF? Based on inter-robot distances.
- What was the backup policy? Robots could stop (xdot = u, simple dynamics).
- Why does this matter? 16,000+ experiments, still running. Real-world validation.
- **Your own critique:** "The Robotarium was easy mode — the robots could just stop. The real challenge is systems where you can't stop, like aircraft."  This is a perfect bridge to Archer.

### 5. How this applies to Archer specifically
You need a clear "here's what I'd do" pitch.
- Archer's #1 challenge: FAA certification for autonomous flight.
- The question FAA asks: "How do you guarantee the vehicle doesn't do something unsafe?"
- Your answer: Runtime assurance. Certify the safety filter separately from the autonomy stack. The filter is mathematically provable. The autonomy stack can evolve without re-certification.
- Specific applications at Archer: detect-and-avoid, geofencing, safe landing corridors, envelope protection (don't exceed structural/aero limits).
- Be honest about gaps: eVTOL dynamics are more complex than ground robots. The CBF design for a full 6-DOF aircraft with aerodynamic coupling is nontrivial. Say this — it shows you understand the real problem.

---

## TIER 2: Should review (likely follow-up questions)

### 6. Invariant sets — the concept
- What's a controlled invariant set? A region of state space you can guarantee you'll never leave, given the right control.
- How do you compute one? For simple systems, Lyapunov-like methods. For complex systems, your thesis used optimization-based approaches (mixed-integer, sum-of-squares).
- Connection to CBFs: the zero-superlevel set of a CBF is a controlled invariant set.
- **Don't need to re-derive.** Just be clear on the concept and why it matters.

### 7. Mixed-integer programming for trajectory planning
- Why mixed-integer? It handles combinatorial constraints (obstacle avoidance, mode switching) that continuous optimization can't.
- Your Stanford work: collision-inclusive trajectory optimization. Used MIPs to plan trajectories where bouncing off obstacles was allowed and sometimes optimal.
- Your AFRL work: natural motion trajectories for spacecraft docking. MIP for optimal transfer between safe parking orbits.
- **Key limitation:** MIPs are NP-hard. Solve time grows with problem size. Real-time is hard for large problems.

### 8. Scalability — the honest gap
- Your thesis contribution was making CBFs work for more complex systems, but there's still a gap between ground robots and full aircraft.
- The QP is fast, but designing the CBF itself for high-dimensional systems is hard.
- The Gurriet/Ames/Mote paper on "scalable controlled set invariance" was about pushing this boundary.
- Be ready to discuss: what's still unsolved? What would you need to make this work on Midnight?

### 9. Spacecraft work (AFRL, JPL) — brief talking points
- AFRL: safe spacecraft docking, backup guidance using natural motion trajectories. Combining RTA with RL.
- JPL: communication-aware swarm navigation around asteroids. Multi-agent coordination.
- These are cool stories but not the main focus. Keep them to 1-2 minutes each as "breadth" examples.

---

## TIER 3: Nice to have (if time permits)

### 10. Formal verification of neural networks (MIT Lincoln Lab)
- You applied formal verification to image classifiers. Can't discuss specifics (restricted).
- But the concept is relevant: how do you certify that an AI component is safe? Formal methods, not just testing.
- Dennis will appreciate this — it connects to his formal methods background.

### 11. Lyapunov stability refresher
- CBFs are the safety analog of Lyapunov functions for stability.
- Lyapunov: V(x) > 0 and V_dot(x) < 0 → stable. CBF: h(x) ≥ 0 and h_dot(x,u) ≥ -α(h) → safe.
- The parallel helps explain CBFs to people who know Lyapunov but not CBFs (probably most of the panel).

### 12. Current state of the field
- What's happened in safe autonomy since 2021? CBFs have exploded in popularity.
- If they ask "what would you do differently now?" — have a 1-2 sentence answer. E.g., learning-based CBFs, data-driven barrier functions, compositional safety for multi-agent systems.

---

---

## GENERAL KNOWLEDGE: Staff Autonomy Engineer at an eVTOL company

These aren't about your PhD — they're things the panel might ask or expect you to be conversational on given the role.

### G1. eVTOL flight phases and autonomy challenges (HIGH PRIORITY)
- Phases: takeoff (hover), transition (hover→cruise), cruise, transition (cruise→hover), landing
- Each phase has different dynamics, different safety concerns, different control modes
- Transition is the hardest — mixed aerodynamic and rotor authority, rapidly changing dynamics
- Know Archer Midnight basics: 6 tilt rotors, 6 lift rotors (lift only used in hover/transition), V-tail, 4 passengers, ~60 mile range, ~150 mph cruise
- FAA certification path: Part 135 air carrier certificate + type certificate for the aircraft

### G2. Detect and Avoid (DAA)
- What it is: the autonomous equivalent of "see and avoid" for piloted aircraft
- Why it matters: FAA requires it for autonomous operations in controlled and uncontrolled airspace
- Components: surveillance (ADS-B, radar, cameras, lidar), tracking, threat assessment, avoidance maneuver generation
- Connection to your work: the avoidance maneuver generator is exactly a safety filter / CBF application
- ACAS-X: the FAA's next-gen collision avoidance system. Uses dynamic programming / MDPs. Know it exists.

### G3. V&V (Verification and Validation) for autonomous systems
- How do you prove an autonomous system is safe enough to certify?
- Testing alone isn't enough — combinatorial explosion of scenarios
- Formal methods: prove properties mathematically (Dennis's background)
- Runtime assurance: your approach — don't certify the whole system, certify the safety envelope
- DO-178C: software certification standard for airborne systems. Know it exists and that it's the bar Archer has to clear.
- The "long tail" problem: how do you handle rare edge cases?

### G4. Sensor fusion for autonomous flight
- Typical sensor suite: IMU, GPS, barometer, airspeed, lidar, cameras, ADS-B
- State estimation: Extended Kalman Filter (EKF) or factor graph-based approaches
- Degraded modes: what happens when GPS is lost? When a sensor fails?
- Dheepak's background is VIO/SLAM — he may probe this area
- Connection to your work: state estimation feeds into the safety filter. Uncertainty in state → uncertainty in safety guarantee.

### G5. Path planning for urban air mobility
- Vertiport-to-vertiport routing with constraints: no-fly zones, noise abatement, weather, traffic
- Real-time replanning: what if conditions change mid-flight?
- Connection to your work: your MIP-based trajectory optimization is directly applicable
- Energy management: battery constraints mean you can't just reroute freely. Range anxiety is real.

### G6. Multi-agent / fleet autonomy
- Archer will eventually run fleets of vehicles in dense urban airspace
- Deconfliction: how do multiple vehicles avoid each other?
- Centralized vs decentralized control
- Connection to your work: Robotarium (multi-agent), JPL swarm work, Peter Anderson's multi-agent background

### G7. Reinforcement Learning + Safety
- RL is increasingly used for autonomous control, but has no safety guarantees out of the box
- Your AFRL work: combining RTA with RL — let RL explore aggressively, safety filter prevents catastrophic actions
- This is a hot topic. Dennis (TuSimple background) and Peter (RL research) will both be interested.
- Sim-to-real gap: policies trained in simulation may not transfer. Safety filter as a safety net for sim-to-real transfer.

### G8. Simulation and testing infrastructure
- How do you test autonomy before flight?
- Hardware-in-the-loop (HIL), software-in-the-loop (SIL), digital twin
- Monte Carlo testing: run thousands of randomized scenarios, check for safety violations
- You did this at the Robotarium — software verification before deploying on hardware
- Mason's background includes simulation (AirSim, Carla). Dennis built simulation at multiple companies.

### G9. Archer competitors and landscape
- Joby Aviation: further along in FAA certification, recently got Part 135 certificate
- Lilium: different design (ducted fans), filed for bankruptcy 2024 then restructured
- Wisk (Boeing-backed): fully autonomous from the start (no pilot)
- Beta Technologies: charging infrastructure focus
- Archer's differentiation: manufacturing approach, pilot-in-the-loop as stepping stone to full autonomy
- Key question: what does the autonomy roadmap look like? Pilot assist → reduced crew → fully autonomous?

### G10. Systems engineering mindset
- At Staff level, they'll expect you to think about how pieces fit together, not just your sub-system
- How does the safety filter interact with the flight controller, the path planner, the perception stack?
- What happens when components disagree? Arbitration, priority, graceful degradation.
- You have this from being a sole engineer at Roostr and Pytheia — you built entire systems, not just components.

---

## Review Format

For each topic, aim for:
1. **Can I explain it in 2 sentences to a smart engineer?** (elevator pitch)
2. **Can I draw the key diagram/equation on a whiteboard?** (for follow-ups)
3. **Can I connect it to Archer's specific problem?** (the "so what")
4. **Do I know the limitations honestly?** (shows maturity)

Don't try to re-learn the proofs. Focus on intuition, practical implications, and honest assessment of what's hard.
