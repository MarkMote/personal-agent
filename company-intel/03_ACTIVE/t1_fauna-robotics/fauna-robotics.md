# Fauna Robotics - Company Research

**Last updated:** 2026-02-24
**Tier:** T1 (Active)
**Status:** Intro call with Josh Merel (CTO) today 5pm ET

---

## What They're Building

Fauna Robotics is building **Sprout**, a lightweight, developer-ready humanoid robot platform designed for **human spaces** -- not factories. Their thesis: over 80% of the workforce is in services, and existing humanoids (Figure, Tesla Optimus, Agility Digit) are heavy, rigid, industrial machines requiring safety cages. Fauna is going the opposite direction: small, soft, safe, expressive, and cheap enough to deploy in homes, hotels, retail, classrooms, and healthcare.

**Sprout specs:**
- 107 cm tall (3.5 ft), 22.7 kg (50 lbs) -- child-sized
- 29 degrees of freedom (including articulated eyebrows)
- NVIDIA Jetson AGX Orin (64GB) onboard compute
- ZED 2i stereo camera, 4x time-of-flight sensors, 4x mic array, IMU
- 3-3.5 hour battery (swappable)
- Integrated grippers for manipulation
- Soft exterior, minimal pinch points, low center of gravity
- **Price: $50,000** (Creator Edition, shipping now)

**Key capabilities out-of-box:**
- Pre-trained motor control policies: walking, kneeling, crawling, sitting, jumping, dancing
- Compliant motor control (yields to external forces rather than resisting)
- Built-in mapping/localization pipeline (visual-inertial-kinematic odometry via EKF)
- Modular navigation stack (pose tracking, obstacle avoidance, global route generation)
- Full-body VR teleoperation
- LLM integration for voice commands
- Expressive face (LED displays, articulated eyebrows, body language)
- Full SDK for rapid application development

**Early customers:** Disney, Boston Dynamics, UC San Diego, NYU

---

## Funding

**Total raised: $30M** (seed round, announced April 8, 2025)

The $16.6M figure that circulated earlier appears to be a partial/earlier reporting. Their X/Twitter announcement confirms $30M total.

**Investors:**
- **Kleiner Perkins** (confirmed)
- **Lux Capital** (confirmed)
- **Quiet Capital** (confirmed)
- **Village Global** (confirmed)
- Bluebirds Capital (per some sources)
- Terrain (per some sources)

**Use of funds:** R&D, product innovation, scaling operations, next-gen robot development.

**Company stage:** Seed. Some sources list "Series B" on Tracxn but this appears incorrect given the $30M seed announcement. Founded 2024, launched from stealth Jan 27, 2026.

---

## Founders & Key People

### Rob Cochran -- Co-founder & CEO
- **Background:** Head of Product Management at CTRL-labs (wearable neurotech, neural interfaces). CTRL-labs was acquired by Facebook/Meta in 2019 for ~$1B. After that, Product at Facebook (2019-2020), then Managing Director at Goldman Sachs (2020-2024). He's joked that he "spent a misguided four years at Goldman Sachs" before teaming up with Merel again.
- **Profile:** Business/product leader, not an engineer per se. Brings the product vision, fundraising muscle, and operational experience.

### Josh Merel -- Co-founder & CTO
- **Background:** Former DeepMind research scientist, expert in robot locomotion and learned motor control in simulation. Co-author of the landmark "virtual rat" paper in Nature (2024) with Diego Aldarondo -- an AI-powered virtual rodent that uses deep RL to learn motor control, with neural activity patterns that predict real rat brain activity. Columbia University educated.
- **Previously at CTRL-labs** alongside Rob Cochran. This is the second time they're building together.
- **Profile:** The technical brain. Deep expertise in exactly the motor control / embodied AI / sim-to-real space that defines Fauna's approach. Published in Nature. This is the person Mark is meeting today.
- **Email:** josh@faunarobotics.com

