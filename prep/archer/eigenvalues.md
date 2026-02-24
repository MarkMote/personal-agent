# Eigenvalues & Eigenvectors for Controls

Plane review for Archer onsite (2/26). Why this matters: eigenvalues are the bridge between linear algebra and system stability/behavior.

---

## The Core Idea

For a matrix A, if Av = λv, then:
- **λ** is an eigenvalue
- **v** is the corresponding eigenvector

The eigenvectors are the directions the matrix "just scales" (no rotation). The eigenvalues are the scale factors.

---

## Why Controls Engineers Care

For a linear system ẋ = Ax, the solution is x(t) = e^(At)·x(0).

If A has eigenvalues λ₁, ..., λn with eigenvectors v₁, ..., vn:

```
x(t) = c₁·e^(λ₁t)·v₁ + c₂·e^(λ₂t)·v₂ + ... + cn·e^(λnt)·vn
```

Each eigenvalue governs how one "mode" of the system evolves:
- **Real λ < 0:** exponential decay (stable mode)
- **Real λ > 0:** exponential growth (unstable mode)
- **Complex λ = σ ± jω:** oscillation at frequency ω, with envelope e^(σt)
  - σ < 0: decaying oscillation (stable)
  - σ > 0: growing oscillation (unstable)
  - σ = 0: sustained oscillation (marginally stable)

**Bottom line:** stability of ẋ = Ax ⟺ all eigenvalues have Re(λ) < 0.

---

## Computing Eigenvalues

### Characteristic equation
```
det(A - λI) = 0
```

For 2×2:
```
A = [a b; c d]

det(A - λI) = λ² - (a+d)λ + (ad-bc) = 0

λ² - tr(A)·λ + det(A) = 0

λ = [tr(A) ± √(tr(A)² - 4·det(A))] / 2
```

**Quick stability check for 2×2:** stable iff tr(A) < 0 AND det(A) > 0.

### For larger matrices
- Don't compute by hand in an interview. Know the concept, use numerical tools in practice.
- Eigenvalues of A = poles of the transfer function G(s) = C(sI-A)⁻¹B + D.

---

## Key Properties

| Property | Consequence |
|----------|------------|
| tr(A) = Σλᵢ | Sum of eigenvalues = trace |
| det(A) = Πλᵢ | Product of eigenvalues = determinant |
| Symmetric A → real λ | Real eigenvalues, orthogonal eigenvectors |
| A and A^T have same λ | Useful for observability/controllability duality |
| Similar matrices (P⁻¹AP) have same λ | Eigenvalues are invariant under coordinate change |

---

## Modal Decomposition

If A is diagonalizable (n linearly independent eigenvectors), let V = [v₁ | v₂ | ... | vn]:

```
A = V·Λ·V⁻¹    where Λ = diag(λ₁, ..., λn)

e^(At) = V·diag(e^(λ₁t), ..., e^(λnt))·V⁻¹
```

This decomposes the system into independent modes. Each mode has:
- Its own time constant (τ = -1/Re(λ))
- Its own oscillation frequency (ω = Im(λ))
- Its own "shape" (the eigenvector v)

### Dominant modes
The modes closest to the jω-axis (smallest |Re(λ)|) dominate the response because they decay slowest. In control design, you mostly care about these.

---

## Connection to Transfer Functions

```
Poles of G(s) = eigenvalues of A
```

But not all eigenvalues appear as poles — if a mode is uncontrollable or unobservable, it doesn't show up in the transfer function. This is the pole-zero cancellation issue, and it's why state-space analysis is more general than transfer functions.

---

## Stability of Discrete-Time Systems

For discrete systems x[k+1] = A·x[k]:

```
Stable ⟺ all |λᵢ| < 1  (inside the unit circle)
```

The mapping from continuous to discrete (zero-order hold):
```
A_d = e^(A·Ts)

If continuous eigenvalue is λ_c, discrete eigenvalue is λ_d = e^(λ_c·Ts)
```

Re(λ_c) < 0 maps to |λ_d| < 1. The left half-plane maps to the interior of the unit circle.

---

## Eigenvalues in Specific Contexts

### Aircraft modes (relevant for Archer)
Longitudinal dynamics have characteristic eigenvalues corresponding to:
- **Short period:** fast, well-damped pitch oscillation (high ωn, high ζ). Usually λ ≈ -3 ± 3j for conventional aircraft.
- **Phugoid:** slow, lightly-damped airspeed/altitude oscillation (low ωn, low ζ). λ ≈ -0.05 ± 0.3j.

For eVTOL in hover, the modes are more like a helicopter — the longitudinal and lateral dynamics are coupled through rotor dynamics.

### Multi-body/structural modes
Flexible structures (rotor blades, wing) have vibration modes. Each mode is an eigenvalue of the structural mass-stiffness system:
```
M·ẍ + K·x = 0  →  eigenvalue problem: K·v = ω²·M·v
```
These structural frequencies must be well-separated from control bandwidth to avoid coupling (the notch filter from frequency domain analysis).

### Controllability and eigenvalue placement
If (A,B) is controllable, you can place all eigenvalues anywhere you want via state feedback u = -Kx. This is pole placement. The eigenvalues of (A - BK) can be chosen to get any desired response.

---

## Matrix Exponential (e^(At))

This is how you solve ẋ = Ax. Three ways to think about it:

**1. Series definition:**
```
e^(At) = I + At + (At)²/2! + (At)³/3! + ...
```

**2. Modal decomposition (diagonalizable case):**
```
e^(At) = V·diag(e^(λᵢt))·V⁻¹
```

**3. Laplace transform:**
```
e^(At) = L⁻¹{(sI - A)⁻¹}
```

For a 2×2 with eigenvalues λ₁, λ₂:
```
e^(At) = (e^(λ₁t)·(A - λ₂I) - e^(λ₂t)·(A - λ₁I)) / (λ₁ - λ₂)
```

---

## Quick Self-Test

1. **A = [0 1; -2 -3]. Find eigenvalues and classify stability.**
   - det(A - λI) = λ² + 3λ + 2 = (λ+1)(λ+2) = 0
   - λ = -1, -2. Both negative real → stable, overdamped.

2. **System has eigenvalues -1 ± 2j. Describe the response.**
   - Decaying oscillation. Time constant τ = 1 sec. Oscillation freq ω = 2 rad/s (≈ 0.32 Hz). Damping ratio ζ = 1/√5 ≈ 0.45.

3. **You design state feedback to place poles at -5 ± 5j. What does this mean physically?**
   - Fast response (ωn = 5√2 ≈ 7 rad/s). Damping ζ = 5/(5√2) ≈ 0.71. Moderate overshoot (~5%). Settles in about 0.8 sec (4/σ).

4. **Why can't transfer functions capture all eigenvalues?**
   - Transfer functions only show controllable AND observable modes. Uncontrollable or unobservable eigenvalues are "hidden" — they still affect internal stability but not the input-output map.
