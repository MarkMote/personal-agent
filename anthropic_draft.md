# Anthropic Application - Draft Responses

apply here: https://job-boards.greenhouse.io/anthropic/jobs/4981828008

## Why do you want to work at Anthropic? (200-400 words)

My path to AI safety began when I lost a family member in a car accident early in my career, which led me to found a startup focused on safer autonomous vehicles. That experience taught me something fundamental: when we build capable systems, safety must be designed in from the beginning, not bolted on afterward.

For the past decade, I've worked on making intelligent systems safe across domains—from spacecraft to robots to AI. My PhD research focused on runtime assurance: embedding safety principles directly into control systems so they maintain safe behavior even when facing unexpected situations. At MIT Lincoln Lab, I worked on formal verification of neural networks, essentially trying to understand why they make the decisions they do. At Air Force Research Lab, I developed principled approaches to spacecraft autonomy that could guarantee safety properties while still allowing capable behavior.

What drew me to this work wasn't fear of technology, but excitement about its potential combined with respect for its risks. I've seen how transformative intelligent systems can be—robots that enable new scientific discoveries, spacecraft that explore asteroids, automation that solves real logistics problems. But I've also learned that the more capable these systems become, the more crucial it is to understand and shape their behavior.

Working with LLMs over the past few years has been both inspiring and humbling. The capabilities are remarkable, but so are the challenges. The interpretability work I did on smaller neural networks feels like early preparation for the much larger challenge of understanding transformer-based models. The constitutional approaches we used for spacecraft control—embedding principles that guide behavior rather than hard-coding specific responses—feel directly relevant to constitutional AI.

What excites me about Anthropic is the combination of ambition and responsibility. You're not just building powerful AI systems—you're building them to be helpful, honest, and harmless. The focus on interpretability, the systematic approach to alignment research, the commitment to understanding model behavior rather than just improving metrics—this is exactly the approach the field needs.

I want to work at Anthropic because you've made safety research a first-class discipline, not a side project. The goal isn't just to build capable AI, but to build AI we can understand and trust. After spending my career working on safety-critical systems, contributing to that mission feels like the most important work I could do.

This technology has incredible potential to help humanity. Getting it right matters.

---

## Cover Letter / Additional Information

I'm Mark Mote, a Georgia Tech Aerospace/Robotics PhD turned 2x founder with experience building safety-critical systems and production AI. I'm drawn to Anthropic because you've made the interpretability and alignment challenges central to your research mission, not secondary considerations.

My academic background focused on a core question that now feels directly relevant to AI alignment: How do you build systems that behave predictably and safely even when facing situations they weren't explicitly trained for? At Georgia Tech, I developed runtime assurance frameworks—essentially constitutional principles embedded directly into control systems. These weren't hard-coded rules but learned safety constraints that could adapt while maintaining key invariants.

At MIT Lincoln Lab, I worked on understanding why neural networks make specific classification decisions—early mechanistic interpretability work focused on proving properties about model behavior rather than just measuring performance. The goal was always transparency: being able to explain not just what a model decided, but why it decided that way.

The work at Air Force Research Lab on spacecraft autonomy involved a challenge similar to Constitutional AI: how do you encode high-level principles (safety, mission success, efficiency) into a learning system and ensure they're followed even during novel situations? The simple solution that worked was embedding the principles as mathematical constraints during the learning process, rather than trying to patch behavior afterward.

Building production AI systems at two startups taught me the practical side of this challenge. At Pytheia, deploying computer vision systems in uncontrolled environments, the biggest lesson was that robustness comes from understanding failure modes, not just achieving good average-case performance. At Roostr, architecting LLM-based automation for freight operations, we learned that helpful AI systems need to be honest about their limitations and fail gracefully when they encounter edge cases.

What excites me about Anthropic's approach is the systematic focus on understanding model behavior. The constitutional AI methodology resonates strongly with my experience building principled safety systems. Rather than trying to anticipate every possible failure mode, you're building systems that can reason about their own behavior according to embedded principles—exactly the kind of scalable approach that safety-critical systems need.

I'm particularly interested in the intersection of interpretability and reinforcement learning. My background spans classical optimal control (mathematical frameworks for multi-objective optimization) and modern RL techniques, with specific focus on safety constraints. The recent work on understanding how constitutional training affects model internals feels like a natural extension of the formal verification approaches I used for simpler systems.