### Lerrel Pinto -- Co-founder (academic)
- **Position:** Assistant Professor of Computer Science at NYU (Courant Institute)
- **Education:** PhD in Robotics from Carnegie Mellon, postdoc at UC Berkeley
- **Awards:** NSF CAREER Award, 2023 Packard Fellowship, 2025 Sloan Fellowship, MIT Technology Review "Robotics Innovator"
- **Research:** Large-scale robot learning, self-supervised learning, dexterous manipulation, affordable open-source robots
- **Vision:** Robots integrated into home life for chores and elder care. Novel data collection approaches (robots learning through self-supervised exploration).
- **Note:** Yann LeCun (Chief AI Scientist at Meta, NYU professor) publicly endorsed Fauna on X, calling it "a new NYC-based robotics startup, co-founded by my dear NYU colleague @LerrelPinto"
- **Profile:** World-class academic co-founder. Provides the research pipeline and NYU connection.

### Diego Aldarondo -- Research Scientist
- **Background:** Co-author with Josh Merel on the Nature "virtual rodent" paper (2024). The paper trained a virtual rat using deep RL to imitate real rat behavior, finding that the virtual agent's neural activity predicts real striatum/motor cortex activity better than movement features alone.
- **Profile:** Senior research talent, deeply embedded in the motor control + neuroscience intersection.

### Michael Mignatti -- Head of Manufacturing
- Based in Brooklyn area (per LinkedIn)

### Other noted contacts:
- **Bolun Dai** -- Research Scientist (Thomas Gurriet is a mutual connection/co-author with Mark)
- **Anthony Moschella** -- GT alum (Mark's original contact point)
- **Ana Pervan, Daniel Corbalan, Dave Petrillo** -- named contributors on the ArXiv paper

---

## Technical Approach -- What Makes Them Different

### 1. Learned Motor Control (not classical control)
Fauna uses **trained neural network policies** for locomotion, not hand-tuned controllers. Policies map high-level commands + proprioceptive state to control targets. The operator controls motion intent; the policy handles dynamics. This is directly from Josh Merel's DeepMind work on locomotion learning.

### 2. Compliance-First Design
Motor control is **compliant** -- the robot yields to external forces rather than resisting. Software-level torque limits ensure the robot can't hurt anyone. This is a fundamental design choice, not a bolt-on safety feature. Most humanoids (Figure, Tesla) are designed to be strong; Fauna is designed to be safe.

### 3. Lightweight + Small Form Factor
At 50 lbs and 3.5 ft, Sprout has inherently low kinetic energy. Even if it falls on you, it can't do serious damage. Compare to Figure 02 (~130 lbs, 5'6") or Tesla Optimus (~125 lbs, 5'8"). This is a deliberate choice to enable deployment in human spaces without safety infrastructure.

### 4. Developer Platform Model
Fauna's bet is that the killer app won't come from them -- it'll come from developers. They provide hardware + motor control + perception + navigation out of the box, and let others build on top. Modular architecture means one team's solution can be used by others. This is the "iPhone for humanoids" play.

### 5. Sim-to-Real Pipeline
The ArXiv paper (49 authors) describes a full system including VR teleoperation, whole-body control, and the connection between simulation-trained policies and real hardware. The odometry system uses an EKF fusing stereo vision, IMU, and a learned proprioceptive velocity estimator from the motor control policy itself.

### 6. Expressivity
Articulated eyebrows, LED face, body language -- designed for social interaction. Most humanoids look industrial. Sprout is designed to be approachable. Think WALL-E, not Terminator.

---

## Competitive Positioning

