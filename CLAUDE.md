# Job Search CRM - Claude Instructions

## What This Is
Local CRM and planner for Mark's job search. We manage outreach, research companies, prep for interviews, and build tools only as needed.

## Current Status
- **Date context:** January 2026
- **Target start:** April 2026
- **Wave 1:** NYC-only companies (80+ targets in tracker.csv)
- **Personal runway:** Through end of April

## Week Reference (February 2026)
- **W06:** Mon Feb 2 - Fri Feb 6
- **W07:** Mon Feb 9 - Fri Feb 13
- **W08:** Mon Feb 16 - Fri Feb 20
- **W09:** Mon Feb 23 - Fri Feb 27 

## Key Principles

### Truth-Seeking (Internal)
Maximize truth when advising. Challenge assumptions. Point out weak spots. Don't be optimistic or pessimistic—be accurate. Ask: what do we know, how do we know it, how certain are we.

### Narrative (External)
Outreach and resumes must be true but should sell effectively. Paul Graham style: simple, real, professional but not overly formal.
Help create a compelling story about the candidate that is true and real. Know strengths and how to sell them. 

### Simplicity
Keep complexity low. Only build tools/software when clearly needed. Use existing tools (LinkedIn, Sales Navigator) as makes sense.

## Mark's Background (Quick Reference)
- **Current:** CTO & Co-Founder @ Roostr (AI freight forwarder), NYC
- **Previous:** CEO & Co-Founder @ Pytheia (CV/robotics → LLM SaaS), 2.5 years, $20k investment → $300k ARR
- **PhD:** Georgia Tech, optimization for spacecraft controls, 1,449 citations, h-index 13
- **Research stints:** NASA JPL, MIT Lincoln Lab (x2), Stanford, AFRL, KAUST, ISAE-ENSMA
- **Core expertise:** GNC, control theory, optimization, computer vision, robotics, ML, safe autonomy

## Resume Variants
Three positioning strategies (resume docs in `/latex` folder):
1. **Chief Engineer** - technical leadership, spacecraft/robotics depth
2. **Product Founder** - zero-to-one, product sense, commercial deep tech
3. **Distinguished Academic** - research pedigree, publications, PhD culture fit

## Directory Structure
```
/search
├── CLAUDE.md              # This file
├── scratch.md             # Working notes
├── PLAN/
│   ├── action_plan.md     # Outreach strategy and execution plan
│   └── timeline.md        # Weekly goals and milestones
├── data/
│   ├── tracker.csv        # Master company list with status
│   ├── outreach_queue.csv # Action queue: all messages to send/follow-up
│   ├── early.csv          # Seed/Series A target companies
│   ├── mid.csv            # Series B-D target companies
│   ├── late.csv           # Big tech / late-stage targets
│   └── out.csv            # Outside NYC targets
├── latex/                 # Resume variants (LaTeX source + PDFs)
│   ├── resume/           # Main resume variants
│   └── basis_cover_letter/ # Cover letters and custom materials
├── ref/                   # Claude's memory bank (see README.md inside)
│   ├── mark_profile.md    # Background, timeline, credentials, narrative hooks
│   ├── web_cv.md          # Full CV from markmote.com/resume (publications, talks, awards)
│   ├── strategic_context.md # Decision framework, priorities, situational factors
│   ├── role_preferences.md # Target role types, ideal domain, team preferences
│   ├── inbound_policy.md  # Scoring framework for inbound opportunities
│   ├── communication_principles.md # Voice, tone, outreach style
│   ├── outreach_template.md
│   ├── roostr/            # Roostr deep context
│   │   ├── roostr.md      # Canonical summary (interview-ready)
│   │   └── roostr_full_tech_documentation.md # Technical deep dive
│   ├── pytheia/           # Pytheia deep context
│   │   ├── pytheia.md     # Canonical summary
│   │   └── full_context.md # Full story + technical details
│   └── phd/               # PhD context (needs more content)
│       └── raw.md
├── story-bank/            # Interview prep materials
│   ├── q&a.md             # Common questions + answers (e.g., "why leaving?")
│   ├── stories.md         # STAR-format behavioral stories
│   └── Talking points.md  # Key themes and selling points
└── company-intel/
    ├── 00_pending/        # Not yet researched/prepped
    ├── 01_disqualified/   # Ruled out
    ├── 02_qualified/      # Researched, ready to send or sent
    │   └── t{tier}_{company}/   # e.g., t0_icarus-robotics/
    │       ├── {company}.md     # Structured research
    │       ├── full_context.md  # Raw research dump
    │       └── outreach.md      # Contacts, messages, status
    └── 03_ACTIVE/         # Active conversations
```

## What to Read When

**Interview prep / "how do I answer X":**
1. `story-bank/q&a.md` — Check if already answered
2. `ref/mark_profile.md` — Background, timeline, narrative hooks
3. `ref/web_cv.md` — Full CV with publications, talks, awards (source: markmote.com/resume)
4. `ref/roostr/roostr.md` — Current company context
5. `ref/pytheia/pytheia.md` or `full_context.md` — Previous company
6. `ref/strategic_context.md` — Why this search, what he wants

**Drafting outreach:**
1. `ref/communication_principles.md` — Voice and tone
2. `ref/outreach_template.md` — Message structure
3. `ref/mark_profile.md` — What to emphasize
4. `company-intel/{company}/` — Company-specific context

**Finding company intel files:**
- Check tracker.csv for status (Qualified → `02_qualified/`, Active → `03_ACTIVE/`)
- Folder naming: `t{tier}_{company-name}/` (e.g., `t0_icarus-robotics/`)
- Glob pattern: `company-intel/**/*{company}*.md` (NOT `**/{company}*/**` which misses files)

