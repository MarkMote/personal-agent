# State Space Methods

Plane review for Archer onsite (2/26). This ties together eigenvalues, controllability, observability, and connects to everything else.

---

## The State Space Representation

```
ẋ = Ax + Bu     (state equation)
y = Cx + Du     (output equation)

x ∈ ℝⁿ: state vector (minimum set of variables that fully describe the system)
u ∈ ℝᵐ: input vector (what you can control)
y ∈ ℝᵖ: output vector (what you can measure)
```

**vs. transfer functions:**
- Transfer functions: SISO input-output map, loses internal information
- State space: captures full internal dynamics, handles MIMO naturally
- Equivalent for LTI systems: G(s) = C(sI-A)⁻¹B + D

---

## Controllability

**Can you drive the system from any state to any other state using the inputs?**

```
Controllability matrix: C = [B | AB | A²B | ... | A^(n-1)B]

Controllable ⟺ rank(C) = n
```

### What it means
- If controllable: full state feedback u = -Kx can place all eigenvalues anywhere
- If not controllable: some modes are "unreachable" — no input can affect them
- Uncontrollable modes have fixed eigenvalues that can't be moved by feedback

### Physical intuition
A mode is uncontrollable if the input B doesn't "excite" it. Example: if you can only apply force in the x-direction, you can't control motion in the y-direction (assuming no coupling).

### For flight control
- Actuator placement determines controllability
- eVTOL with 12 rotors has high controllability (many inputs, redundancy)
- Actuator failure reduces rank of B → can lose controllability of certain modes
- This is why redundancy matters: even with a motor out, the system should remain controllable

---

## Observability

**Can you determine the full state from the measurements alone?**

```
Observability matrix: O = [C; CA; CA²; ...; CA^(n-1)]

Observable ⟺ rank(O) = n
```

### What it means
- If observable: a Kalman filter can estimate the full state from measurements
- If not observable: some states are "hidden" — no measurement reveals them
- Unobservable modes: the estimator can't determine these states regardless of how good the sensors are

### Physical intuition
A mode is unobservable if it doesn't affect any measurement. Example: if you only measure position, and there's an internal state (like a hidden spring) that doesn't affect position, it's unobservable.

### For state estimation
- Sensor selection determines observability
- IMU alone: can observe attitude rate but position drifts (double integration of noise)
- IMU + GPS: position becomes observable
- IMU + camera: visual features make position observable (VIO)
- Sensor failure degrades observability — estimator uncertainty grows for unobservable states

---

## Duality

Controllability and observability are dual:

```
(A, B) controllable  ⟺  (A^T, B^T) observable
(A, C) observable    ⟺  (A^T, C^T) controllable
```

This is why the LQR (control) and Kalman filter (estimation) Riccati equations have the same structure.

| Control (LQR) | Estimation (Kalman) |
|---------------|-------------------|
| A, B | A^T, C^T |
| Q (state cost) | Q (process noise) |
| R (input cost) | R (measurement noise) |
| K = R⁻¹B^TP | K = PC^TR⁻¹ |

---

## Canonical Forms

### Controllable canonical form
```
A = [0   1   0 ... 0  ]     B = [0]
    [0   0   1 ... 0  ]         [0]
    [... ... ... ... ...]         [.]
    [-a₀ -a₁ -a₂ ... -aₙ₋₁]    [1]
```
Last row contains negative coefficients of the characteristic polynomial. Input enters only the last state. This form makes controllability obvious — rank(C) = n always.

### Observable canonical form
Transpose of controllable canonical form (duality). The output reads from the last state. This makes observability obvious.

### Jordan/diagonal form
```
A = diag(λ₁, λ₂, ..., λₙ)
```
Each state is an independent mode. Easy to read stability, time constants, frequencies. Only possible if eigenvectors are linearly independent.

---

## Coordinate Transformations

Any invertible transformation x̄ = Tx gives an equivalent representation:

