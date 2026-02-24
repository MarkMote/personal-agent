# LQR & Optimal Control

Plane review for Archer onsite (2/26). Optimal control is the foundation for how flight control laws are actually designed in aerospace. LQR is the workhorse.

---

## The LQR Problem

Given a linear system ẋ = Ax + Bu, find the control u(t) that minimizes:

```
J = ∫₀^∞ [x^T Q x + u^T R u] dt

Q ≥ 0: penalizes state deviation (what you want to minimize)
R > 0: penalizes control effort (actuator cost)
```

**Tradeoff:** large Q → aggressive control (tight tracking, big actuator commands). Large R → gentle control (saves actuator effort, slower response).

---

## The Solution

The optimal control law is linear state feedback:

```
u = -Kx    where K = R⁻¹ B^T P
```

P is the unique positive definite solution of the Continuous Algebraic Riccati Equation (CARE):

```
A^T P + PA - PBR⁻¹B^T P + Q = 0
```

**Key properties:**
- The closed-loop system (A - BK) is guaranteed stable (if (A,B) controllable and (A,Q^½) observable)
- The solution always exists and is unique under these conditions
- Guaranteed gain margin of at least 6 dB and phase margin of at least 60° (for SISO) — this is remarkable and is why LQR is so popular
- But these margins apply at the *plant input*, not necessarily at other loop-breaking points

---

## Tuning Q and R

This is the art. Some practical approaches:

### Bryson's rule (starting point)
```
Qᵢᵢ = 1/(max acceptable xᵢ)²
Rⱼⱼ = 1/(max acceptable uⱼ)²
```
Scale each state and input by the maximum you're willing to tolerate.

### Adjusting from there
- Want faster response on state i? Increase Qᵢᵢ
- Actuator saturating? Increase Rⱼⱼ for that input
- Cross-coupling? Add off-diagonal terms to Q (less common)
- Want integral action? Augment the state with ∫e dt and include it in Q

### What the eigenvalues of (A-BK) tell you
After solving, check the closed-loop eigenvalues:
- Too fast → actuators will saturate in practice
- Too slow → tracking is poor
- Poorly damped → adjust Q/R balance

---

## LQR as Pole Placement

LQR can be viewed as a principled way to do pole placement. Instead of manually choosing pole locations (which gets hard for MIMO), you specify *what you care about* (Q, R) and the Riccati equation finds the optimal pole locations.

**Comparison:**
| | Pole Placement | LQR |
|---|---|---|
| You specify | Desired eigenvalues | Q, R weighting matrices |
| Complexity | Easy for SISO, hard for MIMO | Same for any dimension |
| Guarantees | None on robustness | Guaranteed margins (SISO) |
| Intuition | Direct (choose dynamics) | Indirect (choose costs) |

---

## Discrete-Time LQR

For x[k+1] = Ax[k] + Bu[k]:

```
J = Σ [x^T Q x + u^T R u]

u[k] = -Kx[k],    K = (R + B^T PB)⁻¹ B^T PA

Discrete Riccati: P = Q + A^T PA - A^T PB(R + B^T PB)⁻¹ B^T PA
```

In practice, you almost always implement in discrete time (digital controller).

---

## LQG: LQR + Kalman Filter

**The Separation Principle:** for linear systems with Gaussian noise, you can design the controller (LQR) and estimator (Kalman filter) independently, and combining them is optimal.

```
System:  ẋ = Ax + Bu + w,  z = Cx + v
         w ~ N(0,W),  v ~ N(0,V)

Step 1: Design Kalman filter → estimate x̂
Step 2: Design LQR → compute u = -Kx̂
Step 3: Combine → LQG controller
```

**Block diagram:**
```
            ┌─────────────────┐
u ────────► │   Plant + Noise  │ ────► z (measurement)
            └─────────────────┘           │
                  ▲                        │
                  │                        ▼
            ┌─────┴──────────────────────────┐
            │   Kalman Filter → x̂ → K·x̂ = u │
            └────────────────────────────────┘
```

