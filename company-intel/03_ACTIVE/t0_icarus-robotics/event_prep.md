# Icarus - Critical Mass Event Prep
**Date:** Wednesday Jan 29, 2026
**Event:** Critical Mass: Continuums @ Newlab, 5-8pm
**Goal:** Natural conversation with Jamie and/or Ethan, learn more, make an impression

---

## Your Relevant Background (what to mention naturally)

**Direct hits:**
- PhD in spacecraft controls + optimization for underactuated systems → their exact domain
- JPL internship: swarm satellites for asteroid exploration → orbital robotics
- AFRL internship: safe spacecraft docking, mixed-integer programming for proximity ops
- Robotarium: safety verification for multi-robot systems → safety-critical control
- Stanford: collision-inclusive trajectory optimization for free-flyers → directly relevant

**Founder angle:**
- 2x founder, know how to ship at seed stage
- Understand the "move fast but don't break the robot" tension

**Don't oversell:**
- Limited direct microgravity experience (but parabolic flight is their next step too)
- ROS2 experience is light (can learn, but don't claim proficiency)

---

## Top questions

Idea: evaluate on vibe + potential of business

Cofounders / general
- What does team look like right now?
- What gaps are you trying to fill? 
- What are biggest risks? 
- Who is paying for the first deployments? How will grow from that? 
	- is the revenue more like contracts or recurring service?
- What hardware are you making in-house? 
- How are you doing perception? what does the stack look like? 
	- “How are you localizing the robot and objects in microgravity. AprilTags, onboard VO, station priors, something else?
- Seems like a lot of different moving parts with government and different entities
- how are you hoping to grow the team over the next year? 
- Why not just keep doing teleop forever? Why arent they doing it now? 
- At what point does teleop stop making sense economically for you? 
- Whats the first thing you expect to automate end to end? 
- How do you prevent a learned component from becoming a safety bottleneck? 
-



Other people on team: 
- What do you work on? Whats day to day like? 
- How do you like it? 
- 

See if can figure out, but only ask if not online - help me answer if you know
- Are you building your own


Interesting things - learn more about, generate quesitons
- have a zero-g testbed like the one i worked with at stanford - seems to use acro tags rather than vicap
- looks like they are doing training, using teleoperation and using that data 
- i worked with a lab at stanford that did a lot of research on gripping robots and free fliers. 
- feel like i should ask more about design descisions


## Questions to Ask

**About the tech:**
- How are you handling the state estimation problem in microgravity? (No gravity vector for IMU reference)
- What's the control architecture look like? Model-based, learning-based, hybrid?
- How much of the autonomy roadmap is teleop-first vs. building autonomy in parallel?
- What simulation fidelity do you need before parabolic flight? How well does Isaac Sim capture microgravity dynamics?
- How are you thinking about contact dynamics for grasping in zero-g? (Objects behave very differently)
- What's your approach to failure recovery when the human operator has 2+ second delays?
- How do you validate safety-critical maneuvers when hardware test time is so expensive?

**About the mission:**
- What's the biggest technical risk for JOYRIDE-1?
- How are you thinking about the jump from cargo ops to station maintenance?
- What does the NASA partnership look like day-to-day?

**About the team/stage:**
- What does the engineering team look like right now? (You know ~10 people)
- What's the biggest gap you're trying to fill?
- What does the next 6-12 months look like milestone-wise?
- How do you balance hardware vs software development cycles with such a small team?
- What's the split between ex-industry vs fresh PhD talent on the team?

**About the competitive landscape:**
- How do you think about Gitai's approach? (They're doing similar ISS robotics work)
- What's your take on the in-space service market vs manufacturing? 
- Are you seeing competition from the traditional aerospace primes, or is this still too early for them?

**Genuine curiosity:**
- The bimanual gripper approach is clever - how did you land on that vs. anthropomorphic hands?
- How do you think about collecting microgravity data at scale when flight opportunities are so limited?

---

## Things You Genuinely Want to Learn

1. Is the culture a fit? Seed stage means you're marrying these people.
2. How technical is Jamie day-to-day vs. managing?
3. What's their actual timeline to orbit? (Claims: parabolic early 2026, ISS demo via Voyager)
4. How real is the Voyager/Bishop airlock partnership?
5. What's comp actually look like for early hires? ($100-200k + equity per JD)

