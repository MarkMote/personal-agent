# Mark L. Mote

Email: marklmote@gmail.com
LinkedIn: https://www.linkedin.com/in/mote/
GitHub: https://github.com/MarkMote
Google Scholar: https://scholar.google.com/citations?user=rvIwsNMAAAAJ&hl=en&oi=ao

## Overview

- I founded two companies: Pytheia (CEO, real-time multi-camera 3D perception) and [Roostr](https://www.shiproostr.com/) (CTO, AI-native freight ops).
- I have a Robotics PhD from Georgia Tech. My research spanned optimization, spacecraft control, and safe autonomy.
- My [dissertation](/papers/MOTE-DISSERTATION-2021.pdf) was on run-time assurance, the art of moving fast without breaking things.
- I was on the founding team of the [Robotarium](https://www.robotarium.gatech.edu/), an open-access multi-agent robotics lab. It's been used in over 16,000 experiments and is still active today.
- I did research collaborations and internships at MIT Lincoln Lab, Stanford, NASA JPL, and AFRL.

## Education

**Ph.D. in Robotics** (Highest Honors)
Georgia Institute of Technology, Atlanta, GA — 2021
*1,449 citations (h-index 13, i10-index 17)*

**M.S. in Aerospace Engineering** (Highest Honors)
Georgia Institute of Technology, Atlanta, GA — 2018

**B.S. in Aerospace Engineering** (Highest Honors)
Georgia Institute of Technology, Atlanta, GA — 2015

## Experience

### Roostr
**Co-Founder & CTO** | 2024 - present | New York, NY

I co-founded [Roostr](https://www.shiproostr.com/), an AI-native freight forwarder, and was the sole production engineer for the freight ops stack.
I built the end-to-end system for automated procurement, quoting, and shipment workflows.
The core was a long-running agent pipeline that turned messy emails and attachments into validated, normalized, searchable pricing offers.
On top of that foundation, we shipped quoting automation and encoded forwarding SOPs as a finite-state policy graph to enable progressive automation. 
The stack was a Python/FastAPI backend (Docker on DigitalOcean) plus a multi-tenant Next.js/TypeScript dashboard (Vercel).
One fully integrated customer attributed roughly $1M in incremental monthly revenue to faster procurement and quoting (customer-reported).

- [Landing page](https://www.shiproostr.com/)
- [Product overview video](https://youtu.be/fRAztbK5-f8)

### Pytheia
**Co-Founder & CEO** | Sept 2021 - 2024 | Atlanta, GA

I was co-founder and CEO of [Pytheia](https://www.pytheia.com/), where we built spatial perception systems and later LLM-based data products.
I owned GTM end-to-end, executing sales calls, pilots, pricing, proposals, and delivery.
On the product side, I led the build of Argus, a real-time multi-camera 3D perception system for detection, tracking, calibration, and fusion from arbitrary camera feeds.
After exploring AV, robotics, and retail use cases, we pivoted to data automation: LLM-driven data acquisition pipelines and demand-forecasting dashboards for enterprise customers.
We bootstrapped to just over $300k ARR on $20k of capital from [Pioneer](https://pioneer.app/).

- [Argus multi-camera demo (donut shop)](https://youtu.be/Wdzhru0Y5f0)
- [Argus prototype (mall)](https://youtu.be/U0U-4g30bqg)

### Georgia Tech
**Graduate Research Assistant** | 2016 - 2021 | Atlanta, GA

I was a founding team member of the [Robotarium](https://www.robotarium.gatech.edu/), a remotely accessible multi-robot testbed funded by NSF/ONR (~$2.5M).
The lab has supported 16,000+ experiments and remains active.
I built safety verification tooling that let researchers run code on physical robots remotely without damaging hardware.
That work directly informed my [PhD thesis](/papers/MOTE-DISSERTATION-2021.pdf) on safe autonomy and runtime assurance ([tutorial paper](https://ieeexplore.ieee.org/document/10081233)).
In my dissertation work, I was especially interested in mixed-integer convex optimization for trajectory planning, and in spacecraft control.

- [Dissertation](/papers/MOTE-DISSERTATION-2021.pdf)
- [Spacecraft demo video](https://youtu.be/JQBrW4yLVHk)
- [Robotarium demo video](https://youtu.be/W68BmRtUNlw)

### NASA Jet Propulsion Laboratory
**Research Intern · Maritime and Multi-Agent Autonomy Group** | May - Aug 2019 | Pasadena, CA

I worked with the [Maritime and Multi-Agent Autonomy Group](https://www-robotics.jpl.nasa.gov/who-we-are/groups/347N/) at NASA JPL.
I designed communication and control algorithms for distributed asteroid exploration with spacecraft swarms.
I built a simulation framework to validate swarm behaviors and we published the results in this [JGCD paper](https://arc.aiaa.org/doi/10.2514/1.G006515).
As a side project, I created an algorithm to approximate Voronoi regions on asteroid surfaces.

- [Communication-Aware Orbit Design for Small Spacecraft Swarms around Small Bodies, AIAA Journal of Guidance, Control, and Dynamics](https://arc.aiaa.org/doi/10.2514/1.G006515)

### Air Force Research Laboratory
**Intern · Autonomy Capabilities Team 3 (ACT3)** | May - Aug 2020 | Dayton, OH

I interned with [ACT3](https://www.afrl.af.mil/ACT3/) at AFRL, working on safe autonomous spacecraft docking.
I developed a backup guidance system that uses natural motion trajectories to safely park a chaser spacecraft around a target, with mixed-integer programming for optimal transfers ([IEEE Aerospace 2021](https://ieeexplore.ieee.org/document/9438434)).
I also contributed to follow-on work combining runtime assurance with reinforcement learning for safe satellite docking.

- [Natural Motion-Based Trajectories (IEEE Aerospace)](https://ieeexplore.ieee.org/document/9438434)
- [Comparing RTA Approaches (IEEE CSL)](https://ieeexplore.ieee.org/document/9483804)
- [RTA + Reinforcement Learning (JAIS)](https://arc.aiaa.org/doi/10.2514/1.I011199)

### MIT Lincoln Laboratory
**Research Intern · BMDS Integration Group** | Summer 2017, Summer 2018 | Boston, MA

I interned with the BMDS Integration Group at MIT Lincoln Laboratory.
My work applied formal verification techniques to neural network image classifiers.
We had a publication in the works, but the research became restricted. 
I can discuss the topic but not specifics.

### Stanford University
**Visiting Researcher · Autonomous Systems Lab** | June - July 2018 | Stanford, CA

I spent a summer at [Marco Pavone's](https://profiles.stanford.edu/marco-pavone) Autonomous Systems Lab ([ASL](https://stanfordasl.github.io/)) at Stanford.
I was researching how collisions could be encoded into optimal trajectory planners, the idea being that bouncing could lead to better performance and even improved safety, solved optimally via mixed-integer programs.
I implemented my algorithm on the lab's 3-DOF spacecraft free-flyer testbed, and we later published a [journal article](https://arc.aiaa.org/doi/abs/10.2514/1.G004788) based on the work.

- [Paper: Collision-Inclusive Trajectory Optimization (AIAA JGCD)](https://arc.aiaa.org/doi/abs/10.2514/1.G004788)
- [Hardware demo](https://youtu.be/S1g-zmkKMME)
- [Simulation demo (collisions for safer planning)](https://youtu.be/B8VU9IS12WU)

### KAUST
**Visiting Student** | Jan - May 2020 | Thuwal, Saudi Arabia

I was a visiting student at the Computer, Electrical and Mathematical Sciences & Engineering department at KAUST. It was collaborative research on safe autonomy and control theory.

### ISAE-ENSMA
**Research Intern · LIAS Laboratory** | May - July 2015 | Poitiers, France

I interned at the [LIAS Lab](https://www.lias-lab.fr/) at ISAE-ENSMA.
I built and compared PID and integral backstepping controllers for a quadcopter in Simulink.
I also contributed to design automation research for credible auto-coding of flight controllers using Simulink and Gene-Auto.

## Publications

- **[Runtime assurance for safety-critical systems: An introduction to safety filtering approaches for complex control systems](https://ieeexplore.ieee.org/document/10081233)** (2023)
  KL Hobbs, ML Mote, MCL Abate, SD Coogan, EM Feron. *IEEE Control Systems Magazine*.
- **[Run time assured reinforcement learning for safe satellite docking](https://arc.aiaa.org/doi/10.2514/1.I011199)** (2023)
  K Dunlap, M Mote, K Delsing, KL Hobbs. *Journal of Aerospace Information Systems*.
- **[Run time assurance for spacecraft attitude control under nondeterministic assumptions](https://ieeexplore.ieee.org/document/10041958)** (2023)
  M Abate, M Mote, M Dor, C Klett, S Phillips, K Lang, P Tsiotras, E Feron, S Coogan. *IEEE Transactions on Control Systems Technology*.
- **[Natural motion-based trajectories for automatic spacecraft collision avoidance during proximity operations](https://ieeexplore.ieee.org/document/9438434)** (2021)
  ML Mote, CW Hays, A Collins, E Feron, KL Hobbs. *IEEE Aerospace Conference*.
- **[Comparing run time assurance approaches for safe spacecraft docking](https://ieeexplore.ieee.org/document/9483804)** (2021)
  K Dunlap, M Hibbard, M Mote, K Hobbs. *IEEE Control Systems Letters*.
- **[Ariadne: A common-sense thread for enabling provable safety in air mobility systems with unreliable components](https://repository.kaust.edu.sa/handle/10754/666807)** (2021)
  O Sanni, M Mote, D Delahaye, M Gariel, T Khamvilai, E Feron, S Saber. *KAUST Repository*.
- **[Verification and runtime assurance for dynamical systems with uncertainty](https://dl.acm.org/doi/10.1145/3447928.3456655)** (2021)
  M Abate, M Mote, E Feron, S Coogan. *ACM HSCC*.
- **[Optimization-based approaches to safety-critical control with applications to space systems](/papers/MOTE-DISSERTATION-2021.pdf)** (2021)
  ML Mote. *PhD Thesis, Georgia Tech*.
- **[The Robotarium: Globally impactful opportunities, challenges, and lessons learned in remote-access, distributed control of multirobot systems](https://ieeexplore.ieee.org/document/8960572)** (2020)
  S Wilson, P Glotfelter, L Wang, S Mayya, G Notomista, M Mote, M Egerstedt. *IEEE Control Systems Magazine*.
- **[A scalable safety critical control framework for nonlinear systems](https://ieeexplore.ieee.org/document/9195216)** (2020)
  T Gurriet, M Mote, A Singletary, P Nilsson, E Feron, AD Ames. *IEEE Access*.
- **[Collision-inclusive trajectory optimization for free-flying spacecraft](https://arc.aiaa.org/doi/10.2514/1.G004468)** (2020)
  M Mote, M Egerstedt, E Feron, A Bylard, M Pavone. *AIAA Journal of Guidance, Control, and Dynamics*.
- **[Communication-aware orbit design for small spacecraft swarms around small bodies](https://arc.aiaa.org/doi/10.2514/1.G006515)** (2020)
  F Rossi, S Bandyopadhyay, M Mote, JP de la Croix, A Rahmani. *AIAA/AAS Astrodynamics Specialist Conference*.
- **[A scalable controlled set invariance framework with practical safety guarantees](https://ieeexplore.ieee.org/document/9029524)** (2019)
  T Gurriet, M Mote, A Singletary, E Feron, AD Ames. *IEEE CDC*.
- **[Modeling and experimental validation of the mechanics of a wheeled non-holonomic robot capable of enabling homeostasis](https://arxiv.org/abs/1909.11653)** (2019)
  J Epps, E Feron, M Mote. *arXiv*.
- **[An online approach to active set invariance](https://ieeexplore.ieee.org/document/8619139)** (2018)
  T Gurriet, M Mote, AD Ames, E Feron. *IEEE CDC*.
- **[The Robotarium: A remotely accessible swarm robotics research testbed](https://ieeexplore.ieee.org/document/7989200)** (2017)
  D Pickem, P Glotfelter, L Wang, M Mote, A Ames, E Feron, M Egerstedt. *IEEE ICRA*.
- **[Robotic trajectory planning through collisional interaction](https://ieeexplore.ieee.org/document/8264095)** (2017)
  M Mote, JP Afman, E Feron. *IEEE CDC*.
- **[Motion rectification for an homeostasis-enabling wheel](https://arxiv.org/abs/1705.04399)** (2017)
  JP Afman, M Mote, E Feron. *arXiv*.
- **[Safe, remote-access swarm robotics research on the Robotarium](https://arxiv.org/abs/1604.00640)** (2016)
  D Pickem, L Wang, P Glotfelter, Y Diaz-Mercado, M Mote, A Ames, E Feron, M Egerstedt. *arXiv*.
- **[On the design and optimization of an autonomous microgravity enabling aerial robot](https://arxiv.org/abs/1611.07650)** (2016)
  JP Afman, J Franklin, ML Mote, T Gurriet, E Feron. *arXiv*.
- **[A framework for collision-tolerant optimal trajectory planning of autonomous vehicles](https://arxiv.org/abs/1611.07608)** (2016)
  ML Mote, JP Afman, E Feron. *arXiv*.
- **[Establishing trust in remotely reprogrammable systems](https://dl.acm.org/doi/10.1145/2950112.2964577)** (2016)
  T Gurriet, ML Mote, A Ames, E Feron. *HCI-Aero*.

## Talks

- **Run Time Assurance for Safe Spacecraft Attitude Control under Nondeterministic Assumptions** — Air Force Research Lab (AFRL), Albuquerque, NM (2020)
- **Run Time Assurance with Control Barrier Functions** — Air Force Research Lab (AFRL), Virtual (2019)
- **A Scalable Controlled Set Invariance Framework with Practical Safety Guarantees** — IEEE CDC, Nice, France (2019)
- **Run Time Assurance through Scalable Controlled Set Invariance** — Air Force Research Lab (AFRL), Dayton, OH (2019)
- **Integrated Communications and Control for Small Body Exploration with Multiple Spacecraft** — JPL Multi-Agent and Maritime Autonomy Group, Los Angeles, CA (2019)
- **Robust Collision Avoidance for Driver Assisted Boats** — DCL Student Symposium, Atlanta, GA (2019)
- **Formal Verification of Image Classification Decisions with Reluplex** — Stanford Intelligent Systems Laboratory (SISL), Stanford, CA (2018)
- **Formal Verification of Image Classifier Neural Networks** — Naval Applications of Machine Learning Conference (NAML), San Diego, CA (2018)
- **An online approach to active set invariance** — IEEE CDC (2018)
- **Robotic Trajectory Planning through Collisional Interaction** — IEEE CDC, Melbourne, Australia (2017)
- **Formal Verification of Image Classifier Neural Networks** — United Technologies Research Center (UTRC), Hartford, CT (2017)
- **Formal Verification of Image Classifier Neural Networks** — MIT Lincoln Laboratory, Boston, MA (2017)
- **Robotic Trajectory Planning through Collisional Interaction** — DCL Student Symposium, Atlanta, GA (2017)
- **Validation of Convex Optimization Algorithms and Credible Implementation for MPC** — AIAA SciTech, Dallas, TX (2017)
- **The Robotarium: A remotely accessible swarm robotics research testbed** — IEEE ICRA (2017)
- **Establishing Trust in Remotely Reprogrammable Systems** — HCI-Aero, Paris, France (2016)

## Awards

- **Best Paper Award - Multi-Robot Systems** — IEEE ICRA (2017)
  *The Robotarium: A Remotely Accessible Swarm Robotics Research Testbed*
- **Best Conference Paper Award - Finalist** — IEEE ICRA (2017)
  *The Robotarium: A Remotely Accessible Swarm Robotics Research Testbed*
- **NASA iTech Innovation Competition - Top 25 Semifinalist** — NASA (2017)
  *Autonomous Zero-Gravity Laboratory; Challenge Area: X-Factor Innovation*
- **PhD with Highest Honors** — Georgia Institute of Technology (2021)
  *Robotics*
- **MS with Highest Honors** — Georgia Institute of Technology (2018)
  *Aerospace Engineering*
- **BS with Highest Honors** — Georgia Institute of Technology (2015)
  *Aerospace Engineering*
- **Presidential Undergraduate Research Award (PURA)** — Georgia Institute of Technology (2015)
  *Communication Protocol Analysis for Unmanned Aerial Vehicles*
- **Coca-Cola Mobility Scholarship** — Coca-Cola / Georgia Tech (2015)
  *Summer Internship 2015*

## Miscellaneous

- I like languages. I'm currently learning Georgian and built this [spaced-repetition app](https://learn-georgian.markmote.com/). I use it every day.
- I worked in a [tutoring lab](https://success.students.gsu.edu/learning-tutoring-center/) at Georgia State University to help pay my way through undergrad.
- Before engineering, I wanted to be a pilot. I funded lessons by working as an electrician and flipping a car.
- Applied control barrier functions (automated collision avoidance software) to a pontoon boat. [Paper](/papers/Online_Collision_Avoidance_for_Driver_Assisted_Boats.pdf), [hardware demo](https://youtu.be/Rp9EWj2MOgc).
- Helped design a [zero-gravity enabling quadcopter](https://arxiv.org/abs/1611.07650).
- Took a tiny part in this SIGBOVIK submission on finding [best shuffled deck](/papers/SIGBOVIK_2024.pdf) of cards.
- Collisions as information sources in a robot swarm. A brief project using Bayes theorem and hidden Markov Models. [Paper](/papers/collisions_as_information.pdf), [hardware demo](https://youtu.be/EYuRmeX5gBo).
- My [academic genealogy](https://www.mathgenealogy.org/id.php?id=305274).