# Pytheia — Full Context

**Company:** Pytheia Corporation
**Founded:** August 23, 2021
**Shut Down:** ~Mid 2024 (after ~2.5 years)
**Investment:** $20k (Pioneer, 2% equity)
**Peak Revenue:** $300k ARR (pricing optimization phase)
**Location:** Atlanta, GA → SF (briefly for Pioneer) 

---

## 1) Founding Team

Three co-founders from the same Georgia Tech robotics lab. Met ~2018, started discussing startups ~late 2019, moved in together January 2021, so that they could run a company out of their appartment. 

### Mark Mote — CEO
- PhD Robotics, MS Aerospace Engineering (Georgia Tech)
- Thesis: optimization for spacecraft controls
- 800+ citations at the time
- Research/internships: Stanford, MIT Lincoln Lab (x2), NASA JPL, AFRL, KAUST, ISAE-ENSMA
- Founding member of the Robotarium (open-access multi-robot research lab)
- Role at Pytheia: Generalist, pitching, customer-facing materials, frontend, high level design, come coding, some builing. 

### Matthew Abate
- PhD Robotics, MS Computer Engineering, MS Electrical Engineering (Georgia Tech)
- Research: applied mathematics, efficient computational prediction methods
- Role at Pytheia: Math/AI, some sales
- Quote from Mark: "Matt understands math more deeply than anyone I've ever met"

### Ben Mains
- MS Electrical and Computer Engineering (Georgia Tech)
- Background: software development, distributed systems scheduling
- Industry: Yamaha (perception for autonomous marine vehicles), General Atomics, Inria, Raytheon
- Role at Pytheia: Software development
- Quote from Mark: "Ben understands software more deeply than anyone I've ever met"

**Team Dynamic:** "We're not just co-founders, we're friends. We're extremely compatible, get along, and complement each other's deficiencies in a way that makes us exponentially stronger than the sum of our parts."

Current state: 
- Still friends, coincidentally we all ended up in NYC together afterwards 
- Ben and mark particularly good relationship: when I flew to the country of georgia to have a small wedding ceremony last summer (2025) ben was one of two people i brought to come with me 

---

## 2) Company Timeline & Pivots

### Phase A: Shared Perception for Autonomous Vehicles (Aug 2021 – Summer 2022)

**Core Idea:** Use traffic cameras and V2X (vehicle-to-everything) to provide shared perception for self-driving cars. Instead of each car solving perception independently with onboard sensors, cars and traffic cameras would share information to build a common world model.

**Tagline:** "Shared Perception for Automated Driving"

**The Insight:**
- All self-driving cars are fundamentally trying to understand the same world
- Mounted traffic cameras are highly undervalued — one camera can cover dozens of cars
- Current approach (adding more onboard sensors) is costly and has diminishing returns
- "It's like Wikipedia only letting you see the articles you have personally authored"
- esseantually a real time semantic search engine

**Pre-AV Ideas (Aug-Dec 2021):**
- Marine mapping
- Parking lot mapping
- Pothole mapping
- Pitched a contract for marine runtime assurance (late 2019)

