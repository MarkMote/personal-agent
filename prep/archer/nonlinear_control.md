# Nonlinear Control Concepts

Plane review for Archer onsite (2/26). eVTOL dynamics are nonlinear, especially in transition. This covers the main techniques beyond linearization.

---

## Why Nonlinear?

Linear control (LQR, frequency domain) works at a single operating point. An eVTOL in transition between hover and cruise has:
- Rapidly changing aerodynamic forces
- Variable rotor authority (tilt rotors changing angle)
- Coupled translational and rotational dynamics
- Large attitude excursions

Linearization fails when the system operates far from a single equilibrium. You need nonlinear tools.

---

## Feedback Linearization

**Idea:** use nonlinear feedback to cancel the nonlinearities, turning the system into a linear one.

For a SISO system ẋ = f(x) + g(x)u, y = h(x):

```
Step 1: Differentiate the output until the input u appears.

  ẏ = Lfh(x)                          (no u yet)
  ÿ = Lf²h(x) + LgLfh(x)·u          (u appears!)

  where Lf is the Lie derivative along f.

Step 2: Choose u to cancel nonlinearities:

  u = [v - Lf²h(x)] / LgLfh(x)

  Result: ÿ = v (a double integrator!)

Step 3: Design v as a linear controller for the double integrator.
```

### The catch
- Requires exact model knowledge (if f(x) is wrong, cancellation is imperfect)
- Not robust to model uncertainty
- "Zero dynamics" — the internal dynamics not visible from the output — must be stable
- Computationally simple once derived, but the derivation can be complex for high-DOF systems

### Relevance to eVTOL
- Quadrotor position control uses a form of feedback linearization (differential flatness)
- Works well near hover where the model is well-known
- Less reliable in transition where aero uncertainty is high

---

## Sliding Mode Control

**Idea:** design a "sliding surface" and drive the system onto it. Once on the surface, the dynamics are reduced-order and well-behaved.

```
Define sliding surface: s(x) = 0

Design control to reach and stay on surface:
  u = u_eq + u_sw

  u_eq: equivalent control (keeps system on surface)
  u_sw: switching control (drives system to surface)
       u_sw = -k · sign(s)   (bang-bang)
```

### Properties
- **Robust:** once on the surface, dynamics are independent of matched uncertainties
- **Chattering:** the sign() function causes high-frequency switching, which excites structural modes and wears actuators
- Solutions: boundary layer (replace sign with sat), higher-order sliding mode, super-twisting algorithm

### Relevance to eVTOL
- Good for inner-loop attitude control where robustness matters and bandwidth is high
- Chattering is a real concern with electric motors
- Often used in combination with other methods (sliding mode for fast inner loop, MPC for slow outer loop)

---

## Backstepping

**Idea:** design the controller recursively, starting from the innermost loop and working outward. At each step, treat the next state as a "virtual control."

For a cascade system:
```
ẋ₁ = f₁(x₁) + g₁(x₁)·x₂        (x₂ is the "virtual input")
ẋ₂ = f₂(x₁,x₂) + g₂(x₁,x₂)·u  (u is the real input)

Step 1: Design desired x₂ = α₁(x₁) to stabilize the x₁ subsystem.
        Find V₁(x₁) with V̇₁ < 0 when x₂ = α₁(x₁).

Step 2: Define error z₂ = x₂ - α₁(x₁).
        Design u to drive z₂ → 0.
        V₂ = V₁ + ½z₂² → V̇₂ < 0
```

