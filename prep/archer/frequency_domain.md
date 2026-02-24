# Frequency Domain Analysis of Control Systems

Plane review for Archer onsite (2/26). Focus: intuition, key results, being conversational.

---

## Why Frequency Domain?

Time domain tells you *what* happens. Frequency domain tells you *why* — which frequencies your system amplifies, attenuates, or inverts. For flight control, this is how you ensure your controller doesn't excite structural modes, doesn't lag behind pilot inputs, and has enough margin to handle model uncertainty.

---

## Transfer Functions

A linear time-invariant (LTI) system relates input U(s) to output Y(s):

```
G(s) = Y(s) / U(s) = N(s) / D(s)
```

- **Poles** = roots of D(s) = eigenvalues of state matrix A. Determine stability and natural response.
- **Zeros** = roots of N(s). Determine which inputs the system "ignores."
- **Stability:** all poles must have Re(s) < 0 (left half-plane).

**Example — second-order system:**
```
G(s) = ωn² / (s² + 2ζωn·s + ωn²)

- ωn: natural frequency (how fast it oscillates)
- ζ: damping ratio (how fast oscillations die)
  - ζ = 0: undamped (pure oscillation)
  - 0 < ζ < 1: underdamped (oscillates, decays)
  - ζ = 1: critically damped (fastest no-overshoot)
  - ζ > 1: overdamped (sluggish, no oscillation)

Poles: s = -ζωn ± ωn√(ζ²-1)
```

---

## Bode Plots

Two plots vs. log frequency ω:
1. **Magnitude** |G(jω)| in dB = 20·log₁₀|G(jω)|
2. **Phase** ∠G(jω) in degrees

### How to sketch by hand

Break G(s) into first-order and second-order factors. Each contributes independently (because log turns multiplication into addition).

**First-order pole at s = -a → factor 1/(1 + s/a):**
- Magnitude: 0 dB until ω = a, then -20 dB/decade roll-off
- Phase: 0° at low freq, -45° at ω = a, -90° at high freq

**First-order zero at s = -a → factor (1 + s/a):**
- Opposite: +20 dB/decade, phase goes 0° → +90°

**Integrator 1/s:**
- -20 dB/decade line through 0 dB at ω = 1
- Constant -90° phase

**Second-order pair (complex poles):**
- -40 dB/decade roll-off starting at ω = ωn
- Phase: 0° → -180° (transition centered at ωn)
- Resonance peak near ωn if ζ is small (peak ≈ 1/(2ζ) in magnitude)

### Reading a Bode plot

- **Bandwidth:** frequency where magnitude drops 3 dB below DC. Roughly how fast the closed-loop system responds.
- **Gain crossover frequency (ωgc):** where |G(jω)| = 0 dB. This is where you read phase margin.
- **Phase crossover frequency (ωpc):** where ∠G(jω) = -180°. This is where you read gain margin.

---

## Stability Margins

The open-loop transfer function L(s) = G(s)·C(s) (plant × controller). Closed-loop is T(s) = L(s)/(1 + L(s)).

Closed-loop goes unstable when L(jω) = -1 (magnitude 1, phase -180°). Stability margins measure how far you are from that point.

### Gain Margin (GM)
```
GM = 1 / |L(jωpc)|    where ∠L(jωpc) = -180°

In dB: GM_dB = -20·log₁₀|L(jωpc)|
```
How much you can *increase* the loop gain before the system goes unstable.

**Rule of thumb:** GM > 6 dB (factor of 2 in gain).

### Phase Margin (PM)
```
PM = 180° + ∠L(jωgc)    where |L(jωgc)| = 1 (0 dB)
```
How much additional phase lag the system can tolerate before instability.

**Rule of thumb:** PM > 30-45° for robust design. For flight control, typically want 45°+.

### Why margins matter for eVTOL
- Model uncertainty: aerodynamic coefficients aren't exact, especially in transition flight
- Actuator dynamics: motor response adds phase lag
- Sensor delays: processing latency adds phase lag
- Structural flexibility: bending modes can couple with control loops
- Margins ensure the controller is robust to all of this

---

## Nyquist Plot

Plot L(jω) in the complex plane as ω goes from 0 to ∞ (then mirror for -∞ to 0).

