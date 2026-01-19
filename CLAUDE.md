# Job Search CRM - Claude Instructions

## What This Is
Local CRM and planner for Mark's job search. We manage outreach, research companies, prep for interviews, and build tools only as needed.

## Current Status
- **Date context:** January 2026
- **Target start:** April 2026
- **Wave 1:** NYC-only companies (48 targets in tracker.csv)
- **Personal runway:** Through end of April 

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
Three positioning strategies (will have actual resume docs):
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
├── ref/                   # Claude's memory bank (see README.md inside)
│   ├── mark_profile.md    # Background, timeline, credentials, narrative hooks
│   ├── strategic_context.md # Decision framework, priorities, situational factors
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
    │   └── {company}/
    │       ├── {company}.md    # Structured research
    │       ├── full_context.md # Raw research dump
    │       └── outreach.md     # Contacts, messages, status
    └── 03_ACTIVE/         # Active conversations
```

## What to Read When

**Interview prep / "how do I answer X":**
1. `story-bank/q&a.md` — Check if already answered
2. `ref/mark_profile.md` — Background, timeline, narrative hooks
3. `ref/roostr/roostr.md` — Current company context
4. `ref/pytheia/pytheia.md` or `full_context.md` — Previous company
5. `ref/strategic_context.md` — Why this search, what he wants

**Drafting outreach:**
1. `ref/communication_principles.md` — Voice and tone
2. `ref/outreach_template.md` — Message structure
3. `ref/mark_profile.md` — What to emphasize
4. `company-intel/{company}/` — Company-specific context

**Evaluating an opportunity:**
1. `ref/strategic_context.md` — Decision framework, priorities
2. `ref/inbound_policy.md` — Scoring criteria
3. `ref/mark_profile.md` — Fit with background

**Technical deep dives (system design interviews, etc.):**
1. `ref/roostr/roostr_full_tech_documentation.md` — LLM systems, agentic architecture
2. `ref/pytheia/full_context.md` — CV/robotics systems, Argus architecture

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
