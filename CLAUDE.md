# Job Search CRM - Claude Instructions

## What This Is
Local CRM and planner for Mark's job search. We manage outreach, research companies, prep for interviews, and build tools only as needed.

## Current Status
- **Date context:** January 2026
- **Target start:** March-April 2026
- **Wave 1:** NYC-only companies (48 targets in tracker.csv)
- **Personal runway:** ~2-3 months - could be stretched, rather not 

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
├── action_plan.md         # Outreach strategy and execution plan
├── scratch.md             # Working notes
├── data/
│   └── tracker.csv        # Master company list with status
├── ref/                   # Long-term reference (auto-maintained)
│   ├── mark_profile.md    # Background, strengths, narrative hooks
│   └── outreach_template.md
└── company-intel/
    ├── 00_pending/        # Companies not yet contacted
    │   └── {company}/
    │       ├── {company}.md    # Structured research
    │       ├── full_context.md # Raw research dump
    │       └── outreach.md     # Contacts, messages, status
    └── 01_disqualified/
```

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
Executing Wave 1 outreach. See `action_plan.md` for full workflow.