**Technical Work:**
- **Core output:** Find position and speed of cars, provide real-time info on dynamic objects (vehicles, pedestrians, bicycles)
- **Delivery:** Common world model shared to vehicles via cell network
- **Data sources:** Traffic cameras + vehicle telemetry
- Proof-of-concept using Georgia 511 traffic camera streams (https://511ga.org/)
- Got API access to 3500 PTZ cameras in Georgia, working on 1500 VDS highway cameras
- Pilot with Curiosity Lab at Peachtree Corners, GA (smart city AV testbed, ~1.5 mile stretch with continuous camera coverage)
- Partnership with OVHcloud for cloud compute
- Filing patent with partnered law firm (Goodwin Procter)
- Enabling tech mentioned: AWS Wavelength for low-latency edge computing

**Technical Challenge Discovered:**
- "Tested latency (it is too high)" — latency was a blocking issue with existing traffic camera infrastructure

**Customer Discovery:**
- ~30 customer interviews with OEMs, Tier 1 suppliers, DOTs
- Talked to Ford, Waymo, Mercedes, Aptiv, Panasonic, Porsche
- OEMs expressed "urgent need" for testing and development tools

**Why It Stalled:**
1. **Long sales cycles:** OEMs are highly risk-averse with 3-5 year development cycles
2. **Red tape:** Using public traffic cameras involves government coordination
3. **High technical requirements:** MVP needed to be very sophisticated
4. **Trust gap:** Hard to get OEMs to trust external perception

**YC Applications:** W22, S22 — rejected both times

---

### Phase B: Robotics Perception Software (Summer 2022 – Early 2023)

**Pivot Rationale:** Same core technology (external/shared camera-based perception), but targeting robotics companies instead of automotive OEMs. Faster sales cycles, less risk aversion, immediate integration ability.

**Tagline:** "Off-the-shelf perception software for robots"

**The Insight:**
- Thousands of robotics companies suffering from the same perception problem
- Perception is "the biggest bottleneck in the development process"
- Most solutions require specialized hardware (Optitrack, Vicon with retroreflective markers) or are onboard-only
- External cameras can provide: better reliability (multiple perspectives), better accuracy (fixed cameras don't need localization), lower cost (one sensor serves multiple robots)

**Technical Approach:**
- Software uses camera feeds to generate a live map of robot's environment
- Tracks locations of people, vehicles, objects of interest
- **Key differentiator:** Interfaces with external (offboard) cameras, not just onboard
- Frame rate and resolution agnostic — works with virtually any camera
- **Advantages of external cameras:**
  - Greater reliability (multiple visual perspectives, can see outside robot's line-of-sight)
  - Greater accuracy (fixed cameras don't need continuous localization)
  - Lower cost (one offboard sensor serves multiple robots, less onboard compute/power)

**Competitors Identified:**
- **Optitrack, Vicon:** External vision-based perception, but require retroreflective markers — "perception for lab environments, not real-world"
- **Mobileye:** Onboard sensor suite for automotive (11 cameras + sensors per vehicle)
- **Tangram Vision, Algolux, SLAMCore:** Onboard perception for robotics with multiple sensors

**Customer Discovery:**
- Talking with potential robotics customers
- Continued work with Peachtree Corners smart city testbed

**Other Ideas Considered (from YC W23 app):**
1. Autonomous shuttles with full external camera coverage along specialized routes
2. "App store for robotics software" — marketplace between free solutions (ROS/GitHub) and enterprise software
3. "Simulink for robotics" — low-code toolkit that auto-generates C++/Python from high-level specs

**Why It Stalled:**
- Timing still felt early — market not large enough yet
- Similar challenges with enterprise sales
- Robotics companies building their own solutions

**YC Application:** W23 — rejected

---

### Phase C: Brick-and-Mortar Management / Restaurant AI (Early 2023 – Summer 2023)

**Pivot Rationale:** Discovered that "robotics-grade perception" could solve problems in retail/restaurant management that traditional computer vision couldn't. Bigger market than robotics. Found a design partner through a serial restaurant owner.

**Tagline:** "Vision-based AI for brick-and-mortar management"

**The Insight:**
- Traditional CV solutions only provide 2D image-frame information (pixels in camera frame)
- Spatial perception (3D, real-world coordinates) enables: knowing where things are located, combining multiple cameras into single representation, calculating real-world metrics like walking/line speeds
- Brick-and-mortar businesses failed to leverage automation because so much relies on observing physical space
- "Ease-of-use is very important for adoption, particularly in restaurants"
- Called this "robotics-grade perception" applied to non-robotics use cases

**Technical Work:**
- **Core perception engine:** Tracks objects in 3D space, fuses multiple video feeds in "a fraction of a second"
- **Natural language interface:** Users communicate via text message (SMS) using natural language prompts to query the system
- **Live visualizer:** Map of the floor showing tracked objects
- **Key technical achievement:** Combines multiple camera feeds into single 3D representation of the environment
- Works with ANY existing CCTV camera — no specialized hardware required
- Uses LLMs to process the spatial data and generate insights
- Had a temporary employee who wrote some code (IP paperwork completed)

**Competitors Identified:**
- **Verkada:** Cloud-based CV, security focus, fully integrated system
- **SpotAI:** Cloud-based CV, wider analytics than Verkada but still limited to 2D image frame
- **VergeSense, Density:** Dedicated spatial analytics but require specialized hardware

**Key Differentiator:** Working in spatial frame (3D) vs image frame (2D) enables broader analytics like real-world walking speeds, line speeds, while competitors limited to what you can measure in pixels

**Customer Discovery:**
- Design partners in healthcare, robotics, and restaurant management
- Narrowed to fast-casual restaurants as biggest pain point
- Live pilot with a fast-casual restaurant design partner
- Letter of Intent from design partner
- Serial restaurant owner provided access to 5 camera streams from one of his restaurants

**Use Cases Explored:**
- Automated alerts (e.g., when registers need attendance)
- Performance insights (average wait times, floor sweeping frequency, customer aggregation patterns)
- Customer forecasting for ingredients/staffing

**Accelerator:** Pioneer (3 months, Feb-May 2023, $20k investment for 2% equity)

**Why It Stalled:**
- Scaling difficult due to hardware differences across locations
- Diversity of customer needs
- "Marginal success" — some traction but not enough

**YC Application:** S23 — rejected

---

### Phase D: Pricing Optimization for Franchises (July 2023 – Oct 2023)

**Pivot Rationale:** Found the idea while working with a private equity firm. Their pricing process was "mostly manual, more reliant on guesswork than data." Hired their point of contact (Jordan) as advisor.

**Tagline:** "AI Pricing Co-Pilot for Franchise Businesses"

**The Insight:**
- Pricing for franchises is location-dependent and complex
- Nobody doing this at scale because getting the data wasn't possible without LLMs
- "Data is key and Agents work exceptionally well for getting it when given enough focus and context"
- Every location is unique, but uniqueness can be discovered through data

**Technical Work:**
- **AI webscraper:** LLM agents that get franchise prices from web given a brand's URL
- **Challenge solved:** "Getting the data was not possible without LLMs" — websites have different locations, offerings, structures. Need something intelligent enough to understand context.
- **Geographic pricing models:** ML model predicts optimal prices at any US location and forecasts price trends over time
- **Demo dashboard** for visualizing recommendations
- **MVP delivery:** Auto-generated monthly email reports with recommended prices
- Developed "strong IP around agent-based web-scraping" — considered productizing directly as separate product

**Technical Insight:**
- "2 PhD's in models and optimization — if you can control a robot you can control a price system"
- Pricing technique closely tied to PhD work on optimization

**Team Addition:** Jordan — Director of Strategy at L5 Capital Partners (their customer), joined as part-time sales/advisory

**Customer Discovery:**
- Talks with Buxton (aggregator/site placement tool)
- Talks with Kalibrate (business intelligence platform)
- ~10 potential customers: corporate brands and multi-unit PE franchisees
- Target: $10-30M revenue franchise businesses

**First Revenue (October 2023):**
- Inbound request for just the data (not the full product)
- Fulfilled request in days, then two more, then two more
- ~$1,500 total, $900 recurring monthly
- "Things changed about three weeks ago" — realized data itself was sellable

**Business Model:**
- Integration fee + $20/store/month
- Target: ~500 PE firms with ~500 store locations each
- 10% penetration = $6M ARR

**Other Ideas Considered:**
- Agent-based web-scraping as a service (productize the IP directly)
- Data marketplace — buy/sell data platform

**Why It Pivoted:**
- "Discovered a bigger opportunity" — while selling pricing data, found that the inventory/demand forecasting problem was larger and stickier
- Pricing itself "wasn't that sticky"

**YC Application:** W24 — rejected

---

### Phase E: Demand Forecasting / Supply Chain AI (Oct 2023 – ~Mid 2024)

**Final Pivot:** From pricing optimization to demand forecasting for manufacturers. Same core tech (LLM agents for web scraping) but different use case.

**Tagline:** "AI for supply chain management"

**The Insight:**
- Tier-1 vehicle suppliers need to plan inventory months in advance
- Poor visibility into downstream demand leads to over/underproduction
- Problem worse since COVID
- "If you can control a robot you can control a price system" (transfer from PhD work)

**Technical Work:**

*Two-Agent Architecture:*
1. **Data sourcing agent:** Writes web scraper executables, maintains infrastructure around the data produced
2. **Customer-facing agent:** Assistant akin to code interpreter, with access to higher-level primitives specific to the problem domain and dataset

*Stack:*
- **Frontend:** Next.js, TypeScript, Tailwind CSS
- **Backend:** FastAPI
- **Data viz:** Apache Superset
- **LLM models:** GPT-3.5-turbo-16k, GPT-3.5-turbo-instruct (primary); experimented with Llama 2 family and Mistral (local models)
- **Agent tooling:** LangChain, ChromaDB, occasionally AutoGPT for robust tool calling
- **Custom tooling:** Internal framework similar to Microsoft's AutoGen, used extensively in data sourcing agent
- All code written by founders

*Product:*
- Online dashboard providing Tier-1 vehicle suppliers with forecasts on downstream sales and inventory levels
- Scrapes dealership listings across US for pricing and inventory data
- Predicts what will sell and be stocked by OEMs and dealerships over coming months
- Provides graphs and tables to understand current supply chain state
- Chat interface for interacting with data (built from start to iterate toward vision)

**Demo URL:** https://garlic-ashen.vercel.app

**Traction:**
- First enterprise customer: **Lippert** (Tier-1 RV parts supplier)
- $25k MRR by Nov 2023 (from Lippert)
- 3 customers total: $25k/mo from Lippert + $1k/mo combined from 2 pricing data customers
- Validated need with Yamaha (confirmed they had the problem)

**Timeline:**
- Nov 2023: Got enterprise customer
- Dec 2023: Built dashboard
- Jan 2024: Released dashboard
- Feb 2024: Hoping for second enterprise sale

**Go-to-Market:**
- RVs → Marine → Other Recreational Vehicles → Auto
- Ben had connections in Marine from Yamaha experience
- Already relatively well-connected in Marine industry

**Product Roadmap (planned):**
- Better demand visualizations (what's selling, where)
- Alerts feed — Twitter-style feed with AI-generated reports on day-to-day changes
- Automated reports
- Build up chat interface
- Long-term: Integrate user supply data to automate production decisions

**Future Vision:**
"Imagine Perplexity or ChatGPT, but with the web's information already cached, structured, and analyzed. It could act as a personal analyst, or produce a personalized McKinsey-style report based on your prompts."

**Accelerator Application:** Betaworks AI Camp W24 — outcome unknown

**Revenue Peak:** This phase achieved highest traction ($25k MRR enterprise)

**Why It Ended:**
[Question for Mark: What happened? Why did the company shut down despite having paying customers?]

---

## 3) Technical Capabilities Built

### Perception Engine (Phases A-C)

**What it did:**
- Real-time 3D multi-camera perception from any camera
- Object tracking in 3D space (position and velocity)
- Video feed fusion in "a fraction of a second"
- Works with any camera (frame rate and resolution agnostic)
- Natural language interface (SMS-based) for queries
- Live visualizer showing map with tracked objects

**Key technical achievements:**
- Combines multiple camera feeds into single 3D spatial representation
- Works in "spatial frame" (real-world coordinates) not "image frame" (pixels)
- No specialized hardware required — works with existing CCTV cameras
- Can calculate real-world metrics (walking speeds, line speeds) that 2D competitors cannot

**Differentiators vs competition:**
- vs Verkada/SpotAI: They work in 2D image frame, limited analytics
- vs VergeSense/Density: They require specialized hardware
- vs Optitrack/Vicon: They require retroreflective markers (lab only)

**Demo:** https://www.youtube.com/@PytheiaAI
**Video example:** https://www.youtube.com/watch?v=Wdzhru0Y5f0

Mark's assessment: "To this day I've never seen anything like it."

### Data/AI Platform (Phases D-E)

**What it did:**
- LLM agent-based web scraping at scale
- Collects pricing data from franchise websites given just a URL
- Collects inventory/listings data from dealerships across US
- Geographic demand modeling (predict optimal prices at any US location)
- Forecasts price/inventory trends over time
- Interactive dashboard with chat interface

**Agent architecture:**
- Data sourcing agent: Writes web scraper executables, maintains data infrastructure
- Customer-facing agent: Code-interpreter style assistant with domain-specific primitives

**Stack:**
- Next.js + TypeScript + Tailwind (frontend)
- FastAPI (backend)
- Apache Superset (data viz)
- GPT-3.5-turbo models, LangChain, ChromaDB
- Custom AutoGen-like framework for agents

**Key technical achievement:**
- Solved data collection problem that "was not possible without LLMs" — handling diverse website structures, locations, offerings

**Demo URL:** https://garlic-ashen.vercel.app

---

## 4) What Was Actually Impressive

### The 3D Perception System
Mark's assessment: "As part of my last startup, we built a software package to do real-time 3D multi-camera perception from any camera. We didn't have a lot of luck selling it, but to this day I've never seen anything like it."

This is referenced as one of his most impressive technical achievements, separate from academic work.

### The Bootstrap to $300k ARR
With only $20k investment (Pioneer), reached $300k ARR on the pricing optimization/data product. This demonstrates:
- Ability to find paying customers
- Capital efficiency
- Willingness to pivot to what sells

---

## 5) Lessons Learned

### On Pivoting
- "Make something people want" (YC motto) only covers supply-side economics
- "You also have to make something you want"
- Pytheia pivoted to profitable-but-less-fulfilling work

### On Market Timing
- "5 years ago impossible, 5 years from now everyone would do it" (on shared perception)
- Some ideas are right but early
- Robotics market timing felt "too early to hit a large enough market"

### On Enterprise Sales
- OEMs have long development cycles (3-5 years)
- Trust is critical — "biggest weakness is establishing trust and credibility"
- "Getting in the door with a small sell" builds trust incrementally
- "Iteration speed, engagement, and feedback is important" (from Pioneer)

### On Technical Differentiation
- "Better software, not just new hardware"
- "External cameras serving multiple robots, not multiple onboard sensors serving each robot"
- Working in spatial frame (3D) vs image frame (2D) enables broader analytics

### On Team
- "We complement each other's deficiencies in a way that makes us exponentially stronger than the sum of our parts"
- "We've lived, studied, and worked together"
- All technical founders who also do sales

---

## 6) Accelerator/Application History

| Program | Batch | Idea | Result |
|---------|-------|------|--------|
| YC | W22 | Shared perception for AVs | Rejected |
| YC | S22 | Shared perception for AVs | Rejected |
| YC | W23 | Robotics perception software | Rejected |
| Pioneer | Spring 2023 | Brick-and-mortar AI | Accepted ($20k, 2%) |
| YC | S23 | Brick-and-mortar AI | Rejected |
| YC | W24 | Pricing optimization | Rejected |
| AI Grant | W24 | Pricing optimization | Unknown |
| Betaworks AI Camp | W24 | Demand forecasting | Unknown |

---

## 7) Co-Founders After Pytheia

**Current state (per Mark):**
- Still friends
- Coincidentally all ended up in NYC afterwards
- Ben and Mark particularly close: When Mark flew to the country of Georgia for a small wedding ceremony (summer 2025), Ben was one of two people he brought

**Questions remaining:**
- What is Matt doing now?
- What is Ben doing now?
- How did the company wind-down happen?

---

## 8) Narrative Hooks for Job Search

### The Technical Achievement
"Built real-time 3D multi-camera perception system that could fuse any camera feeds. To this day, haven't seen anything like it commercially."

### The Bootstrap Story
"Took $20k investment to $300k ARR through multiple pivots. Learned to find what sells, not just what's technically interesting."

### The PhD-to-Founder Bridge
"Applied spacecraft optimization mathematics to pricing and demand forecasting. Turns out controlling robots and controlling price systems have deep mathematical similarities."

### The Pivot Discipline
"5 pivots in 2.5 years. Each time learned what doesn't work, kept the technical core, found better market fit."

---

## 9) Company Details

**Legal Name:** Pytheia Corporation
**EIN:** 87-2443485
**Incorporation Date:** August 23, 2021
**Address:** 1201 W Peachtree St NW Ste 2625 PMB 39641, Atlanta, GA 30309
**Phone:** 404-590-8193
**Email:** pytheia@pytheia.com

**Equity Structure (as of Pioneer):**
- Mark Mote: 20%
- Matt Abate: 20%
- Ben Mains: 20%
- Pioneer: 2%
- Academic advisor: 1%
- (Remaining: options pool / unallocated)

---

## 10) Demo Links & Evidence

- **3D Perception Demo:** https://www.youtube.com/watch?v=Wdzhru0Y5f0
- **YouTube Channel:** https://www.youtube.com/@PytheiaAI
- **PhD work demo (spacecraft):** https://youtu.be/JQBrW4yLVHk
- **Stanford collaboration (bouncing robots):** https://youtu.be/4kOOn6TPuDI
- **Old website:** https://www.pytheia.com/