---

## Natural Conversation Starters

If approaching Jamie:
> "Hey Jamie - we've been messaging about grabbing time. Figured I'd come see what you're building in person."

If he's busy/presenting:
> Wait until after the presentation. Don't interrupt. Catch him during the social portion.

If approaching Ethan instead:
> "I've been talking with Jamie about joining the team. Wanted to see the presentation and say hi."

If someone asks what you do:
> "I'm a robotics PhD turned founder - did my thesis on spacecraft controls at Georgia Tech. Currently wrapping up a startup and exploring what's next. Space robotics is what I've wanted to work on since undergrad."

**Backup conversation topics (if main ones don't land):**
- The broader deep tech ecosystem in NYC - how has it changed in the last few years?
- Their experience at Newlab - what's the community like for hardware startups?
- The transition from research to product in space robotics (vs terrestrial robotics)
- How NASA partnerships actually work day-to-day for startups
- The talent pipeline - where are they finding people with space robotics experience?

---

## What NOT to Do

- Don't be salesy or pitch yourself hard - you're there to learn
- Don't bring up comp or logistics tonight - too early
- Don't trash talk other space robotics approaches
- Don't pretend to know more about microgravity than you do
- Don't monopolize their time - other people want to talk to them too

---

## Relevant Context to Have Ready

**Their recent milestone:** Completed terrestrial long-distance teleop demo (bimanual cargo bag operations)

**Their next steps:** Parabolic flight campaign early 2026, then 1-year ISS demo (JOYRIDE-1)

**The business case:** $130k/hr astronaut labor, 75% of time on cargo logistics. Huge labor arbitrage even with human-in-loop teleop.

**The embodied AI angle:** Collect microgravity data with human-in-loop → foundational models for orbital robotics. Same thesis as terrestrial robotics but for space.

---

## If They Ask You Questions

**"What do you want to work on?"**
> Controls and safe autonomy - the stuff where you need formal guarantees because you can't afford to break hardware. My PhD was exactly this for spacecraft.

**"Why Icarus?"**
> Honest answer: I've wanted to work in space robotics since undergrad. Did the PhD, went the startup route to collect missing skills. Now looking to get back to the work that originally pulled me in. Icarus is doing exactly what I wanted to exist.

**"What's your timeline?"**
> Wrapping up my current role over the next few weeks. Looking to start something new in March/April.

---

## Other Companies to Connect With

**Kyber Labs** (also on your tracker #60):
- Teleoperation/control for autonomous fleets
- Seed stage, Brooklyn Navy Yard
- Good backup conversation if Icarus is swamped

**Other attendees worth meeting:**
- **Birdstop** (now on tracker #83) - BVLOS autonomous drone systems, 7 FAA waivers, detect-and-avoid tech. Controls/autonomy overlap with your background.
- **Diode Computers** - Likely doing edge computing/robotics
- **Moth Quantum** - Quantum computing, could have interesting control applications
- **CREW Carbon** - Climate tech, may have automation/robotics components

**Conversation approach**: "I'm exploring the deep tech ecosystem in NYC - what are you building?" Natural, shows genuine curiosity.

---

## After the Event

- Send Jamie a brief message: "Good to meet in person. Let me know when works for a longer conversation."
- Update this file with notes from the conversation
- Update tracker with any new info

---

## What to Observe Tonight

**Team dynamics:**
- How do Jamie and Ethan present together? Good partnership or tension?
- How do other team members interact with them? (If any are there)
- Do they seem stressed or confident about their timeline?

**Technical depth:**
- How detailed do they get in the presentation vs staying high-level?
- How do they handle technical questions from the audience?
- Do their answers sound rehearsed or do they go deeper when pushed?

**Culture signals:**
- How do they talk about their work-life balance?
- What's their attitude toward risk-taking vs being careful?
- How do they handle setbacks or challenges when asked?

**Red flags to watch for:**
- Overly optimistic timelines with no acknowledgment of difficulty
- Inability to answer basic technical questions about their approach
- Talking more about fundraising than actual engineering progress
- Team members seeming disengaged or checked out

**Green flags:**
- Honest about what they don't know yet
- Excited to talk technical details
- Clear about their role vs what they still need to figure out
- Good energy and enthusiasm from the whole team