### Nyquist Stability Criterion
```
Z = N + P

Z = # unstable closed-loop poles
N = # clockwise encirclements of the point -1+0j
P = # unstable open-loop poles
```

For stability: Z = 0, so N = -P (counter-clockwise encirclements = number of open-loop RHP poles).

If the open-loop system is stable (P = 0), the Nyquist plot must not encircle -1.

### When to use Nyquist vs. Bode
- Bode: easier to sketch, good for design (shaping loop gain)
- Nyquist: handles open-loop unstable systems and time delays correctly
- Both give the same stability margins; Nyquist is the more general criterion

---

## Root Locus

Traces closed-loop pole locations as a gain parameter K varies from 0 to ∞.

### Key rules
1. Starts at open-loop poles (K=0), ends at open-loop zeros (K→∞)
2. Number of branches = number of poles
3. Real-axis segments: to the left of an odd number of real poles+zeros
4. Asymptotes: (n-m) branches go to infinity at angles (2k+1)·180°/(n-m)
5. Breakaway/break-in points: where branches leave/enter the real axis

### What to read from it
- As you increase gain, where do poles go? Into the RHP (unstable) or deeper into LHP (more damped)?
- Where does the locus cross the jω-axis? That's the maximum gain for stability.
- Dominant poles (closest to jω-axis) determine the transient response.

---

## Loop Shaping — Designing Controllers in Frequency Domain

The idea: shape the open-loop Bode plot L(jω) to get desired closed-loop behavior.

### Design goals
```
Low frequency:  high gain → good tracking, disturbance rejection
Crossover:      -20 dB/dec slope → good phase margin
High frequency: low gain → noise rejection, don't excite structural modes
```

### Common compensators

**Lead compensator** (adds phase, increases bandwidth):
```
C(s) = Kc · (s + z) / (s + p)    where p > z

- Adds positive phase near √(z·p)
- Maximum phase lead: φ_max = arcsin((p-z)/(p+z))
- Use when: need more phase margin
```

**Lag compensator** (increases low-freq gain without affecting crossover):
```
C(s) = Kc · (s + z) / (s + p)    where z > p

- Boosts gain at low frequency
- Use when: need better steady-state tracking
```

**Notch filter** (kills a specific frequency):
```
C(s) = (s² + 2ζ₁ωn·s + ωn²) / (s² + 2ζ₂ωn·s + ωn²)    where ζ₁ < ζ₂

- Use when: need to suppress a structural resonance mode
- Critical for flight control to avoid exciting wing/rotor flex modes
```

---

## Flight Control Application: Pitch Axis Example

A simple short-period approximation for aircraft pitch:

```
Plant: G(s) = Mδ / (s² - Mα·s - Mq·s)    (simplified)

where:
- Mδ: control effectiveness (elevator/rotor authority)
- Mα: static stability derivative (positive = unstable)
- Mq: pitch damping (negative = stabilizing)
```

For the Midnight eVTOL in hover, this is closer to a double integrator (like a quadrotor), and in cruise, it's more like a conventional aircraft. The transition between these is where frequency domain analysis is most important — the plant dynamics are changing, so your controller needs adequate margins across the entire envelope.

---

## Quick Self-Test

1. **Draw a Bode plot for G(s) = 10/(s(s+1)(s+10)).** Where are the break frequencies? What's the high-frequency roll-off slope?
   - Breaks at ω = 1 and ω = 10. Integrator gives -20 dB/dec from the start. After ω=1: -40 dB/dec. After ω=10: -60 dB/dec. Phase starts at -90° (integrator), ends at -270°.

2. **A system has PM = 20°. Is it stable? Is it well-designed?**
   - Stable (PM > 0), but poorly designed. Will have significant overshoot and ringing. Need PM > 45° for flight control.

3. **You add a pure time delay of τ seconds to the loop. What happens to the Bode plot?**
   - Magnitude: unchanged. Phase: subtract ωτ radians (linear decrease with frequency). This eats into phase margin, which is why sensor/actuator latency is dangerous.

4. **What's the relationship between bandwidth and rise time?**
   - Rough rule: t_rise ≈ 1/ω_bw. Higher bandwidth = faster response. But bandwidth is limited by actuator speed, noise, and structural modes.