### Properties
- Systematic procedure (doesn't require guessing a Lyapunov function from scratch)
- Provides a constructive Lyapunov function at each step
- Can handle structured uncertainty (adaptive backstepping)
- But: requires the system to be in strict-feedback form

### Relevance to eVTOL
- Natural for cascaded flight control: position → velocity → attitude → angular rate → motor commands
- Each loop "backsteps" through the cascade
- The Lyapunov function from backstepping is a candidate for CBF-type safety analysis

---

## Gain Scheduling

**Idea:** design linear controllers at multiple operating points, then interpolate between them based on current flight condition.

```
Operating points:  hover (V=0), transition (V=30kts), cruise (V=150kts), ...

At each point:
  1. Linearize: ẋ = A(V)x + B(V)u
  2. Design controller: K(V)
  3. In flight: use K(V_current) based on current airspeed

Interpolation: u = -K(V)x where K varies smoothly with V
```

### When it works
- Operating points are well-separated
- System changes slowly relative to control bandwidth
- Linear controllers have sufficient margins at each point

### When it fails
- Rapid transitions (the "scheduling variable" changes fast)
- No formal stability guarantee across the full envelope (unless you verify separately)
- The transitions between operating points can be destabilizing

### For Archer Midnight
Gain scheduling between hover and cruise is the baseline approach. The transition region is where it's most challenging — the dynamics change rapidly as tilt rotors adjust angle.

---

## Adaptive Control

**Idea:** controller parameters adjust online to handle unknown or changing plant dynamics.

### Model Reference Adaptive Control (MRAC)
```
Reference model:  ẋ_m = A_m·x_m + B_m·r     (desired behavior)
Plant:            ẋ = A·x + B·u               (unknown parameters)
Control:          u = θ̂^T·x + k̂·r             (adaptive gains)
Adaptation law:   θ̂̇ = -Γ·x·e^T·P·B           (update gains based on error)
```

The gains θ̂ converge so that the plant tracks the reference model.

### L₁ Adaptive Control
- Faster adaptation than MRAC (decouples adaptation from robustness)
- Uses a low-pass filter on the adaptive signal to ensure robustness
- Growing interest in aerospace applications

### Relevance to eVTOL
- Handles model uncertainty (aero coefficients, motor degradation)
- Can compensate for actuator failures in real time
- But: certification is challenging (how do you verify adaptive behavior?)
- Often combined with a robust baseline controller (adaptive augmentation)

---

## Contraction Theory

**Idea:** instead of analyzing stability of an equilibrium, analyze whether *all trajectories* converge toward each other.

```
A system is contracting if:

  (∂f/∂x) + (∂f/∂x)^T ≤ -2α·I    (Jacobian is uniformly negative definite)

Then any two trajectories converge exponentially with rate α.
```

### Why it's interesting
- Stronger than Lyapunov stability (doesn't need an equilibrium)
- Composes naturally: if subsystems are contracting, the cascade is contracting
- Useful for tracking (not just stabilization)
- Connected to recent work on learning-based control and neural network verification

### Connection to your work
- Contraction metrics can be used to construct CBFs for nonlinear systems
- Active research area in safe learning-based control
- Worth mentioning if Dennis or Peter bring up recent advances

---

## Comparison Table

| Method | Strengths | Weaknesses | Best For |
|--------|-----------|------------|----------|
| Feedback linearization | Exact cancellation, simple result | Needs exact model, fragile | Well-modeled inner loops |
| Sliding mode | Robust to matched uncertainty | Chattering, matched only | Attitude control |
| Backstepping | Systematic, constructive Lyapunov | Strict-feedback form only | Cascaded systems |
| Gain scheduling | Simple, uses linear tools | No global guarantee | Slow parameter variation |
| Adaptive | Handles unknown parameters | Certification hard, transients | Uncertain/degrading systems |
| MPC (nonlinear) | Handles constraints, nonlinear | Computationally heavy | Trajectory planning |
| CBF (your thesis) | Minimal intervention, certifiable | CBF design is hard | Safety layer on top of any controller |

---

## Quick Self-Test

1. **Why not just linearize at every timestep and use LQR?**
   - This is approximately what gain scheduling does. It works if the operating point changes slowly. But there's no global stability guarantee, and at "in-between" points, the linearization may not accurately represent the dynamics.

2. **Feedback linearization requires LgLfh ≠ 0. What if it equals zero?**
   - The system has higher relative degree — you need to differentiate more times before u appears. If u never appears, the output is not controllable through that input.

3. **How does adaptive control interact with a CBF safety filter?**
   - The adaptive controller is the "nominal" controller that the CBF filters. As the adaptive law improves the model, the CBF intervenes less often. But the CBF provides a hard safety guarantee even while the adaptive law is still converging — this is the RTA architecture from your thesis.

4. **For Archer's transition flight, which combination of methods would you propose?**
   - Reasonable answer: gain-scheduled LQR or nonlinear MPC for the nominal controller, with a CBF safety filter for envelope protection. Adaptive augmentation for robustness to aero uncertainty during transition. The CBF ensures safety even if the adaptive law or gain schedule has transient errors.
