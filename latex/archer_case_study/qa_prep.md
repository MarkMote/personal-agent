# Archer Presentation Q&A Prep

## I. Safety & Runtime Assurance Fundamentals

**Q: What are the assumptions for using a control barrier function?**
1. **Control-affine dynamics**: $\dot{x} = f(x) + g(x)u$ -- needed so the CBF constraint is linear in $u$ and the QP is convex
2. **Convex input set** $U$ -- for QP tractability
3. **Known dynamics** -- you need $f(x)$, $g(x)$ to compute Lie derivatives
4. **Full state observation** -- need $x$ to evaluate $h(x)$ and constraints
5. **Smoothness** -- $h$, $f$, $g$ continuously differentiable (Nagumo's theorem)
6. **Non-degenerate boundary** -- $\nabla h(x) \neq 0$ on $\{x : h(x) = 0\}$
7. **Relative degree 1** -- $L_g h(x) \neq 0$, i.e. the input directly affects $\dot{h}$. Higher relative degree requires higher-order CBFs.

**Q: What if the CBF-QP is infeasible?**
Infeasibility means no input exists that satisfies both the barrier constraint and actuator limits. This happens when the safe set $\mathcal{C}_S$ is not actually control invariant. The fix: ensure $\mathcal{C}_S$ is truly control invariant (which is the hard part -- finding large control invariant sets is the central challenge).

**Q: What's the difference between forward invariance and control invariance?**
Forward invariance is w.r.t. a specific closed-loop system (one controller). Control invariance says there *exists* some admissible controller that achieves it. Control invariance is a property of the set + dynamics + input bounds, not a specific controller.

**Q: Why not just prove the primary controller is safe?**
RTA decouples safety from the controller. This lets you use unverified controllers (ML, human pilots, experimental code) while guaranteeing safety. Much more flexible -- you verify the filter once, then swap controllers freely.

**Q: What is Nagumo's theorem?**
If $\dot{h}(x) \geq 0$ for all $x$ on the boundary of $\mathcal{C}_S$ (where $h(x) = 0$), then $\mathcal{C}_S$ is forward invariant. Intuitively: the vector field never points outward at the boundary.

**Q: What is the class-K function $\alpha$ doing?**
It relaxes the barrier condition in the interior of the safe set. Without $\alpha$, you'd only enforce $\dot{h} \geq 0$ on the boundary. With $\alpha(h(x))$, you get $\dot{h} \geq -\alpha(h)$, which allows $h$ to decrease in the interior but guarantees it never crosses zero. Common choice: $\alpha(h) = \gamma h$ (linear).

**Q: What's the difference between SBSF (switching) and IASIF (QP)?**
- **SBSF**: Binary switch -- either pass $u_\text{des}$ or apply $u_b$. Simpler, no QP, but less smooth (hard switching can cause chattering).
- **IASIF**: Solves a QP to find the minimum intervention. Smoother, stays closer to desired input, but requires more computation (Jacobian propagation + QP solve).

**Q: How does implicit safe set approach avoid finding large safe sets?**
Instead of characterizing the entire safe set offline, you only need a small backup set $\mathcal{C}_b$ and a backup controller. At runtime, you simulate forward under the backup controller from the current state. If the trajectory stays in $\mathcal{C}_A$ and reaches $\mathcal{C}_b$, the current state is safe. The safe set is implicitly defined by all states from which this simulation succeeds.

**Q: What's the computational cost of IASIF at runtime?**
Per timestep: integrate the backup trajectory ($N$ steps), propagate the $n \times n$ Jacobian along it, then solve a QP with ~$N \times M + 1$ affine constraints (where $M$ is number of safety constraints). For the ARPOD problem: 75 trajectory points, solved at ~10 Hz.

**Q: How is Auto-GCAS related to your work?**
Auto-GCAS uses the same principle as SBSF: simulate a recovery maneuver (wings-level pull-up), and if the predicted trajectory would hit terrain, override the pilot. It's the implicit safe set / switching filter idea deployed operationally on F-16s. My work generalizes this with QP-based filters and formal guarantees.

**Q: You present safety as forward invariance -- are there other definitions?**
Yes. Reach-avoid (reach a goal while avoiding bad states), finite-time safety (safe for $T$ seconds but not necessarily forever), probabilistic safety (safe with probability $\geq p$). Forward invariance is the strongest deterministic guarantee. For the nondeterministic attitude problem, it becomes *robust* forward invariance (safe for all possible disturbances).

**Q: The viability kernel is defined as the largest control invariant subset -- how do you actually compute it?**
In general, it's very hard. For low-dimensional systems you can use Hamilton-Jacobi reachability (solve a PDE on a grid). For higher dimensions, it's intractable -- which is exactly why implicit methods are valuable. You sidestep computing the viability kernel entirely by instead checking membership online via simulation.

**Q: What happens between discrete sample points on the backup trajectory? Could the system violate a constraint between checks?**
Yes, this is a real gap. The IASIF checks constraints at $N$ discrete points along the trajectory. Between those points, constraint violations are possible. You can mitigate by: (1) choosing small $\Delta t$, (2) using Lipschitz bounds to certify inter-sample safety, or (3) using continuous-time barrier certificates instead. The presentation glosses over this.

**Q: The Robotarium slide says "near-zero stopping distance" makes $\mathcal{C}_A$ already control invariant -- why?**
Single-integrator robots ($\dot{x} = u$) can stop instantly. So every state in the constraint set is safe: just set $u = 0$. No momentum to bleed off, no risk of coasting through a boundary. This is why CBFs work trivially there. Real systems with inertia (spacecraft, eVTOL) are much harder -- you need braking distance, and that's where the backup trajectory comes in.

**Q: What's relative degree and why does it matter for CBFs?**
Relative degree is how many times you differentiate $h(x)$ before $u$ appears. If $L_g h(x) = 0$ (relative degree > 1), the input doesn't directly affect $\dot{h}$, so the standard CBF constraint $L_f h + L_g h \cdot u \geq -\alpha(h)$ is trivially satisfied for all $u$ and provides no useful filtering. You need higher-order CBFs (HOCBF) that differentiate further. The ARPOD position constraints have relative degree 2 w.r.t. thrust (position -> velocity -> acceleration/thrust), which is one reason we use implicit methods instead.

---

## II. ARPOD / CWH Equations

**Q: What are the CWH equations and what do they assume?**
Clohessy-Wiltshire-Hill equations describe relative motion of a chaser spacecraft w.r.t. a target in a local (Hill's) frame. Assumptions:
1. Target is in a **circular** orbit (constant $n$)
2. Separation distance is **small** relative to orbital radius
3. No perturbations (no drag, J2, third-body, SRP) -- two-body only
4. Point masses

**Q: What is the mean motion $n$?**
$n = \sqrt{\mu / a^3}$ where $\mu$ is gravitational parameter and $a$ is the semi-major axis of the target's orbit. It's the angular rate of the circular reference orbit. LEO (~400 km): $n \approx 0.0011$ rad/s, period ~90 min.

**Q: Why are CWH equations linear?**
They're a first-order Taylor expansion of the relative dynamics about the target's circular orbit. The linearization is valid when the chaser-target separation is small compared to the orbital radius (~6800 km for LEO). This linearity is what makes the IASIF and MIP formulations tractable.

**Q: What is a natural motion trajectory (NMT)?**
Solution to CWH with zero thrust ($u = 0$). Closed NMTs (CNMTs) are periodic: they form 2:1 ellipses (semi-major along y-axis) with period $\tau = 2\pi/n$. The periodicity condition is $v_y = -2n s_x$ (no secular drift in $s_y$). Adding $v_x = 0.5n s_y$ gives elliptical CNMTs centered at the target.

**Q: Why is $v_y = -2n s_x$ the closure condition?**
From the analytical CWH solution, $s_y(t)$ has a secular (linearly growing) term: $-6nt \cdot s_{x_0} - 3nt \cdot v_{y_0}/n$. Setting this to zero gives $v_{y_0} = -2n s_{x_0}$. Without it, the chaser drifts away along-track.

**Q: Why use CNMTs as the backup set?**
They're fuel-free (no thrust needed to maintain), naturally periodic, and form a linear subspace so it's easy to define a stabilizing backup controller. The backup set is the subset of CNMTs that stay within the constraint set. Physically meaningful: "park in a safe orbit and coast."

**Q: How does the backup controller work for ARPOD?**
Linear error feedback. Define error as deviation from the NMT subspace: $e_1 = v_x - 0.5n s_y$, $e_2 = v_y + 2n s_x$. The controller drives $e \to 0$ exponentially at rate $K$. Once $\|e\| < \epsilon$, you're on a CNMT and need no further thrust.

**Q: Why use a MIP for the backup controller instead of something simpler?**
The constraint set has non-convex geometry (approach corridor + keep-out zone). Integer variables encode the non-convexity (e.g., which side of the keep-out zone you pass). Benefits: global optimality, completeness (finds a solution if one exists), and can minimize fuel.

**Q: What are the safety constraints in the ARPOD problem?**
- Keep-out sphere around the target (collision avoidance)
- Approach corridor (cone-shaped, defines valid approach angles)
- Velocity limits
These form the constraint set $\mathcal{C}_A$.

**Q: How does this scale to more complex dynamics (e.g., elliptical orbits)?**
CWH is circular-orbit only. For elliptical orbits, you'd use Tschauner-Hempel equations (time-varying, but still linear). The IASIF framework still applies since it only needs forward simulation, but the NMT-based backup set wouldn't transfer directly -- you'd need a different backup strategy.

**Q: The out-of-plane CWH dynamics are "uncoupled; undamped oscillator" -- what does that mean for safety?**
The $z$-axis dynamics ($\ddot{s}_z = -n^2 s_z$) are completely independent of $x$-$y$. It's a simple harmonic oscillator with period $2\pi/n$. Safety in $z$ can be handled separately. The ARPOD work focuses on the in-plane ($x$-$y$) problem because that's where the coupling (Coriolis terms $2n\dot{x}$, $-2n\dot{y}$) and the interesting constraint geometry live.

**Q: Where does the 2:1 ellipse aspect ratio come from?**
From the CWH solution: a CNMT has semi-major axis $2a_0$ along $y$ and semi-minor axis $a_0$ along $x$. The factor of 2 comes from the Coriolis coupling in the CWH equations. The eccentricity $e = \sqrt{3/4} \approx 0.866$ follows directly from the 2:1 ratio.

**Q: How do integer variables encode non-convexity in the MIP?**
Big-M method. For example, the keep-out sphere can be represented as: you must be on one side or the other. Binary variable $z = 0$ activates "pass left" constraints, $z = 1$ activates "pass right." The constraint set for each choice is convex; the binary variable selects which. Same idea for "which CNMT to target" and "which approach corridor face to respect."

**Q: What solver do you use for the MIP?**
Gurobi or CPLEX (commercial MIP solvers). These use branch-and-bound with LP relaxation. For the ARPOD MIP, solve times are seconds to minutes depending on the scenario -- not real-time, but acceptable for offline backup trajectory planning.

**Q: How do you choose the backup controller gain $K$?**
Tradeoff: large $K$ means faster convergence to the NMT (smaller backup set needed, shorter simulation horizon), but requires more thrust (may violate actuator limits). Small $K$ is gentler but the backup trajectory takes longer and the safe set shrinks. In the paper: $K = 0.01$ 1/s, chosen to be well within thrust limits.

**Q: The IASIF requires propagating the Jacobian $D\phi$ -- what is that concretely?**
It's the $n \times n$ state transition matrix (sensitivity of the backup trajectory endpoint to the initial condition). You integrate the variational equation $\dot{\Phi} = A(t) \Phi$ alongside the backup trajectory, where $A(t) = \partial F / \partial x$ evaluated along the trajectory. For linear CWH dynamics, $A$ is constant so this is straightforward. For nonlinear systems (attitude), it's more expensive.

**Q: Why not use LQR or MPC as the backup controller?**
LQR could work for the stabilization to NMT part (and is essentially what we do -- the error feedback is a simple linear controller). MPC would be better in principle but too slow to evaluate at each IASIF timestep (you'd be solving an optimization inside an optimization). The backup controller needs to be cheap to simulate.

---

## III. Attitude Control / Nondeterministic Extension

**Q: What changes when you have disturbances/nondeterminism?**
You can no longer simulate a single backup trajectory because you don't know what $w$ will be. Instead, you must bound *all possible* trajectories under all $w \in W$. Replace trajectory simulation with reachable set overapproximation (RSO).

**Q: What is mixed monotonicity and why use it?**
A technique to compute tight hyperrectangular overapproximations of reachable sets by integrating a single $2n$-dimensional "embedding" system instead of sampling many trajectories. It exploits the structure of how each state variable's derivative depends monotonically on other state variables. Advantage: one ODE integration gives guaranteed bounds.

**Q: How is the robustly invariant backup set found?**
Using Lyapunov analysis + sum-of-squares (SOS) programming. SOS is an offline convex optimization that certifies polynomial Lyapunov functions, giving a provably invariant sublevel set. This is done once offline.

**Q: What's the LOS constraint physically?**
The boresight vector (e.g., antenna or sensor) must stay within a cone around a target direction. The half-angle $\beta_\text{max}$ defines the cone. Expressed as: $\cos(\beta) \geq \cos(\beta_\text{max})$, which becomes the constraint function $\varphi(x) \geq 0$.

**Q: Why quaternions instead of Euler angles?**
No gimbal lock. Quaternions represent all orientations without singularities. The dynamics $\dot{q} = Q(q)\omega$ are polynomial in $q$, which is nice for SOS/Lyapunov analysis.

**Q: How conservative is the reachable set overapproximation?**
Mixed monotonicity gives hyperrectangular (box) bounds, so there's inherent conservatism from wrapping a box around a non-box reachable set. The conservatism grows with the time horizon and disturbance magnitude. In practice, the backup controller is designed to contract quickly, limiting the growth.

**Q: Is this approach real-time capable?**
For the attitude control example, yes. The RSO integration is similar cost to the deterministic trajectory simulation (2n states vs n states), and the switching check is simple comparison. No QP needed -- it's a switching filter, not IASIF.

**Q: What does "sum-of-squares" (SOS) programming actually do?**
SOS is a way to verify that a polynomial is non-negative everywhere (or on a domain). If you can decompose $p(x) = \sum_i q_i(x)^2$, it's clearly non-negative. This is a sufficient condition checkable via semidefinite programming (SDP). For the backup set: you find a polynomial Lyapunov function $V(x)$ such that $\dot{V} \leq 0$ inside a sublevel set, certifying invariance. The computation is offline and exact (no sampling).

**Q: What does the disturbance $w$ represent physically for the attitude problem?**
Unmodeled environmental torques: gravity gradient, solar radiation pressure, magnetic torques, atmospheric drag torque, plus internal sources like reaction wheel friction, slosh, flexible appendage vibrations. Bounded as $w \in [-w_\text{max}, w_\text{max}]^3$. The bound $w_\text{max}$ is a design parameter -- too large and the safe set shrinks to nothing, too small and you lose the robustness guarantee.

**Q: What's the decomposition function in mixed monotonicity?**
A function $d(x, \hat{x})$ that satisfies: (1) $d(x, x) = f(x)$ (recovers true dynamics on diagonal), and (2) $\partial d_i / \partial x_j \geq 0$ and $\partial d_i / \partial \hat{x}_j \leq 0$ (monotonicity in each argument). For systems where $f$ is already monotone in each state variable, $d$ can be constructed by inspection. For general systems, you decompose $f$ into increasing and decreasing parts. The embedding system $\dot{\underline{x}} = d(\underline{x}, \overline{x})$, $\dot{\overline{x}} = d(\overline{x}, \underline{x})$ then propagates tight bounds.

**Q: Why use a switching filter (SBSF) for attitude instead of IASIF?**
The nondeterministic case requires bounding a *set* of trajectories, not just one. The IASIF Jacobian-based approach assumes a single trajectory to linearize around. With RSO, you're tracking bounding boxes, not gradients. A switching filter is more natural: "is the entire reachable set safe? If not, switch." Extending IASIF to nondeterministic systems is an open problem.

**Q: Does the robust approach handle time-varying or state-dependent disturbances?**
As presented, $w$ is bounded but otherwise arbitrary (worst-case over a fixed box). If the disturbance bound depends on state (e.g., gravity gradient torque depends on attitude), you'd need state-dependent $W(x)$, which complicates the RSO. Mixed monotonicity can handle this but the bounds may be more conservative.

**Q: How does the quaternion unit-norm constraint interact with the safety analysis?**
The quaternion must satisfy $\|q\| = 1$ (constraint manifold). The dynamics preserve this automatically if initialized correctly. For SOS analysis, you can either work on $S^3$ directly or add $\|q\|^2 = 1$ as a side constraint. In practice, numerical integration introduces drift, so you renormalize periodically.

---

## IV. Collision-Inclusive Planning

**Q: When would you actually want to plan through collisions?**
When collision-free trajectories don't exist (cluttered environments, failed avoidance, emergency scenarios). Also when allowing a controlled collision leads to significantly better outcomes than the best collision-free plan. Think: bumping off a wall to reach a goal vs. being stuck.

**Q: How do you model collisions?**
Experimentally derived algebraic model: post-collision state is affine in pre-collision normal and tangential velocities. Coefficients fit via least-squares from motion capture data of controlled collisions on an air bearing table. Key property: algebraic (linear constraints), so it integrates into the MIP.

**Q: Why is this approach slow?**
Mixed-integer programs are NP-hard in general. The number of integer variables grows with the number of potential collision events and obstacles. Branch-and-bound solvers can take exponential time in the worst case. Not suitable for real-time replanning.

**Q: How does this relate to RTA?**
Collision-tolerant planners could serve as better backup strategies. If your backup controller can plan through collisions, the implicit safe set is larger (more states are recoverable). The collision-inclusive planner expands the feasible set.

**Q: What's the damage function?**
User-defined cost on collision severity. Could be impact energy, impulse magnitude, etc. The optimizer minimizes total damage subject to reaching the goal. Lets you trade off between path length/fuel and collision severity.

**Q: Does this work for 3D / real spacecraft?**
The formulation is general, but the experimental validation was 3-DOF (planar, air bearing table at Stanford). Extension to 3D and real contact dynamics would require more complex collision models. The MIP formulation scales, but solve times would increase.

**Q: How slow is "very slow" for the collision-inclusive MIP?**
Depends on scenario complexity, but minutes to hours for problems with multiple potential collision events. Each potential collision adds binary variables; the branch-and-bound tree grows exponentially. This is offline planning, not something you'd run in a control loop.

**Q: How do you know the collision model is accurate?**
You don't, perfectly. The algebraic model is fit from experimental data on a specific testbed (air-bearing table, specific materials). Different surfaces, masses, or geometries would need re-calibration. The model captures the dominant physics (coefficient of restitution, friction) but ignores deformation, fragmentation, etc. For spacecraft, real collisions are much more complex.

**Q: Isn't planning through collisions dangerous?**
The point isn't "collisions are good" -- it's that when they're unavoidable, you should plan through them optimally rather than have your planner fail or produce worse outcomes by pretending they can't happen. The damage function lets you penalize collisions heavily while still finding feasible solutions.

**Q: What's the connection between collision-inclusive planning and the safety framework?**
If your RTA backup strategy is "stop" or "slow down," the safe set is limited by braking distance. If the backup strategy can include controlled collisions, more states become recoverable. It's about expanding the implicit safe set by expanding what "recovery" means. This is a conceptual bridge, not something implemented end-to-end in the papers.

---

## V. General / Cross-Cutting

**Q: How does your work differ from Hamilton-Jacobi reachability?**
HJ reachability computes the exact viability kernel via solving a PDE (HJB equation). It gives the true safe set but scales exponentially with state dimension (curse of dimensionality). The implicit approach trades exactness for scalability -- you get a conservative but practical safe set that works in higher dimensions.

**Q: What about learning-based approaches to safety?**
You can learn barrier functions or backup controllers (the segway example uses a NN backup controller). The implicit framework is agnostic to how $u_b$ is designed. But learned components lose formal guarantees unless you verify them separately.

**Q: Could you use this for eVTOL / Archer's vehicles?**
The RTA framework is vehicle-agnostic. The pieces you'd need:
1. Dynamics model (6-DOF flight dynamics)
2. Safety constraints (geofencing, keep-out zones, velocity limits, attitude limits)
3. Backup strategy (e.g., controlled descent, hover, return-to-base)
4. Backup set (e.g., stable hover at safe altitude)
The implicit approach is well-suited because eVTOL dynamics are complex enough that finding large explicit safe sets is hard.

**Q: What about actuator failures / degraded modes?**
The framework handles this if the backup controller accounts for the failure mode. You'd need different backup sets/controllers for different failure scenarios. The robust (nondeterministic) extension helps if you model actuator uncertainty as part of $w$.

**Q: What TRL is this work at?**
The theory and simulation are mature (published, peer-reviewed). Hardware demos exist for the attitude control problem and the Robotarium. Auto-GCAS (same principle) is operational on F-16s. But the specific ARPOD and collision-inclusive implementations are simulation-validated, not flight-tested.

**Q: What are the main limitations of the implicit approach?**
1. **Conservatism**: the backup controller is suboptimal, so the implicit safe set is smaller than the true viability kernel
2. **Computational cost**: online simulation of backup trajectory + Jacobian at each timestep
3. **Backup controller design**: still requires engineering judgment to pick a good $u_b$ and $\mathcal{C}_b$
4. **Model dependence**: still needs a dynamics model for forward simulation
5. **Discrete-time gap**: safety is checked at discrete points along the trajectory, not continuously (inter-sample violations possible without additional analysis)

---

## VI. Background / Career

**Q: Why did you leave academia after your PhD?**
Wanted to build things. The PhD gave deep technical foundations, but I was drawn to the challenge of taking ideas to production. Pytheia was a chance to apply CV/robotics commercially, and Roostr was a chance to build AI systems at scale.

**Q: What did you do at NASA JPL?**
Spacecraft swarm control -- developing algorithms for coordinating multiple spacecraft. Relevant to proximity operations and the multi-agent safety problem.

**Q: What did you do at AFRL?**
Safe spacecraft docking. Directly related to the ARPOD work in this presentation -- applying runtime assurance to autonomous rendezvous and docking.

**Q: What's the connection between your PhD work and what Archer does?**
Both are safety-critical autonomous systems with complex dynamics, actuator constraints, and real consequences for failure. The RTA framework applies directly: eVTOL has 6-DOF flight dynamics, keep-out constraints (terrain, buildings, other aircraft), and needs backup strategies (controlled descent, hover). The attitude control work is especially relevant -- same type of dynamics (rigid body + quaternions), same type of constraints (orientation limits), same disturbance problem (wind gusts instead of space torques).

**Q: You've been at startups for 5 years -- are you rusty on the technical side?**
Both startups were deeply technical. Pytheia was computer vision and robotics (designed the full perception pipeline). Roostr involved building LLM-based agentic systems from scratch. I've stayed current with the field and still think about safety problems regularly -- this presentation is recent work, not a museum piece.

**Q: What would you want to work on at Archer specifically?**
[Tailor based on the role. Natural fits: GNC, flight controls, autonomy, safety/certification, simulation. The RTA framework is directly applicable to flight envelope protection and autonomous flight safety.]