The mission of building AI that's helpful, honest, and harmless feels both ambitious and necessary. The potential for AI to solve important problems is enormous, but realizing that potential requires getting the safety and alignment pieces right. I'd like to contribute to that work, bringing both the theoretical grounding in safety-critical systems and the practical experience of deploying AI in production environments.

The problems are hard, but they're exactly the kind of problems worth working on.

---

*Draft notes: 
- "Why Anthropic" is now ~370 words (good range)
- Cover letter significantly expanded with technical details
- Added AFRL spacecraft RL+safety work, MITLL neural network verification
- Emphasized RL experience and connection to RLHF
- Maintained authentic voice while adding technical depth
- Can trim if too long, but captures the full safety narrative*


Response 1: Why do you want to work at Anthropic? (Limit: 200-400 words)

My commitment to safety engineering began with a personal tragedy—losing a family member to a car accident early in my career. That experience instilled in me a fundamental engineering philosophy: safety cannot be patched in after deployment; it must be an architectural constraint from the start.

For the past decade, I have applied this philosophy to safety-critical systems, from spacecraft control at the Air Force Research Lab to formal verification at MIT Lincoln Lab. My PhD research focused on runtime assurance: the mathematical guarantee that a system will remain within a "safe envelope" regardless of what the learning-based controller attempts to do.

I see a direct parallel between that work and the challenges facing AI today. We are building systems with immense capability but opaque decision-making processes. The transition from physical constraints (preventing a robot from crashing) to cognitive constraints (preventing a model from deceiving or harming) is the logical next step in my career.

Anthropic stands out to me because you treat alignment as an empirical science rather than a philosophical side project. Your work on Constitutional AI resonates deeply with my background in control theory—it is essentially an attempt to embed high-level "invariants" into the model's policy. Similarly, your focus on mechanistic interpretability mirrors the work I did verifying neural networks at MIT—moving beyond "black box" testing to understand the internal causal structures of the system.

I want to work at Anthropic because I believe the rigorous, engineering-led approach used in aerospace is desperately needed in AI alignment. I want to move from ensuring the physical safety of vehicles to ensuring the cognitive safety of general-purpose intelligence. It is the most consequential engineering challenge of our time, and Anthropic is the only lab tackling it with the necessary mix of urgency and responsibility.
Response 2: Cover Letter / Additional Info

Subject: Mark Mote - Application for [Role Name]

I am an aerospace and robotics PhD turned founder with a decade of experience in safety-critical systems, formal verification, and production AI. I am applying to Anthropic because I see a unique opportunity to apply the rigor of control theory and runtime assurance to the problems of LLM alignment and interpretability.

My background is defined by a single technical thread: how to make autonomous systems robust and predictable in open-ended environments.

    Mapping Control Theory to Alignment: During my PhD at Georgia Tech and my time at the Air Force Research Lab, I worked on runtime assurance for spacecraft. The core challenge was allowing a learning agent to optimize for a mission while strictly bounding its behavior within safety constraints. This is structurally identical to the goals of Constitutional AI. I have deep experience defining mathematical "constitutions" (invariant sets) that override unsafe policy outputs, a perspective I am eager to apply to RLHF and reward modeling.

    Interpretability & Verification: At MIT Lincoln Lab, I worked on the formal verification of neural networks. We focused on proving properties about classification boundaries to understand why a network made a decision, rather than relying solely on test-set accuracy. This experience makes me well-suited for work in mechanistic interpretability, as I am accustomed to analyzing the internal state-space of models rather than treating them as black boxes.

    Production ML Reality: As a founder of two startups (Pytheia and Roostr), I learned the difference between theoretical safety and deployment robustness. Whether deploying computer vision in uncontrolled environments or architecting LLM workflows for logistics, I learned that "helpfulness" breaks down without "honesty"—systems must reliably identify and report their own out-of-distribution states.

After several years of building companies, I am eager to return to deep technical work as an individual contributor. I miss the rigor of research and the challenge of solving unsolved engineering problems.

Anthropic’s culture of "doing the simple thing that works" and prioritizing safety over hype aligns perfectly with my engineering ethos. I believe my background in guaranteeing behavior for physical systems offers a valuable, rigorous perspective to the work of aligning cognitive ones. I would be thrilled to contribute to that mission.