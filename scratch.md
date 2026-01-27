---
## HuggingFace Wild Card Application Drafts

Online projects/contributions:

The Robotarium (https://www.robotarium.gatech.edu/)
I was on the founding team of this remotely accessible multi-robot testbed at Georgia Tech. The idea was to let anyone in the world run code on real robots without owning hardware. I built safety verification tooling that let researchers execute untrusted code without damaging the robots. The project has supported 16,000+ experiments and is still active today. Our paper won Best Paper in Multi-Robot Systems at ICRA 2017.
Paper: https://ieeexplore.ieee.org/document/7989200
Demo: https://youtu.be/W68BmRtUNlw

Runtime Assurance Tutorial (https://ieeexplore.ieee.org/document/10081233)
I co-authored a tutorial paper on runtime assurance in IEEE Control Systems Magazine. It's become a reference for making autonomous systems reliable, introducing control barrier functions and safety filtering to a broader audience. Directly relevant to what I'd want to build at LeRobot.

Collision-Inclusive Trajectory Optimization
Research at Stanford's Autonomous Systems Lab on encoding collisions into trajectory planners. The idea: bouncing can lead to better performance and improved safety. I implemented the algorithm on their 3-DOF spacecraft free-flyer testbed.
Paper: https://arc.aiaa.org/doi/10.2514/1.G004788
Hardware demo: https://youtu.be/S1g-zmkKMME

Spacecraft Swarm Control at NASA JPL
Designed communication and control algorithms for distributed asteroid exploration with spacecraft swarms. Built the simulation framework and published in AIAA JGCD.
Paper: https://arc.aiaa.org/doi/10.2514/1.G006515

Safe RL for Spacecraft Docking at AFRL
Contributed to work combining runtime assurance with reinforcement learning for safe satellite docking. The guardrails let the RL policy explore aggressively while preventing unsafe maneuvers.
Paper: https://arc.aiaa.org/doi/10.2514/1.I011199

Argus - Multi-Camera 3D Perception
At my first startup (Pytheia), I led the build of Argus, a real-time multi-camera 3D perception system for detection, tracking, and calibration from arbitrary camera feeds.
Demo (donut shop): https://youtu.be/Wdzhru0Y5f0
Demo (mall): https://youtu.be/U0U-4g30bqg

Control Barrier Functions on a Pontoon Boat
Applied CBF-based collision avoidance to a real boat. A fun side project that showed these techniques work outside of simulation.
Hardware demo: https://youtu.be/Rp9EWj2MOgc

Georgian Language Learning App (https://learn-georgian.markmote.com/)
Built a spaced-repetition app to teach myself Georgian. I use it every day. Small project but shows I build things for fun.

Full publication list: https://scholar.google.com/citations?user=rvIwsNMAAAAJ
GitHub: https://github.com/MarkMote

---

**Expected salary:** $220,000 (or skip)

**Notice period:** Available immediately

**How did you hear:** LeRobot open-source project

---

**Why HuggingFace + impact:**

I want to work on LeRobot. My PhD was in robotics, focused on making autonomous systems reliable in the real world. I've spent the last four years building production ML systems as a founder. The gap between robot learning research and real-world deployment is something I've thought about for a long time.

HuggingFace's approach - open-source infrastructure that makes state-of-the-art accessible - is the right model. LeRobot can do for robotics what Transformers did for NLP. The recent momentum (SmolVLA, NVIDIA integration, Reachy Mini shipping 3,000 units) shows it's working.

This resonates personally. During my PhD, I helped build the Robotarium - a remotely accessible swarm robotics testbed that let anyone run code on real robots without owning hardware. It's supported 16,000+ experiments and is still running. Same core idea: lower the barrier, let more people contribute.

I bring a rare combination: deep controls/robotics background, production ML experience, and the ability to ship robust systems. I can contribute to both the research direction and the engineering quality of the library.

---

**Project in first 3 months:**

I'd build runtime guardrails for LeRobot policies.

The problem: users are scared to deploy learned policies on real hardware. A policy that converges beautifully in sim can jitter wildly on a real SO-101 or Reachy Mini and burn out a motor. Hardware is expensive, and that fear slows adoption.

The solution isn't to replace end-to-end learning with classical control. It's to add a thin safety layer that lets users train more aggressively, not less. The neural net drives; the guardrail is just the seatbelt.

This is exactly what my PhD was about. I published a tutorial on runtime assurance in IEEE Control Systems, and my thesis work focused on control barrier functions - mathematical tools that let an autonomous system do whatever it wants until it approaches a dangerous state, then minimally intervene to keep it safe. The key property: you don't fight the learned policy, you just clip it at the boundary.

Concretely for LeRobot:
- A lightweight, hardware-agnostic safety filter library (torque limits, velocity bounds, workspace constraints)
- Plug-and-play with existing policy interfaces - minimal code change for users
- Fast inference (CBF-style filters are computationally cheap, no neural net overhead)
- Clear documentation so the community can extend it to new hardware

The goal: users run `lerobot deploy` with confidence that their robot won't destroy itself in the first 10 seconds. That unlocks experimentation.

---

Quantitative Software Engineer: Techniques Engineering
 Position Summary
Two Sigma is a financial sciences company, combining data analysis, invention, and rigorous inquiry to help solve the toughest challenges in investment management, securities, private equity, and venture capital.

Our team of scientists, technologists, and academics looks beyond the traditional to develop creative solutions to some of the world’s most complex economic problems.
We’re seeking an experienced Machine Learning/AI Engineer who is passionate about bridging innovative research with production-level deployment. In this role, you will work closely with researchers, data teams, and platform engineers to transform innovative ideas into scalable, efficient, and robust production systems. You’ll have the opportunity to develop and refine ML workflows and drive best practices across the entire ML lifecycle—from initial prototyping to inference and support.
You will take on the following responsibilities:

    Collaborate with ML researchers to explore model architectures, training methodologies, and experimental objectives
    Translate prototypes into reusable, maintainable, and production-ready code, ensuring research insights scale seamlessly into operation
    Design, implement, and optimize fully automated training pipelines and evaluation workflows
    Optimize models for production—improving efficiency through techniques like quantization, distillation, and intelligent batching
    Continuously assess and fine-tune both research and production workflows, integrating user feedback and automated monitoring systems
    Identify and implement opportunities for process improvements to reduce bottlenecks and improve overall modeler efficiency.
    Stay ahead of industry trends and new technologies, incorporating sophisticated methodologies into production systems
    Provide technical guidance and mentorship to peers, ensuring the team uses new tools and techniques that drive innovation


You should possess the following qualifications:

    BS in Computer Science, Mathematics, Physics, or related technical subject area
    Minimum 1 year of experience required; 7-15 years of experience preferred
    Strong software engineering skills using Python, version control, testing frameworks, and CI/CD practices
    Ability to work across functions and influence technical strategy while balancing research innovation with operational excellence
    A phenomenal teammate that can work efficiently with modeling and engineering partners
    Experience with leading ML frameworks (e.g., PyTorch, TensorFlow, HuggingFace) and familiarity with model serving/deployment tools, distributed systems and data infrastructures
    Experience with the following are preferred but not required:
        Working with LLMs, multimodal models, or time-series forecasting
        ML Ops platforms
        Background in research or a proven understanding of ML theory

You will enjoy the following benefits:

    Core Benefits: Fully paid medical and dental insurance premiums for employees and dependents, competitive 401k match, employer-paid life & disability insurance
    Perks: Onsite gyms with laundry service, wellness activities, casual dress, snacks, game rooms
    Learning: Tuition reimbursement, conference and training sponsorship
    Time Off: Generous vacation and unlimited sick days, competitive paid caregiver leaves
    Hybrid Work Policy: Flexible in-office days with budget for home office setup

The base pay for this role will be between $165,000 and $300,000. This role may also be eligible for other forms of compensation and benefits, such as a discretionary bonus, health, dental and other wellness plans and 401(k) contributions. Discretionary bonus can be a significant portion of total compensation. Actual compensation for successful candidates will be carefully determined based on a number of factors, including their skills, qualifications and experience.



Quantitative Researcher - Experienced Hire
 Position Summary
Two Sigma is a financial sciences company, combining data analysis, invention, and rigorous inquiry to help solve the toughest challenges in investment management, securities, private equity, and venture capital.

Our team of scientists, technologists, and academics looks beyond the traditional to develop creative solutions to some of the world’s most complex economic problems.
We are looking for a quantitative researcher with an excellent background in statistical techniques and data analysis. In this role, you will navigate the full research process and apply a rigorous scientific approach to design sophisticated investment models for trading a variety of global markets.
You will take on the following responsibilities:

    Use a rigorous scientific method to develop sophisticated investment models and shape our insights into how the markets will behave
    Apply quantitative techniques like machine learning to a vast array of datasets
    Create and test complex investment ideas and partner with our engineers to test your theories
    Join our reading circles to stay up to date on the latest research papers in your fields
    Attend academic seminars to learn from thought leaders from top universities
    Share insights from conferences focused on statistics, machine learning, and data science

You should possess the following qualifications:

    Degree in a technical or quantitative disciplines, like statistics, mathematics, physics, electrical engineering, or computer science (all levels welcome, from bachelor’s to doctorate)
    Intermediate skills in at least one programming language  (like C, C++, Java, or Python)
    Experience performing an in-depth research project, examining real-world data
    Ability to think independently and creatively approach data analysis and communicate complex ideas clearly

You will enjoy the following benefits:

    Core Benefits: Fully paid medical and dental insurance premiums for employees and dependents, competitive 401k match, employer-paid life & disability insurance
    Perks: Onsite gyms with laundry service, wellness activities, casual dress, snacks, game rooms
    Learning: Tuition reimbursement, conference and training sponsorship
    Time Off: Generous vacation and unlimited sick days, competitive paid caregiver leaves
    Hybrid Work Policy: Flexible in-office days with budget for home office setup

The base pay for this role will be between $165,000 and $325,000. This role may also be eligible for other forms of compensation and benefits, such as a discretionary bonus, health, dental and other wellness plans and 401(k) contributions. Discretionary bonus can be a significant portion of total compensation. Actual compensation for successful candidates will be carefully determined based on a number of factors, including their skills, qualifications and experience.