| Company | Height/Weight | Focus | Price | Stage |
|---------|--------------|-------|-------|-------|
| **Fauna (Sprout)** | 3.5ft / 50 lbs | Human spaces, dev platform | $50K | Seed, shipping |
| Figure (02/03) | 5'6" / 130 lbs | Factory automation | N/A | Series B, $2.6B raised |
| Tesla (Optimus) | 5'8" / 125 lbs | Factory, eventually consumer | TBD | Corporate, pre-revenue |
| Agility (Digit) | 5'9" / 140 lbs | Warehouse logistics | N/A | Series B |
| 1X (NEO) | ~5'6" / ~65 lbs | Home + labor | ~$20K target | Series B |
| Boston Dynamics (Atlas) | 5'0" / 190 lbs | R&D / industrial | Not for sale | Hyundai-owned |

**Fauna's contrarian bet:** Everyone else is going big, strong, and factory-first. Fauna is going small, safe, and service-first. They believe hospitality, healthcare, education, and entertainment will adopt humanoids faster than manufacturing. The $50K price point is roughly one year's salary for a hospitality worker.

**Notable:** Boston Dynamics is listed as an early customer/partner, which is interesting -- the gorilla in the room is buying Fauna's small robot, presumably for research or applications where Atlas is too heavy/dangerous.

---

## Recent News & Timeline

- **2024:** Founded by Rob Cochran, Josh Merel, Lerrel Pinto
- **Sep 2024:** Completed seed round (initial reporting: $16.6M)
- **Apr 2025:** Announced full $30M seed round (Kleiner Perkins, Lux Capital, Quiet Capital)
- **Jan 27, 2026:** Emerged from stealth, launched Sprout (Creator Edition shipping)
- **Jan 27, 2026:** ArXiv paper published: "Fauna Sprout: A lightweight, approachable, developer-ready humanoid robot" (49 authors)
- **Jan 27, 2026:** AP press coverage ("Not ready for robots in homes?"), picked up by Fox News, Yahoo Finance, dozens of outlets
- **Feb 2026:** Actively hiring across research, software, hardware, manufacturing (~15+ open roles)

---

## Company Culture & Office

- **Location:** New York City, Flatiron District (Manhattan). Team members in Brooklyn area. **Not Brooklyn HQ as originally assumed -- it's Flatiron.**
- **Manufacturing:** Assembled in America, in NYC. Tight feedback loop between engineering and production.
- **Team size:** ~35-50 employees (sources vary; growing fast post-stealth launch)
- **Team DNA:** Veterans from CTRL-labs, Meta, Google DeepMind, Amazon. Heavy neuroscience/motor control research DNA from the Merel/Aldarondo/Pinto axis.
- **Culture signals:** "Designed in NYC. Assembled in America." Research-heavy team with Nature publications. Developer-first product philosophy. The CEO's self-deprecating Goldman joke suggests a non-corporate culture. Active on social media. Published a full ArXiv paper (academic credibility).
- **Hiring roles:** Motor Control Scientist, Robot Animation Scientist, Lead Research Scientist (Manipulation & Autonomy), ML Infrastructure Engineer, VR/MR Teleoperation Developer, Mechanical Engineers, Software Engineers, Assembly Technicians, Forward Deployed Engineer

---

## Why This Matters for Mark

**Strong fit signals:**
- Motor control + learned control policies = direct overlap with Mark's controls/optimization PhD
- The CTO (Josh Merel) reached out proactively after seeing Mark's application -- genuine interest
- NYC location (Flatiron) -- Mark's top geography preference
- Robotics + AI intersection = Mark's sweet spot
- Small team (~40 people), early stage = high impact, leadership potential
- "Safe autonomy" emphasis echoes Mark's CBF/safety work
- Lerrel Pinto's research on self-supervised robot learning connects to Mark's RL background

**Potential concerns:**
- $50K price point in competitive humanoid market -- can they win vs. well-funded Figure ($2.6B) and Tesla?
- Seed stage with $30M -- solid but not a warchest
- "Service industry" humanoid bet is unproven -- will hotels really buy robots?
- Humanoid-specific portfolio gap (noted in role.md fit assessment)
