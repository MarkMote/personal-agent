# Robotics Refresher / Prep

For Viam and any robotics-focused roles.

**Status:** Viam interview with Ian Whalen (VP Product) was Feb 17. Waiting on outcome. If advancing, next round will likely be technical.

---

## Priority 1: Robotics Platform Concepts (Viam-specific)

Know these well enough to have a technical conversation, not just recite definitions.

### What Viam Is
- Robotics software development platform — abstracts hardware integration
- Like ROS but cloud-native, with a registry of pre-built components
- Key value prop: make robotics about algorithms, not plumbing
- gRPC + WebRTC + protobuf for robot communication
- Component model: sensors, actuators, services, modules
- Cloud dashboard for fleet management, data capture, ML model deployment

### Viam vs ROS
| | Viam | ROS |
|---|---|---|
| Architecture | Cloud-native, gRPC | Pub-sub, DDS (ROS2) |
| Setup | Config file, no code to start | Launch files, packages, catkin/colcon |
| Language | Go backend, multi-SDK | C++/Python primary |
| Hardware | Registry of drivers, plug-and-play | Manual driver integration |
| Fleet | Built-in cloud management | No built-in fleet management |
| Best for | Product deployment, fleet ops | Research, custom systems |

### Technical Scenarios (from Viam prep)
Be ready to talk through:
- "A robot fails to upload telemetry in low-bandwidth. How do you design a caching/partial-upload system?"
- "Design a fleet management system that pushes config updates to 1,000 robots without bricking them."
- "A customer wants to integrate a legacy sensor Viam doesn't support. Walk through building a custom component."
- "How do you handle a race condition between a sensor reading and an actuator command?"

---

## Priority 2: Core Robotics Fundamentals

### Control Basics
```
PID Controller:
u(t) = Kp * e(t) + Ki * ∫e(t)dt + Kd * de/dt

- Kp: proportional — reacts to current error
- Ki: integral — eliminates steady-state error
- Kd: derivative — dampens oscillation

Tuning: start with P only, add D to reduce overshoot, add I to kill steady-state error
```

**State space representation:**
```
ẋ = Ax + Bu
y = Cx + Du

- x: state vector
- u: input vector
- A: system dynamics
- B: input mapping
- C: output mapping
```

### State Estimation
- **Kalman Filter:** optimal estimator for linear systems with Gaussian noise
  - Predict step: propagate state forward
  - Update step: incorporate measurement
  - Key insight: balances model prediction vs measurement based on their uncertainties
- **Extended Kalman Filter (EKF):** linearize nonlinear systems at each step
- **Particle Filter:** for highly nonlinear/non-Gaussian — sample-based

### Sensor Fusion
- Combine IMU (high rate, drifts) + GPS (low rate, absolute) + camera (visual)
- IMU provides prediction, GPS/camera provides correction
- Handle sensor failure: detect outliers, switch to degraded mode

### Path Planning
- **A\*:** optimal graph search with heuristic
- **RRT (Rapidly-exploring Random Trees):** probabilistic, good for high-dimensional spaces
- **Potential fields:** simple, can get stuck in local minima
- **MPC (Model Predictive Control):** optimize trajectory over rolling horizon

---

## Priority 3: Software / Systems for Robotics

### Linux Fundamentals
- Process management: `ps`, `top`, `kill`, `systemd`
- Networking: `ssh`, `scp`, `netstat`, ports, firewalls
- File permissions, users, groups
- Package management: `apt`, `pip`, `conda`
- Debugging: `dmesg`, `journalctl`, `strace`

### Networking for Robots
- TCP vs UDP: reliability vs latency tradeoff
- WebRTC: peer-to-peer, low latency, used by Viam for remote control
- gRPC: structured RPC, protobuf serialization, used by Viam for component communication
- MQTT: lightweight pub-sub, common in IoT
- Latency matters: 10ms for control loops, 100ms for telemetry, 1s for config updates

### API Design for Hardware
- Synchronous vs asynchronous: sensor reads are often async
- Timeout handling: hardware can hang
- Retry with backoff: transient failures are common
- Idempotent operations: robot shouldn't move twice if command is retried

---

## Priority 4: Your Robotics Stories (have these ready)

### Robotarium
- Founding member of open-access multi-agent robotics lab at Georgia Tech
- Built safety layer (CBFs) that let remote users run untrusted code on real robots
- 16,000+ experiments, still running today
- Key insight: "move fast and not break things" — decouple performance from safety

### Pytheia
- Camera-based robotic perception as a service
- Computer vision for industrial inspection
- Dealt with real hardware deployment challenges (lighting, calibration, edge cases)

### PhD Research
- Spacecraft GNC: docking, formation flying, swarm navigation
- Worked with real hardware at Stanford (free-flyer testbed), JPL, AFRL
- Simulation: Monte Carlo, hardware-in-the-loop

### Roostr (relevant for robotics platform thinking)
- Built entire production stack as sole engineer
- Agentic systems that interact with external APIs (analogous to robot-to-service communication)
- Data pipeline design, reliability, error handling at scale

---

## Practice Questions

1. "Explain how you'd design a safety system for an autonomous mobile robot operating in a warehouse with humans."
2. "A fleet of 50 delivery robots is experiencing intermittent GPS dropouts in urban canyons. How do you maintain navigation?"
3. "Walk me through how you'd debug a robot that's consistently overshooting its target position by 5cm."
4. "How would you design a data pipeline that captures sensor data from 100 robots, stores it, and makes it available for ML training?"
5. "What's the difference between hard real-time and soft real-time, and which do you need for a robot arm vs a mobile robot?"