**Evaluating an opportunity:**
1. `ref/role_preferences.md` — Target role types, ideal domains, team preferences
2. `ref/strategic_context.md` — Decision framework, priorities
3. `ref/inbound_policy.md` — Scoring criteria
4. `ref/mark_profile.md` — Fit with background

**Technical deep dives (system design interviews, etc.):**
1. `ref/roostr/roostr_full_tech_documentation.md` — LLM systems, agentic architecture
2. `ref/pytheia/full_context.md` — CV/robotics systems, Argus architecture
3. `ref/web_cv.md` — Full publication list, research internships, PhD work details

## Outreach Tracking System

Two-file system for managing all outreach:

**1. `data/outreach_queue.csv`** - Centralized action queue
- Use for "what's due today?" queries
- One row per message (initial + follow-ups are separate rows)
- Status: `Queued` → `Sent` → `Done` (or `Pending` for follow-ups awaiting prior outcome)
- Filter by `Scheduled` column to find due actions

**2. `company-intel/.../outreach.md`** - Per-company details
- Full message text (initial + follow-ups)
- Contact info and channel
- Strategy notes (tier, delay rules, warm paths)
- Post-response instructions

**Workflow:**
1. "What's due today?" → Read queue, filter by scheduled date
2. "What do I send?" → Pull message text from that company's outreach.md
3. "I sent it" → Update queue status to `Sent`, add sent date
4. "They responded" → Update queue to `Done`, update outreach.md notes, update tracker.csv status

**When prepping a new company:**
1. Mark adds raw research to `full_context.md`
2. Claude synthesizes into `{company}.md` and drafts `outreach.md`
3. Claude adds rows to `outreach_queue.csv` with scheduled dates

**When Mark shares a job description:**
- Save it to `company-intel/{company}/role.md`
- Include: title, requirements, key skills, and prep notes (what to study/brush up on)
- This builds a reference for interview prep and skill gap analysis

**When Mark applies to a company:**
1. `tracker.csv` → status to "📨 Sent", date applied = today, follow-up = +7 days
2. `company-intel/{company}/` → create folder if needed, update:
   - `role.md` — job description + fit assessment
   - Application questions/answers if any
   - Notes on contact (or "no LinkedIn contact found")
3. `message_draft.md` → mark status as SENT if there was a draft

**Moving companies between status folders:**
- `00_pending` → `02_qualified`: Once researched and outreach drafted
- `02_qualified` → `03_ACTIVE`: Once we get a response (positive or neutral)
- `02_qualified` → `01_disqualified`: If ruled out (bad fit, closed, etc.)
- `03_ACTIVE` → `01_disqualified`: If process ends negatively (rejected, ghosted after follow-ups)
- Also update tracker.csv status when moving folders

## The ref/ Folder
This is Claude's memory bank. Automatically update `ref/` with new information about Mark as it comes up in conversation—experiences, preferences, stories, wins, lessons. This accumulates context for better assistance over time.

## What I Help With
- Research companies before outreach
- Draft cold emails and LinkedIn messages
- Prep for conversations and interviews
- Track status and remind on follow-ups
- Challenge strategy and assumptions
- Build tools when genuinely useful

## Current Phase
Executing Wave 1 outreach. See `PLAN/action_plan.md` for workflow and `PLAN/timeline.md` for weekly goals.

## Important Rules
- Be familiar with communication principles before writing messages
- Any message you write for mark should be added to the top of `message_draft.md` so Mark has a single place to copy/paste from. Message drafts put only in the terminal are not usable on their own. This document is a temporary staging ground for the most recent message. It will likely be wiped clean every few messages so do not bother storing permanent info here.

## Status Change Triggers (Do These Automatically)

**Before drafting or advising:**
- [ ] Check `ref/` for relevant context (preferences, background, stories)

**When drafting any message:**
- [ ] Add to top of `message_draft.md` with date, status (DRAFT), channel

**When message is sent:**
- [ ] `tracker.csv` → status to 📨 Sent, date applied = today
- [ ] `outreach_queue.csv` → update row status if applicable

**When company responds positively:**
- [ ] `tracker.csv` → status to 🟢 Active, add response date, update next step
- [ ] Move folder `02_qualified` → `03_ACTIVE`
- [ ] Update intel file with new contact info and process details
- [ ] Update contact name in tracker if different from original

**When interview is scheduled:**
- [ ] `tracker.csv` → next step = interview type + date
- [ ] Company intel → add interview details, prep notes
- [ ] If technical interview: note prep areas based on JD/process

**When company disqualified:**
- [ ] `tracker.csv` → status to ❌ Disqualified, add reason in notes
- [ ] Move folder → `01_disqualified`

**When process ends (rejected/ghosted):**
- [ ] `tracker.csv` → status to ❌ Closed or 💀 Dead
- [ ] Move folder `03_ACTIVE` → `01_disqualified`
- [ ] Note outcome in intel file for future reference

**When new info about Mark comes up:**
- [ ] Update relevant file in `ref/` (profile, stories, preferences, etc.)
- [ ] This includes: preferences, experiences, wins, lessons, stories, constraints, lifestyle factors

## Interview Scheduling Rules

**Tier 0 (All-stars):** Delay technical interviews until Feb 16+ (calibration complete). These are career-defining—don't interview rusty.

**Tier 1 (Protect):** Delay technical screens 7-14 days if possible. If pushed hard, accept.

**Tier 2 (Calibration):** Schedule normally. Use for practice and rust removal.

**Delay script:** "I'm wrapping up some prior commitments. Would [date] work?"

**Exception:** If any company says "this week or never," take the shot. Don't lose opportunities over scheduling purity. 