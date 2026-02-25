# Fauna Robotics -- Technical Review for Josh Merel Conversation

**Prepared:** 2026-02-24
**Purpose:** Deep technical reference for CTO conversation. Know enough to ask good questions, identify genuine overlaps with Mark's background, and have credible opinions.

---

## 1. Learned Locomotion Policies for Humanoid Robots

### The Standard Pipeline (Isaac Gym / PPO)

The dominant approach for humanoid locomotion in 2025-2026 follows this pipeline:

1. **Simulation**: Run thousands of parallel environments on GPU using NVIDIA Isaac Gym (now Isaac Lab). A single A100 can simulate 4,096 humanoid agents simultaneously.

2. **Training**: Use PPO (Proximal Policy Optimization) to train a neural network policy. The policy maps proprioceptive observations (joint angles, joint velocities, IMU data, gravity vector in body frame) plus a command vector (desired velocity, heading, height) to joint-level actions (typically PD position targets or torques).

3. **Reward shaping**: The reward function is the secret sauce. Typical terms include:
   - Tracking reward (match commanded velocity/heading)
   - Alive bonus (don't fall)
   - Energy penalty (minimize torque usage)
   - Smoothness penalties (minimize jerk, action rate changes)
   - Foot clearance / contact schedule rewards (encourage proper gait)
   - Orientation penalties (keep torso upright)

4. **Domain randomization**: During training, randomize physics parameters (friction, mass, motor strength, latency, terrain) so the policy learns to be robust. This is the primary mechanism for sim-to-real transfer.

5. **Teacher-student distillation**: A critical technique. First train a "teacher" policy with access to privileged information (exact ground truth terrain heights, exact friction coefficients, exact body parameters). Then train a "student" policy that only sees what the real robot sees (proprioception, IMU) to imitate the teacher. The student implicitly learns to infer the hidden state from observation history. This is how most companies handle the sim-to-real gap without explicit system identification.

6. **Deployment**: The student policy runs on the real robot at 50-200 Hz. Typically a small MLP (2-3 hidden layers, 256-512 units). Low compute cost.

**Key results**: Agility Robotics (Digit), Unitree (H1/G1), and several academic groups have demonstrated zero-shot sim-to-real transfer of walking policies trained entirely in Isaac Gym with PPO. Humanoid-Gym (RobotEra) verified this on 1.2m and 1.65m humanoids.

**Key papers**:
- Makoviychuk et al., "Isaac Gym" (2021) -- GPU-parallel RL training
- Radosavovic et al., "Real-World Humanoid Locomotion with RL" (Science Robotics, 2024) -- Berkeley group, Digit robot
- RobotEra, "Humanoid-Gym" (2024) -- open-source framework for humanoid locomotion

### Merel's Approach: Hierarchical Motor Primitives

Josh Merel's research lineage takes a fundamentally different philosophical approach from the standard Isaac Gym pipeline. The key differences:

**Standard pipeline**: Train a single monolithic policy end-to-end for each task. The policy is a flat mapping from observations to actions. Simple, scales well with GPU compute, but each policy is specialized and behaviors can be unnatural.

**Merel's approach**: Learn a structured, reusable motor control module that captures the *space* of natural movements, then compose higher-level behaviors on top of it. Key ideas:

1. **Motor primitive embedding space**: Instead of training one policy per task, learn a latent space that encodes diverse motor behaviors. A higher-level controller selects points in this latent space to produce movement. This is the "Neural Probabilistic Motor Primitives" idea (ICLR 2019).

2. **Hierarchical decomposition**: Factor control into low-level motor execution (proprioception-driven, handles dynamics and balance) and high-level task coordination (vision-driven, handles goals and sequencing). The low-level module is trained once and reused across tasks.

3. **Naturalistic movement**: By training on motion capture data or biomechanically informed objectives, the movements look more natural than pure reward-optimized policies. This matters enormously for a social robot like Sprout.

4. **Neuroscience grounding**: Merel's work explicitly draws from how biological motor systems work -- motor cortex as a dynamical system generating movement, basal ganglia for action selection, cerebellum for online correction. The virtual rodent paper (Nature 2024) validated this: the virtual agent's neural network activity predicts real rat brain activity better than movement features alone.

**Why this matters for Fauna**: Sprout needs to look natural, be expressive, and handle diverse behaviors (walking, kneeling, crawling, dancing, carrying objects). A flat PPO policy per behavior would be brittle at transitions and look robotic. Merel's hierarchical approach naturally handles mode switching, produces more natural movement, and allows the same motor module to be reused across tasks.

**Connection to Mark's background**: Mark's PhD work on optimization-based control, CBFs for safety, and safe RL connects well here. The compliance and safety aspects of motor control are areas where classical controls expertise (Lyapunov stability, constraint satisfaction) complements learned policies. Mark can credibly discuss the tension between learned and classical approaches, and where safety guarantees fit into a learned locomotion stack.

---

## 2. MuJoCo vs Isaac Sim

### The Two Ecosystems

| Dimension | MuJoCo | Isaac Gym / Isaac Lab |
|-----------|--------|----------------------|
| **Developer** | Google DeepMind (open-sourced 2022) | NVIDIA |
| **Physics** | Generalized coordinates, implicit Euler integration, soft contacts | Maximal coordinates, GPU-native rigid body + articulation |
| **Speed (single env)** | Very fast on CPU (~20x faster than Isaac Sim for single instance) | Slower per-instance but designed for massive parallelism |
| **GPU parallelism** | MJX (JAX-based): 70-150x speedup on RTX 4090 for locomotion | Native GPU parallelism: 4096+ envs on single GPU |
| **Contact modeling** | Convex contact model, excellent for articulated robots | PhysX-based, good for large-scale contact-rich scenarios |
| **Accuracy** | Considered most accurate for robotic dynamics in benchmarks | Good but less precise for detailed articulated dynamics |
| **Ecosystem** | dm_control, Gymnasium, MuJoCo Playground (2025) | IsaacGymEnvs, IsaacLab, Omniverse |
| **Rendering** | Basic OpenGL; ray-tracing via external tools | Built-in Omniverse ray-tracing (photorealistic) |
| **Cost** | Free (Apache 2.0 since 2022) | Free for research; commercial licensing varies |
| **Community** | Dominant in academic research | Dominant in industry/commercial robotics |

### Why Fauna Likely Uses Both

The ArXiv paper reveals Fauna trains policies in **IsaacSim with IsaacLab**, not MuJoCo. This is notable given Merel's DeepMind background and the dm_control ecosystem. Likely reasons:

1. **GPU parallelism for RL**: Training locomotion policies requires billions of timesteps. Isaac Lab's native GPU parallelism is mature and well-supported for this.

2. **Actuator modeling**: Isaac Sim provides good support for modeling DC motor dynamics with delay, saturation, and power constraints -- which Fauna's paper explicitly describes.

3. **MuJoCo for validation**: The Booster Gym framework (2025) demonstrates a common pattern: train in Isaac Gym, validate in MuJoCo as a sim-to-sim sanity check before deploying to real hardware.

4. **MuJoCo Playground (Jan 2025)**: DeepMind released MuJoCo Playground, a GPU-accelerated suite built on MJX that trains locomotion policies in under 10 minutes on a single GPU. This closes the GPU gap. Fauna may use this going forward.

**Key insight for conversation**: Asking about their simulation strategy (single vs. multi-engine validation, how they handle the sim-to-real gap, whether they use MuJoCo for anything) is a natural technical question that shows depth.

---

## 3. Compliance and Safety in Humanoid Robots

### Three Approaches to Compliance

**1. Series Elastic Actuators (SEA)**
- **Mechanism**: A spring element placed in series between the motor/gearbox and the output joint. The spring deflection is measured to estimate and control force.
- **History**: Introduced by Pratt and Williamson (1995) at MIT. Used in Boston Dynamics Atlas (earlier versions), NASA Valkyrie, IHMC robots.
- **Pros**: Inherent shock absorption. Enables accurate force control. Energy storage (spring can store and release energy). Decouples motor inertia from output.
- **Cons**: Reduced bandwidth (the spring limits how fast you can change force). Added mechanical complexity and weight. The compliance bandwidth is limited by the spring stiffness -- stiffer spring = better bandwidth but less compliance.
- **Status**: Well-proven but falling out of favor for legged robots due to bandwidth limitations.

**2. Quasi-Direct Drive (QDD)**
- **Mechanism**: High-torque-density BLDC motor with very low gear ratio (typically 6:1 to 10:1, vs. 100:1+ for traditional actuators). The low gear ratio makes the actuator naturally backdrivable.
- **History**: Popularized by MIT Cheetah (Sangbae Kim's lab). Used in Mini Cheetah (2019), and now widely adopted.
- **Pros**: Excellent backdrivability (the joint moves freely when pushed). High bandwidth (fast force response). Simple mechanism (fewer parts to break). Transparent force control via motor current sensing -- the motor current directly reflects output torque.
- **Cons**: Lower gear ratio means you need bigger, heavier motors for the same output torque. Power-hungry at high loads (no mechanical advantage). Thermal management is critical.
- **Status**: Dominant approach for modern legged robots that need agility and contact-rich interaction.

**3. Software Compliance (What Fauna Does)**
- **Mechanism**: Use conventional actuators (motors + gearboxes) but implement compliance in the control software. PD controllers with low gains, torque limits enforced in software, current limiting at the motor driver level.
- **How Fauna does it**: The ArXiv paper describes "PD control, current limiting, and power constraints" applied to the output of the learned policy. The policy itself is trained in environments with disturbances, so it learns compliant behavior. Conservative torque limits are enforced regardless of what the policy commands.
- **Pros**: No special hardware needed. Can tune compliance characteristics in software. Works with cheaper, lighter actuators. The learned policy can be inherently compliant rather than relying on mechanical compliance.
- **Cons**: Relies on software working correctly (failure mode: if the controller crashes, the robot is no longer compliant). Latency in the control loop limits effective compliance bandwidth. No passive energy storage.
- **Why Fauna chose this**: At 22.7 kg and 1.07 m, Sprout's kinetic energy is inherently low. A 50 lb child-sized robot with software torque limits simply cannot generate dangerous forces. The physics is on their side -- even a worst-case collision is bounded by mass * velocity, and both are small. This lets them avoid the weight and cost of SEAs or QDD.

### Safety Standards

**ISO 13482:2014 (Personal Care Robots)**
- Covers mobile servant robots, physical assistant robots, and person carrier robots
- Defines hazard analysis methodology, protective measures, safety requirements
- Applies to robots operating in close contact with the general public
- Currently under revision as ISO/FDIS 13482 (2024)
- This is the relevant standard for Sprout (personal care / service robot category)

**ISO 10218-1:2025 (Industrial Robots)**
- Updated in 2025, covers industrial robot safety
- Less relevant for Fauna but defines collaborative robot (cobot) safety principles

**UL 3300 (Service Robots)**
- US standard for safety of service robots
- Often pursued for commercial deployments in public spaces

**Key insight for conversation**: Mark can connect his CBF (Control Barrier Function) work to the safety challenge. CBFs provide formal guarantees that safety constraints are never violated -- a stronger claim than "we trained the policy to be safe." Asking whether Fauna uses any formal safety verification on top of their learned policies is a great question.

---

## 4. Sim-to-Real Transfer for Locomotion

### The Core Problem

Simulation is never perfect. Every discrepancy between sim and real is a potential failure mode. The policy learns to exploit the simulator's quirks, not the real world's physics.

### Main Failure Modes

**1. Actuator Dynamics Mismatch (Most Common, Most Dangerous)**
- Simulated motors respond instantly; real motors have latency, bandwidth limits, thermal effects, and nonlinear friction.
- Gear backlash, cable stretch, and joint compliance create unmodeled dynamics.
- Research shows policies trained without actuator models fail even at low speeds. The gap grows with step frequency.
- **Fauna's approach**: They explicitly model "DC motor dynamics augmented with delay, saturation, and power constraints" and refine parameters using "motor manufacturer specifications, dynamometer measurements, and optimization from real data." This is careful engineering.

**2. Contact Dynamics**
- Ground contact (friction, restitution, surface compliance) is notoriously hard to simulate.
- Foot-ground interaction during walking involves complex deformable contact.
- Sim typically uses simplified contact models (point contact, Coulomb friction) while real floors are varied.
- **Mitigation**: Friction randomization, terrain randomization, training on diverse surfaces.

**3. Sensor Noise and Latency**
- Real IMUs have bias drift, noise, and vibration artifacts.
- Real encoders have quantization and noise.
- Communication latency between sensors, compute, and actuators varies.
- **Mitigation**: Add noise and latency to simulated observations during training.

**4. Morphology Errors**
- Center of mass location, link lengths, inertia tensors are never perfectly known.
- Assembly tolerances mean every robot is slightly different.
- **Mitigation**: Randomize mass, CoM, link lengths during training.

**5. Soft Body / Deformation**
- Real robots have cables, soft covers, compliant joints that affect dynamics.
- These are hard to model accurately.
- **Mitigation**: Domain randomization over stiffness parameters.

### Approaches to Closing the Gap

**Domain Randomization (Standard)**
- Randomize everything: mass, friction, motor strength, latency, terrain, sensor noise.
- Train a single policy that works across all randomized environments.
- Simple but can lead to overly conservative policies (policy hedges against worst case).

**System Identification (Classical)**
- Carefully measure and model the real system parameters.
- Minimize the sim-real gap directly rather than randomizing over it.
- More engineering effort but potentially higher performance.
- **Fauna's approach**: They do both. Careful actuator modeling (system ID) plus training with "disturbances and modeling uncertainty" (domain randomization).

**Teacher-Student Distillation (Modern Best Practice)**
- Teacher has privileged info (ground truth terrain, exact parameters).
- Student learns from observation history only.
- Student implicitly estimates hidden state, bridging the sim-real gap.
- Student policy is more robust than teacher when deployed to real world.

**Sim-to-Sim Validation**
- Train in one sim (Isaac), test in another (MuJoCo) before deploying to real.
- If the policy transfers between simulators, it's more likely to transfer to reality.

**Key insight for conversation**: Ask about their biggest sim-to-real surprises. What broke first? How do they validate before deploying to hardware? This shows practical understanding and genuine curiosity.

---

## 5. Key Papers from Josh Merel

### Paper 1: "Neural Probabilistic Motor Primitives for Humanoid Control" (ICLR 2019)

**Key idea**: Learn a single motor module that compresses thousands of expert policies into a latent space of movement primitives. Architecture: an inverse model with a latent-variable bottleneck. The model is trained entirely offline (no online RL needed) to create a "motor primitive embedding space." Once trained, the system can perform one-shot imitation of whole-body humanoid behaviors -- give it a trajectory it has never seen and it produces natural-looking movement by finding the right point in the latent space. Downstream task controllers operate in the latent space rather than raw action space.

**Why it matters for Fauna**: This is the intellectual foundation for Sprout's control architecture. Instead of a separate policy for each behavior, you have one motor module that can express any behavior through its latent space.

### Paper 2: "Hierarchical Visuomotor Control of Humanoids" (ICLR 2019)

**Key idea**: Factor humanoid control into two levels: (1) low-level motor control from proprioception (trained via imitation learning on motion capture) and (2) high-level task coordination from egocentric vision (trained via RL to maximize sparse task reward). The high-level controller selects and sequences pre-learned motor skills based on what it sees. Demonstrated on tasks requiring visual navigation from an unstabilized egocentric RGB camera during locomotion.

**Why it matters for Fauna**: Sprout has an egocentric camera (ZED 2i) and needs to combine locomotion with visual perception for navigation and manipulation. This paper established the architecture for doing exactly that.

### Paper 3: "Catch & Carry: Reusable Neural Controllers for Vision-Guided Whole-Body Tasks" (SIGGRAPH 2020)

**Key idea**: Extends the hierarchical approach to whole-body tasks involving object interaction (catching balls, carrying boxes). Uses a physics-based environment with realistic actuation, egocentric vision, and touch sensors. Combines motor primitives with human demonstrations and instructed RL with curricula. Key contribution: the neural controllers are *reusable* across different tasks -- same motor module handles catching, carrying, and navigating.

**Why it matters for Fauna**: Sprout needs to do exactly this -- walk to objects, pick them up, carry them, hand them to people. The reusability of the motor module across tasks is the core value proposition of Merel's approach.

### Paper 4: "Learning Transferable Motor Skills with Hierarchical Latent Mixture Policies" (ICLR 2022)

**Key idea**: Introduces a three-level hierarchy of discrete and continuous latent variables to capture high-level behaviors while allowing variance in execution. The learned skills transfer to new tasks, unseen objects, and from state-based to vision-based policies, yielding better sample efficiency than existing methods. Key advance: the mixture of discrete and continuous latents captures both the categorical structure of behaviors (walk vs. reach vs. grasp) and the continuous variation within each category.

**Why it matters for Fauna**: Directly relevant to Sprout's multi-behavior architecture. The discrete modes (walking, kneeling, crawling, dancing) correspond to discrete latent categories, while the continuous variation within each mode (speed, direction, style) corresponds to the continuous latents.

### Paper 5: "Universal Humanoid Motion Representations for Physics-Based Control" (ICLR 2024, Spotlight)

**Key idea**: PULSE -- train a motion imitator on a large unstructured motion dataset (AMASS), then distill the skills into a low-dimensional latent space (32 dimensions) using an encoder-decoder with variational information bottleneck. Learns a prior conditioned on proprioception for sampling. Achieves 99.8% coverage of AMASS motions. The latent space can be used as the action space for hierarchical RL, and sampling from the prior generates long, stable, diverse human motions.

**Why it matters for Fauna**: This is likely the closest precursor to Sprout's actual motor control architecture. A compact, universal motion representation that can be composed into higher-level behaviors.

**Authors include Josh Merel** (Meta Reality Labs Research at this point).

### Paper 6: "Fauna Sprout: A Lightweight, Approachable, Developer-Ready Humanoid Robot" (ArXiv, Jan 2026)

**Key idea**: Full system paper describing Sprout. See Section 6 below for the detailed breakdown.

### Bonus: "A Virtual Rodent Predicts the Structure of Neural Activity Across Behaviours" (Nature, 2024)

**Key idea**: Trained a virtual rat using deep RL to imitate real rat behavior in a physics simulator. Found that the virtual agent's neural network activity predicts real striatum and motor cortex activity better than movement features alone. This validates the hypothesis that biological motor cortex implements something like an inverse dynamics model -- and that the representations learned by RL agents in simulation share structural properties with biological neural activity.

**Authors**: Diego Aldarondo and Josh Merel (both now at Fauna). Published in Nature 632, 594-602 (2024).

**Why it matters**: This is arguably the most scientifically significant paper from the Fauna founding team. It bridges motor control AI and neuroscience, validating that the computational approach underlying Sprout's control has biological plausibility. It also demonstrates the team's scientific caliber.

---

## 6. The Fauna Sprout ArXiv Paper -- Detailed Technical Architecture

**Paper**: "Fauna Sprout: A Lightweight, Approachable, Developer-Ready Humanoid Robot" (arXiv:2601.18963, Jan 26 2026, 49 authors)

### Hardware Platform

- **Size**: 1.07 m (3.5 ft) tall, 22.7 kg (50 lbs)
- **DOF**: 29 degrees of freedom (including articulated eyebrows for expression)
- **Compute**: NVIDIA Jetson AGX Orin (64 GB) for perception, planning, high-level decision-making
- **Motor control**: Custom embedded Motor Control Modules (MCMs) running real-time control loops, connected via Ethernet using CBOR protocol
- **Sensors**:
  - ZED 2i stereo RGB-D camera (30 Hz)
  - IMU (inertial measurement unit)
  - 4x time-of-flight sensors (obstacle detection)
  - 4-microphone array (speech recognition, sound localization)
  - Joint encoders + motor current sensors (proprioception)
  - Force-limited gripper sensors (12 N max)
- **Battery**: Custom high energy density, swappable, 3-3.5 hour runtime
- **Actuators**: "Appropriately sized motors and gear reductions" (favoring small, light actuators over oversized ones to reduce mass, power draw, thermal load while improving controllability and safety)

### Motor Control Stack

**Architecture**: State machine with discrete control modes, NOT a single end-to-end policy.

**Control modes**: Walking, kneeling, crawling, dancing. Each mode encapsulates:
- A behavior-specific RL policy
- Mode-specific safety checks
- Validity conditions
- Transition logic

**Policy structure**: RL policies trained in IsaacSim/IsaacLab. Each policy maps:
- **Inputs**: Short histories of proprioceptive observations + inertial measurements + previous actions
- **Outputs**: Intermediate control targets (not raw torques)
- The control targets are then processed through PD control + current limiting + power constraints before reaching the motors

**Command interface**: Policies accept parameterized commands including:
- Desired base linear velocity
- Desired yaw rate
- Desired root orientation (roll and pitch, specified via projected gravity vector in body frame)
- Desired root height
- Target configurations for upper-body joints

**Transition policies**: Trained via imitation learning. Each transition is a short motion sequence that moves the robot into a configuration compatible with the destination mode.

**Compliance**: Trained into the policies by exposing the robot to disturbances and modeling uncertainty during training, combined with reward structures encouraging stable responses to perturbations. Software torque limits cap maximum force output.

### Actuator Modeling

DC motor dynamics model augmented with:
- Communication/computation delay
- Current saturation
- Power constraints

Model parameters refined from three sources:
1. Motor manufacturer specifications
2. Dynamometer measurements
3. Optimization against real-world data

All actuator assumptions documented and released to developers for transparency.

### Navigation System (Three Components)

**1. Odometry (State Estimation)**
- Extended Kalman Filter (EKF) fusing:
  - Visual features from ZED 2i stereo camera
  - IMU measurements
  - Learned proprioceptive velocity estimator (from the motor control policy itself -- the policy's internal estimate of base velocity)
  - Loop closure constraints
- Output: 50 Hz pose, velocity, and covariance estimates
- Design rationale: Bipedal locomotion causes "intermittent, asymmetric foot contacts and rapid changes in support surfaces" that break standard visual odometry. The learned proprioceptive estimator regularizes short-term motion estimates.

**2. Volumetric Mapping**
- TSDF-based dense 3D reconstruction
- Organized into locally-consistent submaps ("maplets")
- Hierarchical pose graph for global alignment (optimized via GTSAM)
- ML-based loop closure with cascaded neural networks
- Claims ~30% of RTAB-Map's compute while outperforming it

**3. Navigation Planning**
- Occupancy grid with static + dynamic OctoMap layers
- Global planner: Hybrid A*
- Local planner: Pure pursuit path tracker
- Planning cycle: 10 Hz
- Generates velocity commands fed to the locomotion policy's command interface

### Manipulation

- Custom single-DOF grippers (not multi-fingered hands)
- Software-limited fingertip force: 12 N maximum
- Prioritizes "durability and consistent grasping performance" over dexterity
- Gripper commands integrated into whole-body control via inverse kinematics (PINK library)
- Use case: object fetching, hand-offs, simple grasps -- not fine manipulation

### Teleoperation System

- **Platform**: "Embody" -- Unity application for Meta Quest VR headsets
- **Input**: Meta Movement SDK for hand/controller tracking
- **Calibration**: Startup routine estimates user's arm lengths, torso height, comfortable range
- **Retargeting**: Morphology-aware linear mapping from calibrated VR space to robot frame
- **IK solver**: PINK library -- converts Cartesian poses to joint angles with position cost, orientation cost, and regularization
- **Modes**: Full-body, upper-body-only, seated teleoperation
- **Data collection**: Records at 30 Hz (stereo RGB), 50 Hz (commands), 125 Hz (proprioceptive state)
- **DAgger support**: "Ghost" controller visualization for seamless human takeover during autonomous operation (enables iterative policy improvement)

### Software Architecture

- Docker containerization
- ROS 2 for inter-process communication
- High-bandwidth paths use shared-memory/zero-copy transports
- Zenoh middleware for on/off-board compute bridging
- WebRTC for video/audio streaming
- Foxglove protocol for visualization/telemetry
- CBOR/Ethernet for motor controller communication
- JSON/WebSocket for VR headset communication

### Safety Architecture (Three-Tier Defense in Depth)

1. **Mechanical/Electrical**: Soft exterior materials, minimal pinch points, low center of gravity, conservative motor sizing
2. **Embedded**: Real-time safety subsystem independent of application compute (hardware watchdog)
3. **Application**: Compliant policies, vision-based navigation safety, software torque limits

### Key Design Decisions

- **Why small?** 22.7 kg at 1.07 m has inherently low kinetic energy. Physics limits the damage even in worst-case collisions. This is the fundamental safety argument.
- **Why state machine, not end-to-end?** Explicit mode structure allows per-mode safety checks, easier debugging, and cleaner transition logic. The policies within each mode can be end-to-end, but the mode switching is structured.
- **Why IsaacSim for training?** GPU parallelism for RL training at scale. Despite Merel's DeepMind/MuJoCo background, Isaac Lab was the pragmatic choice for massive parallel simulation.
- **Why developer platform?** Fauna's bet is that the killer app comes from external developers, not internal teams. Full SDK, documented actuator models, and modular architecture lower the barrier.

---

## Quick Reference: Vocabulary and Concepts

| Term | Meaning |
|------|---------|
| **Projected gravity** | Gravity vector expressed in the robot's body frame. Used as input to locomotion policies to maintain balance regardless of terrain slope. |
| **PD control** | Proportional-Derivative control. The final layer that converts policy outputs to motor commands. P gain controls stiffness, D gain controls damping. |
| **TSDF** | Truncated Signed Distance Field. A 3D representation where each voxel stores the signed distance to the nearest surface. Efficient for real-time 3D reconstruction. |
| **Hybrid A*** | A* search extended to handle continuous heading (not just grid cells). Used for planning paths for non-holonomic vehicles/robots. |
| **Pure pursuit** | A path-tracking algorithm that computes the curvature needed to reach a lookahead point on the path. Simple, robust, well-understood. |
| **PINK** | A Python inverse kinematics library. Converts desired end-effector poses to joint angles. |
| **GTSAM** | Georgia Tech Smoothing and Mapping. A factor graph optimization library for SLAM. Literally from GT -- Mark could mention familiarity. |
| **DAgger** | Dataset Aggregation. An iterative imitation learning algorithm where the expert corrects the learner's mistakes to improve the training distribution. |
| **CBOR** | Concise Binary Object Representation. A compact binary data format used for efficient communication between Jetson and motor controllers. |
| **Zenoh** | A pub/sub middleware designed for robotics and IoT. Low-latency alternative to ROS DDS for high-bandwidth data. |
| **Motor primitive** | A reusable low-level motor skill (e.g., a step, a reach, a turn) that can be composed into complex behaviors. |
| **Variational information bottleneck** | A technique that forces a neural network to compress information through a low-dimensional latent space, regularized by a KL divergence term. Produces structured, smooth latent representations. |
| **Backdrivability** | How easily an actuator's output can be moved by external forces (pushing back through the gearbox). High backdrivability = compliant/safe. Low = rigid/dangerous. |

---

## Threads to Pull On in Conversation

**Technical questions that demonstrate depth:**
1. "The paper describes a state machine over control modes rather than an end-to-end policy. Was that a deliberate architectural choice or something you converged on? How do you handle the transition policies between modes?"
2. "You use a learned proprioceptive velocity estimator as part of your EKF. Does that estimator come from the locomotion policy itself, or is it trained separately?"
3. "How much of the sim-to-real gap was actuator modeling vs. contact dynamics? What surprised you most?"
4. "The compliance is trained into the policy via disturbances during training. Have you explored any formal safety guarantees on top of the learned compliance -- something like CBFs or safety filters?"
5. "With GTSAM for the mapping backend -- how do you handle the computational cost of the pose graph growing over long deployments?"

**Questions that connect to Mark's background:**
6. "My PhD was in optimization for spacecraft controls, and I did work on Control Barrier Functions for safe autonomy. The compliance and safety approach in Sprout is interesting -- it's all trained behavior plus torque limits. Have you thought about formal safety layers that could provide guarantees, especially for edge cases the training distribution didn't cover?"
7. "I built a shielded RL system at AFRL -- essentially a learned policy with a safety filter that provably prevents constraint violations. Is that kind of safety architecture relevant to what you're building, or is the lightweight form factor sufficient?"

**Strategic questions:**
8. "Who's building applications on Sprout today? What's surprised you about how developers are using it?"
9. "What's the hardest open problem in the motor control stack right now?"
10. "How do you think about the manipulation roadmap? Single-DOF grippers are a starting point -- where does that go?"