```
Ā = TAT⁻¹,  B̄ = TB,  C̄ = CT⁻¹,  D̄ = D
```

**Key invariants (don't change with coordinates):**
- Eigenvalues of A
- Transfer function G(s)
- Controllability (rank of controllability matrix)
- Observability (rank of observability matrix)

**What changes:**
- The specific form of A, B, C
- Physical interpretation of states (unless you pick meaningful coordinates)

---

## Kalman Decomposition

Any LTI system can be decomposed into four subsystems:

```
         ┌─────────────────────────────┐
         │  Controllable & Observable  │ ← appears in transfer function
         │  Controllable & Unobserv.   │ ← affects state but not output
         │  Uncontr. & Observable      │ ← visible but can't influence
         │  Uncontr. & Unobservable    │ ← hidden, can't affect/see
         └─────────────────────────────┘
```

Only the "controllable AND observable" part appears in the transfer function G(s). The rest is hidden from the input-output perspective but still affects internal stability.

**Why this matters:** if you design a controller using only the transfer function, you might miss unstable hidden modes. State-space analysis catches everything.

---

## Pole Placement via State Feedback

If (A, B) is controllable, u = -Kx places eigenvalues of (A - BK) at any desired locations.

### Ackermann's formula (SISO, n states)
```
K = [0 0 ... 0 1] · C⁻¹ · φ(A)

where φ(s) = (s-p₁)(s-p₂)...(s-pₙ) is the desired characteristic polynomial
and C is the controllability matrix
```

### For MIMO systems
Use LQR instead — direct pole placement for MIMO is underdetermined (more degrees of freedom than equations) and doesn't give robustness guarantees.

---

## Observer Design

If (A, C) is observable, you can build a state observer (Luenberger observer):

```
x̂̇ = Ax̂ + Bu + L(y - Cx̂)

L is the observer gain. Eigenvalues of (A - LC) determine how fast the estimate converges.
```

**Design rule:** observer poles should be 2-5x faster than controller poles so the estimate converges before the controller needs it.

The Kalman filter is the optimal observer when the noise is Gaussian. The Luenberger observer is the deterministic version.

---

## MIMO Systems

For multi-input multi-output systems, state space is the natural framework.

**Transfer function matrix:**
```
G(s) = C(sI-A)⁻¹B + D    ← p×m matrix of transfer functions
```

**MIMO challenges:**
- Coupling: inputs affect multiple outputs
- Direction-dependent gain: the system may amplify some input directions and attenuate others
- Singular values of G(jω) replace the scalar magnitude plot — the largest singular value is the maximum gain in any direction

### Singular Value Bode Plot
```
σ̄(G(jω)): maximum gain (worst-case amplification)
σ_(G(jω)): minimum gain (best-case amplification)
```
For robust control, you care about σ̄ (maximum sensitivity to disturbances) and σ_ of the loop transfer (minimum loop gain for tracking).

---

## Quick Self-Test

1. **System has 4 states, 2 inputs. Controllability matrix is 4×8. What rank do you need?**
   - Rank 4 (= n, the number of states) for full controllability.

2. **You lose one sensor (C loses a row). What's the first thing to check?**
   - Re-check observability with the reduced C. If rank(O) < n, some states are no longer observable and the estimator will degrade for those states.

3. **A 6-DOF aircraft has 12 states (position, velocity, attitude, angular rate). An eVTOL has 12 motors. Is it controllable?**
   - Almost certainly yes — 12 inputs for 12 states is generous. Even with motor failures, there's likely enough redundancy. But it depends on the geometry — if all motors are identical and symmetric, certain modes might require differential thrust that symmetric failures could eliminate.

4. **Why use state space instead of transfer functions for Archer's flight control system?**
   - MIMO (multiple rotors, multiple axes), internal stability matters (hidden modes), need for state estimation (Kalman filter operates in state space), natural framework for LQR/MPC design, handles nonlinear extensions (EKF, nonlinear MPC).
