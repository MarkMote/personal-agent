# Lyapunov Stability

Plane review for Archer onsite (2/26). Foundation for everything in your thesis. The CBF story doesn't land without this.

---

## The Core Idea

You want to prove a system is stable without solving the differential equation. Lyapunov's insight: find an "energy-like" function that always decreases along system trajectories.

If you can find such a function, the system must be converging to equilibrium — energy is draining away.

---

## Definitions

Consider ẋ = f(x), equilibrium at x = 0.

**Stable (Lyapunov):** trajectories that start near 0 stay near 0.
**Asymptotically stable:** stable AND trajectories converge to 0.
**Exponentially stable:** converges at rate e^(-αt) for some α > 0.
**Unstable:** not stable (trajectories can escape).

---

## Lyapunov's Direct Method

Find a function V(x) such that:

### Stability
```
V(0) = 0
V(x) > 0  for x ≠ 0      (positive definite)
V̇(x) ≤ 0                  (negative semi-definite)
```
Then the equilibrium is **stable**.

### Asymptotic stability
```
V(0) = 0
V(x) > 0  for x ≠ 0      (positive definite)
V̇(x) < 0  for x ≠ 0      (negative definite)
```
Then the equilibrium is **asymptotically stable**.

### How to compute V̇
```
V̇ = (∂V/∂x)·ẋ = (∂V/∂x)·f(x) = ∇V · f(x)
```
No need to solve the ODE. Just plug in the dynamics.

---

## For Linear Systems: V(x) = x^T P x

For ẋ = Ax, try V(x) = x^T P x where P is symmetric positive definite.

```
V̇ = x^T(A^T P + PA)x = -x^T Q x
```

So V̇ < 0 iff A^T P + PA = -Q for some Q > 0.

This is the **Lyapunov equation:** given Q > 0, solve for P. If P > 0, the system is stable.

**Key fact:** for a linear system, this is equivalent to checking eigenvalues of A. But for nonlinear systems, Lyapunov functions are the primary tool.

---

## Common Lyapunov Function Candidates

| System Type | V(x) | Why |
|-------------|-------|-----|
| Mechanical | ½mv² + ½kx² (kinetic + potential energy) | Physical energy |
| Linear | x^T P x | Quadratic, works if Lyapunov eq. has solution |
| Robot with PD control | ½ė^T M ė + ½e^T Kp e | Tracking energy |
| Spacecraft attitude | ½ω^T J ω + k(1 - q₀²) | Rotational KE + potential |

---

## The Lyapunov → CBF Parallel

This is the key connection in your thesis. Present them as duals:

| | Lyapunov (Stability) | CBF (Safety) |
|---|---|---|
| Function | V(x) | h(x) |
| Set of interest | {0} (equilibrium) | {x : h(x) ≥ 0} (safe set) |
| Condition | V(x) > 0, V̇(x) < 0 | If h(x) ≥ 0, then ḣ ≥ -α(h) |
| Guarantees | State converges to 0 | State stays in safe set |
| Controller | V̇ < 0 constrains u | ḣ ≥ -α(h) constrains u |

Lyapunov says "you're going toward the goal." CBF says "you're staying away from danger." Both use the same mathematical machinery — a scalar function with a derivative condition.

When you have both:
```
min  ||u - u_nom||²
s.t. ḣ(x,u) ≥ -α(h(x))     ← safety (CBF)
     V̇(x,u) ≤ -γ(V(x))     ← stability (CLF)
```
This is the CLF-CBF-QP. Safety and stability in one optimization. Safety takes priority (if the constraints conflict, you relax the CLF constraint, not the CBF).

---

## LaSalle's Invariance Principle

What if V̇ ≤ 0 (not strictly negative)? You can still prove asymptotic stability using LaSalle:

```
If V̇(x) ≤ 0, and the largest invariant set where V̇ = 0 is just {0},
then the system is asymptotically stable.
```

**Classic example:** pendulum with friction. V = ½ml²θ̇² + mgl(1-cosθ). V̇ = -bθ̇². V̇ = 0 when θ̇ = 0. But if θ̇ = 0 and θ ≠ 0, gravity will cause θ̇ ≠ 0 (not invariant). So the only invariant set is θ = θ̇ = 0. Asymptotically stable.

---

## Exponential Stability and Converse Theorems

**Exponential stability:** there exist α, β, λ > 0 such that ||x(t)|| ≤ β·||x(0)||·e^(-λt).

For quadratic Lyapunov functions:
```
If  α₁||x||² ≤ V(x) ≤ α₂||x||²  and  V̇ ≤ -α₃||x||²

Then exponentially stable with rate λ = α₃/(2α₂)
```

**Converse theorem:** if the system IS asymptotically stable, a Lyapunov function EXISTS. The hard part is finding it. For linear systems, the Lyapunov equation gives it directly. For nonlinear systems, there's no general algorithm — it requires insight.

---

## Region of Attraction

For nonlinear systems, stability may be local. The **region of attraction** is the set of initial conditions from which the system converges to equilibrium.

If V(x) ≤ c is a sublevel set where V̇ < 0 everywhere inside, then that sublevel set is contained in the region of attraction.

**Connection to CBFs:** the safe set {h(x) ≥ 0} is the region you want to stay in. The region of attraction for a CLF is where you're guaranteed to reach the goal. The intersection is where you're both safe and making progress.

---

## Practical Considerations for Flight Control

### Model uncertainty
Lyapunov analysis assumes you know f(x). In practice, you have f̂(x) + Δf(x). Robust Lyapunov analysis accounts for bounded Δf — you need V̇ < 0 for ALL possible Δf in the uncertainty set.

### Gain scheduling
The Midnight eVTOL has very different dynamics in hover vs. cruise. You can design a Lyapunov function for each operating point and show stability for each. The hard part is the transition — you need to show stability across the entire flight envelope, not just at isolated points.

### Multiple Lyapunov functions
For switched systems (like an eVTOL transitioning between flight modes), you can use multiple Lyapunov functions — one per mode — and show that the "total energy" decreases across switches even if individual functions increase temporarily.

---

## Quick Self-Test

1. **V(x) = x₁² + x₂². ẋ₁ = -x₁, ẋ₂ = -x₂³. Is the origin asymptotically stable?**
   - V̇ = 2x₁(-x₁) + 2x₂(-x₂³) = -2x₁² - 2x₂⁴. This is ≤ 0, but = 0 when x₂ = 0 (any x₁... no, also needs x₁ = 0). V̇ = 0 only at origin. So V̇ < 0 for x ≠ 0. Asymptotically stable.

2. **Why is the CLF-CBF-QP important? Why not just use the CBF alone?**
   - CBF alone guarantees safety but doesn't guarantee you make progress toward the goal. You could stay safe but never arrive. The CLF adds a performance guarantee. Together, you get "safe AND making progress." The QP resolves conflicts — safety wins.

3. **You have a Lyapunov function that proves stability for hover, and another for cruise. Does this prove the full system is stable?**
   - No. You haven't shown what happens during transition. The system could go unstable during the switch between modes. You need either a common Lyapunov function (hard to find) or a multiple-Lyapunov argument with dwell-time conditions.

4. **What's the relationship between Lyapunov functions and energy?**
   - For mechanical systems, the Lyapunov function often IS the energy (or a modified energy). But Lyapunov functions are more general — any positive definite function with decreasing derivative works. The energy interpretation gives intuition but isn't required.
