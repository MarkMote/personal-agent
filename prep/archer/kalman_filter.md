# Kalman Filter

Plane review for Archer onsite (2/26). Dheepak (VIO/SLAM background) will likely probe this area. State estimation feeds into the safety filter — uncertainty in state means uncertainty in safety guarantees.

---

## What It Is

The Kalman filter is the optimal state estimator for linear systems with Gaussian noise. It fuses noisy measurements with a dynamic model to produce the best (minimum variance) estimate of the true state.

```
System:   x[k+1] = A·x[k] + B·u[k] + w[k]     w ~ N(0, Q)
Measure:  z[k]   = H·x[k] + v[k]               v ~ N(0, R)

Q = process noise covariance (how uncertain the model is)
R = measurement noise covariance (how noisy the sensors are)
```

---

## The Two Steps

### Predict (Time Update)
Propagate the state and covariance forward using the model:
```
x̂⁻[k] = A·x̂[k-1] + B·u[k-1]        (state prediction)
P⁻[k]  = A·P[k-1]·A^T + Q            (covariance prediction)
```
The covariance grows — we become less certain because the model isn't perfect.

### Update (Measurement Update)
Incorporate the new measurement:
```
K[k]   = P⁻[k]·H^T · (H·P⁻[k]·H^T + R)⁻¹    (Kalman gain)
x̂[k]  = x̂⁻[k] + K[k]·(z[k] - H·x̂⁻[k])      (state update)
P[k]   = (I - K[k]·H)·P⁻[k]                    (covariance update)
```

**Innovation:** ỹ = z[k] - H·x̂⁻[k] is the difference between what we measured and what we predicted. The Kalman gain decides how much to trust this innovation.

---

## Intuition for the Kalman Gain

```
K = P⁻·H^T / (H·P⁻·H^T + R)
```

- If **R is small** (sensors are precise): K is large → trust the measurement
- If **R is large** (sensors are noisy): K is small → trust the model prediction
- If **P⁻ is large** (prediction is uncertain): K is large → lean on the measurement
- If **P⁻ is small** (prediction is confident): K is small → lean on the model

The Kalman filter optimally balances model vs. measurement at every timestep.

---

## Steady-State Kalman Filter

If A, Q, R, H are constant, P[k] converges to a steady-state P∞ and the Kalman gain becomes constant K∞. You can pre-compute this by solving the Discrete Algebraic Riccati Equation (DARE):

```
P = A·P·A^T + Q - A·P·H^T·(H·P·H^T + R)⁻¹·H·P·A^T
```

This is the dual of the LQR Riccati equation (estimation and control are duals).

---

## Extended Kalman Filter (EKF)

For nonlinear systems:
```
x[k+1] = f(x[k], u[k]) + w[k]
z[k]   = h(x[k]) + v[k]
```

Linearize at the current estimate at each step:
```
F[k] = ∂f/∂x |_{x̂[k]}     (Jacobian of dynamics)
H[k] = ∂h/∂x |_{x̂⁻[k]}    (Jacobian of measurement)
```

Then run the standard Kalman equations using F and H instead of A and H.

**Predict:**
```
x̂⁻[k] = f(x̂[k-1], u[k-1])          (propagate through nonlinear model)
P⁻[k]  = F[k-1]·P[k-1]·F[k-1]^T + Q  (covariance via linearization)
```

**Update:**
```
K[k]  = P⁻·H[k]^T · (H[k]·P⁻·H[k]^T + R)⁻¹
x̂[k] = x̂⁻[k] + K[k]·(z[k] - h(x̂⁻[k]))
P[k]  = (I - K[k]·H[k])·P⁻[k]
```

### EKF limitations
- Linearization can be poor if the system is highly nonlinear
- Can diverge if the initial estimate is far from truth
- The covariance P is only approximate (not truly optimal)
- Widely used in practice despite these limitations (it works well enough for most systems)

---

## Unscented Kalman Filter (UKF)

Alternative to EKF that avoids computing Jacobians. Instead of linearizing, it passes carefully chosen "sigma points" through the nonlinear functions:

```
1. Choose 2n+1 sigma points around the current estimate
2. Propagate each through f() and h()
3. Compute predicted mean and covariance from the propagated points
```

**Advantages over EKF:**
- No Jacobian computation needed
- Better approximation of nonlinear transformations (captures up to second-order statistics)
- More robust for highly nonlinear systems

**Disadvantage:** Slightly more computationally expensive (2n+1 function evaluations per step).

---

## Sensor Fusion for eVTOL (Archer Application)

A typical eVTOL state estimation system fuses multiple sensors:

| Sensor | Measures | Rate | Characteristics |
|--------|----------|------|----------------|
| IMU (accel + gyro) | Specific force, angular rate | 200-1000 Hz | High rate, drifts over time |
| GPS | Position, velocity | 1-10 Hz | Absolute, can drop out |
| Barometer | Altitude | 10-50 Hz | Absolute, affected by weather |
| Magnetometer | Heading | 50-100 Hz | Affected by magnetic interference |
| Airspeed sensor | Forward velocity | 10-50 Hz | Only useful in cruise |
| Camera/LiDAR | Relative position, features | 10-30 Hz | Rich, computationally expensive |

### IMU-centric architecture
The standard approach:
1. **IMU provides the prediction step** at high rate (propagate position, velocity, attitude using accelerometer and gyroscope)
2. **Other sensors provide update steps** at their respective rates (correct the IMU drift)

This is sometimes called a "loosely-coupled" architecture. The EKF state vector typically includes:
```
x = [position(3), velocity(3), attitude(4 quaternion), accel_bias(3), gyro_bias(3)]
    = 16 states
```

The accelerometer and gyroscope biases are estimated online — they drift slowly and the other sensors allow the filter to track them.

### GPS-denied navigation
When GPS drops out (urban canyons, jamming, indoor):
- IMU drifts (especially position — double integration of noisy acceleration)
- Visual odometry / VIO can substitute (camera + IMU)
- LiDAR SLAM provides position updates
- Barometer still gives altitude
- Key question: how long can you navigate without GPS? Depends on IMU quality and availability of visual/LiDAR features.

This is Dheepak's area (VIO/SLAM). Be ready to discuss tradeoffs between filter-based (EKF) and optimization-based (factor graph/GTSAM) approaches to sensor fusion.

---

## Factor Graphs vs. EKF

Modern SLAM and VIO systems increasingly use factor graph optimization instead of EKF:

| | EKF | Factor Graph |
|---|---|---|
| Approach | Sequential, one estimate | Batch optimization over a window |
| Consistency | Can become inconsistent (linearization errors accumulate) | Better consistency (can re-linearize) |
| Computation | O(n²) per update (n = state dim) | O(n) per step with incremental solvers (iSAM2) |
| Loop closure | Difficult | Natural (just add a factor) |
| Implementation | Simple | More complex (need GTSAM, g2o, etc.) |

For flight control state estimation, EKF is still standard (real-time, well-understood, good enough). For mapping and localization with cameras/LiDAR, factor graphs are increasingly preferred.

---

## Observability

A system is observable if you can determine the full state from the measurements. For (A, H):

```
Observable ⟺ rank([H; H·A; H·A²; ...; H·A^(n-1)]) = n
```

**Why it matters for Kalman filter:**
- Unobservable modes: the filter can't estimate those states — their covariance stays large or grows
- Example: a single GPS gives position but not attitude. You need the IMU + GPS combination to observe the full state.
- Sensor placement and selection is partly an observability problem

---

## Connection to Safety Filters

This is the bridge between Dheepak's area and your thesis work:

1. The safety filter (CBF) assumes you know the state x
2. In reality, you have an estimate x̂ with covariance P
3. The safety guarantee h(x) ≥ 0 must account for estimation uncertainty
4. Robust CBF: enforce h(x̂) ≥ margin, where margin depends on P
5. If estimation degrades (GPS lost, sensors fail), the safety margin must grow — the system becomes more conservative

This is an active research area and a real engineering challenge. Worth mentioning if the conversation goes there — it shows you understand how the pieces fit together.

---

## Quick Self-Test

1. **What happens to the Kalman gain if you set R = 0 (perfect measurements)?**
   - K = I (after appropriate dimensions). The filter completely trusts the measurement. x̂ = z/H. The model is ignored.

2. **You have an IMU at 200 Hz and GPS at 1 Hz. Describe the filter operation.**
   - 200 predict steps per second using IMU (high rate, captures fast dynamics). Every 200th step, also do a GPS measurement update that corrects accumulated drift. Between GPS fixes, position estimate drifts; GPS update snaps it back.

3. **Your EKF is diverging. What do you check?**
   - Initial P too small (filter is overconfident in initial estimate). Q too small (model is overconfident — can't track real dynamics). Linearization is poor (system is too nonlinear for EKF — try UKF). Numerical issues (Joseph form for covariance update, or enforce symmetry).

4. **Why estimate IMU biases in the state vector?**
   - Accelerometer and gyro biases drift slowly (temperature, aging). If you don't estimate them, the drift contaminates position/velocity estimates. By including them in the state and observing them through GPS/other sensors, you can track and remove the bias in real time.