### LQG caveats
- Unlike LQR, LQG does NOT have guaranteed robustness margins
- The Doyle 1978 result: LQG can have arbitrarily small gain margin
- This led to H∞ and μ-synthesis (robust control) — more complex but with guaranteed robustness
- In practice, people often use LQR/LQG as a starting point and verify margins separately

---

## Model Predictive Control (MPC)

MPC is the natural extension of LQR for:
- Nonlinear systems
- Constraints on states and inputs (actuator limits, safety bounds)
- Time-varying references

### Formulation
At each timestep, solve:
```
min  Σ_{k=0}^{N} [x[k]^T Q x[k] + u[k]^T R u[k]] + x[N]^T Qf x[N]
s.t. x[k+1] = f(x[k], u[k])    (dynamics)
     x[k] ∈ X                    (state constraints)
     u[k] ∈ U                    (input constraints — e.g., actuator limits)
     x[0] = x_current            (initial condition)
```

Apply only u[0], then re-solve at the next timestep (receding horizon).

### MPC vs LQR
| | LQR | MPC |
|---|---|---|
| System | Linear | Linear or nonlinear |
| Constraints | None (implicit) | Explicit (states, inputs, safety) |
| Computation | Solve Riccati once (offline) | Solve optimization at each step (online) |
| Horizon | Infinite | Finite (N steps) |
| Guarantees | Stable + optimal | Stable if Qf chosen well + constraints feasible |

### Connection to your work
- MPC with safety constraints is closely related to CBFs
- CBF-QP can be viewed as MPC with N=1 (one-step horizon, safety constraint only)
- Your thesis bridged these: the CBF ensures safety; MPC handles performance over a longer horizon
- For Archer: MPC is likely what they use for trajectory planning; CBF could provide the safety layer underneath

---

## Practical Application: eVTOL Flight Control

### Hover (like a multirotor)
- Near-hover, dynamics are nearly linear
- LQR works well for attitude and position control
- State: [position, velocity, attitude, angular rate] — 12 states
- Inputs: motor speeds / collective + differential thrust — 4-6 inputs
- Q penalizes position/attitude error; R penalizes motor effort

### Cruise (like a fixed-wing)
- Different linearization point
- Aerodynamic forces become dominant
- Gain scheduling: different LQR gains at different airspeeds
- Or: single MPC with a nonlinear model that covers the full envelope

### Transition (the hard part)
- Dynamics are highly nonlinear and rapidly changing
- Switching between hover and cruise control modes
- Gain scheduling with interpolation, or nonlinear MPC
- This is where robust control matters most — model uncertainty is largest during transition

---

## Quick Self-Test

1. **You increase Q₁₁ by 10x. What happens?**
   - The controller becomes 10x more aggressive about state x₁. The corresponding closed-loop eigenvalue moves further into the LHP (faster response for that state). Actuator effort increases.

2. **LQR gives guaranteed margins. Why do people still check margins separately?**
   - The margins are guaranteed at the plant input for SISO. For MIMO, or when there are unmodeled dynamics, sensor noise, or actuator nonlinearities, the guarantees can break. Also, LQG (adding the estimator) destroys the LQR margin guarantees.

3. **Why is MPC computationally expensive compared to LQR?**
   - LQR: solve Riccati once offline, then u = -Kx is a matrix multiply (nanoseconds). MPC: solve a constrained optimization problem at every timestep (milliseconds to seconds depending on horizon and model complexity). For eVTOL at 100-200 Hz control rate, this matters.

4. **The separation principle says design controller and estimator independently. When does this break?**
   - When the system is nonlinear (EKF + nonlinear controller don't separate). When there are constraints (MPC + estimator interact through feasibility). When there's model uncertainty (robust control needs to consider estimation error jointly with control error).
